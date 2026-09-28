# Extract — Chunks 09–11 (Most Recent / Highest Authority)
Source: corpus/chunk_09.md, chunk_10.md, chunk_11.md — user messages + pasted attachments only, 2026-09-22 through 2026-09-28.

---

## 1. Project names / aliases (date first seen)

- **Empirium Studio AI Workforce** — canonical product identity for architecture/repo boundaries (2026-09-22, pasted product brief).
- **AI Staff Force / AI Star Force** — project-history/internal aliases, acceptable in docs only (2026-09-22).
- **Empirium OS** — brand shown in older visual mockups; explicitly NOT the product, and NOT to be merged into the existing personal Empirium OS app (2026-09-22).
- **Empirium Studio** — the frozen canonical brand name decision (S0.1, 2026-09-22): "Product brand: Empirium Studio; Product descriptor: AI Workforce."
- **AI Star Force** — used again as the chat/session title by Ash on 2026-09-28 ("Autonomous build prompt for AI Star Force"); Ash himself flags: *"this project has had a fe[w] names ... you need to be very meticulous in your gathering of data from past chats"* (2026-09-28 13:44).
- **Nailify / "Nailed It"** — separate, unrelated prior project (nail try-on app) referenced only as a methodology precedent, not part of this product.
- **Star Force X / "Nailed It" (Nailify)** and **AIStaffForce** — named as the two historical experimental workloads in the pasted Forensic Retrospective (2026-09-22).

---

## 2. Product requirements (date + short verbatim quotes)

All from the 2026-09-22 pasted "COMPLETE CONSOLIDATED PRODUCT BRIEF" / "OWNER DECISION REGISTER" / "FINAL AUTONOMOUS COMPLETION MANDATE" — pasted into chat by Ash, therefore carrying his authority as of that date.

- Not an agent dashboard: *"The product is **not primarily an AI-agent dashboard**. It is a **persistent AI workforce operations platform**..."*
- Mantra: *"Define the work once. Give the right AI employee the right tools, model, memory and permissions. Let the system perform, hand off, repeat, learn and report."*
- Three kinds of work required simultaneously: recurring operational work, event-driven workflows, one-off projects.
- Handoffs must be structured, not "start a new chat and hope the next model understands."
- Rules are first-class configuration (approval gates, retry limits, escalation conditions).
- Time/scheduling is first-class: timezones, DST, deadlines, recurring series, dependencies.
- Employees may be backed by non-chat implementations: voice agents, deterministic scripts, browser automation, DB tools, hybrid processes — *"The product model is 'AI employee / work capability,' not 'one chat model per bot.'"*
- Both lightweight personal jobs (free-game checks) and serious jobs (infra, finance, reception) belong in the same platform; difference is permission/risk tier, not a different product.
- *"The user should manage outcomes rather than sessions"* — minimize prompt babysitting; system handles ordinary execution autonomously.
- Explicit non-goals: not a dashboard, not roleplay, not a Kanban board with robot graphics, not a prompt library, not a single coding orchestrator, not a one-shot multi-agent swarm, not an LLM benchmark app, not a scheduler with no agent intelligence.
- Completion standard: workflows must actually execute, schedules actually fire, handoffs preserve context, state survives restarts, reports accurately describe what happened, office visuals match real state.
- Canonical one-line definition (S0.2, frozen): *"Empirium Studio is a persistent AI workforce operations platform in which specialized digital employees, each with configurable models, MCP/tool access, memory, permissions and job rules, execute recurring, scheduled, event-driven and project-based work through durable workflows and handoffs, while the user plans, observes, approves, audits and improves that work through a truthful living-office control interface."*

