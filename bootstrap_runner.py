#!/usr/bin/env python3
"""Empirium Studio bootstrap runner — deterministic, resumable, no chat session required.

Runs as a systemd --user service. Executes bootstrap steps P0..P1 of
STARFORCE_AUTONOMOUS_BUILD_PROMPT.md by launching disposable `claude -p` sessions,
and advances ONLY when a deterministic check (not the model's claim) passes.

Failure handling:
  * Claude subscription session limit -> sleep until parsed reset (+2 min), then resume.
  * Other subscription failure        -> retry; after 3 failures on a step, run the same
                                         step on the FREE lane (Claude Code -> FreeLLMAPI ladder).
  * FreeLLMAPI model failure          -> per-model breaker, next model.
  * Everything unavailable            -> sleep (max 10 min) and retry forever. Never exits
                                         with an error; systemd restarts it if it dies.
State: ~/.local/state/empirium-build/bootstrap.json (atomic writes).
"""
import json, os, re, subprocess, sys, time, random, datetime, pathlib, urllib.request

HOME = pathlib.Path.home()
PLAN = HOME / "work/starforce-plan"
PROMPT = PLAN / "STARFORCE_AUTONOMOUS_BUILD_PROMPT.md"
REPO = HOME / "empirium-studio-v2"
STATE_DIR = HOME / ".local/state/empirium-build"
STATE = STATE_DIR / "bootstrap.json"
LOG = STATE_DIR / "bootstrap.log"
FREE_URL = "http://127.0.0.1:3102"  # via freellm-shield
LUNA_MODEL = "gpt-5.6-luna"        # Codex CLI, ChatGPT subscription (planning lane; NOT the API)
FREE_LADDER = ["mistral-code", "codestral-2508", "gpt-oss-120b", "mimo-v2.6-flashfree",
               "deepseek-v4-flashfree", "nemotron-3-super-120b", "auto"]
STEP_TIMEOUT = 90 * 60


def sh(cmd, cwd=None, timeout=1800):
    try:
        r = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True, timeout=timeout)
        return r.returncode, (r.stdout + r.stderr)[-4000:]
    except subprocess.TimeoutExpired:
        return 124, "timeout"


def fresh_heartbeat(max_age=300):
    p = STATE_DIR / "controller/heartbeat.json"
    return p.exists() and time.time() - p.stat().st_mtime < max_age


# (id, instruction, deterministic check -> bool)
STEPS = [
    ("P0.1-facts", "Execute §14 step 1: write .build/FACTS.md in ~/empirium-studio-v2 (create the directory if the repo does not exist yet, as ~/empirium-studio-v2/.build/FACTS.md) from live commands.",
     lambda: (REPO / ".build/FACTS.md").exists() and (REPO / ".build/FACTS.md").stat().st_size > 1500),
    ("P0.2-repo", "Execute §14 step 3: create ~/empirium-studio-v2 from hermes-studio-control, verify baseline install/build/test, record base SHA, then `touch .build/baseline.ok` only if all three succeeded.",
     lambda: (REPO / ".git").exists() and (REPO / ".build/baseline.ok").exists()),
    ("P0.3-controller", "Execute §14 step 4 (controller, verify.sh, release_gate.py, watchdog, janitor, systemd units, §15 fail-safes). Unit tests must live in .build/controller/tests.",
     lambda: sh("python3 -m pytest -q .build/controller/tests", cwd=REPO)[0] == 0),
    ("P1.1-commission", "Execute §14 step 5: pass commissioning proofs C1-C12 against the fixture project and write .build/evidence/commissioning/C*.json with real PIDs/log excerpts.",
     lambda: len(list((REPO / ".build/evidence/commissioning").glob("C*.json"))) >= 12
     and sh("python3 .build/controller/commission_check.py", cwd=REPO)[0] == 0),
    ("P1.2-review", None,  # runner itself obtains the independent review
     lambda: _review_ok()),
    ("P1.3-enable", "Execute §14 step 6: enable empirium-build-controller.service, the watchdog timer and the crontab third-layer check; confirm a fresh heartbeat.",
     lambda: sh("systemctl --user is-active empirium-build-controller")[0] == 0 and fresh_heartbeat()),
    ("P1.4-seed", "Execute §14 step 7: seed F0 work items and the phase plan into the controller and confirm the first F0 attempt was dispatched (controller.py status).",
     lambda: _attempts_total() > 0),
]


