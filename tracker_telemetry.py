"""Read-only collectors for tracker agent concurrency and project throughput."""
from __future__ import annotations

import json
import os
import re
import sqlite3
import subprocess
import time
from pathlib import Path


AGENT_PATTERNS = (("claude -p", "claude"), ("codex exec", "codex"),
                  ("fixture_claude.py", "claude"), ("fixture_codex.py", "codex"),
                  ("fixture_freellm.py", "freellm"))
BUILD_DB = os.path.expanduser("~/.local/state/empirium-build/build.db")
# Both controllers can own sub-agents: production state and the commissioning fixture.
BUILD_DBS = [os.path.expanduser("~/.local/state/empirium-build/build.db"),
             os.path.expanduser("~/.local/state/empirium-fixture/build.db")]
# Two controllers run live: the production one and the commissioning fixture controller
# (EMPIRIUM_BUILD_STATE=~/.local/state/empirium-fixture). A sub-agent is only "visible"
# if we read the DB of every controller that can own one.
BUILD_DBS = [os.path.expanduser("~/.local/state/empirium-build/build.db"),
             os.path.expanduser("~/.local/state/empirium-fixture/build.db")]
DELEG_LIVE = os.path.expanduser("~/.hermes/cache/delegation/live")
DELEG_STALE_S = 15 * 60


def _env_for_pid(pid: str) -> dict[str, str]:
    """Return only non-secret environment markers used to classify a worker."""
    wanted = {"EMPIRIUM_ATTEMPT_ID", "ANTHROPIC_BASE_URL", "FREELLMAPI_BASE_URL"}
    try:
        values = Path(f"/proc/{pid}/environ").read_bytes().split(b"\0")
    except OSError:
        return {}
    out = {}
    for value in values:
        key, sep, raw = value.partition(b"=")
        if sep and key.decode(errors="ignore") in wanted:
            out[key.decode()] = raw.decode(errors="replace")
    return out


def _model(kind: str, cmd: str) -> str:
    if kind == "claude":
        match = re.search(r"--model\s+(\S+)", cmd)
    else:
        match = re.search(r"(?:^|\s)-m\s+(\S+)", cmd)
    return match.group(1) if match else "default"


def collect_agents(lines: list[str] | None = None, env_for_pid=_env_for_pid) -> list[dict]:
    """Identify live CLI agents and their lane without collecting secrets."""
    if lines is None:
        try:
            result = subprocess.run(
                ["ps", "-eo", "pid=,ppid=,etimes=,args="], capture_output=True, text=True, timeout=10, check=True
            )
            lines = result.stdout.splitlines()
        except Exception:
            return []
    agents = []
    for line in lines:
        fields = line.strip().split(None, 3)
        if len(fields) != 4 or not fields[0].isdigit() or not fields[2].isdigit():
            continue
        pid, ppid, elapsed, command = fields
        kind = next((name for pattern, name in AGENT_PATTERNS if pattern in command), None)
        if not kind:
            continue
        if "--role " in command:      # fixture gateway/shield servers, not a worker session
            continue
        env = env_for_pid(pid)
        base = " ".join((env.get("ANTHROPIC_BASE_URL", ""), env.get("FREELLMAPI_BASE_URL", ""))).lower()
        # free lane = anything pointed at the freellm gateway or the shield (real: 3101/3102,
        # fixture: 3201/3202); everything else is a subscription lane.
        free_tokens = ("3101", "3102", "3201", "3202", "freellm", "shield")
        lane = "free" if any(token in base for token in free_tokens) else "luna" if kind == "codex" else "subscription"
        agents.append({
            "pid": pid,
            "ppid": ppid,
            "runtime_s": int(elapsed),
            "kind": kind,
            "lane": lane,
            "model": _model(kind, command),
            "attempt_id": env.get("EMPIRIUM_ATTEMPT_ID", ""),
            "command": command[:300],
        })
    return sorted(agents, key=lambda agent: int(agent["runtime_s"]), reverse=True)


def _pid_start_fields(stat_text: str) -> str:
    """Field 22 of /proc/[pid]/stat (start ticks) — the same marker the controller uses
    to prove a pid is still the process it recorded, so a recycled pid cannot masquerade."""
    return stat_text.rsplit(")", 1)[1].split()[19]


