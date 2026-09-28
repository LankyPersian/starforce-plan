#!/usr/bin/env python3
"""Fault-injection tests for freellm_shield against tests/fake_upstream.py.
Requires: fake upstream on :3198, shield on :3197 with SHIELD_STATE=/tmp/shield-fake SHIELD_TRY_CAP_S=5."""
import json, os, sqlite3, threading, time, urllib.request, pathlib

SH = "http://127.0.0.1:3197/v1/messages"
LADDER = pathlib.Path("/tmp/shield-fake/ladder.json")
DOWN = pathlib.Path("/tmp/shield-test/DOWN")
DB = "/tmp/shield-fake/shield.db"
results = []


def call(stream=False, text="hi"):
    body = json.dumps({"model": "claude-sonnet-4-5", "max_tokens": 50, "stream": stream,
                       "messages": [{"role": "user", "content": text}]}).encode()
    req = urllib.request.Request(SH, body, {"content-type": "application/json"})
    t = time.time()
    with urllib.request.urlopen(req, timeout=400) as r:
        return r.status, r.read().decode(), time.time() - t


def rows(since):
    return sqlite3.connect(DB).execute("select model,outcome from tries where ts>?", (since,)).fetchall()


def check(name, cond, info=""):
    results.append((name, cond))
    print(("PASS " if cond else "FAIL ") + name, info)


# 1: every failure type sits in front of the only good model
LADDER.write_text(json.dumps(["m-429", "m-503", "m-empty", "m-loop", "m-hang", "m-flaky", "m-good"]))
t0 = time.time()
code, body, secs = call(text="test1")
outs = rows(t0)
check("T1 non-stream survives 429/503/empty/loop/hang/flaky", code == 200 and "hello from m-good" in body or "hello from m-flaky" in body,
      f"{secs:.1f}s trail={outs}")
check("T1 every failure classified", {o for _, o in outs} >= {"RATE_LIMITED", "PROVIDER_DOWN", "EMPTY", "GARBAGE", "TIMEOUT"}, "")

# 2: tripped models are skipped on the next request (breakers work)
t0 = time.time()
code, body, secs = call(text="test2")
outs = rows(t0)
check("T2 breakers skip known-bad models", code == 200 and len(outs) <= 2 and secs < 10, f"{secs:.1f}s trail={outs}")

# 3: streaming request through failures
LADDER.write_text(json.dumps(["m-503", "m-empty", "m-good"]))
code, body, secs = call(stream=True, text="test3")
check("T3 streaming survives failures, valid SSE", code == 200 and "message_stop" in body and "hello from m-good" in body, f"{secs:.1f}s")

# 4: whole gateway down for 25 s -> request waits and completes, no error to client
LADDER.write_text(json.dumps(["m-good"]))
DOWN.parent.mkdir(parents=True, exist_ok=True)
DOWN.touch()
threading.Timer(25, lambda: DOWN.unlink(missing_ok=True)).start()
t0 = time.time()
code, body, secs = call(text="test4")
check("T4 total outage 25s: request held and completed", code == 200 and "hello" in body and secs >= 20, f"{secs:.1f}s")

# 5: 8 concurrent requests during partial outage all succeed
LADDER.write_text(json.dumps(["m-429", "m-flaky", "m-good"]))
out = []
ths = [threading.Thread(target=lambda i=i: out.append(call(text=f"c{i}"))) for i in range(8)]
[t.start() for t in ths]; [t.join() for t in ths]
check("T5 8 concurrent requests all succeed", len(out) == 8 and all(c == 200 for c, _, _ in out), "")

print(f"\n{sum(c for _, c in results)}/{len(results)} passed")