def _attempts_total():
    rc, out = sh("python3 .build/controller/controller.py status --json", cwd=REPO)
    try:
        return int(json.loads(out[out.index("{"):]).get("attempts_total", 0)) if rc == 0 else 0
    except Exception:
        return 0


def _review_ok():
    p = REPO / ".build/evidence/commissioning/INDEPENDENT_REVIEW.json"
    try:
        return json.loads(p.read_text()).get("verdict") == "APPROVED"
    except Exception:
        return False


def log(msg):
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    line = f"{datetime.datetime.now(datetime.UTC).isoformat()} {msg}"
    print(line, flush=True)
    with open(LOG, "a") as f:
        f.write(line + "\n")


def load():
    try:
        return json.loads(STATE.read_text())
    except Exception:
        return {"done": [], "fails": {}, "breakers": {}, "sub_cooldown_until": 0, "luna_cooldown_until": 0}


def save(s):
    tmp = STATE.with_suffix(".tmp")
    tmp.write_text(json.dumps(s, indent=1))
    os.replace(tmp, STATE)


def parse_reset(text):
    """Return epoch seconds for 'resets 11pm (UTC)' / 'reset ~10m' style hints, else None."""
    m = re.search(r"reset\S*\s*~\s*(\d+)\s*m", text)
    if m:
        return time.time() + int(m.group(1)) * 60
    m = re.search(r"resets\s+(\d{1,2})(?::(\d{2}))?\s*(am|pm)\s*\(UTC\)", text, re.I)
    if m:
        h = int(m.group(1)) % 12 + (12 if m.group(3).lower() == "pm" else 0)
        now = datetime.datetime.now(datetime.UTC)
        t = now.replace(hour=h, minute=int(m.group(2) or 0), second=0, microsecond=0)
        if t <= now:
            t += datetime.timedelta(days=1)
        return t.timestamp()
    m = re.search(r"try again at\s+(\d{1,2})(?::(\d{2}))?\s*(AM|PM)", text, re.I)
    if m:
        h = int(m.group(1)) % 12 + (12 if m.group(3).lower() == "pm" else 0)
        now = datetime.datetime.now(datetime.UTC)
        t = now.replace(hour=h, minute=int(m.group(2) or 0), second=0, microsecond=0)
        if t <= now:
            t += datetime.timedelta(days=1)
        return t.timestamp()
    return None


def run_luna(task):
    """Codex CLI on the ChatGPT subscription (NOT the API). Primary planning lane.
    Own CODEX_HOME with only the subscription auth symlinked; no API key of any kind is passed,
    so it can never fall onto paid API billing."""
    home = STATE_DIR / "codex-sub"
    home.mkdir(parents=True, exist_ok=True)
    auth = home / "auth.json"
    real = HOME / ".codex" / "auth.json"
    if real.exists() and not auth.exists():
        try:
            auth.symlink_to(real)
        except OSError:
            pass
    env = {k: v for k, v in os.environ.items()
           if k not in ("OPENAI_API_KEY", "ANTHROPIC_API_KEY", "ANTHROPIC_BASE_URL",
                        "ANTHROPIC_AUTH_TOKEN", "CODEX_API_KEY")}
    env["CODEX_HOME"] = str(home)
    env["RUST_LOG"] = "error"
    prompt = (f"You are a disposable bootstrap worker. Read {PROMPT} (§0-§15). Then do exactly this step and nothing else:\n{task}\n"
              f"The step may be partially done by a previous worker: inspect the current state first and continue; do not restart finished work. "
              f"Commit to git after meaningful progress. Do not claim success; a deterministic check decides.")
    cmd = ["codex", "exec", "-m", LUNA_MODEL, "--json", "--skip-git-repo-check",
           "--dangerously-bypass-approvals-and-sandbox", prompt]
    cwd = REPO if REPO.exists() else HOME
    try:
        r = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True,
                           stdin=subprocess.DEVNULL, timeout=STEP_TIMEOUT, start_new_session=True)
    except subprocess.TimeoutExpired:
        return "TIMEOUT", ""
    text = (r.stdout or "") + (r.stderr or "")[-2000:]
    msgs, usage, err = [], None, None
    for line in (r.stdout or "").splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            d = json.loads(line)
        except Exception:
            continue
        if d.get("type") == "item.completed" and (d.get("item") or {}).get("type") == "agent_message":
            msgs.append((d["item"].get("text") or ""))
        elif d.get("type") == "turn.completed":
            usage = d.get("usage") or usage
        elif d.get("type") == "error":
            err = d.get("message") or d.get("error") or d
    if not msgs and not usage:
        return "CRASH", text[-800:]
    limit = re.search(r"usage limit|rate limit|try again at", text, re.I)
    if limit:
        return "LIMIT", text[-800:]
    if err and not msgs:
        return "ERROR", text[-800:]
    return "OK", "\n".join(msgs)[-4000:]


