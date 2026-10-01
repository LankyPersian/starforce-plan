# EMPIRIUM STUDIO (AI STAR FORCE) — AUTONOMOUS BUILD PROMPT v7
### One prompt. No further owner input. Never stalls on a failed model call.

> **Who runs this:** `bootstrap_runner.py` (systemd user service `empirium-bootstrap`) launches disposable Claude Code workers against this document to build and commission a deterministic controller (§14), then hands the project to it. No chat session keeps this project alive at any point.
>
> **Compiled:** 2026-09-28 from all 147 relevant Hermes chat sessions (2026-09-01 → 2026-09-28), every pasted spec, the desktop asset folder, the live repo state and a live FreeLLMAPI reliability probe. Evidence pack: `/home/ash/work/starforce-plan/` (see §2).

---

## 0. THE FIVE LAWS (read these if you read nothing else)

1. **Keep the project alive, not the LLM session.** All LLM sessions — planner, worker, reviewer — are disposable. The only durable authority is a *non-LLM* controller process + its database + git. No conversation is ever the project's memory.
2. **A failed model call is a normal event, never a stop.** Any failure (429, 503, timeout, empty reply, no-progress, subscription limit) is classified, recorded, and routed around. The DAG always keeps moving on every task that is not directly affected. There is **no terminal FAILED state** for the project.
3. **Nobody approves their own work.** Implementer ≠ reviewer. Only the deterministic acceptance harness running against the exact integrated SHA, plus an independent review, can accept work. Only the deterministic release-gate script can say `RELEASE_READY`.
4. **Truth over theatre.** No fake metrics, fake activity, fake evidence, fixture "proofs" presented as live, or `{"restart_passed": true}` written by something that didn't restart anything. Unknown data shows as unknown.
5. **Never shrink the product.** Difficulty changes decomposition, not requirement status. A newer document forgetting an older requirement does not delete it.

---

## 1. WHAT IS BEING BUILT

### 1.1 Names (all refer to ONE product)
| Name | Status |
|---|---|
| **Empirium Studio** (descriptor: *AI Workforce*) | **Canonical** product brand (owner ruling S0.1, 2026-09-22) |
| AI Star Force, AI Staff Force, AI Taskforce, AI Workforce, AI Organization | Historical/working aliases — docs only |
| Personal Software Department | The first seeded department, not the product |
| "EMPIRIUM OS" text in mockups | Visual reference only. **Empirium OS (Ash's separate personal OS) is out of scope — do not modify it.** |
| Nailify / Nailed It / "Star Force X" | A *different* project. Only its controller code is reused (§6.2). |

Branding must be configurable so a rename never touches the domain model.

### 1.2 One-line definition (frozen, S0.2)
> Empirium Studio is a persistent AI workforce operations platform in which specialized digital employees, each with configurable models, MCP/tool access, memory, permissions and job rules, execute recurring, scheduled, event-driven and project-based work through durable workflows and handoffs, while the user plans, observes, approves, audits and improves that work through a truthful living-office control interface.

Mantra: *Define the work once. Give the right AI employee the right tools, model, memory and permissions. Let the system perform, hand off, repeat, learn and report.*

It is **not**: an agent dashboard, a roleplay toy, a Kanban board with robot graphics, a prompt library, a single coding orchestrator, a one-shot swarm, an LLM benchmark app, a scheduler without intelligence, Hermes Studio re-skinned, or a static animated office.

### 1.3 Canonical product specification
The **product contract** is `sources/EMPIRIUM_STUDIO_COMPLETE_PRODUCT_BRIEF.md` (4,353 lines, 2026-09-22) together with `sources/EMPIRIUM_HERMES_S0-S9_OWNER_ANSWERS_2026-09-22.md` (binding owner answers). Precedence for product meaning:

1. This prompt's §1 and §13 resolutions (they encode Ash's newest decisions, 2026-09-28).
2. Owner answers S0–S9 + G1–G6 rulings (2026-09-22).
3. The Complete Product Brief (2026-09-22).
4. The original Part A/B master protocols and the Context Dossier (`sources/history/`).
5. Mockups (`sources/mockups/` + `/home/ash/Desktop/AI Taskforce/`) for visual direction.
6. Earlier chat extracts (`sources/history/chunk_*.md`) for requirements not later removed.

The Architect phase (§8, F0) compiles these into an atomic requirement ledger. The old 710-item ledger (`~/empirium-studio/AI_WORKFORCE_BUILD/REQUIREMENTS_TRACEABILITY.json`) is an **input to reconcile**, not truth. Expect several hundred atomic requirements; do not cap the count.

### 1.4 Release tiers
**M0 — Foundation (first acceptance gate, not "done"):**
- M0.1 Durable domain: Organization, Department, Employee, Execution Profile, Workflow Definition, Schedule, Workflow Run, **Project**, Task/Step, Attempt/Run, Artifact, Handoff, Review, Approval, Notification, Memory, Knowledge reference, Event, Report, Temporary Worker, Crew. All distinct, never collapsed (Department ≠ Crew, Employee ≠ session/profile/worker, Run ≠ Task, Project ≠ Kanban card).
- M0.2 Durable scheduler: works with browser closed, persistent schedules, unique occurrence IDs, missed-run policy, no duplicates, timezone-aware (default Europe/London, UTC stored), DST tested, survives restart. Two *separate* proofs: browser-independence; missed-run recovery after service downtime.
- M0.3 Seed department **Personal Software** with 5 real persistent employees: **Director, Research Architect, Developer, QA Engineer, Learning Analyst.**
- M0.4 First real recurring workflow: **Steam + Epic free-games monitor** (dedup, artifacts, notification; both MATCH and NO_MATCH produce a persisted "checked" run record).
- M0.5 Second workflow: a small Personal Software change passing a **structured handoff** between employees, with an approval that pauses only the dependent path and resumes durably.
- M0.6 One fully animated, truthful living office (Personal Software); org overview uses throttled/snapshot mini-offices.
- M0.7 Reporting: ran today / succeeded / failed / waiting / needs attention / next scheduled / which employee-model-tool acted.
- M0.8 Form/template workflow creation without code.
- M0.9 ≥2 configurable model routes; ≥2 employees on different routes; per-employee policy visible; effective route telemetry recorded.
- M0.10 QA and approval provably distinct.
- M0.11 Persistent employee memory: write → kill session → retrieve → use, with provenance.
- M0.12 MCP/tool permission proof: one employee allowed, another denied **server-side**, audited.
- M0.13 Calendar/schedule view: next/recent occurrences, pause, run-now, edit recurrence.
- M0.14 One free-games run appears consistently in run history, activity feed, employee recent work, report, schedule history and office state simultaneously.

**CORE — required for release (all must pass):** everything in M0 plus: full learning/improvement loop (evidence-backed proposals, human approval for critical changes, versioned prompt/config with diff + rollback); full MCP registry + capability-management UI; cross-department workflows; voice/receptionist-capable employee type (provider chosen by evaluation, not pre-committed); visual workflow graph builder (mockup 1); operations/runtime health screen (mockup 2); richer calendar; multiple real departments (runtime create/rename/archive, tombstones, hard-delete approval-protected); advanced model routing + model performance comparison; employee dossier with versioned config; Organization overview (mockup 9) and Department cockpit (mockups 3–5, 7–8) at mockup density; agent click-through observability (why is this bot busy/blocked/scared); knowledge (Obsidian references, scoped global/department/project/employee); cost/model transparency (requested vs effective route, free/paid classification, tokens, attribution); responsive/mobile inspection + approvals; WCAG 2.1 AA; reduced motion; backups + versioned migrations with rollback; security (least privilege, server-side permission enforcement, no secrets in UI/logs/prompts).

