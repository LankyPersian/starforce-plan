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
