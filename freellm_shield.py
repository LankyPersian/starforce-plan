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
# Owner directive 2026-09-29: FreeLLMAPI `auto` is the adaptive default.  Named models remain
# fallbacks, including Nemotron Super, rather than a single brittle hot-path pin. The three
# formerly-head-pinned OpenRouter free ids were MEASURED, not assumed:
#   qwen/qwen3.8-27b:free                54 real calls -> 53 errors (107 shield tries, 0% ok, 429)
#   thinkingmachines/inkling:free        85 shield tries -> 0% ok, 429 in ~0.0s (instant reject)
#   nvidia/nemotron-3.5-lightning:free   51 tries -> 27% ok, 60s median, PROVIDER_DOWN (502)
# They were NOT bad models - they were unreachable routes that still burned ~42 min of wall clock
# and 6% of all attempts from the head of the ladder. They now sit in FLAKY_TIER at the tail: still
# reachable as a fallback, never preferred, and parked on the RELIABLE (longer) schedule so they
# stop re-entering the hot path every window.
# `STRONG_TIER` remains the legacy name used by the concurrency/picker code. It is deliberately
# `auto`, not a named model, so new worker sessions use the healthy provider pool first.
STRONG_TIER = ["auto"]
RELIABLE_TIER = ["nemotron-3-super-120b", "mistral-code", "gpt-oss-120b", "codestral-2508",
                 "mimo-v2.6-flashfree", "deepseek-v4-flashfree", "qwen3.8-flashfree"]
FLAKY_TIER = ["qwen/qwen3.8-27b:free", "thinkingmachines/inkling:free",
              "nvidia/nemotron-3.5-lightning:free", "nvidia/nemotron-3-ultra-550b-a55b:free",
              "nvidia/nemotron-3-super-120b-a12b:free"]
DEFAULT_LADDER = STRONG_TIER + RELIABLE_TIER + FLAKY_TIER
DENY = re.compile(r"^(claude-|gpt-6|gpt-5\.6|.*luna)", re.I)   # never route to subscription look-alikes
REQUEST_BUDGET_S = int(os.environ.get("SHIELD_BUDGET_S", 45 * 60))
TRY_CAP_S = int(os.environ.get("SHIELD_TRY_CAP_S", 240))
# The adaptive default gets a small extra concurrency allowance; the gateway's own global window
# is still respected via gateway_until.
MAX_CONC_STRONG = int(os.environ.get("SHIELD_MAX_CONC_STRONG", 12))
MAX_CONC_RELIABLE = int(os.environ.get("SHIELD_MAX_CONC_RELIABLE", 8))
# A model the gateway says does not exist / is disabled will never recover on its own; parking it
# for minutes would waste one request per recovery window forever, so park it for hours and let
# only the prober re-admit it.
DISABLED_S = int(os.environ.get("SHIELD_DISABLED_S", 4 * 3600))
DISABLED_RE = re.compile(r"is disabled|model_not_found|no such model|invalid model|unknown model", re.I)
KEY = next((l.split("=", 1)[1].strip() for l in open(HOME / ".hermes/.env") if l.startswith("FREELLMAPI_API_KEY=")), "")

# Owner directive 2026-09-29: the OpenRouter strong tier are the best coders but fail more —
# the same model often just WORKS on the 5th or 6th consecutive try. The old policy tripped a
# model's circuit breaker on the FIRST failure, which wasted them. New policy: hammer the same
# model STRIKE_LIMIT times in a row before declaring it truly failed (trip breaker + rotate).
# Deterministic failures do NOT strike — the same payload to the same model fails the same way:
# disabled/unknown model, auth, context-too-long, leaked paid routes.
STRIKE_LIMIT = int(os.environ.get("SHIELD_STRIKES", 6))             # fast failures (429/garbage/empty)
STRIKE_LIMIT_SLOW = int(os.environ.get("SHIELD_STRIKES_SLOW", 3))   # expensive ones (240 s timeouts)
STRIKE_WAIT_MAX_S = int(os.environ.get("SHIELD_STRIKE_WAIT_MAX_S", 120))  # long gateway hint -> rotate, don't wait-strike
STRIKE_BUDGET_S = int(os.environ.get("SHIELD_STRIKE_BUDGET_S", 360))  # per-request cap for striking ONE model
HAMMERABLE = {"RATE_LIMITED", "PROVIDER_DOWN", "TIMEOUT", "NETWORK", "GARBAGE", "EMPTY",
              "BAD_TOOL", "LEAKED_TOOL_XML", "TOOL_NO_BLOCK"}
