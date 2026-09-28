#!/usr/bin/env python3
"""Build tracker.html from live evidence only. No hardcoded numbers.

Reads: shield DB (free lane, per model), Claude session files (Sonnet/Opus tokens),
Codex session files (Luna tokens), process table, git log, runner state.
Any source that is unavailable renders as 'unknown' rather than a made-up figure.
"""
import html, json, os, subprocess, time
import lane_report as lr

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tracker.html")
NOW = time.time()


def esc(x):
    return html.escape(str(x))


def section(title, rows, note=""):
    body = "".join(rows) if rows else '<tr><td colspan="4" class="dim">no data</td></tr>'
    n = f'<div class="note">{esc(note)}</div>' if note else ""
    return f'<section><h2>{esc(title)}</h2>{n}<table>{head()}{body}</table></section>'


def head():
    return "<tr><th>count</th><th>state</th><th>model / lane</th><th>last</th></tr>"


def main():
    ts = time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime(NOW))

    # --- subscription lanes -------------------------------------------------
    cu = lr.claude_usage()
    xu = lr.codex_usage()
    rows = []
    for name, tbl in (("claude", cu), ("codex", xu)):
        for m, e in sorted(tbl.items(), key=lambda kv: -kv[1]["tok"]):
            if m == "<synthetic>":
                continue
            n = e.get("calls") or e.get("sessions") or 0
            rows.append(f'<tr><td>{n}</td><td>{esc(name)}</td><td>{esc(m)}</td>'
                        f'<td>{esc(lr.human_ago(e["last"]))}</td></tr>')
    sub = section("Subscription lanes (measured from CLI session logs)", rows,
                  "tokens are real usage; meters on the vendor dashboards lag these by minutes")

    # --- free lane ----------------------------------------------------------
    rows, strong = [], {"ok": 0, "fail": 0}
    db = os.path.expanduser("~/.local/state/freellm-shield/shield.db")
    if os.path.exists(db):
        import sqlite3
        c = sqlite3.connect(db); c.row_factory = sqlite3.Row
        agg = {}
        for r in c.execute("select model,outcome,count(*) n,max(ts) last from tries "
                           "where ts>? group by model,outcome", (NOW - 6 * 3600,)):
            e = agg.setdefault(r["model"], {"ok": 0, "bad": 0, "last": 0, "lastbad": ""})
            if r["outcome"] in ("OK", "PROBE_OK"):
                e["ok"] += r["n"]
            else:
                e["bad"] += r["n"]; e["lastbad"] = r["outcome"]
            e["last"] = max(e["last"], r["last"])
        for m, e in sorted(agg.items(), key=lambda kv: -(kv[1]["ok"] + kv[1]["bad"])):
            tier = "PINNED strong" if m in lr.STRONG_TIER else "reliable"
            st = "OK" if e["bad"] == 0 else f"{e['lastbad']} x{e['bad']}"
            if m in lr.STRONG_TIER:
                strong["ok"] += e["ok"]; strong["fail"] += e["bad"]
            rows.append(f'<tr><td>{e["ok"]}ok/{e["bad"]}fail</td><td>{esc(tier)}</td>'
                        f'<td>{esc(m)}</td><td>{esc(st)} · {esc(lr.human_ago(e["last"]))}</td></tr>')
    free = section("Free lane via shield (last 6 h)", rows,
                   f"pinned strong tier: {strong['ok']} ok / {strong['fail']} failed — "
                   "failures are expected by design; the ladder falls through to the next model")

    # --- runner + processes -------------------------------------------------
    st = json.load(open(os.path.expanduser("~/.local/state/empirium-build/bootstrap.json"))) \
        if os.path.exists(os.path.expanduser("~/.local/state/empirium-build/bootstrap.json")) else {}
    rows = []
    for sid, n in (st.get("fails") or {}).items():
        rows.append(f'<tr><td>{n}</td><td>step</td><td>{esc(sid)}</td><td>failing</td></tr>')
    rows.append(f'<tr><td>{len(st.get("done") or [])}</td><td>done</td>'
                f'<td>{esc(", ".join(st.get("done") or []) or "-")}</td><td></td></tr>')
    procs = section("Live processes / steps", rows,
                    "\n".join(lr.procs()[:6]) or "none")

    # --- commits ------------------------------------------------------------
    rows = [f'<tr><td></td><td>{esc(repo)}</td><td>{esc(h)} {esc(s[:60])}</td>'
            f'<td>{esc(when)}</td></tr>' for repo, h, s, when in lr.commits()]
    git = section("Recent commits", rows)

    doc = f"""<!doctype html><html><head><meta charset="utf-8">
<meta http-equiv="refresh" content="60">
<style>
:root {{ color-scheme: dark; }}
body {{ font: 13px/1.45 ui-monospace, monospace; padding: 10px; }}
h1 {{ font-size: 15px; margin: 0 0 4px; }}
h2 {{ font-size: 13px; margin: 18px 0 6px; color: var(--accent, #7aa2f7); }}
.note {{ color: var(--muted-foreground, #888); font-size: 11px; margin-bottom: 6px;
        white-space: pre-wrap; }}
table {{ border-collapse: collapse; width: 100%; }}
th, td {{ text-align: left; padding: 3px 8px 3px 0; border-bottom: 1px solid var(--border, #333);
         vertical-align: top; }}
th {{ color: var(--muted-foreground, #999); font-weight: 500; font-size: 11px; }}
.dim {{ color: var(--muted-foreground, #777); }}
.stamp {{ color: var(--muted-foreground, #888); font-size: 11px; }}
</style></head><body>
<h1>Empirium build tracker — regenerated from live data every 60 s</h1>
<div class="stamp">built {esc(ts)} · this file is written by tracker_build.py, not hand-edited</div>
{sub}{free}{procs}{git}
</body></html>"""
    open(OUT, "w").write(doc)
    print(f"wrote {OUT} ({len(doc)} bytes) at {ts}")


if __name__ == "__main__":
    main()
