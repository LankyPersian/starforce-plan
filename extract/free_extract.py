"""Resilient extraction via FreeLLMAPI: fallback ladder + per-model circuit breaker + retries.
Usage: python3 free_extract.py chunk_03 chunk_04 chunk_05 -> extract/free_<chunk>_partN.md"""
import json, os, re, sys, time, random, urllib.request, urllib.error, pathlib

KEY = next(l.split("=", 1)[1].strip() for l in open(os.path.expanduser("~/.hermes/.env")) if l.startswith("FREELLMAPI_API_KEY="))
URL = "http://127.0.0.1:3101/v1/chat/completions"
LADDER = ["deepseek-v4-flashfree", "gpt-oss-120b", "nemotron-3-super-120b", "mimo-v2.6-flashfree", "glm-5.3", "kimi-k3-fast", "auto"]
breaker = {}  # model -> reopen epoch
BASE = pathlib.Path.home() / "work/starforce-plan"
PIECE = 45000

SYS = ("You extract requirements from a user's chat messages about his AI workforce app (aliases: AI Star Force, AI Staff Force, "
       "AI Taskforce, Empirium Studio, AI Workforce, AI Organization, Personal Software Department). Record ONLY what the user said "
       "or pasted as spec. Output markdown with headings: Names/aliases; Product requirements; Visual/design; Architecture/tech; "
       "Model/LLM routing; Autonomy/orchestration + complaints about past failures; Corrections/reversals (with dates); Rejected approaches; "
       "Open questions. Each bullet prefixed with the [YYYY-MM-DD] of its message. Short verbatim quotes where decisive. Dedupe. No invention.")

def call(model, text):
    body = json.dumps({"model": model, "temperature": 0.1, "max_tokens": 6000,
                       "messages": [{"role": "system", "content": SYS}, {"role": "user", "content": text}]}).encode()
    req = urllib.request.Request(URL, body, {"Content-Type": "application/json", "Authorization": f"Bearer {KEY}"})
    with urllib.request.urlopen(req, timeout=300) as r:
        j = json.loads(r.read())
    out = (j.get("choices") or [{}])[0].get("message", {}).get("content") or ""
    if len(out) < 300:
        raise ValueError("short/empty output")
    return out, j.get("model", model)

def resilient(text):
    for rnd in range(40):  # never give up quickly; rotate models
        now = time.time()
        for m in LADDER:
            if breaker.get(m, 0) > now:
                continue
            try:
                out, eff = call(m, text)
                return out, m, eff
            except urllib.error.HTTPError as e:
                msg = e.read().decode(errors="ignore")[:400]
                mins = re.search(r"reset ~(\d+)m", msg)
                breaker[m] = now + (int(mins.group(1)) * 60 if mins else 120)
                print(f"  {m}: http {e.code} -> breaker {int(breaker[m]-now)}s", flush=True)
            except Exception as e:
                breaker[m] = now + 60
                print(f"  {m}: {type(e).__name__} {str(e)[:80]} -> breaker 60s", flush=True)
        wait = max(15, min(breaker.values()) - time.time()) + random.uniform(0, 10)
        print(f"  all models cooling; sleep {int(wait)}s", flush=True)
        time.sleep(min(wait, 600))
    raise RuntimeError("exhausted")

def pieces(txt):
    blocks = re.split(r"(?=\n\n===== \d{4}-)", txt)
    cur = ""
    for b in blocks:
        if len(b) > PIECE:  # giant paste: slice
            if cur: yield cur; cur = ""
            for i in range(0, len(b), PIECE):
                yield b[i:i + PIECE]
            continue
        if len(cur) + len(b) > PIECE and cur:
            yield cur; cur = ""
        cur += b
    if cur: yield cur

for name in sys.argv[1:]:
    txt = (BASE / "corpus" / f"{name}.md").read_text()
    for i, p in enumerate(pieces(txt)):
        dst = BASE / "extract" / f"free_{name}_part{i:02d}.md"
        if dst.exists() and dst.stat().st_size > 300:
            continue  # resumable
        print(f"{name} part {i} ({len(p)} chars)", flush=True)
        out, m, eff = resilient(p)
        dst.write_text(f"<!-- model={m} effective={eff} -->\n" + out)
        print(f"  done via {m}", flush=True)
print("ALL DONE")
