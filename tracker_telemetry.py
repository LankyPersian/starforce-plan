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
            "route_url": env.get("ANTHROPIC_BASE_URL") or env.get("FREELLMAPI_BASE_URL") or "",
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
    """Derive product progress and ETA only from accepted product integrations."""
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
        columns = {row[1] for row in con.execute("PRAGMA table_info(work_items)")}
        phase_expr = "phase" if "phase" in columns else "NULL AS phase"
        rows = con.execute(
            f"SELECT id, {phase_expr}, kind, status, integrated_at FROM work_items"
        ).fetchall()
        con.close()
    except sqlite3.Error:
        return None
    rows = [row for row in rows if _is_product_item(row)]
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


def _phase_for(row) -> str | None:
    phase = row["phase"] if "phase" in row.keys() else None
    if phase:
        return str(phase)
    match = re.match(r"^(F\d+)(?:-|$)", str(row["id"] or ""), re.I)
    return match.group(1).upper() if match else None


def _is_product_item(row) -> bool:
    """Product delivery excludes controller-only planning, diagnosis and containers."""
    return (row["kind"] or "") == "implement" and _phase_for(row) is not None


def _json_list(value) -> list:
    try:
        parsed = json.loads(value or "[]")
        return parsed if isinstance(parsed, list) else []
    except (TypeError, json.JSONDecodeError):
        return []


def load_delivery_snapshot(db_path: str = BUILD_DB, now: float | None = None) -> dict | None:
    """Return the product truth needed by the dashboard from the production DB."""
    if not os.path.exists(db_path):
        return None
    now = time.time() if now is None else now
    try:
        con = sqlite3.connect(f"file:{Path(db_path)}?mode=ro", uri=True, timeout=2)
        con.row_factory = sqlite3.Row
        items = con.execute(
            "SELECT id,title,kind,status,phase,lane,scope_json,acceptance_json,attempt_count,"
            "fail_count,last_fail_class,active_attempt_id,integrated_at,updated_at,park_reason "
            "FROM work_items ORDER BY id"
        ).fetchall()
        attempts = {r["id"]: r for r in con.execute(
            "SELECT id,work_item_id,status,lane,requested_model,effective_model,started_at,"
            "last_progress_at,result_sha,failure_class,detail FROM attempts WHERE status='running'"
        ).fetchall()}
        gate = con.execute(
            "SELECT at,sha,exit_code,report_path,ready FROM release_gate_runs ORDER BY id DESC LIMIT 1"
        ).fetchone()
        con.close()
    except sqlite3.Error:
        return None

    product = [row for row in items if _is_product_item(row)]
    controls = [row for row in items if not _is_product_item(row)]
    status_names = ("integrated", "running", "awaiting_review", "ready", "waiting_capacity",
                    "waiting_dependency", "parked", "blocked", "failed", "todo")

    def counts(rows):
        out = {name: 0 for name in status_names}
        out["total"] = len(rows)
        for row in rows:
            out[row["status"]] = out.get(row["status"], 0) + 1
        out["remaining"] = out["total"] - out.get("integrated", 0)
        return out

    phase_map = {}
    for row in product:
        phase = _phase_for(row) or "unassigned"
        bucket = phase_map.setdefault(phase, {"phase": phase, "total": 0, "integrated": 0, "running": 0})
        bucket["total"] += 1
        bucket["integrated"] += row["status"] == "integrated"
        bucket["running"] += row["status"] == "running"
    phases = []
    for phase in sorted(phase_map, key=lambda value: (int(value[1:]) if re.match(r"^F\d+$", value) else 999, value)):
        bucket = phase_map[phase]
        bucket["remaining"] = bucket["total"] - bucket["integrated"]
        bucket["percent"] = round(bucket["integrated"] / bucket["total"] * 100, 1) if bucket["total"] else 0
        phases.append(bucket)
    current_phase = next((p["phase"] for p in phases if p["remaining"]), None)

    active = []
    for row in items:
        if row["status"] not in ("running", "awaiting_review", "waiting_capacity", "waiting_dependency", "ready"):
            continue
        attempt = attempts.get(row["active_attempt_id"])
        active.append({
            "id": row["id"], "title": row["title"] or "", "category": "product" if _is_product_item(row) else "control",
            "phase": _phase_for(row) or "control", "status": row["status"], "lane": row["lane"] or "unknown",
            "model": ((attempt["effective_model"] or attempt["requested_model"]) if attempt else None) or "—",
            "runtime_s": max(0, int(now - float(attempt["started_at"]))) if attempt and attempt["started_at"] else None,
            "last_progress_s": max(0, int(now - float(attempt["last_progress_at"]))) if attempt and attempt["last_progress_at"] else None,
            "scope": _json_list(row["scope_json"]), "acceptance": _json_list(row["acceptance_json"]),
            "attempts": row["attempt_count"] or 0, "failures": row["fail_count"] or 0,
            "last_failure": row["last_fail_class"] or "", "park_reason": row["park_reason"] or "",
        })
    order = {"running": 0, "awaiting_review": 1, "ready": 2, "waiting_capacity": 3, "waiting_dependency": 4}
    active.sort(key=lambda row: (order.get(row["status"], 9), row["phase"], row["id"]))

    release = {"ready": False, "passed": 0, "total": 0, "failing": [], "checks": [], "at": None, "sha": None}
    if gate:
        release.update(ready=bool(gate["ready"]), at=gate["at"], sha=gate["sha"])
        try:
            report = json.loads(Path(gate["report_path"]).read_text())
            checks = report.get("checks") or []
            release["checks"] = checks
            release["total"] = len(checks)
            release["passed"] = sum(bool(check.get("ok")) for check in checks)
            release["failing"] = [check.get("name", "unknown") for check in checks if not check.get("ok")]
        except (OSError, TypeError, json.JSONDecodeError):
            release["failing"] = ["release report unavailable"]
    return {"delivery": counts(product), "control": counts(controls), "phases": phases,
            "current_phase": current_phase, "active": active, "release": release}


def derive_product_status(snapshot: dict | None, controller_up: bool) -> dict:
    if not snapshot:
        return {"label": "UNKNOWN", "complete": False, "reason": "production controller state is unavailable"}
    delivery, release = snapshot["delivery"], snapshot["release"]
    remaining = delivery["remaining"]
    if remaining == 0 and release.get("ready"):
        return {"label": "RELEASE READY", "complete": True,
                "reason": "all product work integrated and deterministic release gate passed"}
    gate = f'release gate {release.get("passed", 0)}/{release.get("total", 0)} checks passing'
    reason = f"{remaining} product work items remain; {gate}"
    if controller_up and remaining:
        return {"label": "BUILDING", "complete": False, "reason": reason}
    if remaining:
        return {"label": "STOPPED / NEEDS ATTENTION", "complete": False, "reason": reason + "; controller is not running"}
    return {"label": "AWAITING RELEASE GATE", "complete": False, "reason": gate}


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
