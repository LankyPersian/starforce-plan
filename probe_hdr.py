import json
import subprocess

KEY = [l.split('=', 1)[1].strip() for l in open('/home/ash/.hermes/.env')
       if l.startswith('FREELLMAPI_API_KEY=')][0]

MODELS = [
    "nvidia/nemotron-3.5-lightning:free",
    "nvidia/nemotron-3-super-120b-a12b:free",
    "qwen/qwen3.8-27b:free",
    "thinkingmachines/inkling:free",
    "nvidia/nemotron-3-ultra-550b-a55b:free",
]

for m in MODELS:
    body = json.dumps({"model": m, "max_tokens": 60,
                       "messages": [{"role": "user", "content": "Reply with exactly: OK"}]})
    p = subprocess.run(
        ["curl", "-s", "-D", "-", "-m", "60", "http://127.0.0.1:3101/v1/chat/completions",
         "-H", "content-type: application/json", "-H", "x-api-key: " + KEY, "-d", body],
        capture_output=True, text=True)
    head, _, pl = p.stdout.partition("\r\n\r\n")
    if not pl:
        head, _, pl = p.stdout.partition("\n\n")
    routed = ""
    status = ""
    for line in head.splitlines():
        low = line.lower()
        if low.startswith("x-routed-via"):
            routed = line.split(":", 1)[1].strip()
        if line.startswith("HTTP/"):
            status = line.split()[1]
    blocked = ("openrouter" in routed.lower()) and (":free" not in routed.lower())
    verdict = "WOULD BE BLOCKED by POLICY_PAID_ROUTE" if blocked else "passes the paid-route guard"
    print(m)
    print("    http=%s  route=%r" % (status, routed))
    print("    -> " + verdict)
