#!/usr/bin/env python3
"""FreeLLMAPI resilience shield — request-level "never fail" proxy.

Sits between Claude Code workers (Anthropic /v1/messages API) and FreeLLMAPI.
A single upstream failure must never reach the worker, because past runs showed one
failed request ("freellmapi didn't answer after 3 attempts", stream error events,
hung streams, garbage/repetition output) kills the whole agent session.

Per request:
  * Upstream is called NON-streaming, so the full reply can be validated before the
    worker sees anything; if the worker asked for a stream, SSE is synthesised.
  * Each try has a first-response deadline (fast models) and a hard cap.
  * Failures are classified; the model gets a circuit breaker (parsed "reset ~Nm",
    else escalating backoff); the request is re-sent to the next model in the ladder.
  * Replies are validated: non-empty, no repetition loop, no script-salad garbage,
    tool_use inputs are objects. Bad replies count as failures and are retried.
  * Sticky model per worker session (keeps coherence); switches only on failure.
  * If every model is cooling down, the request WAITS (keeps the socket alive) and
    retries — up to REQUEST_BUDGET_S — instead of erroring.
  * Every try is logged to SQLite for model ranking by the build controller.

Only a request that exhausts the whole budget (default 45 min) returns an error, as
HTTP 529 "overloaded" so Claude Code's own retry logic backs off and retries again.

Stdlib only. Run: python3 freellm_shield.py  (listens 127.0.0.1:3102)
"""
import http.server, json, os, re, socketserver, sqlite3, threading, time, random, urllib.request, urllib.error, pathlib, hashlib, uuid

HOME = pathlib.Path.home()
UP = os.environ.get("SHIELD_UPSTREAM", "http://127.0.0.1:3101")
PORT = int(os.environ.get("SHIELD_PORT", "3102"))
STATE = pathlib.Path(os.environ.get("SHIELD_STATE", HOME / ".local/state/freellm-shield"))
STATE.mkdir(parents=True, exist_ok=True)
DB = STATE / "shield.db"
LADDER_FILE = STATE / "ladder.json"   # editable at runtime; controller re-ranks it
# Owner directive 2026-09-28: maximise use of these OpenRouter free models. They fail far more
# often than the workhorses - that is their nature - so they sit at the HEAD of the ladder
# (the strongest coders when they do answer) and the reliable tier below is the fallback.
STRONG_TIER = ["qwen/qwen3.8-27b:free",
               "thinkingmachines/inkling:free",
               "nvidia/nemotron-3-ultra-550b-a55b:free",
               "nvidia/nemotron-3.5-lightning:free",
               "nvidia/nemotron-3-super-120b-a12b:free"]
RELIABLE_TIER = ["mistral-code", "codestral-2508", "gpt-oss-120b", "mimo-v2.6-flashfree",
                 "deepseek-v4-flashfree", "auto"]
DEFAULT_LADDER = STRONG_TIER + RELIABLE_TIER
DENY = re.compile(r"^(claude-|gpt-6|gpt-5\.6|.*luna)", re.I)   # never route to subscription look-alikes
REQUEST_BUDGET_S = int(os.environ.get("SHIELD_BUDGET_S", 45 * 60))
TRY_CAP_S = int(os.environ.get("SHIELD_TRY_CAP_S", 240))
# Owner wants the strong tier hammered as hard as it will take: allow it more in-flight requests
# than the workhorses. The gateway's own global window is still respected via gateway_until.
MAX_CONC_STRONG = int(os.environ.get("SHIELD_MAX_CONC_STRONG", 3))
MAX_CONC_RELIABLE = int(os.environ.get("SHIELD_MAX_CONC_RELIABLE", 2))
# A model the gateway says does not exist / is disabled will never recover on its own; parking it
# for minutes would waste one request per recovery window forever, so park it for hours and let
# only the prober re-admit it.
DISABLED_S = int(os.environ.get("SHIELD_DISABLED_S", 4 * 3600))
DISABLED_RE = re.compile(r"is disabled|model_not_found|no such model|invalid model|unknown model", re.I)
KEY = next((l.split("=", 1)[1].strip() for l in open(HOME / ".hermes/.env") if l.startswith("FREELLMAPI_API_KEY=")), "")

lock = threading.Lock()
breakers = {}      # model -> (until_epoch, consecutive_failures)
inflight = {}      # model -> count
sticky = {}        # session key -> model
gateway_until = 0  # FreeLLMAPI's own global per-key rate limit window