**EXTENDED — optional, after CORE:** finance module/templates, multi-tenant SaaS, native mobile app.

### 1.5 The living office (the heart of the UI)
- **2D only** (no 3D engine). Lightweight renderer: evaluate the existing SVG/CSS `office-view.tsx` vs PixiJS in F0 and pick with measured evidence (bundle size, 60 fps on a normal desktop, CPU). Only the open department runs a full scene; offscreen/mini scenes pause or snapshot.
- **Canonical character: the yellow-head / blue-body bot** (mockup 6 turnaround sheet; palette Head Yellow, Head Shade, Body Blue, Accent Blue, Joint Grey, Top Cap Grey, Hand Yellow, Hand Accent, Eye Pupil, Eye Rim, Mouth Red). Build a **layered 2D puppet rig** (head, eyes, mouth, body, arms, claws, legs, cap, accessory) so many skins share one rig. Source art: `/home/ash/Desktop/AI Taskforce/AI agents taskforce future assets/Servbots/` (115 images) and `/Robots/` (11). The white/purple robots in some mockups are **not** the final characters.
- Skins are data (character bank; assign/swap per employee; missing-asset fallback; provenance metadata). Temporary workers look visibly temporary.
- Behaviour is **derived from real state**, never random decoration. Canonical state→behaviour map:

| Real state (with evidence) | Behaviour |
|---|---|
| idle | slow roam, look around, breathing/bob — never frozen |
| queued | glance at board, light pacing |
| thinking / planning | focused pacing |
| coding / terminal | sit at desk, type |
| research | read tablet / books |
| review / testing | inspect screen / QA console |
| dependency wait | coffee, stretch, look at collaborator |
| rate-limited | annoyed wait + timer (visibly NOT an error) |
| error | frustrated |
| blocked / needs Ash | urgent wave + alert marker, clickable |
| crash / timeout | frightened / confused, then recover |
| handoff | walk to recipient, pass token, brief exchange |
| changes requested | frustrated, return to desk |
| completed | short celebration → idle |
| offline | quiet low-energy loop |

- Clicking a bot opens its dossier (identity, role, config version, current task/project/run, effective model/provider, tokens/cost, current tool, last error, review status, skills/tools/MCPs, memory scope, permissions, history, links to chat/task/run/logs/evidence) and **explains why** it looks the way it does.
- Screen-reader list alternative, reduced-motion mode, the app fully usable without animation. 3–7 visible workers per room before grouping.
- **Tron Bonne ROM work is out of scope** (flagged as source-register contamination on 2026-09-22). Servbot *behaviour language* is inspiration only; ship original art.

### 1.6 Visual contracts (mockups)
Mockups in `sources/mockups/` (9 images supplied 2026-09-28) and `/home/ash/Desktop/AI Taskforce/`:
- **UI-REF-ORG-001** — Organization overview (image 9): KPI row (active employees, departments online, spend today, active projects, pending improvements, health with *documented formula*), department cards with mini-offices + agents/projects/spend/QA, Add Department card that persists a real department, activity chart, recent activity, upcoming tasks.
- **UI-REF-DEPT-001** — Department cockpit (images 3,4,5,7,8): global left nav; header (icon, name, purpose, status, motto, **New Project**, **Ask Department** — real actions); tabs Overview/Projects/Tasks/Agents/QA/Knowledge/Learning/History/Models & Cost/Settings; dominant living office with name/status tags; right rail Department Status + Live Activity; panels Active Projects, Upcoming Work, Completed Recently, Department QA, Knowledge (Obsidian), Learning & Improvements, Models & Cost.
- **UI-REF-WF-001** — Workflow Builder (image 1): node library (Trigger, Plan Task, Assign Agent, Conditional Branch, Delay, Retry Logic, Approval, Review, Notify, Publish + advanced), canvas, node configuration panel, test run, versions, publish.
- **UI-REF-OPS-001** — Operations / Runtime Health (image 2): services, workers, queues, providers, incidents, alerts, logs, request volume, provider latency, compute, subsystem status, remediation controls.
- Design language: dark navy, cyan/blue accents, controlled status colours, dense but legible, glow/glass cards, no dead space. Emit machine-readable design tokens. Match structure, hierarchy and density; **never copy the fake sample numbers**.

---

## 2. INPUTS YOU MUST READ FIRST

```
/home/ash/work/starforce-plan/
├── STARFORCE_AUTONOMOUS_BUILD_PROMPT.md   ← this file
├── sources/
│   ├── EMPIRIUM_STUDIO_COMPLETE_PRODUCT_BRIEF.md     ← product contract
│   ├── EMPIRIUM_HERMES_S0-S9_OWNER_ANSWERS_2026-09-22.md
│   ├── 00_READ_ME_FIRST.md, 11_HERMES_EXECUTION_HANDOFF_PROMPT.md
│   ├── FORENSIC_RETROSPECTIVE.md                     ← why every previous attempt failed
│   ├── mockups/upload_20260928_*.png                 ← 9 visual references
│   └── history/  (dossier, v1–v6 protocols, chat extracts chunk_00-11, raw chat corpus, repo_state.md, probe_findings.md)
/home/ash/Desktop/AI Taskforce/   ← asset folder (Servbots/, Robots/, dashboards, character sheets)
/home/ash/empirium-studio/        ← previous build (230 commits, 403/403 tests) — SALVAGE SOURCE, read-only
/home/ash/hermes-studio-control/  ← stable Hermes Studio base
/home/ash/Desktop/nailify/.hermes/autonomy/controller.py  ← proven SQLite controller skeleton to adapt
```

Read the Forensic Retrospective before designing anything. Its core lesson: *worker reliability never justified the orchestration built on top of it (~20% accepted attempts); nine director incarnations in nine hours; completion semantics were the root failure; measure one bounded task before building more machinery.*

---

## 3. WHAT WENT WRONG LAST TIME (do not repeat)
| Failure | Evidence | Rule now |
|---|---|---|
| Subscription loop died on session limit | `claude-autonomous-loop`: 30 passes, all `429 session limit`, zero commits | Detect limit, sleep until reset, keep free lanes running (§5.4) |
| Free-model workers timed out endlessly | `freellmapi-reef-loop-v2`: `hermes_exit=124` on most passes, commit frozen | Hard attempt timeout + no-progress kill + model ladder + task splitting (§5) |
| Single pinned model went dark | 2026-09-28 probe: 6/13 models 0% success (`out_of_credits`, reset ~10 min) | Circuit breaker per model, parse reset hint (§5.2) |
| Hermes Kanban board stalled | 27 ready cards idle 11.75 days; 1 card blocked 240 h | Controller owns dispatch; nothing can sit unowned (§6) |
| False `PROJECT_COMPLETE` | worker self-report reverted by orchestrator | Only `release_gate.py` may declare release (§10) |
| Fixture proofs passed off as live | Proofs A–D in `meta-director-checkpoint.json` | Commissioning uses real process kills (§7) |
| "One more supervisor" | 9 directors / 9 h; custom supervisor retired then re-introduced | Exactly one controller + one dumb systemd watchdog. No LLM supervisors (§6) |
| Scope collapse | Specs repeatedly shrunk into dashboards | Anti-scope-collapse law; ledger coverage check (§8) |
| Architecture churn without measurement | V1→V6 protocols in 5 days | Architecture is frozen by this prompt; change only via recorded ADR with evidence |
| Live service ran a stub | `hermes-studio.service` runs `/home/ash/hermes-studio` stub, not the build | Target runs as its own service on port 3003 (§9) |

