# Empirium Studio / AI Workforce — Forensic State Report

Generated: 2026-09-28 (read-only inspection, no mutations made)

## 1. Repos & branches

| Repo | Path | Branch | HEAD | Notes |
|---|---|---|---|---|
| Target fork | `/home/ash/empirium-studio` | `feat/empirium-studio-workforce` | `796e944` "fix(workforce): bound CAO continuation inspection" | 230 commits on branch (`git log --oneline` count). Large uncommitted diff (~60 modified files + new untracked files) under `AI_WORKFORCE_BUILD/` — see §2. |
| Control | `/home/ash/hermes-studio-control` | `main` | `39f9ceb` | Same tip as the pre-workforce baseline in `hermes-studio`; treated as the stable reference. |
| Service repo | `/home/ash/hermes-studio` | `main` | `c1bf6a9` "Add workforce implementation and updates" (one commit ahead of `39f9ceb`) | **This is what `hermes-studio.service` actually runs** (`WorkingDirectory=/home/ash/hermes-studio`, `ExecStart=node server-entry.js`). Its one workforce commit is a small, early, throwaway stub (`generated-workforce-screen.tsx`, `generated-workforce.ts`, ~546 lines) — NOT the same 230-commit workforce build living in `empirium-studio`. **The real/live systemd service is running old/stub code, not the fork under active development.** |

## 2. Uncommitted working-tree state (`empirium-studio`)

`git status --short` shows ~60 modified tracked files (all under `AI_WORKFORCE_BUILD/**`, `src/server/**`, `src/routes/api/**`, `src/test/**`, `src/types/director.ts`, `scripts/production-*.ts`, `src/cli/reconcile-binding-integrity.ts`) plus untracked additions: `.hermes/`, `controller/director-checkpoints.db`, `controller/freellmapi-director/` (turn logs), `controller/runtime/`, several new `leases/*.json`, screenshots (`baseline-workforce*.png`, `preview-workforce-before.png`), and `test-results-9b54bd4-*.txt`. This is live controller/evidence churn from an in-progress autonomous run, not feature work — nothing here was committed or cleaned up.

## 3. AI_WORKFORCE_BUILD program status