def db():
    c = sqlite3.connect(DB, timeout=30)
    c.execute("""create table if not exists tries(ts real, req text, session text, model text, effective text,
                 outcome text, detail text, secs real, in_tok int, out_tok int)""")
    return c


def log_try(**kw):
    try:
        with db() as c:
            c.execute("insert into tries values(?,?,?,?,?,?,?,?,?,?)",
                      (time.time(), kw.get("req"), kw.get("session"), kw.get("model"), kw.get("effective"),
                       kw.get("outcome"), (kw.get("detail") or "")[:400], kw.get("secs"), kw.get("in_tok"), kw.get("out_tok")))
    except Exception:
        pass


def ladder():
    try:
        lst = json.loads(LADDER_FILE.read_text())
    except Exception:
        lst = DEFAULT_LADDER
    return [m for m in lst if not DENY.match(m)]


def _wait_for(model, detail, outcome, n):
    """How long to park a model after a failure. The strong tier fails often BY DESIGN (owner
    directive 2026-09-28), so it is parked SHORTER, not longer: a pinned model that is put to sleep
    for 30 minutes on every 429 stops being used at all, which is the opposite of what was asked."""
    text = detail or ""
    # The gateway tells us exactly when the route frees up; honour it instead of guessing.
    m = re.search(r'"retryAtMs"\s*:\s*(\d+)', text)
    if m:
        return max(5.0, int(m.group(1)) / 1000.0 - time.time()) + 5
    m = re.search(r"reset\S*\s*~\s*(\d+)\s*m", text)
    if m:
        return int(m.group(1)) * 60 + 15
    m = re.search(r"reset\S*\s*~\s*(\d+)\s*s", text)
    if m:
        return int(m.group(1)) + 10
    if DISABLED_RE.search(text):
        return float(DISABLED_S)          # never recovers by waiting; park for hours
    strong = model in STRONG_TIER
    if outcome == "RATE_LIMITED":
        return 90 if strong else 300      # flaky-by-nature: retry the route soon
    if outcome in ("GARBAGE", "EMPTY", "BAD_TOOL", "LEAKED_TOOL_XML", "TOOL_NO_BLOCK"):
        return min(30 * n, 300) if strong else min(60 * n, 900)
    if outcome in ("PROVIDER_DOWN", "TIMEOUT", "NETWORK"):
        return min(20 * 2 ** (n - 1), 600) if strong else min(30 * 2 ** (n - 1), 1800)
    return min(30 * 2 ** (n - 1), 1800) if not strong else min(20 * n, 240)


def trip(model, detail, outcome):
    with lock:
        _, n = breakers.get(model, (0, 0))
        n += 1
        breakers[model] = (time.time() + _wait_for(model, detail, outcome, n), n)


def set_gateway_until(t):
    global gateway_until
    gateway_until = max(gateway_until, t)


def heal(model):
    with lock:
        breakers[model] = (0, 0)


def cap_for(model):
    return MAX_CONC_STRONG if model in STRONG_TIER else MAX_CONC_RELIABLE


def pick(session, hint):
    now = time.time()
    order = ladder()
    with lock:
        pref = []
        # Coherence first: a session already talking to a model stays on it (it must read its own
        # tool-call history). Only NEW sessions get the owner-pinned strong tier pushed to the head
        # of the queue (directive 2026-09-28: maximise use of the OpenRouter strong models).
        if session in sticky:
            pref.append(sticky[session])
        pref.extend([m for m in order if m in STRONG_TIER])
        if hint and hint in order and hint not in pref:
            pref.append(hint)
        for m in pref + order:
            if breakers.get(m, (0, 0))[0] <= now and inflight.get(m, 0) < cap_for(m):
                inflight[m] = inflight.get(m, 0) + 1
                return m, 0
        soonest = min([breakers.get(m, (0, 0))[0] for m in order] or [now + 30])
        return None, max(5, min(120, soonest - now))


def release(model):
    with lock:
        inflight[model] = max(0, inflight.get(model, 1) - 1)


CJK = re.compile(r"[\u3040-\u30ff\u3400-\u9fff\uac00-\ud7af]")

