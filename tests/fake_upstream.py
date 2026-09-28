#!/usr/bin/env python3
"""Fake flaky upstream for shield fault-injection tests.
Behaviour per model name:
  m-429    : always 429 with 'reset ~1m'
  m-503    : always 503
  m-empty  : 200 with empty content
  m-loop   : 200 with repetition garbage
  m-hang   : sleeps 30s (exceeds shield try cap in test)
  m-good   : valid reply
  m-flaky  : fails 3 times, then works
Global switch: if /tmp/shield-test/DOWN exists, every request -> connection drop.
"""
import http.server, json, os, socketserver, time
count = {}
class H(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers.get("content-length") or 0)))
        m = body.get("model")
        if os.path.exists("/tmp/shield-test/DOWN"):
            self.connection.close(); return
        count[m] = count.get(m, 0) + 1
        def send(code, obj):
            d = json.dumps(obj).encode(); self.send_response(code)
            self.send_header("content-type", "application/json"); self.send_header("content-length", str(len(d)))
            self.send_header("X-Routed-Via", f"fake/{m}"); self.end_headers(); self.wfile.write(d)
        ok = {"id": "x", "type": "message", "role": "assistant", "model": m, "stop_reason": "end_turn",
              "content": [{"type": "text", "text": f"hello from {m}"}], "usage": {"input_tokens": 3, "output_tokens": 3}}
        if m == "m-429": return send(429, {"error": {"type": "rate_limit_error", "message": "rate-limited. Soonest reset ~1m."}})
        if m == "m-503": return send(503, {"error": {"message": "No candidate model"}})
        if m == "m-empty": ok["content"] = [{"type": "text", "text": ""}]; return send(200, ok)
        if m == "m-loop": ok["content"] = [{"type": "text", "text": "the same thing again " * 300}]; return send(200, ok)
        if m == "m-hang": time.sleep(30); return send(200, ok)
        if m == "m-flaky" and count[m] <= 3: return send(500, {"error": {"message": "boom"}})
        return send(200, ok)
class S(socketserver.ThreadingMixIn, http.server.HTTPServer): daemon_threads = True
S(("127.0.0.1", 3198), H).serve_forever()
