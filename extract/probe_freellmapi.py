import json, os, time, urllib.request, urllib.error, statistics, sys

KEY = None
with open(os.path.expanduser("~/.hermes/.env")) as f:
    for line in f:
        if line.startswith("FREELLMAPI_API_KEY="):
            KEY = line.strip().split("=", 1)[1]
BASE = "http://127.0.0.1:3101/v1/chat/completions"

MODELS = [
    "auto", "glm-5.3", "glm-5.3-fast", "kimi-k3-fast", "qwen3.6-27b",
    "qwen3.7-flash", "deepseek-v4-flashfree", "gpt-oss-120b",
    "nemotron-3-super-120b", "mistral-code", "gemma-4-26b-a4b",
    "mimo-v2.6-flashfree", "codestral-2508",
]

def call(model, messages, tools=None, timeout=25, max_tokens=64):
    body = {"model": model, "messages": messages, "max_tokens": max_tokens, "temperature": 0}
    if tools:
        body["tools"] = tools
        body["tool_choice"] = "auto"
    data = json.dumps(body).encode()
    req = urllib.request.Request(BASE, data=data, method="POST", headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {KEY}",
    })
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            dt = time.time() - t0
            j = json.loads(raw)
            choice = j.get("choices", [{}])[0]
            msg = choice.get("message", {})
            content = msg.get("content") or ""
            tool_calls = msg.get("tool_calls")
            if not content and not tool_calls:
                return {"ok": False, "err": "empty_response", "latency": dt}
            return {"ok": True, "latency": dt, "content_len": len(content or ""), "tool_calls": bool(tool_calls)}
    except urllib.error.HTTPError as e:
        dt = time.time() - t0
        try:
            body_err = e.read().decode()[:200]
        except Exception:
            body_err = ""
        return {"ok": False, "err": f"http_{e.code}", "detail": body_err, "latency": dt}
    except Exception as e:
        dt = time.time() - t0
        return {"ok": False, "err": type(e).__name__, "detail": str(e)[:200], "latency": dt}

PROMPT = [{"role": "user", "content": "Reply with exactly the word: PONG"}]

TOOL_DEF = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the weather for a city",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string"}},
            "required": ["city"],
        },
    },
}]
TOOL_PROMPT = [{"role": "user", "content": "What's the weather in Paris? Use the get_weather function."}]

results = {}
for model in MODELS:
    print(f"=== {model} ===", file=sys.stderr)
    trials = []
    for i in range(5):
        r = call(model, PROMPT)
        trials.append(r)
        print(f"  trial{i}: {r}", file=sys.stderr)
    tool_r = call(model, TOOL_PROMPT, tools=TOOL_DEF)
    print(f"  tool_call: {tool_r}", file=sys.stderr)
    oks = [t for t in trials if t.get("ok")]
    latencies = [t["latency"] for t in oks]
    errs = [t.get("err") for t in trials if not t.get("ok")]
    results[model] = {
        "success_rate": len(oks) / len(trials),
        "avg_latency": round(statistics.mean(latencies), 2) if latencies else None,
        "max_latency": round(max(latencies), 2) if latencies else None,
        "errors": errs,
        "tool_call_ok": tool_r.get("ok"),
        "tool_call_used": tool_r.get("tool_calls", False),
        "tool_call_err": tool_r.get("err"),
    }

with open(os.path.expanduser("~/work/starforce-plan/extract/probe_results.json"), "w") as f:
    json.dump(results, f, indent=2)

print(json.dumps(results, indent=2))