### M0 (Foundation) required scope — S0.3, 2026-09-22
- **M0.1** Durable domain: Organization, Department, Employee, Execution Profile, Workflow Definition, Schedule, Workflow Run, Task/Step, Attempt/Run, Artifact, Handoff, Review, Approval, Notification, Memory, Knowledge reference, Event, Report. SQLite acceptable as first authority.
- **M0.2** Durable scheduler: operates with browser closed, persists schedules, unique occurrence identities, missed-run policy, prevents duplicates, timezone-aware, survives restart.
- **M0.3** Seed department = **Personal Software** (strongest product definition). Seed **5 permanent employees**: Director, Research Architect, Developer/Implementation Engineer, QA Engineer, Learning Analyst. Office may show 3–5 at once but all 5 must exist as real persistent employees.
- **M0.4** First recurring real workflow = **Steam + Epic free-games monitor** — low risk, exercises scheduling, external data, dedup, artifacts, notification.
- **M0.5** Second workflow proving structured handoff between employees + approval pausing only the dependent path + durable resumption (small Personal Software change workflow).
- **M0.6** One fully animated/operational department living office; org overview may use lightweight/static mini-office projections.
- **M0.7** Reporting: what ran today, succeeded, failed, waiting, needs attention, scheduled next, which employee/model/tool acted.
- **M0.8** Simple (form/template) workflow creation without code.
- **M0.9** Model routing: at least 2 configurable model routes, ≥2 employees/steps using different routes, per-employee policy visible in UI, actual/effective route telemetry.
- **M0.10** QA vs approval must be provably distinct.
- **M0.11 (added)** Persistent employee memory: write → terminate session → retrieve → use → retain provenance.
- **M0.12 (added)** MCP/tool permission proof: one employee has access, another explicitly denied server-side, usage auditable.
- **M0.13 (added)** Basic calendar/schedule view: next/recent occurrences, pause/run-now/edit recurrence.
- **M0.14** Free-games run must appear consistently across run history, activity, employee recent work, report, schedule history, and office state simultaneously — "an important integration proof."

### Deferred from M0 but mandatory for CORE product (S0.4)
Full learning/improvement loop; full MCP registry + capability-management UI; cross-department workflows; voice/receptionist execution; richer workflow graph builder; richer calendar integration; multiple real departments; advanced model-routing optimization. Underlying architecture must still support voice workers, cross-department handoffs, multiple integrations, model diversity before final release.

### Likely post-core / optional (EXTENDED)
Finance-specific module/templates; broad multi-tenant SaaS; native mobile app.

---

## 3. Visual / design requirements

- Dark navy premium command-center UI; cyan/blue primary accents with controlled role/status colors; dense but legible dashboards.
- Organization overview = department cards; miniature department-office representations; large living office as visual anchor per department.
- Side/global nav + department-local nav; cards for active/upcoming/completed work, QA, knowledge, learning, costs, activity.
- Inspectable named workers with role/status overlays.
- **Preferred visible density: roughly 3–7 visible workers per room** before grouping/multiple rooms (repeated in multiple docs, confirmed 2026-09-22 and again in the 2026-09-22 14:38 Final Autonomous Completion Mandate).
- Do not run multiple full 60fps office simulations simultaneously; only the opened department runs the full scene; mini-offices are snapshot/throttled (S0.5).
- Design tokens must be machine-readable: colors, background layers, borders, accent roles, typography scale, spacing, radius, shadows/glow, status colors, motion durations, office sizing (S4.3).
- Accessibility: WCAG 2.1 AA where reasonably applicable; textual equivalents for office animation; reduced-motion support required; no third-party analytics; first-party operational telemetry required (S0.15).
- Character asset pack is absent — **not a blocker**: *"Create original reusable 2D character/office assets consistent with the approved visual language."* (2026-09-22 14:38 mandate)
- The 5 supplied organization/department mockups remain valid Empirium Studio visual references even though some show the older "EMPIRIUM OS" brand string — do not dismiss them as unrelated (owner ruling, G1, 2026-09-22 12:22).
- M0 design fidelity target: strong structural fidelity, correct information hierarchy, coherent dark/cyan system, high-quality Personal Software office, correct states, no generic/unfinished screens — literal pixel identity not required if it harms responsiveness/clarity (S8.7).
- 2026-09-28: Ash re-uploaded a further set of 9 images/screenshots as additional design/asset reference for the "AI Star Force" build, stating: *"there's even a series of different assets that we can use to describe how that should look... I've given you so much information."*

---

## 4. Architecture / tech decisions