# Foreign tool-call markup leaked into the *text* stream. Evidence 2026-09-28: the dominant
# free routes are non-Anthropic models (dots-3-note-preview, deepseek-v4.1-flash) behind a
# gateway that silently swaps the serving model mid-session. A swapped-in model can emit its
# OWN native function-call syntax as prose instead of a real tool_use block:
#     <dots_function_call><invoke name="Bash"><parameter name="command">...
# Claude Code cannot parse that, so the worker session dies mid-task even though the HTTP
# reply was a perfectly valid 200. The old validate() only inspected tool_use blocks that
# were PRESENT, so leaked markup passed as "OK" text -- the failure was invisible here and
# surfaced only as a stuck worker. With no tool_use block and stop_reason=tool_use we must
# also treat the reply as broken.
FOREIGN_TOOL_XML = re.compile(
    r"<\s*(dots_function_call|function_calls?|tool_calls?|invoke|parameter|antml:invoke|antml:parameter)\b",
    re.I)


def validate(resp, want_english=True):
    """Return (ok, outcome, detail)."""
    blocks = resp.get("content") or []
    texts = "".join(b.get("text", "") for b in blocks if b.get("type") == "text")
    tools = [b for b in blocks if b.get("type") == "tool_use"]
    if not texts.strip() and not tools:
        return False, "EMPTY", f"stop={resp.get('stop_reason')}"
    # Leaked native function-call markup in prose == the model cannot speak the tool protocol.
    # Only a FAILURE when the reply carries no usable tool_use block: if a real block is present
    # Claude Code will act on it, and text mentioning e.g. "<invoke>" is then just prose (a worker
    # documenting or testing the parser). dots_function_call is unambiguous -- no legitimate
    # code emits that name except a parser test -- so it is always a failure.
    m = FOREIGN_TOOL_XML.search(texts)
    if m and (not tools or m.group(1).lower().startswith("dots_function_call")):
        return False, "LEAKED_TOOL_XML", f"emitted {m.group(0)!r} as text"
    # Claimed a tool call but produced no parseable block: equally unusable.
    if not tools and resp.get("stop_reason") == "tool_use":
        return False, "TOOL_NO_BLOCK", f"stop_reason=tool_use, no tool_use block; text={texts[:120]!r}"
    for t in tools:
        if not isinstance(t.get("input"), dict) or not t.get("name"):
            return False, "BAD_TOOL", str(t)[:200]
    if not tools and texts.strip():
        # A plain text reply with no tool call is normal in itself, BUT in an agentic session
        # that has already used tools, silently dropping the tool protocol is the failure mode
        # above expressed as prose. Only flag the unambiguous markup cases (done above).
        pass
    if len(texts) > 400:
        tail = texts[-3000:]
        for size in (20, 40, 80):
            chunks = [tail[i:i + size] for i in range(0, len(tail) - size, size)]
            if chunks and max(chunks.count(c) for c in set(chunks)) >= 8:
                return False, "GARBAGE", "repetition loop"
        if want_english and len(CJK.findall(tail)) / max(1, len(tail)) > 0.08:
            return False, "GARBAGE", "script salad"
        words = re.findall(r"[A-Za-z]{2,}", tail)
        if want_english and len(tail) > 1500 and len(words) < len(tail) / 40:
            return False, "GARBAGE", "low word density"
    return True, "OK", ""


def classify(code, body):
    b = (body or "").lower()
    if code == 429 or "rate_limit" in b or "out_of_credits" in b or "rate-limited" in b or "exhausted" in b:
        return "RATE_LIMITED"
    if code in (500, 502, 503, 504, 520, 522, 524, 529) or "no candidate" in b or "unavailable" in b:
        return "PROVIDER_DOWN"
    if code == 400 and ("context" in b or "too long" in b or "maximum" in b):
        return "CONTEXT_TOO_LONG"
    if code in (401, 403):
        return "AUTH"
    return "HTTP_" + str(code)