- **BUILD_STATE.md**: Status `IN_PROGRESS`. Checkpoint commit `7c568ea5...`. 710 reconciled atomic requirements from 140 source sections (0 unmapped). **Mandatory requirements verified: 0.** Release gate: `NOT_READY`. Explicitly labeled "resumable state, not a completion claim."
- **FINAL_RELEASE_GATE.json**: `status: NOT_READY`, release commit `9ce4db1`. 710 mandatory requirements, 0 "not_verified" but **710 "missing_proof"** (no four-proof evidence attached to any requirement). 9 stale-evidence items. Failing checks: `mandatory_requirements_have_four_proofs`, `fresh_evidence`, `blocking_security_zero`, `self_verification`, `restart`, `burn_in`, `red_team`, `migration_rollback`, `regression`, `required_phases_verified`. Passing checks: `source_checksum`, `source_coverage_zero_unmapped`, `mandatory_requirements_verified` (counted as 0/0 — vacuously true), `no_partial_completion_contradiction`.
- **BLOCKERS.md** (4 items):
  1. Kanban/crew task stores (`task-store.ts` → `.runtime/tasks.json`, `crew-store.ts` → `.runtime/crews.json`) are file-backed and domain-mismatched vs. the Postgres `workforce.tasks` table; merging them needs an explicit ADR, not a drop-in swap.
  2. Postgres ownership/target DB/migration/backup/rollback "not verified" as of doc text, but a 2026-09-17 update reports two real bugs found and fixed once the integration test suite was actually made to run (previously silently skipped because `vitest.config.ts` only loads `.env` via `setup-env.ts`, and `WORKFORCE_DATABASE_SCHEMA` was read into a module-level const before tests could override it, causing test schema leakage into the shared default schema). Formal down-migration/rollback scripts still don't exist (schema only grows via `IF NOT EXISTS`). Backup/restore still unverified.
  3. Independent semantic review + four-proof evidence still pending (matches gate `missing_proof: 710`).
  4. RESOLVED note: `event-store.test.ts`/`analytics.test.ts` were not flaky — `better-sqlite3` was compiled against the wrong Node ABI (147 vs. runtime's 115), so every DB call silently returned null. Fixed with `npm rebuild better-sqlite3`; flag as a required deploy step.
- **MASTER_SPEC.md**: Frames the whole program as "evolve Hermes Studio into a persistent departmental AI-workforce application while preserving the stable Control Studio." Lists unresolved verification items (native-Kanban integration authority, 16 specialist profile routing/quotas, workspace isolation, permission boundaries) still open at spec level even though BUILD_STATE claims 710 reconciled requirements.
- **MODEL_POLICY.md**: Hard "free-only, no paid fallback, fail-closed" policy via FreeLLMAPI. On quota/route exhaustion the contract is to fail with `FREE_ROUTE_EXHAUSTED`/`MODEL_UNAVAILABLE`, never silently fall back to paid. Workers must probe `/models` and record `_routed_via`/`execution_id`.
- **ASSET_MANIFEST.md**: 586 source asset files, 312 MB, 23 duplicate-hash groups. Categorized (character sheets, furniture sheets, office-environment refs, status visual language, etc.) — mostly `operational-history` (493 files) and `visual-unclassified` (64). A short list of "identified production candidates" (turnaround/expression/furniture/office-shell art assets) exists but has not been wired into the app.
- **REQUIREMENTS.json**: Not the 710-item list itself — it's a 3-key pointer/manifest: `requirements_source` (`/home/ash/.hermes/attachments/STUDIO_WORKFORCE_PLAN-2.md`), `status: draft`, and notes reiterating "no renderer authority," "no fabricated live metrics," "PostgreSQL topology unverified," "FreeLLMAPI route must be evidenced." (The actual 710-requirement breakdown lives in `REQUIREMENTS_PASS_A/B.json` / `REQUIREMENTS_TRACEABILITY.json`, both currently uncommitted-modified.)
- **DECISIONS.md** (short, binding): build inside embedded Hermes Studio; preserve existing embed/basepath commits; use supplied Nexus character sheets for employee visuals; **renderer prototype is not authoritative**; no deployment or destructive migration without explicit approval.

### controller/ directory (orchestration state)
- `HEARTBEAT.json` (last write 2026-09-17T09:24Z): phase `1-source-and-baseline`, no active leases/workers, provider health `FreeLLMAPI: configured_not_probed`, blocking issues `partial existing Workforce implementation`, `PostgreSQL authority not implemented`. Stale relative to later commits — heartbeat wasn't kept current through later runs.
- `meta-director-checkpoint.json` (tail, updated 2026-09-19T13:15:57Z, generation 100): release gate `NOT_READY`, `independentlyVerified: 0/710`. `orchestrationAudit.approval: NOT_GRANTED`. Four "proofs" (A–D) of orchestration capability were run against **fixtures**, not live conditions, and every one has an admitted gap:
  - Proof A: live process launches supported, but proof doc cites the wrong first PID.
  - Proof B: lease-recovery mechanism works but a fixture bug (`!state.proofB?.recovered` checked against a field actually named `recoveredAt`) causes repeated spurious lease replacement; does not prove stable terminal completion.
  - Proof C: reviewer/model were fixture stand-ins (`fixture-independent-reviewer`, `fixture-opus`); no real subscription-Claude review or real Git SHA was exercised.
  - Proof D: `SUBSCRIPTION_LIMIT` was **injected by the fixture**, not a real exhausted subscription; restart persistence across true process restart was not located as separately verified.
  - `discoveredWork` explicitly flags: release gate JSON is missing an `exitCode` field the supervisor completion config requires, and "fresh semantic Opus requirements reconciliation remains pending; deterministic extraction is not independent Opus approval."
- `controller/freellmapi-director/`: 18 turns of prompt/response/usage logs from a FreeLLMAPI-routed director session (prompt-1..18.md, turn-N.log, turn-N-usage.json). Confirms the FreeLLMAPI route was actually exercised multiple times, not just configured.
- `controller/leases/`: many `pm-*` lease files (`pm-free-route-g6.json`, `pm-proof-recovery-g6.json`, `pm-proof-d-capture.json`, `pm-release-audit-101.json`, etc.) — evidence of repeated lease acquisition/recovery cycles, consistent with a director that keeps restarting/retrying.
- `controller/director-checkpoints.db` and `controller/runtime/restart-before-state.json` — a restart-resilience checkpoint mechanism exists and has state, but "restart" is still a **failing** release-gate check.

## 4. Test & typecheck status (run live in this session, 2026-09-28, unmodified repo)

- `npx vitest run` in `/home/ash/empirium-studio`: **39 test files passed, 403/403 tests passed**, 28.75s. Covers workforce API routes, director-service, reconciliation, employee/department stores, workforce-office-state, workforce-invariants, native-kanban-adapter, event-store, analytics, design-system components, etc. No failures, no skips reported in the final summary.
- `npx tsc --noEmit`: **exit code 0, zero output** — clean typecheck.
- Caveat: this is the code currently on disk (post-`better-sqlite3` rebuild, per BLOCKERS §4); it does **not** by itself satisfy the release gate's "regression," "burn_in," "restart," or "red_team" checks, which require dedicated runs beyond a single green vitest pass.

## 5. Stack

- React 19.2, Vite 7.1, TanStack (router codegen present — `src/routeTree.gen.ts`), `better-sqlite3` 12.8 (native SQLite for event store / task-store / crew-store), `pg` 8.23 (Postgres client) via `src/server/workforce-postgres.ts` + `src/server/workforce-postgres-adapter.ts`. No PixiJS anywhere in `src` (`grep -ril pixi src` returned nothing) — the "living office" renderer is pure SVG + CSS animations, not a canvas/WebGL engine.

## 6. Screens / workforce UI that actually exist

`src/screens/` contains (non-exhaustive, workforce-relevant): `workforce/`, `conductor/` (with `hooks/` and `components/`), `tasks/`, `operations/`, `agents/`, `crews/`, `profiles/`, `audit/`, plus generic app screens (`chat`, `dashboard`, `memory`, `docs`, `settings`, `patterns`, `analytics`, `logs`, `jobs`, `files`, `session-history`, `skills`, `help`).

- **`src/screens/conductor/components/office-view.tsx`** (42.8 KB) — the "living office." Header comment: *"Animated SVG office view — shows agent desks, monitors, speech bubbles, status glows, social spots, and wandering idle agents. Three layouts: Grid, Roundtable, War Room. Pure CSS animations + SVG, no framer-motion."* Explicitly documented as **"Ported from upstream hermes-workspace office-view.tsx"** with Studio-specific adaptations (localStorage key `hermes-studio:office-layout`, header text "Mission Control", imports `AgentAvatar`/`AGENT_ACCENT_COLORS` from `./agent-avatar`). Exports `AgentWorkingRow`/`AgentWorkingStatus` types (`spawning|ready|active|idle|paused|error|none|waiting_for_input`). This is a real, working, non-trivial renderer — not a stub — but it is SVG/CSS, not the PixiJS engine the build docs speculated about elsewhere; DECISIONS.md itself states "renderer prototype is not the authority."
- `src/screens/workforce/` exists as a distinct screen dir separate from `conductor` — there appear to be two workforce-facing UI surfaces (a `workforce` screen and the `conductor` office view); their relationship/precedence is not documented in the files inspected and should be clarified before reuse.

## 7. Server-side workforce/domain code (`src/server/`)

Present and covered by passing tests: `workforce-capability-broker.ts`, `workforce-domain-store.ts`, `workforce-invariants.ts`, `workforce-learning-store.ts`, `workforce-office-state.ts`, `workforce-postgres.ts`, `workforce-postgres-adapter.ts`, `workforce-qa-store.ts`, `workforce-qa.ts`, `workforce-run-store.ts`, `department-store.ts`, `employee-store.ts`, `director-service.ts`, `autonomy-kernel.ts`. API routes under `src/routes/api/`: `departments/`, `employees/`, `workforce-director.intake.ts`, `workforce-director.plan.ts`, `workforce-director.status.$projectId.ts`, `workforce-kanban.ts`, `workforce-projects.ts`.

## 8. Postgres schema status

- Integration test `src/test/workforce-postgres-integration.test.ts` now actually runs (previously silently skipped — see BLOCKERS §2) and passes as part of the 403/403 green run.
- Schema is additive-only: created/extended via `CREATE TABLE IF NOT EXISTS` / `ALTER TABLE ... ADD COLUMN IF NOT EXISTS` in `workforce-postgres.ts`. **No down-migrations exist.** Backup/restore procedure unverified. Per-test schema isolation (`WORKFORCE_DATABASE_SCHEMA`) had a caching bug that was fixed (schema now re-resolved per `ensureWorkforceSchema()` call, with `resetWorkforceSchemaCache()` for tests that drop schemas).
- The Kanban/crew domain (`task-store.ts`, `crew-store.ts`) remains file-backed (`.runtime/tasks.json`, `.runtime/crews.json`) and is a structurally different shape from the Postgres `workforce.tasks` table — unreconciled, flagged as needing an ADR (Blocker #1).

## 9. Reconciler / CAO / director controller architecture

- **`empirium-cao.service`** (systemd --user): "Empirium CAO worker-session transport," active/running, uptime ~1 week 2 days at inspection time, PID via `/home/ash/.local/share/uv/tools/cli-agent-orchestrator/bin/python3 .../cao-server`. Has a drop-in `workforce-env.conf`. Recent log lines show session lifecycle traffic for `cao-flow-empirium-v6-continuation` (GET terminals, DELETE session) — i.e., it's actively brokering worker sessions, not idle.
- **Autonomy reconciler**: `/home/ash/.local/state/empirium/autonomy-reconciler-production/` contains a `controller.json`, and **over 100 `attempt_<uuid>.context.json` / `.result.json` pairs** plus a `worktrees/` directory with well over 100 detached-HEAD git worktrees (product IDs `product-emp-003`, `product-off-001`, `product-prj-001`, `product-res-001`, `product-wrk-005`, all under one project `proj_d53933df-df89-4a2f-a9ed-2509805bb8c1`). This is a large volume of individually-sandboxed autonomous attempt executions — the reconciler pattern is real and was exercised heavily, not theoretical.
- **`scripts/production-reconciler.ts`** and **`scripts/production-autonomy-commission.ts`** in the repo (both currently in the uncommitted diff) correspond to this reconciler machinery.
- `controller/*.py` scripts (`bootstrap_requirements.py`, `finish_bootstrap.py`, `autonomy_kernel_gate.py`, `initial_product_gate.py`, `update_build_state.py`, `update_slice_ledger.py`, `inspect_build_state.py`, `test_workforce_release_gate.py`) form a Python-side gate/ledger toolchain alongside the TS runtime.

## 10. Worktrees

- `git worktree list` in `empirium-studio` returns **130 entries total**; **112 of them** are reconciler-production attempt worktrees under `/home/ash/.local/state/empirium/autonomy-reconciler-production/worktrees/` (detached HEADs at various commits, mostly `a769b83`/`712039d`, i.e., largely converged on a couple of base commits with a long tail of one-off attempts).
- **18 entries** are local task/feature worktrees under `/home/ash/empirium-studio/.worktrees/`, notably:
  - `.worktrees/ESB-RUNTIME-001` → branch `ai/ESB-RUNTIME-001-postgres-authority` (`ad93912`)
  - `.worktrees/ESB-RUNTIME-002` → branch `ai/ESB-RUNTIME-002-department-authority` (`898b7ac`)
  - `.worktrees/t_5ee57658` → branch `wt/off-001-living-office` (`712039d`)
  - `.worktrees/t_7aa2f299` → branch `wt/prj-001-project-workspace` (`712039d`)
  - `.worktrees/t_c105dc8b` → branch `wt/emp-003-dossier` (`c92a282`)
  - `.worktrees/t_e6f32b63` → branch `wt/res-001-browser-close` (`7031266`)
  - `.worktrees/t_e91b8b17` → branch `wt/wrk-005-reconciler` (`c92a282`)
  - Six more (`t_0910e5d5`, `t_1e280149`, `t_2360c072`, `t_3774b392`, `t_5fc6f842`, `t_8869d071`, `t_982148b2`, `t_b32e3ee0`, `t_d08ebfab`, `t_fae8afad`) all sit at the same old `39f9ceb` base and look unmerged/abandoned.
- `hermes kanban` currently shows two **running worker sessions** actively bound to two of these task worktrees (`t_7aa2f299`, `t_c105dc8b` — matching `wt/prj-001-project-workspace` and `wt/emp-003-dossier`), confirmed via `systemctl --user list-units` showing `hermes-worker-kanban-t_7aa2f299-run-258.scope` and `hermes-worker-kanban-t_c105dc8b-run-255.scope`, both `frontend-engineer` profile, provider `custom:freellmapi`, still running at inspection time.

## 11. Kanban board (`empirium-studio-build`, read-only via `hermes kanban stats`)

- By status: `triage=0, todo=6, scheduled=0, ready=27, running=0, blocked=1, done=11` (total 45 cards).
- By assignee (done counts): `frontend-engineer=3, model-routing-engineer=1, platform-engineer=2, qa=ready:1, qa-engineer=1, repo-archaeologist=1, systems-architect=2, technical-artist=blocked:1/done:1/todo:6`.
- `technical-artist` carries the most unstarted work (6 todo) plus the one `blocked` card — visual/asset integration is the least-progressed lane.
- Oldest ready task age: 1,015,350s (~11.75 days) — ready work has been sitting unpicked for well over a week, consistent with the loop stalls in §12.
- Note: `hermes kanban list --board <name>` is not a valid CLI form in this Hermes version (errors "unrecognized arguments: --board"); stats/list must be queried without that flag or via the correct subcommand syntax.

## 12. Why autonomous runs stalled/failed — evidence from loop logs

Five separate autonomous-loop attempts under `/home/ash/Desktop/AI Taskforce/`:

| Loop | Passes | Outcome | Failure mode |
|---|---|---|---|
| `claude-autonomous-loop` | 30 passes (pass 1→30, all at fixed commit `4fd469e`) | **LOOP_EXIT with no completion** | Every single pass returned `claude_exit=1` and `marker=PROJECT_INCOMPLETE`; zero code progress (commit hash never changed across 30 passes) — the Claude-subscription-driven loop was stuck failing to invoke/produce work at all. |
| `claude-autonomous-loop-2` | 4 passes | **Reached `PROJECT_COMPLETE`** (pass 34, commit `9b54bd4`) | Real progress this time (`test_exit=0 typecheck_exit=0 build_exit=0` on later passes), but see the reef-loop-v2 entry below — this same `PROJECT_COMPLETE` was later invalidated. |
| `freellmapi-autonomous-loop` | 14 passes | **Reached `PROJECT_COMPLETE`** (commit `900082d`) | Two passes hit `hermes_exit=124` (timeout) before recovering; otherwise steady progress on a fixed commit for many passes before advancing. |
| `freellmapi-reef-loop` | ≥12 passes shown | Ongoing/incomplete in the tail shown | `typecheck_exit=2` appears on pass 11 — a real regression the loop had to work through; commit stuck at `9b28e32`/`9fa7415` across many passes (slow progress). |
| `freellmapi-reef-loop-v2` | 55+ passes, largest log (323 lines) | Cycled `PROJECT_INCOMPLETE`/`PASS_COMPLETE`/`LOOP_EXIT` repeatedly, commit frozen at `70aa2b3` for at least passes 48–55 | **Root cause pattern: `hermes_exit=124` (timeout) recurring on almost every pass** (`route=freellmapi`), with `progress=no` on most of them — i.e., the FreeLLMAPI-routed worker was repeatedly **timing out** rather than making forward progress, and the outer harness just restarts a fresh pass each time (`LOOP_EXIT` → new `START`) without the code changing. **Most significant finding:** a `PROJECT_COMPLETE` marker recorded 2026-09-17T01:07:32Z was later explicitly reverted: *"marker removed by orchestrator: BUILD_STATE.json status=IN_PROGRESS, release gate NOT_READY (699/710 unstarted), self_verification/restart_test/burn_in all null - PROJECT_COMPLETE was a false positive from worker self-report."* This directly corroborates the release-gate's `missing_proof: 710` and confirms **at least one worker self-reported completion falsely** and had to be caught/reverted by a supervising orchestrator layer. |

- No literal `429` HTTP status strings were found in any loop log or evidence file; the closest analog is `hermes_exit=124` (process timeout) recurring heavily in `freellmapi-reef-loop-v2`, and 16 references to `SUBSCRIPTION_LIMIT` inside `AI_WORKFORCE_BUILD/` — but the orchestration-audit (§3, Proof D) confirms those `SUBSCRIPTION_LIMIT` events were **fixture-injected for testing the recovery path**, not organic Claude-subscription exhaustion. So: the actual observed stall cause across the real overnight runs was **timeouts on the FreeLLMAPI route**, not rate-limit/429s; the rate-limit/session-limit handling that exists is largely proven only against synthetic fixtures.
- Combined with §3's `orchestrationAudit.approval: NOT_GRANTED` and four proofs all carrying documented gaps, the overall picture is: the controller/reconciler/proof machinery is real and has been exercised at volume (112+ worktree attempts, 18-turn FreeLLMAPI director sessions, dozens of lease files), but **no run has produced verifiable, non-fixture, four-proof-backed completion**, and at least one run's self-reported completion was caught as false and rolled back.

## 13. Keep / Salvage / Discard recommendations

**Keep (working, tested, reusable as-is):**
- `src/server/workforce-*.ts` domain/store modules and their API routes — 403/403 tests green, `tsc --noEmit` clean.
- `src/screens/conductor/components/office-view.tsx` — real, working SVG/CSS living-office renderer with three layouts; reuse directly, don't rebuild in PixiJS unless there's a specific reason (none found in docs beyond speculative asset categories).
- The Postgres adapter pattern (`workforce-postgres.ts`/`-adapter.ts`) and its additive-migration discipline — sound approach, just needs down-migrations and a real backup/restore test written before being trusted.
- `empirium-cao.service` — stable, long-uptime, actively used worker-session transport; keep running as infrastructure.
- The reconciler/worktree pattern itself (isolated git worktree per attempt) — proven at scale (112+ attempts), worth keeping as the execution isolation model for a new build.
- FreeLLMAPI free-only routing policy (`MODEL_POLICY.md`) — sound safety contract; keep, but harden the timeout handling given §12's dominant failure mode.

**Salvage (partially useful, needs rework before trust):**
- `FINAL_RELEASE_GATE.json` / `REQUIREMENTS_PASS_A/B.json` / `REQUIREMENTS_TRACEABILITY.json` — the 710-requirement structure and gate-check taxonomy are a good skeleton for a new plan's acceptance criteria, but every requirement currently lacks proof; treat as a template, not as evidence of readiness.
- `controller/` Python gate scripts — logic worth reviewing/reusing, but the fact that `PROJECT_COMPLETE` false-positives got through once means the self-verification step they gate needs independent (non-worker-self-report) checking before reuse.
- The 586-file asset manifest — a handful of "production candidate" character/furniture/office assets are usable; the bulk (`operational-history`: 493 files, `visual-unclassified`: 64) should be triaged, not carried forward wholesale.
- `src/screens/workforce/` vs `conductor/` office-view duplication — figure out which is canonical before continuing either.

**Discard / do not carry forward:**
- `hermes-studio` (the live service repo) as a source of workforce code — its one workforce commit is a disconnected early stub, superseded by 230 commits of real work in `empirium-studio`; don't resync from it, retarget the service's deploy source instead.
- The 100+ stale `.worktrees/t_*` entries in `empirium-studio` at old base `39f9ceb` — abandoned, safe to prune (outside this read-only task's scope to actually delete).
- Fixture-only orchestration proofs (A–D in `meta-director-checkpoint.json`) as evidence of production readiness — they prove the mechanism *can* work under controlled conditions, not that it *has* worked live; re-run for real before claiming release-gate checks pass.
- Any reliance on `HEARTBEAT.json`/`BUILD_STATE.md` as current status — both are stale (last real updates 2026-09-17/19) relative to the 796e944 tip; a new plan needs fresh state capture, not a resume from these files as-is.
