#!/usr/bin/env python3
"""Serve tracker.html with a live Refresh button.

GET /            -> the freshest built tracker (rebuilt if older than 55 s)
POST /api/refresh-> re-runs tracker_build.main() NOW and returns status JSON

The button in the page calls /api/refresh and reloads, so the stats shown are
regenerated from the live evidence (shield DB, session logs, ps, git) at click
time — never from a cached copy.

Binds 127.0.0.1 only. No auth, no external exposure.
"""
import json, time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import tracker_build

PORT = 8790
LAST_BUILD = {"t": 0.0, "ok": True, "err": ""}


def rebuild(force=True, min_age=55):
    now = time.time()
    if not force and now - LAST_BUILD["t"] < min_age:
        return True
    try:
        # Re-import on every rebuild: editing tracker_build/lane_report must take
        # effect on the next refresh WITHOUT restarting this long-lived server.
        # (A stale in-memory copy silently overwrote tracker.html with old panels once.)
        import importlib
        import lane_report
        import tracker_telemetry
        importlib.reload(lane_report)
        importlib.reload(tracker_telemetry)
        importlib.reload(tracker_build)
        tracker_build.NOW = now  # tracker_build stamps at import-time NOW otherwise
        tracker_build.lr.NOW = now  # same for the "x ago" / 6h-window reference
        tracker_build.main()
        LAST_BUILD.update(t=time.time(), ok=True, err="")
    except Exception as e:  # surface, never crash the server
        LAST_BUILD.update(t=time.time(), ok=False, err=f"{type(e).__name__}: {e}")
    return LAST_BUILD["ok"]


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _send(self, code, ctype, body):
        b = body.encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(b)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(b)

    def do_GET(self):
        if self.path.split("?")[0] in ("/", "/index.html", "/tracker.html"):
            rebuild(force=False)
            if not LAST_BUILD["ok"]:
                self._send(200, "text/html; charset=utf-8",
                           f"<h1>tracker build failed</h1><pre>{LAST_BUILD['err']}</pre>")
                return
            try:
                with open(tracker_build.OUT) as f:
                    self._send(200, "text/html; charset=utf-8", f.read())
            except OSError as e:
                self._send(500, "text/html", f"cannot read tracker: {e}")
        else:
            self._send(404, "text/plain", "not found")

    def do_POST(self):
        if self.path == "/api/refresh":
            ok = rebuild(force=True)
            self._send(200, "application/json", json.dumps(
                {"ok": ok, "built_at": LAST_BUILD["t"], "error": LAST_BUILD["err"]}))
        else:
            self._send(404, "application/json", '{"ok":false,"error":"not found"}')


if __name__ == "__main__":
    rebuild(force=True)
    # 0.0.0.0 so Ash's laptop can open it over Tailscale (100.69.118.112:8790);
    # reachable by anything on his tailnet, not the public internet.
    ThreadingHTTPServer(("0.0.0.0", PORT), H).serve_forever()
