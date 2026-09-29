import os
import sqlite3

import tracker_telemetry as tt


def test_collect_agents_labels_free_lane_and_duration():
    lines = [
        "101 1 125 claude -p --model sonnet --output-format json build the feature",
        "102 1 30 codex exec -m gpt-5.6-luna --json plan the work",
        "103 1 20 python3 unrelated.py",
    ]

    agents = tt.collect_agents(
        lines,
        env_for_pid=lambda pid: {
            "101": {"EMPIRIUM_ATTEMPT_ID": "attempt-free", "ANTHROPIC_BASE_URL": "http://127.0.0.1:3102"},
            "102": {"EMPIRIUM_ATTEMPT_ID": "attempt-luna"},
        }.get(str(pid), {}),
    )

    assert [(a["pid"], a["lane"], a["runtime_s"]) for a in agents] == [
        ("101", "free", 125),
        ("102", "luna", 30),
    ]
    assert agents[0]["attempt_id"] == "attempt-free"
    assert agents[0]["model"] == "sonnet"


def test_project_progress_requires_two_integrations_for_eta(tmp_path):
    db = tmp_path / "build.db"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE work_items (id TEXT, kind TEXT, status TEXT, created_at REAL, integrated_at REAL)")
    con.executemany(
        "INSERT INTO work_items VALUES(?,?,?,?,?)",
        [
            ("F1", "implement", "integrated", 100.0, 200.0),
            ("F2", "implement", "integrated", 100.0, 400.0),
            ("F3", "implement", "ready", 100.0, None),
            ("parent", "container", "integrated", 100.0, 250.0),
        ],
    )
    con.commit()
    con.close()

    progress = tt.load_project_progress(str(db))

    assert progress["done"] == 2
    assert progress["total"] == 3
    assert progress["percent"] == 66.7
    assert progress["eta_s"] == 200.0


def test_project_progress_returns_no_eta_without_two_integrations(tmp_path):
    db = tmp_path / "build.db"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE work_items (id TEXT, kind TEXT, status TEXT, created_at REAL, integrated_at REAL)")
    con.execute("INSERT INTO work_items VALUES('F1','implement','integrated',100,200)")
    con.execute("INSERT INTO work_items VALUES('F2','implement','ready',100,NULL)")
    con.commit()
    con.close()

    progress = tt.load_project_progress(str(db))

    assert progress["eta_s"] is None
    assert progress["eta_reason"] == "need at least two accepted integrations"