def collect_db_attempts(db_path: str = BUILD_DB, now: float | None = None) -> list[dict]:
    """Attempts the controller claims are running, verified alive by pid+start marker.

    The CLI scan above misses attempts whose worker is hidden behind a wrapper shell and
    cannot attribute a process to a work item; the attempts table is the controller's own
    authority and /proc proves the claim live.
    """
    if isinstance(db_path, (list, tuple)):
        out_all: list[dict] = []
        seen_pids = set()
        for fp in db_path:
            for a in collect_db_attempts(fp, now):
                if a["pid"] not in seen_pids:
                    seen_pids.add(a["pid"])
                    out_all.append(a)
        return out_all
    if isinstance(db_path, (list, tuple)):
        merged, pids = [], set()
        for fp in db_path:
            for a in collect_db_attempts(fp, now):
                if a["pid"] not in pids:
                    pids.add(a["pid"])
                    merged.append(a)
        return merged
    if not os.path.exists(db_path):
        return []
    try:
        con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True, timeout=2)
        con.row_factory = sqlite3.Row
        rows = con.execute(
            "SELECT id, work_item_id, kind, lane, requested_model, effective_model, pid, "
            "pid_start, started_at FROM attempts WHERE status='running'"
        ).fetchall()
        con.close()
    except sqlite3.Error:
        return []
    now = now if now is not None else time.time()
    out = []
    for r in rows:
        try:
            stat = Path(f"/proc/{r['pid']}/stat").read_text()
        except (OSError, TypeError):
            continue
        if stat.split()[0] == "Z" or _pid_start_fields(stat) != str(r["pid_start"] or ""):
            continue
        started = float(r["started_at"] or now)
        out.append({
            "pid": str(r["pid"]), "ppid": "",
            "runtime_s": max(0, int(now - started)),
            "kind": r["kind"] or "worker", "lane": r["lane"] or "free",
            "model": r["effective_model"] or r["requested_model"] or "auto",
            "attempt_id": r["id"], "item_id": r["work_item_id"],
            "controller": os.path.basename(os.path.dirname(os.path.dirname(db_path))),
            "controller": os.path.basename(os.path.dirname(db_path)),
            "command": f"controller {r['lane']} attempt for {r['work_item_id']}",
        })
    return out


def collect_delegations(now: float | None = None, base: str = DELEG_LIVE,
                        stale_s: int = DELEG_STALE_S) -> list[dict]:
    """Hermes delegate_task children — the only workers that run OUTSIDE the controller.

    They are FreeLLMAPI sub-agents by provider/model, but no CLI process-table entry or
    attempts row represents them, so without this they are invisible on the tracker.
    Freshness = transcript mtime: a child that is truly working appends to it constantly.
    """
    now = now if now is not None else time.time()
    out: list[dict] = []
    try:
        dirs = sorted(os.listdir(base))
    except OSError:
        return out
    for d in dirs:
        manifest = os.path.join(base, d, "manifest.json")
        try:
            with open(manifest) as fh:
                doc = json.load(fh)
        except (OSError, json.JSONDecodeError):
            continue
        for task in doc.get("tasks") or []:
            if task.get("status") != "running":
                continue
            transcript = os.path.join(base, d, f"task-{task.get('index')}.log")
            try:
                last = os.path.getmtime(transcript)
            except OSError:
                last = 0
            if now - last > stale_s:
                continue
            out.append({
                "pid": "", "ppid": "", "runtime_s": max(0, int(now - last)),
                "kind": "hermes", "lane": "free",
                "model": task.get("model") or doc.get("model") or "auto",
                "attempt_id": "%s:%s" % (doc.get("delegation_id") or d, task.get("index")),
                "command": str(task.get("goal") or "")[:300],
            })
    return out


def load_project_progress(db_path) -> dict | None:
    """Derive progress and ETA only from accepted integrations in the controller DB."""
    if isinstance(db_path, (list, tuple)):
        best = None
        for fp in db_path:
            r = load_project_progress(fp)
            if r and (best is None or r["total"] > best["total"]):
                best = r
        return best
    if not os.path.exists(db_path):
        return None
    try:
        con = sqlite3.connect(f"file:{Path(db_path)}?mode=ro", uri=True, timeout=2)
        con.row_factory = sqlite3.Row
        rows = con.execute(
            "SELECT status, integrated_at FROM work_items WHERE kind != 'container'"
        ).fetchall()
        con.close()
    except sqlite3.Error:
        return None
    total = len(rows)
    if not total:
        return None
    done_times = sorted(float(row["integrated_at"]) for row in rows
                        if row["status"] == "integrated" and row["integrated_at"] is not None)
    done = len(done_times)
    out = {
        "done": done,
        "total": total,
        "percent": round(done / total * 100, 1),
        "eta_s": None,
        "eta_reason": "need at least two accepted integrations",
        "rate_per_hour": None,
    }
    if len(done_times) >= 2 and done_times[-1] > done_times[0]:
        rate = (len(done_times) - 1) / ((done_times[-1] - done_times[0]) / 3600)
        if rate > 0:
            out["rate_per_hour"] = rate
            out["eta_s"] = (total - done) / rate * 3600
            out["eta_reason"] = "observed accepted-integration throughput"
    return out


def record_concurrency(agents: list[dict], sample_path: str, now: float, retention_s: int = 7 * 86400) -> dict:
    """Persist bounded local samples so the tracker can report observed FreeLLM concurrency."""
    path = Path(sample_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    sample = {"t": int(now), "agents": len(agents), "free": sum(a["lane"] == "free" for a in agents)}
    recent = []
    try:
        for line in path.read_text().splitlines():
            row = json.loads(line)
            if row.get("t", 0) >= now - retention_s:
                recent.append(row)
    except (OSError, json.JSONDecodeError):
        pass
    recent.append(sample)
    path.write_text("".join(json.dumps(row, separators=(",", ":")) + "\n" for row in recent))
    return {"current_free": sample["free"], "peak_free": max(row.get("free", 0) for row in recent), "samples": len(recent)}