---

## 4. MODEL ROUTING LAW (build-time)

Ash's standing rule (repeated 2026-09-17 ×3, 2026-09-28): **orchestration = Codex "Luna" (`gpt-5.6-luna`) via the ChatGPT/Codex subscription FIRST, Sonnet via the Claude subscription as the second planner; code grunt work = FreeLLMAPI pool; review + further planning = Opus via Claude subscription. No OpenRouter spending. No paid API fallback. ChatGPT "Luna" via OpenRouter is prohibited** (using the Codex CLI on the subscription is explicitly wanted and is NOT the prohibited OpenRouter route). New pay-as-you-go spend ceiling: **$0.00**.

**Owner update 2026-09-28 (latest wins): the planning lane is Codex `gpt-5.6-luna` on the ChatGPT/Codex subscription, not Sonnet.** Both subscriptions are separate accounts with separate windows, so the controller budgets each independently: exhausting the ChatGPT window must not block the Claude lanes and vice-versa. Lanes: `luna` = Codex CLI (`codex exec -m gpt-5.6-luna`, planning), `sonnet`/`opus` = Claude CLI (planner fallback / reviewer), `free` = Claude Code → freellm_shield → FreeLLMAPI (≈90% of coding). Codex is invoked with its own `CODEX_HOME` holding only the subscription auth, and **no API key of any kind is passed**, so it can never fall onto paid API billing. Codex reports tokens (not dollars): budget unit for the `luna` lane is kilo-tokens, learned from the first observed limit hit.

### 4.1 One harness for everything: Claude Code CLI
Verified live on 2026-09-28: FreeLLMAPI exposes an Anthropic-compatible `/v1/messages` endpoint, and Claude Code runs headless against it:
```bash
ANTHROPIC_BASE_URL=http://127.0.0.1:3101 \
ANTHROPIC_AUTH_TOKEN="$FREELLMAPI_API_KEY" ANTHROPIC_API_KEY= \
CLAUDE_CONFIG_DIR=$STATE/claude-free \
claude -p --model deepseek-v4-flashfree --dangerously-skip-permissions --output-format json "…"
```
(It wrote code and ran tests in ~10 s with `deepseek-v4-flashfree` and `gpt-oss-120b`. The `total_cost_usd` Claude Code prints is a fictional list-price estimate — the real cost is $0; record it but label it `estimated_list_price_not_billed`.)

**Workers never talk to FreeLLMAPI directly.** They go through the **FreeLLMAPI Shield** (`freellm_shield.py`, service `freellm-shield`, `127.0.0.1:3102` → `:3101`), already built and tested (§5.0). Worker env therefore uses `ANTHROPIC_BASE_URL=http://127.0.0.1:3102`, `ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-5`, `ANTHROPIC_SMALL_FAST_MODEL=claude-haiku-4-5` (names are placeholders the shield maps onto its ladder), `API_TIMEOUT_MS=3000000` (the shield may legitimately hold a request for up to 45 min while it retries), `CLAUDE_CODE_MAX_RETRIES=10`.

So every lane uses the same tool, same worktree semantics, same JSON result format:

| Lane | Invocation | Used for |
|---|---|---|
| **FREE** (bulk) | Claude Code → FreeLLMAPI (`ANTHROPIC_BASE_URL` override, separate `CLAUDE_CONFIG_DIR`) | implementation, tests, refactors, asset scripts, first-pass research, free pre-review |
| **SONNET** (planner) | Claude Code, subscription login, `--model sonnet` | decomposition, re-specifying failed tasks, integration conflict resolution, daily progress digest |
| **OPUS** (reviewer) | Claude Code, subscription login, `--model opus` | architecture freeze, harness review, batched code review, visual QA (screenshots), diagnosis of repeatedly failing tasks, milestone and final acceptance |

Subscription lanes must run with **no `ANTHROPIC_API_KEY` / `ANTHROPIC_BASE_URL` in the environment** (strip them), so they can never fall onto API billing.

**Silent-failure guard (this has bitten Ash before):** a subscription call only counts as successful if the JSON result has `is_error=false`, non-empty `result`, and `modelUsage` contains the requested model family. Anything else is classified (§5.1) — never treated as a pass.

### 4.2 Free model ladder (starting order, then re-ranked by B0 data)
From live routing telemetry, start with FreeLLMAPI `auto` so it can choose a healthy free provider. Named routes are fallbacks in this order: `nemotron-3-super-120b`, `mistral-code`, `codestral-2508`, `gpt-oss-120b`, `mimo-v2.6-flashfree`, `deepseek-v4-flashfree`. Probe-only candidates, add when healthy: `glm-5.3`, `glm-5.3-fast`, `kimi-k3-fast`, `qwen3.6-27b`, `qwen3.7-flash`, `devstral-2`. The ladder lives in the controller DB (`model_routes` table), not in code, and is re-ranked by measured first-review acceptance rate (§8 B0, then continuously).

- **Do not use** FreeLLMAPI entries that are subscription models in disguise (`claude-*`, `gpt-6-*`, `gpt-5.6-*`) as free workers unless the route's effective provider is proven $0 and it is not an OpenRouter-paid route.
- OpenRouter: effective routes ending `:free` are $0 and allowed (Ash explicitly used `openrouter …:free` on 2026-09-22); **any non-`:free` OpenRouter route is denied** by a deterministic post-response guard that reads the attribution FreeLLMAPI returns. Log every effective route.

### 4.3 Product runtime routes (M0.9)
Ollama has **no models installed**, so Route A = FreeLLMAPI quality route (e.g. `gpt-oss-120b`), Route B = a different FreeLLMAPI family (e.g. `mistral-code`). Both configurable per employee/step. Do not install Ollama models just to satisfy the test.

---

## 5. NEVER-STALL DESIGN (Ash's hard requirement, 2026-09-28)

> "When an LLM call fails, that stalls the entire project, and we can't allow that to be an issue."

### 5.0 Request-level shield (built 2026-09-28, tested — do not rebuild, extend if needed)
FreeLLMAPI's nature, from the logs: individual requests fail constantly (429 `out_of_credits`, 503 `No candidate`, `Provider stream returned an error event`, hung streams, empty replies, repetition/"script-salad" garbage, and a gateway-wide 120-request window). In the previous build **one** such failed request killed the whole worker session — 30 of 84 attempts ended `TIMEOUT` and 23 `NO_PROGRESS` with `effective_model=unknown`. The fix is to make individual request failure invisible to the worker:

