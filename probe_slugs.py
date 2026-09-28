#!/usr/bin/env python3
"""Probe FreeLLMAPI with the owner's exact OpenRouter slugs and report who ACTUALLY served
each call (X-Routed-Via), in both the Anthropic and OpenAI request shapes."""
import json, subprocess, sys

KEY = [l.split('=', 1)[1].strip() for l in open('/home/ash/.hermes/.env')
       if l.startswith('FREELLMAPI_API_KEY=')][0]
URL = "http://127.0.0.1:3101"

SLUGS = [
    "qwen/qwen3.8-27b:free",
    "thinkingmachines/inkling:free",
    "nvidia/nemotron-3-ultra-550b-a55b:free",
    "nvidia/nemotron-3.5-lightning:free",
    "nvidia/nemotron-3-super-120b-a12b:free",
    # short forms too - the gateway may only know these
    "qwen3.8-27b", "inkling", "nemotron-3-ultra-550b", "nemotron-3.5-lightning",
    "nemotron-3-super-120b",
]


def post(path, body):
    p = subprocess.run(
        ["curl", "-s", "-D", "-", "-m", "120", URL + path,
         "-H", "content-type: application/json",
         "-H", "x-api-key: " + KEY, "-H", "authorization: Bearer " + KEY,
         "-H", "anthropic-version: 2023-06-01",
         "-d", json.dumps(body)],
        capture_output=True, text=True, timeout=140)
    raw = p.stdout
    head, _, payload = raw.partition("\r\n\r\n")
    if not payload:
        head, _, payload = raw.partition("\n\n")
    routed = ""
    status = ""
    for line in head.splitlines():
        low = line.lower()
        if low.startswith("x-routed-via"):
            routed = line.split(":", 1)[1].strip()
        if low.startswith("x-new-头"):
            pass
        if line.startswith("HTTP/"):
            status = line.split()[1]
    return status, routed, payload


def classify(payload):
    try:
        d = json.loads(payload)
    except Exception:
        return "BADJSON", payload[:80]
    if isinstance(d, dict) and d.get("error"):
        e = d["error"]
        msg = e.get("message", str(e)) if isinstance(e, dict) else str(e)
        return "ERR", msg[:90]
    # anthropic shape
    blocks = d.get("content")
    if isinstance(blocks, list):
        txt = "".join(b.get("text", "") for b in blocks if b.get("type") == "text")
        return "OK", (txt or str(d))[:70]
    # openai shape
    ch = (d.get("choices") or [{}])[0]
    msg = ch.get("message", {}) or {}
    txt = msg.get("content") or ""
    if msg.get("tool_calls"):
        return "OK(tools)", json.dumps(msg["tool_calls"][0].get("function", {}))[:70]
    return "OK", (txt or str(d))[:70]


print("advertised models containing the owner's keywords:")
st, ro, pl = post("/v1/models", {})
try:
    names = sorted({m.get("id", "") for m in json.loads(pl).get("data", [])})
    for n in names:
        low = n.lower()
        if any(k in low for k in ("qwen3.8", "inkling", "nemotron", "thinkingmachines")):
            print("   ", n)
    print("total advertised:", len(names))
except Exception:
    print("  could not parse /v1/models:", pl[:120])

print()
print("%-42s %-8s %-40s %s" % ("asked for", "http", "actually served (X-Routed-Via)", "reply"))
print("-" * 140)
for slug in SLUGS:
    st, ro, pl = post("/v1/chat/completions", {
        "model": slug, "max_tokens": 40,
        "messages": [{"role": "user", "content": "Reply with exactly: SLUG-PROBE-OK"}]})
    kind, det = classify(pl)
    print("%-42s %-8s %-40s %s %s" % (slug, st, (ro or "(none)")[:40], kind, det[:60]))