- **Repo**: preserve existing `empirium-studio` repo untouched as evidence; create new clean target (`empirium-studio-v2` or a re-created clean `empirium-studio` after old path archived) — decided only after inspection confirms significant failed-build baggage (S2.1). Salvage audit required first: classify existing screens/modules KEEP/ADAPT/REPLACE/LEGACY/PRESERVE (owner ruling G4, 2026-09-22).
- **Fork base**: use newest compatible, stable, locally-proven Hermes Studio base, not blind pin/blind latest; freeze base SHA once selected (S2.2).
- **Old repo disposition**: quarantine/preserve, no deletion — forensic evidence + reusable code + failed-pattern lessons (S2.4).
- **Database**: SQLite acceptable as initial single authoritative operational DB if scale-tested sufficient; runtime state dir outside repo (`~/.local/state/empirium-studio/`); WAL mode, migrations, transactional writes, backups, FKs; design for later Postgres migration but don't move prematurely (S1.1).
- **State authority conflict resolution rule** (2026-09-22 14:38 mandate, Section 7D): if validated existing PostgreSQL implementation substantially reduces migration/rewrite risk while satisfying the product contract, it MAY be retained as canonical instead of SQLite — "Never retain dual authority." This is an engineering decision, not one requiring owner sign-off unless genuinely irreversible.
- **Event log**: append-only + SQLite structured/queryable event records; JSONL only a secondary audit stream (S1.3), with an extensive defined event-class list.
- **Employee memory storage**: product-owned persistent storage, SQLite metadata + compact text; do NOT bind employee identity solely to Hermes profile memory (S1.4).
- **Artifacts**: hybrid storage — small/text in DB, large/binary in files/object storage with DB metadata/reference; retain all at P0 scale, no silent hard-delete (S1.5).
- **Settings**: authoritative persistence, not localStorage (except transient UI state) (S1.6).
- **Secrets**: prefer existing Hermes/host secret store; else root-owned/env/systemd file with strict perms for M0; never plaintext secrets in UI, logs, prompts, artifacts, memory (S1.7).
- **Backups**: automatic local backups required at M0/core — nightly snapshot, pre-migration, pre-destructive-op, configurable retention (S1.8).
- **Migrations**: versioned schema/migration system from day one, with rollback plans (S1.9).
- **Reuse-first is a hard engineering preference** — inspect Hermes, installed infra, mature OSS components, and the previously-discussed AWS CAO/orchestration system before custom-building generic orchestration/scheduling/retries/queues/MCP plumbing (Owner Decision Register, Section 0C, 2026-09-22).
- Hermes component reuse rule (S2.5): Profiles → likely useful as execution profiles (Profile ≠ Employee); MCP → strongly prefer reuse, MCP is core; Cron/scheduling → evaluate, don't auto-replace, use stronger scheduler only if Hermes cron can't satisfy durability/timezone/missed-run/occurrence-identity/observability; Kanban → may back some Task lifecycle but Task ≠ Project/Workflow, one canonical authority must be chosen; Conductor/Crews → only for bounded temporary execution, never as Department or permanent Employee identity.
- **Third-party orchestrator evaluation required** (S2.6): AWS CAO/orchestrator previously referenced by Ash, Hermes-native primitives, BullMQ, Agenda/node-cron, n8n, Temporal, Hatchet, Inngest/Trigger.dev-style engines, Windmill/Kestra/Prefect-class systems. Score against self-hostability, resource use, license, durable timers, retries, idempotency, human pause/resume, observability, MCP compatibility. "Temporal may be too heavy for the current VPS, but exclude only after measuring fit." Do not turn into an endless survey.
- **Git**: frequent small coherent commits; stable task IDs in commit messages; local + private GitHub remote if project already uses GitHub securely; no new public remote; neutral build identity `Empirium Build <build@local>` (S2.7).
- **Toolchain**: reuse-first, don't churn Node/package manager/ESLint/Prettier/Vitest/Playwright/TypeScript without measured reason (S2.8).
- **Repo structure**: start with existing Hermes Studio structure; no monorepo split for aesthetics alone; only split into packages when boundaries become materially useful (office renderer, workflow engine adapter, shared domain contracts) (S2.9).
- **Testing on VPS**: headless Playwright acceptable; benchmark RAM/CPU, limit concurrency, deterministic viewport captures, no display server required (S2.10).
- **Delivery form**: web application on the VPS, consistent with Hermes Studio; Electron/desktop wrapper deferred — background execution must not depend on desktop app lifetime (S0.8).
- **Deployment**: standalone VPS service, private access only, bind locally + Tailscale/existing trusted proxy, no new public internet exposure by default; port discovered/configured in Stage 1, not hardcoded; no GPU required (S0.9).
- **Port**: confirmed **3003** for Empirium Studio target if sweep confirms free; must be configuration-driven, must not disturb Empirium OS/other services on 3000/3001 (owner ruling G3, 2026-09-22).
- **Kanban board**: create new canonical campaign board **`empirium-studio-v2-build`** (not `empirium-studio-m0`), preserving `empirium-studio-build`/`empirium-studio-test` as historical evidence; exactly one canonical dispatch authority (owner ruling G5, 2026-09-22).
- **Hermes profiles**: inspect all 5 existing profiles fully before creating anything; create only genuinely missing roles (`product-architect`, `repo-researcher`, `backend-integrator` likely candidates); reuse `studio-director`, `frontend-engineer`, `animation-engineer`, `visual-reviewer`, `qa-engineer` if they pass inspection (owner ruling G6, 2026-09-22).
- **Build campaign state**: separate from product runtime state; canonical project campaign state root resolved to `/home/ash/empirium-studio/.hermes/autonomy/`; versioned acceptance files (`verify.sh`, `checks`, `fixtures`, `requirements`, `predicates`) live in the repo; global `~/.hermes/` must NOT hold a second copy of campaign project.db/packets/evidence (V3 correction pass, 2026-09-22 13:08).
- **Build controller**: reuse the repaired "Nailify" deterministic controller as a proven starting point (not unquestioned truth) — strip Nailify-specific semantics first (S6.1, and 2026-09-22 14:38 mandate Section 10).
- Users/multi-tenancy: single-user/operator at M0 and initial core deployment; permissions designed as real policy concepts, not hardcoded single-user assumptions (S0.7).
- Org structure mutability: runtime create/rename/edit/archive for departments & employees; soft delete/archive with tombstones by default; hard delete is separate, high-friction, approval-protected (S0.12).
- Timezone: default **Europe/London**, but configurable from day one; store canonical UTC + explicit timezone metadata for recurrence; DST must be tested (S0.13).

