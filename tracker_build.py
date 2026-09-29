#!/usr/bin/env python3
"""Build tracker.html from live evidence only. No hardcoded numbers.

Reads: bootstrap runner state, commissioning evidence (C1-C12 JSON), Claude session files
(Sonnet/Opus tokens), Codex session files (Luna tokens), shield DB (free lane, per model),
process table, git log. Any source that is unavailable renders as 'unknown' / 'not run'
rather than a made-up figure.

Contract (tracker_serve.py): module globals NOW, OUT, esc(); main() stamps from the
module-level NOW at call time.
"""
import glob, html, json, os, sqlite3, time
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
@media (max-width:1100px){.pipe{grid-template-columns:repeat(4,minmax(0,1fr))}.proofs{grid-template-columns:repeat(4,minmax(0,1fr))}.grid2{grid-template-columns:1fr}}
@media (max-width:640px){header,main{padding-left:10px;padding-right:10px}
 .pipe{grid-template-columns:1fr 1fr}.proofs{grid-template-columns:1fr 1fr}
 td,th{padding:6px 8px}.hide-s{display:none}}
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
    conc = tt.record_concurrency(cli + dba + dlg, SAMPLES, now)
    prog = tt.load_project_progress([tt.BUILD_DB, FIX_DB])
    prog_html, prog_frac = render_progress(prog)
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
        step_txt,
        f'steps <b>{done_n}/{len(STEPS)}</b>',
        f'proofs <b>{n_pass}/{len(PROOFS)}</b> pass <span class="dim">({n_run} run)</span>',
        f'lanes <b>{sub_hot + free_hot}</b> hot',
        f'sub-agents <b>{len(agents)}</b> live <span class="dim">{agent_src_txt}</span>',
        f'items integrated <b>{prog_frac}</b>',
        f'runner <b class="{"c-pass" if runner_up else "c-fail"}">{"up" if runner_up else "down"}</b>',
        f'controller <b class="{"c-pass" if ctl_up else "c-fail"}">{"up" if ctl_up else "down"}</b>',
    ))
    live = runner_up or workers > 0
    badge = '<span class="badge b-live">live</span>' if live else '<span class="badge b-idle">idle</span>'
    # stall alerts are written by the cron heartbeat watchdog; surface them here
    stall_txt, stall_note = "", ""
    try:
        import pathlib
        lines = [l for l in pathlib.Path(os.path.expanduser(
            "~/.local/state/empirium-build/heartbeat.log")).read_text().splitlines()
                 if "STALL ALERT" in l and now - os.path.getmtime(
            os.path.expanduser("~/.local/state/empirium-build/heartbeat.log")) < 3 * 3600]
        if lines:
            stall_txt = lines[-1]
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
<title>{esc(active.split("-")[0] if active else "done")} · Empirium monitor</title>
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
