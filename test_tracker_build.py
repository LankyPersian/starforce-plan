from pathlib import Path

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


def test_shield_panel_distinguishes_live_calls_from_completed_history():
    shield = {"models": {}, "buckets": [{"ok": 0, "bad": 0}], "since": 100.0}

    html = tb.render_shield_panel(
        '<tr><td colspan="5">no completed attempts</td></tr>',
        "", "0 ok / 0 fail", 0, shield, live_free=12,
    )

    assert "Completed shield attempts" in html
    assert "12 live now" in html
    assert "0 completed in the last 6 h" in html
    assert "does not mean the free lane is idle" in html


def test_setup_history_is_collapsed_and_not_presented_as_product_progress():
    html = tb.render_setup_history(
        pipe_html="<li>bootstrap passed</li>", prog_html="<div>product progress</div>",
        proofs_html="<div>C1 passed</div>", cooldowns="", done_n=7,
        n_pass=12, n_run=12, n_checks_ok=140, n_checks=140, blocked_note="",
    )

    assert html.startswith("<details")
    assert "Setup &amp; commissioning history" in html
    assert "not current product progress" in html
    assert "bootstrap passed" in html
    assert "C1 passed" in html


def test_cap_managed_agents_excludes_external_hermes_delegations():
    agents = [
        {"source": "db attempts", "lane": "free", "attempt_id": "controller-a"},
        {"source": "hermes registry", "lane": "free", "attempt_id": "delegated-a"},
        {"source": "db attempts", "lane": "luna", "attempt_id": "planner-a"},
    ]

    managed = tb.cap_managed_agents(agents)

    assert [a["attempt_id"] for a in managed] == ["controller-a", "planner-a"]
