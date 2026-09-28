#!/usr/bin/env python3
"""Report real subscription + free-lane usage from on-disk evidence (no made-up numbers)."""
import glob, json, os, re, sqlite3, subprocess, time

try:  # single source of truth for the pinned ladder lives in the shield
    from freellm_shield import STRONG_TIER
except Exception:
    STRONG_TIER = []

HOME = os.path.expanduser("~")
NOW = time.time()


def human_ago(t):
    d = NOW - t
    if d < 0:
        return "now"
    for unit, size in (("h", 3600), ("m", 60), ("s", 1)):
        pass
    if d >= 3600:
        return f"{d/3600:.1f}h ago"
    if d >= 60:
        return f"{d/60:.0f}m ago"
    return f"{d:.0f}s ago"


def claude_usage():
    """Tokens per model from Claude Code project session files."""
    out = {}
    files = glob.glob(f"{HOME}/.claude/projects/**/*.jsonl", recursive=True)
    for path in files:
        try:
            mtime = os.path.getmtime(path)
        except OSError:
            continue
        if NOW - mtime > 12 * 3600:
            continue
        try:
            with open(path) as f:
                for line in f:
                    if '"usage"' not in line:
                        continue
                    try:
                        j = json.loads(line)
                    except Exception:
                        continue
                    msg = j.get("message") or {}
                    model = msg.get("model")
                    u = msg.get("usage") or {}
                    if not model or not u:
                        continue
                    tot = (u.get("input_tokens", 0) + u.get("output_tokens", 0)
                           + u.get("cache_read_input_tokens", 0)
                           + u.get("cache_creation_input_tokens", 0))
                    e = out.setdefault(model, {"tok": 0, "last": 0, "calls": 0})
                    e["tok"] += tot
                    e["calls"] += 1
                    e["last"] = max(e["last"], mtime)
        except OSError:
            pass
    return out


def codex_usage():
    """Tokens from Codex rollout session files (Luna lane)."""
    out = {}
    files = glob.glob(f"{HOME}/.local/state/empirium-build/codex-sub/sessions/**/*.jsonl",
                      recursive=True)
    for path in files:
        mtime = os.path.getmtime(path)
        if NOW - mtime > 12 * 3600:
            continue
        model = None
        turn_toks = []          # per-turn totals; a session's usage = sum of its turns
        turns = 0
        try:
            with open(path) as f:
                for line in f:
                    # Codex rollouts record usage as {"type":"token_usage_record",
                    # "payload":{"usage":{"total_tokens":N,...}}} and the model in
                    # turn_context/token_usage_record lines. The old "tokens used"
                    # string format never appears — that's why Luna showed nothing.
                    if '"token_usage_record"' not in line and '"turn_context"' not in line:
                        continue
                    try:
                        j = json.loads(line)
                    except Exception:
                        continue
                    p = j.get("payload") if isinstance(j.get("payload"), dict) else {}
                    if p.get("model"):
                        model = p["model"]
                    elif j.get("model"):
                        model = j["model"]
                    u = p.get("usage") if isinstance(p.get("usage"), dict) else None
                    if j.get("type") == "token_usage_record" and u:
                        turn_toks.append(int(u.get("total_tokens") or 0))
                        turns += 1
        except OSError:
            pass
        if model and turn_toks:
            e = out.setdefault(model, {"tok": 0, "last": 0, "sessions": 0, "calls": 0})
            e["tok"] += sum(turn_toks)
            e["calls"] += turns
            e["last"] = max(e["last"], mtime)
            e["sessions"] += 1
    return out


def shield_stats():
    db = f"{HOME}/.local/state/freellm-shield/shield.db"
    if not os.path.exists(db):
        return None
    c = sqlite3.connect(db)
    c.row_factory = sqlite3.Row
    total = c.execute("select count(*) n from tries").fetchone()["n"]
    since = c.execute("select count(*) n from tries where ts>?", (NOW - 3600,)).fetchone()["n"]
    per = c.execute("select model,outcome,count(*) n from tries group by model,outcome "
                    "order by n desc limit 12").fetchall()
    return {"total": total, "last_hour": since,
            "per": [(r["model"], r["outcome"], r["n"]) for r in per]}


def procs():
    try:
        r = subprocess.run(["ps", "-eo", "pid,etimes,cmd"], capture_output=True, text=True, timeout=10)
    except Exception:
        return []
    keep = []
    for line in r.stdout.splitlines()[1:]:
        if re.search(r"claude -p|codex exec|bootstrap_runner|freellm_shield|controller\.py run|run_commissioning", line):
            keep.append(line.strip()[:160])
    return keep


def commits():
    for repo in (f"{HOME}/empirium-studio-v2", f"{HOME}/work/starforce-plan"):
        try:
            r = subprocess.run(["git", "-C", repo, "log", "-3", "--format=%ct|%h|%s"],
                               capture_output=True, text=True, timeout=15)
            for line in r.stdout.splitlines():
                ts, h, s = line.split("|", 2)
                yield repo.split("/")[-1], h, s, human_ago(float(ts))
        except Exception:
            continue


if __name__ == "__main__":
    print(f"=== lane usage report @ {time.strftime('%H:%M:%S UTC', time.gmtime())} ===\n")
    print("CLAUDE subscription (sonnet/opus), last 12h:")
    cu = claude_usage()
    if not cu:
        print("  (no claude token records found)")
    for m, e in sorted(cu.items(), key=lambda kv: -kv[1]["tok"]):
        print(f"  {m:22s} {e['tok']:>12,} tok  {e['calls']:>4} calls  last {human_ago(e['last'])}")

    print("\nCODEX subscription (luna), last 12h:")
    xu = codex_usage()
    if not xu:
        print("  (no codex token records found)")
    for m, e in sorted(xu.items(), key=lambda kv: -kv[1]["tok"]):
        print(f"  {m:22s} {e['tok']:>12,} tok  {e['sessions']:>3} sessions  last {human_ago(e['last'])}")

    print("\nFREE lane via shield:")
    ss = shield_stats()
    if ss:
        print(f"  {ss['total']} tries total, {ss['last_hour']} in the last hour")
        for m, o, n in ss["per"]:
            print(f"    {n:>5}  {o:14s} {m}")

    print("\nlive processes:")
    for p in procs():
        print("  " + p)

    print("\nrecent commits:")
    for repo, h, s, when in commits():
        print(f"  {when:>10}  {repo}/{h}  {s[:70]}")
