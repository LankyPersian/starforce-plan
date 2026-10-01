import os
import sqlite3

import tracker_telemetry as tt
import tracker_build as tb


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


def test_merge_agents_counts_one_live_call_per_attempt():
    cli = [
        {"pid": "101", "ppid": "1", "runtime_s": 20, "kind": "claude", "lane": "free",
         "model": "model-a", "attempt_id": "attempt-a", "command": "wrapper"},
        {"pid": "102", "ppid": "101", "runtime_s": 19, "kind": "claude", "lane": "free",
         "model": "model-a", "attempt_id": "attempt-a", "command": "claude child"},
    ]
    db = [
        {"pid": "101", "ppid": "", "runtime_s": 20, "kind": "implement", "lane": "free",
         "model": "model-a", "attempt_id": "attempt-a", "item_id": "F0-A",
         "command": "controller attempt"},
    ]

    merged = tb.merge_agents(cli, db, [])

    assert len(merged) == 1
    assert merged[0]["attempt_id"] == "attempt-a"
    assert merged[0]["item_id"] == "F0-A"
    assert merged[0]["source"] == "db attempts"


def test_free_runtime_infers_real_route_from_live_worker(monkeypatch):
    monkeypatch.setattr(tb, "_proc_env", lambda pid: {
        "EMPIRIUM_BUILD_STATE": tb.FSTATE,
        "EMPIRIUM_MAX_FREE_WORKERS": "12",
    })
    monkeypatch.setattr(tb, "_endpoint_status", lambda url: "HTTP 200" if url else "unknown")
    ps = [{"kind": "controller", "pid": "42"}]
    agents = [{"lane": "free", "route_url": "http://127.0.0.1:3102"}]

    runtime = tb.load_free_runtime(ps, {"current_free": 1}, agents)

    assert runtime["mode"] == "REAL FreeLLMAPI"
    assert runtime["shield"] == "http://127.0.0.1:3102"
    assert runtime["upstream"] == "http://127.0.0.1:3101"


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


def _dashboard_db(path):
    con = sqlite3.connect(path)
    con.executescript("""
        CREATE TABLE work_items (
          id TEXT, title TEXT, kind TEXT, status TEXT, phase TEXT, lane TEXT,
          scope_json TEXT, acceptance_json TEXT, attempt_count INTEGER,
          fail_count INTEGER, last_fail_class TEXT, active_attempt_id TEXT,
          integrated_at REAL, updated_at REAL, park_reason TEXT
        );
        CREATE TABLE attempts (
          id TEXT, work_item_id TEXT, status TEXT, lane TEXT,
          requested_model TEXT, effective_model TEXT, started_at REAL,
          last_progress_at REAL, result_sha TEXT, failure_class TEXT, detail TEXT
        );
        CREATE TABLE release_gate_runs (
          id INTEGER, at REAL, sha TEXT, exit_code INTEGER, report_path TEXT, ready INTEGER
        );
    """)
    return con


def test_delivery_snapshot_separates_product_work_from_control_work(tmp_path):
    db = tmp_path / "build.db"
    con = _dashboard_db(db)
    con.executemany(
        "INSERT INTO work_items VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        [
            ("F0-A", "architecture", "implement", "integrated", "F0", "free", '["a.md"]', '["test -f a.md"]', 1, 0, None, None, 200, 200, None),
            ("F0-B", "contracts", "implement", "running", "F0", "free", '["b.md"]', '["test -f b.md"]', 2, 1, "TEST_FAILED", "a2", None, 300, None),
            ("PLAN-B", "respec contracts", "respec", "integrated", None, "luna", '[]', '[]', 1, 0, None, None, 250, 250, None),
            ("PARENT", "container", "container", "waiting_dependency", "F0", "free", '[]', '[]', 0, 0, None, None, None, 100, None),
        ],
    )
    con.execute("INSERT INTO attempts VALUES(?,?,?,?,?,?,?,?,?,?,?)", ("a2", "F0-B", "running", "free", "auto", "model-x", 290, 299, None, None, None))
    con.commit(); con.close()

    snap = tt.load_delivery_snapshot(str(db), now=310)

    assert snap["delivery"]["total"] == 2
    assert snap["delivery"]["integrated"] == 1
    assert snap["control"]["total"] == 2
    assert snap["current_phase"] == "F0"
    assert snap["phases"][0]["remaining"] == 1
    assert snap["active"][0]["id"] == "F0-B"
    assert snap["active"][0]["model"] == "model-x"
    assert snap["active"][0]["scope"] == ["b.md"]


def test_product_status_never_calls_bootstrap_completion_product_done():
    snapshot = {
        "delivery": {"total": 8, "integrated": 2, "remaining": 6},
        "release": {"ready": False, "passed": 4, "total": 20, "failing": ["build"]},
        "current_phase": "F0",
    }

    status = tt.derive_product_status(snapshot, controller_up=True)

    assert status["label"] == "BUILDING"
    assert status["complete"] is False
    assert "6 product work items remain" in status["reason"]
    assert "release gate 4/20" in status["reason"]


def test_product_status_requires_green_release_gate_and_zero_remaining():
    snapshot = {
        "delivery": {"total": 8, "integrated": 8, "remaining": 0},
        "release": {"ready": True, "passed": 20, "total": 20, "failing": []},
        "current_phase": None,
    }

    status = tt.derive_product_status(snapshot, controller_up=False)

    assert status == {"label": "RELEASE READY", "complete": True, "reason": "all product work integrated and deterministic release gate passed"}


def test_product_dashboard_renders_delivery_truth_and_release_failures():
    snapshot = {
        "delivery": {"total": 8, "integrated": 2, "remaining": 6, "running": 2,
                     "awaiting_review": 1, "ready": 1, "waiting_capacity": 1,
                     "waiting_dependency": 1, "parked": 0, "blocked": 0, "failed": 0, "todo": 0},
        "control": {"total": 3, "integrated": 1, "remaining": 2},
        "current_phase": "F0",
        "phases": [{"phase": "F0", "total": 8, "integrated": 2, "remaining": 6, "running": 2, "percent": 25.0}],
        "active": [{"id": "F0-B", "title": "contracts", "category": "product", "phase": "F0",
                    "status": "running", "lane": "free", "model": "model-x", "runtime_s": 20,
                    "last_progress_s": 4, "scope": ["b.md"], "acceptance": ["test -f b.md"],
                    "attempts": 2, "failures": 1, "last_failure": "TEST_FAILED", "park_reason": ""}],
        "release": {"ready": False, "passed": 4, "total": 20, "failing": ["build"],
                    "checks": [{"name": "build", "ok": False, "detail": "no fresh evidence"}],
                    "at": 300, "sha": "abc123"},
    }
    status = tt.derive_product_status(snapshot, controller_up=True)

    html = tb.render_product_dashboard(snapshot, status, bootstrap_complete=True)

    assert "BUILDING" in html
    assert "Bootstrap complete is not product complete" in html
    assert "2/8" in html
    assert "4/20" in html
    assert "F0-B" in html
    assert "b.md" in html
    assert "no fresh evidence" in html