- `freellm_shield.py` receives every worker request and **re-sends it until it gets a valid reply**: next model in the ladder on each failure, per-model circuit breakers (parsed `reset ~Nm`, else escalating backoff), FreeLLMAPI's global `X-RateLimit-*` window respected, reply validation (non-empty, no repetition loop, no garbage, well-formed tool calls), non-streaming upstream so broken streams can't corrupt a turn (SSE is synthesised for the worker, with keep-alive pings while it retries), sticky model per worker session, recovered models re-probed every 5 min.
- If every model is cooling down, the request **waits** (up to 45 min) instead of failing. Only then does it return HTTP 529, which Claude Code itself retries.
- Effective route from `X-Routed-Via` is logged per try in `~/.local/state/freellm-shield/shield.db` (`tries` table) — the controller reads it for model ranking and for the paid-route guard (non-`:free` OpenRouter routes are rejected and retried elsewhere).
- Ladder is `~/.local/state/freellm-shield/ladder.json`, re-ranked by the controller from B0 and ongoing acceptance data. Subscription look-alike names (`claude-*`, `gpt-6*`, `gpt-5.6*`, `*luna*`) can never be selected.
- Evidence: `tests/test_shield_faults.py` 6/6 pass (429, 503, empty, garbage loop, hang, flaky, 25 s total outage, 8 concurrent); live run: a Claude Code worker built a module + 7 passing tests in 44 s while 3 dead models at the head of the ladder were skipped automatically.
- Note: FreeLLMAPI may serve a request with a different model than asked (observed: `mistral-code` requested, `openrouter/…dots-3-note-preview:free` served). Rank models on the **effective** route, not the requested name.

The layers are therefore: **request** (shield: retry until valid) → **attempt** (controller: timeout / no-progress / re-queue on another model, §5.1–5.2) → **task** (re-spec, split, diagnose, park) → **project** (never ends before release, §15).

### 5.1 Failure taxonomy (every attempt gets exactly one)
| Class | Detection | Response |
|---|---|---|
| `RATE_LIMITED` | HTTP 429 / `rate_limit_error` / `out_of_credits` | open model breaker for parsed `reset ~Nm` (default 10 min); requeue same task on next ladder model immediately |
| `PROVIDER_DOWN` | 5xx, `No candidate model`, connection refused | breaker 5 min, exponential up to 60 min; next model |
| `EMPTY` | 200 with empty/whitespace result or no tool use | breaker 2 min; next model |
| `TIMEOUT` | attempt exceeded wall-clock budget (default 25 min implement, 15 min review) | kill process group; next model; if 2× on same task → **split task** |
| `NO_PROGRESS` | no git diff change and no new tool call for 8 min, or finished with zero diff on an implement task | kill; next model; 2× → split/re-spec |
| `TEST_FAILED` / `HARNESS_FAILED` | acceptance harness exit ≠ 0 | back to same task with failing output attached (counts toward strategy change) |
| `REVIEW_REJECTED` | reviewer verdict `CHANGES_REQUESTED` | rework with exact defects |
| `SUB_LIMIT` | subscription JSON `api_error_status=429` or "session limit · resets …" | set lane-wide cooldown until parsed reset + 2 min; **free lane continues** |
| `POLICY_VIOLATION` | paid/unknown route, secret in output, write outside worktree | discard attempt, disable route, record incident |
| `CRASH` | non-zero exit not matching above | retry once on same model, then next |

### 5.2 Mechanisms
1. **Per-model circuit breakers** in the DB (`model_routes.breaker_until`, rolling success rate). A 1-token health probe runs every 5 min per model (cheap, bounded) and closes breakers early when a model recovers.
2. **Fallback ladder per attempt**, not per project: an attempt picks the best closed-breaker model ranked by acceptance rate for that task class. Switching model mid-task is normal and recorded.
3. **Attempt ≠ task.** A task persists; attempts are disposable. Every attempt runs in its own git worktree, under its own lease with expiry, in its own process group with a hard timeout.
4. **Parallel DAG.** Up to `MAX_FREE_WORKERS` (start 2, raise to 4 then 6 only if first-review acceptance ≥60% and host RAM < 75%) run concurrently on *different* ready tasks. A failing task never blocks unrelated tasks.
5. **Strategy change, not repetition.** After 2 same-class failures on one task: Sonnet re-specifies or splits it. After 4 total failed attempts: Opus diagnoses. After 8: task is `PARKED_NEEDS_REDESIGN` and its dependents wait while everything else proceeds; parked tasks get a batched Opus redesign pass every 6 h. Nothing is ever abandoned silently.
6. **Subscription cooldown is not a stall.** When Sonnet/Opus are cooling down: implementation continues; tasks awaiting review queue in `AWAITING_REVIEW`; integration of unreviewed work waits; a **WIP cap** (max 12 unreviewed accepted-by-harness tasks) throttles new implementation of dependent work only. Free pre-review (different model family from the implementer) runs meanwhile so Opus reviews arrive at pre-filtered diffs.
7. **Everything-down mode.** If all free breakers and both subscription lanes are open, the controller sleeps until the earliest reset (max 10 min per sleep), logs `WAITING_FOR_CAPACITY` as a visible state, and resumes automatically. It never exits.
8. **Idempotent steps.** Every controller action is a DB transaction keyed by task/attempt ID; restart replays from DB. Expired leases → `recovery_needed` → resume from the worktree's dirty state rather than restarting from scratch.
9. **Quota hygiene.** Never replay an identical request after an identical failure; never run the whole ladder twice for one attempt; cap concurrent requests per model at 1 while its success rate < 50%.

### 5.3 Liveness supervision (dumb, deterministic)
- `empirium-build-controller.service` (systemd **user**, `Restart=always`, `RestartSec=10`, linger enabled) runs the controller.
- `empirium-build-watchdog.timer` (every 5 min) runs a ≤60-line script: if heartbeat older than 3 min → `systemctl --user restart` the controller; enforces single instance via `flock`. **No LLM in the watchdog. No second supervisor.**
- **Progress SLA:** if no task reaches `ACCEPTED` in 6 h while work exists, the controller itself enqueues one Opus `DIAGNOSE_STALL` task (normal task, normal review) — not a new supervisor.

### 5.4 Subscription usage planning
Claude subscription windows are ~5 h. Budget Opus deliberately: batch reviews (5–10 small tasks per review session, diff + harness output + screenshots), reserve ~20% of each window for diagnosis. Sonnet planning calls are short and bounded. Record per-window usage in the DB to learn the real limit.

---

## 6. BUILD ARCHITECTURE

### 6.1 Topology
```
systemd --user
 ├─ empirium-build-controller.service   (Python, deterministic, SQLite WAL)
 │     ├─ spawns FREE workers   : claude -p → FreeLLMAPI     (worktrees)
 │     ├─ spawns SONNET planner : claude -p --model sonnet   (subscription)
 │     ├─ spawns OPUS reviewer  : claude -p --model opus     (subscription)
 │     ├─ runs acceptance harness (verify.sh) on exact SHAs
 │     ├─ merge queue → integration branch → re-run harness
 │     └─ release_gate.py (the only thing that can say RELEASE_READY)
 ├─ empirium-build-watchdog.timer       (heartbeat, FreeLLMAPI, disk, product; + crontab layer, §15)
 └─ empirium-studio.service             (the product, port 3003, from integration branch)
```

