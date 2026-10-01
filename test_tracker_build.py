from pathlib import Path
import sqlite3

import tracker_build as tb


def test_fresh_stall_uses_alert_timestamp_not_log_mtime(tmp_path):
    log = tmp_path / "heartbeat.log"
    log.write_text(
        "2026-09-29T23:12:01Z STALL ALERT: old failure\n"
        "2026-09-30T15:00:00Z ordinary healthy heartbeat\n"
    )
    now = 1790781000.0  # 2026-09-30T15:10:00Z
    assert tb.latest_fresh_stall(log, now, freshness_s=3 * 3600) is None


def test_recent_stall_is_renderable(tmp_path):
    log = tmp_path / "heartbeat.log"
    log.write_text("2026-09-30T15:05:00Z STALL ALERT: current failure\n")
    now = 1790781000.0
    assert tb.latest_fresh_stall(log, now, freshness_s=3 * 3600) == "2026-09-30T15:05:00Z STALL ALERT: current failure"


def test_malformed_stall_timestamp_is_ignored_safely(tmp_path):
    log = tmp_path / "heartbeat.log"
    log.write_text("not-a-time STALL ALERT: invalid\n")
    assert tb.latest_fresh_stall(log, 1790781000.0, freshness_s=3 * 3600) is None


def test_bot_office_has_one_robot_per_live_agent_and_no_standby_fakes():
    agents = [
        {"kind": "claude", "model": "model-a", "attempt_id": "call-a", "source": "db"},
        {"kind": "hermes", "model": "model-b", "item_id": "call-b", "source": "registry"},
    ]
    html = tb.render_bot_office(agents)
    assert html.count('class="office-bot state-working"') == 2
    assert "2 live calls" in html
    assert "standby" not in html
    assert "NO LIVE LLM CALLS" not in html


def test_shield_panel_uses_actual_shield_inflight_and_flags_stale_history():
    shield = {"models": {}, "buckets": [{"ok": 0, "bad": 0}], "since": 100.0, "latest": 100.0}

    html = tb.render_shield_panel(
        '<tr><td colspan="5">no completed attempts</td></tr>',
        "", "0 ok / 0 fail", 0, shield, active_upstream=10, now=4000.0,
    )

    assert "Shield lane attempts" in html
    assert "10 active upstream" in html
    assert "0 completed in the last 6 h" in html
    assert "completion history is stale" in html


def test_load_shield_health_sums_model_inflight(monkeypatch):
    class Response:
        status = 200
        def __enter__(self): return self
        def __exit__(self, *args): return None
        def read(self):
            return b'{"ok":true,"inflight":{"auto":7,"model-b":3},"breakers_s":{"auto":0}}'

    monkeypatch.setattr(tb.urllib.request, "urlopen", lambda *args, **kwargs: Response())

    health = tb.load_shield_health("http://127.0.0.1:3102")

    assert health["active_upstream"] == 10
    assert health["inflight"] == {"auto": 7, "model-b": 3}


def test_unavailable_shield_health_is_not_presented_as_zero(monkeypatch):
    monkeypatch.setattr(tb.urllib.request, "urlopen", lambda *args, **kwargs: (_ for _ in ()).throw(TimeoutError()))

    health = tb.load_shield_health("http://127.0.0.1:3102")
    html = tb.render_shield_panel(
        '<tr><td colspan="5">no completed attempts</td></tr>', "", "0 ok / 0 fail", 0,
        {"models": {}, "buckets": [{"ok": 0, "bad": 0}], "latest": 0},
        active_upstream=health["active_upstream"], now=4000.0,
    )

    assert health["active_upstream"] is None
    assert "active upstream unavailable" in html
    assert "0 active upstream" not in html


def test_load_shield_counts_only_real_upstream_attempts(tmp_path, monkeypatch):
    db_path = tmp_path / "shield.db"
    con = sqlite3.connect(db_path)
    con.execute("""create table tries(
        ts real, req text, session text, model text, effective text, outcome text,
        detail text, secs real, in_tok int, out_tok int, logical_request text,
        upstream_attempt text, retry_fallback text, gateway_wait real,
        capacity_wait real, health_probe text)""")
    rows = [
        (3900, "a", "s", "auto", "model-a", "OK", "", 2, 1, 1, "upstream_attempt", 1, 0, 0, 0, 0),
        (3950, "a", "s", None, None, "WAITING", "", 0, 0, 0, "capacity_wait", 0, 0, 0, 3, 0),
        (3990, "probe", None, "auto", "model-a", "PROBE_OK", "", 1, 1, 1, "health_probe", 0, 0, 0, 0, 1),
    ]
    con.executemany("insert into tries values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", rows)
    con.commit(); con.close()
    monkeypatch.setattr(tb, "SHIELD_DB", str(db_path))

    data = tb.load_shield(now=4000)

    assert data["latest"] == 3900
    assert sum(x["ok"] + x["bad"] for x in data["models"].values()) == 1
    assert sum(x["ok"] + x["bad"] for x in data["buckets"]) == 1


def test_completed_setup_history_is_removed_from_the_dashboard():
    html = tb.render_setup_history(
        pipe_html="<li>bootstrap passed</li>", prog_html="<div>product progress</div>",
        proofs_html="<div>C1 passed</div>", cooldowns="", done_n=7,
        n_pass=12, n_run=12, n_checks_ok=140, n_checks=140, blocked_note="",
    )

    assert html == ""


def test_incomplete_setup_history_remains_visible_as_an_alert():
    html = tb.render_setup_history(
        pipe_html="<li>bootstrap failed</li>", prog_html="", proofs_html="<div>C1 failed</div>",
        cooldowns="", done_n=6, n_pass=11, n_run=12, n_checks_ok=139, n_checks=140,
        blocked_note="",
    )

    assert html.startswith("<details")
    assert "Setup or commissioning needs attention" in html
    assert "bootstrap failed" in html


def test_cap_managed_agents_excludes_external_hermes_delegations():
    agents = [
        {"source": "db attempts", "lane": "free", "attempt_id": "controller-a"},
        {"source": "hermes registry", "lane": "free", "attempt_id": "delegated-a"},
        {"source": "db attempts", "lane": "luna", "attempt_id": "planner-a"},
    ]

    managed = tb.cap_managed_agents(agents)

    assert [a["attempt_id"] for a in managed] == ["controller-a", "planner-a"]
