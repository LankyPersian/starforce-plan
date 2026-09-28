#!/usr/bin/env bash
# Start fake upstream + test shield, run fault tests, then clean up.
# Cleanup is BY PORT, never pkill -f: a pattern that also appears in the caller's own
# command line matches that shell and SIGTERMs the run.
set -u
cd /home/ash/work/starforce-plan
rm -rf /tmp/shield-fake /tmp/shield-test
mkdir -p /tmp/shield-fake

kill_port() {  # kill whatever listens on $1
  local pids
  pids=$(ss -ltnp "sport = :$1" 2>/dev/null | grep -o "pid=[0-9]*" | cut -d= -f2 | sort -u)
  for p in $pids; do kill "$p" 2>/dev/null || true; done
}
kill_port 3197; kill_port 3198; sleep 1

python3 tests/fake_upstream.py >/tmp/fakeup.log 2>&1 &
FAKE_PID=$!
sleep 1

SHIELD_STATE=/tmp/shield-fake SHIELD_PORT=3197 \
  SHIELD_UPSTREAM=http://127.0.0.1:3198 SHIELD_TRY_CAP_S=5 \
  python3 freellm_shield.py >/tmp/shield-test.log 2>&1 &
SHIELD_PID=$!
sleep 2

curl -s -m 3 -o /dev/null -w "fake upstream: %{http_code}\n" http://127.0.0.1:3198/v1/messages \
  -X POST -H 'content-type: application/json' \
  -d '{"model":"m-good","max_tokens":5,"messages":[{"role":"user","content":"hi"}]}'
curl -s -m 3 -o /dev/null -w "test shield health: %{http_code}\n" http://127.0.0.1:3197/health || true

timeout 420 python3 tests/test_shield_faults.py
RC=$?

echo "--- test exit: $RC"
kill $SHIELD_PID $FAKE_PID 2>/dev/null
kill_port 3197; kill_port 3198
exit $RC