### 6.2 Controller implementation
- **Start from** `/home/ash/Desktop/nailify/.hermes/autonomy/controller.py` (436 lines: leases, recovery, verify, release gate, reconcile loop). Strip Nailify semantics; extend with §5 failure handling, model routes, three lanes, merge queue, review batching.
- Location: `/home/ash/empirium-studio-v2/.build/controller/` (code, versioned) with runtime state in `~/.local/state/empirium-build/` (`build.db`, logs, attempt transcripts, leases). One canonical state root; never a second copy under `~/.hermes/`.
- Tables (minimum): `requirements, work_items, dependencies, attempts, leases, model_routes, provider_events, reviews, artifacts, evidence, decisions, incidents, lane_cooldowns, heartbeats, release_gate_runs, events`.
- Work item statuses: `todo → ready → running → harness → awaiting_review → changes_requested → accepted → integrating → integrated`; side states `parked_needs_redesign`, `waiting_dependency`, `waiting_capacity`, `recovery_needed`. No `failed` terminal state.
- Worker prompt = a **packet** file (goal, requirement IDs, allowed file scope, contracts to obey, out of scope, acceptance commands, evidence required, prior failure output). Packets are ≤ 6k tokens; workers get the packet, not transcripts. Handoffs are structured JSON + short markdown (base SHA, result SHA, files, commands + exit codes, evidence paths, assumptions, open issues).
- Worker sandbox: write only inside its worktree; no access to `~/.hermes`, secrets, other repos, systemd; env stripped of paid API keys. Worker cannot merge.
- Visibility for Ash (read-only): a `status` CLI (`python3 controller.py status`) printing phase, counts per status, lane cooldowns, breaker states, last 20 events, release-gate summary; and a nightly markdown digest written to Obsidian `Empirium Studio/Build Log/YYYY-MM-DD.md`. Optional: mirror work items read-only into Hermes Kanban board `empirium-studio-v2-build` (owner ruling G5) — the mirror is never the authority.

### 6.3 Why not the alternatives (decision record)
- **Hermes Kanban as authority** — tried; the board stalled 11+ days with no owner. Kept only as optional read-only mirror.
- **One long Claude session / `/goal` / `/loop` / ralph loop** — dies on session limits and context; exactly the failure Ash keeps hitting.
- **CAO** (`empirium-cao.service`) — a session transport, not a state authority; adds a layer without solving failure routing. Leave it running; don't depend on it.
- **Temporal / Hatchet** — durable-execution engines are sound but heavy for a 16 GB CPU VPS and add a second authority. The controller is a few hundred lines with SQLite; revisit only if the controller becomes the bottleneck (recorded ADR required).
- **OpenCode / Aider** as free workers — viable, but Claude Code → FreeLLMAPI is already proven working here and gives one uniform harness and JSON result format across all three lanes.

---

## 7. COMMISSIONING — PROVE THE CONTROLLER BEFORE ANY PRODUCT WORK

Run against a **disposable fixture project** (`~/empirium-build-fixture`, 6 tiny work items, one deliberately failing test, one deliberate review rejection). All proofs use real processes and real kills; evidence = logs + DB rows + PIDs, captured by script.

| Proof | Must show |
|---|---|
| C1 restart | `kill -9` the controller mid-attempt → systemd restarts it → lease expires → attempt `recovery_needed` → resumed; no duplicate attempt |
| C2 model failure | force a breaker open (point one route at a dead port) → next model used within 60 s, other tasks unaffected |
| C3 timeout / no-progress | a packet that makes the worker idle → killed at budget, classified, requeued on another model, split after 2 |
| C4 review loop | deliberate defect → Opus (or Sonnet if Opus cooling) `CHANGES_REQUESTED` bound to exact SHA → rework → accept → merge → harness re-run on integrated SHA |
| C5 subscription limit | simulate by wrapping the subscription CLI to return the real 429 JSON shape → lane cooldown set, free lane keeps working, auto-resume after "reset" |
| C6 all-down | all routes dead → `WAITING_FOR_CAPACITY`, controller alive, resumes when a route returns |
| C7 reboot-survivable | `systemctl --user daemon-reload`, stop/start, linger check; state intact |
| C8 no self-approval | a worker that writes `PROJECT_COMPLETE` / edits the gate file → ignored, incident recorded |
| C9 no paid route | a route whose attribution is non-`:free` OpenRouter → rejected before result is used |

C10–C12 are defined in §15.3. C5 is the only simulated proof and must be labelled so; the first real session limit in production must be logged as the live confirmation. Only when C1–C12 pass does the controller take the real project.

---

## 8. PHASES (the controller runs these; the bootstrap session only does P0–P1)

| Phase | Owner | Exit condition |
|---|---|---|
| **P0 Bootstrap** | bootstrap runner (§14) | environment facts recorded (`.build/FACTS.md`: SHAs, ports, services, Node/pnpm, Postgres, FreeLLMAPI health, Claude CLI auth, RAM/CPU); v2 repo created; controller written + unit-tested |
| **P1 Commission** | bootstrap runner (§14) | C1–C12 pass + independent review; controller, watchdog + cron layer enabled; real project registered; runner exits |
| **F0 Architecture freeze** | Opus task(s) | salvage audit of `~/empirium-studio` (KEEP/ADAPT/REPLACE/LEGACY per module); requirement ledger compiled (hundreds, each with acceptance predicate + tier); ARCHITECTURE.md, domain schema, API contracts, event taxonomy, state→animation map, design tokens, renderer decision (measured); reuse matrix vs Hermes Studio; acceptance harness `verify.sh` + per-requirement checks; calibration fixtures proving the harness rejects known-bad code; frozen and hashed |
| **B0 Worker benchmark** | controller | one frozen bounded task × 20 attempts from the same base SHA across the ladder; independent acceptance. **≥60% accepted → proceed automatically (this prompt is the launch authorisation).** 30–59% → improve packets/decomposition and rerun (no new supervisor layer). <30% → Opus redesign of packets + smaller task granularity, rerun. Results re-rank the ladder |
| **F1 Domain + persistence** | free workers | M0.1 domain in Postgres with versioned migrations + rollback, backups, seed Personal Software + 5 employees |
| **F2 Execution + scheduler** | free workers | M0.2, M0.4, M0.5, M0.9–M0.12 |
| **F3 Core UI shell** | free workers | Org overview, Department cockpit, dossier, reports, calendar, workflow form builder — real data only |
| **F4 Living office** | free workers + Opus visual QA | rig, skins, state machine, pathing, handoff/celebration/fright animations, perf budget, a11y alternative |
| **F5 M0 acceptance** | harness + Opus | all M0 predicates pass on the integrated SHA; M0.14 consistency proof; this is **not** release |
| **F6 CORE completion** | free workers | all CORE requirements (§1.4) incl. visual workflow builder, ops screen, learning loop, MCP registry, cross-dept, voice-capable employee, multi-department |
| **F7 Hardening** | controller | security review (Opus), restart/soak (48 h burn-in with scheduled workflows firing), failure injection, performance (60 fps office, no leak after 50 navigations), accessibility audit, backup/restore + migration rollback test, responsive checks |
| **F8 Release** | release_gate.py + Opus | all CORE predicates pass with fresh evidence on frozen SHA; zero open CRITICAL/HIGH; visual acceptance; autonomous demo (§10.2) recorded; `RELEASE_READY` written by the gate script only |

