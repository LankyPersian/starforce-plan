import json
import subprocess

KEY = [l.split('=', 1)[1].strip() for l in open('/home/ash/.hermes/.env')
       if l.startswith('FREELLMAPI_API_KEY=')][0]

STRONG = ["qwen/qwen3.8-27b:free",
          "thinkingmachines/inkling:free",
          "nvidia/nemotron-3-ultra-550b-a55b:free",
          "nvidia/nemotron-3.5-lightning:free",
          "nvidia/nemotron-3-super-120b-a12b:free"]

TOOL = {"name": "Bash", "description": "Run a shell command",
        "input_schema": {"type": "object",
                         "properties": {"command": {"type": "string"}},
                         "required": ["command"]}}

print("=== A) /v1/messages plain text (this is the endpoint the shield uses) ===")
for m in STRONG:
    body = json.dumps({"model": m, "max_tokens": 100,
                       "messages": [{"role": "user", "content": "Reply with exactly: MSG-OK"}]})
    p = subprocess.run(["curl", "-s", "-D", "-", "-m", "90", "http://127.0.0.1:3101/v1/messages",
                        "-H", "content-type: application/json", "-H", "x-api-key: " + KEY,
                        "-H", "anthropic-version: 2023-06-01", "-d", body],
                       capture_output=True, text=True)
    head, _, pl = p.stdout.partition("\r\n\r\n")
    if not pl:
        head, _, pl = p.stdout.partition("\n\n")
    routed, status = "", ""
    for line in head.splitlines():
        if line.lower().startswith("x-routed-via"):
            routed = line.split(":", 1)[1].strip()
        if line.startswith("HTTP/"):
            status = line.split()[1]
    try:
        d = json.loads(pl)
        if d.get("error"):
            res = "ERR " + str(d["error"].get("message", d["error"]))[:70]
        else:
            blocks = d.get("content") or []
            kinds = [b.get("type") for b in blocks]
            txt = "".join(b.get("text", "") for b in blocks if b.get("type") == "text")
            res = "OK %s %r" % (kinds, txt[:40])
    except Exception:
        res = "RAW " + pl[:70].replace("\n", " ")
    print("%-40s %-5s %-42s %s" % (m, status, routed[:42], res))

print()
print("=== B) /v1/messages WITH a tool (does it honour the Anthropic tool protocol?) ===")
for m in STRONG:
    body = json.dumps({"model": m, "max_tokens": 300, "tools": [TOOL],
                       "messages": [{"role": "user",
                                     "content": "Use the Bash tool to run exactly: echo hello. Call the tool, do not explain."}]})
    p = subprocess.run(["curl", "-s", "-D", "-", "-m", "120", "http://127.0.0.1:3101/v1/messages",
                        "-H", "content-type: application/json", "-H", "x-api-key: " + KEY,
                        "-H", "anthropic-version: 2023-06-01", "-d", body],
                       capture_output=True, text=True)
    head, _, pl = p.stdout.partition("\r\n\r\n")
    if not pl:
        head, _, pl = p.stdout.partition("\n\n")
    routed = ""
    for line in head.splitlines():
        if line.lower().startswith("x-routed-via"):
            routed = line.split(":", 1)[1].strip()
    try:
        d = json.loads(pl)
        if d.get("error"):
            res = "ERR " + str(d["error"].get("message", d["error"]))[:70]
        else:
            blocks = d.get("content") or []
            tools = [b for b in blocks if b.get("type") == "tool_use"]
            txt = "".join(b.get("text", "") for b in blocks if b.get("type") == "text")
            if tools:
                good = all(isinstance(t.get("input"), dict) and t.get("input") for t in tools)
                res = "TOOL_USE %s %s" % ("VALID" if good else "BAD_INPUT", str(tools[0].get("input"))[:50])
            elif "<invoke" in txt or "<parameter" in txt or "function_call" in txt:
                res = "LEAKED_MARKUP " + txt[:55].replace("\n", " ")
            else:
                res = "NO_TOOL stop=%s %r" % (d.get("stop_reason"), txt[:45])
    except Exception:
        res = "RAW " + pl[:70].replace("\n", " ")
    print("%-40s %-42s %s" % (m, routed[:42], res))
