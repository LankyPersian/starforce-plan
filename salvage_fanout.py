#!/usr/bin/env python3
"""F0 salvage inventory fan-out on the FREE lane (mirrors bootstrap_runner's
worker launch so shield/radars/breakers are the only path to free models).

Each worker READS the old repo (~/empirium-studio) and WRITES only to
starforce-plan/salvage/inventory-<slice>.md — never inside either repo's build
path, so it cannot poison the live commissioning round (mixed-SHA rule).
"""
import json
import os
import subprocess
import sys
import threading
import time
from pathlib import Path

HOME = Path.home()
PLAN = HOME / "work" / "starforce-plan"
OLD = HOME / "empirium-studio"
FREE_URL = "http://127.0.0.1:3102"
OUT = PLAN / "salvage"
OUT.mkdir(exist_ok=True)
LOG = OUT / "fanout.log"
FREE_LADDER = ["qwen/qwen3.8-27b:free", "thinkingmachines/inkling:free",
               "nvidia/nemotron-3-ultra-550b-a55b:free", "mockinghair/llama-3.3-70b:free"]
MAX_PAR = int(os.environ.get("SALVAGE_PAR", "6"))

SLICES = {
    "domain-persistence": ["src/server/workforce-postgres.ts", "src/server"],
    "autonomy-kernel": ["src/server/autonomy-kernel.ts"],
    "server-rest": ["src/server"],
    "screens": ["src/screens"],
    "components": ["src/components"],
    "routes-shell": ["src/routes", "src/router.tsx", "src/routeTree.gen.ts", "src/stores"],
    "lib-hooks": ["src/lib", "src/hooks", "src/utils", "src/types"],
    "agent-governance": ["agent", "AI_WORKFORCE_BUILD"],
}

TASK = """You are doing a MECHANICAL INVENTORY of one slice of a legacy codebase so a
senior architect can later decide KEEP/ADAPT/REPLACE per module. Do NOT decide
keep/replace yourself. Do NOT modify any file in the scanned repo.

Repo root: {root}
Your slice: {paths}

Produce a markdown inventory at {out_file} with, for EACH source file in the
slice (skip node_modules, dist, test-results, generated files):

- path
- size (LOC) and language
- one-line purpose (read the code; do not guess from the name)
- public exports / API surface (names + signatures, brief)
- what it imports from inside the repo (coupling) and notable third-party deps
- whether tests exist for it and where
- red flags: hard-coded secrets/paths, global mutable state, direct DB access
  bypassing a layer, `any`-typed public API, dead-looking code, TODO/FIXME

End the file with: `TOTALS:` (files, LOC) and `COUPLING: <other slices this one
touches>`. Keep it factual and dense. No prose padding. Write the file with your
file tools, then reply with one line: `WROTE <path> <n_files> files`.
"""

lock = threading.Lock()


def log(msg):
    with lock:
        line = f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} {msg}"
        with open(LOG, "a") as fh:
            fh.write(line + "\n")
        print(line, flush=True)


def shield_breakers():
    try:
        raw = subprocess.run(["curl", "-s", "-m", "5", FREE_URL + "/_shield/stats"],
                             capture_output=True, text=True).stdout
        return json.loads(raw).get("breakers", {}) if raw else {}
    except Exception:
        return {}


def run_slice(name, paths):
    out_file = OUT / f"inventory-{name}.md"
    if out_file.exists() and out_file.stat().st_size > 800:
        log(f"{name}: already inventoried, skipping")
        return True
    prompt = TASK.format(root=OLD, paths=", ".join(str(OLD / p) for p in paths),
                         out_file=out_file)
    key = None
    for line in open(HOME / ".hermes/.env"):
        if line.startswith("FREELLMAPI_API_KEY="):
            key = line.split("=", 1)[1].strip()
    env = {k: v for k, v in os.environ.items()
           if k not in ("ANTHROPIC_API_KEY", "ANTHROPIC_BASE_URL",
                        "ANTHROPIC_AUTH_TOKEN", "CODEX_API_KEY")}
    for attempt in range(3):
        br = shield_breakers()
        model = next((m for m in FREE_LADDER if br.get(m, 0) < time.time()), FREE_LADDER[0])
        env.update(ANTHROPIC_BASE_URL=FREE_URL, ANTHROPIC_AUTH_TOKEN=key or "x",
                   ANTHROPIC_API_KEY="", ANTHROPIC_MODEL=model,
                   CLAUDE_CODE_EFFORT_LEVEL="low",
                   CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC="1",
                   DISABLE_TELEMETRY="1", DISABLE_AUTOUPDATER="1")
        log(f"{name}: attempt {attempt+1} model={model}")
        r = subprocess.run(["claude", "-p", "--model", model,
                            "--dangerously-skip-permissions", "--output-format", "text",
                            prompt],
                           capture_output=True, text=True, timeout=1500, env=env, cwd=OLD)
        if out_file.exists() and out_file.stat().st_size > 800:
            log(f"{name}: WROTE {out_file} ({out_file.stat().st_size} bytes)")
            return True
        log(f"{name}: no usable file (rc={r.returncode}) {r.stderr[:120] or r.stdout[:120]}")
        time.sleep(20)
    return False


def main():
    names = sys.argv[1:] or list(SLICES)
    log(f"fan-out start par<={MAX_PAR} slices={len(names)}")
    results = {}
    sem = threading.Semaphore(MAX_PAR)

    def go(n):
        with sem:
            results[n] = run_slice(n, SLICES[n])

    ts = [threading.Thread(target=go, args=(n,), daemon=True) for n in names]
    [t.start() for t in ts]
    [t.join() for t in ts]
    ok = [n for n, v in results.items() if v]
    log(f"DONE ok={len(ok)}/{len(names)} failed={sorted(set(results) - set(ok))}")
    return 0 if len(ok) == len(names) else 1


if __name__ == "__main__":
    sys.exit(main())