Campaign checkpoint (owner S6.11): 200 valid attempts per phase-rebaseline or 14 calendar days without F5 → Opus writes `DIAGNOSTIC_REPORT.md` with a re-plan, Ash is notified once (§12), and the controller **applies the re-plan and keeps running**. It is a checkpoint, not a pause, not failure and not completion.

---

## 9. PRODUCT ENGINEERING DECISIONS (resolved — do not reopen)

| Topic | Decision | Source |
|---|---|---|
| Repo | New clean repo `/home/ash/empirium-studio-v2`, branched from the newest locally-proven Hermes Studio (`hermes-studio-control`, verify it builds and tests first; freeze the base SHA). Old `~/empirium-studio` preserved untouched as salvage source + evidence. | S2.1, G4 |
| Salvage | Port KEEP modules from old repo: `src/server/workforce-*.ts`, department/employee stores, Postgres adapter pattern, `office-view.tsx` (SVG office, 3 layouts), tests (403 passing). Discard the reconciler/director/proof machinery and the 112+ stale worktrees (don't delete; just don't carry forward). | repo_state.md |
| Database | **PostgreSQL** is the single operational authority (already running, existing adapter + integration tests pass). Add versioned migrations **with down-migrations**, nightly + pre-migration backups, restore test. No dual authority, no localStorage for business data. Build-controller state is separate (SQLite). | 09-18 + mandate §7D |
| Task authority | Product's own Task/Project tables. Hermes Kanban may be an *execution adapter* but never a competing mutable queue. | S2.5 |
| Hermes reuse | Profiles = execution profiles (≠ employees). MCP = reuse. Hermes cron only if it meets durability/timezone/missed-run/occurrence-identity; otherwise product scheduler. Conductor/Crews only for bounded temporary execution. | S2.5 |
| Stack | Keep Hermes Studio's stack (React 19, TanStack Router/Query, Vite, TypeScript, Vitest, Playwright, pnpm). No framework churn. | S2.8 |
| Delivery | Web app on VPS, `empirium-studio.service`, port **3003** (config-driven), bind localhost + Tailscale; no public exposure. Don't touch ports 3000/3001 or Empirium OS. | S0.9, G3 |
| Secrets | Existing Hermes/host secret store or 0600 env file loaded by systemd; never in UI/logs/prompts/artifacts. | S1.7 |
| Users | Single operator now; permissions are real server-side policy objects. | S0.7 |
| Timezone | Europe/London default, configurable, UTC storage, DST tests. | S0.13 |
| Git | Small coherent commits, task ID in message, identity `Empirium Build <build@local>`; private GitHub remote only if one already exists; never force-push. | S2.7 |
| Testing | Headless Playwright, deterministic viewports 1536×1024, 1366×768, 1920×1080, 768 tablet, 390 mobile; limited concurrency on the VPS. | S2.10 |
| Knowledge | Obsidian vault `/home/ash/Documents/Obsidian Vault` = human-readable knowledge; operational truth stays in Postgres. | dossier §19 |
| Health metric | Either a documented formula shown on hover, or replaced with a truthful status summary. | dossier §22 |

---

## 10. ACCEPTANCE & RELEASE

### 10.1 Acceptance rule per work item
Accepted only when: harness passes on the exact result SHA → free pre-review passes → **Opus review** (batched) approves the exact SHA → merged by controller → harness re-passes on the integrated SHA. Visual items additionally need Playwright screenshots at the reference viewports reviewed by Opus against the named UI-REF contract with concrete defect lists. "Tests pass" ≠ visual acceptance; "looks like the mockup" ≠ functional acceptance.

### 10.2 Autonomous demonstration (release requirement)
From the finished UI: create a small real software task for Personal Software → Director decomposes → Developer bot visibly changes state → implementation runs → QA rejects a seeded defect (frustrated bot) → rework → approval requested (urgent bot) → approved in UI → integration → project complete → run, evidence, model and cost inspectable → close browser, restart service, reopen: state intact. Plus: free-games workflow fires on schedule with browser closed, appears consistently everywhere (M0.14).

### 10.3 `release_gate.py` (deterministic)
Checks: every CORE requirement has a passing predicate with evidence ≤ 72 h old on the frozen SHA; zero open CRITICAL/HIGH defects; typecheck/build/unit/integration/E2E green; 48 h soak with zero lost runs; restart + failure-injection suite green; migration rollback + backup restore green; perf + a11y budgets met; visual acceptance recorded; security review with no blockers; no paid spend recorded; Empirium OS and `hermes-studio-control` unchanged (git status/SHA check). Writes `RELEASE_GATE.json` with `exitCode`. Only a green gate may write `RELEASE_READY`.

### 10.4 Not completion
M0 passing; dashboards looking good; empty queue; no active workers; a subset of tests passing; any LLM saying "done"; the office rendering; the free-games workflow working.

---

## 11. SAFETY & SCOPE BOUNDARIES
Authorised without asking: enabling `freellm-shield.service`; everything reversible inside `~/empirium-studio-v2`, its worktrees, `~/.local/state/empirium-build/`, the fixture project, new systemd **user** units for this project, a new Postgres database/schema for this project, installing npm packages, Playwright browsers.
Never: modify Empirium OS, `hermes-studio-control`, `hermes-studio` (live service), other repos, other users' Hermes profiles/memory, existing Postgres databases of other services; delete the old `empirium-studio` repo; public exposure / firewall / DNS changes; paid inference or buying credits; force-push; leaked or unauthorized assets; storing secrets in the repo.

---

## 12. OWNER INTERRUPTION POLICY
Do **not** ask Ash about: retries, test fixes, re-dispatching, waiting for providers, choosing between reversible approaches, moving to the next phase, running QA/soak, model switches within policy.
**Only** notify Ash (Telegram via Hermes, one message, then continue other work) for: a credential/login action only he can do; a required `sudo` command (give the exact command); an irreversible/destructive decision; a genuine product decision absent from every source; a security incident; the 14-day checkpoint report; `RELEASE_READY`.

---