SLOW_OUTCOMES = {"TIMEOUT", "NETWORK", "PROVIDER_DOWN"}


def parsed_wait(detail):
    """Seconds the gateway says its route needs ("retryAtMs" / "reset ~Nm" / "reset ~Ns"), else None."""
    text = detail or ""
    m = re.search(r'"retryAtMs"\s*:\s*(\d+)', text)
    if m:
        return max(0.0, int(m.group(1)) / 1000.0 - time.time())
    m = re.search(r"reset\S*\s*~\s*(\d+)\s*m", text)
    if m:
        return int(m.group(1)) * 60
    m = re.search(r"reset\S*\s*~\s*(\d+)\s*s", text)
    if m:
        return int(m.group(1))
    return None

lock = threading.Lock()
breakers = {}      # model -> (until_epoch, consecutive_failures)
inflight = {}      # model -> count
sticky = {}        # session key -> model
strikes = {}       # model -> (consecutive transient failures, epoch of last failure) — 09-29 hammer policy
gateway_until = 0  # FreeLLMAPI's own global per-key rate limit window


def db():
    c = sqlite3.connect(DB, timeout=30)
    c.execute("""create table if not exists tries(ts real, req text, session text, model text, effective text,
                 outcome text, detail text, secs real, in_tok int, out_tok int)""")
    return c



