"""Read-only collectors for tracker agent concurrency and project throughput."""
from __future__ import annotations

import json
import os
import re
import sqlite3
import subprocess
import time
from pathlib import Path


AGENT_PATTERNS = (("claude -p", "claude"), ("codex exec", "codex"))


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
        env = env_for_pid(pid)
        base = " ".join((env.get("ANTHROPIC_BASE_URL", ""), env.get("FREELLMAPI_BASE_URL", ""))).lower()
        lane = "free" if any(token in base for token in ("3102", "freellm")) else "luna" if kind == "codex" else "subscription"
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


def load_project_progress(db_path: str) -> dict | None:
    """Derive progress and ETA only from accepted integrations in the controller DB."""
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