## 13. RESOLVED CONFLICTS (so no agent re-litigates them)
| Conflict in history | Resolution | Why |
|---|---|---|
| Build inside Hermes Studio embedded in Empirium OS (09-15) vs standalone Studio fork (09-16 → 09-22) | **Standalone Hermes Studio fork, separate from Empirium OS** | Latest explicit owner decision (S0.1, V5, brief §3) |
| Opus/Sonnet (09-17) vs Luna/Sol only (V5, 09-19) vs Sonnet orchestrator + Opus review (09-28) | **Sonnet + Opus via Claude subscription; FreeLLMAPI for code** | Newest statement (09-28) + standing memory rule; Luna via OpenRouter prohibited |
| SQLite-first (S1.1) vs PostgreSQL authority (09-18) | **PostgreSQL** | Mandate §7D permits retaining validated Postgres; avoids rewriting salvaged tested code |
| OpenRouter banned entirely (V5) vs Ash using `openrouter …:free` (09-22) | **$0 `:free` routes allowed via FreeLLMAPI; any paid OpenRouter route technically blocked** | Latest owner behaviour; $0 ceiling preserved |
| Robots (09-15 AM) vs character sheets (09-15 PM) vs white robots in some mockups | **Yellow/blue bot rig** | "Use these characters instead of the robots"; V5 "blue-and-yellow bot is canonical"; 09-28 turnaround sheet |
| Tron Bonne ROM R&D (09-16) vs contamination flag (09-22) | **Out of scope** | Latest; ship original art |
| Two approval gates after B0 (09-22 12:47) vs auto-launch (09-22 14:38) | **Auto-launch F1 when B0 ≥60%** | Later mandate supersedes |
| 30 / 40 / 50 consecutive failures before escalating | **Replaced** by class-based breakers + 2-failure strategy change (§5) | "Do NOT wait for 30 identical failures" (09-18); 09-28 no-stall requirement |
| Custom heartbeat supervisor / Meta-Director / CAO-as-orchestrator | **One deterministic controller + dumb watchdog** | Retrospective; V6 "no custom supervisor watching an LLM PID" — the controller supervises work, not an LLM |
| Hermes Kanban board `empirium-studio-v2-build` as authority (G5) | **Optional read-only mirror** | Board-authority stalled for 11 days; deviation recorded here |

---

## 13b. OWNER ANSWERS 2026-09-28 (binding)
1. **Employees ("servbots") are the core abstraction.** Each employee is a worker with one very specific function; work from one servbot is handed to another for further work; employees collaborate on **workstreams**. Ash must be able to **add new specific employees at any time** from the UI (name, one precise function/job contract, model route, tools/MCPs, memory scope, permissions, skin) without code changes, and wire them into workstreams/workflows. The departments and roles in the mockups are *suggestions*, not a fixed roster. Therefore: seed Personal Software with its 5 employees (needed for M0); create the other mockup departments only as editable examples with **no fabricated activity**; the "Add Employee" and "Add Department" flows and the employee-to-employee handoff chain are CORE and must be excellent. Workstream = a workflow whose steps are assigned to specific employees with structured handoffs between them.
2. **Claude subscription budget: up to ~70% of each 5-hour window** for the build (Sonnet + Opus combined); ~30% stays free for Ash. The controller tracks per-window usage and stops dispatching subscription work at the 70% mark until the window resets (free lanes continue).
3. **Notifications: Telegram via Hermes** — `hermes send -t telegram "<message>"` (no LLM, works without the gateway). One message per event, never spam.
4. **Tron Bonne disc-image research: dropped.** Servbot behaviour is inspiration only; original art.
5. **Launch authorised:** old Kanban workers stopped, old repo untouched, shield + bootstrap services started.
7. **Maximise free-model fan-out (2026-09-28, binding):** Codex/Luna's primary job as planner is to **decompose work into as many independent, individually-verifiable `free`-lane items as the work honestly allows** — the free FreeLLMAPI lane runs many workers concurrently at zero marginal cost, while the subscription lanes are the scarce resource. The planner prompt (`escalate.FORMAT`) states this explicitly, and `max_free_workers` ships at **6** concurrent free workers (the RAM governor in `safety.resources()` may throttle this live and restores it automatically when memory frees). Over-declaring dependencies serialises the build and is a planning failure; items that can start immediately must carry no deps.
8. **Opus 5.5 runs at MEDIUM effort only (2026-09-28, binding):** every Opus invocation carries `--effort medium` (`cfg.opus_effort`), passed **per-invocation** in `workers.worker_cmd()` so the global `~/.claude/settings.json` value (`effortLevel: high`) can never leak into review spend. Verified: the CLI accepts `low|medium|high|xhigh|max` and warns on anything else. Codex's reasoning effort is likewise pinned per-invocation (`-c model_reasoning_effort=medium`, `cfg.codex_effort`) so a future `config.toml` edit cannot silently raise it and drain the ChatGPT window.

## 14. BOOTSTRAP — HOW P0–P1 RUN
P0–P1 are **not** run by a long chat session. They are run by `/home/ash/work/starforce-plan/bootstrap_runner.py` as `empirium-bootstrap.service` (systemd user unit, restart on failure). The runner launches a disposable worker per step — **Codex `gpt-5.6-luna` on the ChatGPT subscription (primary planning lane)**, falling back to `claude -p --model sonnet` on the Claude subscription — and advances **only when a deterministic check passes** (file/test/evidence/heartbeat), never on the worker's say-so. On a subscription session limit it sleeps until the parsed reset; after 3 failures on a step, or while a subscription is cooling down, it runs the same step on the free lane (Claude Code → FreeLLMAPI ladder with breakers). The commissioning review is requested and recorded by the runner itself (Opus, fallback Sonnet), not by the worker being reviewed. When the last step passes it writes `BOOTSTRAP_COMPLETE` and exits; the controller owns the project from then on.

If you are a bootstrap worker, you are executing one of the steps below. Inspect the current state first (a previous worker may have done part of it), continue from there, commit, and stop when your step is done:

1. Read §2 inputs (brief, owner answers, retrospective, this prompt). Write `.build/FACTS.md` from live commands, not assumptions.
2. Verify FreeLLMAPI health (`/v1/models`, one `/v1/messages` call) and Claude subscription auth (`claude -p --model sonnet "reply OK" --output-format json`, check the §4.1 guard). If subscription auth is missing → §12 notify; continue with free-lane-only commissioning meanwhile.
3. Create `~/empirium-studio-v2` from `hermes-studio-control` (verify baseline `pnpm install && pnpm build && pnpm test` first; record SHA). Branch `main`, integration branch `integration`.
4. Build the controller (§6.2) with unit tests for every §5.1 class and every state transition. Build `verify.sh` skeleton, `release_gate.py`, watchdog script, systemd units.
5. Build the fixture project and pass C1–C12 (§7 + §15.3). Store evidence under `.build/evidence/commissioning/`.
6. Enable `empirium-build-controller.service` + watchdog timer; `loginctl enable-linger ash` if not already (if it needs sudo → §12 with exact command).
7. Seed the controller with the F0 work items (Opus lane) and the phase plan (§8). Confirm the controller dispatches the first F0 task and records a heartbeat.
8. Write the handover summary to Obsidian `Empirium Studio/Build Log/` and exit. **From here the controller owns the project.** If this session is reopened later, it must only run `controller.py status` and act on §12 items — never become a second orchestrator.

---

## 15. FAIL-SAFE MATRIX — EVERY WAY IT CAN STOP, AND WHAT RESTARTS IT

Design rule: **every component that can stop has something outside it that restarts it, and every restart resumes from durable state.** No single process, session, model, provider or file is a point of failure. The controller must implement every row below and C10–C12 must prove the new rows.