def run_claude(task, lane, model):
    env = {k: v for k, v in os.environ.items() if k not in ("ANTHROPIC_API_KEY", "ANTHROPIC_BASE_URL", "ANTHROPIC_AUTH_TOKEN")}
    if lane == "free":
        key = next(l.split("=", 1)[1].strip() for l in open(HOME / ".hermes/.env") if l.startswith("FREELLMAPI_API_KEY="))
        env.update(ANTHROPIC_BASE_URL=FREE_URL, ANTHROPIC_AUTH_TOKEN=key, ANTHROPIC_API_KEY="",
                   CLAUDE_CONFIG_DIR=str(STATE_DIR / "claude-free"), API_TIMEOUT_MS="3000000",
                   CLAUDE_CODE_MAX_RETRIES="10", ANTHROPIC_DEFAULT_SONNET_MODEL="claude-sonnet-4-5",
                   ANTHROPIC_SMALL_FAST_MODEL="claude-haiku-4-5")
        model = "sonnet"  # shield picks the real free model from its ladder
    prompt = (f"You are a disposable bootstrap worker. Read {PROMPT} (§0-§15). Then do exactly this step and nothing else:\n{task}\n"
              f"The step may be partially done by a previous worker: inspect the current state first and continue; do not restart finished work. "
              f"Commit to git after meaningful progress. Do not claim success; a deterministic check decides.")
    cmd = ["claude", "-p", "--model", model, "--dangerously-skip-permissions", "--output-format", "json", prompt]
    cwd = REPO if REPO.exists() else HOME
    try:
        r = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True, timeout=STEP_TIMEOUT, start_new_session=True)
        out = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-2000:]
    except subprocess.TimeoutExpired:
        return "TIMEOUT", ""
    try:
        j = json.loads(out)
    except Exception:
        return "CRASH", out[-500:]
    text = json.dumps(j)
    if j.get("api_error_status") == 429 or "session limit" in text or "rate_limit" in text:
        return "LIMIT", text
    if j.get("is_error") or not str(j.get("result", "")).strip():
        return "ERROR", text
    return "OK", text


def independent_review():
    """Opus (fallback Sonnet) reviews commissioning evidence; verdict written by THIS runner."""
    task = ("Independently review ~/empirium-studio-v2/.build/evidence/commissioning/ and the controller code. "
            "Check every proof C1-C12 used real processes (real PIDs, real kills, real timestamps), not fixtures claiming success. "
            "Reply with ONLY a JSON object: {\"verdict\":\"APPROVED\"|\"CHANGES_REQUESTED\",\"defects\":[...]}")
    for model in ("opus", "sonnet"):
        status, text = run_claude(task, "sub", model)
        if status == "OK":
            m = re.search(r'\{[^{}]*"verdict"[^{}]*(\[[^\]]*\])?[^{}]*\}', json.loads(text).get("result", ""))
            if m:
                (REPO / ".build/evidence/commissioning").mkdir(parents=True, exist_ok=True)
                v = json.loads(m.group(0)); v["reviewer_model"] = model; v["at"] = time.time()
                (REPO / ".build/evidence/commissioning/INDEPENDENT_REVIEW.json").write_text(json.dumps(v, indent=1))
                if v.get("verdict") != "APPROVED":
                    (REPO / ".build/evidence/commissioning/REVIEW_DEFECTS.md").write_text("\n".join(map(str, v.get("defects", []))))
                return status, text
        if status == "LIMIT":
            return status, text
    return "ERROR", ""