def log_try(req, session, model=None, effective=None, outcome=None, detail=None, secs=0, in_tok=0, out_tok=0, logical_request='upstream_attempt', upstream_attempt=1, retry_fallback=0, gateway_wait=0, capacity_wait=0, health_probe=0):
    try:
        with db() as c:
            c.execute(
                """INSERT INTO tries(ts, req, session, model, effective, outcome, detail, secs, in_tok, out_tok, logical_request, upstream_attempt, retry_fallback, gateway_wait, capacity_wait, health_probe)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (time.time(), req, session, model, effective, outcome, (detail or "")[:400], secs, in_tok, out_tok, logical_request, upstream_attempt, retry_fallback, gateway_wait, capacity_wait, health_probe)
            )
    except Exception:
        pass
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
        strikes.pop(model, None)


def cap_for(model):
    return MAX_CONC_STRONG if model in STRONG_TIER else MAX_CONC_RELIABLE


def pick(session, hint, stick=None):
    """Choose a model and reserve a slot. `stick` (model name) means: this caller is hammering
    that model under the strike policy — honour it if it still has capacity, else rotate."""
    now = time.time()
    order = ladder()
    with lock:
        pref = []
        if stick and stick in order and breakers.get(stick, (0, 0))[0] <= now \
                and inflight.get(stick, 0) < cap_for(stick):
            inflight[stick] = inflight.get(stick, 0) + 1
            return stick, 0
        # Coherence first: a session already talking to a model stays on it (it must read its own
        # tool-call history). Only NEW sessions get the adaptive default pushed to the head.
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
    if "gateway_throttle" in b or "gateway_until" in b:
        return "GATEWAY_THROTTLE"
    return "HTTP_" + str(code)
def resilient(path, payload, headers):
    req_id = uuid.uuid4().hex[:10]
    session = session_key(headers, payload)
    hint = payload.get("model")
    started = time.time()
    tries = 0
    hammer = None            # model we are currently striking
    hammer_started = 0.0     # when this request started striking it
    is_retry_fallback = False
    while time.time() - started < REQUEST_BUDGET_S:
        if gateway_until > time.time():
            log_try(req=req_id, session=session, outcome="GATEWAY_THROTTLE", detail=f"until {gateway_until}", secs=0, logical_request="gateway_wait", gateway_wait=gateway_until - time.time())
            time.sleep(min(60, gateway_until - time.time()) + random.uniform(0, 2))
            continue
        model, wait = pick(session, hint, stick=hammer)
        if not model:
            log_try(req=req_id, session=session, model=None, outcome="WAITING", detail=f"all cooling {int(wait)}s", secs=0, logical_request="capacity_wait", capacity_wait=wait, retry_fallback=int(is_retry_fallback))
            time.sleep(wait + random.uniform(0, 3))
            continue
        tries += 1
        t0 = time.time()
        fail = None                      # (outcome, detail) when this try did not validate
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
                    secs=time.time() - t0, in_tok=u.get("input_tokens"), out_tok=u.get("output_tokens"),
                    logical_request="upstream_attempt", upstream_attempt=1, retry_fallback=int(is_retry_fallback))
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
            fail = (outcome, detail)
        except urllib.error.HTTPError as e:
            body = e.read().decode(errors="ignore")[:1000]
            outcome = classify(e.code, body)
            log_try(req=req_id, session=session, model=model, outcome=outcome, detail=body, secs=time.time() - t0,
                    logical_request="upstream_attempt", upstream_attempt=1, retry_fallback=int(is_retry_fallback))
            if e.code == 429 and e.headers.get("X-RateLimit-Remaining") == "0":
                set_gateway_until(int(e.headers.get("X-RateLimit-Reset") or time.time() + 30))
            fail = (outcome, body)
        except Exception as e:
            outcome = "TIMEOUT" if "timed out" in str(e).lower() else "NETWORK"
            log_try(req=req_id, session=session, model=model, outcome=outcome, detail=str(e), secs=time.time() - t0,
                    logical_request="upstream_attempt", upstream_attempt=1, retry_fallback=int(is_retry_fallback))
            fail = (outcome, str(e))
        finally:
            release(model)
        # ---- decide: strike the same model again, or declare it truly failed and rotate -------
        outcome, detail = fail
        pw = parsed_wait(detail)
        if outcome == "CONTEXT_TOO_LONG" or DISABLED_RE.search(detail or ""):
            trip(model, "", outcome)                        # deterministic: park, rotate next
            hammer = None
            time.sleep(0.2)
            continue
        if outcome == "AUTH":
            trip(model, detail or "", outcome)
            hammer = None
            time.sleep(0.2)
            continue
        if outcome == "POLICY_PAID_ROUTE":
            trip(model, detail, outcome)                    # never hammer a paid-route leak
            hammer = None
            time.sleep(0.2)
            continue
        if outcome not in HAMMERABLE:
            trip(model, detail, outcome)
            hammer = None
            time.sleep(min(2 + tries * 0.5, 10) + random.uniform(0, 1))
            continue
        # transient failure on a strikeable outcome: count it globally for this model
        limit = STRIKE_LIMIT_SLOW if outcome in SLOW_OUTCOMES else STRIKE_LIMIT
        with lock:
            c, last = strikes.get(model, (0, 0.0))
            if time.time() - last > 900:
                c = 0                                        # stale window: start fresh
            c += 1
            strikes[model] = (c, time.time())
        if hammer != model:
            hammer, hammer_started = model, time.time()
        exhausted = (c >= limit
                     or time.time() - hammer_started > STRIKE_BUDGET_S
                     or (pw is not None and pw > STRIKE_WAIT_MAX_S))
        if exhausted:
            trip(model, detail, outcome)                    # truly failed after {c} strikes -> park+rotate
            with lock:
                strikes[model] = (0, 0.0)
            hammer = None
            time.sleep(0.2 + random.uniform(0, 0.5))
            continue
        # keep hammering the same model: honour a short gateway hint, else fast jitter
        sleep_s = pw if (pw is not None and pw <= STRIKE_WAIT_MAX_S) else min(1.5 + c * 0.5, 8)
        time.sleep(max(sleep_s, 0.3) + random.uniform(0, 0.7))
        # Mark as retry_fallback if this is a fallback attempt
        is_retry_fallback = True
    return 529, {"type": "error", "error": {"type": "overloaded_error",
                 "message": f"freellm-shield: no valid reply within {REQUEST_BUDGET_S}s after {tries} tries"}}, None

