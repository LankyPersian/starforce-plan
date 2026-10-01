import freellm_shield as shield
import sqlite3
import threading


def test_shield_module_contains_http_runtime_entrypoint():
    assert hasattr(shield, "upstream")
    assert hasattr(shield, "session_key")
    assert hasattr(shield, "sse")
    assert hasattr(shield, "H")
    assert hasattr(shield, "Server")


def test_log_try_migrates_fresh_database_and_records_attempt(tmp_path, monkeypatch):
    db_path = tmp_path / "shield.db"
    monkeypatch.setattr(shield, "DB", db_path)

    shield.log_try(
        req="request-a", session="session-a", model="auto", effective="model-a",
        outcome="OK", logical_request="upstream_attempt", upstream_attempt=1,
    )

    con = sqlite3.connect(db_path)
    columns = {row[1] for row in con.execute("pragma table_info(tries)")}
    row = con.execute(
        "select req,session,outcome,logical_request,upstream_attempt from tries"
    ).fetchone()
    con.close()

    assert {"logical_request", "upstream_attempt", "retry_fallback", "gateway_wait",
            "capacity_wait", "health_probe"} <= columns
    assert row == ("request-a", "session-a", "OK", "upstream_attempt", 1)


def test_health_probe_can_log_without_a_worker_session(tmp_path, monkeypatch):
    db_path = tmp_path / "shield.db"
    monkeypatch.setattr(shield, "DB", db_path)

    shield.log_try(req="probe", model="auto", outcome="PROBE_OK", health_probe=1)

    con = sqlite3.connect(db_path)
    row = con.execute("select req,session,outcome,health_probe from tries").fetchone()
    con.close()
    assert row == ("probe", None, "PROBE_OK", 1)


def test_stream_worker_exception_returns_error_and_signals_done(monkeypatch):
    def explode(*args, **kwargs):
        raise ValueError("bad payload")

    monkeypatch.setattr(shield, "resilient", explode)
    result, done = {}, threading.Event()

    shield.run_stream_work(result, done, "/v1/messages", {"messages": None}, {})

    assert done.is_set()
    code, response, model = result["v"]
    assert code == 500
    assert response["error"]["type"] == "api_error"
    assert model is None