def main():
    log("bootstrap runner start")
    while True:
        s = load()
        pending = [st for st in STEPS if st[0] not in s["done"]]
        # re-validate completed steps cheaply: never trust recorded progress blindly
        for sid, _, check in STEPS:
            if sid in s["done"] and sid in ("P0.3-controller",) and not check():
                s["done"].remove(sid); log(f"{sid} regressed; reopening")
        if not pending:
            log("BOOTSTRAP COMPLETE — controller owns the project. Runner exiting cleanly.")
            (STATE_DIR / "BOOTSTRAP_COMPLETE").write_text(str(time.time()))
            return 0
        sid, task, check = pending[0]
        if check():
            s["done"].append(sid); save(s); log(f"{sid} PASS (check)"); continue
        if sid == "P1.2-review" and (REPO / ".build/evidence/commissioning/REVIEW_DEFECTS.md").exists() \
                and not _review_ok() and s["fails"].get(sid, 0) % 2 == 1:
            # defects found: send commissioning back for rework, then re-review
            task = "Fix the defects in .build/evidence/commissioning/REVIEW_DEFECTS.md, re-run the affected proofs, then delete REVIEW_DEFECTS.md."
            status, text = run_claude(task, "sub", "sonnet"); lane = "sub"
        elif sid == "P1.2-review":
            status, text = independent_review(); lane = "sub"
        else:
            n = s["fails"].get(sid, 0)
            if time.time() < s["sub_cooldown_until"] or n >= 3:
                # subscription cooling down or repeatedly failing -> free lane keeps the step moving
                now = time.time()
                model = next((m for m in FREE_LADDER if s["breakers"].get(m, 0) < now), None)
                if model is None:
                    wake = min([s["sub_cooldown_until"]] + list(s["breakers"].values()))
                    nap = max(30, min(600, wake - now)) + random.uniform(0, 15)
                    log(f"all lanes cooling; sleeping {int(nap)}s"); time.sleep(nap); continue
                status, text = run_claude(task, "free", model); lane = "free"
                if status != "OK":
                    s["breakers"][model] = time.time() + (parse_reset(text) and parse_reset(text) - time.time() or 300)
            else:
                # planning lane = Codex/Luna (ChatGPT subscription); Sonnet is the fallback
                status, text = run_luna(task); lane = "luna"
                if status in ("CRASH", "ERROR", "TIMEOUT", "LIMIT"):
                    log(f"{sid}: luna {status}; falling back to Claude Sonnet")
                    if status == "LIMIT":
                        s["luna_cooldown_until"] = (parse_reset(text) or time.time() + 1800) + 120
                    if time.time() >= s.get("luna_cooldown_until", 0):
                        status, text = run_claude(task, "sub", "sonnet"); lane = "sub"
        if status == "LIMIT" and lane == "sub":
            reset = parse_reset(text) or time.time() + 1800
            s["sub_cooldown_until"] = reset + 120
            log(f"{sid}: subscription limit; sub lane cooling until {datetime.datetime.fromtimestamp(reset, datetime.UTC)}; free lane continues")
        elif status != "OK":
            s["fails"][sid] = s["fails"].get(sid, 0) + 1
            log(f"{sid}: {status} (fail #{s['fails'][sid]})")
            time.sleep(20 + random.uniform(0, 20))
        if check():
            s["done"].append(sid); log(f"{sid} PASS")
        elif status == "OK":
            s["fails"][sid] = s["fails"].get(sid, 0) + 1
            log(f"{sid}: worker finished but check not yet passing (fail #{s['fails'][sid]}); continuing")
        save(s)


if __name__ == "__main__":
    sys.exit(main())