### 15.1 Supervision layers
| Layer | What | Restarted by |
|---|---|---|
| L0 | worker attempts (disposable `claude -p`) | controller (timeout, no-progress kill, requeue on another model) |
| L1 | `empirium-build-controller.service` | systemd `Restart=always`, `RestartSec=10`, `StartLimitIntervalSec=0` (never gives up) |
| L2 | `empirium-build-watchdog.timer` (every 5 min) | systemd timer; checks controller heartbeat + FreeLLMAPI + disk + product service |
| L3 | user **crontab** entry (every 15 min) running the same watchdog script | cron — independent of the systemd user manager, so if timers are broken it still fires |
| L4 | boot | linger is **already enabled** for `ash` (verified 2026-09-28); all units `WantedBy=default.target`; crontab `@reboot` entry as belt-and-braces |
| L5 | the build itself stalling (running but not progressing) | progress SLA → automatic Opus `DIAGNOSE_STALL` task; escalating SLA ladder in 15.2 |

### 15.2 Failure → automatic response
| # | Failure | Automatic response | Human needed? |
|---|---|---|---|
| 1 | Free model 429/503/empty/timeout | breaker for parsed reset; next model (§5) | No |
| 2 | All free models down | `WAITING_FOR_CAPACITY`; sleep ≤10 min; 1-token probes; resume | No |
| 2b | **Shield process dead** | systemd `Restart=always` (5 s); watchdog also checks `127.0.0.1:3102/health` and restarts it; workers' own retries (`CLAUDE_CODE_MAX_RETRIES=10`) cover the gap | No |
| 3 | **FreeLLMAPI process dead or hung** (`/v1/models` fails 3× in 3 min) | watchdog restarts it: `systemctl --user restart <unit>` if it has one; else re-exec its recorded start command (F0 records the exact start command/PID owner in FACTS.md and creates a user unit for it if it runs as `ash`). While down, planning/review on subscription lanes continue. If FreeLLMAPI (verified: Docker container `freellmapi-freellmapi-1`, `restart: unless-stopped`, root-owned — Docker itself restarts it on crash) is hung but not crashed and cannot be restarted as `ash` → keep running subscription lanes (Sonnet implements, bounded by §15.4), notify Ash once with the exact restart command | Only if root-owned *and* down >2 h |
| 4 | Claude subscription session limit | lane cooldown until parsed reset + 2 min; free lanes continue; reviews queue | No |
| 5 | Opus unavailable >12 h (limit/outage) | **Sonnet becomes reviewer** (different model from any implementer); reviews tagged `reviewer_fallback=sonnet`; Opus re-reviews those SHAs in batch when it returns — a rejection reopens the item | No |
| 6 | Sonnet unavailable (planner) | Opus plans; if both unavailable, planning waits while implementation/harness continue on already-specified tasks; free-lane "split task" planner (strongest free model, then structural split by file) handles re-specification | No |
| 7 | Both subscription lanes down >24 h | free-lane reviewer from a *different model family* than the implementer is allowed for non-visual, non-security items with harness green; those items are flagged `provisional` and must be re-reviewed by Opus before F5/F8 gates count them | No |
| 8 | Claude CLI logged out / auth expired | detect (`claude -p "OK"` auth error); free lanes continue with rule 7; one notification to Ash with the exact `claude /login` step (vault/OAuth is his action) | Yes — one login, build keeps going meanwhile |
| 9 | Controller crash | systemd restart; leases expire → `recovery_needed` → resume dirty worktree | No |
| 10 | Controller hang (heartbeat stale >3 min) | watchdog `kill -9` + restart | No |
| 11 | Controller crash-loop (≥5 restarts / 10 min) | watchdog starts it in `--safe-mode`: skip the work item implicated in the last 3 crashes (mark `parked_needs_redesign`), run DB integrity check, restore last good DB backup if corrupt, continue | No |
| 12 | Controller DB corruption | `PRAGMA integrity_check` on start; auto-restore from hourly backup (keep 48); replay git + evidence to rebuild lost rows | No |
| 13 | Worker hangs / zombie process | process-group kill at budget; orphan reaper on every loop kills any `claude` process not owned by a live lease | No |
| 14 | Disk filling | janitor every hour: prune integrated/abandoned worktrees, compress transcripts >3 days, keep last 20 attempts per item; at >85% disk pause new attempts until <75% | No |
| 15 | RAM pressure (>85%) | lower `MAX_FREE_WORKERS` by 1 per 5 min, restore when <70%; Playwright runs serialized | No |
| 16 | Postgres down | product tests needing DB wait; watchdog tries `systemctl --user` restart if user-owned; system-owned → notify once, continue non-DB work (UI, office, docs, controller) | Only if system-owned and down >2 h |
| 17 | Git corruption / bad merge on integration | integration branch protected by controller: every merge re-runs harness; on failure auto-revert the merge commit and reopen the item; `git fsck` nightly; nightly bundle backup of the repo | No |
| 18 | Harness itself broken (all items fail the same new way) | detect ≥5 consecutive identical harness failures across different items → pause dispatch, create top-priority `FIX_HARNESS` task for Opus/Sonnet, resume after green | No |
| 19 | Task stuck forever | escalation §5.2.5 (2 → re-spec, 4 → Opus diagnose, 8 → park + 6-hourly redesign batch). Parked items never block unrelated items | No |
| 20 | Whole build stuck (no `ACCEPTED` item) | 6 h → Opus `DIAGNOSE_STALL`; 24 h → Opus re-plans the phase (smaller items, different ladder); 72 h → controller switches whole free lane to the best B0 model only and halves item size; still stuck at 7 days → diagnostic report + notification — **and keeps running the other phases' work** | Only at 7 days, and only a notification |
| 21 | Bootstrap runner dies | `empirium-bootstrap.service` restart; state file resumes at the last passing step | No |
| 22 | VPS reboot | linger + default.target + `@reboot` cron bring back FreeLLMAPI (if user-owned), controller, watchdog, product | No |
| 23 | False completion claimed | ignored — only `release_gate.py` writes `RELEASE_READY`; worker edits to gate/evidence files outside its scope are rejected at merge | No |
| 24 | Something unforeseen | L1–L3 restart the controller; the controller's main loop wraps every step in try/except → log incident → continue with next item. The loop has no code path that exits except `RELEASE_READY` | No |

### 15.3 Additional commissioning proofs
- **C10** kill FreeLLMAPI (or point the route at a dead port if it is not user-restartable) → watchdog detects and restarts/fails over; subscription lanes keep working.
- **C11** crash-loop: make the controller crash 5× on one fixture item → safe mode parks the item and the rest of the fixture completes.
- **C12** disable the systemd timer → the crontab layer still restores a killed controller within 15 min; corrupt a copy of the DB → auto-restore works.

### 15.4 Spend guard on fallbacks
Rules 3, 5, 6 and 7 only ever move work between **subscription** and **free** lanes. None of them may introduce a paid route. The build's total Claude usage is capped at ~70% of each 5-hour window (§13b). If the subscription has to carry implementation (rule 3), implementation may use at most 30 of those 70 points so reviews are never starved.

### 15.5 What "stops" is still possible, stated plainly
The build can *wait* (capacity, login, a root-only restart) but it cannot *end* early: there is no code path from which the controller exits before `RELEASE_READY`, and three independent layers restart it. The only human actions that can ever be required are the ones in §12, each announced once by notification while all unaffected work continues.

The project ends only when `release_gate.py` writes `RELEASE_READY`. Nothing else ends it. Begin.