def upstream(path, payload, model, timeout):
    body = dict(payload)
    body["model"] = model
    body["stream"] = False
    body.pop("thinking", None)          # free models reject/garble Anthropic thinking params
    data = json.dumps(body).encode()
    req = urllib.request.Request(UP + path, data=data, method="POST", headers={
        "content-type": "application/json", "x-api-key": KEY, "authorization": f"Bearer {KEY}",
        "anthropic-version": "2023-06-01", "user-agent": "freellm-shield"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        out = json.loads(r.read())
        out["_routed_via"] = r.headers.get("X-Routed-Via") or ""
        out["_fallback_trail"] = r.headers.get("X-Fallback-Trail") or ""
        rem, reset = r.headers.get("X-RateLimit-Remaining"), r.headers.get("X-RateLimit-Reset")
        if rem is not None and rem.isdigit() and int(rem) <= 3 and reset and reset.isdigit():
            set_gateway_until(int(reset))
        return out


def english(payload):
    s = json.dumps(payload.get("messages", [])[-2:])[-4000:]
    return len(CJK.findall(s)) < 20


def session_key(headers, payload):
    sid = headers.get("x-claude-code-session-id") or headers.get("x-session-id")
    if sid:
        return sid
    first = json.dumps(payload.get("messages", [])[:1])[:2000] + str(payload.get("system", ""))[:500]
    return hashlib.sha1(first.encode()).hexdigest()[:16]


def resilient(path, payload, headers):
    req_id = uuid.uuid4().hex[:10]
    session = session_key(headers, payload)
    hint = payload.get("model")
    started = time.time()
    tries = 0
    while time.time() - started < REQUEST_BUDGET_S:
        if gateway_until > time.time():
            log_try(req=req_id, session=session, outcome="GATEWAY_THROTTLE", detail=f"until {gateway_until}", secs=0)
            time.sleep(min(60, gateway_until - time.time()) + random.uniform(0, 2))
            continue
        model, wait = pick(session, hint)
        if not model:
            log_try(req=req_id, session=session, model=None, outcome="WAITING", detail=f"all cooling {int(wait)}s", secs=0)
            time.sleep(wait + random.uniform(0, 3))
            continue
        tries += 1
        t0 = time.time()
        try:
            resp = upstream(path, payload, model, TRY_CAP_S)
            ok, outcome, detail = validate(resp, english(payload))
            eff = resp.pop("_routed_via", "") or model
            resp.pop("_fallback_trail", None)
            plat = eff
            if "openrouter" in plat.lower() and ":free" not in plat.lower():
                ok, outcome, detail = False, "POLICY_PAID_ROUTE", plat[:200]
            u = resp.get("usage") or {}
            log_try(req=req_id, session=session, model=model, effective=eff, outcome=outcome, detail=detail,
                    secs=time.time() - t0, in_tok=u.get("input_tokens"), out_tok=u.get("output_tokens"))
            if ok:
                heal(model)
                with lock:
                    sticky[session] = model
                resp["model"] = hint or model
                resp.setdefault("id", "msg_" + req_id)
                resp.setdefault("type", "message")
                resp.setdefault("role", "assistant")
                resp["content"] = [b for b in resp.get("content", []) if b.get("type") in ("text", "tool_use")]
                return 200, resp, model
            trip(model, detail, outcome)
        except urllib.error.HTTPError as e:
            body = e.read().decode(errors="ignore")[:1000]
            outcome = classify(e.code, body)
            log_try(req=req_id, session=session, model=model, outcome=outcome, detail=body, secs=time.time() - t0)
            if e.code == 429 and e.headers.get("X-RateLimit-Remaining") == "0":
                set_gateway_until( int(e.headers.get("X-RateLimit-Reset") or time.time() + 30))
            elif outcome == "CONTEXT_TOO_LONG":
                # try models with bigger windows next; don't punish long
                trip(model, "", "CONTEXT_TOO_LONG")
            else:
                trip(model, body, outcome)
        except Exception as e:
            outcome = "TIMEOUT" if "timed out" in str(e).lower() else "NETWORK"
            log_try(req=req_id, session=session, model=model, outcome=outcome, detail=str(e), secs=time.time() - t0)
            trip(model, "", outcome)
        finally:
            release(model)
        with lock:
            if sticky.get(session) == model:
                sticky.pop(session, None)
        time.sleep(min(2 + tries * 0.5, 10) + random.uniform(0, 1))
    return 529, {"type": "error", "error": {"type": "overloaded_error",
                 "message": f"freellm-shield: no valid reply within {REQUEST_BUDGET_S}s after {tries} tries"}}, None


def sse(resp):
    out = []
    def ev(name, data):
        out.append(f"event: {name}\ndata: {json.dumps(data)}\n\n")
    msg = {k: resp[k] for k in ("id", "type", "role", "model") if k in resp}
    msg.update(content=[], stop_reason=None, stop_sequence=None,
               usage={"input_tokens": (resp.get("usage") or {}).get("input_tokens", 0), "output_tokens": 0})
    ev("message_start", {"type": "message_start", "message": msg})
    for i, b in enumerate(resp.get("content", [])):
        if b["type"] == "text":
            ev("content_block_start", {"type": "content_block_start", "index": i, "content_block": {"type": "text", "text": ""}})
            ev("content_block_delta", {"type": "content_block_delta", "index": i, "delta": {"type": "text_delta", "text": b.get("text", "")}})
        else:
            ev("content_block_start", {"type": "content_block_start", "index": i,
                                       "content_block": {"type": "tool_use", "id": b.get("id") or "toolu_" + uuid.uuid4().hex[:20], "name": b["name"], "input": {}}})
            ev("content_block_delta", {"type": "content_block_delta", "index": i,
                                       "delta": {"type": "input_json_delta", "partial_json": json.dumps(b.get("input", {}))}})
        ev("content_block_stop", {"type": "content_block_stop", "index": i})
    ev("message_delta", {"type": "message_delta", "delta": {"stop_reason": resp.get("stop_reason") or "end_turn", "stop_sequence": None},
                         "usage": {"output_tokens": (resp.get("usage") or {}).get("output_tokens", 0)}})
    ev("message_stop", {"type": "message_stop"})
    return "".join(out).encode()


class H(http.server.BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, *a):
        pass

    def _send(self, code, obj, ctype="application/json"):
        data = obj if isinstance(obj, bytes) else json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("content-type", ctype)
        self.send_header("content-length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path.startswith("/health"):
            now = time.time()
            with lock:
                st = {m: max(0, int(breakers.get(m, (0, 0))[0] - now)) for m in ladder()}
            return self._send(200, {"ok": True, "breakers_s": st, "inflight": inflight})
        if self.path.startswith("/v1/models"):
            return self._send(200, {"data": [{"id": m, "type": "model"} for m in ladder()]})
        self._send(404, {"error": "not found"})

    def do_POST(self):
        n = int(self.headers.get("content-length") or 0)
        try:
            payload = json.loads(self.rfile.read(n) or b"{}")
        except Exception:
            return self._send(400, {"type": "error", "error": {"type": "invalid_request_error", "message": "bad json"}})
        path = self.path.split("?")[0]
        if path.endswith("/count_tokens"):
            est = len(json.dumps(payload)) // 4
            return self._send(200, {"input_tokens": est})
        if not path.endswith("/v1/messages"):
            return self._send(404, {"error": "unsupported path"})
        want_stream = bool(payload.get("stream"))
        if want_stream:
            # keep the client's connection alive while we retry upstream
            self.send_response(200)
            self.send_header("content-type", "text/event-stream")
            self.send_header("cache-control", "no-cache")
            self.send_header("connection", "close")
            self.end_headers()
            result = {}
            done = threading.Event()
            def work():
                result["v"] = resilient(path, payload, self.headers)
                done.set()
            threading.Thread(target=work, daemon=True).start()
            try:
                while not done.wait(15):
                    self.wfile.write(b"event: ping\ndata: {\"type\": \"ping\"}\n\n")
                    self.wfile.flush()
                code, resp, _ = result["v"]
                if code == 200:
                    self.wfile.write(sse(resp))
                else:
                    self.wfile.write(f"event: error\ndata: {json.dumps(resp)}\n\n".encode())
                self.wfile.flush()
            except (BrokenPipeError, ConnectionResetError):
                pass
            self.close_connection = True
            return
        code, resp, _ = resilient(path, payload, self.headers)
        self._send(code, resp)


class Server(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True


def prober():
    """Every 5 min, 1 cheap probe per tripped model so recovered models return early."""
    while True:
        time.sleep(300)
        now = time.time()
        for m in ladder():
            if breakers.get(m, (0, 0))[0] > now + 60:
                try:
                    r = upstream("/v1/messages", {"max_tokens": 400, "messages": [{"role": "user", "content": "Reply with the word OK."}]}, m, 60)
                    if validate(r)[0]:
                        heal(m)
                        log_try(req="probe", model=m, outcome="PROBE_OK", secs=0)
                except Exception:
                    pass


if __name__ == "__main__":
    if not LADDER_FILE.exists():
        LADDER_FILE.write_text(json.dumps(DEFAULT_LADDER, indent=1))
    threading.Thread(target=prober, daemon=True).start()
    print(f"freellm-shield on 127.0.0.1:{PORT} -> {UP}", flush=True)
    Server(("127.0.0.1", PORT), H).serve_forever()