---

## 5. Model / LLM routing decisions

- **Two independently configurable model routes required for M0**, per-employee/step, with effective route telemetry recorded (product requirement, repeated).
- Owner ruling G2 (2026-09-22): use the already-running **FreeLLMAPI route as Route A**. Inspect installed Ollama models; if a suitable local model exists, use **Ollama as Route B**. Suggested split: Research Architect/high-semantic work → FreeLLMAPI quality route; low-risk classification/formatting steps (e.g. Deals/Free-Games Monitor) → fast local Ollama route. If no Ollama model is capable enough, use two distinguishable FreeLLMAPI-verified-free routes instead rather than blocking — "do not stop and ask me which model to install merely to satisfy the test."
- 2026-09-22 12:34: Ash flags that **Ollama had zero models installed and FreeLLMAPI's models endpoint returned zero models** — Route B not actually proven yet; "That should remain an environmental action/risk... not an owner decision anymore, but also not complete merely because the architecture permits it."
- Route B should block the **F4/M0 product acceptance gate**, not the B0 worker benchmark itself, unless the frozen benchmark task specifically requires model-routing implementation (V3 correction #12, 2026-09-22).
- **Provider/model freeze for build workers** (S6.6): use a verified free implementation pool, effective-model attribution mandatory. Prefer pinned model for benchmark reproducibility/high-risk comparisons. Allow `auto`/pool for routine implementation only if effective model/provider is recorded. Reviewer = Opus/Sonnet subscription depending on risk. "Do not let strong subscription reviewers silently become primary implementers."
- **Paid ceiling (S6.7)**: build-time new pay-as-you-go AI spend ceiling remains **$0** unless owner explicitly changes it. Existing subscriptions allowed. No automatic paid fallback. Repeated in 2026-09-22 14:38 mandate Section 12: "Do not incur new pay-as-you-go AI spend... Provider 429/outage is a normal operational event... Do not interpret provider failure as product failure."
- Independent harness review should use a fresh strong reviewer, ideally a different model family from the harness implementer — **"Opus via subscription is appropriate where available"** (S5.4).
- 2026-09-22 13:56 (session "Extract atomic requirements"): Ash: *"these are taking too long, use sonnet from claude subscription to speed up."*
- 2026-09-22 14:03: Ash: *"switch to link[sic] 3.0 flash"* then confirms *"the free one right"* then specifies exact model string `inclusionai/ling-3.0-flash-vl:free`.
- 2026-09-22 14:06: Ash: *"stop all of the sub agents, make sure they use this free model via open router ffs."*
- 2026-09-22 14:16: Ash: *"sitch[sic] to open router:free and instead of wa[i]ting over 6 minutes, if it fails within 20 seconds, then try ag[a]in."* — explicit fast-fail/retry preference for free-router models.
- 2026-09-22 14:30: Ash: *"switch to sonnet 5 via the claude subscription to do this quickly"* then clarifies *"no, i meant [f]or the subagents, to get the work done now"* — Sonnet-5-via-subscription explicitly directed at the extraction subagents, not just the orchestrator.
- 2026-09-28 13:42: Ash: *"we've got access to a lot of different LLM models via the free LLM API which I want to use as much as possible and we've also got a Sonnet subscription which I don't mind ... a Claude subscription which I don't mind using as an orchestrator."* — FreeLLMAPI preferred for bulk work; Claude/Sonnet subscription acceptable as orchestrator.
- 2026-09-28 mandate text (chunk 11, restating the 2026-09-22 policy verbatim): build implementation should use verified zero-pay routes unless an existing subscription route is explicitly allowed for planning/review; strong subscription models reserved for architecture review, acceptance review, high-risk review, difficult diagnosis.

---

## 6. Autonomy / orchestration requirements and complaints about past failures

- **Explicit complaint from Ash (2026-09-28 13:44, HIGH PRIORITY / LATEST)**: *"I feel like, and this is something that we really need to plan around, especially if we're going to use the free LL[M] API[,] is it fails a lot, and when an LLM call fails, that stalls the entire project, and we can't allow that to be an issue."* — This is a direct, current-date requirement: **LLM call failures must not stall the whole project.** Must be treated as superseding/reinforcing any earlier retry policy.
- 2026-09-28 13:45: Ash: *"use sub agents to speed things up"* — explicit direction to parallelize via subagents for the autonomous build.
- Retrospective findings pasted 2026-09-22 (forensic self-audit, treated as evidence Ash wants applied):
  - Worker reliability never justified the orchestration built on top of it; no architecture generation ever exceeded ~20% accepted-worker-attempt rate.
  - "One more supervisor" pattern is real and costly — 9 director incarnations in under 9 hours triggered by a watchdog, while the real blocker (699 unimplemented requirements) couldn't be fixed by any supervisor.
  - Completion semantics were the recurring root failure: systems repeatedly could not distinguish "nothing runnable" from "objectively complete."
  - Self-approval was default until very late — same agent implemented, tested, and declared success with zero independent review for most of the project's history.
  - False-progress metrics (worktree counts, commit counts, passing unit-test counts, heartbeats) drove "success" claims while product-level acceptance stayed near zero.
  - Provider/model churn confounded almost every experiment — switching providers at the same time as architecture changes made root-cause attribution impossible.
  - "The single most actionable lesson: the first experiment should have been one bounded task, run 20 times, measuring independently-accepted passes — before any manager, orchestrator, database, or watchdog existed."
- Owner-mandated fix from this history (S6.10, stop rules, 2026-09-22): no concurrency growth until single-worker baseline proven (≥20 attempts, ≥60% accepted first-pass); no recursive supervisor/director hierarchies — a single durable planner/controller is preferred, bounded temporary planning/review sessions allowed; model/provider switching can occur when a provider is objectively unavailable/rate-limited (not only after 10 failures) but must follow pre-approved routing policy and be recorded.
- **Worker benchmark (B0)** required before scaling: 20 valid independent attempts on one frozen bounded task from the same base SHA; ≥60% accepted → launch autonomous build automatically; 30–59% → improve packet/decomposition, no added supervisor layer; <30% → stop scaling, redesign, no recursive orchestration (Section 8/S7, both documents).
- **Campaign ceiling**: 200 valid attempts / 14 calendar days / 2 structured re-baselining rounds before mandatory diagnostic pause and owner decision — "not permission to call the product failed or finished" (S6.11).
- **Watchdog rules** (S6.12 / mandate Section 21): restart dead controller, enforce one instance, log, respect pause, no LLM reasoning, no spawning recursive supervisors.
- **Owner interruption rule** (mandate Section 24, 2026-09-22 14:38, latest authority before chunk-11's 09-28 messages): do not ask permission to retry, fix tests, repair code, re-dispatch a worker, wait for a free provider, choose between reversible approaches, continue to next task/phase, run QA/acceptance/soak. Only interrupt for a true product decision absent from all sources, unsafe irreversible action, credential/account action needing owner interaction, HARD_STOP, or campaign ceiling.
- **This prompt is the launch authorization** (mandate Section 9): once B0 passes ≥60%, do NOT come back to ask "should I launch the campaign" — answer is already yes; proceed immediately into F1.
- **Completion is NOT**: M0 passing, dashboard looking good, all current tasks closed, no active workers, tests passing for a subset, orchestrator saying "done," free-games workflow working, living office rendering, Foundation being complete (mandate Section 23). Full CORE RELEASE requires every CORE-REQUIRED requirement implemented + passed acceptance, zero unresolved CRITICAL/HIGH defects, security/visual/resilience checks pass, soak evidence, independent full-release review, frozen SHA.
- 2026-09-28 13:42: Ash's task framing for the new autonomous-build prompt: *"analyze all the chats I've given you about Star Force... and create a prompt that will genuinely autonomously build this entire thing in its entirety... you are planning every single thing that we need to be able to build this app without my future input."* He notes that last time (a different app) required many upfront questions, but here: *"I feel like I've given you so many different examples of what I want this to be that you should already have all the answers on hand."*

---

## 7. CORRECTIONS / reversals (chronological — latest wins, superseded items marked)

1. **2026-09-22 ~11:25** — Initial brief posted (Empirium Studio Complete Product Brief v1-ish). SUPERSEDED by later revision passes below where noted.
2. **2026-09-22 11:52** — Owner Decision Register (S0–S9) issued as binding answers; **corrects** the framing that "P0 is the finished product" → *"P0 must not be treated as 'SHIPPED' for the whole product."* Establishes 3-tier system M0/Foundation, M1/Core, M2/Extended. **This supersedes any earlier looser P0=done framing.**
3. **Owner Decision Register Section 0B** — corrects AC-001–060 from being treated as the exhaustive ledger: *"Do not cap the ledger at 60–90 requirements."* Full product will compile to "hundreds of atomic requirements."
4. **2026-09-22 12:22 (G1–G6 owner rulings)** — resolves 6 items Hermes had raised as open questions, explicitly stating these are engineering/environmental decisions, not new owner decision cycles. **Supersedes** any assumption that character mockups needed a separate asset pack before starting (G1), that repo should be rebuilt clean without salvage audit (G4 corrects to "preserve → inventory → classify → choose base → salvage"), and that a new Kanban board name of `empirium-studio-m0` was final (G5 corrects to `empirium-studio-v2-build`).
5. **2026-09-22 12:34** — Ash **rejects launch approval** on Hermes's first Stage-0 summary, citing unreviewed pack, profile-count inconsistency (8 existing/3 missing vs. reported "5 of 11"), Route B not proven, salvage classification not actually done yet. Explicit "not yet approved" status.
6. **2026-09-22 12:47** — Ash issues **"REVISE BEFORE LAUNCH"** verdict on the actual Stage-0 pack (V1), citing 10 blocking defects, most importantly:
   - Full requirement ledger not actually present (placeholder text found) — **corrects** false claim of completeness.
   - V4 Part A/B originals missing from source register — flagged HIGH severity, later resolved (source pack recovery task, 2026-09-22 13:34).
   - Tron Bonne / ROM-R&D contamination suspected in source register — must be traced/removed, unrelated to this product.
   - **Domain model regression: `Project` entity was accidentally dropped** — corrected, must be restored as first-class.
   - F7 gate self-contradicted M0/Core separation — corrected to require only M0-REQUIRED predicates at F7, not all CORE-REQUIRED.
   - CORE vs EXTENDED tier inconsistent (voice wrongly placed in EXTENDED at one point, finance/multi-tenant/mobile wrongly placed in CORE at another) — corrected: voice/learning/full-MCP-registry/cross-department/visual-builder/richer-calendar/multi-department/model-routing = **CORE-REQUIRED**; finance module/broad multi-tenancy/native mobile = **EXTENDED**.
   - Benchmark positioned too late (at F4, after F1–F3 already built) — corrected to run **before** F1, after F0/harness freeze.
   - Pack conflated "approve this pack" with "launch full campaign" — corrected: pack approval only authorizes finishing F0 + running B0; a **second explicit approval** is required after B0 to launch F1+.
   - Scheduler acceptance predicate impossible as written (browser closed AND service stopped simultaneously) — split into two separate proofs: browser-independence vs. missed-run recovery.
   - Free-games predicate wrongly assumed every successful run finds a game — corrected to add explicit MATCH / NO_MATCH scenarios, with NO_MATCH still producing a persisted "checked successfully" run record (not literally "no artifact of any kind").
7. **2026-09-22 13:08** — V2 review: **"structurally sound, not yet approved. One targeted consistency pass required."** 20 remaining defects listed (benchmark renamed `B0`, removed duplicate benchmark gate from F4, removed premature "F1 starts after F0" language, removed routine owner approval baked into F0 exit gate, removed finance/multi-user from CORE continuation wording, restored missing MATCH scenario text, resolved dual build-state topology to single canonical root, separated calibration fixtures from the B0 benchmark experiment, Route B reclassified as blocking F4/M0 not B0, Temporary Worker/Crew explicitly added back to reconciliation checklist so they "cannot disappear again," BUILD-*/GOV-* namespace split from product M0 requirements, stale risk-register entries corrected). **Ash explicitly instructs Hermes to edit V2 in place, not redesign or reopen product questions.**
8. **2026-09-22 14:38 (pasted Final Autonomous Completion Mandate)** — the most authoritative/latest full document in chunks 09-11 predating the 09-28 session. Explicitly supersedes prior "return to owner after B0" procedural requirement: *"It supersedes the previous procedural requirement that you return to the owner for another routine 'launch the campaign' message after B0. If B0 passes its pre-registered gate, you are authorized to launch F1+ automatically."* Also reiterates: state-authority conflict may resolve to PostgreSQL instead of SQLite if evidence supports it (a refinement/possible override of the earlier SQLite-first default, made conditional on salvage-audit evidence).
9. **2026-09-28 13:42–13:45 (NEWEST, highest authority)** — Ash restarts the planning process in a new session ("Autonomous build prompt for AI Star Force"), asking Hermes to synthesize ALL prior chats into one final autonomous-build prompt. He:
   - Reiterates that this project has had multiple names and demands meticulous cross-session data gathering (implicit correction: don't rely on a single alias).
   - Adds a **new explicit requirement not previously stated as sharply**: free LLM API failures must not stall the whole project.
   - Confirms Claude/Sonnet subscription is acceptable as orchestrator, FreeLLMAPI preferred for bulk work.
   - Directs use of subagents to speed up the planning/build work itself.
   - States he expects Hermes to already have "all the answers" from prior context rather than re-running a big Q&A cycle like the Nailify project required — a preference/correction versus the earlier S0–S9 exhaustive-questionnaire approach used earlier in the same project.

---

## 8. Rejected approaches

- Rejected: treating M0/P0 as the shipped/finished product (Owner Decision Register 0A).
- Rejected: capping the requirement ledger at ~60–90 items just because AC-001–060 exists (0B).
- Rejected: building custom generic orchestration/scheduling/queue/retry machinery before evaluating reuse (0C).
- Rejected: conflating temporary build workers with permanent product employees (0D).
- Rejected: merging the new product into the existing personal "Empirium OS" app just because older mockups show that brand (S0.1, G1).
- Rejected: discarding the existing `empirium-studio` repo wholesale without a salvage audit ("rename it and start again before inspection") (G4).
- Rejected: naming the new Kanban board `empirium-studio-m0` (chose `empirium-studio-v2-build` instead) (G5).
- Rejected: overwriting/cloning existing Hermes profiles unnecessarily without inspecting them first (G6).
- Rejected: approving a Stage-0 pack sight-unseen based only on a summary (2026-09-22 12:34).
- Rejected: a domain model missing the `Project` entity (2026-09-22 12:47).
- Rejected: classifying finance/multi-tenant SaaS/native mobile as CORE-REQUIRED, and voice/receptionist as EXTENDED (inverted — corrected the other way) (2026-09-22 12:47).
- Rejected: running the 20-attempt worker benchmark late (at F4, after F1–F3 implementation already underway) — must run before F1 (2026-09-22 12:47, 13:08).
- Rejected: treating pack approval as full campaign-launch approval; two separate approval gates required (2026-09-22 12:47) — later itself superseded/loosened by the 14:38 mandate which pre-authorizes F1+ automatically once B0 passes.
- Rejected: an impossible scheduler acceptance predicate requiring "browser closed AND service stopped" simultaneously (2026-09-22 12:47).
- Rejected: assuming every successful free-games run must find a game (no NO_MATCH allowance) (2026-09-22 12:47).
- Rejected: dual/competing build-state topology across `/home/ash/empirium-studio/.hermes/autonomy/` and `/home/ash/.hermes/autonomy/` (2026-09-22 13:08).
- Rejected: conflating calibration fixtures (harness catches known-bad code) with the B0 worker benchmark (measures worker ability) (2026-09-22 13:08).
- Rejected: leaving Temporary Worker and Crew as "add only if required" — they must be explicit in the reconciliation checklist so they don't silently disappear again (2026-09-22 13:08).
- Rejected: recursive supervisor/director hierarchies ("one more supervisor" pattern) — directly blamed for prior project failure in the Forensic Retrospective and explicitly forbidden going forward (S6.10, mandate Section 10).
- Rejected: worker self-report as acceptance authority — only the canonical harness run against the exact integrated SHA decides (S5.6, S7.6, mandate Section 7G).
- Rejected: silently deferring a CORE requirement just because it's difficult — "Difficulty changes decomposition. It does not change requirement status." (mandate Section 6).
- Rejected: requiring human approval for routine/low-risk recurring work (bot-to-bot handoffs, QA verdicts, free-games alerts, first-time scheduled execution after activation) — approval reserved for genuinely consequential/irreversible actions (S8.6, mandate Section 19).
- Rejected (2026-09-22 14:38, Section 26): letting the older parallel "Extract atomic requirements" session remain an uncontrolled parallel writer once a new integrator session takes over; also rejects starting another large extraction swarm — one canonical merger owns the ledger.
- Rejected (implicit, 2026-09-28): re-running an exhaustive upfront Q&A cycle like the earlier Nailify project — Ash wants Hermes to synthesize existing chat history into the plan instead of asking him everything again.

---

## 9. Open questions

- **Exact telephony/voice provider** not precommitted to Twilio — "Evaluate current providers, cost, latency and existing stack before choosing" (S8.5, 2026-09-22). Still open as of latest chunks.
- **Whether validated existing PostgreSQL implementation is sufficient to become the canonical DB** instead of SQLite — explicitly left as an engineering decision to be made from salvage-audit evidence, not yet resolved in the transcript (mandate Section 7D, 2026-09-22 14:38).
- **Whether the exact original V4 Part A/B documents were ever definitively located** — a dedicated recovery task was launched (2026-09-22 13:34, "prepare a clean source pack") but chunks 09-11 do not show its completion report; the 14:38 mandate simply asserts "The exact original Version 4 Part A and Part B have already been recovered" without chunk-visible confirmation of the search outcome.
- **Whether Tron Bonne / ROM-R&D material was conclusively confirmed unrelated and purged from the source register** — flagged for investigation (2026-09-22 13:29 audit task) but resolution not shown in these chunks.
- **Final F0 traceability ledger contents** (hundreds of atomic requirements) — extraction work was actively in progress at end of chunk 10 (multiple subagent/model-switching messages, 13:56–14:30) with no completion confirmation visible in this range.
- **B0 benchmark outcome** — not shown in chunks 09-11; the 2026-09-28 session restarts planning from scratch ("create a prompt that will genuinely autonomously build this entire thing"), which itself raises the open question of whether F0/B0 from the 09-22 session were ever completed/launched, or whether this is effectively a reset.
- **Which orchestrator to use for the 2026-09-28 rebuild** — Ash explicitly leaves this open: *"I don't know what orchestrator will be best if you need to do an online search for a better orchestrator you're more than welcome to."*
- **Specific mechanism for preventing free-LLM-API failures from stalling the project** — Ash raises this as a critical concern (2026-09-28 13:44) but does not prescribe the exact fallback/retry mechanism, leaving the design open other than the general principle stated.

---

## Final state of the build as Ash describes it (as of latest message, 2026-09-28 13:45)

As of the end of chunk 11 (most recent messages), the project has **not been shown as built or even re-launched** in this transcript range. Ash opens an entirely new session on 2026-09-28 to have Hermes:
1. Analyze all prior chats/history about "Star Force"/AI Star Force/Empirium Studio (spanning multiple aliases).
2. Incorporate newly uploaded asset/mockup images from the VPS desktop.
3. Produce a single new autonomous-build prompt capable of building "this entire thing in its entirety" without further owner input — effectively a fresh synthesis/restart of the planning-to-build handoff that had been worked through extensively on 2026-09-22 (Stage-0 pack V1→V2→V3, F0/B0 preparation, owner decision register, salvage/domain/acceptance audits).
4. He explicitly does not want another exhaustive upfront Q&A like the previous Nailify project, believing sufficient context already exists across past chats.
5. He adds a new hard constraint: free LLM API failures must not stall the whole project.
6. He directs use of subagents to speed the (re)planning work.

No confirmation in these chunks that F0 was finished, that B0 ran, or that any autonomous build campaign actually launched — the 2026-09-28 session reads as restarting/re-consolidating the build authorization rather than continuing a running campaign.
