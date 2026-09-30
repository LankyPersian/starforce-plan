#!/usr/bin/env python3
"""Build tracker.html from live evidence only. No hardcoded numbers.

Reads: bootstrap runner state, commissioning evidence (C1-C12 JSON), Claude session files
(Sonnet/Opus tokens), Codex session files (Luna tokens), shield DB (free lane, per model),
process table, git log. Any source that is unavailable renders as 'unknown' / 'not run'
rather than a made-up figure.

Contract (tracker_serve.py): module globals NOW, OUT, esc(); main() stamps from the
module-level NOW at call time.
"""
import glob, html, json, os, sqlite3, time, urllib.error, urllib.request
import calendar
import lane_report as lr
import tracker_telemetry as tt

FSTATE = os.path.expanduser("~/.local/state/empirium-build")
SAMPLES = os.path.join(FSTATE, "tracker_agent_samples.jsonl")
FIX_DB = os.path.expanduser("~/.local/state/empirium-fixture/build.db")
FIX_DB = os.path.expanduser("~/.local/state/empirium-fixture/build.db")

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tracker.html")
NOW = time.time()

STATE = os.path.expanduser("~/.local/state/empirium-build/bootstrap.json")
SHIELD_DB = os.path.expanduser("~/.local/state/freellm-shield/shield.db")
EVIDENCE = os.path.expanduser("~/empirium-studio-v2/.build/evidence/commissioning")
# order mirrors bootstrap_runner.STEPS (not imported: that module has runtime side effects)
STEPS = ["P0.1-facts", "P0.2-repo", "P0.3-controller",
         "P1.1-commission", "P1.2-review", "P1.3-enable", "P1.4-seed"]
PROOFS = [f"C{i}" for i in range(1, 13)]
HOT_S = 15 * 60          # a lane is "hot" if it produced usage within this window
FREE_H = 6               # free-lane window, hours


def esc(x):
    return html.escape(str(x))


# --- formatting helpers -----------------------------------------------------
def ftok(n):
    if n >= 1e9:
        return f"{n/1e9:.2f}B"
    if n >= 1e6:
        return f"{n/1e6:.1f}M"
    if n >= 1e3:
        return f"{n/1e3:.1f}k"
    return str(int(n))


def fdur(s):
    s = int(s)
    if s >= 86400:
        return f"{s//86400}d{(s%86400)//3600}h"
    if s >= 3600:
        return f"{s//3600}h{(s%3600)//60:02d}m"
    if s >= 60:
        return f"{s//60}m{s%60:02d}s"
    return f"{s}s"


def hhmm(t):
    return time.strftime("%H:%M", time.gmtime(t))


def ago(t):
    return lr.human_ago(t) if t else "unknown"


def latest_fresh_stall(path, now, freshness_s=3 * 3600):
    """Return the newest fresh STALL line, based on its own UTC timestamp.

    The heartbeat file is continually appended to; its mtime is not evidence
    that an old STALL condition is still active.
    """
    try:
        lines = open(path).read().splitlines()
    except OSError:
        return None
    newest = None
    for line in lines:
        if "STALL ALERT" not in line:
            continue
        try:
            stamp = line.split(None, 1)[0]
            at = calendar.timegm(time.strptime(stamp, "%Y-%m-%dT%H:%M:%SZ"))
        except (IndexError, ValueError, OverflowError):
            continue
        if 0 <= now - at <= freshness_s and (newest is None or at > newest[0]):
            newest = (at, line)
    return newest[1] if newest else None


# --- collectors -------------------------------------------------------------
def load_state():
    try:
        with open(STATE) as f:
            return json.load(f), None
    except FileNotFoundError:
        return {}, "bootstrap.json missing"
    except Exception as e:
        return {}, f"bootstrap.json unreadable: {e}"


def load_proofs():
    out, blocked = {}, os.path.exists(os.path.join(EVIDENCE, "BLOCKED.md"))
    for pid in PROOFS:
        p = os.path.join(EVIDENCE, f"{pid}.json")
        if not os.path.exists(p):
            out[pid] = None
            continue
        try:
            with open(p) as f:
                j = json.load(f)
        except Exception as e:
            out[pid] = {"error": str(e)}
            continue
        checks = j.get("checks") or []
        out[pid] = {
            "title": j.get("title") or "",
            "passed": j.get("passed"),
            "ok": sum(1 for c in checks if c.get("ok")),
            "n": len(checks),
            "failed": [c.get("name", "?") for c in checks if not c.get("ok")],
            "finished": j.get("finished_at") or j.get("started_at") or os.path.getmtime(p),
            "simulated": j.get("simulated") or [],
        }
    return out, blocked


def load_shield(now):
    """Per-model ok/fail over FREE_H hours, plus hourly buckets for the trend strip."""
    if not os.path.exists(SHIELD_DB):
        return None
    since = now - FREE_H * 3600
    c = sqlite3.connect(SHIELD_DB)
    c.row_factory = sqlite3.Row
    agg = {}
    for r in c.execute("select model,outcome,count(*) n,max(ts) last,avg(secs) secs from tries "
                       "where ts>? group by model,outcome", (since,)):
        e = agg.setdefault(r["model"], {"ok": 0, "bad": 0, "last": 0, "lastbad": "",
                                         "lastbad_ts": 0, "secs_sum": 0.0, "secs_n": 0})
        if r["outcome"] in ("OK", "PROBE_OK"):
            e["ok"] += r["n"]
            if r["secs"] is not None:
                e["secs_sum"] += r["secs"] * r["n"]; e["secs_n"] += r["n"]
        else:
            e["bad"] += r["n"]
            if r["last"] > e["lastbad_ts"]:
                e["lastbad"], e["lastbad_ts"] = r["outcome"], r["last"]
        e["last"] = max(e["last"], r["last"])
    buckets = [{"ok": 0, "bad": 0} for _ in range(FREE_H * 4)]   # 15-min buckets
    for r in c.execute("select ts,outcome from tries where ts>?", (since,)):
        i = min(len(buckets) - 1, int((r["ts"] - since) // 900))
        buckets[i]["ok" if r["outcome"] in ("OK", "PROBE_OK") else "bad"] += 1
    c.close()
    return {"models": agg, "buckets": buckets, "since": since}


def _proc_env(pid):
    """Read non-secret controller markers for transparent runtime reporting."""
    try:
        raw = open(f"/proc/{pid}/environ", "rb").read().split(b"\0")
    except OSError:
        return {}
    wanted = {"EMPIRIUM_BUILD_STATE", "EMPIRIUM_MAX_FREE_WORKERS", "EMPIRIUM_SHIELD_URL",
              "EMPIRIUM_UPSTREAM_URL", "EMPIRIUM_PLAN_LANE"}
    out = {}
    for item in raw:
        key, sep, value = item.partition(b"=")
        if sep and key.decode(errors="ignore") in wanted:
            out[key.decode()] = value.decode(errors="replace")
    return out


def _endpoint_status(url):
    if not url:
        return "unknown"
    try:
        with urllib.request.urlopen(url.rstrip("/") + "/v1/models", timeout=1.5) as r:
            return f"HTTP {r.status}"
    except urllib.error.HTTPError as e:
        # The real upstream commonly returns 401 without its bearer key; that still proves reachability.
        return f"HTTP {e.code}"
    except Exception as e:
        return type(e).__name__


def load_free_runtime(ps, conc):
    """Collect the live controller's free-lane target, cap, governor and health."""
    ctl = next((p for p in ps if p["kind"] == "controller"), None)
    commissioning = any(p["kind"] == "commissioning" for p in ps)
    env = _proc_env(ctl["pid"]) if ctl else {}
    if not ctl and commissioning:
        # The commissioning driver owns the fixture DB even during its short controller restart window.
        env = {"EMPIRIUM_BUILD_STATE": FIX_DB.rsplit("/", 1)[0],
               "EMPIRIUM_MAX_FREE_WORKERS": "12", "EMPIRIUM_SHIELD_URL": "http://127.0.0.1:3202",
               "EMPIRIUM_UPSTREAM_URL": "http://127.0.0.1:3201"}
    elif not ctl:
        # Keep the completed/current fixture visible after the driver exits; production DB may be empty.
        try:
            con = sqlite3.connect(f"file:{FIX_DB}?mode=ro", uri=True, timeout=1)
            has_fixture = con.execute("select count(*) from work_items").fetchone()[0] > 0
            con.close()
        except sqlite3.Error:
            has_fixture = False
        if has_fixture:
            env = {"EMPIRIUM_BUILD_STATE": FIX_DB.rsplit("/", 1)[0],
                   "EMPIRIUM_MAX_FREE_WORKERS": "12", "EMPIRIUM_SHIELD_URL": "http://127.0.0.1:3202",
                   "EMPIRIUM_UPSTREAM_URL": "http://127.0.0.1:3201"}
    state = env.get("EMPIRIUM_BUILD_STATE", FSTATE)
    cap = int(env.get("EMPIRIUM_MAX_FREE_WORKERS", "12") or 12)
    effective, paused, safe = cap, False, False
    db = os.path.join(state, "build.db")
    try:
        con = sqlite3.connect(f"file:{db}?mode=ro", uri=True, timeout=1)
        rows = dict(con.execute("select key,value from kv where key in ('eff_workers','pause_dispatch','safe_mode')"))
        con.close()
        effective = int(rows.get("eff_workers", cap))
        paused = str(rows.get("pause_dispatch", "0")) not in ("", "0", "false", "False", "None")
        safe = str(rows.get("safe_mode", "0")) not in ("", "0", "false", "False", "None")
    except (OSError, ValueError, sqlite3.Error):
        pass
    shield = env.get("EMPIRIUM_SHIELD_URL", "")
    upstream = env.get("EMPIRIUM_UPSTREAM_URL", "")
    urls = f"{shield} {upstream}"
    mode = "REAL FreeLLMAPI" if any(port in urls for port in (":3101", ":3102")) else "FIXTURE ROUTE" if any(port in urls for port in (":3201", ":3202")) else "UNKNOWN ROUTE"
    running = conc["current_free"]
    return {
        "mode": mode, "cap": cap, "effective": effective, "running": running,
        "util": (running / effective * 100) if effective else 0,
        "shield": shield or "not set", "upstream": upstream or "not set",
        "shield_status": _endpoint_status(shield), "upstream_status": _endpoint_status(upstream),
        "state": state, "paused": paused, "safe": safe, "controller_pid": ctl["pid"] if ctl else "—",
    }


def render_free_runtime(rt, conc):
    mode_cls = "c-pass" if rt["mode"] == "REAL FreeLLMAPI" else "c-retry" if rt["mode"] == "FIXTURE ROUTE" else "c-fail"
    state = "paused" if rt["paused"] else "safe mode" if rt["safe"] else "dispatching"
    util = min(100, rt["util"])
    return f'''<section class="panel free-runtime {"fixture" if rt["mode"] != "REAL FreeLLMAPI" else "real"}">
  <div class="ph"><h2>FreeLLMAPI live control plane</h2><span class="meta">this is the authoritative routing view</span>
    <div class="right"><span class="tag t-{"pass" if rt["mode"] == "REAL FreeLLMAPI" else "retry"}">{esc(rt["mode"])}</span><span class="chip">controller PID <b>{esc(rt["controller_pid"])}</b></span></div></div>
  <div class="runtime-grid">
    <div class="runtime-hero"><div class="runtime-label">FREE WORKERS NOW / EFFECTIVE CAP</div><div class="runtime-number"><b>{rt["running"]}</b><span>/ {rt["effective"]}</span></div><div class="runtime-bar"><i style="width:{util:.1f}%"></i></div><div class="runtime-sub"><b>{util:.0f}% utilized</b> · configured cap {rt["cap"]} · {state}</div></div>
    <div class="runtime-stat"><span>route mode</span><b class="{mode_cls}">{esc(rt["mode"])}</b><small>fixture means simulated upstream, not the real gateway</small></div>
    <div class="runtime-stat"><span>shield</span><b>{esc(rt["shield_status"])}</b><small class="mono">{esc(rt["shield"])}</small></div>
    <div class="runtime-stat"><span>upstream</span><b>{esc(rt["upstream_status"])}</b><small class="mono">{esc(rt["upstream"])}</small></div>
  </div>
  <div class="runtime-foot"><span>controller state <b>{esc(rt["state"])}</b></span><span>observed peak <b>{conc["peak_free"]}</b></span><span>samples <b>{conc["samples"]}</b></span><span>state DB <b class="mono">{esc(rt["state"])}</b></span></div>
</section>'''


def load_workload(rt, st, proofs, prog, now, snapshot=None):
    """Read the active controller DB for workload, blockers and human-attention items."""
    db = os.path.join(rt["state"], "build.db")
    counts = {"integrated": 0, "awaiting_review": 0, "running": 0, "queued": 0,
              "failed": 0, "parked": 0, "other": 0, "total": 0}
    issues = []
    try:
        con = sqlite3.connect(f"file:{db}?mode=ro", uri=True, timeout=1)
        con.row_factory = sqlite3.Row
        rows = con.execute("select id,title,status,lane,attempt_count,fail_count,last_fail_class,park_reason from work_items").fetchall()
        counts["total"] = len(rows)
        for row in rows:
            status = row["status"] or "other"
            if status in counts: counts[status] += 1
            elif status in ("pending", "ready", "queued", "waiting_capacity"): counts["queued"] += 1
            else: counts["other"] += 1
            if row["status"] in ("parked", "blocked"):
                issues.append({"severity": "HIGH", "kind": "WORK_ITEM_BLOCKED", "detail": f'{row["id"]}: {row["park_reason"] or row["title"]}'})
            elif row["status"] == "awaiting_review":
                issues.append({"severity": "INFO", "kind": "AWAITING_REVIEW", "detail": f'{row["id"]}: waiting for review ({row["lane"] or "unknown"} lane)'})
            if row["last_fail_class"]:
                counts["failed"] += 1
                issues.append({"severity": "WARN", "kind": row["last_fail_class"], "detail": f'{row["id"]}: {row["fail_count"] or 0} failures'})
        for row in con.execute("select severity,kind,detail,at from incidents where resolved_at is null order by at desc limit 8"):
            issues.append(dict(row))
        for row in con.execute("select lane,model,classification,detail,at from provider_events order by at desc limit 8"):
            issues.append({"severity": "WARN", "kind": f'{row["lane"]}:{row["classification"]}', "detail": f'{row["model"]}: {row["detail"]}', "at": row["at"]})
        con.close()
    except (OSError, sqlite3.Error):
        issues.append({"severity": "WARN", "kind": "DB_UNAVAILABLE", "detail": f"Could not read {db}"})
    # Deduplicate identical bulletins while keeping the newest/highest-signal entries.
    seen, clean = set(), []
    rank = {"HIGH": 0, "WARN": 1, "INFO": 2}
    for item in sorted(issues, key=lambda x: (rank.get(x.get("severity"), 3), -(x.get("at") or 0))):
        key = (item.get("kind"), item.get("detail"))
        if key not in seen:
            seen.add(key); clean.append(item)
    active = (snapshot or {}).get("current_phase") or next((s for s in STEPS if s not in (st.get("done") or [])), None)
    pass_n = sum(1 for p in proofs.values() if p and p.get("passed") is True)
    if snapshot and active:
        phase = next((p for p in snapshot.get("phases", []) if p["phase"] == active), None)
        phase_total = phase["total"] if phase else 0
        phase_done = phase["integrated"] if phase else 0
        phase_label = active
    else:
        phase_total = len(PROOFS) if active == "P1.1-commission" else len(STEPS)
        phase_done = pass_n if active == "P1.1-commission" else len(st.get("done") or [])
        phase_label = active or "no active product phase"
    if counts["awaiting_review"] and not counts["running"] and not counts["queued"]:
        eta, eta_note = "blocked", f'{counts["awaiting_review"]} item(s) awaiting review; no reviewer currently running'
    elif prog and prog.get("eta_s") is not None:
        eta = "~" + fdur(prog["eta_s"])
        eta_note = prog.get("eta_reason") or "based on accepted integrations"
    elif counts["awaiting_review"]:
        eta, eta_note = "blocked", f'{counts["awaiting_review"]} item(s) awaiting review'
    else:
        eta, eta_note = "unknown", "not enough accepted-integration history"
    return {"counts": counts, "issues": clean[:10], "active": phase_label, "phase_done": phase_done,
            "phase_total": phase_total, "phase_pct": (phase_done / phase_total * 100 if phase_total else 100),
            "eta": eta, "eta_note": eta_note, "db": db}


def render_transparency(w):
    c, pct = w["counts"], min(100, w["phase_pct"])
    bullets = []
    for item in w["issues"]:
        sev = item.get("severity", "INFO")
        cls = "c-fail" if sev == "HIGH" else "c-retry" if sev == "WARN" else "dim"
        bullets.append(f'<li><span class="issue-sev {cls}">{esc(sev)}</span><b>{esc(item.get("kind", "ISSUE"))}</b><span>{esc(item.get("detail", ""))}</span></li>')
    if not bullets:
        bullets.append('<li><span class="c-pass">CLEAR</span><span>no unresolved controller incidents or provider failures reported</span></li>')
    return f'''<section class="panel transparency">
  <div class="ph"><h2>Progress, workload &amp; issues bulletin</h2><span class="meta">derived from the active controller DB and live proof files</span><div class="right"><span class="chip">ETA <b class="{"c-fail" if w["eta"] == "blocked" else "c-run"}">{esc(w["eta"])}</b></span></div></div>
  <div class="overview-grid">
    <div class="overview-hero"><div class="runtime-label">CURRENT PHASE</div><div class="overview-phase">{esc(w["active"])}</div><div class="runtime-bar"><i style="width:{pct:.1f}%"></i></div><div class="runtime-sub"><b>{w["phase_done"]}/{w["phase_total"]}</b> phase gates/proofs complete · {pct:.0f}%</div><small>{esc(w["eta_note"])}</small></div>
    <div class="overview-stat"><span>total workload</span><b>{c["total"]}</b><small>{c["integrated"]} integrated · {c["total"] - c["integrated"]} remaining</small></div>
    <div class="overview-stat"><span>active / waiting</span><b>{c["running"]} / {c["awaiting_review"]}</b><small>{c["queued"]} queued · {c["parked"]} parked</small></div>
    <div class="overview-stat"><span>failure pressure</span><b class="{"c-fail" if c["failed"] else "c-pass"}">{c["failed"]}</b><small>failed or retry-classified items</small></div>
  </div>
  <div class="workload-strip"><span>integrated <b class="c-pass">{c["integrated"]}</b></span><span>awaiting review <b class="c-retry">{c["awaiting_review"]}</b></span><span>running <b class="c-run">{c["running"]}</b></span><span>queued <b>{c["queued"]}</b></span><span>failed <b class="c-fail">{c["failed"]}</b></span><span>parked <b>{c["parked"]}</b></span></div>
  <div class="issues"><div class="issues-title">WHAT THE LLMs CANNOT RESOLVE ALONE / CURRENT EXCEPTIONS</div><ul>{"".join(bullets)}</ul></div>
</section>'''


def load_activity(rt, now, limit=36):
    """Merge build-controller events and shield attempts into one honest timeline.

    Shield traffic is deliberately labelled separately from product work: a busy
    provider lane is not evidence that a product item is being implemented.
    """
    items = []
    build_db = os.path.join(rt["state"], "build.db")
    since = now - 12 * 3600
    try:
        con = sqlite3.connect(f"file:{build_db}?mode=ro", uri=True, timeout=1)
        con.row_factory = sqlite3.Row
        for row in con.execute("select at,type,entity_id,payload_json from events where at>? order by at desc limit 80", (since,)):
            try:
                payload = json.loads(row["payload_json"] or "{}")
            except json.JSONDecodeError:
                payload = {}
            typ = row["type"] or "EVENT"
            title = {
                "ATTEMPT_STARTED": "Worker started", "ATTEMPT_FINISHED": "Worker finished",
                "STATUS": "Work item changed state", "HARNESS_PASSED": "Integration passed",
                "HARNESS_FAILED": "Integration failed", "REVIEW_STARTED": "Review started",
            }.get(typ, typ.replace("_", " ").title())
            detail = str(row["entity_id"] or "")
            if payload.get("lane") or payload.get("model"):
                detail += " · " + ":".join(str(payload.get(k)) for k in ("lane", "model") if payload.get(k))
            if payload.get("from") or payload.get("to"):
                detail += f' · {payload.get("from", "?")} → {payload.get("to", "?")}'
            tone = "fail" if "FAILED" in typ else "pass" if "PASSED" in typ else "run" if "STARTED" in typ else "info"
            items.append({"ts": row["at"], "kind": "BUILD", "tone": tone, "title": title, "detail": detail})
        con.close()
    except (OSError, sqlite3.Error):
        pass
    if os.path.exists(SHIELD_DB):
        try:
            con = sqlite3.connect(f"file:{SHIELD_DB}?mode=ro", uri=True, timeout=1)
            con.row_factory = sqlite3.Row
            cols = {r[1] for r in con.execute("pragma table_info(tries)")}
            extra = ",logical_request,retry_fallback" if {"logical_request", "retry_fallback"} <= cols else ""
            for row in con.execute(f"select ts,model,effective,outcome,detail{extra} from tries where ts>? order by ts desc limit 80", (since,)):
                outcome = row["outcome"] or "UNKNOWN"
                logical = (row["logical_request"] if "logical_request" in row.keys() else None) or "upstream_attempt"
                detail = f'{row["model"] or "unassigned"} → {row["effective"] or "unresolved"}'
                if row["detail"]:
                    detail += f' · {str(row["detail"])[:110]}'
                items.append({"ts": row["ts"], "kind": "SHIELD", "tone": "pass" if outcome in ("OK", "PROBE_OK") else "fail",
                              "title": f'{logical.replace("_", " ").title()} · {outcome}', "detail": detail})
            con.close()
        except (OSError, sqlite3.Error):
            pass
    items.sort(key=lambda x: x["ts"], reverse=True)
    # Keep both narratives visible even when provider traffic is much denser:
    # the feed must not bury build events under shield retries/probes.
    build = [x for x in items if x["kind"] == "BUILD"][:limit // 2]
    shield = [x for x in items if x["kind"] == "SHIELD"][:limit // 2]
    return sorted(build + shield, key=lambda x: x["ts"], reverse=True)[:limit]


def render_activity(activity, workload, rt):
    c = workload["counts"]
    feed = []
    for item in activity:
        feed.append(f'<li class="activity-item"><span class="activity-dot a-{item["tone"]}"></span>'
                    f'<div><b>{esc(item["title"])}</b><span>{esc(item["detail"])}</span></div>'
                    f'<time>{esc(ago(item["ts"]))}</time></li>')
    if not feed:
        feed.append('<li class="activity-empty">No activity recorded in the last 12 hours.</li>')
    build_n = sum(1 for x in activity if x["kind"] == "BUILD")
    shield_n = sum(1 for x in activity if x["kind"] == "SHIELD")
    return f'''<section class="panel activity-panel">
  <div class="ph"><h2>All activity</h2><span class="meta">one timeline · last 12 hours · build work separated from provider traffic</span></div>
  <div class="activity-layout">
    <div class="activity-summary">
      <div class="activity-kicker">WHAT IS ACTUALLY BUILDING</div>
      <div class="activity-big">{c["running"]}<span> active work item</span></div>
      <div class="activity-bar"><i style="width:{min(100, c["running"] / max(1, rt["effective"]) * 100):.1f}%"></i></div>
      <p><b>{c["queued"]}</b> ready/queued · <b>{c["awaiting_review"]}</b> awaiting review · <b>{c["parked"]}</b> parked or dependency-blocked</p>
      <div class="activity-callout {"callout-warn" if c["running"] < 2 and c["queued"] else ""}">
        <b>{"Build fan-out is low" if c["running"] < 2 and c["queued"] else "Build fan-out is active"}</b>
        <span>{"The controller is alive, but ready work is not being dispatched at the configured capacity." if c["running"] < 2 and c["queued"] else "Workers are actively consuming the ready queue."}</span>
      </div>
      <div class="activity-legend"><span><i class="activity-dot a-run"></i> build events <b>{build_n}</b></span><span><i class="activity-dot a-pass"></i> shield/provider events <b>{shield_n}</b></span></div>
    </div>
    <ol class="activity-feed">{"".join(feed)}</ol>
  </div>
</section>'''


def render_product_dashboard(snapshot, status, bootstrap_complete):
    if not snapshot:
        return '<section class="panel product-truth"><div class="pb"><b class="c-fail">PRODUCT STATUS UNKNOWN</b><br><span class="dim">Production build.db could not be read. Bootstrap completion is not evidence that the product is complete.</span></div></section>'
    d, ctl, rel = snapshot["delivery"], snapshot["control"], snapshot["release"]
    pct = d["integrated"] / d["total"] * 100 if d["total"] else 0
    status_cls = "c-pass" if status["complete"] else "c-run" if status["label"] == "BUILDING" else "c-fail"
    phase_cards = []
    for phase in snapshot["phases"]:
        phase_cards.append(
            f'<div class="phase-card {"phase-active" if phase["phase"] == snapshot["current_phase"] else ""}">'
            f'<div><b>{esc(phase["phase"])}</b><span>{phase["integrated"]}/{phase["total"]}</span></div>'
            f'<div class="runtime-bar"><i style="width:{min(100, phase["percent"]):.1f}%"></i></div>'
            f'<small>{phase["remaining"]} remaining · {phase["running"]} running</small></div>')
    if not phase_cards:
        phase_cards.append('<span class="dim">No product phases have been seeded yet.</span>')
    work_rows = []
    for item in snapshot["active"][:30]:
        scope = ", ".join(item["scope"][:3]) or "no file scope recorded"
        if len(item["scope"]) > 3:
            scope += f' (+{len(item["scope"]) - 3})'
        runtime = fdur(item["runtime_s"]) if item["runtime_s"] is not None else "—"
        progress = fdur(item["last_progress_s"]) + " ago" if item["last_progress_s"] is not None else "—"
        fail = f'<span class="c-retry">{esc(item["last_failure"])}</span>' if item["last_failure"] else '<span class="dim">none</span>'
        work_rows.append(
            f'<tr><td><b class="mono">{esc(item["id"])}</b><div class="dim small">{esc(item["title"])}</div></td>'
            f'<td><span class="tag t-{"run" if item["status"] == "running" else "pend"}">{esc(item["status"])}</span><div class="dim small">{esc(item["category"])} · {esc(item["phase"])}</div></td>'
            f'<td>{esc(item["lane"])}<div class="mono small">{esc(item["model"])}</div></td>'
            f'<td class="cmd" title="{esc(scope)}">{esc(scope)}</td><td class="r num">{runtime}<div class="dim small">progress {progress}</div></td>'
            f'<td class="r num">{item["attempts"]} / {item["failures"]}<div class="small">{fail}</div></td></tr>')
    if not work_rows:
        work_rows.append('<tr><td colspan="6" class="dim">No running, ready, review, capacity-blocked, or dependency-blocked work items.</td></tr>')
    gate_rows = []
    for check in rel.get("checks", []):
        gate_rows.append(f'<tr><td><span class="c-{"pass" if check.get("ok") else "fail"}">{"PASS" if check.get("ok") else "FAIL"}</span></td><td class="mono">{esc(check.get("name", "unknown"))}</td><td>{esc(check.get("detail", ""))}</td></tr>')
    if not gate_rows:
        gate_rows.append('<tr><td colspan="3" class="dim">No release-gate report is available yet.</td></tr>')
    bootstrap_text = "complete" if bootstrap_complete else "incomplete"
    return f'''<section class="panel product-truth">
  <div class="truth-head"><div><div class="runtime-label">ACTUAL PRODUCT STATUS</div><div class="truth-status {status_cls}">{esc(status["label"])}</div><div class="truth-reason">{esc(status["reason"])}</div></div><div class="truth-warning"><b>Bootstrap complete is not product complete.</b><span>Bootstrap is {bootstrap_text}; release readiness requires zero remaining product items and a green deterministic release gate.</span></div></div>
  <div class="truth-grid"><div class="truth-stat"><span>product integration</span><b>{d["integrated"]}/{d["total"]}</b><small>{pct:.1f}% accepted · {d["remaining"]} remaining</small></div><div class="truth-stat"><span>current product phase</span><b>{esc(snapshot["current_phase"] or "none")}</b><small>derived from unfinished delivery items</small></div><div class="truth-stat"><span>release gate</span><b class="{"c-pass" if rel["ready"] else "c-fail"}">{rel["passed"]}/{rel["total"]}</b><small>{"ready" if rel["ready"] else str(len(rel["failing"])) + " checks failing"}</small></div><div class="truth-stat"><span>control/support work</span><b>{ctl["integrated"]}/{ctl["total"]}</b><small>planning, diagnosis, containers; excluded from product progress</small></div></div>
  <div class="phase-roadmap"><div class="subhead">PHASE ROADMAP</div><div class="phase-grid">{"".join(phase_cards)}</div></div>
  <div class="subsection"><div class="subhead">LIVE WORK QUEUE — WHAT EACH ACTIVE OR BLOCKED CALL CONTRIBUTES</div><div class="table-scroll"><table><thead><tr><th>work item</th><th>state</th><th>lane / model</th><th>expected artifact scope</th><th class="r">runtime</th><th class="r">attempts / fails</th></tr></thead><tbody>{"".join(work_rows)}</tbody></table></div></div>
  <div class="subsection"><div class="subhead">DETERMINISTIC RELEASE GATE — THE ONLY PRODUCT-DONE AUTHORITY</div><div class="table-scroll"><table><thead><tr><th>result</th><th>check</th><th>evidence</th></tr></thead><tbody>{"".join(gate_rows)}</tbody></table></div></div>
</section>'''


def parse_procs(lines):
    kinds = (("bootstrap_runner", "runner"), ("controller.py run", "controller"),
             ("run_commissioning", "commissioning"), ("freellm_shield", "shield"),
             ("fixture_claude_worker", "claude"), ("fixture_codex_worker", "codex"),
             ("fixture_freellm_worker", "freellm"),
             ("codex exec", "codex"), ("claude -p", "claude"))
    out = []
    for ln in lines:
        parts = ln.split(None, 2)
        if len(parts) < 3 or not parts[1].isdigit():
            continue
        kind = next((k for pat, k in kinds if pat in parts[2]), "other")
        out.append({"pid": parts[0], "et": int(parts[1]), "cmd": parts[2], "kind": kind})
    return out


# --- renderers --------------------------------------------------------------
def render_pipeline(st, runner_up):
    done, fails = st.get("done") or [], st.get("fails") or {}
    active = next((s for s in STEPS if s not in done), None)
    cells = []
    for i, sid in enumerate(STEPS):
        code, _, name = sid.partition("-")
        n = fails.get(sid, 0)
        if sid in done:
            cls, label = "done", "done"
            sub = f"{n} retr{'y' if n == 1 else 'ies'} before pass" if n else "passed"
        elif sid == active:
            if n:
                cls, label, sub = "retry", f"retry {n}", f"{n} failed check{'s' if n != 1 else ''}"
            else:
                cls, label, sub = "run", "running", "first attempt"
            if not runner_up:
                cls, label, sub = "stall", "stalled", "runner not in process table"
        else:
            cls, label, sub = "pend", "pending", f"{n} past fails" if n else "queued"
        cells.append(
            f'<li class="step s-{cls}"><div class="bar"></div>'
            f'<div class="st-top"><span class="code">{esc(code)}</span>'
            f'<span class="tag t-{cls}">{esc(label)}</span></div>'
            f'<div class="st-name">{esc(name)}</div><div class="st-sub">{esc(sub)}</div></li>')
    return "".join(cells), active


def render_proofs(proofs):
    cells = []
    for pid in PROOFS:
        p = proofs[pid]
        if p is None:
            cells.append(f'<div class="proof p-none" title="no evidence file">'
                         f'<div class="pr-top"><b>{pid}</b><span class="tag t-pend">not run</span></div>'
                         f'<div class="meter"><i style="width:0"></i></div>'
                         f'<div class="pr-t dim">no {pid}.json</div></div>')
            continue
        if "error" in p:
            cells.append(f'<div class="proof p-fail"><div class="pr-top"><b>{pid}</b>'
                         f'<span class="tag t-fail">unreadable</span></div>'
                         f'<div class="pr-t">{esc(p["error"][:80])}</div></div>')
            continue
        frac = p["ok"] / p["n"] if p["n"] else 0
        if p["passed"] is True:
            cls, tag = "pass", "pass"
        elif p["passed"] is False:
            cls, tag = "fail", "fail"
        else:
            cls, tag = "pend", "unknown"
        tip = p["title"]
        if p["failed"]:
            tip += "\n\nfailing:\n- " + "\n- ".join(p["failed"])
        sim = f' · {len(p["simulated"])} simulated' if p["simulated"] else ""
        cells.append(
            f'<div class="proof p-{cls}" title="{esc(tip)}">'
            f'<div class="pr-top"><b>{pid}</b><span class="num">{p["ok"]}/{p["n"]}</span>'
            f'<span class="tag t-{cls}">{tag}</span></div>'
            f'<div class="meter"><i style="width:{frac*100:.1f}%"></i></div>'
            f'<div class="pr-t">{esc(p["title"])}</div>'
            f'<div class="pr-m">{esc(ago(p["finished"]))}{esc(sim)}</div></div>')
    return "".join(cells)


def render_sub_lanes(cu, xu, now):
    rows, hot = [], 0
    items = [("claude", m, e) for m, e in cu.items() if m != "<synthetic>"] + \
            [("codex", m, e) for m, e in xu.items()]
    items.sort(key=lambda t: -t[2]["tok"])
    top = max((e["tok"] for _, _, e in items), default=0) or 1
    for vendor, m, e in items:
        is_hot = now - e["last"] < HOT_S
        hot += is_hot
        extra = f' · {e["sessions"]} sess' if "sessions" in e else ""
        rows.append(
            f'<tr class="{"hot" if is_hot else ""}"><td><span class="dot {"d-run" if is_hot else "d-idle"}"></span>'
            f'{esc(m)}<div class="dim small">{esc(vendor)}</div></td>'
            f'<td class="r num">{ftok(e["tok"])}<div class="hbar"><i style="width:{e["tok"]/top*100:.1f}%"></i></div></td>'
            f'<td class="r num">{e.get("calls", 0)}<span class="dim">{esc(extra)}</span></td>'
            f'<td class="r num {"c-run" if is_hot else "dim"}">{esc(ago(e["last"]))}</td></tr>')
    if not rows:
        rows.append('<tr><td colspan="4" class="dim">no session logs in the last 12 h</td></tr>')
    return "".join(rows), hot, len(items)


def render_free(sh, now):
    if sh is None:
        return ('<tr><td colspan="5" class="dim">shield.db not found — free lane unknown</td></tr>',
                "", {"ok": 0, "bad": 0}, 0)
    rows, strong, hot = [], {"ok": 0, "bad": 0}, 0
    for m, e in sorted(sh["models"].items(), key=lambda kv: -(kv[1]["ok"] + kv[1]["bad"])):
        pinned = m in lr.STRONG_TIER
        if pinned:
            strong["ok"] += e["ok"]; strong["bad"] += e["bad"]
        is_hot = now - e["last"] < HOT_S
        hot += is_hot
        tot = e["ok"] + e["bad"]
        okp = e["ok"] / tot * 100 if tot else 0
        lat = f'{e["secs_sum"]/e["secs_n"]:.1f}s' if e["secs_n"] else "–"
        state = (f'<span class="c-pass">ok</span>' if e["bad"] == 0 else
                 f'<span class="c-retry">{esc(e["lastbad"])}</span> <span class="dim">{esc(ago(e["lastbad_ts"]))}</span>')
        rows.append(
            f'<tr><td><span class="dot {"d-run" if is_hot else "d-idle"}"></span>{esc(m)}'
            f'<div class="small">{"<span class=c-run>pinned strong</span>" if pinned else "<span class=dim>reliable</span>"}</div></td>'
            f'<td class="r num"><span class="c-pass">{e["ok"]}</span><span class="dim"> / </span>'
            f'<span class="{"c-fail" if e["bad"] else "dim"}">{e["bad"]}</span>'
            f'<div class="split"><i class="ok" style="width:{okp:.1f}%"></i><i class="bad" style="width:{100-okp:.1f}%"></i></div></td>'
            f'<td class="r num">{lat}</td><td>{state}</td>'
            f'<td class="r num {"c-run" if is_hot else "dim"}">{esc(ago(e["last"]))}</td></tr>')
    if not rows:
        rows.append(f'<tr><td colspan="5" class="dim">no tries in the last {FREE_H} h</td></tr>')
    # trend strip: stacked ok/fail per 15-min bucket, heights relative to the busiest bucket
    b = sh["buckets"]
    peak = max((x["ok"] + x["bad"] for x in b), default=0) or 1
    bars = []
    for i, x in enumerate(b):
        t0 = sh["since"] + i * 900
        tip = f'{hhmm(t0)}–{hhmm(t0 + 900)} UTC: {x["ok"]} ok, {x["bad"]} fail'
        bars.append(f'<span title="{esc(tip)}"><i class="bad" style="height:{x["bad"]/peak*100:.1f}%"></i>'
                    f'<i class="ok" style="height:{x["ok"]/peak*100:.1f}%"></i></span>')
    total = sum(x["ok"] + x["bad"] for x in b)
    trend = (f'<div class="trend">{"".join(bars)}</div>'
             f'<div class="axis"><span>{hhmm(sh["since"])}</span>'
             f'<span>{total} tries · peak {peak}/15 min</span><span>{hhmm(now)} UTC</span></div>')
    return "".join(rows), trend, strong, hot


def render_cooldowns(st, now):
    out = []
    for key, label in (("sub_cooldown_until", "claude"), ("luna_cooldown_until", "luna")):
        t = st.get(key)
        if t is None:
            out.append(f'<span class="chip">{label} <b class="dim">unknown</b></span>')
        elif t > now:
            out.append(f'<span class="chip c-retry">{label} cooldown <b>{fdur(t - now)}</b>'
                       f' <span class="dim">→ {hhmm(t)}</span></span>')
        else:
            out.append(f'<span class="chip">{label} <b class="c-pass">clear</b></span>')
    for m, t in (st.get("breakers") or {}).items():
        if t > now:
            out.append(f'<span class="chip c-fail">breaker {esc(m)} <b>{fdur(t - now)}</b></span>')
    return "".join(out)


def render_procs(ps):
    if not ps:
        return '<tr><td colspan="4" class="dim">no build processes in the process table</td></tr>'
    return "".join(
        f'<tr><td><span class="kind k-{p["kind"]}">{p["kind"]}</span></td>'
        f'<td class="r num dim">{esc(p["pid"])}</td><td class="r num">{fdur(p["et"])}</td>'
        f'<td class="cmd" title="{esc(p["cmd"])}">{esc(p["cmd"])}</td></tr>' for p in ps)


def render_commits(cs):
    rows = [f'<tr><td class="dim">{esc(repo)}</td><td class="num c-run">{esc(h)}</td>'
            f'<td class="cmd" title="{esc(s)}">{esc(s)}</td><td class="r num dim">{esc(when)}</td></tr>'
            for repo, h, s, when in cs]
    return "".join(rows) or '<tr><td colspan="4" class="dim">git log unavailable</td></tr>'


def merge_agents(cli_agents, db_agents, dlg_agents):
    """One row per live sub-agent from three independent sources.

    The CLI scan proves a worker process exists but not which item it owns; the
    attempts table proves the item but is the controller's own claim; /proc is the
    arbiter and collect_db_attempts already applied it. Hermes children (delegate_task)
    exist in neither: their provider/model lane is invisible unless the registry is read.
    """
    by_pid, rows = {}, []
    for a in list(cli_agents) + list(db_agents):
        if a["pid"] in by_pid:
            cur = by_pid[a["pid"]]
            if a.get("item_id"):            # DB row wins: it carries item attribution
                cur.update({k: v for k, v in a.items() if v})
            continue
        a = dict(a)
        a.setdefault("source", "process scan")
        a["source"] = "db attempts" if a.get("attempt_id") else "process scan"
        by_pid[a["pid"]] = a
        rows.append(a)
    for a in dlg_agents:
        a = dict(a)
        a["source"] = "hermes registry"
        rows.append(a)
    rows.sort(key=lambda r: (r["kind"], -(r.get("runtime_s") or 0)))
    return rows


def render_agents(agents):
    if not agents:
        return ('<tr><td colspan="7" class="dim">no sub-agents are running right now — the process table, '
                'the controller attempts table and the Hermes delegation registry all agree (every lane '
                'is idle or capacity-blocked)</td></tr>', 0)
    srcs = sorted({a["source"] for a in agents})
    kinds = sorted({a["kind"] for a in agents})
    out = []
    for a in agents:
        rt = f'<span class="num">{fdur(a["runtime_s"])}</span>' if a.get("runtime_s") else '<span class="dim">—</span>'
        out.append(
            f'<tr><td><span class="kind k-{esc(a["kind"])}">{esc(a["kind"])}</span></td>'
            f'<td><span class="lane l-{esc(a["lane"])}">{esc(a["lane"])}</span></td>'
            f'<td class="mono">{esc(a["model"])}</td>'
            f'<td class="mono">{esc(a.get("item_id") or a.get("attempt_id") or "—")}</td>'
            f'<td class="r">{rt}</td><td class="dim small">{esc(a["source"])}</td>'
            f'<td class="cmd" title="{esc(a["command"])}">{esc(a["command"])}</td></tr>')
    n = len(agents)
    return "".join(out), (n, srcs, kinds)


def render_progress(prog):
    if not prog:
        return '<div class="note dim">Overall project progress: no controller work items exist yet.</div>', "0/0"
    done, total = prog["done"], prog["total"]
    pct = prog["percent"]
    eta = ("ETA ~" + fdur(prog["eta_s"])) if prog.get("eta_s") else ("ETA: " + esc(prog.get("eta_reason") or "n/a"))
    rate = f'{prog["rate_per_hour"]:.1f}/h' if prog.get("rate_per_hour") else "—"
    frac = f"{done}/{total}"
    return (f'<div class="note">Overall project progress: <b class="num">{frac}</b> work items integrated '
            f'(<b class="num">{pct:.0f}%</b>) · throughput <b class="num">{esc(rate)}</b> · {eta}'
            f'<br><span class="dim">{esc(prog.get("eta_reason") or "")}</span></div>'), frac


def render_bot_office(agents):
    """Show the live workforce as little robots placed in the supplied office art."""
    views = ["front", "three-quarter", "side", "front", "back", "three-quarter", "side", "front"]
    names = ["CONTROL", "REVIEW", "BUILD", "PROVIDER", "TEST", "RELEASE", "RESEARCH", "QUEUE"]
    cards = []
    for i, name in enumerate(names):
        a = agents[i] if i < len(agents) else None
        state = "working" if a else "standby"
        kind = (a.get("kind") if a else "station")
        model = (a.get("model") if a else "available")
        item = (a.get("item_id") or a.get("attempt_id") if a else "ready")
        cards.append(
            f'<article class="office-bot bot-{i+1} state-{state}">'
            f'<div class="bot-shadow"></div><img class="robot-figure" src="/assets/office/robot-{views[i]}.png" alt="{esc(name)} robot">'
            f'<div class="bot-plate"><b>{esc(name)}</b><span>{esc(kind)} · {esc(model)}</span><small>{esc(item)}</small></div>'
            f'</article>')
    return f'''<section class="panel bot-office">
  <div class="ph"><h2>Industrial Steam / Bot Floor</h2><span class="meta">each live worker has a station in the office</span><div class="right"><span class="tag t-run">{len(agents)} active</span><span class="chip">visual layer · live data below</span></div></div>
  <div class="office-scene"><div class="office-sign">EMPIRIUM STUDIO <span>BOT OPERATIONS</span></div><div class="office-grid"></div>{"".join(cards)}</div>
</section>'''


CSS = """
:root{color-scheme:dark;
 --bg:#0b0d10;--panel:#111418;--panel2:#161a1f;--line:#22272e;--line2:#2d333b;
 --fg:#d7dde4;--fg2:#9aa4af;--dim:#5f6b77;
 --pass:#3fb950;--retry:#d29922;--fail:#f85149;--run:#58a6ff;--pend:#6e7681;
 --mono:ui-monospace,SFMono-Regular,"JetBrains Mono",Menlo,Consolas,monospace;
 --sans:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
*{box-sizing:border-box}
html,body{margin:0;background:var(--bg);color:var(--fg)}
body{font:13px/1.45 var(--sans);min-width:380px;padding:0 0 32px}
.num,td,.code,.mono{font-variant-numeric:tabular-nums}
.num,.code,.mono,table{font-family:var(--mono)}
.dim{color:var(--dim)} .small{font-size:11px} .r{text-align:right}
.c-pass{color:var(--pass)} .c-retry{color:var(--retry)} .c-fail{color:var(--fail)} .c-run{color:var(--run)}
header{position:sticky;top:0;z-index:5;background:rgba(11,13,16,.94);backdrop-filter:blur(6px);
 border-bottom:1px solid var(--line);padding:10px 20px;display:flex;align-items:center;gap:14px;flex-wrap:wrap}
.brand{font-weight:600;letter-spacing:.01em;font-size:13px}
.brand span{color:var(--dim);font-weight:400}
.badge{font:600 10px/1 var(--mono);letter-spacing:.08em;text-transform:uppercase;padding:4px 7px;border-radius:3px;border:1px solid}
.b-live{color:var(--pass);border-color:rgba(63,185,80,.4);background:rgba(63,185,80,.08)}
.b-idle{color:var(--pend);border-color:var(--line2)}
.b-live::before{content:"";display:inline-block;width:6px;height:6px;border-radius:50%;background:var(--pass);margin-right:6px;vertical-align:1px;animation:pulse 2s infinite}
@keyframes pulse{50%{opacity:.3}}
.stamp{font:11px var(--mono);color:var(--fg2)} .stamp .stale{color:var(--retry)}
.spacer{flex:1}
#refresh{font:600 11px var(--mono);letter-spacing:.06em;padding:6px 11px;cursor:pointer;background:var(--panel2);
 color:var(--fg);border:1px solid var(--line2);border-radius:4px}
#refresh:hover{border-color:var(--run);color:var(--run)}
#refresh[disabled]{opacity:.6;cursor:wait}
main{padding:14px 20px;max-width:1480px;margin:0 auto;display:grid;gap:14px}
.health{font:12px var(--mono);color:var(--fg2);padding:9px 12px;border:1px solid var(--line);border-radius:6px;background:var(--panel);
 display:flex;flex-wrap:wrap;gap:4px 0}
.health>span:not(:last-child)::after{content:"·";color:var(--dim);margin:0 10px}
.health b{color:var(--fg);font-weight:600}
.panel{background:var(--panel);border:1px solid var(--line);border-radius:6px;min-width:0}
.ph{display:flex;align-items:baseline;gap:10px;padding:9px 12px;border-bottom:1px solid var(--line);flex-wrap:wrap}
.ph h2{margin:0;font-size:11px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--fg2)}
.ph .meta{font:11px var(--mono);color:var(--dim)}
.ph .right{margin-left:auto;display:flex;gap:6px;flex-wrap:wrap}
.pb{padding:12px}
.free-runtime{border-color:rgba(88,166,255,.45);box-shadow:0 0 0 1px rgba(88,166,255,.08)}
.free-runtime.fixture{border-color:rgba(210,153,34,.65);box-shadow:0 0 0 1px rgba(210,153,34,.10)}
.runtime-grid{display:grid;grid-template-columns:minmax(260px,1.35fr) repeat(3,minmax(150px,1fr));gap:8px;padding:12px}
.runtime-hero,.runtime-stat{background:var(--panel2);border:1px solid var(--line);border-radius:5px;padding:11px}
.runtime-label,.runtime-stat span{font:600 10px var(--mono);letter-spacing:.07em;text-transform:uppercase;color:var(--dim)}
.runtime-number{display:flex;align-items:baseline;gap:5px;margin:5px 0 4px;font-family:var(--mono)}
.runtime-number b{font-size:32px;color:var(--run)} .runtime-number span{font-size:16px;color:var(--fg2)}
.runtime-bar{height:8px;background:var(--line);border-radius:4px;overflow:hidden;margin:6px 0}
.runtime-bar i{display:block;height:100%;background:var(--run);border-radius:4px;min-width:2px}
.runtime-sub{font:11px var(--mono);color:var(--fg2)}
.runtime-stat{display:flex;flex-direction:column;gap:6px}.runtime-stat b{font:600 16px var(--mono);color:var(--fg)}
.runtime-stat small{font-size:10px;color:var(--dim);overflow-wrap:anywhere}.runtime-foot{display:flex;gap:16px;flex-wrap:wrap;padding:8px 12px;border-top:1px solid var(--line);font:11px var(--mono);color:var(--dim)}
.runtime-foot b{color:var(--fg)}
.transparency{border-color:rgba(63,185,80,.35)}
.product-truth{border-color:rgba(88,166,255,.65);box-shadow:0 0 0 1px rgba(88,166,255,.10)}
.truth-head{display:grid;grid-template-columns:minmax(280px,1.25fr) minmax(280px,1fr);gap:12px;padding:14px}
.truth-status{font:700 30px var(--mono);margin:4px 0}.truth-reason{font:12px var(--mono);color:var(--fg2)}
.truth-warning{border:1px solid rgba(210,153,34,.5);background:rgba(210,153,34,.07);border-radius:5px;padding:11px;display:flex;flex-direction:column;gap:4px}.truth-warning b{color:var(--retry)}.truth-warning span{color:var(--fg2);font-size:11px}
.truth-grid{display:grid;grid-template-columns:repeat(4,minmax(150px,1fr));gap:8px;padding:0 14px 14px}.truth-stat{background:var(--panel2);border:1px solid var(--line);border-radius:5px;padding:10px;display:flex;flex-direction:column;gap:5px}.truth-stat span,.subhead{font:600 10px var(--mono);letter-spacing:.07em;text-transform:uppercase;color:var(--dim)}.truth-stat b{font:600 22px var(--mono)}.truth-stat small{color:var(--dim)}
.phase-roadmap,.subsection{border-top:1px solid var(--line);padding:11px 14px}.phase-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:7px;margin-top:8px}.phase-card{border:1px solid var(--line);border-radius:4px;padding:8px;background:var(--panel2)}.phase-card.phase-active{border-color:rgba(88,166,255,.65)}.phase-card>div:first-child{display:flex;justify-content:space-between}.phase-card small{color:var(--dim)}
.table-scroll{overflow-x:auto;margin:8px -14px -11px}
.overview-grid{display:grid;grid-template-columns:minmax(280px,1.4fr) repeat(3,minmax(150px,1fr));gap:8px;padding:12px}
.overview-hero,.overview-stat{background:var(--panel2);border:1px solid var(--line);border-radius:5px;padding:11px}
.overview-phase{font:600 21px var(--mono);color:var(--run);margin:6px 0 8px;overflow-wrap:anywhere}
.overview-hero small{display:block;margin-top:7px;color:var(--dim);font-size:10px}
.overview-stat{display:flex;flex-direction:column;gap:6px}.overview-stat span{font:600 10px var(--mono);letter-spacing:.07em;text-transform:uppercase;color:var(--dim)}
.overview-stat>b{font:600 22px var(--mono);color:var(--fg)}.overview-stat small{font-size:10px;color:var(--dim)}
.workload-strip{display:flex;gap:8px;flex-wrap:wrap;padding:0 12px 12px}.workload-strip span{font:11px var(--mono);padding:5px 8px;border:1px solid var(--line2);border-radius:4px;color:var(--fg2)}.workload-strip b{color:var(--fg)}
.issues{border-top:1px solid var(--line);padding:10px 12px 12px}.issues-title{font:600 10px var(--mono);letter-spacing:.08em;color:var(--retry);margin-bottom:6px}.issues ul{list-style:none;margin:0;padding:0;display:grid;gap:5px}.issues li{display:grid;grid-template-columns:46px 170px minmax(0,1fr);gap:8px;align-items:baseline;font-size:11px}.issues li b{font:600 10px var(--mono);color:var(--fg2);overflow-wrap:anywhere}.issues li span:last-child{color:var(--fg2);overflow-wrap:anywhere}.issue-sev{font:600 9px var(--mono)}
@media (max-width:1100px){.runtime-grid{grid-template-columns:1fr 1fr}.runtime-hero{grid-column:1/-1}.overview-grid{grid-template-columns:1fr 1fr}.overview-hero{grid-column:1/-1}.truth-grid{grid-template-columns:1fr 1fr}}
@media (max-width:640px){.runtime-grid{grid-template-columns:1fr}.runtime-hero{grid-column:auto}.overview-grid{grid-template-columns:1fr}.overview-hero{grid-column:auto}.issues li{grid-template-columns:42px 1fr}.issues li span:last-child{grid-column:2}.truth-head{grid-template-columns:1fr}.truth-grid{grid-template-columns:1fr}}
/* pipeline */
.pipe{list-style:none;margin:0;padding:12px;display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:6px}
.step{position:relative;background:var(--panel2);border:1px solid var(--line);border-radius:4px;padding:10px 10px 9px;min-width:0}
.step .bar{position:absolute;left:0;right:0;top:0;height:3px;border-radius:4px 4px 0 0;background:var(--pend);opacity:.35}
.st-top{display:flex;justify-content:space-between;align-items:center;gap:6px}
.code{font-size:15px;font-weight:600}
.st-name{font:12px var(--mono);color:var(--fg2);margin-top:3px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.st-sub{font:11px var(--mono);color:var(--dim);margin-top:2px}
.s-done .bar{background:var(--pass);opacity:1} .s-done .code{color:var(--pass)}
.s-run .bar{background:var(--run);opacity:1} .s-run{border-color:rgba(88,166,255,.45)}
.s-retry .bar{background:var(--retry);opacity:1} .s-retry{border-color:rgba(210,153,34,.5);background:rgba(210,153,34,.05)}
.s-retry .st-sub{color:var(--retry)}
.s-stall .bar{background:var(--fail);opacity:1} .s-stall{border-color:rgba(248,81,73,.5)}
.s-pend{opacity:.62}
.s-run .bar,.s-retry .bar{animation:pulse 2.4s infinite}
.tag{font:600 9.5px/1 var(--mono);letter-spacing:.07em;text-transform:uppercase;padding:3px 5px;border-radius:3px;white-space:nowrap}
.t-done,.t-pass{color:var(--pass);background:rgba(63,185,80,.12)}
.t-run{color:var(--run);background:rgba(88,166,255,.12)}
.t-retry{color:var(--retry);background:rgba(210,153,34,.14)}
.t-fail,.t-stall{color:var(--fail);background:rgba(248,81,73,.12)}
.t-pend{color:var(--pend);background:rgba(110,118,129,.14)}
/* proofs */
.proofs{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:6px;padding:12px}
.proof{background:var(--panel2);border:1px solid var(--line);border-left:3px solid var(--pend);border-radius:4px;padding:8px 9px;min-width:0;cursor:default}
.pr-top{display:flex;align-items:center;gap:8px}
.pr-top b{font:600 13px var(--mono)} .pr-top .num{font-size:12px;color:var(--fg2)} .pr-top .tag{margin-left:auto}
.meter{height:4px;background:var(--line);border-radius:2px;margin:7px 0 6px;overflow:hidden}
.meter i{display:block;height:100%;background:var(--pend)}
.pr-t{font-size:11px;color:var(--fg2);line-height:1.3;height:2.6em;overflow:hidden;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}
.pr-m{font:10.5px var(--mono);color:var(--dim);margin-top:4px}
.p-pass{border-left-color:var(--pass)} .p-pass .meter i{background:var(--pass)}
.p-fail{border-left-color:var(--fail)} .p-fail .meter i{background:var(--retry)}
.p-none{opacity:.55;border-style:dashed;border-left-style:solid}
/* tables */
.grid2{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.25fr);gap:14px}
table{width:100%;border-collapse:collapse;font-size:12px}
th{font:600 10px var(--sans);letter-spacing:.07em;text-transform:uppercase;color:var(--dim);text-align:left;padding:7px 12px;border-bottom:1px solid var(--line)}
th.r{text-align:right}
td{padding:7px 12px;border-bottom:1px solid var(--line);vertical-align:top}
tr:last-child td{border-bottom:0}
tbody tr:hover td{background:rgba(255,255,255,.02)}
.dot{display:inline-block;width:7px;height:7px;border-radius:50%;margin-right:8px;vertical-align:1px}
.d-run{background:var(--run);box-shadow:0 0 0 3px rgba(88,166,255,.15)} .d-idle{background:var(--line2)}
.hbar,.split{height:3px;background:var(--line);border-radius:2px;margin-top:5px;overflow:hidden;display:flex;margin-left:auto;max-width:120px}
.hbar i{background:var(--run);opacity:.7}
.split i.ok{background:var(--pass)} .split i.bad{background:var(--fail)}
.cmd{font-size:11.5px;color:var(--fg2);max-width:0;width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.kind{font:600 10px var(--mono);text-transform:uppercase;letter-spacing:.05em;color:var(--fg2)}
.k-runner,.k-controller{color:var(--pass)} .k-claude,.k-codex{color:var(--run)} .k-commissioning{color:var(--retry)}
.k-hermes,.k-worker{color:var(--run)}
.lane{font:600 10px var(--mono);text-transform:uppercase;padding:2px 5px;border-radius:3px;border:1px solid var(--line2)}
.l-free{color:var(--retry)} .l-strong{color:var(--pass)} .l-cheap,.l-local{color:var(--fg2)}
.chip{font:11px var(--mono);color:var(--fg2);border:1px solid var(--line2);border-radius:3px;padding:2px 7px}
.chip.c-retry{color:var(--retry);border-color:rgba(210,153,34,.45)} .chip.c-fail{color:var(--fail);border-color:rgba(248,81,73,.45)}
.trend{display:flex;align-items:flex-end;gap:2px;height:44px;padding:0 12px;margin-top:12px}
.trend span{flex:1;height:100%;display:flex;flex-direction:column;justify-content:flex-end;background:rgba(255,255,255,.015)}
.trend i{display:block;width:100%} .trend i.ok{background:var(--pass);opacity:.75} .trend i.bad{background:var(--fail)}
.axis{display:flex;justify-content:space-between;font:10px var(--mono);color:var(--dim);padding:4px 12px 10px;border-bottom:1px solid var(--line)}
.note{font-size:11px;color:var(--dim);padding:8px 12px;border-top:1px solid var(--line)}
.warn{color:var(--retry)}
/* activity and visual hierarchy */
.activity-panel{border-color:rgba(88,166,255,.42);box-shadow:0 8px 30px rgba(0,0,0,.16)}
.activity-layout{display:grid;grid-template-columns:minmax(280px,.8fr) minmax(0,1.5fr);gap:0}
.activity-summary{padding:18px;border-right:1px solid var(--line);background:linear-gradient(145deg,rgba(88,166,255,.08),transparent 65%)}
.activity-kicker{font:600 10px var(--mono);letter-spacing:.1em;color:var(--dim)}
.activity-big{font:600 42px/1 var(--mono);color:var(--run);margin:9px 0}.activity-big span{font:12px var(--sans);font-weight:400;color:var(--fg2)}
.activity-summary p{font-size:12px;color:var(--fg2);line-height:1.7;margin:10px 0 16px}.activity-summary p b{color:var(--fg);font-family:var(--mono)}
.activity-bar{height:7px;background:var(--line);border-radius:8px;overflow:hidden}.activity-bar i{display:block;height:100%;background:linear-gradient(90deg,var(--run),#8b5cf6);border-radius:8px}
.activity-callout{display:flex;flex-direction:column;gap:4px;padding:10px 11px;border:1px solid rgba(63,185,80,.35);border-radius:7px;background:rgba(63,185,80,.06);font-size:11px;color:var(--fg2)}
.activity-callout b{color:var(--pass);font-family:var(--mono);font-size:11px}.activity-callout.callout-warn{border-color:rgba(210,153,34,.5);background:rgba(210,153,34,.07)}.activity-callout.callout-warn b{color:var(--retry)}
.activity-legend{display:flex;gap:12px;flex-wrap:wrap;margin-top:16px;color:var(--dim);font:10px var(--mono)}.activity-legend span{display:flex;align-items:center;gap:5px}.activity-legend b{color:var(--fg)}
.activity-feed{list-style:none;margin:0;padding:10px 14px;max-height:330px;overflow:auto}.activity-item{display:grid;grid-template-columns:9px minmax(0,1fr) auto;gap:9px;align-items:start;padding:9px 3px;border-bottom:1px solid rgba(45,51,59,.7)}.activity-item:last-child{border-bottom:0}.activity-item b{display:block;font:600 11px var(--mono);color:var(--fg)}.activity-item span:not(.activity-dot){display:block;margin-top:2px;font-size:11px;color:var(--fg2);overflow-wrap:anywhere}.activity-item time{font:10px var(--mono);color:var(--dim);white-space:nowrap}.activity-dot{display:inline-block;width:8px;height:8px;border-radius:50%;margin-top:4px;background:var(--dim);flex:none}.a-run{background:var(--run);box-shadow:0 0 0 3px rgba(88,166,255,.13)}.a-pass{background:var(--pass)}.a-fail{background:var(--fail)}.a-info{background:var(--retry)}.activity-empty{padding:25px;color:var(--dim);font:11px var(--mono)}
.bot-office{overflow:hidden;border-color:rgba(210,153,34,.42);box-shadow:0 8px 30px rgba(0,0,0,.2)}
.office-scene{position:relative;min-height:590px;background:#172238 url('/assets/office/industrial-steam-office.png') center/cover no-repeat;overflow:hidden;isolation:isolate}
.office-scene:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(4,10,22,.08),rgba(4,10,22,.2));pointer-events:none;z-index:0}
.office-sign{position:absolute;top:16px;left:24px;z-index:2;color:#ffd166;font:700 12px var(--mono);letter-spacing:.14em;text-shadow:0 2px 8px #000}.office-sign span{color:#fff;display:block;font-size:10px;margin-top:3px;letter-spacing:.22em}
.office-grid{position:absolute;inset:44% 16% 9%;background:repeating-linear-gradient(0deg,rgba(255,255,255,.15) 0 1px,transparent 1px 48px),repeating-linear-gradient(90deg,rgba(255,255,255,.12) 0 1px,transparent 1px 48px);transform:perspective(420px) rotateX(58deg);transform-origin:center bottom;opacity:.48;z-index:1}
.office-bot{position:absolute;width:150px;height:250px;z-index:2;filter:drop-shadow(0 10px 7px rgba(0,0,0,.32));animation:bot-float 4s ease-in-out infinite}
.robot-figure{position:absolute;top:0;left:0;width:150px;height:205px;object-fit:contain;mix-blend-mode:multiply}.bot-shadow{position:absolute;bottom:26px;left:20px;width:110px;height:18px;border-radius:50%;background:rgba(0,0,0,.35);filter:blur(6px)}
.bot-plate{position:absolute;bottom:0;left:4px;right:4px;padding:6px 8px;border:1px solid rgba(255,209,102,.38);border-radius:6px;background:rgba(8,13,22,.84);box-shadow:0 3px 10px rgba(0,0,0,.24);font:10px var(--mono)}.bot-plate b{display:block;color:#ffd166;letter-spacing:.09em}.bot-plate span,.bot-plate small{display:block;color:#d7dde4;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.bot-plate small{color:#8fa1b8;margin-top:2px}.state-working .bot-plate{border-color:rgba(88,166,255,.7)}.state-working .bot-plate b:before{content:"● ";color:#58a6ff}.state-standby{opacity:.82}.state-standby .bot-plate b:before{content:"○ ";color:#6e7681}
.bot-1{left:8%;top:27%;animation-delay:-.2s}.bot-2{left:27%;top:15%;animation-delay:-1.1s}.bot-3{left:45%;top:30%;animation-delay:-2.3s}.bot-4{right:7%;top:21%;animation-delay:-.8s}.bot-5{left:17%;bottom:5%;transform:scale(.84);animation-delay:-1.7s}.bot-6{left:37%;bottom:1%;transform:scale(.9);animation-delay:-2.8s}.bot-7{right:19%;bottom:4%;transform:scale(.82);animation-delay:-.5s}.bot-8{right:1%;bottom:1%;transform:scale(.72);animation-delay:-3.1s}
@keyframes bot-float{50%{translate:0 -5px}}
.panel{border-radius:10px;box-shadow:0 4px 18px rgba(0,0,0,.10)}.ph{padding:12px 15px}.ph h2{letter-spacing:.1em}.health{border-radius:10px;padding:11px 15px;background:linear-gradient(90deg,rgba(88,166,255,.07),rgba(139,92,246,.04))}
@media (max-width:850px){.activity-layout{grid-template-columns:1fr}.activity-summary{border-right:0;border-bottom:1px solid var(--line)}.activity-feed{max-height:280px}}
@media (max-width:1100px){.pipe{grid-template-columns:repeat(4,minmax(0,1fr))}.proofs{grid-template-columns:repeat(4,minmax(0,1fr))}.grid2{grid-template-columns:1fr}}
@media (max-width:640px){header,main{padding-left:10px;padding-right:10px}.pipe{grid-template-columns:1fr 1fr}.proofs{grid-template-columns:1fr 1fr}td,th{padding:6px 8px}.hide-s{display:none}}
"""

JS = """
const b = document.getElementById("refresh");
b.addEventListener("click", async () => {
  b.disabled = true; b.textContent = "REFRESHING\\u2026";
  try {
    const r = await fetch("/api/refresh", {method: "POST"});
    const j = await r.json();
    if (!j.ok) throw new Error(j.error || "build failed");
    location.reload();
  } catch (e) {
    b.disabled = false; b.textContent = "OFFLINE";
    b.title = "refresh server not reachable at " + location.host +
              " \\u2014 run tracker_serve.py (port 8790), or use file:// which only "
              + "updates every 3 min via the heartbeat";
    setTimeout(() => { b.textContent = "\\u27f3 REFRESH"; }, 2500);
  }
});
// age of this snapshot, ticking client-side from the build stamp
const el = document.getElementById("age"), built = +el.dataset.built;
function tick() {
  const d = Math.max(0, Date.now() / 1000 - built);
  el.textContent = d < 60 ? Math.floor(d) + "s ago" : d < 3600 ? Math.floor(d / 60) + "m ago"
                 : (d / 3600).toFixed(1) + "h ago";
  el.className = d > 300 ? "stale" : "";
}
tick(); setInterval(tick, 1000);
"""


def main():
    now = NOW                       # read the module global at call time (server reassigns it)
    lr.NOW = now
    ts = time.strftime("%H:%M:%S UTC", time.gmtime(now))
    date = time.strftime("%Y-%m-%d", time.gmtime(now))

    st, st_err = load_state()
    ps = parse_procs(lr.procs())
    runner_up = any(p["kind"] == "runner" for p in ps)
    ctl_up = any(p["kind"] == "controller" for p in ps)
    workers = sum(1 for p in ps if p["kind"] in ("claude", "codex", "freellm"))

    pipe_html, active = render_pipeline(st, runner_up)
    proofs, blocked = load_proofs()
    proofs_html = render_proofs(proofs)
    n_run = sum(1 for p in proofs.values() if p is not None)
    n_pass = sum(1 for p in proofs.values() if p and p.get("passed") is True)
    n_checks_ok = sum(p.get("ok", 0) for p in proofs.values() if p)
    n_checks = sum(p.get("n", 0) for p in proofs.values() if p)

    cli = tt.collect_agents()
    dba = tt.collect_db_attempts(tt.BUILD_DBS)
    dlg = tt.collect_delegations(now)
    agents = merge_agents(cli, dba, dlg)
    office_html = render_bot_office(agents)
    conc = tt.record_concurrency(cli + dba + dlg, SAMPLES, now)
    free_runtime = load_free_runtime(ps, conc)
    free_runtime_html = render_free_runtime(free_runtime, conc)
    prog = tt.load_project_progress(tt.BUILD_DB)
    prog_html, prog_frac = render_progress(prog)
    snapshot = tt.load_delivery_snapshot(tt.BUILD_DB, now)
    product_status = tt.derive_product_status(snapshot, ctl_up)
    product_html = render_product_dashboard(snapshot, product_status, len(st.get("done") or []) == len(STEPS))
    workload = load_workload(free_runtime, st, proofs, prog, now, snapshot)
    transparency_html = render_transparency(workload)
    activity_html = render_activity(load_activity(free_runtime, now), workload, free_runtime)
    agent_rows, agent_meta = render_agents(agents)
    if isinstance(agent_meta, tuple):
        _n_agents, agent_srcs, agent_kinds = agent_meta
    else:
        agent_srcs, agent_kinds = [], []
    agent_src_txt = esc(", ".join(agent_srcs)) if agent_srcs else "none"
    sub_rows, sub_hot, sub_n = render_sub_lanes(lr.claude_usage(), lr.codex_usage(), now)
    sh = load_shield(now)
    free_rows, trend, strong, free_hot = render_free(sh, now)
    cooldowns = render_cooldowns(st, now) if st else '<span class="chip">state <b class="dim">unknown</b></span>'
    commits = list(lr.commits())

    # health summary line — every figure below is derived from the collectors above
    done_n = len(st.get("done") or [])
    if st_err:
        step_txt = f'<span class="warn">{esc(st_err)}</span>'
    elif active is None:
        step_txt = '<b class="c-pass">bootstrap complete</b>'
    else:
        f = (st.get("fails") or {}).get(active, 0)
        step_txt = (f'<b>{esc(active.split("-")[0])}</b> '
                    + (f'<span class="c-retry">retry {f}</span>' if f else '<span class="c-run">running</span>'))
    health = "".join(f"<span>{x}</span>" for x in (
        f'product <b class="{"c-pass" if product_status["complete"] else "c-run"}">{esc(product_status["label"])}</b>',
        step_txt,
        f'steps <b>{done_n}/{len(STEPS)}</b>',
        f'proofs <b>{n_pass}/{len(PROOFS)}</b> pass <span class="dim">({n_run} run)</span>',
        f'lanes <b>{sub_hot + free_hot}</b> hot',
        f'sub-agents <b>{len(agents)}</b> live <span class="dim">{agent_src_txt}</span>',
        f'items integrated <b>{prog_frac}</b>',
        f'bootstrap owner <b class="{"c-pass" if runner_up or active is None else "c-fail"}">{"runner active" if runner_up else "handed off" if active is None else "runner down"}</b>',
        f'controller <b class="{"c-pass" if ctl_up else "c-fail"}">{"up" if ctl_up else "down"}</b>',
    ))
    live = ctl_up or runner_up or workers > 0 or bool(agents)
    badge = '<span class="badge b-live">live</span>' if live else '<span class="badge b-idle">idle</span>'
    # STALL freshness is tied to the timestamp inside each alert, not the
    # heartbeat file mtime (ordinary fresh heartbeat writes must not revive it).
    stall_txt, stall_note = "", ""
    try:
        stall_txt = latest_fresh_stall(
            os.path.expanduser("~/.local/state/empirium-build/heartbeat.log"), now
        ) or ""
        if stall_txt:
            stall_note = f'<div class="note warn">&#9888; {esc(stall_txt)}</div>'
    except OSError:
        pass
    blocked_note = ('<div class="note warn">BLOCKED.md present in evidence dir — a worker recorded a blocking '
                    'condition; see .build/evidence/commissioning/BLOCKED.md</div>') if blocked else ""
    strong_txt = (f'pinned strong tier: {strong["ok"]} ok / {strong["bad"]} fail'
                  if lr.STRONG_TIER else "pinned strong tier: unknown (freellm_shield not importable)")

    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="refresh" content="60">
<title>{esc(product_status["label"])} · Empirium Studio v2</title>
<style>{CSS}</style></head><body>
<header>
  <div class="brand">Empirium Studio v2 <span>/ Star Force monitor</span></div>
  {'<span class="badge b-live" style="background:#f85149">STALL</span>' if stall_txt else badge}
  <div class="stamp">built <span class="num">{esc(ts)}</span> <span class="dim">{esc(date)}</span> · <span id="age" data-built="{now:.0f}"></span></div>
  <div class="spacer"></div>
  <button id="refresh" title="re-collect every stat from live evidence now">&#10227; REFRESH</button>
</header>
<main>
<div class="health">{health}</div>
{office_html}
{product_html}
{activity_html}
{free_runtime_html}
{transparency_html}
{stall_note}

<section class="panel">
  <div class="ph"><h2>Bootstrap pipeline</h2><span class="meta">bootstrap.json · {done_n} done</span>
    <div class="right">{cooldowns}</div></div>
  <ol class="pipe">{pipe_html}</ol>
  {prog_html}
</section>

<section class="panel">
  <div class="ph"><h2>Commissioning proofs</h2>
    <span class="meta">{n_pass} pass · {n_run - n_pass} not passing · {len(PROOFS) - n_run} not run · checks {n_checks_ok}/{n_checks}</span></div>
  <div class="proofs">{proofs_html}</div>{blocked_note}
</section>

<div class="grid2">
<section class="panel">
  <div class="ph"><h2>Subscription lanes</h2><span class="meta">12 h · {sub_hot}/{sub_n} hot (&lt;15 m)</span></div>
  <table><thead><tr><th>model</th><th class="r">tokens</th><th class="r">calls</th><th class="r">last</th></tr></thead>
  <tbody>{sub_rows}</tbody></table>
  <div class="note">measured from CLI session logs; vendor dashboards lag by minutes</div>
</section>

<section class="panel">
  <div class="ph"><h2>Free lane · shield</h2><span class="meta">{FREE_H} h · {free_hot} hot · {esc(strong_txt)}</span></div>
  {trend}
  <table><thead><tr><th>model</th><th class="r">ok / fail</th><th class="r hide-s">avg ok</th><th>last error</th><th class="r">last</th></tr></thead>
  <tbody>{free_rows}</tbody></table>
  <div class="note">strong-tier failures are expected; the ladder falls through to the next model</div>
</section>
</div>

<section class="panel">
  <div class="ph"><h2>Current sub-agents</h2><span class="meta">{len(agents)} live · hermes delegation registry + controller attempts + process scan</span></div>
  <table><thead><tr><th>kind</th><th>lane</th><th>model</th><th>item</th><th class="r">running</th><th>source</th><th>goal / command</th></tr></thead>
  <tbody>{agent_rows}</tbody></table>
  <div class="note">FreeLLMAPI concurrency observed: <b class="num">{conc["current_free"]}</b> now · peak <b class="num">{conc["peak_free"]}</b> across <span class="num">{conc["samples"]}</span> builds (7-day retention)</div>
</section>

<section class="panel">
  <div class="ph"><h2>Processes</h2><span class="meta">{len(ps)} matching ps entries</span></div>
  <table><thead><tr><th>kind</th><th class="r">pid</th><th class="r">up</th><th>command</th></tr></thead>
  <tbody>{render_procs(ps)}</tbody></table>
</section>

<section class="panel">
  <div class="ph"><h2>Recent commits</h2></div>
  <table><thead><tr><th>repo</th><th>hash</th><th>subject</th><th class="r">age</th></tr></thead>
  <tbody>{render_commits(commits)}</tbody></table>
</section>
</main>
<script>{JS}</script>
</body></html>"""
    with open(OUT, "w") as f:
        f.write(doc)
    print(f"wrote {OUT} ({len(doc)} bytes) at {ts}")


if __name__ == "__main__":
    main()
