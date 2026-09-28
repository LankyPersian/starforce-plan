

===== 2026-09-22 11:52 | session 20260922_105531_432d90 | AI staff force set up =====
@file:.hermes/attachments/EMPIRIUM_HERMES_S0-S9_OWNER_ANSWERS_2026-09-22.md

are there any remaining gaps in the questionsing before we can start

--- Attached Context ---

📄 @file:.hermes/attachments/EMPIRIUM_HERMES_S0-S9_OWNER_ANSWERS_2026-09-22.md (14512 tokens)
```markdown
# EMPIRIUM STUDIO / AI STAFF FORCE
# OWNER DECISION REGISTER — ANSWERS TO HERMES S0–S9 AUTONOMY QUESTIONS

**Date:** 2026-09-22  
**Status:** Owner-intent answer set for Stage-0 planning.  
**Purpose:** Remove ambiguity before Hermes is allowed to plan or execute autonomously.

---

# 0. Read this before interpreting any individual answer

There are several important corrections to the framing of the question set.

## A. P0 is NOT the finished product

The most important correction is that **P0 must not be treated as “SHIPPED” for the whole product**.

The product has repeatedly suffered from scope collapse: a large intended system becomes a small vertical slice, the small slice passes tests, and an orchestrator then describes the overall product as finished.

That is not acceptable here.

For this project:

- **P0 / M0 = Foundation + first representative end-to-end operating slice.**
- It proves the architecture can support the real product.
- It is allowed to be narrower than the full product.
- Passing P0 means “the foundation is proven,” not “Empirium Studio is shipped.”
- The final release gate must remain tied to the complete mandatory requirement ledger derived from all authoritative product sources.

If Hermes wants a three-tier system, use:
- **M0 / Foundation** — first integrated proof.
- **M1 / Core Product** — all central product capabilities implemented.
- **M2 / Extended Product** — explicitly non-core future enhancements.

Do not use “P1 = not required for SHIPPED” for capabilities that are clearly mandatory in the product charter.

## B. AC-001–060 is a base, not the exhaustive requirement ledger

AC-001–060 is useful as a behavioral spine, but it is **not exhaustive enough to represent the complete product**.

The full ledger must also be extracted from:
- the original two-part Empirium Studio master protocol;
- the consolidated final product brief;
- supplied mockups;
- later conversation clarifications;
- relevant AI Staff Force project decisions;
- explicit workflow, memory, MCP, model-routing, scheduling, calendar, reporting, voice/receptionist and observability requirements.

Do not cap the ledger at 60–90 requirements merely because AC-001–060 has 60 entries.

The full product will almost certainly compile to **hundreds of atomic requirements** once UI states, workflow behavior, security, failure recovery, permissions, model routing, memory, observability, accessibility and acceptance predicates are decomposed properly.

## C. Reuse-first is a hard engineering preference

Before custom-building generic orchestration, scheduling, retries, queues, MCP plumbing, long-running workflow state, or worker lifecycle mechanisms:

1. inspect Hermes;
2. inspect already-installed infrastructure;
3. evaluate mature open-source components;
4. evaluate the AWS CAO/orchestration system previously discussed by the user, if locally/relevantly available;
5. compare candidates to the exact Empirium contract;
6. integrate or wrap the best-fitting existing substrate.

Empirium should own the product semantics, not necessarily every low-level runtime mechanism.

## D. Product employees and build workers are different things

The workers that build Empirium are disposable engineering workers.

The employees inside Empirium are permanent product entities.

Do not confuse them.

---

# S0 — PRODUCT CHARTER & SCOPE FREEZE

## S0.1 — Canonical name

**Decision:** Use **“Empirium Studio”** as the canonical product/UI name for this build. The descriptive subtitle may be **“AI Workforce”** or **“AI Staff Force”** in documentation and onboarding.

Use:
- Product brand: **Empirium Studio**
- Product descriptor: **AI Workforce**
- Internal project aliases: AI Staff Force / AI Star Force are acceptable project-history terms only.

Do **not** merge this product into the existing personal “Empirium OS” application merely because older mockups show “EMPIRIUM OS.”

The branding should be configuration-driven so the product can later be renamed without changing the domain model.

---

## S0.2 — One-line definition

**Decision:** Replace the proposed line with the following canonical definition:

> **Empirium Studio is a persistent AI workforce operations platform in which specialized digital employees, each with configurable models, MCP/tool access, memory, permissions and job rules, execute recurring, scheduled, event-driven and project-based work through durable workflows and handoffs, while the user plans, observes, approves, audits and improves that work through a truthful living-office control interface.**

This sentence is a better decomposition anchor because it captures:
- persistent employees;
- specialization;
- multiple LLMs;
- MCPs/tools;
- memory;
- permissions;
- workflows;
- schedules;
- event-driven work;
- projects;
- handoffs;
- human control;
- reporting/observability;
- living office.

Do not shorten it in a way that loses those concepts.

---

## S0.3 — P0 “shipped” slice

**Decision:** I do **not** accept P0 as the whole product’s SHIPPED slice. Treat it as **M0 Foundation / Representative Vertical Slice**.

For M0, the proposed items are approved with the following additions and amendments:

### M0.1 Durable domain
Required.

The minimum durable domain should include:
- Organization;
- Department;
- Employee;
- Execution Profile;
- Workflow Definition;
- Schedule;
- Workflow Run;
- Task/Step;
- Attempt/Run;
- Artifact;
- Handoff;
- Review;
- Approval;
- Notification;
- Memory;
- Knowledge reference;
- Event;
- Report.

SQLite may be the first authority if the architecture remains migration-friendly.

### M0.2 Durable scheduler
Required.

Must:
- operate with browser closed;
- persist schedules;
- create unique occurrence identities;
- support missed-run policy;
- prevent duplicate occurrences;
- support timezone-aware scheduling;
- survive process restart.

### M0.3 Seed department
Required.

Use **Personal Software** as the canonical first fully exercised department because it already has the strongest product definition.

Seed **5 permanent employees**:
1. Director;
2. Research Architect;
3. Developer / Implementation Engineer;
4. QA Engineer;
5. Learning Analyst.

The office may visibly show 3–5 at a time if layout requires, but all five must exist as real persistent employees.

### M0.4 Recurring real workflow
Required.

Use the **Steam + Epic free-games monitor** as the first real unattended recurring workflow because:
- it is real;
- it is low risk;
- it exercises scheduling;
- it exercises external data acquisition;
- it exercises deduplication;
- it exercises artifacts;
- it exercises notification;
- it gives immediate proof that background work is real.

### M0.5 Project/handoff workflow
Required.

Use one second workflow that proves:
- one employee performs work;
- structured handoff occurs;
- another employee continues;
- approval can pause only the dependent path;
- resumption is durable.

A small Personal Software change workflow is suitable.

### M0.6 Truthful living office
Required.

One fully animated/operational department is enough for M0.

The organization overview can use lightweight/static mini-office projections.

### M0.7 Reporting
Required.

Must answer:
- what ran today;
- what succeeded;
- what failed;
- what is waiting;
- what requires attention;
- what is scheduled next;
- which employee/model/tool acted.

### M0.8 Simple workflow creation without code
Required.

A form/template builder is sufficient for M0.

### M0.9 Model routing
The original proposed default is **too weak**.

M0 must prove that the architecture genuinely supports different models for different employees.

Therefore M0 should have:
- at least **two configurable model routes**;
- at least **two employees/steps using different routes**;
- per-employee model policy visible in UI;
- actual/effective route telemetry where available.

This does not mean two paid providers are required. Two verified usable routes are enough.

### M0.10 QA vs approval
Required.

Must prove:
- independent quality review is not the same thing as;
- human authorization to perform a consequential action.

### M0.11 Persistent employee memory
**Add to M0.**

At least one employee must:
- write an approved memory;
- terminate its session;
- later retrieve that memory;
- use it appropriately;
- retain provenance.

Memory is too central to defer entirely.

### M0.12 MCP/tool permission proof
**Add to M0.**

A full integration marketplace is not necessary, but M0 must prove:
- one employee has access to a real MCP/tool;
- another employee does not;
- unauthorized use is denied by policy/server-side enforcement;
- usage is auditable.

MCP capability is too central to leave completely unproven.

### M0.13 Calendar/schedule view
**Add to M0.**

A basic in-app schedule/calendar surface should show:
- next occurrences;
- recurring routine;
- recent occurrences;
- pause/run-now/edit recurrence.

### M0.14 Memory/reporting/office truth
The free-games run should become visible simultaneously in:
- workflow run history;
- activity;
- employee current/recent work;
- report;
- schedule history;
- office state while active.

This is an important integration proof.

---

## S0.4 — P0 exclusions register

**Decision:** Reclassify the exclusions carefully.

### Out of M0, but mandatory later in the core product
- full learning/improvement loop;
- full MCP registry and capability-management UI;
- cross-department workflows;
- voice/receptionist execution;
- richer workflow graph builder;
- richer calendar integration;
- multiple real departments;
- advanced model-routing optimization.

These are not “optional backlog.” They are deferred from the first foundation milestone only.

### Likely post-core / optional expansion
- full finance-specific module/templates;
- broad multi-tenant SaaS support;
- native mobile app.

### Important distinction
The underlying architecture must support:
- voice workers;
- cross-department handoffs;
- multiple integrations;
- model diversity

before final product release, even if every possible connector/template is not shipped.

---

## S0.5 — Office scope

**Decision:** For M0:
- one department gets the full animated living office;
- organization overview uses static or heavily throttled mini-office cards.

For the final product:
- every department can have a living-office representation;
- only the currently opened department should run the full scene;
- mini-offices should be snapshot/throttled representations for performance.

Do not run multiple full 60fps office simulations.

---

## S0.6 — Workflow builder depth

**Decision:** M0 uses:
- form-based creation;
- templates;
- read-only visual graph/timeline;
- explicit step configuration.

A full drag-and-drop graph editor is not required for M0.

However, **a true visual workflow builder is mandatory for the core product**, because the long-term experience is that users should be able to assemble and modify work cascades without editing source code.

The visual builder must eventually support:
- agent nodes;
- deterministic tool nodes;
- branches;
- delays;
- approvals;
- handoffs;
- joins;
- sub-workflows;
- MCP actions.

---

## S0.7 — Users

**Decision:** Single-user/operator at M0 and initial core deployment.

No secondary operator account is required for M0.

However:
- permissions must be designed as real policy concepts rather than hardcoded “because there is one user” assumptions;
- future multi-user support should not require rewriting the core employee/workflow model.

Multi-user is not a first milestone priority.

---

## S0.8 — Delivery form

**Decision:** Web application served on the VPS, consistent with Hermes Studio.

Desktop wrapper/Electron is deferred.

Reason:
- browser UI is appropriate for a persistent server-side workforce;
- background execution must not rely on desktop app lifetime;
- web access via secure private networking is simpler.

---

## S0.9 — Deployment & access

**Decision:** Initial deployment:
- standalone service on the VPS;
- private access only;
- bind locally and expose through the user’s existing secure private access method, preferably Tailscale or existing trusted proxy;
- no new public internet exposure by default.

Do not hardcode a port before inspecting current services and avoiding conflicts.

Port should be discovered/configured during Stage 1.

Primary machine is the current VPS/host where Hermes is already being operated.

Do not require GPU.

---

## S0.10 — First production workload

**Decision:** Yes, the Steam + Epic free-games monitor should run for real from the first live milestone.

**Primary notification channel for M0:** in-app notification/attention inbox.

Reason:
- it proves the Empirium notification system itself;
- it avoids making Telegram/email credentials a blocker;
- external notification adapters can then be added cleanly.

**Secondary preferred channel after core in-app proof:** Telegram.

Do **not** create external accounts/bots without explicit user action if provider setup requires account authorization.

The architecture should make notification channels pluggable.

---

## S0.11 — Seed content

**Decision:** Hermes may draft:
- Personal Software department content;
- the five employee personas;
- roles;
- responsibilities;
- routing descriptions;
- model/tool policies;
- starter workflows.

However:
- these become versioned configuration;
- they are not immutable product code;
- they should be reviewable/editable by the user.

Hermes does **not** need to stop for approval of every individual name before building the schema/UI.

Use high-quality provisional names and roles; owner approval can occur at the configuration-freeze checkpoint.

Role correctness is more important than character naming.

---

## S0.12 — Org structure mutability

**Decision:** Yes, P0/M0 should support runtime:
- create;
- rename;
- edit;
- disable/archive

for departments and employees.

Deletion should use **soft delete/archive with tombstones** by default.

Hard delete should be:
- separate;
- high-friction;
- approval-protected;
- only possible where retention/reference integrity is preserved.

No sub-team hierarchy is required initially.

---

## S0.13 — Timezone

**Decision:** Default timezone is **Europe/London**, but timezone is a real configurable field from day one.

Use:
- organization default timezone;
- workflow/schedule override where necessary;
- display in user/local timezone.

Do not make Europe/London an unchangeable global constant.

All stored timestamps should use an unambiguous canonical representation such as UTC plus explicit timezone metadata for recurrence.

DST behavior must be tested.

---

## S0.14 — No fake data

**Decision:** Confirm with one refinement.

Allowed:
- deterministic test fixtures;
- Storybook/dev/demo fixtures;
- clearly labeled synthetic acceptance data.

Not allowed in production:
- fake active employees;
- fake runs;
- fake spend;
- fake QA;
- fake “health”;
- fake progress;
- fake activity.

Seed configuration such as default employees and a default workflow is real configuration, not fake telemetry.

Production dashboards must derive from real stored state.

---

## S0.15 — Language / accessibility / analytics

**Decision:**
- English only initially.
- Architecture should not actively prevent future i18n.
- Accessibility target: **WCAG 2.1 AA where reasonably applicable** for the product UI.
- Full living-office animation must have textual equivalents.
- Reduced-motion support is required.
- No third-party product analytics/telemetry by default.
- First-party operational telemetry/logging is required because the product must report its own work.

---

# S1 — DATA & STATE ARCHITECTURE

## S1.1 — P0 database

**Decision:** SQLite is acceptable as the initial single authoritative operational database if current-scale testing confirms it is sufficient.

Use a runtime state directory outside the repository, e.g.:
`~/.local/state/empirium-studio/`

Do not store mutable production DB state in Git.

Use:
- WAL mode where appropriate;
- migrations;
- transactional writes;
- backups;
- foreign keys.

Design schema so a later move to Postgres is feasible.

Do not prematurely move to Postgres unless scale/concurrency requires it.

---

## S1.2 — Complete mutable-state list

**Decision:** The proposed list is incomplete.

SQLite/authoritative persistence should cover at least:

- organization;
- organization policies/settings;
- departments;
- employees;
- execution profiles;
- employee config versions;
- workflow definitions;
- workflow versions;
- workflow triggers;
- schedules;
- schedule occurrences;
- workflow runs;
- steps/tasks;
- attempts;
- artifacts metadata;
- handoffs;
- reviews;
- approvals;
- notifications;
- employee memory;
- knowledge metadata/index references;
- learning proposals;
- reports;
- tool/MCP registry;
- tool grants/permissions;
- model/provider registry;
- model-routing policy;
- provider health state;
- notification channels;
- secrets references (not raw secrets unless a vault design specifically allows it);
- app settings;
- audit/config change records;
- meaningful events;
- leases/claims if the execution engine does not own them;
- idempotency keys;
- retry state;
- calendar items generated by the system;
- user/operator attention items.

If a third-party workflow engine owns low-level execution state, Empirium may store an authoritative product projection plus external engine IDs, but there must be one clearly documented canonical writer for each lifecycle.

---

## S1.3 — Event log

**Decision:** Yes to an append-only event history, but SQLite should also hold structured event records or a queryable event projection.

JSONL can be a useful secondary audit stream, not the only event store.

Add these event classes:
- workflow activated/paused/version changed;
- schedule occurrence created;
- schedule fired/missed/coalesced/skipped;
- run queued/started/ended;
- step ready/assigned/started/ended;
- attempt started/ended;
- retry scheduled;
- provider/model selected;
- provider rate-limited;
- MCP/tool call started/result/failed;
- handoff created/consumed;
- artifact created;
- review requested/verdict;
- approval requested/granted/rejected/expired;
- memory proposed/written/edited/expired;
- notification created/sent/failed;
- config changed;
- permission denied;
- employee state changed;
- integration connection changed;
- report generated;
- learning proposal created/activated/rolled back;
- recovery/restart events;
- idle reason.

Keep low-level token streaming out of the semantic event log.

---

## S1.4 — Employee memory

**Decision:** Use product-owned persistent memory storage, with SQLite for canonical metadata and compact text/structured memories.

Do not bind employee identity to Hermes profile memory as the only source of truth.

Hermes memory can be an adapter/source if useful.

P0 UI should support at minimum:
- view memory;
- provenance/source;
- mark obsolete;
- edit/correct;
- delete/archive where allowed.

Export can be P1/core-later, but the storage format should remain inspectable.

---

## S1.5 — Artifacts

**Decision:** Use hybrid storage.

- Small structured/text artifacts: database body acceptable.
- Large/binary artifacts: files/object storage with DB metadata/reference.
- Every artifact gets stable ID, provenance, content type, creator run, timestamps, hash where useful.

Retention:
- do **not** silently hard-delete after 500 rows.
- P0 may retain all because scale is tiny.
- build a later configurable retention/archive policy.

Artifact viewer in P0: yes, for text/JSON/links/basic files.

---

## S1.6 — Settings

**Decision:** App settings and behaviorally important preferences should be in authoritative persistence, not only localStorage.

LocalStorage may be used only for non-authoritative browser convenience such as:
- panel collapse state;
- transient UI preference;
- last selected tab.

---

## S1.7 — Secrets

**Decision:** Prefer a dedicated secret boundary rather than raw secrets in SQLite.

Order of preference:
1. reuse an existing Hermes/host secret store if secure, stable and independently addressable;
2. otherwise root-owned/env/systemd environment file with strict permissions for M0;
3. later add encrypted-at-rest credential storage if the product must manage multiple user-entered credentials.

The UI should never read back plaintext secrets.

Model/integration settings should show:
- configured/not configured;
- last validated;
- provider identity;
- scope;
- update/replace action.

No secrets in logs, prompts, artifacts or memory.

---

## S1.8 — Backups

**Decision:** Automatic local backups are **M0/core**, not a distant P1.

At minimum:
- nightly SQLite snapshot;
- before schema migration;
- before destructive admin operation;
- configurable retention.

External/offsite sync such as Google Drive can come later.

The backup process itself should be observable.

---

## S1.9 — Migration story

**Decision:** Confirm.

Versioned schema/migration system from day one.

Each migration should have:
- ID/version;
- timestamp;
- forward migration;
- rollback/recovery plan where feasible;
- backup precondition for destructive change.

---

## S1.10 — Deterministic fixtures

**Decision:** Confirm.

Committed deterministic fixtures may include:
- organization;
- department;
- employees;
- workflow definitions;
- run histories;
- failure states.

They must be:
- clearly test-only;
- never automatically imported into production;
- safe to reset.

---

# S2 — REPO, TOOLCHAIN, REUSE

## S2.1 — Target repo

**Decision:** Prefer a fresh, clean target fork/repo **if** inspection confirms the existing Empirium Studio tree contains significant failed-build baggage.

Recommended:
- preserve existing `empirium-studio` repository untouched as evidence/reference;
- create a new clean repository such as `empirium-studio-v2` or preferably simply a new clean `empirium-studio` after the old path is archived/read-only.

Do not decide path names blindly.

Stage 1 should inspect:
- current Git state;
- useful code;
- current Hermes version;
- what is salvageable.

No destructive cleanup of old evidence.

---

## S2.2 — Fork base

**Decision:** Check upstream/current local Hermes Studio state first.

Use the newest **compatible, stable, locally proven** base rather than blindly pinning v1.20.0 or blindly following upstream main.

Avoid moving-target development on an unverified latest commit.

Freeze a base SHA once selected.

---

## S2.3 — Old build salvage

**Decision:** Use the old `AI_WORKFORCE_BUILD/` documents/contracts/ADRs as input material, but never as unquestioned authority.

Process:
- ingest;
- map to current requirement IDs;
- classify still-valid / superseded / implementation-specific / obsolete;
- preserve provenance;
- reuse code/contracts only after validation.

Do not rebuild valuable work from scratch if it remains correct.

---

## S2.4 — Old repo disposition

**Decision:** Confirm.

Quarantine/preserve it.

No deletion.

It is:
- forensic evidence;
- source of reusable code;
- source of failed-pattern lessons.

---

## S2.5 — Hermes built-in reuse

**Decision:** The proposed default is too prescriptive.

Use this rule instead:

### Product domain
Empirium owns the durable product semantics.

### Hermes capabilities
Evaluate and reuse where they fit:
- **Profiles:** likely useful as execution profiles/backends. Use, but Profile ≠ Employee.
- **MCP:** strongly prefer reuse. MCP is core.
- **Cron/scheduling:** evaluate, do not automatically replace. If Hermes cron can satisfy durability, timezone, missed-run, occurrence identity and observability requirements, it may back schedules. If not, use a stronger scheduler.
- **Kanban:** may back some Task lifecycle, but Task ≠ Project/Workflow and one canonical authority must be chosen.
- **Conductor/Crews:** use only for bounded temporary execution/grouping where they add value. Do not use them as Department or permanent Employee identity.

Do not declare “product scheduler must be custom” before evaluating reuse.

---

## S2.6 — Third-party orchestrator evaluation

**Decision:** Include a deliberate reuse study.

Evaluate at least:
- the AWS CAO/orchestrator the user previously referenced;
- Hermes-native execution primitives;
- BullMQ;
- Agenda or node-cron only for simpler scheduling roles;
- n8n;
- Temporal;
- Hatchet;
- Inngest/Trigger.dev style durable workflow engines where self-host/open-source fit exists;
- Windmill/Kestra/Prefect-class systems if they fit resource and licensing constraints.

Do not turn this into an endless survey.

Score against:
- self-hostability;
- resource use;
- license;
- durable timers;
- retries;
- idempotency;
- human pause/resume;
- long-running workflows;
- observability;
- step metadata;
- worker/tool flexibility;
- ease of embedding;
- MCP compatibility;
- operational complexity.

Temporal may be too heavy for the current VPS, but exclude only after measuring fit.

---

## S2.7 — Git

**Decision:**
- frequent small coherent commits;
- stable task IDs in commit messages where practical;
- local repo plus private GitHub remote if the existing project already uses GitHub securely.

Do not create a new public remote.

Use a neutral build identity such as:
`Empirium Build <build@local>`

The exact identity is not important; traceability is.

---

## S2.8 — Toolchain pins

**Decision:** Confirm reuse-first.

Do not churn:
- Node;
- package manager;
- ESLint;
- Prettier;
- Vitest;
- Playwright;
- TypeScript

without a measured reason.

Pin versions after base audit.

---

## S2.9 — Monorepo vs single package

**Decision:** Start with the existing Hermes Studio structure.

Do not create a monorepo/workspace split merely for architecture aesthetics.

Create packages/modules only when boundaries become materially useful, for example:
- office renderer;
- workflow engine adapter;
- shared domain contracts.

Avoid premature package fragmentation.

---

## S2.10 — Test runtime on VPS

**Decision:** Headless Playwright on the VPS is acceptable.

But:
- benchmark RAM/CPU;
- limit concurrency;
- run visual captures at deterministic viewport sizes;
- do not compete with many simultaneous build workers.

Acceptance should include:
- DOM/state assertions;
- screenshots;
- browser console;
- real interaction.

A display server should not be required.

---

# S3 — REQUIREMENT LEDGER & SCOPE

## S3.1 — Ledger base

**Decision:** AC-001–060 is **one input**, not the complete base.

The authoritative ledger must be generated from all product sources.

Each source item should map to one or more atomic requirements.

The ledger needs:
- stable ID;
- source;
- source priority;
- capability;
- mandatory/deferred/optional status;
- milestone;
- dependency;
- acceptance predicate;
- evidence;
- current state.

No substantive source paragraph should remain unmapped.

---

## S3.2 — Target size

**Decision:** Do not set an artificial ledger-size appetite.

For M0/Foundation, ~60–100 atomic requirements may be reasonable.

For the full product, expect **several hundred**.

Correct decomposition is more important than keeping the list short.

A large requirement ledger is acceptable if:
- it is machine-readable;
- grouped hierarchically;
- dependency-aware;
- not duplicated;
- each atomic item is testable.

---

## S3.3 — IDs & mapping

**Decision:** Keep AC-001–060 as stable acceptance references.

Create requirement IDs such as:
- PROD-ORG-###
- PROD-EMP-###
- PROD-WF-###
- PROD-SCHED-###
- PROD-MEM-###
- PROD-MCP-###
- PROD-MODEL-###
- PROD-OFFICE-###
- PROD-REPORT-###
- PROD-SEC-###
- PROD-QA-###
- PROD-UI-###

Each requirement maps to:
- one or more sources;
- one or more acceptance criteria;
- one or more predicates.

Orphan count for mandatory requirements must be zero.

---

## S3.4 — Priority semantics

**Decision:** Reject “P1 = not required for SHIPPED” as the global product rule.

Use:

- **M0-REQUIRED** — required for foundation gate.
- **CORE-REQUIRED** — mandatory before the complete product can be called shipped.
- **EXTENDED** — deliberately optional future enhancement.

Risk is a separate field:
- LOW;
- MEDIUM;
- HIGH;
- CRITICAL.

A requirement can be CORE-REQUIRED and implemented after M0.

---

## S3.5 — Definition of Done source

**Decision:** Derive a canonical DoD from:
- the complete mandatory requirement ledger;
- AC-001–060;
- final product brief completion rules;
- original master-protocol release principles.

DoD is not one prose section.

It should be machine-checkable:
- all mandatory requirements in accepted state;
- all blocking predicates pass;
- no unresolved critical/high defects;
- required soak/recovery evidence complete;
- independent release review complete;
- release SHA fixed.

Owner approval should freeze the DoD before broad campaign execution.

---

## S3.6 — Failure contract

**Decision:** Confirm with one addition.

Every failing mandatory predicate must create:
- a defect/work item;
- failure classification;
- reproduction/evidence;
- responsible requirement;
- next action;
- retry/rework counter.

Failure does not terminate the campaign unless a pre-registered safety/budget condition is reached.

The system must diagnose repeated failure rather than endlessly retry.

---

## S3.7 — Requirement extraction standard

**Decision:** Confirm, and add these questions:

For each requirement:
1. Is this a capability rather than a restated sentence?
2. Can a fresh engineer understand success?
3. Is it atomic enough to verify?
4. Is it traceable to source?
5. Is its mandatory/deferred status explicit?
6. Does it preserve the full product intent?
7. Does it have a proof method?
8. Would passing it still allow an obvious fake implementation?

If #8 is yes, strengthen the predicate.

---

# S4 — ACCEPTANCE PREDICATES

## S4.1 — Predicate classes

**Decision:** The proposed classes are useful but not “exactly one class.”

A requirement may need multiple proofs.

Use proof dimensions:
- deterministic/static;
- unit;
- integration;
- UI runtime;
- unattended/recovery;
- visual;
- accessibility;
- security;
- performance;
- human/subjective review where unavoidable.

Significant behavior may require multiple proof types.

Do not force an office requirement to choose between “UI-runtime” and “visual” when it needs both.

---

## S4.2 — Boot acceptance

**Decision:** Canonical Home = **Organization Overview**.

From there the user enters departments.

Viewport set:
- 1280×800;
- 1366×768;
- 1672×941 if that is the supplied mockup frame;
- 1920×1080;
- representative tablet;
- narrow mobile for responsive checks later.

M0 boot predicate can use 1280×800 and 1672×941; final visual suite should be broader.

---

## S4.3 — Design tokens

**Decision:** Extract a token specification from the supplied mockups and final visual brief.

Store machine-readable design tokens:
- colors;
- background layers;
- borders;
- accent roles;
- typography scale;
- spacing;
- radius;
- shadows/glow;
- status colors;
- motion durations;
- office sizing conventions.

Owner approval is useful before visual freeze.

Do not use tokens as an excuse to flatten the design into a generic template.

---

## S4.4 — Existing test suite

**Decision:** Confirm.

Existing baseline suite must stay green unless:
- a test is proven obsolete/incorrect;
- its replacement is explicitly documented.

Baseline failures discovered before implementation must be recorded separately.

---

## S4.5 — Unattended predicates

**Decision:** Confirm the injected-clock harness for fast deterministic testing.

Additionally:
- perform at least one real-clock schedule test;
- perform one real browser-closed/background execution test;
- perform a multi-day soak.

Injected time is excellent for logic; it does not completely replace real scheduling evidence.

---

## S4.6 — Office truthfulness

**Decision:** DOM/state assertions are necessary but not sufficient.

For each canonical state verify:
1. backend semantic state;
2. API/state adapter output;
3. textual employee dossier;
4. office status label/badge;
5. animation/state class or renderer state;
6. visual evidence for representative states.

The animation may contain decorative motion, but its semantic class must match real state.

Idle ambient behavior is allowed; fake productive behavior is not.

---

## S4.7 — Performance gates

**Decision:** Do not remove all performance criteria.

For M0:
- boot/service ready <30s is acceptable as a coarse gate;
- UI interaction should not visibly stall;
- schedule fire drift should be measured.

For final product preserve the stronger targets from the product protocol:
- warm navigation target around <=2s p95 where realistic;
- local UI feedback around <=200ms p95;
- local read APIs around <=300ms p95 where meaningful;
- main office aiming ~55–60fps on documented test hardware;
- memory-leak investigation on repeated mounts/navigation.

Do not make these brittle if the environment makes a specific number meaningless; measure and document.

---

## S4.8 — Flake policy

**Decision:** Confirm with classification.

- Logic failure: zero blind retry.
- Known transport/network transient: at most one automatic retry.
- Flaky test: defect in test/product until root cause established.
- Do not rerun until green and call it success.

Every retry remains visible in evidence.

---

## S4.9 — Failure creates work

**Decision:** Confirm.

The failure-generated work item should include:
- failing predicate ID;
- requirement IDs;
- exact SHA;
- observed result;
- expected result;
- reproduction command;
- evidence paths;
- likely failure class;
- permitted file scope;
- completion proof.

Spot-checking a sample of 10 during Stage-0 is appropriate, but the controller should schema-validate all automatically.

---

# S5 — ACCEPTANCE HARNESS

## S5.1 — Harness layout

**Decision:** `verify.sh` plus modular `checks/` is acceptable.

The controller must run verification against the exact integrated SHA.

Do not automatically revert every failing integration blindly.

Instead:
- mark integration rejected;
- preserve the SHA/branch/evidence;
- revert or repair according to task policy.

Evidence preservation is more important than keeping the branch artificially green.

---

## S5.2 — Hash protection

**Decision:** Confirm.

Workers must not be able to silently modify acceptance criteria to pass.

Protected:
- requirement ledger;
- predicate definitions;
- harness core;
- release gate;
- test fixtures used as independent acceptance truth.

Changes require dedicated harness-change workflow/review.

---

## S5.3 — Calibration fixtures

**Decision:** Strongly confirm.

Use known-bad cases including:
- missed schedule falsely marked success;
- duplicate schedule occurrence;
- office state lies;
- unauthorized MCP access;
- approval bypass;
- memory leakage between employees;
- retry causes duplicate side effect;
- workflow completion despite failed mandatory step.

The harness must prove it catches bad behavior.

---

## S5.4 — Independent harness review

**Decision:** Confirm.

Use a fresh strong reviewer, ideally a different model family from the harness implementer.

Opus via subscription is appropriate where available.

The reviewer must:
- inspect false-negative risk;
- inspect weak assertions;
- inspect fixture validity;
- challenge bypass paths.

---

## S5.5 — Time budget

**Decision:** <10 minutes for the routine post-integration harness is a good target.

Longer suites should be tiered:
- fast verify;
- integration;
- visual;
- security;
- soak/recovery.

Do not force the 3-day soak into `verify.sh`.

---

## S5.6 — Release gate

**Decision:** For **M0 gate**, require:
- all M0 predicates pass;
- representative real background run passes;
- short soak passes;
- independent review passes.

For **final product release**, require:
- all CORE-REQUIRED predicates pass;
- full required resilience/soak suite passes;
- independent full release review;
- visual release gate;
- security gate;
- final exact SHA.

No LLM may mark the product globally shipped by prose alone.

---

# S6 — EXECUTION GOVERNANCE

## S6.1 — Build controller

**Decision:** Reuse the repaired Nailify controller **as a proven starting point**, not as unquestioned product-specific truth.

Before adapting:
- isolate generic controller behavior;
- remove Nailify-specific requirement semantics;
- verify current acceptance semantics;
- add only failure classes actually needed.

Do not build another large orchestrator from scratch unless the current controller fundamentally cannot meet requirements.

---

## S6.2 — Build state store

**Decision:** In-repo `.hermes/autonomy/project.db` is acceptable for **build-campaign state**.

This is separate from product runtime state.

Keep this distinction explicit.

---

## S6.3 — Build event log

**Decision:** Confirm.

Log:
- tick;
- queue state;
- claim;
- dispatch;
- worker start/end;
- result classification;
- verification;
- rework;
- idle reason;
- provider state;
- human intervention;
- controller restart.

“Why is the controller idle?” must be answerable deterministically.

---

## S6.4 — Worker packet fields

**Decision:** Confirm proposed fields and add:
- task ID;
- run/attempt ID;
- base SHA;
- worktree/branch;
- source requirement text;
- dependencies;
- known architecture contracts;
- allowed data/secrets class;
- model/tool policy;
- relevant prior review defects;
- expected structured handoff schema;
- explicit out-of-scope list;
- escalation behavior;
- no-self-approval clause.

Packets should be bounded and minimal-complete.

---

## S6.5 — Worker runtime

**Decision:** Use fresh bounded Hermes sessions under dedicated build profiles.

Do not expose:
- this chat’s broad personal context;
- unrelated skills;
- unrelated projects;
- unnecessary secrets.

Each worker receives only task-relevant context.

---

## S6.6 — Provider/model freeze

**Decision:** Use a verified free implementation pool with **effective-model attribution mandatory**.

Prefer pinned model for:
- benchmark reproducibility;
- high-risk comparisons.

Allow `auto`/pool for:
- routine implementation after benchmark;
- only if effective model/provider is recorded.

Reviewer:
- Opus/Sonnet subscription depending risk.

Do not let strong subscription reviewers silently become primary implementers.

---

## S6.7 — Paid ceiling

**Decision:** Build-time new pay-as-you-go AI spend ceiling remains **$0** unless the owner explicitly changes it later.

Existing subscriptions are allowed.

No automatic paid fallback.

---

## S6.8 — Attempt schema

**Decision:** Proposed fields are good. Add:
- base_sha;
- result_sha;
- worker/profile ID;
- task class;
- failure_class;
- files_changed;
- tests_run;
- review_verdict;
- retry_of_attempt;
- artifact/evidence paths;
- provider response/error code;
- quota/rate-limit marker;
- human intervention reason.

Add statuses:
- ACCEPTED;
- REVIEW_REJECTED;
- WAITING_PROVIDER;
- CANCELLED;
- POLICY_BLOCKED.

Keep implementation result and acceptance result separate where possible.

---

## S6.9 — Human-intervention counter

**Decision:** Confirm, but do not treat every owner review/sign-off as a failure.

Classify:
- required governance approval;
- product decision;
- rescue/intervention;
- manual technical repair;
- informational review.

Campaign KPI should focus on avoidable rescue interventions, not penalize legitimate product decisions.

---

## S6.10 — Stop rules

**Decision:** Amend.

### Rule 1
Keep: no concurrency growth until single-worker baseline is proven.

Threshold:
- at least 20 representative valid attempts;
- ≥60% accepted first-pass or equivalent clear evidence.

### Rule 2
Do not create recursive supervisor/director hierarchies.

A single durable planner/controller is preferred.

However, bounded temporary planning/review sessions are allowed.

The product’s “Director” employee is unrelated to the build campaign.

### Rule 3
Confirm:
do not build recovery machinery for failure classes not observed or clearly unavoidable by architecture.

### Rule 4
Amend:
model/provider switching can also occur when a provider is objectively unavailable/rate-limited, not only after ten failures.

But it must follow pre-approved routing policy and be recorded.

---

## S6.11 — Campaign budget ceiling

**Decision:** Use **200 valid attempts / 14 calendar days / 2 structured re-baselining rounds** for the first autonomous build campaign.

At that threshold:
- stop autonomous dispatch;
- produce a diagnostic report;
- preserve state;
- request owner decision.

This is **not** permission to call the product failed or finished.

It is a campaign-control boundary to avoid infinite burn.

---

## S6.12 — Watchdog

**Decision:** Confirm.

Systemd watchdog/controller:
- restart dead controller;
- enforce one instance;
- log;
- respect pause;
- no LLM reasoning;
- no spawning recursive supervisors.

Linger/start-on-boot must be proven.

---

## S6.13 — Reporting cadence

**Decision:**
- immediate alert only for genuine owner blocker, policy violation or campaign stop condition;
- daily summary;
- phase-gate checkpoint.

Daily summary should contain:
- requirements accepted that day;
- tasks attempted;
- first-pass acceptance;
- retries/rework;
- open tasks;
- blocking failures;
- provider health;
- controller idle time + reasons;
- human rescue interventions;
- current Git SHA;
- next planned dependency frontier;
- build spend classification.

Do not spam the owner for normal failures.

---

## S6.14 — Artifact locations

**Decision:** Build-campaign artifacts can live under `.hermes/` if:
- structured;
- documented;
- excluded from product runtime state;
- not containing secrets.

Suggested:
- `.hermes/autonomy/`
- `.hermes/packets/`
- `.hermes/checkpoints/`
- `.hermes/reviews/`
- `.hermes/evidence/`
- `.hermes/benchmarks/`

Large generated artifacts may live outside Git with indexed paths.

---

## S6.15 — Kill criteria

**Decision:** Amend wording from “campaign ends” to “autonomous campaign pauses for owner review.”

Trigger pause on:
a. 200 valid attempts / campaign budget exhausted without meaningful gate progress;
b. acceptance <30% after two packet/decomposition redesign rounds;
c. owner materially changes product definition;
d. soak fails 3 consecutive times for the same unresolved cause;
e. security/policy violation;
f. evidence suggests controller is creating duplicate work or losing state;
g. unexpected paid AI spend.

Do not continue blindly.

---

## S6.16 — Provider outage

**Decision:** Free implementation provider pool unavailable >4h:
- pause affected AI implementation dispatch;
- continue deterministic tests/reconciliation that do not need the provider;
- notify in daily/exception channel;
- do not auto-fallback to paid route.

If another already-approved verified-free route exists, it may be used according to routing policy.

---

# S7 — PRE-REGISTERED BENCHMARK

## S7.1 — Benchmark task

**Decision:** Use the **free-games monitor end-to-end** as the primary benchmark vertical slice.

It is the best first slice because it tests:
- external information retrieval;
- schedule;
- workflow run;
- employee assignment;
- model/tool route;
- artifact;
- dedup;
- notification;
- persistence;
- reporting.

However the 20 attempts should not hit live stores identically each time.

Use:
- deterministic fixture/source adapter for repeatability;
- one or more real integration runs separately.

---

## S7.2 — Count

**Decision:** 20 valid attempts initial benchmark.

Hard ceiling 40 before mandatory diagnosis.

Provider aborts that never started meaningful work can be excluded from quality denominator but must remain reported separately.

---

## S7.3 — Decision rules

**Decision:** Confirm thresholds as build-system rules:

- ≥60% accepted → allow controlled concurrency growth.
- 30–59% → improve packet/task decomposition; no added orchestration layer.
- <30% → stop scaling; redesign task shape/context; diagnose.

Do not respond to poor quality by adding more supervisors.

---

## S7.4 — Measurement fields

**Decision:** Confirm and add:
- first-pass acceptance;
- final acceptance after rework;
- failure class;
- diff size;
- tests executed;
- token use if known;
- provider latency;
- reviewer verdict;
- collateral-edit rate;
- task complexity class.

Flat JSONL plus summarized report.

---

## S7.5 — Freeze before attempt 1

**Decision:** Confirm.

Freeze:
- task;
- acceptance predicate;
- fixture;
- packet format;
- selected route/policy.

Harness bug fixes are allowed only with:
- dedicated issue;
- independent review;
- rerun of affected attempts if comparability changed.

---

## S7.6 — Session hygiene

**Decision:** Confirm.

Fresh worker session per attempt.

Worker self-report is evidence input, never the acceptance authority.

The exact integrated code + harness decides.

---

# S8 — CAMPAIGN PHASES, SOAK, POST-FOUNDATION

## S8.1 — Phase gates

**Decision:** Amend order slightly.

Recommended:

### Phase F0 — Source reconciliation / architecture freeze
- complete ledger;
- reuse matrix;
- domain contracts;
- engine decision;
- acceptance harness.

### Phase F1 — Durable domain + persistence
- organization;
- department;
- employee;
- workflow definitions;
- schedules;
- runs;
- memory skeleton;
- permissions skeleton.

### Phase F2 — Scheduler + workflow engine
- durable occurrences;
- task/attempt lifecycle;
- retries;
- handoffs;
- approvals;
- events.

### Phase F3 — First real recurring workflow
- free-games monitor;
- notification;
- reporting;
- real unattended execution.

### Phase F4 — Model/MCP/Memory proof
- two model routes;
- scoped MCP/tool permission;
- persistent employee memory retrieval.

### Phase F5 — Living office + organization/department UI
- truthful state adapter;
- employee dossier;
- calendar;
- activity;
- reports.

### Phase F6 — QA/review + project workflow
- implementation handoff;
- independent QA;
- human approval distinction.

### Phase F7 — Resilience / soak / foundation gate
- recovery;
- browser closed;
- restart;
- provider failure;
- 3-day soak;
- independent review.

Then continue into the remaining CORE-REQUIRED product capabilities.

No owner sign-off should be needed after every tiny phase unless a real product/architecture decision is pending. The goal is autonomy, not repeated permission prompts.

---

## S8.2 — Soak definition

**Decision:** 72 consecutive hours is acceptable for M0/Foundation.

During soak:
- normal user viewing is allowed;
- no AI coding workers may patch the product;
- deterministic runtime processes continue;
- free-games workflow runs on real schedule;
- state survives;
- errors are recorded;
- no manual DB state patches.

For final release, perform broader resilience tests beyond this one routine.

---

## S8.3 — Games monitor specifics

### Stores
M0:
- Steam;
- Epic Games Store.

Later adapters:
- GOG;
- Amazon Prime Gaming;
- others.

### Data source
Preference order:
1. official/public documented source/API/feed;
2. stable first-party web endpoint;
3. browser/scraping fallback.

Do not depend on brittle scraping if a reliable official source exists.

### Frequency
**Daily**, not hourly, for real production use.

Default time:
**09:00 Europe/London**.

Reason:
free-game promotions do not justify 24 hourly checks/day, and unnecessary runs waste resources.

For soak testing, a test schedule may run more frequently using a dedicated test workflow/clock.

### Dedup
Do not use a blind “30 days” rule only.

Deduplicate primarily by:
- store;
- canonical item ID;
- promotion/free-window identity.

Alert again only if:
- a genuinely new free promotion occurs;
- the prior promotion ended and a new one starts;
- the source meaningfully changes.

### History
Keep all run history initially.

Do not silently delete alerts at M0.

### Alert payload
Include:
- game/item name;
- store;
- normal/current price if available;
- current free price;
- source URL;
- promotion start;
- promotion end / claim-by deadline;
- time checked;
- confidence/source notes if data is uncertain.

---

## S8.4 — Soak failure handling

**Decision:** Confirm.

Failure:
- creates defect;
- preserves evidence;
- repairs via normal workflow;
- restarts soak window relevant to the repaired subsystem.

No manual DB patching to manufacture a pass.

---

## S8.5 — Next-stage ordering

**Decision:** The proposed order should change because MCPs and learning are more central than voice/finance.

After M0 Foundation:

1. full workflow builder and reusable workflow templates;
2. full MCP/integration registry + per-employee permissions;
3. richer employee memory + controlled learning loop;
4. second real department + cross-department workflows;
5. richer model routing and performance learning;
6. voice receptionist/realtime-worker capability;
7. external calendar/email/notification integrations;
8. finance templates/module;
9. multi-user/multi-tenant if desired.

The exact order may move based on dependency analysis.

Telephony provider is **not precommitted to Twilio**. Evaluate current providers, cost, latency and existing stack before choosing.

---

## S8.6 — Approvals UX at M0

**Decision:** The defaults proposed are too approval-heavy and would undermine autonomy.

### (a) Publishing a free-games alert artifact
**No approval after workflow activation.**

The user explicitly wants the bot to monitor and bring findings to attention automatically.

### (b) Project workflow past a handoff point
Approval only if that specific step is configured as approval-required.

A normal bot-to-bot handoff should not require the owner.

### (c) Approving a review verdict
No owner approval required for routine QA verdict.

QA can accept/reject according to criteria.

Human authorization is separate.

### (d) First-time scheduled execution
Use a workflow activation/test flow:
- user explicitly activates workflow;
- once activated, recurring executions run autonomously.

Do not request approval every first occurrence after restart/version.

Require human approval only for high-impact actions:
- destructive production action;
- external spending;
- irreversible data change;
- public deployment/publishing if configured;
- security/firewall/DNS;
- financial transfer;
- other user-defined risky actions.

---

## S8.7 — Design fidelity

**Decision:** For M0:
- strong structural fidelity;
- correct information hierarchy;
- coherent dark/cyan visual system;
- high-quality Personal Software office;
- correct states;
- no obviously generic/unfinished screens.

Do not require literal pixel identity to concept art if it harms responsiveness or operational clarity.

For final core release:
- premium polish across all core screens;
- no unresolved critical/high visual defects;
- mockups remain quality/direction references.

---

## S8.8 — Office character assets

**Decision:** Reuse the supplied character/reference assets first.

The original source package reportedly includes:
- character designs;
- proportion sheets;
- state references;
- movement keyframes;
- office environments.

Inventory those before creating replacement SVGs.

If production-ready assets are missing:
- create deterministic original 2D assets;
- use shared rig/state system;
- do not make character production a blocker for workflow semantics.

Do not assume simple six-state SVGs are the final aesthetic if better supplied material exists.

---

## S8.9 — Audio

**Decision:** No general UI audio subsystem required at M0.

Voice/receptionist audio is a later runtime capability and should be architected separately.

Do not import unrelated personal-OS audio requirements.

---

## S8.10 — Post-ship operation

**Decision:** Initial deployment is a personal/private operational system.

No formal external commercial SLO at M0.

However:
- persistent jobs should be expected to recover automatically;
- failures should be visible;
- backups and restart behavior should be reliable.

If later offered commercially, define SLOs then.

---

## S8.11 — Product runtime model costs

**Decision:** Product runtime must support configurable provider routes.

M0:
- one or more preconfigured route adapters;
- at least two usable routes if possible to prove model diversity;
- no API keys in repository;
- settings UI shows configured status;
- employee/step model policy is editable.

FreeLLMAPI may be a default route where fit is good.

But the product must not be architecturally tied to FreeLLMAPI.

The user can later add OpenRouter, direct providers, research providers such as Perplexity, local models, etc.

Runtime product costs are a product policy, distinct from the $0 build-campaign policy.

---

## S8.12 — Calendar

**Decision:** M0 includes an **in-app schedule/calendar view**.

External Google/Outlook calendar synchronization can be later.

The in-app calendar is mandatory because planning bot work over time is central to the product.

---

# S9 — PROCESS & META

## S9.1 — Answer batch

**Decision:** This document answers **all S0–S9 questions now**.

Do not wait for another owner questionnaire unless a truly unresolved product choice emerges from the live environment.

Hermes should now produce the Stage-0 pack.

---

## S9.2 — “All defaults” mechanic

**Decision:** This answer set supersedes the need for “S# all defaults.”

Where this document explicitly confirms a default, it is approved.

Where it amends a default, the amendment wins.

Any future changed owner decision becomes:
- a versioned Decision Register entry;
- with date;
- reason;
- affected requirements.

Do not silently rewrite historical decisions.

---

## S9.3 — Stage-0 pack review

**Decision:** Confirm with one addition.

Stage-0 pack should include:

1. Decision Register;
2. source inventory;
3. source conflict register;
4. reuse/build matrix;
5. orchestrator/workflow-engine evaluation;
6. current-repo audit;
7. canonical domain model;
8. full requirement ledger v1;
9. milestone grouping;
10. dependency graph;
11. predicate drafts;
12. acceptance harness design;
13. calibration fixture plan;
14. build governance files;
15. provider/model benchmark plan;
16. product architecture diagrams/contracts;
17. risk register;
18. explicit list of still-unanswered decisions, ideally empty.

Then run the representative benchmark.

---

## S9.4 — Start trigger

**Decision:** The first **large autonomous campaign** should begin only after:
- Stage-0 pack exists;
- benchmark exists;
- no critical unresolved source conflict remains;
- controller/harness are proven.

However, the user should not need to manually say “continue” at every subsequent stage.

One explicit launch approval for the autonomous campaign is sufficient unless:
- product definition materially changes;
- destructive action requires approval;
- campaign stop condition fires.

---

## S9.5 — This chat’s role / review time

**Decision:** Do not design the system around a fixed weekly owner-review quota.

Assume owner attention is scarce.

The system should:
- batch non-urgent decisions;
- produce concise phase summaries;
- interrupt only for genuine blockers/risk;
- continue routine work autonomously.

For planning purposes, design as if the user may inspect the project only **once per day or less** during an autonomous campaign.

The acceptance machinery must not require constant human presence.

---

# FINAL LOCKED PRINCIPLES FOR HERMES

The following principles supersede any narrower default in the questionnaire:

1. **Do not call M0/P0 the finished product.**
2. **AC-001–060 is not exhaustive.**
3. **The complete requirement ledger must be extracted from all authoritative sources.**
4. **Specialized persistent employees are a core product concept.**
5. **Recurring and event-driven workflows are as important as one-off projects.**
6. **Scheduling/calendar is first-class.**
7. **Durable bot-to-bot handoffs are first-class.**
8. **Each employee needs durable, scoped memory.**
9. **Different employees/jobs must be able to use different LLMs.**
10. **MCP/tool access is per employee and least-privilege.**
11. **The user should not babysit routine execution.**
12. **The browser may close while work continues.**
13. **The living office must reflect real operational state.**
14. **Reporting must make all meaningful work understandable after the fact.**
15. **QA and human approval are different concepts.**
16. **Open-source/existing infrastructure should be reused before generic custom plumbing is built.**
17. **One deterministic control plane owns build execution state; avoid recursive supervisor trees.**
18. **Workers are disposable; durable state is not.**
19. **Evidence, not worker self-report, determines acceptance.**
20. **No fake production metrics or synthetic operational state.**
21. **No automatic paid AI fallback during the build campaign.**
22. **Final product release requires the complete mandatory product ledger, not only the first vertical slice.**

---

# EXPECTED NEXT ACTION FROM HERMES

Hermes should not ask another broad generic questionnaire.

It should now:

1. ingest this answer set;
2. reconcile it with the original product sources;
3. audit the actual machine/repositories;
4. produce the Stage-0 pack;
5. identify only genuinely unresolved decisions that cannot be answered from existing evidence;
6. run the pre-registered representative benchmark after the Stage-0 pack is approved;
7. use benchmark evidence to size the autonomous build campaign;
8. proceed without routine owner interruption once the campaign is explicitly launched.

```

===== 2026-09-22 11:52 | session 20260922_105531_432d90 | AI staff force set up =====
are there any remaining gaps in the questionsing before we can start

===== 2026-09-22 11:53 | session 20260922_105531_432d90 | AI staff force set up =====
@file:`.hermes/attachments/EMPIRIUM_HERMES_S0-S9_OWNER_ANSWERS_2026-09-22.md`

are there any remaining gaps in the questionsing before we can start

--- Attached Context ---

📄 @file:`.hermes/attachments/EMPIRIUM_HERMES_S0-S9_OWNER_ANSWERS_2026-09-22.md` (14512 tokens)
```markdown
# EMPIRIUM STUDIO / AI STAFF FORCE
# OWNER DECISION REGISTER — ANSWERS TO HERMES S0–S9 AUTONOMY QUESTIONS

**Date:** 2026-09-22  
**Status:** Owner-intent answer set for Stage-0 planning.  
**Purpose:** Remove ambiguity before Hermes is allowed to plan or execute autonomously.

---

# 0. Read this before interpreting any individual answer

There are several important corrections to the framing of the question set.

## A. P0 is NOT the finished product

The most important correction is that **P0 must not be treated as “SHIPPED” for the whole product**.

The product has repeatedly suffered from scope collapse: a large intended system becomes a small vertical slice, the small slice passes tests, and an orchestrator then describes the overall product as finished.

That is not acceptable here.

For this project:

- **P0 / M0 = Foundation + first representative end-to-end operating slice.**
- It proves the architecture can support the real product.
- It is allowed to be narrower than the full product.
- Passing P0 means “the foundation is proven,” not “Empirium Studio is shipped.”
- The final release gate must remain tied to the complete mandatory requirement ledger derived from all authoritative product sources.

If Hermes wants a three-tier system, use:
- **M0 / Foundation** — first integrated proof.
- **M1 / Core Product** — all central product capabilities implemented.
- **M2 / Extended Product** — explicitly non-core future enhancements.

Do not use “P1 = not required for SHIPPED” for capabilities that are clearly mandatory in the product charter.

## B. AC-001–060 is a base, not the exhaustive requirement ledger

AC-001–060 is useful as a behavioral spine, but it is **not exhaustive enough to represent the complete product**.

The full ledger must also be extracted from:
- the original two-part Empirium Studio master protocol;
- the consolidated final product brief;
- supplied mockups;
- later conversation clarifications;
- relevant AI Staff Force project decisions;
- explicit workflow, memory, MCP, model-routing, scheduling, calendar, reporting, voice/receptionist and observability requirements.

Do not cap the ledger at 60–90 requirements merely because AC-001–060 has 60 entries.

The full product will almost certainly compile to **hundreds of atomic requirements** once UI states, workflow behavior, security, failure recovery, permissions, model routing, memory, observability, accessibility and acceptance predicates are decomposed properly.

## C. Reuse-first is a hard engineering preference

Before custom-building generic orchestration, scheduling, retries, queues, MCP plumbing, long-running workflow state, or worker lifecycle mechanisms:

1. inspect Hermes;
2. inspect already-installed infrastructure;
3. evaluate mature open-source components;
4. evaluate the AWS CAO/orchestration system previously discussed by the user, if locally/relevantly available;
5. compare candidates to the exact Empirium contract;
6. integrate or wrap the best-fitting existing substrate.

Empirium should own the product semantics, not necessarily every low-level runtime mechanism.

## D. Product employees and build workers are different things

The workers that build Empirium are disposable engineering workers.

The employees inside Empirium are permanent product entities.

Do not confuse them.

---

# S0 — PRODUCT CHARTER & SCOPE FREEZE

## S0.1 — Canonical name

**Decision:** Use **“Empirium Studio”** as the canonical product/UI name for this build. The descriptive subtitle may be **“AI Workforce”** or **“AI Staff Force”** in documentation and onboarding.

Use:
- Product brand: **Empirium Studio**
- Product descriptor: **AI Workforce**
- Internal project aliases: AI Staff Force / AI Star Force are acceptable project-history terms only.

Do **not** merge this product into the existing personal “Empirium OS” application merely because older mockups show “EMPIRIUM OS.”

The branding should be configuration-driven so the product can later be renamed without changing the domain model.

---

## S0.2 — One-line definition

**Decision:** Replace the proposed line with the following canonical definition:

> **Empirium Studio is a persistent AI workforce operations platform in which specialized digital employees, each with configurable models, MCP/tool access, memory, permissions and job rules, execute recurring, scheduled, event-driven and project-based work through durable workflows and handoffs, while the user plans, observes, approves, audits and improves that work through a truthful living-office control interface.**

This sentence is a better decomposition anchor because it captures:
- persistent employees;
- specialization;
- multiple LLMs;
- MCPs/tools;
- memory;
- permissions;
- workflows;
- schedules;
- event-driven work;
- projects;
- handoffs;
- human control;
- reporting/observability;
- living office.

Do not shorten it in a way that loses those concepts.

---

## S0.3 — P0 “shipped” slice

**Decision:** I do **not** accept P0 as the whole product’s SHIPPED slice. Treat it as **M0 Foundation / Representative Vertical Slice**.

For M0, the proposed items are approved with the following additions and amendments:

### M0.1 Durable domain
Required.

The minimum durable domain should include:
- Organization;
- Department;
- Employee;
- Execution Profile;
- Workflow Definition;
- Schedule;
- Workflow Run;
- Task/Step;
- Attempt/Run;
- Artifact;
- Handoff;
- Review;
- Approval;
- Notification;
- Memory;
- Knowledge reference;
- Event;
- Report.

SQLite may be the first authority if the architecture remains migration-friendly.

### M0.2 Durable scheduler
Required.

Must:
- operate with browser closed;
- persist schedules;
- create unique occurrence identities;
- support missed-run policy;
- prevent duplicate occurrences;
- support timezone-aware scheduling;
- survive process restart.

### M0.3 Seed department
Required.

Use **Personal Software** as the canonical first fully exercised department because it already has the strongest product definition.

Seed **5 permanent employees**:
1. Director;
2. Research Architect;
3. Developer / Implementation Engineer;
4. QA Engineer;
5. Learning Analyst.

The office may visibly show 3–5 at a time if layout requires, but all five must exist as real persistent employees.

### M0.4 Recurring real workflow
Required.

Use the **Steam + Epic free-games monitor** as the first real unattended recurring workflow because:
- it is real;
- it is low risk;
- it exercises scheduling;
- it exercises external data acquisition;
- it exercises deduplication;
- it exercises artifacts;
- it exercises notification;
- it gives immediate proof that background work is real.

### M0.5 Project/handoff workflow
Required.

Use one second workflow that proves:
- one employee performs work;
- structured handoff occurs;
- another employee continues;
- approval can pause only the dependent path;
- resumption is durable.

A small Personal Software change workflow is suitable.

### M0.6 Truthful living office
Required.

One fully animated/operational department is enough for M0.

The organization overview can use lightweight/static mini-office projections.

### M0.7 Reporting
Required.

Must answer:
- what ran today;
- what succeeded;
- what failed;
- what is waiting;
- what requires attention;
- what is scheduled next;
- which employee/model/tool acted.

### M0.8 Simple workflow creation without code
Required.

A form/template builder is sufficient for M0.

### M0.9 Model routing
The original proposed default is **too weak**.

M0 must prove that the architecture genuinely supports different models for different employees.

Therefore M0 should have:
- at least **two configurable model routes**;
- at least **two employees/steps using different routes**;
- per-employee model policy visible in UI;
- actual/effective route telemetry where available.

This does not mean two paid providers are required. Two verified usable routes are enough.

### M0.10 QA vs approval
Required.

Must prove:
- independent quality review is not the same thing as;
- human authorization to perform a consequential action.

### M0.11 Persistent employee memory
**Add to M0.**

At least one employee must:
- write an approved memory;
- terminate its session;
- later retrieve that memory;
- use it appropriately;
- retain provenance.

Memory is too central to defer entirely.

### M0.12 MCP/tool permission proof
**Add to M0.**

A full integration marketplace is not necessary, but M0 must prove:
- one employee has access to a real MCP/tool;
- another employee does not;
- unauthorized use is denied by policy/server-side enforcement;
- usage is auditable.

MCP capability is too central to leave completely unproven.

### M0.13 Calendar/schedule view
**Add to M0.**

A basic in-app schedule/calendar surface should show:
- next occurrences;
- recurring routine;
- recent occurrences;
- pause/run-now/edit recurrence.

### M0.14 Memory/reporting/office truth
The free-games run should become visible simultaneously in:
- workflow run history;
- activity;
- employee current/recent work;
- report;
- schedule history;
- office state while active.

This is an important integration proof.

---

## S0.4 — P0 exclusions register

**Decision:** Reclassify the exclusions carefully.

### Out of M0, but mandatory later in the core product
- full learning/improvement loop;
- full MCP registry and capability-management UI;
- cross-department workflows;
- voice/receptionist execution;
- richer workflow graph builder;
- richer calendar integration;
- multiple real departments;
- advanced model-routing optimization.

These are not “optional backlog.” They are deferred from the first foundation milestone only.

### Likely post-core / optional expansion
- full finance-specific module/templates;
- broad multi-tenant SaaS support;
- native mobile app.

### Important distinction
The underlying architecture must support:
- voice workers;
- cross-department handoffs;
- multiple integrations;
- model diversity

before final product release, even if every possible connector/template is not shipped.

---

## S0.5 — Office scope

**Decision:** For M0:
- one department gets the full animated living office;
- organization overview uses static or heavily throttled mini-office cards.

For the final product:
- every department can have a living-office representation;
- only the currently opened department should run the full scene;
- mini-offices should be snapshot/throttled representations for performance.

Do not run multiple full 60fps office simulations.

---

## S0.6 — Workflow builder depth

**Decision:** M0 uses:
- form-based creation;
- templates;
- read-only visual graph/timeline;
- explicit step configuration.

A full drag-and-drop graph editor is not required for M0.

However, **a true visual workflow builder is mandatory for the core product**, because the long-term experience is that users should be able to assemble and modify work cascades without editing source code.

The visual builder must eventually support:
- agent nodes;
- deterministic tool nodes;
- branches;
- delays;
- approvals;
- handoffs;
- joins;
- sub-workflows;
- MCP actions.

---

## S0.7 — Users

**Decision:** Single-user/operator at M0 and initial core deployment.

No secondary operator account is required for M0.

However:
- permissions must be designed as real policy concepts rather than hardcoded “because there is one user” assumptions;
- future multi-user support should not require rewriting the core employee/workflow model.

Multi-user is not a first milestone priority.

---

## S0.8 — Delivery form

**Decision:** Web application served on the VPS, consistent with Hermes Studio.

Desktop wrapper/Electron is deferred.

Reason:
- browser UI is appropriate for a persistent server-side workforce;
- background execution must not rely on desktop app lifetime;
- web access via secure private networking is simpler.

---

## S0.9 — Deployment & access

**Decision:** Initial deployment:
- standalone service on the VPS;
- private access only;
- bind locally and expose through the user’s existing secure private access method, preferably Tailscale or existing trusted proxy;
- no new public internet exposure by default.

Do not hardcode a port before inspecting current services and avoiding conflicts.

Port should be discovered/configured during Stage 1.

Primary machine is the current VPS/host where Hermes is already being operated.

Do not require GPU.

---

## S0.10 — First production workload

**Decision:** Yes, the Steam + Epic free-games monitor should run for real from the first live milestone.

**Primary notification channel for M0:** in-app notification/attention inbox.

Reason:
- it proves the Empirium notification system itself;
- it avoids making Telegram/email credentials a blocker;
- external notification adapters can then be added cleanly.

**Secondary preferred channel after core in-app proof:** Telegram.

Do **not** create external accounts/bots without explicit user action if provider setup requires account authorization.

The architecture should make notification channels pluggable.

---

## S0.11 — Seed content

**Decision:** Hermes may draft:
- Personal Software department content;
- the five employee personas;
- roles;
- responsibilities;
- routing descriptions;
- model/tool policies;
- starter workflows.

However:
- these become versioned configuration;
- they are not immutable product code;
- they should be reviewable/editable by the user.

Hermes does **not** need to stop for approval of every individual name before building the schema/UI.

Use high-quality provisional names and roles; owner approval can occur at the configuration-freeze checkpoint.

Role correctness is more important than character naming.

---

## S0.12 — Org structure mutability

**Decision:** Yes, P0/M0 should support runtime:
- create;
- rename;
- edit;
- disable/archive

for departments and employees.

Deletion should use **soft delete/archive with tombstones** by default.

Hard delete should be:
- separate;
- high-friction;
- approval-protected;
- only possible where retention/reference integrity is preserved.

No sub-team hierarchy is required initially.

---

## S0.13 — Timezone

**Decision:** Default timezone is **Europe/London**, but timezone is a real configurable field from day one.

Use:
- organization default timezone;
- workflow/schedule override where necessary;
- display in user/local timezone.

Do not make Europe/London an unchangeable global constant.

All stored timestamps should use an unambiguous canonical representation such as UTC plus explicit timezone metadata for recurrence.

DST behavior must be tested.

---

## S0.14 — No fake data

**Decision:** Confirm with one refinement.

Allowed:
- deterministic test fixtures;
- Storybook/dev/demo fixtures;
- clearly labeled synthetic acceptance data.

Not allowed in production:
- fake active employees;
- fake runs;
- fake spend;
- fake QA;
- fake “health”;
- fake progress;
- fake activity.

Seed configuration such as default employees and a default workflow is real configuration, not fake telemetry.

Production dashboards must derive from real stored state.

---

## S0.15 — Language / accessibility / analytics

**Decision:**
- English only initially.
- Architecture should not actively prevent future i18n.
- Accessibility target: **WCAG 2.1 AA where reasonably applicable** for the product UI.
- Full living-office animation must have textual equivalents.
- Reduced-motion support is required.
- No third-party product analytics/telemetry by default.
- First-party operational telemetry/logging is required because the product must report its own work.

---

# S1 — DATA & STATE ARCHITECTURE

## S1.1 — P0 database

**Decision:** SQLite is acceptable as the initial single authoritative operational database if current-scale testing confirms it is sufficient.

Use a runtime state directory outside the repository, e.g.:
`~/.local/state/empirium-studio/`

Do not store mutable production DB state in Git.

Use:
- WAL mode where appropriate;
- migrations;
- transactional writes;
- backups;
- foreign keys.

Design schema so a later move to Postgres is feasible.

Do not prematurely move to Postgres unless scale/concurrency requires it.

---

## S1.2 — Complete mutable-state list

**Decision:** The proposed list is incomplete.

SQLite/authoritative persistence should cover at least:

- organization;
- organization policies/settings;
- departments;
- employees;
- execution profiles;
- employee config versions;
- workflow definitions;
- workflow versions;
- workflow triggers;
- schedules;
- schedule occurrences;
- workflow runs;
- steps/tasks;
- attempts;
- artifacts metadata;
- handoffs;
- reviews;
- approvals;
- notifications;
- employee memory;
- knowledge metadata/index references;
- learning proposals;
- reports;
- tool/MCP registry;
- tool grants/permissions;
- model/provider registry;
- model-routing policy;
- provider health state;
- notification channels;
- secrets references (not raw secrets unless a vault design specifically allows it);
- app settings;
- audit/config change records;
- meaningful events;
- leases/claims if the execution engine does not own them;
- idempotency keys;
- retry state;
- calendar items generated by the system;
- user/operator attention items.

If a third-party workflow engine owns low-level execution state, Empirium may store an authoritative product projection plus external engine IDs, but there must be one clearly documented canonical writer for each lifecycle.

---

## S1.3 — Event log

**Decision:** Yes to an append-only event history, but SQLite should also hold structured event records or a queryable event projection.

JSONL can be a useful secondary audit stream, not the only event store.

Add these event classes:
- workflow activated/paused/version changed;
- schedule occurrence created;
- schedule fired/missed/coalesced/skipped;
- run queued/started/ended;
- step ready/assigned/started/ended;
- attempt started/ended;
- retry scheduled;
- provider/model selected;
- provider rate-limited;
- MCP/tool call started/result/failed;
- handoff created/consumed;
- artifact created;
- review requested/verdict;
- approval requested/granted/rejected/expired;
- memory proposed/written/edited/expired;
- notification created/sent/failed;
- config changed;
- permission denied;
- employee state changed;
- integration connection changed;
- report generated;
- learning proposal created/activated/rolled back;
- recovery/restart events;
- idle reason.

Keep low-level token streaming out of the semantic event log.

---

## S1.4 — Employee memory

**Decision:** Use product-owned persistent memory storage, with SQLite for canonical metadata and compact text/structured memories.

Do not bind employee identity to Hermes profile memory as the only source of truth.

Hermes memory can be an adapter/source if useful.

P0 UI should support at minimum:
- view memory;
- provenance/source;
- mark obsolete;
- edit/correct;
- delete/archive where allowed.

Export can be P1/core-later, but the storage format should remain inspectable.

---

## S1.5 — Artifacts

**Decision:** Use hybrid storage.

- Small structured/text artifacts: database body acceptable.
- Large/binary artifacts: files/object storage with DB metadata/reference.
- Every artifact gets stable ID, provenance, content type, creator run, timestamps, hash where useful.

Retention:
- do **not** silently hard-delete after 500 rows.
- P0 may retain all because scale is tiny.
- build a later configurable retention/archive policy.

Artifact viewer in P0: yes, for text/JSON/links/basic files.

---

## S1.6 — Settings

**Decision:** App settings and behaviorally important preferences should be in authoritative persistence, not only localStorage.

LocalStorage may be used only for non-authoritative browser convenience such as:
- panel collapse state;
- transient UI preference;
- last selected tab.

---

## S1.7 — Secrets

**Decision:** Prefer a dedicated secret boundary rather than raw secrets in SQLite.

Order of preference:
1. reuse an existing Hermes/host secret store if secure, stable and independently addressable;
2. otherwise root-owned/env/systemd environment file with strict permissions for M0;
3. later add encrypted-at-rest credential storage if the product must manage multiple user-entered credentials.

The UI should never read back plaintext secrets.

Model/integration settings should show:
- configured/not configured;
- last validated;
- provider identity;
- scope;
- update/replace action.

No secrets in logs, prompts, artifacts or memory.

---

## S1.8 — Backups

**Decision:** Automatic local backups are **M0/core**, not a distant P1.

At minimum:
- nightly SQLite snapshot;
- before schema migration;
- before destructive admin operation;
- configurable retention.

External/offsite sync such as Google Drive can come later.

The backup process itself should be observable.

---

## S1.9 — Migration story

**Decision:** Confirm.

Versioned schema/migration system from day one.

Each migration should have:
- ID/version;
- timestamp;
- forward migration;
- rollback/recovery plan where feasible;
- backup precondition for destructive change.

---

## S1.10 — Deterministic fixtures

**Decision:** Confirm.

Committed deterministic fixtures may include:
- organization;
- department;
- employees;
- workflow definitions;
- run histories;
- failure states.

They must be:
- clearly test-only;
- never automatically imported into production;
- safe to reset.

---

# S2 — REPO, TOOLCHAIN, REUSE

## S2.1 — Target repo

**Decision:** Prefer a fresh, clean target fork/repo **if** inspection confirms the existing Empirium Studio tree contains significant failed-build baggage.

Recommended:
- preserve existing `empirium-studio` repository untouched as evidence/reference;
- create a new clean repository such as `empirium-studio-v2` or preferably simply a new clean `empirium-studio` after the old path is archived/read-only.

Do not decide path names blindly.

Stage 1 should inspect:
- current Git state;
- useful code;
- current Hermes version;
- what is salvageable.

No destructive cleanup of old evidence.

---

## S2.2 — Fork base

**Decision:** Check upstream/current local Hermes Studio state first.

Use the newest **compatible, stable, locally proven** base rather than blindly pinning v1.20.0 or blindly following upstream main.

Avoid moving-target development on an unverified latest commit.

Freeze a base SHA once selected.

---

## S2.3 — Old build salvage

**Decision:** Use the old `AI_WORKFORCE_BUILD/` documents/contracts/ADRs as input material, but never as unquestioned authority.

Process:
- ingest;
- map to current requirement IDs;
- classify still-valid / superseded / implementation-specific / obsolete;
- preserve provenance;
- reuse code/contracts only after validation.

Do not rebuild valuable work from scratch if it remains correct.

---

## S2.4 — Old repo disposition

**Decision:** Confirm.

Quarantine/preserve it.

No deletion.

It is:
- forensic evidence;
- source of reusable code;
- source of failed-pattern lessons.

---

## S2.5 — Hermes built-in reuse

**Decision:** The proposed default is too prescriptive.

Use this rule instead:

### Product domain
Empirium owns the durable product semantics.

### Hermes capabilities
Evaluate and reuse where they fit:
- **Profiles:** likely useful as execution profiles/backends. Use, but Profile ≠ Employee.
- **MCP:** strongly prefer reuse. MCP is core.
- **Cron/scheduling:** evaluate, do not automatically replace. If Hermes cron can satisfy durability, timezone, missed-run, occurrence identity and observability requirements, it may back schedules. If not, use a stronger scheduler.
- **Kanban:** may back some Task lifecycle, but Task ≠ Project/Workflow and one canonical authority must be chosen.
- **Conductor/Crews:** use only for bounded temporary execution/grouping where they add value. Do not use them as Department or permanent Employee identity.

Do not declare “product scheduler must be custom” before evaluating reuse.

---

## S2.6 — Third-party orchestrator evaluation

**Decision:** Include a deliberate reuse study.

Evaluate at least:
- the AWS CAO/orchestrator the user previously referenced;
- Hermes-native execution primitives;
- BullMQ;
- Agenda or node-cron only for simpler scheduling roles;
- n8n;
- Temporal;
- Hatchet;
- Inngest/Trigger.dev style durable workflow engines where self-host/open-source fit exists;
- Windmill/Kestra/Prefect-class systems if they fit resource and licensing constraints.

Do not turn this into an endless survey.

Score against:
- self-hostability;
- resource use;
- license;
- durable timers;
- retries;
- idempotency;
- human pause/resume;
- long-running workflows;
- observability;
- step metadata;
- worker/tool flexibility;
- ease of embedding;
- MCP compatibility;
- operational complexity.

Temporal may be too heavy for the current VPS, but exclude only after measuring fit.

---

## S2.7 — Git

**Decision:**
- frequent small coherent commits;
- stable task IDs in commit messages where practical;
- local repo plus private GitHub remote if the existing project already uses GitHub securely.

Do not create a new public remote.

Use a neutral build identity such as:
`Empirium Build <build@local>`

The exact identity is not important; traceability is.

---

## S2.8 — Toolchain pins

**Decision:** Confirm reuse-first.

Do not churn:
- Node;
- package manager;
- ESLint;
- Prettier;
- Vitest;
- Playwright;
- TypeScript

without a measured reason.

Pin versions after base audit.

---

## S2.9 — Monorepo vs single package

**Decision:** Start with the existing Hermes Studio structure.

Do not create a monorepo/workspace split merely for architecture aesthetics.

Create packages/modules only when boundaries become materially useful, for example:
- office renderer;
- workflow engine adapter;
- shared domain contracts.

Avoid premature package fragmentation.

---

## S2.10 — Test runtime on VPS

**Decision:** Headless Playwright on the VPS is acceptable.

But:
- benchmark RAM/CPU;
- limit concurrency;
- run visual captures at deterministic viewport sizes;
- do not compete with many simultaneous build workers.

Acceptance should include:
- DOM/state assertions;
- screenshots;
- browser console;
- real interaction.

A display server should not be required.

---

# S3 — REQUIREMENT LEDGER & SCOPE

## S3.1 — Ledger base

**Decision:** AC-001–060 is **one input**, not the complete base.

The authoritative ledger must be generated from all product sources.

Each source item should map to one or more atomic requirements.

The ledger needs:
- stable ID;
- source;
- source priority;
- capability;
- mandatory/deferred/optional status;
- milestone;
- dependency;
- acceptance predicate;
- evidence;
- current state.

No substantive source paragraph should remain unmapped.

---

## S3.2 — Target size

**Decision:** Do not set an artificial ledger-size appetite.

For M0/Foundation, ~60–100 atomic requirements may be reasonable.

For the full product, expect **several hundred**.

Correct decomposition is more important than keeping the list short.

A large requirement ledger is acceptable if:
- it is machine-readable;
- grouped hierarchically;
- dependency-aware;
- not duplicated;
- each atomic item is testable.

---

## S3.3 — IDs & mapping

**Decision:** Keep AC-001–060 as stable acceptance references.

Create requirement IDs such as:
- PROD-ORG-###
- PROD-EMP-###
- PROD-WF-###
- PROD-SCHED-###
- PROD-MEM-###
- PROD-MCP-###
- PROD-MODEL-###
- PROD-OFFICE-###
- PROD-REPORT-###
- PROD-SEC-###
- PROD-QA-###
- PROD-UI-###

Each requirement maps to:
- one or more sources;
- one or more acceptance criteria;
- one or more predicates.

Orphan count for mandatory requirements must be zero.

---

## S3.4 — Priority semantics

**Decision:** Reject “P1 = not required for SHIPPED” as the global product rule.

Use:

- **M0-REQUIRED** — required for foundation gate.
- **CORE-REQUIRED** — mandatory before the complete product can be called shipped.
- **EXTENDED** — deliberately optional future enhancement.

Risk is a separate field:
- LOW;
- MEDIUM;
- HIGH;
- CRITICAL.

A requirement can be CORE-REQUIRED and implemented after M0.

---

## S3.5 — Definition of Done source

**Decision:** Derive a canonical DoD from:
- the complete mandatory requirement ledger;
- AC-001–060;
- final product brief completion rules;
- original master-protocol release principles.

DoD is not one prose section.

It should be machine-checkable:
- all mandatory requirements in accepted state;
- all blocking predicates pass;
- no unresolved critical/high defects;
- required soak/recovery evidence complete;
- independent release review complete;
- release SHA fixed.

Owner approval should freeze the DoD before broad campaign execution.

---

## S3.6 — Failure contract

**Decision:** Confirm with one addition.

Every failing mandatory predicate must create:
- a defect/work item;
- failure classification;
- reproduction/evidence;
- responsible requirement;
- next action;
- retry/rework counter.

Failure does not terminate the campaign unless a pre-registered safety/budget condition is reached.

The system must diagnose repeated failure rather than endlessly retry.

---

## S3.7 — Requirement extraction standard

**Decision:** Confirm, and add these questions:

For each requirement:
1. Is this a capability rather than a restated sentence?
2. Can a fresh engineer understand success?
3. Is it atomic enough to verify?
4. Is it traceable to source?
5. Is its mandatory/deferred status explicit?
6. Does it preserve the full product intent?
7. Does it have a proof method?
8. Would passing it still allow an obvious fake implementation?

If #8 is yes, strengthen the predicate.

---

# S4 — ACCEPTANCE PREDICATES

## S4.1 — Predicate classes

**Decision:** The proposed classes are useful but not “exactly one class.”

A requirement may need multiple proofs.

Use proof dimensions:
- deterministic/static;
- unit;
- integration;
- UI runtime;
- unattended/recovery;
- visual;
- accessibility;
- security;
- performance;
- human/subjective review where unavoidable.

Significant behavior may require multiple proof types.

Do not force an office requirement to choose between “UI-runtime” and “visual” when it needs both.

---

## S4.2 — Boot acceptance

**Decision:** Canonical Home = **Organization Overview**.

From there the user enters departments.

Viewport set:
- 1280×800;
- 1366×768;
- 1672×941 if that is the supplied mockup frame;
- 1920×1080;
- representative tablet;
- narrow mobile for responsive checks later.

M0 boot predicate can use 1280×800 and 1672×941; final visual suite should be broader.

---

## S4.3 — Design tokens

**Decision:** Extract a token specification from the supplied mockups and final visual brief.

Store machine-readable design tokens:
- colors;
- background layers;
- borders;
- accent roles;
- typography scale;
- spacing;
- radius;
- shadows/glow;
- status colors;
- motion durations;
- office sizing conventions.

Owner approval is useful before visual freeze.

Do not use tokens as an excuse to flatten the design into a generic template.

---

## S4.4 — Existing test suite

**Decision:** Confirm.

Existing baseline suite must stay green unless:
- a test is proven obsolete/incorrect;
- its replacement is explicitly documented.

Baseline failures discovered before implementation must be recorded separately.

---

## S4.5 — Unattended predicates

**Decision:** Confirm the injected-clock harness for fast deterministic testing.

Additionally:
- perform at least one real-clock schedule test;
- perform one real browser-closed/background execution test;
- perform a multi-day soak.

Injected time is excellent for logic; it does not completely replace real scheduling evidence.

---

## S4.6 — Office truthfulness

**Decision:** DOM/state assertions are necessary but not sufficient.

For each canonical state verify:
1. backend semantic state;
2. API/state adapter output;
3. textual employee dossier;
4. office status label/badge;
5. animation/state class or renderer state;
6. visual evidence for representative states.

The animation may contain decorative motion, but its semantic class must match real state.

Idle ambient behavior is allowed; fake productive behavior is not.

---

## S4.7 — Performance gates

**Decision:** Do not remove all performance criteria.

For M0:
- boot/service ready <30s is acceptable as a coarse gate;
- UI interaction should not visibly stall;
- schedule fire drift should be measured.

For final product preserve the stronger targets from the product protocol:
- warm navigation target around <=2s p95 where realistic;
- local UI feedback around <=200ms p95;
- local read APIs around <=300ms p95 where meaningful;
- main office aiming ~55–60fps on documented test hardware;
- memory-leak investigation on repeated mounts/navigation.

Do not make these brittle if the environment makes a specific number meaningless; measure and document.

---

## S4.8 — Flake policy

**Decision:** Confirm with classification.

- Logic failure: zero blind retry.
- Known transport/network transient: at most one automatic retry.
- Flaky test: defect in test/product until root cause established.
- Do not rerun until green and call it success.

Every retry remains visible in evidence.

---

## S4.9 — Failure creates work

**Decision:** Confirm.

The failure-generated work item should include:
- failing predicate ID;
- requirement IDs;
- exact SHA;
- observed result;
- expected result;
- reproduction command;
- evidence paths;
- likely failure class;
- permitted file scope;
- completion proof.

Spot-checking a sample of 10 during Stage-0 is appropriate, but the controller should schema-validate all automatically.

---

# S5 — ACCEPTANCE HARNESS

## S5.1 — Harness layout

**Decision:** `verify.sh` plus modular `checks/` is acceptable.

The controller must run verification against the exact integrated SHA.

Do not automatically revert every failing integration blindly.

Instead:
- mark integration rejected;
- preserve the SHA/branch/evidence;
- revert or repair according to task policy.

Evidence preservation is more important than keeping the branch artificially green.

---

## S5.2 — Hash protection

**Decision:** Confirm.

Workers must not be able to silently modify acceptance criteria to pass.

Protected:
- requirement ledger;
- predicate definitions;
- harness core;
- release gate;
- test fixtures used as independent acceptance truth.

Changes require dedicated harness-change workflow/review.

---

## S5.3 — Calibration fixtures

**Decision:** Strongly confirm.

Use known-bad cases including:
- missed schedule falsely marked success;
- duplicate schedule occurrence;
- office state lies;
- unauthorized MCP access;
- approval bypass;
- memory leakage between employees;
- retry causes duplicate side effect;
- workflow completion despite failed mandatory step.

The harness must prove it catches bad behavior.

---

## S5.4 — Independent harness review

**Decision:** Confirm.

Use a fresh strong reviewer, ideally a different model family from the harness implementer.

Opus via subscription is appropriate where available.

The reviewer must:
- inspect false-negative risk;
- inspect weak assertions;
- inspect fixture validity;
- challenge bypass paths.

---

## S5.5 — Time budget

**Decision:** <10 minutes for the routine post-integration harness is a good target.

Longer suites should be tiered:
- fast verify;
- integration;
- visual;
- security;
- soak/recovery.

Do not force the 3-day soak into `verify.sh`.

---

## S5.6 — Release gate

**Decision:** For **M0 gate**, require:
- all M0 predicates pass;
- representative real background run passes;
- short soak passes;
- independent review passes.

For **final product release**, require:
- all CORE-REQUIRED predicates pass;
- full required resilience/soak suite passes;
- independent full release review;
- visual release gate;
- security gate;
- final exact SHA.

No LLM may mark the product globally shipped by prose alone.

---

# S6 — EXECUTION GOVERNANCE

## S6.1 — Build controller

**Decision:** Reuse the repaired Nailify controller **as a proven starting point**, not as unquestioned product-specific truth.

Before adapting:
- isolate generic controller behavior;
- remove Nailify-specific requirement semantics;
- verify current acceptance semantics;
- add only failure classes actually needed.

Do not build another large orchestrator from scratch unless the current controller fundamentally cannot meet requirements.

---

## S6.2 — Build state store

**Decision:** In-repo `.hermes/autonomy/project.db` is acceptable for **build-campaign state**.

This is separate from product runtime state.

Keep this distinction explicit.

---

## S6.3 — Build event log

**Decision:** Confirm.

Log:
- tick;
- queue state;
- claim;
- dispatch;
- worker start/end;
- result classification;
- verification;
- rework;
- idle reason;
- provider state;
- human intervention;
- controller restart.

“Why is the controller idle?” must be answerable deterministically.

---

## S6.4 — Worker packet fields

**Decision:** Confirm proposed fields and add:
- task ID;
- run/attempt ID;
- base SHA;
- worktree/branch;
- source requirement text;
- dependencies;
- known architecture contracts;
- allowed data/secrets class;
- model/tool policy;
- relevant prior review defects;
- expected structured handoff schema;
- explicit out-of-scope list;
- escalation behavior;
- no-self-approval clause.

Packets should be bounded and minimal-complete.

---

## S6.5 — Worker runtime

**Decision:** Use fresh bounded Hermes sessions under dedicated build profiles.

Do not expose:
- this chat’s broad personal context;
- unrelated skills;
- unrelated projects;
- unnecessary secrets.

Each worker receives only task-relevant context.

---

## S6.6 — Provider/model freeze

**Decision:** Use a verified free implementation pool with **effective-model attribution mandatory**.

Prefer pinned model for:
- benchmark reproducibility;
- high-risk comparisons.

Allow `auto`/pool for:
- routine implementation after benchmark;
- only if effective model/provider is recorded.

Reviewer:
- Opus/Sonnet subscription depending risk.

Do not let strong subscription reviewers silently become primary implementers.

---

## S6.7 — Paid ceiling

**Decision:** Build-time new pay-as-you-go AI spend ceiling remains **$0** unless the owner explicitly changes it later.

Existing subscriptions are allowed.

No automatic paid fallback.

---

## S6.8 — Attempt schema

**Decision:** Proposed fields are good. Add:
- base_sha;
- result_sha;
- worker/profile ID;
- task class;
- failure_class;
- files_changed;
- tests_run;
- review_verdict;
- retry_of_attempt;
- artifact/evidence paths;
- provider response/error code;
- quota/rate-limit marker;
- human intervention reason.

Add statuses:
- ACCEPTED;
- REVIEW_REJECTED;
- WAITING_PROVIDER;
- CANCELLED;
- POLICY_BLOCKED.

Keep implementation result and acceptance result separate where possible.

---

## S6.9 — Human-intervention counter

**Decision:** Confirm, but do not treat every owner review/sign-off as a failure.

Classify:
- required governance approval;
- product decision;
- rescue/intervention;
- manual technical repair;
- informational review.

Campaign KPI should focus on avoidable rescue interventions, not penalize legitimate product decisions.

---

## S6.10 — Stop rules

**Decision:** Amend.

### Rule 1
Keep: no concurrency growth until single-worker baseline is proven.

Threshold:
- at least 20 representative valid attempts;
- ≥60% accepted first-pass or equivalent clear evidence.

### Rule 2
Do not create recursive supervisor/director hierarchies.

A single durable planner/controller is preferred.

However, bounded temporary planning/review sessions are allowed.

The product’s “Director” employee is unrelated to the build campaign.

### Rule 3
Confirm:
do not build recovery machinery for failure classes not observed or clearly unavoidable by architecture.

### Rule 4
Amend:
model/provider switching can also occur when a provider is objectively unavailable/rate-limited, not only after ten failures.

But it must follow pre-approved routing policy and be recorded.

---

## S6.11 — Campaign budget ceiling

**Decision:** Use **200 valid attempts / 14 calendar days / 2 structured re-baselining rounds** for the first autonomous build campaign.

At that threshold:
- stop autonomous dispatch;
- produce a diagnostic report;
- preserve state;
- request owner decision.

This is **not** permission to call the product failed or finished.

It is a campaign-control boundary to avoid infinite burn.

---

## S6.12 — Watchdog

**Decision:** Confirm.

Systemd watchdog/controller:
- restart dead controller;
- enforce one instance;
- log;
- respect pause;
- no LLM reasoning;
- no spawning recursive supervisors.

Linger/start-on-boot must be proven.

---

## S6.13 — Reporting cadence

**Decision:**
- immediate alert only for genuine owner blocker, policy violation or campaign stop condition;
- daily summary;
- phase-gate checkpoint.

Daily summary should contain:
- requirements accepted that day;
- tasks attempted;
- first-pass acceptance;
- retries/rework;
- open tasks;
- blocking failures;
- provider health;
- controller idle time + reasons;
- human rescue interventions;
- current Git SHA;
- next planned dependency frontier;
- build spend classification.

Do not spam the owner for normal failures.

---

## S6.14 — Artifact locations

**Decision:** Build-campaign artifacts can live under `.hermes/` if:
- structured;
- documented;
- excluded from product runtime state;
- not containing secrets.

Suggested:
- `.hermes/autonomy/`
- `.hermes/packets/`
- `.hermes/checkpoints/`
- `.hermes/reviews/`
- `.hermes/evidence/`
- `.hermes/benchmarks/`

Large generated artifacts may live outside Git with indexed paths.

---

## S6.15 — Kill criteria

**Decision:** Amend wording from “campaign ends” to “autonomous campaign pauses for owner review.”

Trigger pause on:
a. 200 valid attempts / campaign budget exhausted without meaningful gate progress;
b. acceptance <30% after two packet/decomposition redesign rounds;
c. owner materially changes product definition;
d. soak fails 3 consecutive times for the same unresolved cause;
e. security/policy violation;
f. evidence suggests controller is creating duplicate work or losing state;
g. unexpected paid AI spend.

Do not continue blindly.

---

## S6.16 — Provider outage

**Decision:** Free implementation provider pool unavailable >4h:
- pause affected AI implementation dispatch;
- continue deterministic tests/reconciliation that do not need the provider;
- notify in daily/exception channel;
- do not auto-fallback to paid route.

If another already-approved verified-free route exists, it may be used according to routing policy.

---

# S7 — PRE-REGISTERED BENCHMARK

## S7.1 — Benchmark task

**Decision:** Use the **free-games monitor end-to-end** as the primary benchmark vertical slice.

It is the best first slice because it tests:
- external information retrieval;
- schedule;
- workflow run;
- employee assignment;
- model/tool route;
- artifact;
- dedup;
- notification;
- persistence;
- reporting.

However the 20 attempts should not hit live stores identically each time.

Use:
- deterministic fixture/source adapter for repeatability;
- one or more real integration runs separately.

---

## S7.2 — Count

**Decision:** 20 valid attempts initial benchmark.

Hard ceiling 40 before mandatory diagnosis.

Provider aborts that never started meaningful work can be excluded from quality denominator but must remain reported separately.

---

## S7.3 — Decision rules

**Decision:** Confirm thresholds as build-system rules:

- ≥60% accepted → allow controlled concurrency growth.
- 30–59% → improve packet/task decomposition; no added orchestration layer.
- <30% → stop scaling; redesign task shape/context; diagnose.

Do not respond to poor quality by adding more supervisors.

---

## S7.4 — Measurement fields

**Decision:** Confirm and add:
- first-pass acceptance;
- final acceptance after rework;
- failure class;
- diff size;
- tests executed;
- token use if known;
- provider latency;
- reviewer verdict;
- collateral-edit rate;
- task complexity class.

Flat JSONL plus summarized report.

---

## S7.5 — Freeze before attempt 1

**Decision:** Confirm.

Freeze:
- task;
- acceptance predicate;
- fixture;
- packet format;
- selected route/policy.

Harness bug fixes are allowed only with:
- dedicated issue;
- independent review;
- rerun of affected attempts if comparability changed.

---

## S7.6 — Session hygiene

**Decision:** Confirm.

Fresh worker session per attempt.

Worker self-report is evidence input, never the acceptance authority.

The exact integrated code + harness decides.

---

# S8 — CAMPAIGN PHASES, SOAK, POST-FOUNDATION

## S8.1 — Phase gates

**Decision:** Amend order slightly.

Recommended:

### Phase F0 — Source reconciliation / architecture freeze
- complete ledger;
- reuse matrix;
- domain contracts;
- engine decision;
- acceptance harness.

### Phase F1 — Durable domain + persistence
- organization;
- department;
- employee;
- workflow definitions;
- schedules;
- runs;
- memory skeleton;
- permissions skeleton.

### Phase F2 — Scheduler + workflow engine
- durable occurrences;
- task/attempt lifecycle;
- retries;
- handoffs;
- approvals;
- events.

### Phase F3 — First real recurring workflow
- free-games monitor;
- notification;
- reporting;
- real unattended execution.

### Phase F4 — Model/MCP/Memory proof
- two model routes;
- scoped MCP/tool permission;
- persistent employee memory retrieval.

### Phase F5 — Living office + organization/department UI
- truthful state adapter;
- employee dossier;
- calendar;
- activity;
- reports.

### Phase F6 — QA/review + project workflow
- implementation handoff;
- independent QA;
- human approval distinction.

### Phase F7 — Resilience / soak / foundation gate
- recovery;
- browser closed;
- restart;
- provider failure;
- 3-day soak;
- independent review.

Then continue into the remaining CORE-REQUIRED product capabilities.

No owner sign-off should be needed after every tiny phase unless a real product/architecture decision is pending. The goal is autonomy, not repeated permission prompts.

---

## S8.2 — Soak definition

**Decision:** 72 consecutive hours is acceptable for M0/Foundation.

During soak:
- normal user viewing is allowed;
- no AI coding workers may patch the product;
- deterministic runtime processes continue;
- free-games workflow runs on real schedule;
- state survives;
- errors are recorded;
- no manual DB state patches.

For final release, perform broader resilience tests beyond this one routine.

---

## S8.3 — Games monitor specifics

### Stores
M0:
- Steam;
- Epic Games Store.

Later adapters:
- GOG;
- Amazon Prime Gaming;
- others.

### Data source
Preference order:
1. official/public documented source/API/feed;
2. stable first-party web endpoint;
3. browser/scraping fallback.

Do not depend on brittle scraping if a reliable official source exists.

### Frequency
**Daily**, not hourly, for real production use.

Default time:
**09:00 Europe/London**.

Reason:
free-game promotions do not justify 24 hourly checks/day, and unnecessary runs waste resources.

For soak testing, a test schedule may run more frequently using a dedicated test workflow/clock.

### Dedup
Do not use a blind “30 days” rule only.

Deduplicate primarily by:
- store;
- canonical item ID;
- promotion/free-window identity.

Alert again only if:
- a genuinely new free promotion occurs;
- the prior promotion ended and a new one starts;
- the source meaningfully changes.

### History
Keep all run history initially.

Do not silently delete alerts at M0.

### Alert payload
Include:
- game/item name;
- store;
- normal/current price if available;
- current free price;
- source URL;
- promotion start;
- promotion end / claim-by deadline;
- time checked;
- confidence/source notes if data is uncertain.

---

## S8.4 — Soak failure handling

**Decision:** Confirm.

Failure:
- creates defect;
- preserves evidence;
- repairs via normal workflow;
- restarts soak window relevant to the repaired subsystem.

No manual DB patching to manufacture a pass.

---

## S8.5 — Next-stage ordering

**Decision:** The proposed order should change because MCPs and learning are more central than voice/finance.

After M0 Foundation:

1. full workflow builder and reusable workflow templates;
2. full MCP/integration registry + per-employee permissions;
3. richer employee memory + controlled learning loop;
4. second real department + cross-department workflows;
5. richer model routing and performance learning;
6. voice receptionist/realtime-worker capability;
7. external calendar/email/notification integrations;
8. finance templates/module;
9. multi-user/multi-tenant if desired.

The exact order may move based on dependency analysis.

Telephony provider is **not precommitted to Twilio**. Evaluate current providers, cost, latency and existing stack before choosing.

---

## S8.6 — Approvals UX at M0

**Decision:** The defaults proposed are too approval-heavy and would undermine autonomy.

### (a) Publishing a free-games alert artifact
**No approval after workflow activation.**

The user explicitly wants the bot to monitor and bring findings to attention automatically.

### (b) Project workflow past a handoff point
Approval only if that specific step is configured as approval-required.

A normal bot-to-bot handoff should not require the owner.

### (c) Approving a review verdict
No owner approval required for routine QA verdict.

QA can accept/reject according to criteria.

Human authorization is separate.

### (d) First-time scheduled execution
Use a workflow activation/test flow:
- user explicitly activates workflow;
- once activated, recurring executions run autonomously.

Do not request approval every first occurrence after restart/version.

Require human approval only for high-impact actions:
- destructive production action;
- external spending;
- irreversible data change;
- public deployment/publishing if configured;
- security/firewall/DNS;
- financial transfer;
- other user-defined risky actions.

---

## S8.7 — Design fidelity

**Decision:** For M0:
- strong structural fidelity;
- correct information hierarchy;
- coherent dark/cyan visual system;
- high-quality Personal Software office;
- correct states;
- no obviously generic/unfinished screens.

Do not require literal pixel identity to concept art if it harms responsiveness or operational clarity.

For final core release:
- premium polish across all core screens;
- no unresolved critical/high visual defects;
- mockups remain quality/direction references.

---

## S8.8 — Office character assets

**Decision:** Reuse the supplied character/reference assets first.

The original source package reportedly includes:
- character designs;
- proportion sheets;
- state references;
- movement keyframes;
- office environments.

Inventory those before creating replacement SVGs.

If production-ready assets are missing:
- create deterministic original 2D assets;
- use shared rig/state system;
- do not make character production a blocker for workflow semantics.

Do not assume simple six-state SVGs are the final aesthetic if better supplied material exists.

---

## S8.9 — Audio

**Decision:** No general UI audio subsystem required at M0.

Voice/receptionist audio is a later runtime capability and should be architected separately.

Do not import unrelated personal-OS audio requirements.

---

## S8.10 — Post-ship operation

**Decision:** Initial deployment is a personal/private operational system.

No formal external commercial SLO at M0.

However:
- persistent jobs should be expected to recover automatically;
- failures should be visible;
- backups and restart behavior should be reliable.

If later offered commercially, define SLOs then.

---

## S8.11 — Product runtime model costs

**Decision:** Product runtime must support configurable provider routes.

M0:
- one or more preconfigured route adapters;
- at least two usable routes if possible to prove model diversity;
- no API keys in repository;
- settings UI shows configured status;
- employee/step model policy is editable.

FreeLLMAPI may be a default route where fit is good.

But the product must not be architecturally tied to FreeLLMAPI.

The user can later add OpenRouter, direct providers, research providers such as Perplexity, local models, etc.

Runtime product costs are a product policy, distinct from the $0 build-campaign policy.

---

## S8.12 — Calendar

**Decision:** M0 includes an **in-app schedule/calendar view**.

External Google/Outlook calendar synchronization can be later.

The in-app calendar is mandatory because planning bot work over time is central to the product.

---

# S9 — PROCESS & META

## S9.1 — Answer batch

**Decision:** This document answers **all S0–S9 questions now**.

Do not wait for another owner questionnaire unless a truly unresolved product choice emerges from the live environment.

Hermes should now produce the Stage-0 pack.

---

## S9.2 — “All defaults” mechanic

**Decision:** This answer set supersedes the need for “S# all defaults.”

Where this document explicitly confirms a default, it is approved.

Where it amends a default, the amendment wins.

Any future changed owner decision becomes:
- a versioned Decision Register entry;
- with date;
- reason;
- affected requirements.

Do not silently rewrite historical decisions.

---

## S9.3 — Stage-0 pack review

**Decision:** Confirm with one addition.

Stage-0 pack should include:

1. Decision Register;
2. source inventory;
3. source conflict register;
4. reuse/build matrix;
5. orchestrator/workflow-engine evaluation;
6. current-repo audit;
7. canonical domain model;
8. full requirement ledger v1;
9. milestone grouping;
10. dependency graph;
11. predicate drafts;
12. acceptance harness design;
13. calibration fixture plan;
14. build governance files;
15. provider/model benchmark plan;
16. product architecture diagrams/contracts;
17. risk register;
18. explicit list of still-unanswered decisions, ideally empty.

Then run the representative benchmark.

---

## S9.4 — Start trigger

**Decision:** The first **large autonomous campaign** should begin only after:
- Stage-0 pack exists;
- benchmark exists;
- no critical unresolved source conflict remains;
- controller/harness are proven.

However, the user should not need to manually say “continue” at every subsequent stage.

One explicit launch approval for the autonomous campaign is sufficient unless:
- product definition materially changes;
- destructive action requires approval;
- campaign stop condition fires.

---

## S9.5 — This chat’s role / review time

**Decision:** Do not design the system around a fixed weekly owner-review quota.

Assume owner attention is scarce.

The system should:
- batch non-urgent decisions;
- produce concise phase summaries;
- interrupt only for genuine blockers/risk;
- continue routine work autonomously.

For planning purposes, design as if the user may inspect the project only **once per day or less** during an autonomous campaign.

The acceptance machinery must not require constant human presence.

---

# FINAL LOCKED PRINCIPLES FOR HERMES

The following principles supersede any narrower default in the questionnaire:

1. **Do not call M0/P0 the finished product.**
2. **AC-001–060 is not exhaustive.**
3. **The complete requirement ledger must be extracted from all authoritative sources.**
4. **Specialized persistent employees are a core product concept.**
5. **Recurring and event-driven workflows are as important as one-off projects.**
6. **Scheduling/calendar is first-class.**
7. **Durable bot-to-bot handoffs are first-class.**
8. **Each employee needs durable, scoped memory.**
9. **Different employees/jobs must be able to use different LLMs.**
10. **MCP/tool access is per employee and least-privilege.**
11. **The user should not babysit routine execution.**
12. **The browser may close while work continues.**
13. **The living office must reflect real operational state.**
14. **Reporting must make all meaningful work understandable after the fact.**
15. **QA and human approval are different concepts.**
16. **Open-source/existing infrastructure should be reused before generic custom plumbing is built.**
17. **One deterministic control plane owns build execution state; avoid recursive supervisor trees.**
18. **Workers are disposable; durable state is not.**
19. **Evidence, not worker self-report, determines acceptance.**
20. **No fake production metrics or synthetic operational state.**
21. **No automatic paid AI fallback during the build campaign.**
22. **Final product release requires the complete mandatory product ledger, not only the first vertical slice.**

---

# EXPECTED NEXT ACTION FROM HERMES

Hermes should not ask another broad generic questionnaire.

It should now:

1. ingest this answer set;
2. reconcile it with the original product sources;
3. audit the actual machine/repositories;
4. produce the Stage-0 pack;
5. identify only genuinely unresolved decisions that cannot be answered from existing evidence;
6. run the pre-registered representative benchmark after the Stage-0 pack is approved;
7. use benchmark evidence to size the autonomous build campaign;
8. proceed without routine owner interruption once the campaign is explicitly launched.

```

===== 2026-09-22 11:54 | session 20260922_105531_432d90 | AI staff force set up =====
@file:.hermes/attachments/EMPIRIUM_HERMES_S0-S9_OWNER_ANSWERS_2026-09-22-2.md

--- Attached Context ---

📄 @file:.hermes/attachments/EMPIRIUM_HERMES_S0-S9_OWNER_ANSWERS_2026-09-22-2.md (14512 tokens)
```markdown
# EMPIRIUM STUDIO / AI STAFF FORCE
# OWNER DECISION REGISTER — ANSWERS TO HERMES S0–S9 AUTONOMY QUESTIONS

**Date:** 2026-09-22  
**Status:** Owner-intent answer set for Stage-0 planning.  
**Purpose:** Remove ambiguity before Hermes is allowed to plan or execute autonomously.

---

# 0. Read this before interpreting any individual answer

There are several important corrections to the framing of the question set.

## A. P0 is NOT the finished product

The most important correction is that **P0 must not be treated as “SHIPPED” for the whole product**.

The product has repeatedly suffered from scope collapse: a large intended system becomes a small vertical slice, the small slice passes tests, and an orchestrator then describes the overall product as finished.

That is not acceptable here.

For this project:

- **P0 / M0 = Foundation + first representative end-to-end operating slice.**
- It proves the architecture can support the real product.
- It is allowed to be narrower than the full product.
- Passing P0 means “the foundation is proven,” not “Empirium Studio is shipped.”
- The final release gate must remain tied to the complete mandatory requirement ledger derived from all authoritative product sources.

If Hermes wants a three-tier system, use:
- **M0 / Foundation** — first integrated proof.
- **M1 / Core Product** — all central product capabilities implemented.
- **M2 / Extended Product** — explicitly non-core future enhancements.

Do not use “P1 = not required for SHIPPED” for capabilities that are clearly mandatory in the product charter.

## B. AC-001–060 is a base, not the exhaustive requirement ledger

AC-001–060 is useful as a behavioral spine, but it is **not exhaustive enough to represent the complete product**.

The full ledger must also be extracted from:
- the original two-part Empirium Studio master protocol;
- the consolidated final product brief;
- supplied mockups;
- later conversation clarifications;
- relevant AI Staff Force project decisions;
- explicit workflow, memory, MCP, model-routing, scheduling, calendar, reporting, voice/receptionist and observability requirements.

Do not cap the ledger at 60–90 requirements merely because AC-001–060 has 60 entries.

The full product will almost certainly compile to **hundreds of atomic requirements** once UI states, workflow behavior, security, failure recovery, permissions, model routing, memory, observability, accessibility and acceptance predicates are decomposed properly.

## C. Reuse-first is a hard engineering preference

Before custom-building generic orchestration, scheduling, retries, queues, MCP plumbing, long-running workflow state, or worker lifecycle mechanisms:

1. inspect Hermes;
2. inspect already-installed infrastructure;
3. evaluate mature open-source components;
4. evaluate the AWS CAO/orchestration system previously discussed by the user, if locally/relevantly available;
5. compare candidates to the exact Empirium contract;
6. integrate or wrap the best-fitting existing substrate.

Empirium should own the product semantics, not necessarily every low-level runtime mechanism.

## D. Product employees and build workers are different things

The workers that build Empirium are disposable engineering workers.

The employees inside Empirium are permanent product entities.

Do not confuse them.

---

# S0 — PRODUCT CHARTER & SCOPE FREEZE

## S0.1 — Canonical name

**Decision:** Use **“Empirium Studio”** as the canonical product/UI name for this build. The descriptive subtitle may be **“AI Workforce”** or **“AI Staff Force”** in documentation and onboarding.

Use:
- Product brand: **Empirium Studio**
- Product descriptor: **AI Workforce**
- Internal project aliases: AI Staff Force / AI Star Force are acceptable project-history terms only.

Do **not** merge this product into the existing personal “Empirium OS” application merely because older mockups show “EMPIRIUM OS.”

The branding should be configuration-driven so the product can later be renamed without changing the domain model.

---

## S0.2 — One-line definition

**Decision:** Replace the proposed line with the following canonical definition:

> **Empirium Studio is a persistent AI workforce operations platform in which specialized digital employees, each with configurable models, MCP/tool access, memory, permissions and job rules, execute recurring, scheduled, event-driven and project-based work through durable workflows and handoffs, while the user plans, observes, approves, audits and improves that work through a truthful living-office control interface.**

This sentence is a better decomposition anchor because it captures:
- persistent employees;
- specialization;
- multiple LLMs;
- MCPs/tools;
- memory;
- permissions;
- workflows;
- schedules;
- event-driven work;
- projects;
- handoffs;
- human control;
- reporting/observability;
- living office.

Do not shorten it in a way that loses those concepts.

---

## S0.3 — P0 “shipped” slice

**Decision:** I do **not** accept P0 as the whole product’s SHIPPED slice. Treat it as **M0 Foundation / Representative Vertical Slice**.

For M0, the proposed items are approved with the following additions and amendments:

### M0.1 Durable domain
Required.

The minimum durable domain should include:
- Organization;
- Department;
- Employee;
- Execution Profile;
- Workflow Definition;
- Schedule;
- Workflow Run;
- Task/Step;
- Attempt/Run;
- Artifact;
- Handoff;
- Review;
- Approval;
- Notification;
- Memory;
- Knowledge reference;
- Event;
- Report.

SQLite may be the first authority if the architecture remains migration-friendly.

### M0.2 Durable scheduler
Required.

Must:
- operate with browser closed;
- persist schedules;
- create unique occurrence identities;
- support missed-run policy;
- prevent duplicate occurrences;
- support timezone-aware scheduling;
- survive process restart.

### M0.3 Seed department
Required.

Use **Personal Software** as the canonical first fully exercised department because it already has the strongest product definition.

Seed **5 permanent employees**:
1. Director;
2. Research Architect;
3. Developer / Implementation Engineer;
4. QA Engineer;
5. Learning Analyst.

The office may visibly show 3–5 at a time if layout requires, but all five must exist as real persistent employees.

### M0.4 Recurring real workflow
Required.

Use the **Steam + Epic free-games monitor** as the first real unattended recurring workflow because:
- it is real;
- it is low risk;
- it exercises scheduling;
- it exercises external data acquisition;
- it exercises deduplication;
- it exercises artifacts;
- it exercises notification;
- it gives immediate proof that background work is real.

### M0.5 Project/handoff workflow
Required.

Use one second workflow that proves:
- one employee performs work;
- structured handoff occurs;
- another employee continues;
- approval can pause only the dependent path;
- resumption is durable.

A small Personal Software change workflow is suitable.

### M0.6 Truthful living office
Required.

One fully animated/operational department is enough for M0.

The organization overview can use lightweight/static mini-office projections.

### M0.7 Reporting
Required.

Must answer:
- what ran today;
- what succeeded;
- what failed;
- what is waiting;
- what requires attention;
- what is scheduled next;
- which employee/model/tool acted.

### M0.8 Simple workflow creation without code
Required.

A form/template builder is sufficient for M0.

### M0.9 Model routing
The original proposed default is **too weak**.

M0 must prove that the architecture genuinely supports different models for different employees.

Therefore M0 should have:
- at least **two configurable model routes**;
- at least **two employees/steps using different routes**;
- per-employee model policy visible in UI;
- actual/effective route telemetry where available.

This does not mean two paid providers are required. Two verified usable routes are enough.

### M0.10 QA vs approval
Required.

Must prove:
- independent quality review is not the same thing as;
- human authorization to perform a consequential action.

### M0.11 Persistent employee memory
**Add to M0.**

At least one employee must:
- write an approved memory;
- terminate its session;
- later retrieve that memory;
- use it appropriately;
- retain provenance.

Memory is too central to defer entirely.

### M0.12 MCP/tool permission proof
**Add to M0.**

A full integration marketplace is not necessary, but M0 must prove:
- one employee has access to a real MCP/tool;
- another employee does not;
- unauthorized use is denied by policy/server-side enforcement;
- usage is auditable.

MCP capability is too central to leave completely unproven.

### M0.13 Calendar/schedule view
**Add to M0.**

A basic in-app schedule/calendar surface should show:
- next occurrences;
- recurring routine;
- recent occurrences;
- pause/run-now/edit recurrence.

### M0.14 Memory/reporting/office truth
The free-games run should become visible simultaneously in:
- workflow run history;
- activity;
- employee current/recent work;
- report;
- schedule history;
- office state while active.

This is an important integration proof.

---

## S0.4 — P0 exclusions register

**Decision:** Reclassify the exclusions carefully.

### Out of M0, but mandatory later in the core product
- full learning/improvement loop;
- full MCP registry and capability-management UI;
- cross-department workflows;
- voice/receptionist execution;
- richer workflow graph builder;
- richer calendar integration;
- multiple real departments;
- advanced model-routing optimization.

These are not “optional backlog.” They are deferred from the first foundation milestone only.

### Likely post-core / optional expansion
- full finance-specific module/templates;
- broad multi-tenant SaaS support;
- native mobile app.

### Important distinction
The underlying architecture must support:
- voice workers;
- cross-department handoffs;
- multiple integrations;
- model diversity

before final product release, even if every possible connector/template is not shipped.

---

## S0.5 — Office scope

**Decision:** For M0:
- one department gets the full animated living office;
- organization overview uses static or heavily throttled mini-office cards.

For the final product:
- every department can have a living-office representation;
- only the currently opened department should run the full scene;
- mini-offices should be snapshot/throttled representations for performance.

Do not run multiple full 60fps office simulations.

---

## S0.6 — Workflow builder depth

**Decision:** M0 uses:
- form-based creation;
- templates;
- read-only visual graph/timeline;
- explicit step configuration.

A full drag-and-drop graph editor is not required for M0.

However, **a true visual workflow builder is mandatory for the core product**, because the long-term experience is that users should be able to assemble and modify work cascades without editing source code.

The visual builder must eventually support:
- agent nodes;
- deterministic tool nodes;
- branches;
- delays;
- approvals;
- handoffs;
- joins;
- sub-workflows;
- MCP actions.

---

## S0.7 — Users

**Decision:** Single-user/operator at M0 and initial core deployment.

No secondary operator account is required for M0.

However:
- permissions must be designed as real policy concepts rather than hardcoded “because there is one user” assumptions;
- future multi-user support should not require rewriting the core employee/workflow model.

Multi-user is not a first milestone priority.

---

## S0.8 — Delivery form

**Decision:** Web application served on the VPS, consistent with Hermes Studio.

Desktop wrapper/Electron is deferred.

Reason:
- browser UI is appropriate for a persistent server-side workforce;
- background execution must not rely on desktop app lifetime;
- web access via secure private networking is simpler.

---

## S0.9 — Deployment & access

**Decision:** Initial deployment:
- standalone service on the VPS;
- private access only;
- bind locally and expose through the user’s existing secure private access method, preferably Tailscale or existing trusted proxy;
- no new public internet exposure by default.

Do not hardcode a port before inspecting current services and avoiding conflicts.

Port should be discovered/configured during Stage 1.

Primary machine is the current VPS/host where Hermes is already being operated.

Do not require GPU.

---

## S0.10 — First production workload

**Decision:** Yes, the Steam + Epic free-games monitor should run for real from the first live milestone.

**Primary notification channel for M0:** in-app notification/attention inbox.

Reason:
- it proves the Empirium notification system itself;
- it avoids making Telegram/email credentials a blocker;
- external notification adapters can then be added cleanly.

**Secondary preferred channel after core in-app proof:** Telegram.

Do **not** create external accounts/bots without explicit user action if provider setup requires account authorization.

The architecture should make notification channels pluggable.

---

## S0.11 — Seed content

**Decision:** Hermes may draft:
- Personal Software department content;
- the five employee personas;
- roles;
- responsibilities;
- routing descriptions;
- model/tool policies;
- starter workflows.

However:
- these become versioned configuration;
- they are not immutable product code;
- they should be reviewable/editable by the user.

Hermes does **not** need to stop for approval of every individual name before building the schema/UI.

Use high-quality provisional names and roles; owner approval can occur at the configuration-freeze checkpoint.

Role correctness is more important than character naming.

---

## S0.12 — Org structure mutability

**Decision:** Yes, P0/M0 should support runtime:
- create;
- rename;
- edit;
- disable/archive

for departments and employees.

Deletion should use **soft delete/archive with tombstones** by default.

Hard delete should be:
- separate;
- high-friction;
- approval-protected;
- only possible where retention/reference integrity is preserved.

No sub-team hierarchy is required initially.

---

## S0.13 — Timezone

**Decision:** Default timezone is **Europe/London**, but timezone is a real configurable field from day one.

Use:
- organization default timezone;
- workflow/schedule override where necessary;
- display in user/local timezone.

Do not make Europe/London an unchangeable global constant.

All stored timestamps should use an unambiguous canonical representation such as UTC plus explicit timezone metadata for recurrence.

DST behavior must be tested.

---

## S0.14 — No fake data

**Decision:** Confirm with one refinement.

Allowed:
- deterministic test fixtures;
- Storybook/dev/demo fixtures;
- clearly labeled synthetic acceptance data.

Not allowed in production:
- fake active employees;
- fake runs;
- fake spend;
- fake QA;
- fake “health”;
- fake progress;
- fake activity.

Seed configuration such as default employees and a default workflow is real configuration, not fake telemetry.

Production dashboards must derive from real stored state.

---

## S0.15 — Language / accessibility / analytics

**Decision:**
- English only initially.
- Architecture should not actively prevent future i18n.
- Accessibility target: **WCAG 2.1 AA where reasonably applicable** for the product UI.
- Full living-office animation must have textual equivalents.
- Reduced-motion support is required.
- No third-party product analytics/telemetry by default.
- First-party operational telemetry/logging is required because the product must report its own work.

---

# S1 — DATA & STATE ARCHITECTURE

## S1.1 — P0 database

**Decision:** SQLite is acceptable as the initial single authoritative operational database if current-scale testing confirms it is sufficient.

Use a runtime state directory outside the repository, e.g.:
`~/.local/state/empirium-studio/`

Do not store mutable production DB state in Git.

Use:
- WAL mode where appropriate;
- migrations;
- transactional writes;
- backups;
- foreign keys.

Design schema so a later move to Postgres is feasible.

Do not prematurely move to Postgres unless scale/concurrency requires it.

---

## S1.2 — Complete mutable-state list

**Decision:** The proposed list is incomplete.

SQLite/authoritative persistence should cover at least:

- organization;
- organization policies/settings;
- departments;
- employees;
- execution profiles;
- employee config versions;
- workflow definitions;
- workflow versions;
- workflow triggers;
- schedules;
- schedule occurrences;
- workflow runs;
- steps/tasks;
- attempts;
- artifacts metadata;
- handoffs;
- reviews;
- approvals;
- notifications;
- employee memory;
- knowledge metadata/index references;
- learning proposals;
- reports;
- tool/MCP registry;
- tool grants/permissions;
- model/provider registry;
- model-routing policy;
- provider health state;
- notification channels;
- secrets references (not raw secrets unless a vault design specifically allows it);
- app settings;
- audit/config change records;
- meaningful events;
- leases/claims if the execution engine does not own them;
- idempotency keys;
- retry state;
- calendar items generated by the system;
- user/operator attention items.

If a third-party workflow engine owns low-level execution state, Empirium may store an authoritative product projection plus external engine IDs, but there must be one clearly documented canonical writer for each lifecycle.

---

## S1.3 — Event log

**Decision:** Yes to an append-only event history, but SQLite should also hold structured event records or a queryable event projection.

JSONL can be a useful secondary audit stream, not the only event store.

Add these event classes:
- workflow activated/paused/version changed;
- schedule occurrence created;
- schedule fired/missed/coalesced/skipped;
- run queued/started/ended;
- step ready/assigned/started/ended;
- attempt started/ended;
- retry scheduled;
- provider/model selected;
- provider rate-limited;
- MCP/tool call started/result/failed;
- handoff created/consumed;
- artifact created;
- review requested/verdict;
- approval requested/granted/rejected/expired;
- memory proposed/written/edited/expired;
- notification created/sent/failed;
- config changed;
- permission denied;
- employee state changed;
- integration connection changed;
- report generated;
- learning proposal created/activated/rolled back;
- recovery/restart events;
- idle reason.

Keep low-level token streaming out of the semantic event log.

---

## S1.4 — Employee memory

**Decision:** Use product-owned persistent memory storage, with SQLite for canonical metadata and compact text/structured memories.

Do not bind employee identity to Hermes profile memory as the only source of truth.

Hermes memory can be an adapter/source if useful.

P0 UI should support at minimum:
- view memory;
- provenance/source;
- mark obsolete;
- edit/correct;
- delete/archive where allowed.

Export can be P1/core-later, but the storage format should remain inspectable.

---

## S1.5 — Artifacts

**Decision:** Use hybrid storage.

- Small structured/text artifacts: database body acceptable.
- Large/binary artifacts: files/object storage with DB metadata/reference.
- Every artifact gets stable ID, provenance, content type, creator run, timestamps, hash where useful.

Retention:
- do **not** silently hard-delete after 500 rows.
- P0 may retain all because scale is tiny.
- build a later configurable retention/archive policy.

Artifact viewer in P0: yes, for text/JSON/links/basic files.

---

## S1.6 — Settings

**Decision:** App settings and behaviorally important preferences should be in authoritative persistence, not only localStorage.

LocalStorage may be used only for non-authoritative browser convenience such as:
- panel collapse state;
- transient UI preference;
- last selected tab.

---

## S1.7 — Secrets

**Decision:** Prefer a dedicated secret boundary rather than raw secrets in SQLite.

Order of preference:
1. reuse an existing Hermes/host secret store if secure, stable and independently addressable;
2. otherwise root-owned/env/systemd environment file with strict permissions for M0;
3. later add encrypted-at-rest credential storage if the product must manage multiple user-entered credentials.

The UI should never read back plaintext secrets.

Model/integration settings should show:
- configured/not configured;
- last validated;
- provider identity;
- scope;
- update/replace action.

No secrets in logs, prompts, artifacts or memory.

---

## S1.8 — Backups

**Decision:** Automatic local backups are **M0/core**, not a distant P1.

At minimum:
- nightly SQLite snapshot;
- before schema migration;
- before destructive admin operation;
- configurable retention.

External/offsite sync such as Google Drive can come later.

The backup process itself should be observable.

---

## S1.9 — Migration story

**Decision:** Confirm.

Versioned schema/migration system from day one.

Each migration should have:
- ID/version;
- timestamp;
- forward migration;
- rollback/recovery plan where feasible;
- backup precondition for destructive change.

---

## S1.10 — Deterministic fixtures

**Decision:** Confirm.

Committed deterministic fixtures may include:
- organization;
- department;
- employees;
- workflow definitions;
- run histories;
- failure states.

They must be:
- clearly test-only;
- never automatically imported into production;
- safe to reset.

---

# S2 — REPO, TOOLCHAIN, REUSE

## S2.1 — Target repo

**Decision:** Prefer a fresh, clean target fork/repo **if** inspection confirms the existing Empirium Studio tree contains significant failed-build baggage.

Recommended:
- preserve existing `empirium-studio` repository untouched as evidence/reference;
- create a new clean repository such as `empirium-studio-v2` or preferably simply a new clean `empirium-studio` after the old path is archived/read-only.

Do not decide path names blindly.

Stage 1 should inspect:
- current Git state;
- useful code;
- current Hermes version;
- what is salvageable.

No destructive cleanup of old evidence.

---

## S2.2 — Fork base

**Decision:** Check upstream/current local Hermes Studio state first.

Use the newest **compatible, stable, locally proven** base rather than blindly pinning v1.20.0 or blindly following upstream main.

Avoid moving-target development on an unverified latest commit.

Freeze a base SHA once selected.

---

## S2.3 — Old build salvage

**Decision:** Use the old `AI_WORKFORCE_BUILD/` documents/contracts/ADRs as input material, but never as unquestioned authority.

Process:
- ingest;
- map to current requirement IDs;
- classify still-valid / superseded / implementation-specific / obsolete;
- preserve provenance;
- reuse code/contracts only after validation.

Do not rebuild valuable work from scratch if it remains correct.

---

## S2.4 — Old repo disposition

**Decision:** Confirm.

Quarantine/preserve it.

No deletion.

It is:
- forensic evidence;
- source of reusable code;
- source of failed-pattern lessons.

---

## S2.5 — Hermes built-in reuse

**Decision:** The proposed default is too prescriptive.

Use this rule instead:

### Product domain
Empirium owns the durable product semantics.

### Hermes capabilities
Evaluate and reuse where they fit:
- **Profiles:** likely useful as execution profiles/backends. Use, but Profile ≠ Employee.
- **MCP:** strongly prefer reuse. MCP is core.
- **Cron/scheduling:** evaluate, do not automatically replace. If Hermes cron can satisfy durability, timezone, missed-run, occurrence identity and observability requirements, it may back schedules. If not, use a stronger scheduler.
- **Kanban:** may back some Task lifecycle, but Task ≠ Project/Workflow and one canonical authority must be chosen.
- **Conductor/Crews:** use only for bounded temporary execution/grouping where they add value. Do not use them as Department or permanent Employee identity.

Do not declare “product scheduler must be custom” before evaluating reuse.

---

## S2.6 — Third-party orchestrator evaluation

**Decision:** Include a deliberate reuse study.

Evaluate at least:
- the AWS CAO/orchestrator the user previously referenced;
- Hermes-native execution primitives;
- BullMQ;
- Agenda or node-cron only for simpler scheduling roles;
- n8n;
- Temporal;
- Hatchet;
- Inngest/Trigger.dev style durable workflow engines where self-host/open-source fit exists;
- Windmill/Kestra/Prefect-class systems if they fit resource and licensing constraints.

Do not turn this into an endless survey.

Score against:
- self-hostability;
- resource use;
- license;
- durable timers;
- retries;
- idempotency;
- human pause/resume;
- long-running workflows;
- observability;
- step metadata;
- worker/tool flexibility;
- ease of embedding;
- MCP compatibility;
- operational complexity.

Temporal may be too heavy for the current VPS, but exclude only after measuring fit.

---

## S2.7 — Git

**Decision:**
- frequent small coherent commits;
- stable task IDs in commit messages where practical;
- local repo plus private GitHub remote if the existing project already uses GitHub securely.

Do not create a new public remote.

Use a neutral build identity such as:
`Empirium Build <build@local>`

The exact identity is not important; traceability is.

---

## S2.8 — Toolchain pins

**Decision:** Confirm reuse-first.

Do not churn:
- Node;
- package manager;
- ESLint;
- Prettier;
- Vitest;
- Playwright;
- TypeScript

without a measured reason.

Pin versions after base audit.

---

## S2.9 — Monorepo vs single package

**Decision:** Start with the existing Hermes Studio structure.

Do not create a monorepo/workspace split merely for architecture aesthetics.

Create packages/modules only when boundaries become materially useful, for example:
- office renderer;
- workflow engine adapter;
- shared domain contracts.

Avoid premature package fragmentation.

---

## S2.10 — Test runtime on VPS

**Decision:** Headless Playwright on the VPS is acceptable.

But:
- benchmark RAM/CPU;
- limit concurrency;
- run visual captures at deterministic viewport sizes;
- do not compete with many simultaneous build workers.

Acceptance should include:
- DOM/state assertions;
- screenshots;
- browser console;
- real interaction.

A display server should not be required.

---

# S3 — REQUIREMENT LEDGER & SCOPE

## S3.1 — Ledger base

**Decision:** AC-001–060 is **one input**, not the complete base.

The authoritative ledger must be generated from all product sources.

Each source item should map to one or more atomic requirements.

The ledger needs:
- stable ID;
- source;
- source priority;
- capability;
- mandatory/deferred/optional status;
- milestone;
- dependency;
- acceptance predicate;
- evidence;
- current state.

No substantive source paragraph should remain unmapped.

---

## S3.2 — Target size

**Decision:** Do not set an artificial ledger-size appetite.

For M0/Foundation, ~60–100 atomic requirements may be reasonable.

For the full product, expect **several hundred**.

Correct decomposition is more important than keeping the list short.

A large requirement ledger is acceptable if:
- it is machine-readable;
- grouped hierarchically;
- dependency-aware;
- not duplicated;
- each atomic item is testable.

---

## S3.3 — IDs & mapping

**Decision:** Keep AC-001–060 as stable acceptance references.

Create requirement IDs such as:
- PROD-ORG-###
- PROD-EMP-###
- PROD-WF-###
- PROD-SCHED-###
- PROD-MEM-###
- PROD-MCP-###
- PROD-MODEL-###
- PROD-OFFICE-###
- PROD-REPORT-###
- PROD-SEC-###
- PROD-QA-###
- PROD-UI-###

Each requirement maps to:
- one or more sources;
- one or more acceptance criteria;
- one or more predicates.

Orphan count for mandatory requirements must be zero.

---

## S3.4 — Priority semantics

**Decision:** Reject “P1 = not required for SHIPPED” as the global product rule.

Use:

- **M0-REQUIRED** — required for foundation gate.
- **CORE-REQUIRED** — mandatory before the complete product can be called shipped.
- **EXTENDED** — deliberately optional future enhancement.

Risk is a separate field:
- LOW;
- MEDIUM;
- HIGH;
- CRITICAL.

A requirement can be CORE-REQUIRED and implemented after M0.

---

## S3.5 — Definition of Done source

**Decision:** Derive a canonical DoD from:
- the complete mandatory requirement ledger;
- AC-001–060;
- final product brief completion rules;
- original master-protocol release principles.

DoD is not one prose section.

It should be machine-checkable:
- all mandatory requirements in accepted state;
- all blocking predicates pass;
- no unresolved critical/high defects;
- required soak/recovery evidence complete;
- independent release review complete;
- release SHA fixed.

Owner approval should freeze the DoD before broad campaign execution.

---

## S3.6 — Failure contract

**Decision:** Confirm with one addition.

Every failing mandatory predicate must create:
- a defect/work item;
- failure classification;
- reproduction/evidence;
- responsible requirement;
- next action;
- retry/rework counter.

Failure does not terminate the campaign unless a pre-registered safety/budget condition is reached.

The system must diagnose repeated failure rather than endlessly retry.

---

## S3.7 — Requirement extraction standard

**Decision:** Confirm, and add these questions:

For each requirement:
1. Is this a capability rather than a restated sentence?
2. Can a fresh engineer understand success?
3. Is it atomic enough to verify?
4. Is it traceable to source?
5. Is its mandatory/deferred status explicit?
6. Does it preserve the full product intent?
7. Does it have a proof method?
8. Would passing it still allow an obvious fake implementation?

If #8 is yes, strengthen the predicate.

---

# S4 — ACCEPTANCE PREDICATES

## S4.1 — Predicate classes

**Decision:** The proposed classes are useful but not “exactly one class.”

A requirement may need multiple proofs.

Use proof dimensions:
- deterministic/static;
- unit;
- integration;
- UI runtime;
- unattended/recovery;
- visual;
- accessibility;
- security;
- performance;
- human/subjective review where unavoidable.

Significant behavior may require multiple proof types.

Do not force an office requirement to choose between “UI-runtime” and “visual” when it needs both.

---

## S4.2 — Boot acceptance

**Decision:** Canonical Home = **Organization Overview**.

From there the user enters departments.

Viewport set:
- 1280×800;
- 1366×768;
- 1672×941 if that is the supplied mockup frame;
- 1920×1080;
- representative tablet;
- narrow mobile for responsive checks later.

M0 boot predicate can use 1280×800 and 1672×941; final visual suite should be broader.

---

## S4.3 — Design tokens

**Decision:** Extract a token specification from the supplied mockups and final visual brief.

Store machine-readable design tokens:
- colors;
- background layers;
- borders;
- accent roles;
- typography scale;
- spacing;
- radius;
- shadows/glow;
- status colors;
- motion durations;
- office sizing conventions.

Owner approval is useful before visual freeze.

Do not use tokens as an excuse to flatten the design into a generic template.

---

## S4.4 — Existing test suite

**Decision:** Confirm.

Existing baseline suite must stay green unless:
- a test is proven obsolete/incorrect;
- its replacement is explicitly documented.

Baseline failures discovered before implementation must be recorded separately.

---

## S4.5 — Unattended predicates

**Decision:** Confirm the injected-clock harness for fast deterministic testing.

Additionally:
- perform at least one real-clock schedule test;
- perform one real browser-closed/background execution test;
- perform a multi-day soak.

Injected time is excellent for logic; it does not completely replace real scheduling evidence.

---

## S4.6 — Office truthfulness

**Decision:** DOM/state assertions are necessary but not sufficient.

For each canonical state verify:
1. backend semantic state;
2. API/state adapter output;
3. textual employee dossier;
4. office status label/badge;
5. animation/state class or renderer state;
6. visual evidence for representative states.

The animation may contain decorative motion, but its semantic class must match real state.

Idle ambient behavior is allowed; fake productive behavior is not.

---

## S4.7 — Performance gates

**Decision:** Do not remove all performance criteria.

For M0:
- boot/service ready <30s is acceptable as a coarse gate;
- UI interaction should not visibly stall;
- schedule fire drift should be measured.

For final product preserve the stronger targets from the product protocol:
- warm navigation target around <=2s p95 where realistic;
- local UI feedback around <=200ms p95;
- local read APIs around <=300ms p95 where meaningful;
- main office aiming ~55–60fps on documented test hardware;
- memory-leak investigation on repeated mounts/navigation.

Do not make these brittle if the environment makes a specific number meaningless; measure and document.

---

## S4.8 — Flake policy

**Decision:** Confirm with classification.

- Logic failure: zero blind retry.
- Known transport/network transient: at most one automatic retry.
- Flaky test: defect in test/product until root cause established.
- Do not rerun until green and call it success.

Every retry remains visible in evidence.

---

## S4.9 — Failure creates work

**Decision:** Confirm.

The failure-generated work item should include:
- failing predicate ID;
- requirement IDs;
- exact SHA;
- observed result;
- expected result;
- reproduction command;
- evidence paths;
- likely failure class;
- permitted file scope;
- completion proof.

Spot-checking a sample of 10 during Stage-0 is appropriate, but the controller should schema-validate all automatically.

---

# S5 — ACCEPTANCE HARNESS

## S5.1 — Harness layout

**Decision:** `verify.sh` plus modular `checks/` is acceptable.

The controller must run verification against the exact integrated SHA.

Do not automatically revert every failing integration blindly.

Instead:
- mark integration rejected;
- preserve the SHA/branch/evidence;
- revert or repair according to task policy.

Evidence preservation is more important than keeping the branch artificially green.

---

## S5.2 — Hash protection

**Decision:** Confirm.

Workers must not be able to silently modify acceptance criteria to pass.

Protected:
- requirement ledger;
- predicate definitions;
- harness core;
- release gate;
- test fixtures used as independent acceptance truth.

Changes require dedicated harness-change workflow/review.

---

## S5.3 — Calibration fixtures

**Decision:** Strongly confirm.

Use known-bad cases including:
- missed schedule falsely marked success;
- duplicate schedule occurrence;
- office state lies;
- unauthorized MCP access;
- approval bypass;
- memory leakage between employees;
- retry causes duplicate side effect;
- workflow completion despite failed mandatory step.

The harness must prove it catches bad behavior.

---

## S5.4 — Independent harness review

**Decision:** Confirm.

Use a fresh strong reviewer, ideally a different model family from the harness implementer.

Opus via subscription is appropriate where available.

The reviewer must:
- inspect false-negative risk;
- inspect weak assertions;
- inspect fixture validity;
- challenge bypass paths.

---

## S5.5 — Time budget

**Decision:** <10 minutes for the routine post-integration harness is a good target.

Longer suites should be tiered:
- fast verify;
- integration;
- visual;
- security;
- soak/recovery.

Do not force the 3-day soak into `verify.sh`.

---

## S5.6 — Release gate

**Decision:** For **M0 gate**, require:
- all M0 predicates pass;
- representative real background run passes;
- short soak passes;
- independent review passes.

For **final product release**, require:
- all CORE-REQUIRED predicates pass;
- full required resilience/soak suite passes;
- independent full release review;
- visual release gate;
- security gate;
- final exact SHA.

No LLM may mark the product globally shipped by prose alone.

---

# S6 — EXECUTION GOVERNANCE

## S6.1 — Build controller

**Decision:** Reuse the repaired Nailify controller **as a proven starting point**, not as unquestioned product-specific truth.

Before adapting:
- isolate generic controller behavior;
- remove Nailify-specific requirement semantics;
- verify current acceptance semantics;
- add only failure classes actually needed.

Do not build another large orchestrator from scratch unless the current controller fundamentally cannot meet requirements.

---

## S6.2 — Build state store

**Decision:** In-repo `.hermes/autonomy/project.db` is acceptable for **build-campaign state**.

This is separate from product runtime state.

Keep this distinction explicit.

---

## S6.3 — Build event log

**Decision:** Confirm.

Log:
- tick;
- queue state;
- claim;
- dispatch;
- worker start/end;
- result classification;
- verification;
- rework;
- idle reason;
- provider state;
- human intervention;
- controller restart.

“Why is the controller idle?” must be answerable deterministically.

---

## S6.4 — Worker packet fields

**Decision:** Confirm proposed fields and add:
- task ID;
- run/attempt ID;
- base SHA;
- worktree/branch;
- source requirement text;
- dependencies;
- known architecture contracts;
- allowed data/secrets class;
- model/tool policy;
- relevant prior review defects;
- expected structured handoff schema;
- explicit out-of-scope list;
- escalation behavior;
- no-self-approval clause.

Packets should be bounded and minimal-complete.

---

## S6.5 — Worker runtime

**Decision:** Use fresh bounded Hermes sessions under dedicated build profiles.

Do not expose:
- this chat’s broad personal context;
- unrelated skills;
- unrelated projects;
- unnecessary secrets.

Each worker receives only task-relevant context.

---

## S6.6 — Provider/model freeze

**Decision:** Use a verified free implementation pool with **effective-model attribution mandatory**.

Prefer pinned model for:
- benchmark reproducibility;
- high-risk comparisons.

Allow `auto`/pool for:
- routine implementation after benchmark;
- only if effective model/provider is recorded.

Reviewer:
- Opus/Sonnet subscription depending risk.

Do not let strong subscription reviewers silently become primary implementers.

---

## S6.7 — Paid ceiling

**Decision:** Build-time new pay-as-you-go AI spend ceiling remains **$0** unless the owner explicitly changes it later.

Existing subscriptions are allowed.

No automatic paid fallback.

---

## S6.8 — Attempt schema

**Decision:** Proposed fields are good. Add:
- base_sha;
- result_sha;
- worker/profile ID;
- task class;
- failure_class;
- files_changed;
- tests_run;
- review_verdict;
- retry_of_attempt;
- artifact/evidence paths;
- provider response/error code;
- quota/rate-limit marker;
- human intervention reason.

Add statuses:
- ACCEPTED;
- REVIEW_REJECTED;
- WAITING_PROVIDER;
- CANCELLED;
- POLICY_BLOCKED.

Keep implementation result and acceptance result separate where possible.

---

## S6.9 — Human-intervention counter

**Decision:** Confirm, but do not treat every owner review/sign-off as a failure.

Classify:
- required governance approval;
- product decision;
- rescue/intervention;
- manual technical repair;
- informational review.

Campaign KPI should focus on avoidable rescue interventions, not penalize legitimate product decisions.

---

## S6.10 — Stop rules

**Decision:** Amend.

### Rule 1
Keep: no concurrency growth until single-worker baseline is proven.

Threshold:
- at least 20 representative valid attempts;
- ≥60% accepted first-pass or equivalent clear evidence.

### Rule 2
Do not create recursive supervisor/director hierarchies.

A single durable planner/controller is preferred.

However, bounded temporary planning/review sessions are allowed.

The product’s “Director” employee is unrelated to the build campaign.

### Rule 3
Confirm:
do not build recovery machinery for failure classes not observed or clearly unavoidable by architecture.

### Rule 4
Amend:
model/provider switching can also occur when a provider is objectively unavailable/rate-limited, not only after ten failures.

But it must follow pre-approved routing policy and be recorded.

---

## S6.11 — Campaign budget ceiling

**Decision:** Use **200 valid attempts / 14 calendar days / 2 structured re-baselining rounds** for the first autonomous build campaign.

At that threshold:
- stop autonomous dispatch;
- produce a diagnostic report;
- preserve state;
- request owner decision.

This is **not** permission to call the product failed or finished.

It is a campaign-control boundary to avoid infinite burn.

---

## S6.12 — Watchdog

**Decision:** Confirm.

Systemd watchdog/controller:
- restart dead controller;
- enforce one instance;
- log;
- respect pause;
- no LLM reasoning;
- no spawning recursive supervisors.

Linger/start-on-boot must be proven.

---

## S6.13 — Reporting cadence

**Decision:**
- immediate alert only for genuine owner blocker, policy violation or campaign stop condition;
- daily summary;
- phase-gate checkpoint.

Daily summary should contain:
- requirements accepted that day;
- tasks attempted;
- first-pass acceptance;
- retries/rework;
- open tasks;
- blocking failures;
- provider health;
- controller idle time + reasons;
- human rescue interventions;
- current Git SHA;
- next planned dependency frontier;
- build spend classification.

Do not spam the owner for normal failures.

---

## S6.14 — Artifact locations

**Decision:** Build-campaign artifacts can live under `.hermes/` if:
- structured;
- documented;
- excluded from product runtime state;
- not containing secrets.

Suggested:
- `.hermes/autonomy/`
- `.hermes/packets/`
- `.hermes/checkpoints/`
- `.hermes/reviews/`
- `.hermes/evidence/`
- `.hermes/benchmarks/`

Large generated artifacts may live outside Git with indexed paths.

---

## S6.15 — Kill criteria

**Decision:** Amend wording from “campaign ends” to “autonomous campaign pauses for owner review.”

Trigger pause on:
a. 200 valid attempts / campaign budget exhausted without meaningful gate progress;
b. acceptance <30% after two packet/decomposition redesign rounds;
c. owner materially changes product definition;
d. soak fails 3 consecutive times for the same unresolved cause;
e. security/policy violation;
f. evidence suggests controller is creating duplicate work or losing state;
g. unexpected paid AI spend.

Do not continue blindly.

---

## S6.16 — Provider outage

**Decision:** Free implementation provider pool unavailable >4h:
- pause affected AI implementation dispatch;
- continue deterministic tests/reconciliation that do not need the provider;
- notify in daily/exception channel;
- do not auto-fallback to paid route.

If another already-approved verified-free route exists, it may be used according to routing policy.

---

# S7 — PRE-REGISTERED BENCHMARK

## S7.1 — Benchmark task

**Decision:** Use the **free-games monitor end-to-end** as the primary benchmark vertical slice.

It is the best first slice because it tests:
- external information retrieval;
- schedule;
- workflow run;
- employee assignment;
- model/tool route;
- artifact;
- dedup;
- notification;
- persistence;
- reporting.

However the 20 attempts should not hit live stores identically each time.

Use:
- deterministic fixture/source adapter for repeatability;
- one or more real integration runs separately.

---

## S7.2 — Count

**Decision:** 20 valid attempts initial benchmark.

Hard ceiling 40 before mandatory diagnosis.

Provider aborts that never started meaningful work can be excluded from quality denominator but must remain reported separately.

---

## S7.3 — Decision rules

**Decision:** Confirm thresholds as build-system rules:

- ≥60% accepted → allow controlled concurrency growth.
- 30–59% → improve packet/task decomposition; no added orchestration layer.
- <30% → stop scaling; redesign task shape/context; diagnose.

Do not respond to poor quality by adding more supervisors.

---

## S7.4 — Measurement fields

**Decision:** Confirm and add:
- first-pass acceptance;
- final acceptance after rework;
- failure class;
- diff size;
- tests executed;
- token use if known;
- provider latency;
- reviewer verdict;
- collateral-edit rate;
- task complexity class.

Flat JSONL plus summarized report.

---

## S7.5 — Freeze before attempt 1

**Decision:** Confirm.

Freeze:
- task;
- acceptance predicate;
- fixture;
- packet format;
- selected route/policy.

Harness bug fixes are allowed only with:
- dedicated issue;
- independent review;
- rerun of affected attempts if comparability changed.

---

## S7.6 — Session hygiene

**Decision:** Confirm.

Fresh worker session per attempt.

Worker self-report is evidence input, never the acceptance authority.

The exact integrated code + harness decides.

---

# S8 — CAMPAIGN PHASES, SOAK, POST-FOUNDATION

## S8.1 — Phase gates

**Decision:** Amend order slightly.

Recommended:

### Phase F0 — Source reconciliation / architecture freeze
- complete ledger;
- reuse matrix;
- domain contracts;
- engine decision;
- acceptance harness.

### Phase F1 — Durable domain + persistence
- organization;
- department;
- employee;
- workflow definitions;
- schedules;
- runs;
- memory skeleton;
- permissions skeleton.

### Phase F2 — Scheduler + workflow engine
- durable occurrences;
- task/attempt lifecycle;
- retries;
- handoffs;
- approvals;
- events.

### Phase F3 — First real recurring workflow
- free-games monitor;
- notification;
- reporting;
- real unattended execution.

### Phase F4 — Model/MCP/Memory proof
- two model routes;
- scoped MCP/tool permission;
- persistent employee memory retrieval.

### Phase F5 — Living office + organization/department UI
- truthful state adapter;
- employee dossier;
- calendar;
- activity;
- reports.

### Phase F6 — QA/review + project workflow
- implementation handoff;
- independent QA;
- human approval distinction.

### Phase F7 — Resilience / soak / foundation gate
- recovery;
- browser closed;
- restart;
- provider failure;
- 3-day soak;
- independent review.

Then continue into the remaining CORE-REQUIRED product capabilities.

No owner sign-off should be needed after every tiny phase unless a real product/architecture decision is pending. The goal is autonomy, not repeated permission prompts.

---

## S8.2 — Soak definition

**Decision:** 72 consecutive hours is acceptable for M0/Foundation.

During soak:
- normal user viewing is allowed;
- no AI coding workers may patch the product;
- deterministic runtime processes continue;
- free-games workflow runs on real schedule;
- state survives;
- errors are recorded;
- no manual DB state patches.

For final release, perform broader resilience tests beyond this one routine.

---

## S8.3 — Games monitor specifics

### Stores
M0:
- Steam;
- Epic Games Store.

Later adapters:
- GOG;
- Amazon Prime Gaming;
- others.

### Data source
Preference order:
1. official/public documented source/API/feed;
2. stable first-party web endpoint;
3. browser/scraping fallback.

Do not depend on brittle scraping if a reliable official source exists.

### Frequency
**Daily**, not hourly, for real production use.

Default time:
**09:00 Europe/London**.

Reason:
free-game promotions do not justify 24 hourly checks/day, and unnecessary runs waste resources.

For soak testing, a test schedule may run more frequently using a dedicated test workflow/clock.

### Dedup
Do not use a blind “30 days” rule only.

Deduplicate primarily by:
- store;
- canonical item ID;
- promotion/free-window identity.

Alert again only if:
- a genuinely new free promotion occurs;
- the prior promotion ended and a new one starts;
- the source meaningfully changes.

### History
Keep all run history initially.

Do not silently delete alerts at M0.

### Alert payload
Include:
- game/item name;
- store;
- normal/current price if available;
- current free price;
- source URL;
- promotion start;
- promotion end / claim-by deadline;
- time checked;
- confidence/source notes if data is uncertain.

---

## S8.4 — Soak failure handling

**Decision:** Confirm.

Failure:
- creates defect;
- preserves evidence;
- repairs via normal workflow;
- restarts soak window relevant to the repaired subsystem.

No manual DB patching to manufacture a pass.

---

## S8.5 — Next-stage ordering

**Decision:** The proposed order should change because MCPs and learning are more central than voice/finance.

After M0 Foundation:

1. full workflow builder and reusable workflow templates;
2. full MCP/integration registry + per-employee permissions;
3. richer employee memory + controlled learning loop;
4. second real department + cross-department workflows;
5. richer model routing and performance learning;
6. voice receptionist/realtime-worker capability;
7. external calendar/email/notification integrations;
8. finance templates/module;
9. multi-user/multi-tenant if desired.

The exact order may move based on dependency analysis.

Telephony provider is **not precommitted to Twilio**. Evaluate current providers, cost, latency and existing stack before choosing.

---

## S8.6 — Approvals UX at M0

**Decision:** The defaults proposed are too approval-heavy and would undermine autonomy.

### (a) Publishing a free-games alert artifact
**No approval after workflow activation.**

The user explicitly wants the bot to monitor and bring findings to attention automatically.

### (b) Project workflow past a handoff point
Approval only if that specific step is configured as approval-required.

A normal bot-to-bot handoff should not require the owner.

### (c) Approving a review verdict
No owner approval required for routine QA verdict.

QA can accept/reject according to criteria.

Human authorization is separate.

### (d) First-time scheduled execution
Use a workflow activation/test flow:
- user explicitly activates workflow;
- once activated, recurring executions run autonomously.

Do not request approval every first occurrence after restart/version.

Require human approval only for high-impact actions:
- destructive production action;
- external spending;
- irreversible data change;
- public deployment/publishing if configured;
- security/firewall/DNS;
- financial transfer;
- other user-defined risky actions.

---

## S8.7 — Design fidelity

**Decision:** For M0:
- strong structural fidelity;
- correct information hierarchy;
- coherent dark/cyan visual system;
- high-quality Personal Software office;
- correct states;
- no obviously generic/unfinished screens.

Do not require literal pixel identity to concept art if it harms responsiveness or operational clarity.

For final core release:
- premium polish across all core screens;
- no unresolved critical/high visual defects;
- mockups remain quality/direction references.

---

## S8.8 — Office character assets

**Decision:** Reuse the supplied character/reference assets first.

The original source package reportedly includes:
- character designs;
- proportion sheets;
- state references;
- movement keyframes;
- office environments.

Inventory those before creating replacement SVGs.

If production-ready assets are missing:
- create deterministic original 2D assets;
- use shared rig/state system;
- do not make character production a blocker for workflow semantics.

Do not assume simple six-state SVGs are the final aesthetic if better supplied material exists.

---

## S8.9 — Audio

**Decision:** No general UI audio subsystem required at M0.

Voice/receptionist audio is a later runtime capability and should be architected separately.

Do not import unrelated personal-OS audio requirements.

---

## S8.10 — Post-ship operation

**Decision:** Initial deployment is a personal/private operational system.

No formal external commercial SLO at M0.

However:
- persistent jobs should be expected to recover automatically;
- failures should be visible;
- backups and restart behavior should be reliable.

If later offered commercially, define SLOs then.

---

## S8.11 — Product runtime model costs

**Decision:** Product runtime must support configurable provider routes.

M0:
- one or more preconfigured route adapters;
- at least two usable routes if possible to prove model diversity;
- no API keys in repository;
- settings UI shows configured status;
- employee/step model policy is editable.

FreeLLMAPI may be a default route where fit is good.

But the product must not be architecturally tied to FreeLLMAPI.

The user can later add OpenRouter, direct providers, research providers such as Perplexity, local models, etc.

Runtime product costs are a product policy, distinct from the $0 build-campaign policy.

---

## S8.12 — Calendar

**Decision:** M0 includes an **in-app schedule/calendar view**.

External Google/Outlook calendar synchronization can be later.

The in-app calendar is mandatory because planning bot work over time is central to the product.

---

# S9 — PROCESS & META

## S9.1 — Answer batch

**Decision:** This document answers **all S0–S9 questions now**.

Do not wait for another owner questionnaire unless a truly unresolved product choice emerges from the live environment.

Hermes should now produce the Stage-0 pack.

---

## S9.2 — “All defaults” mechanic

**Decision:** This answer set supersedes the need for “S# all defaults.”

Where this document explicitly confirms a default, it is approved.

Where it amends a default, the amendment wins.

Any future changed owner decision becomes:
- a versioned Decision Register entry;
- with date;
- reason;
- affected requirements.

Do not silently rewrite historical decisions.

---

## S9.3 — Stage-0 pack review

**Decision:** Confirm with one addition.

Stage-0 pack should include:

1. Decision Register;
2. source inventory;
3. source conflict register;
4. reuse/build matrix;
5. orchestrator/workflow-engine evaluation;
6. current-repo audit;
7. canonical domain model;
8. full requirement ledger v1;
9. milestone grouping;
10. dependency graph;
11. predicate drafts;
12. acceptance harness design;
13. calibration fixture plan;
14. build governance files;
15. provider/model benchmark plan;
16. product architecture diagrams/contracts;
17. risk register;
18. explicit list of still-unanswered decisions, ideally empty.

Then run the representative benchmark.

---

## S9.4 — Start trigger

**Decision:** The first **large autonomous campaign** should begin only after:
- Stage-0 pack exists;
- benchmark exists;
- no critical unresolved source conflict remains;
- controller/harness are proven.

However, the user should not need to manually say “continue” at every subsequent stage.

One explicit launch approval for the autonomous campaign is sufficient unless:
- product definition materially changes;
- destructive action requires approval;
- campaign stop condition fires.

---

## S9.5 — This chat’s role / review time

**Decision:** Do not design the system around a fixed weekly owner-review quota.

Assume owner attention is scarce.

The system should:
- batch non-urgent decisions;
- produce concise phase summaries;
- interrupt only for genuine blockers/risk;
- continue routine work autonomously.

For planning purposes, design as if the user may inspect the project only **once per day or less** during an autonomous campaign.

The acceptance machinery must not require constant human presence.

---

# FINAL LOCKED PRINCIPLES FOR HERMES

The following principles supersede any narrower default in the questionnaire:

1. **Do not call M0/P0 the finished product.**
2. **AC-001–060 is not exhaustive.**
3. **The complete requirement ledger must be extracted from all authoritative sources.**
4. **Specialized persistent employees are a core product concept.**
5. **Recurring and event-driven workflows are as important as one-off projects.**
6. **Scheduling/calendar is first-class.**
7. **Durable bot-to-bot handoffs are first-class.**
8. **Each employee needs durable, scoped memory.**
9. **Different employees/jobs must be able to use different LLMs.**
10. **MCP/tool access is per employee and least-privilege.**
11. **The user should not babysit routine execution.**
12. **The browser may close while work continues.**
13. **The living office must reflect real operational state.**
14. **Reporting must make all meaningful work understandable after the fact.**
15. **QA and human approval are different concepts.**
16. **Open-source/existing infrastructure should be reused before generic custom plumbing is built.**
17. **One deterministic control plane owns build execution state; avoid recursive supervisor trees.**
18. **Workers are disposable; durable state is not.**
19. **Evidence, not worker self-report, determines acceptance.**
20. **No fake production metrics or synthetic operational state.**
21. **No automatic paid AI fallback during the build campaign.**
22. **Final product release requires the complete mandatory product ledger, not only the first vertical slice.**

---

# EXPECTED NEXT ACTION FROM HERMES

Hermes should not ask another broad generic questionnaire.

It should now:

1. ingest this answer set;
2. reconcile it with the original product sources;
3. audit the actual machine/repositories;
4. produce the Stage-0 pack;
5. identify only genuinely unresolved decisions that cannot be answered from existing evidence;
6. run the pre-registered representative benchmark after the Stage-0 pack is approved;
7. use benchmark evidence to size the autonomous build campaign;
8. proceed without routine owner interruption once the campaign is explicitly launched.

```

===== 2026-09-22 12:22 | session 20260922_105531_432d90 | AI staff force set up =====
@file:`.hermes/attachments/Pasted content (7.8 KB)`

--- Attached Context ---

📄 @file:`.hermes/attachments/Pasted content (7.8 KB)` (1986 tokens)
```
Yes. I would answer Hermes now rather than open another decision cycle. Several of these “owner decisions” can actually be resolved from the product decisions we've already made.

You can give Hermes the following as the binding answer:

1. **G1 — Design references and character assets: use the mockups already supplied for this project; do not block on `/home/ash/empirium-studio-inputs/`.** The five organization/department mockups supplied at the beginning of this project conversation are intentional **Empirium Studio design references**, even though some of them display the older `EMPIRIUM OS` brand string. They show the intended dark premium command-centre aesthetic, organization overview, department cards, living office, named robots, status rails, activity, projects, QA, knowledge, learning and models/cost layout. Do **not** dismiss them as references for an unrelated personal-OS application simply because of the branding. The branding conflict has already been resolved: architecture/product name is Empirium Studio; those images remain valid visual references. There is no requirement to wait for a separate character sprite pack before Stage 0. First search the existing project/repository/archive once for any genuine supplied character sheets or office assets. If none exist, record `CHARACTER_ASSET_PACK_NOT_PRESENT` and proceed by creating original reusable 2D assets based on the visual language of the supplied mockups and textual design specification. Do not fabricate a claim that a missing asset archive was supplied. The design-reference requirement is therefore **not blocked**. If practical, copy/export the supplied mockups into a stable project `references/` directory so the build and visual-review workers can consume the same immutable references.

2. **G2 — Two M0 model routes: this is an environmental selection, not another owner decision.** The product requirement is that M0 proves **two independently configurable model routes used by different employees/tasks**, with the employee identity remaining stable regardless of the route. Use the already-running **FreeLLMAPI route as Route A**. Inspect the currently installed Ollama models and benchmark them briefly; if there is a suitable local model, use **Ollama as Route B**. A sensible first assignment is Research Architect / higher-semantic work → FreeLLMAPI quality-capable route, and the low-risk Deals/Free-Games Monitor or another bounded classification/formatting step → fast local Ollama route. If no installed Ollama model is capable enough, do not stop and ask me which model to install merely to satisfy the test: use two independently identifiable verified-free routes/models through FreeLLMAPI for M0 and record the effective model for every attempt. The longer-term architecture must support routes such as research-specialist providers like Perplexity and very fast models such as Seed-class models, but those examples are **not M0 provider commitments**. The important proof is per-employee/per-step routing, attribution, and replaceability—not forcing a particular vendor. This continues the model-agnostic design in which employees survive provider/model changes.

3. **G3 — Port: confirm `3003`.** Use port **3003** for the Empirium Studio target if your final port/process sweep still confirms it is free. Make the port configuration-driven rather than hardcoded throughout the codebase. Empirium OS/other existing services on 3000/3001 must not be disturbed.

4. **G4 — Existing `empirium-studio` repository: approve the preserve-and-salvage approach, with one important refinement.** Do **not** throw away substantial existing code simply to obtain a psychologically “clean” project. Preserve the entire existing repository as immutable evidence/reference first. Then perform a structured salvage audit of its 34 screens, 40+ server modules, product docs, existing domain contracts and prior AI workforce implementation. Classify meaningful pieces as `KEEP`, `ADAPT`, `REPLACE`, or `DELETE/LEGACY`. After that audit, create the new clean integration target from whichever base minimizes rework while preserving the correct architecture. If the existing Empirium tree already contains a large amount of valid Hermes Studio plus useful Workforce code, prefer deriving the clean target from it rather than arbitrarily starting from upstream and rebuilding everything. If it is fundamentally contaminated by failed architecture, use the stable Hermes Studio base and selectively port proven components. The old tree must remain available as something like `empirium-studio-legacy` or an immutable Git tag/archive; no destructive cleanup. In other words: **preserve → inventory → classify → choose base → salvage**, not “rename it and start again” before inspection.

5. **G5 — New Kanban board: yes, create a new board, but call it something broader than `empirium-studio-m0`.** Preserve `empirium-studio-build` and `empirium-studio-test` untouched as historical evidence. Create a new canonical campaign board such as **`empirium-studio-v2-build`**. I prefer that over `empirium-studio-m0` because M0 is explicitly only the Foundation gate, not the endpoint of the product; the same durable campaign state should be capable of continuing from M0 into CORE-REQUIRED work without pretending a new project has begun. Tasks themselves can carry milestone fields such as `M0_FOUNDATION`, `CORE`, etc. There must be exactly one canonical dispatch authority for the new board.

6. **G6 — Hermes profiles: inspect before creating anything.** This follows the reuse-first doctrine. Inspect the five existing profiles in full—their SOUL/instructions, tools, MCPs, workspace permissions, model policy, skills, routing descriptions and whether they were created specifically for this project. Then map them to the required build roles. Create **only genuinely missing roles** and do not overwrite or clone existing profiles unnecessarily. One detail in your report also needs reconciliation before action: you wrote “5 of 6 required profiles exist” and then listed five existing profiles plus **three missing profiles**, which mathematically implies eight roles rather than six. Resolve that inventory/source discrepancy first. The likely outcome is that `product-architect`, `repo-researcher`, and `backend-integrator` should be created only where no existing profile semantically covers those responsibilities. Profile names are less important than clear non-overlapping routing contracts. Existing `studio-director`, `frontend-engineer`, `animation-engineer`, `visual-reviewer`, and `qa-engineer` should be reused if their current definitions pass inspection.

And **yes, proceed with the environmental sweep in parallel**. Do not wait for another reply before checking gateway/dispatcher health, kanban configuration, existing profile definitions, the full MCP inventory, model availability in Ollama, FreeLLMAPI current capability/lease status, available ports, systemd services, and the current repository/working-tree situation.

There are also two corrections I want Hermes to carry into the Stage-0 pack. First, the currently discovered codebase means **this is no longer a greenfield planning exercise**: Stage 0 needs a serious salvage/reconciliation pass before architecture is frozen. Second, finding an old deterministic supervisor and old Kanban state does **not** mean they automatically become the new control plane. They are candidates to reuse after their semantics are checked against the newer acceptance doctrine.

After those inspections, Hermes should produce the complete Stage-0 pack. It should **not** return with another general questionnaire. Only bring back a decision if inspection exposes a genuinely irreducible owner choice that cannot be resolved from the existing product charter, decision register, source hierarchy or safe reversible engineering judgment.
```

===== 2026-09-22 12:34 | session 20260922_105531_432d90 | AI staff force set up =====
@file:`.hermes/attachments/Pasted content (5.8 KB)`

--- Attached Context ---

📄 @file:`.hermes/attachments/Pasted content (5.8 KB)` (1476 tokens)
```
I would **not give the launch approval yet** based only on this summary. The Stage-0 structure sounds much closer to what we want, but I need the actual `stage-0-pack-v1.md` before I can review it properly. I cannot access `/home/ash/.hermes/state/stage-0-pack-v1.md` directly from here, so please attach that file or paste it into this chat. I searched the prior project context as well, and the actual 86 KB pack has not previously been provided here.

There are already several things in Hermes's summary that I would want to scrutinize very closely before approving it:

* **The “50 M0 requirements” may be fine for the Foundation milestone, but the pack also needs the full product ledger structure.** Our binding decision was that M0 is only the first architectural proof and that the complete product is likely to decompose into hundreds of atomic requirements. If the pack contains only the 50 M0 requirements and merely postpones extracting CORE-REQUIRED requirements until later, that is a major problem. Stage 0 was supposed to prevent scope loss by establishing the complete source-to-requirement map before autonomous implementation begins.
* **There is a concrete profile-count inconsistency in Hermes's own report.** Earlier in the sweep it says there are **8 existing profiles and 3 missing**, which would give 11 required roles. The final summary then says **“5 of 11 master-prompt profiles already configured” and only 3 are missing**, which accounts for only 8. That needs correcting in the pack before we treat its environment inventory as authoritative.
* **The two-model-route M0 requirement is not actually solved yet.** Ollama has zero models installed. FreeLLMAPI's models endpoint returned zero models. It may still work through its auto route, but M0 requires proof that two distinguishable routes can actually execute work for different employees/steps. That should remain an environmental action/risk until Hermes has machine evidence for Route A and Route B. It is not an owner decision anymore, but it is also not complete merely because the architecture permits it.
* **The existing repository situation needs very careful treatment.** A dirty repository containing 34 screens, 40+ backend modules, architecture docs and prior build artifacts could contain a substantial percentage of the product already—or a large quantity of partially correct architecture. I want to see that the Stage-0 pack actually performs the `KEEP / ADAPT / REPLACE / LEGACY` classification rather than just saying it will happen in F0. Likewise, before anything modifies that tree, the current dirty state should be preserved reproducibly.
* **The old controller and old Kanban board must not accidentally become authority through reuse.** We explicitly decided they are evidence and candidates, not automatically the new control plane. The pack needs an acceptance test for whichever controller/board becomes canonical, especially because one of the major lessons from the earlier attempts was that having a controller that exists and passes tests is not the same as having a controller that genuinely continues the project independently of the temporary LLM session.
* **I want to inspect U1–U12 personally.** Hermes says none require owner decisions, which may be correct, but that is precisely the kind of assertion that can accidentally bury a product choice inside an “engineering resolution.” I want to see each unresolved item, its proposed deterministic resolution, and why it does not alter product behavior.
* **The acceptance predicates deserve the most scrutiny.** This is where earlier autonomous builds have failed conceptually. I want to check whether each predicate proves the actual behavior or merely proves that a row, component or piece of code exists. For example, “scheduler record exists” is not equivalent to “scheduled work fires while the browser is closed, survives restart, does not duplicate, and leaves an intelligible history.” The same applies to memory, MCP permissions, office truthfulness, approvals and handoffs.
* **The harness calibration fixtures sound promising.** Ten deliberately bad implementations are exactly the right idea. But I want to verify that those fixtures attack plausible shortcuts—especially fake office state, duplicate side effects after retry, approval bypass, memory leakage, incorrect schedule recovery, worker self-report being mistaken for acceptance, and a task becoming “complete” merely because no worker remains.
* **The source inventory must include the supplied UI mockups as real visual sources.** Hermes previously almost misclassified them as unrelated Empirium OS material because of the old branding. We already resolved that. I want the source register to reflect that decision, not repeat the mistake.
* **The benchmark must remain an experiment, not become implementation by stealth.** The free-games monitor is supposed to test the worker packet + acceptance machinery across 20 bounded attempts. It should use deterministic fixtures for comparability, with separate live integration proof. It must not mutate the task definition between attempts until a properly recorded benchmark round ends.

So the high-level shape looks encouraging, but I would **not yet respond “approved, launch F0.”** The whole purpose of this Stage-0 exercise is to catch exactly the sort of subtle assumptions that caused the previous systems to run autonomously in the wrong direction.

Attach [`/home/ash/.hermes/state/stage-0-pack-v1.md`] to this chat. Once I have the actual file, I can audit it section by section against the original master protocol, our final product brief, the S0–S9 binding answers, the six G1–G6 resolutions, and the lessons from the previous orchestration failures—and then give you a precise **approve / revise-before-launch** response with every defect called out.
```

===== 2026-09-22 12:47 | session 20260922_105531_432d90 | AI staff force set up =====
@file:`.hermes/attachments/Pasted content (15.6 KB)`

--- Attached Context ---

📄 @file:`.hermes/attachments/Pasted content (15.6 KB)` (3964 tokens)
```
I have now audited the actual Stage-0 pack. The result is **REVISE BEFORE LAUNCH**.

It is a substantial improvement over the earlier planning and I would keep most of it, but I would **not give Hermes the autonomous-campaign launch approval yet**. There are several internal contradictions and two genuine scope-integrity problems that are exactly the kind of thing Stage 0 is supposed to catch.

The strongest parts are worth preserving: the decision register correctly locks M0 as Foundation rather than SHIPPED, treats AC-001–060 as non-exhaustive, preserves reuse-first architecture, separates product employees from build workers, and correctly makes MCP, memory, calendar, model routing and truthful office state part of the real product.  The controller acceptance tests, known-bad harness calibration and explicit behavioral-predicate standard are also very good foundations.  

But I found the following blocking defects.

1. **The “full requirement ledger v1” is not actually in the pack.** Item 8 says that the complete ledger is a Stage-0/F0 requirement and that several hundred atomic requirements are expected, which is correct. But the purported M0 ledger literally contains a placeholder: `"... (50 requirements as listed in original Item 8) ..."`.  It then says another 70–100 requirements still need to be extracted later.  So this is not yet the “complete Stage-0 pack” it claims to be; it is effectively a **pre-F0 planning pack**. That is okay as an intermediate artifact, but it must not be frozen as the product/acceptance baseline.

2. **The authoritative original Part A + Part B V4 sources appear to be missing from the source register.** The source inventory lists an 840-line “V1” master prompt and a separate V2 hardened protocol, but the original source of truth we worked from was the much larger two-part Version 4 protocol.  Before ledger freeze, Hermes must either locate those exact V4 Part A and Part B documents or machine-prove that another registered source is byte/content-equivalent. The complete consolidated brief is useful, but we explicitly decided summaries/derived material do not silently replace the original authority. This is a **HIGH-severity source-integrity issue**.

3. **There is likely source contamination from unrelated material.** The pack treats `rom-rnd` as one of the master-prompt profiles and explicitly references **Tron Bonne** research; U9 even proposes creating a `tron-bonne/` input directory.   Nothing in the consolidated AI Workforce product definition we've established requires Tron Bonne ROM R&D. Hermes must trace those requirements to their exact authoritative source. If they originate from a stale/mixed prompt or another project, they must be classified as unrelated and removed from the current build requirement/profile count. Do not let a contaminated build prompt silently add another project's requirements.

4. **The canonical domain model accidentally drops `Project`.** This is a major product regression. Item 7 contains Department, Employee, Workflow Definition, Schedule, Workflow Run, Task/Step, Attempt, Artifact, Handoff, Review, Approval and so on—but **no Project entity at all**.  The original product contract explicitly requires Projects as durable user intent, distinct from workflows, tasks and runs. One-off projects are a major mode of work alongside recurring/event-driven workflows. Add `Project` back as a first-class entity, with relationships to workflows/tasks/runs/artifacts/reviews/approvals. Also restore or explicitly defer other original entities such as Temporary Worker and Crew rather than accidentally losing them during workflow expansion.

5. **The F7 gate contradicts the entire M0/Core separation.** The milestone table says F7 Foundation exits only when **“All CORE-REQUIRED predicates pass”**, then the very next row says CORE-REQUIRED work continues **after F7**.  Those cannot both be true. F7 should require **all M0-REQUIRED predicates**, the M0 resilience/soak evidence and independent Foundation review. The later final-release gate requires all CORE-REQUIRED predicates.

6. **CORE vs EXTENDED classification is inconsistent.** The binding decision correctly says voice, learning, full MCP registry, cross-department workflows and the richer workflow builder are deferred from M0 but mandatory for Core, while finance, broad multi-tenancy and native mobile are optional/post-core.  But Item 8 puts finance, multi-tenant SaaS and native mobile under “CORE-REQUIREMENTS,” and Item 9 then places **voice receptionist** under EXTENDED.   Fix the tiers before any requirement ledger is frozen:

   * **CORE-REQUIRED:** voice/realtime worker capability, controlled learning, full MCP capability management, cross-department workflows, real visual workflow builder, richer calendar/integrations, multiple departments, model-routing system.
   * **EXTENDED unless subsequently promoted:** finance-specific module/templates, broad SaaS multi-tenancy, native mobile.

7. **The benchmark is positioned too late and therefore cannot perform its intended governance function.** The agreed methodology was: Stage-0/F0 preparation → frozen harness/packet → **20-attempt benchmark** → inspect acceptance rate → decide whether autonomous campaign/concurrency has been earned. Here the phase table puts the benchmark at **F4**, after F1 durable domain, F2 workflow engine and F3 free-games implementation have already been built.  That defeats the point of benchmarking the worker contract before scaling implementation. Move the build-worker benchmark to **after F0/harness freeze and before F1 autonomous implementation**. F4 can still contain a *product* model/MCP/memory acceptance gate, but that is a different test.

8. **The pack conflates “approve this pack” with “launch the autonomous campaign.”** Next Steps says the owner reviews the pack and that this is the single launch approval, after which F0 begins.  But our binding process was that the broad autonomous campaign is launched after the Stage-0/F0 material and benchmark numbers exist. Pack approval should authorize Hermes to **finish F0 and run the benchmark**, not yet unleash the full build campaign. Then one explicit launch approval can authorize F1 onward. Otherwise you're approving a campaign before you've seen the very benchmark intended to determine whether it should run.

9. **The scheduler acceptance predicate is internally impossible as written.** It says the browser is closed **and the service is stopped**, then time passes and the workflow run is created and completed.  Split this into two different proofs:

   * **Browser independence:** browser closed, backend running → scheduled occurrence executes normally.
   * **Missed-run recovery:** backend stopped across the due time → backend restarts → configured missed-run policy (`run-once`, `skip`, `coalesce`, etc.) is correctly applied.

   Those are materially different resilience behaviors.

10. **The free-games predicate assumes that every successful run finds a free game.** It says the run must create an artifact and deliver a notification.  A legitimate run can find nothing. Add two deterministic acceptance scenarios:

* fixture containing qualifying promotions → produce alert/artifact;
* fixture containing no qualifying promotion → successful `NO_MATCH` outcome, no false alert.

This directly protects the “no-result is success” requirement.

11. **The build benchmark does not explicitly freeze the base SHA across all 20 attempts.** It correctly freezes task definition, predicate, fixture, packet and route policy.  But if attempt 2 starts from code produced by attempt 1, and attempt 3 starts from attempt 2, the 20 results are no longer comparable. For the experiment, all 20 independent worker attempts should start from the **same frozen base SHA/worktree state**, unless the benchmark is explicitly defined as a cumulative sequence—which it currently is not. Add `benchmark_base_sha` to the frozen experiment contract.

12. **The controller “No self-decomposition” test says the opposite of its own title.** It currently says the controller “creates its own child tasks from its own analysis only.”  The deterministic controller should not semantically invent work from “its own analysis.” A planner may propose bounded decomposition; the deterministic controller should validate it against requirements/dependencies/budgets and persist/dispatch it. Rewrite this test to prevent autonomous unbounded task invention.

13. **The graceful-pause rule is unsafe for hard-stop conditions.** Item 14 says the controller finishes its current attempt before pausing.  That is reasonable for a normal campaign budget threshold, but not necessarily for:

* security violation;
* unexpected paid spend;
* destructive behavior;
* duplicate state corruption.

Define `SOFT_PAUSE` vs `HARD_STOP`. Hard-stop conditions must be allowed to terminate/cancel the current attempt safely.

14. **There are two conflicting homes for the acceptance harness/build state.** Item 12 puts `verify.sh`, `checks/`, fixtures and evidence in `/home/ash/empirium-studio/`.  Item 14 puts the harness and `project.db` under `/home/ash/.hermes/autonomy/`.  Choose one explicit topology. My recommendation:

* **repo-owned versioned acceptance definition:** `/home/ash/empirium-studio/verify.sh`, `checks/`, fixtures, requirement/predicate files;
* **runtime build-control state/evidence:** `/home/ash/empirium-studio/.hermes/autonomy/` or another explicitly documented durable control directory;
* hashes in control state point to the exact committed harness SHA.

What matters is that workers cannot mutate acceptance and that the exact acceptance version is tied to the integrated SHA.

15. **The risk register understates scope-collapse risk.** It marks scope collapse LOW likelihood because D3 says not to do it.  A written rule is not a mitigation strong enough to make the likelihood low—especially while the full ledger is still missing and `Project` has already disappeared from the domain model. Keep scope collapse at **HIGH severity / MEDIUM or HIGH likelihood until the complete source→requirement map is frozen and orphan count is zero**. Add separate high risks for:

* missing authoritative V4 source;
* source contamination/stale prompt material;
* incomplete full ledger;
* domain concept loss during reconciliation.

16. **The claim “No speculative or unverified claims” is not true yet.** The pack itself contains “likely,” “pending F0,” preliminary classifications and unverified source attachments.  That's perfectly acceptable in a planning document, but don't label it verified. Change this to something like: “Unverified environmental or source conclusions are explicitly marked and have F0 resolution actions.”

### My verdict

This is **not a failed Stage-0 pack**. In fact, most of the governance thinking is considerably better than the systems you were using before. The pack now understands durable state, evidence, benchmark discipline, independent acceptance, scope tiers, reuse-first engineering and the difference between background autonomy and a persistent model session.

But it is **not ready to be frozen or used to launch the autonomous campaign**.

I would make the next status:

> **STAGE-0 PACK V1 — CONDITIONAL / REVISION REQUIRED**
> No product implementation campaign authorized.
> Authorized work: source reconciliation, Stage-0 corrections, environment verification, acceptance-harness preparation and benchmark preparation only.

Then give Hermes this instruction:

> Revise `stage-0-pack-v1.md` into `stage-0-pack-v2.md` before requesting launch approval. Preserve all correct material. Do not restart the document from scratch.
>
> Mandatory corrections:
>
> 1. Locate and register the exact authoritative Empirium Studio Part A + Part B Version 4 master protocol files, or prove content-equivalence to registered sources. Do not freeze the ledger without them.
> 2. Investigate and remove or explicitly justify apparent unrelated source contamination, especially `rom-rnd` / Tron Bonne material. No unrelated project requirement/profile may enter this build without exact authoritative provenance.
> 3. Replace the placeholder Item-8 M0 ledger with the actual atomic entries. F0 must produce the complete product ledger from all authoritative sources before implementation scaling. The ledger must include M0-REQUIRED, CORE-REQUIRED and EXTENDED classifications and maintain zero substantive unmapped authoritative source content.
> 4. Restore `Project` as a first-class canonical domain entity, distinct from Workflow, Task and Run. Audit the original domain contract for any other lost entities, especially Temporary Worker, Crew and their persistence/identity rules.
> 5. Correct F7: Foundation gate requires all M0-REQUIRED predicates, not all CORE-REQUIRED predicates. Final product release requires all CORE-REQUIRED predicates.
> 6. Correct classification contradictions: voice/realtime worker capability remains CORE-REQUIRED; finance-specific module, broad multi-tenancy and native mobile remain EXTENDED unless separately promoted. Reconcile every tier against D8/D83.
> 7. Move the 20-attempt build-worker benchmark to after F0/harness freeze and before F1 autonomous implementation. F4 may retain a separate product-runtime model/MCP/memory gate but must not be the first worker benchmark.
> 8. Separate Stage-0/F0 authorization from autonomous-campaign launch. Approval of V2 authorizes completion of F0 and the benchmark. The broad F1+ campaign launches only after benchmark results meet pre-registered thresholds and one explicit owner launch approval is given.
> 9. Split the scheduler predicate into browser-closed execution and service-down missed-run recovery.
> 10. Add both MATCH and NO_MATCH cases to the free-games workflow acceptance contract.
> 11. Freeze one identical `benchmark_base_sha` for every attempt in a benchmark round so the 20 attempts are genuinely comparable.
> 12. Rewrite Controller Acceptance “No self-decomposition”: semantic decomposition may come from a bounded planner, but the deterministic controller must only validate/persist/dispatch according to requirements, dependencies and budgets; it must not invent unbounded work.
> 13. Define SOFT_PAUSE vs HARD_STOP behavior. Security/policy/spend/state-corruption hard stops may cancel the active attempt; ordinary budget/benchmark pauses may finish safely.
> 14. Resolve harness/control-state path topology. Specify one canonical location for versioned acceptance definitions and one durable runtime-control state location. Remove conflicting paths.
> 15. Raise scope-collapse risk until complete source→requirement coverage is frozen. Add risks for missing V4 authority, source contamination, incomplete ledger and domain concept loss.
> 16. Replace “No speculative or unverified claims” with an honest statement distinguishing verified findings from F0-pending findings.
> 17. Re-run the entire pack self-audit after these changes: source coverage, decision consistency, tier consistency, domain completeness, timeline consistency, predicate quality, benchmark integrity and controller semantics. Do not merely patch the listed lines; search for downstream contradictions caused by each correction.
>
> Output a concise V1→V2 change log at the top and a final table stating every blocking defect above as `RESOLVED` with its exact section/line reference.
>
> Do **not** start F1 implementation and do **not** declare the campaign launched. Return V2 for review.

That is the point at which I would review it once more. If V2 genuinely fixes these items, I expect the next review to be much shorter, because the underlying structure is now largely sound.
```

===== 2026-09-22 12:50 | session 20260922_114520_1bd1f5 | Continue previous task =====
I want to make sure that the contents of the mock-ups are something you have access to. So, the mock-ups for AI Star Force, you should already have some of the mock-ups, but there might be some you don't have. If you go into my Google Drive and go into AI Task Force, inside of there are all of the mock-ups for the AI Star Force, and then similarly for Nailify, all of the mock-ups are in a folder called nail app. Again, same location on my drive and Google Drive. Please make sure both are on the VPS and then also give me the link to them. I either location that they're in on the VPS drive

===== 2026-09-22 12:54 | session 20260922_114520_1bd1f5 | Continue previous task =====
continue this task please

===== 2026-09-22 13:08 | session 20260922_105531_432d90 | AI staff force set up =====
@file:`.hermes/attachments/Pasted content (12.2 KB)`

--- Attached Context ---

📄 @file:`.hermes/attachments/Pasted content (12.2 KB)` (3110 tokens)
```
I’ve reviewed V2. It is **much better**, and the 17 major defects from V1 were mostly understood correctly. But I would still make **one short V3 cleanup pass before approving F0**. This is no longer a product-design problem; it is mostly internal consistency and bookkeeping.

The good news is that Hermes correctly preserved the most important corrections: M0 is still only Foundation, the full product ledger is still required before autonomous implementation scales, Project is restored, the M0/Core/Extended distinction is mostly corrected, the benchmark has been moved before the main build, scheduler recovery was separated from browser-closed execution, MATCH/NO_MATCH behavior was added, the benchmark base SHA is frozen, and hard-stop vs soft-pause semantics now exist. 

I would **not ask it to rethink the architecture again**. I would give it a very targeted V3 correction prompt because I found these remaining issues:

1. **The benchmark timeline is still contradictory.** Item 9 inserts `F1.5` before F1, but Item 10’s dependency graph completely omits it and still shows `F0 → F1 → F2...`.   Rename it something unambiguous like **B0 — Worker Benchmark**, and make the graph explicitly `F0 → B0 → launch approval → F1`.

2. **F4 still has the old benchmark as its exit gate.** F4 is now Model/MCP/Memory proof, but its gate still says “Benchmark: 20 attempts, ≥60% accepted.”  That benchmark belongs only in B0. F4 should instead require the actual **product-runtime** proofs: two routes, per-employee attribution, MCP allow/deny, persistent memory write→restart→retrieve→use.

3. **The NEXT STEPS section contradicts itself.** It correctly says pack approval → F0 → benchmark → second launch approval → F1+, but a few lines later it says **“After F0 gate → F1 begins”**.  Remove the latter. F1 must never begin before the benchmark and second explicit launch approval.

4. **There is accidentally a third owner approval hidden in F0.** The F0 exit gate says “Owner approval: architecture frozen,” while the new process says this pack approval authorizes F0 + benchmark, and the second approval comes only after benchmark.  Unless an irreducible product decision emerges, F0 should close through objective criteria + independent review, not require another routine owner sign-off.

5. **CORE vs EXTENDED still leaks in one place.** The CORE continuation row still lists **finance and multi-user**, even though the next row correctly classifies finance-specific functionality, broad multi-tenancy and native mobile as EXTENDED.  Remove finance/multi-user from the CORE continuation wording unless individually promoted later.

6. **The scheduler predicate was fixed, but the following text is corrupted.** Immediately after the missed-run predicate, lines 602–608 suddenly contain the tail end of the free-games MATCH scenario with no heading/GIVEN/WHEN.  Restore a complete explicit **Scenario 1: MATCH** before Scenario 2.

7. **NO_MATCH should not mean “no artifact of any kind.”** It should mean no *promotion/alert artifact*. A successful run still needs a run result/report/evidence saying “checked successfully, no qualifying promotions.” Otherwise the reporting/audit model gets weakened. Adjust that predicate accordingly.

8. **The harness topology is still not actually resolved.** Item 12 currently defines both `/home/ash/empirium-studio/.hermes/autonomy/` and `/home/ash/.hermes/autonomy/` as build-control state, while Item 14 again puts the full campaign state—including a `harness/` directory—under the global path.   Pick **one canonical project campaign state root**. I recommend:

   * versioned acceptance: `/home/ash/empirium-studio/{verify.sh,checks,fixtures,requirements,predicates}`
   * runtime campaign state: `/home/ash/empirium-studio/.hermes/autonomy/`
   * global `/home/ash/.hermes/` may contain Hermes service/profile infrastructure, but **not a second copy of this campaign’s project.db/packets/evidence**.

9. **Item 12 contains a duplicated directory tree.** After the first complete `checks/` structure, another `checks/` block appears again.  Delete the duplicate so workers have one canonical topology.

10. **The benchmark description still conflates calibration with benchmarking.** Calibration fixtures prove the harness rejects known-bad implementations. The 20-attempt benchmark measures whether bounded workers can implement the same frozen task successfully. Those are different experiments. Lines 777–783 blur this slightly by saying the calibration fixtures make benchmark attempts comparable.  The benchmark’s comparability actually comes from the frozen task, predicate, deterministic task fixture, packet, route policy and `benchmark_base_sha`.

11. **Make it explicit that benchmark code is isolated experimental work, not the build campaign.** All 20 attempts should use independent worktrees from the same SHA and **must not modify canonical main**. Passing benchmark implementations may be retained as evidence, but should not silently become F1 product code before campaign approval. This is especially important because you were concerned earlier about whether we had started building.

12. **Route B should block the appropriate product gate, not necessarily the worker benchmark.** The pack currently says Route B is an “environmental blocker for benchmark launch.”  The worker benchmark is testing autonomous coding quality. It does not inherently require the finished product to already have two runtime model routes. Unless the frozen benchmark task specifically requires model-routing implementation, Route B should block **F4/M0 product acceptance**, not B0 itself.

13. **Temporary Worker and Crew should not be left as “if required.”** The domain section says they will be added only “if required” after the source audit.  We already know permanent Employee vs Temporary Worker is an important distinction in the product definition, and Crew exists as a separate execution/grouping concept rather than a Department. Add them to the reconciliation checklist explicitly so they cannot disappear again. Their exact M0/Core tier can be decided from the authoritative source pass.

14. **The product ledger mixes product requirements and build-governance requirements.** For example, `M0.42 Git worktree support` and `M0.50 Build governance/harness protection` are build-system requirements, not things the Empirium product itself does.  Keep them mandatory for the Foundation process, but give them a separate namespace such as `BUILD-*` or `GOV-*`. This makes the eventual product completion ledger much cleaner.

15. **Several “resolved” risks are stale from V1.** R20 still says Item 8 contains a placeholder, even though V2 replaced it. R21 still says Project is missing even though V2 restored it.  Rewrite them as the actual remaining risks:

* R20: full cross-source ledger is not yet extracted/frozen;
* R21: domain completeness is not yet proven; Project restored, other canonical concepts pending reconciliation.

16. **The change log references `U7a`, but Item 18 contains no U7a.** The V4-source recovery task therefore exists in the prose/conflict register but not in the unresolved-work table. Add it explicitly.

17. **The final verification summary is stale.** It still says there are only C1–C17 and R1–R17 despite V2 adding C18/C19 and R18–R21.  This also means the promised V2 self-audit has not actually been completed yet. Fix all counts from the actual document rather than hardcoding old numbers.

18. **One implementation-audit statement is too strong:** “All real, all substantial — none appear to be stubs.” A line count does not establish that.  Change it to something like “substantial source files exist; semantic correctness and completeness remain unverified pending salvage audit.”

19. **F0 must expand the entire product ledger, not merely “full M0 requirements.”** The Next Steps currently says “Ledger v1 expansion to full M0 requirements.”  The binding rule is stronger: before implementation scaling, F0 must compile **M0 + CORE-REQUIRED + EXTENDED traceability across all authoritative sources**, even though only M0 predicates need implementation immediately.

20. **Source conflict resolution step still says C1–C17.** It must include C18 and C19, especially because those are the two critical source-integrity issues. 

So my status is now:

> **V2: structurally sound, not yet approved. One targeted consistency pass required.**

You can send Hermes this:

> Produce `stage-0-pack-v3.md` by editing V2 in place conceptually—do not redesign the plan and do not reopen product questions.
>
> Fix only the remaining consistency/integrity defects from the latest audit:
>
> 1. Rename the pre-build 20-attempt worker benchmark to `B0 — Worker Benchmark` and place it explicitly between F0 and F1 everywhere, including Item 9, Item 10 and Next Steps.
> 2. Remove the obsolete 20-attempt benchmark gate from F4. F4 is a product-runtime Model/MCP/Memory proof only.
> 3. Remove every path saying F1 starts immediately after F0. F1 starts only after B0 passes and the second explicit autonomous-campaign launch approval.
> 4. Remove routine owner approval from the F0 exit gate. Current pack approval authorizes F0 + B0. Escalate only irreducible product decisions. The next routine owner approval is the campaign launch after B0.
> 5. Remove finance/multi-user from CORE continuation wording unless explicitly promoted. Keep finance-specific module, broad multi-tenancy and native mobile EXTENDED.
> 6. Repair Item 11: restore a complete `Scenario 1 — MATCH` section before `Scenario 2 — NO_MATCH`. In NO_MATCH, create no promotion/alert artifact and no alert, but still persist the successful NO_MATCH run/result/report/evidence.
> 7. Resolve build-state topology completely. Use one project campaign state root only: `/home/ash/empirium-studio/.hermes/autonomy/`. Keep versioned acceptance files in the repo. Remove duplicate project.db/packets/evidence/harness state under `/home/ash/.hermes/autonomy/`; global Hermes directories may contain only global Hermes infrastructure.
> 8. Remove the duplicated directory tree in Item 12 and reconcile Item 14 to the same topology.
> 9. Clearly separate calibration fixtures from the worker benchmark. Calibration proves the harness catches bad implementations. B0 measures worker ability on one frozen bounded implementation task.
> 10. State explicitly that all 20 B0 attempts use isolated worktrees from one identical `benchmark_base_sha`, do not modify canonical main, and are experimental evidence rather than campaign implementation.
> 11. Route B is an M0/F4 product acceptance blocker, not automatically a B0 worker-benchmark blocker unless the frozen benchmark predicate itself requires two product runtime routes.
> 12. Add Temporary Worker and Crew explicitly to the F0 domain reconciliation checklist; do not leave them vulnerable to silent omission.
> 13. Separate BUILD/GOV requirements from PRODUCT M0 requirements in Item 8. Worktree/harness/controller governance should have BUILD-* or GOV-* IDs while remaining mandatory for campaign/Foundation governance.
> 14. Update R20/R21 to reflect V2 reality rather than old V1 defects.
> 15. Add the missing V4 recovery item (`U7a` or a correctly numbered replacement) to Item 18.
> 16. Recalculate all conflict/risk/unresolved counts from the actual V3 document. Remove stale “C1–C17 / R1–R17” claims.
> 17. Replace “none appear to be stubs” with an evidence-limited statement: source files are substantial in size but semantic completeness remains unverified until salvage audit.
> 18. F0 ledger work must produce full source coverage across M0-REQUIRED, CORE-REQUIRED and EXTENDED requirements, not only expand M0.
> 19. Update the F0 conflict-resolution action to include all current conflicts, especially C18/C19.
> 20. Run a final mechanical self-audit for contradictory phase transitions, stale counts, duplicated paths, stale V1 language and tier inconsistencies. Include a V2→V3 resolution table with every item above marked RESOLVED and the exact section reference.
>
> Do not build product functionality. Do not begin B0 yet. Return V3 for final review.

After that, I expect we can probably approve **F0 + benchmark preparation** rather than doing another broad planning cycle.
```

===== 2026-09-22 13:16 | session 20260922_114520_1bd1f5 | Continue previous task =====
is the nail stuff stored seperately to the taskforce stuff? if so lcoaiton please

===== 2026-09-22 13:18 | session 20260922_114520_1bd1f5 | Continue previous task =====
no i mean specifically these mock ups for the nail app
@image:/home/ash/.hermes/images/upload_20260922_131807_1.png
@image:/home/ash/.hermes/images/upload_20260922_131807_2.png
@image:/home/ash/.hermes/images/upload_20260922_131807_3.png
@image:/home/ash/.hermes/images/upload_20260922_131807_4.png
@image:/home/ash/.hermes/images/upload_20260922_131808_5.png
@image:/home/ash/.hermes/images/upload_20260922_131808_6.png
@image:/home/ash/.hermes/images/upload_20260922_131808_7.png
@image:/home/ash/.hermes/images/upload_20260922_131808_8.png
@image:/home/ash/.hermes/images/upload_20260922_131809_9.png
@image:/home/ash/.hermes/images/upload_20260922_131809_10.png
@image:/home/ash/.hermes/images/upload_20260922_131809_11.png
@image:/home/ash/.hermes/images/upload_20260922_131809_12.png
@image:/home/ash/.hermes/images/upload_20260922_131809_13.png
@image:/home/ash/.hermes/images/upload_20260922_131810_14.png
@image:/home/ash/.hermes/images/upload_20260922_131810_15.png
@image:/home/ash/.hermes/images/upload_20260922_131810_16.png
@image:/home/ash/.hermes/images/upload_20260922_131810_17.png
@image:/home/ash/.hermes/images/upload_20260922_131810_18.png
@image:/home/ash/.hermes/images/upload_20260922_131811_19.png
@image:/home/ash/.hermes/images/upload_20260922_131811_20.png
@image:/home/ash/.hermes/images/upload_20260922_131811_21.png
@image:/home/ash/.hermes/images/upload_20260922_131811_22.png
@image:/home/ash/.hermes/images/upload_20260922_131811_23.png
@image:/home/ash/.hermes/images/upload_20260922_131812_24.png
@image:/home/ash/.hermes/images/upload_20260922_131812_25.png
@image:/home/ash/.hermes/images/upload_20260922_131812_26.png
@image:/home/ash/.hermes/images/upload_20260922_131812_27.png
@image:/home/ash/.hermes/images/upload_20260922_131812_28.png
@image:/home/ash/.hermes/images/upload_20260922_131813_29.png
@image:/home/ash/.hermes/images/upload_20260922_131813_30.png
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]

===== 2026-09-22 13:28 | session 20260922_132753_cb3799 | Read-only salvage audit of empirium-studio =====
Perform a READ-ONLY salvage audit of /home/ash/empirium-studio.

Do not modify any file, commit, branch, service, database or configuration.

The current Stage-0 process needs every meaningful existing component classified as:

KEEP — already consistent with current product contract;
ADAPT — useful implementation but requires bounded changes;
REPLACE — functionality needed but current architecture conflicts with the product contract;
LEGACY — obsolete implementation not used going forward;
PRESERVE — forensic/history evidence only.

Do not classify from filenames or line counts alone. Read enough implementation to establish actual semantics.

For each screen/server module/domain store/service:

purpose;
current data authority;
important dependencies;
state it reads/writes;
whether it is genuinely functional or partial;
product requirements it already satisfies;
mismatches with current Empirium Studio contract;
reuse classification;
confidence;
evidence paths/functions.

Pay special attention to:
workforce-domain-store, employee-store, department-store, event-store, autonomy-kernel, director-service, native-kanban-adapter, workforce-office-state, workforce-qa-store, workforce-learning-store, template-store, run-store, workflow builder, workforce screens, jobs/scheduling, memory UI, dashboard and reporting.

Explicitly distinguish old autonomous-build machinery from product-runtime machinery.

Return a salvage report only. No code changes.

===== 2026-09-22 13:28 | session 20260922_132843_72f859 | Red-team Empirium Studio Stage-0 acceptance predicates =====
Red-team the Empirium Studio Stage-0 acceptance strategy.

ANALYSIS ONLY. Do not implement anything.

Review every supplied M0 requirement, acceptance predicate, harness rule and calibration fixture.

For every predicate ask:

Does it prove actual user/system behavior, or merely existence?
Can an implementation technically pass while violating the product intent?
Could it produce a false positive?
Could it produce a false negative?
Does it test restart/browser-closed/background behavior where required?
Does it prove idempotency and duplicate protection?
Does it distinguish successful NO_RESULT/NO_MATCH outcomes from failure?
Does it prove server-side permission enforcement rather than UI hiding?
Does it distinguish QA from human authorization?
Does memory prove session/model/runtime persistence and scope isolation?
Does office state trace all the way from canonical backend state to UI/animation?
Is evidence sufficient for an independent reviewer?

Output a table:
requirement/predicate → current weakness → exploit/bypass scenario → recommended stronger predicate → required evidence → severity.

Then propose additional known-bad calibration fixtures that would catch realistic shortcuts.

Do not rewrite the whole plan. Return only defects and strengthened acceptance language.

===== 2026-09-22 13:29 | session 20260922_132901_0349d7 | Audit Empirium Studio domain model completeness =====
Audit the Empirium Studio canonical domain model for completeness against the supplied authoritative sources.

ANALYSIS ONLY. Do not modify code or the canonical plan.

Build an entity/concept register containing every durable or semantically important product concept, including but not limited to Organization, Department, Employee, Execution Profile, Temporary Worker, Crew, Project, Workflow Definition, Workflow Version, Trigger, Schedule, Occurrence, Workflow Run, Task/Step, Attempt, Artifact, Handoff, Review, Approval, Memory, Knowledge, Learning Proposal, Notification, Report, MCP/Tool, Tool Grant, Model Provider, Model Route, Event, Calendar Item, Audit Record and Attention Item.

For every concept show:

authoritative source;
purpose;
identity/lifetime;
parent/child relationships;
what it must NOT be conflated with;
mutable vs immutable/versioned;
probable M0 / CORE / EXTENDED status based only on supplied decisions;
whether Stage-0 V3 currently contains it correctly.

Then identify:

missing concepts;
concepts accidentally collapsed together;
concepts added without authoritative support;
stale or unrelated material;
contradictions between sources.

Specifically investigate Tron Bonne / ROM-R&D material and state whether it belongs to this product, with exact source provenance.

Return an audit report only. Do not change the product definition yourself.

===== 2026-09-22 13:29 | session 20260922_132919_24b945 | Extract atomic requirements for Empirium Studio =====
You are performing a source-to-requirement extraction for Empirium Studio.

This is ANALYSIS ONLY. Do not write code, modify files, redesign the product, or make new product decisions.

I will provide authoritative product documents. Your job is to exhaustively extract atomic product requirements so another system can merge them into the canonical requirement ledger.

For every substantive requirement, output:

provisional source-local ID;
domain: ORG / DEPARTMENT / EMPLOYEE / PROJECT / WORKFLOW / SCHEDULING / CALENDAR / MEMORY / KNOWLEDGE / LEARNING / MCP / TOOLS / MODELS / QA / APPROVAL / REPORTING / OFFICE / UI / SECURITY / PERFORMANCE / RESILIENCE / OTHER;
atomic requirement statement;
exact source document;
exact section/heading and quote or close paraphrase establishing it;
whether the source makes it mandatory, optional, deferred, or unclear;
behavioral acceptance idea;
dependencies;
possible duplicate of another extracted requirement;
ambiguity/conflict note.

Important rules:

Extract capabilities, not paragraphs.
Split compound requirements where independent failure is possible.
Do not silently merge requirements that merely look similar.
Do not invent requirements.
Do not assume AC-001–060 is exhaustive.
Preserve distinctions such as Employee ≠ Execution Profile ≠ Temporary Worker; Department ≠ Crew; Project ≠ Workflow ≠ Task ≠ Run; QA ≠ Approval; Memory ≠ Knowledge.
Flag anything that appears unrelated to Empirium Studio, particularly stale material from other projects.
Do not assign final canonical PROD-* IDs; the main reconciliation process will do that.

Finish with:

total atomic requirements extracted by domain;
list of source sections with zero extracted requirements and why;
conflicts/ambiguities;
likely duplicates;
concepts that appear in one authoritative source but disappear from another.

The goal is exhaustive source coverage, not brevity.

===== 2026-09-22 13:30 | session 20260922_133028_0e9ebb | None =====
Perform a READ-ONLY audit of the Empirium Studio WORKFORCE UI + WORKFORCE HTTP API layer and return a structured per-module classification. DO NOT modify, create, or delete any file. Only read.

Modules to audit (all paths relative to /home/ash/empirium-studio):
- src/screens/workforce/workforce-screen.tsx (2426 lines - read it all, in chunks)
- src/screens/workforce/workforce-avatar.tsx, src/screens/workforce/avatar-mapping.ts
- src/routes/workforce.tsx
- src/routes/api/workforce-kanban.ts, workforce-projects.ts, workforce-review.ts, workforce-learning.ts
- src/routes/api/workforce/persistence.ts
- src/routes/api/workforce-director.intake.ts, workforce-director.plan.ts, workforce-director.status.$projectId.ts
- src/routes/api/employees/index.ts, src/routes/api/employees/$employeeId.ts
- src/routes/api/departments/index.ts, src/routes/api/departments/$departmentId.ts
- src/types/workforce.ts, src/types/director.ts, src/types/native-kanban.ts
- src/server/workforce-postgres-adapter.ts, src/server/employee-identity-adapter.ts

For EACH module report, in markdown:
1. purpose
2. current data authority (PostgreSQL / JSON file in .runtime / SQLite / native Hermes kanban CLI / in-memory / hardcoded demo data) — prove it by naming the concrete call or constant
3. important dependencies (imports that matter)
4. state it reads and state it writes
5. genuinely functional vs partial/stub — cite the code that shows it (e.g. TODO, hardcoded array, unimplemented branch, empty-state-only)
6. mismatches with the product contract (see context)
7. reuse classification: KEEP / ADAPT / REPLACE / LEGACY / PRESERVE, with a one-line justification
8. confidence: high/medium/low
9. evidence: file path + line numbers + function names

Be specific about: does the workforce screen fabricate any activity/metrics not derived from durable state? Does it read PostgreSQL-backed APIs or file-backed ones? Which panels are wired to real endpoints vs static? Are director intake/plan routes writing durable state or just returning computed plans?

Output ONLY the audit report. No code changes, no git commands that write.

===== 2026-09-22 13:30 | session 20260922_133028_45ed2b | None =====
Perform a READ-ONLY audit of the Empirium Studio NON-WORKFORCE product screens and their backing stores/APIs, and return a structured per-module classification. DO NOT modify, create, or delete any file. Only read.

Modules to audit (paths relative to /home/ash/empirium-studio):
Screens:
- src/screens/jobs/ (jobs-screen.tsx, create-job-dialog.tsx, edit-job-dialog.tsx)
- src/screens/memory/ (memory-browser-screen.tsx, knowledge-browser-screen.tsx) and src/components/memory-viewer/
- src/screens/dashboard/dashboard-screen.tsx
- src/screens/analytics/analytics-screen.tsx
- src/screens/audit/audit-trail-screen.tsx
- src/screens/operations/operations-screen.tsx
- src/screens/tasks/tasks-screen.tsx
- src/screens/crews/ (crews-screen.tsx, crew-detail-screen.tsx) - this contains the WORKFLOW BUILDER; identify the workflow builder component precisely
- src/screens/patterns/patterns-corrections-screen.tsx
- src/screens/conductor/, src/screens/agents/
Backing server modules / routes:
- src/server/task-store.ts, crew-store.ts, workflow-store.ts, template-store.ts, run-store.ts, cost-store.ts, operations-aggregator.ts, memory-browser.ts, knowledge-browser.ts, agent-definitions-store.ts, local-session-store.ts
- relevant routes under src/routes/api/ (tasks, crews, jobs/hermes-jobs, memory, analytics, audit if present)

For EACH module report, in markdown:
1. purpose
2. current data authority (PostgreSQL / JSON file under .runtime / SQLite / ~/.hermes files / Hermes gateway HTTP API / in-memory / hardcoded demo data) — prove it with the concrete call or constant
3. important dependencies
4. state it reads and state it writes
5. genuinely functional vs partial/stub — cite evidence
6. mismatches with the product contract (see context)
7. reuse classification KEEP / ADAPT / REPLACE / LEGACY / PRESERVE with one-line justification
8. confidence high/medium/low
9. evidence: file path + line numbers + function names

Pay particular attention to: whether dashboard/analytics/audit display FABRICATED or demo metrics vs real derived data; whether jobs/scheduling is a real scheduler or a thin proxy to the Hermes agent gateway cron; whether the workflow builder persists to a JSON file (competing authority) and whether it maps to the WorkItem/Attempt model at all.

Output ONLY the audit report. No code changes.

===== 2026-09-22 13:30 | session 20260922_133028_0a7070 | None =====
Perform a READ-ONLY forensic classification of the AUTONOMOUS-BUILD MACHINERY in /home/ash/empirium-studio, and critically determine which parts of it (if any) are imported or executed by the PRODUCT RUNTIME. DO NOT modify, create or delete any file. Only read. Do not run git commands that write.

Scope:
- AI_WORKFORCE_BUILD/ (all subdirs: cao/, controller/, evidence/, evidence-index/, source/, worker-briefs/, worker-results/, opus-reviews/, reef-integration/, plus the JSON/MD ledgers and generated-workforce*.ts/tsx)
- agent/ (AGENTS.md, ORCHESTRATION_CONSTITUTION.md, WORKER_RULES.md, REVIEW_RULES.md, FAILURE_POLICY.md, CONTEXT_PACKET_SPEC.md)
- scripts/ (all files; especially production-autonomy-commission.ts, autonomy-kernel-commission.ts, workforce-migrate.ts, workforce-rollback.ts)
- .worktrees/ (17 worktrees) - determine what they are, whether they are live git worktrees, and whether any contains unmerged work that matters
- .runtime/ - list what state files exist and which code writes them
- test-results/, dist/, .tanstack/
- root-level docs: DEVLOG.md, CHANGELOG.md, FEATURES-INVENTORY.md, RECONCILIATION_EVIDENCE.md, STEAM_DECK_SETUP_GUIDE.md, README.md

Required analysis:
1. For each area: purpose, what produced it, whether it is build-time/forensic machinery or product-runtime machinery.
2. CRITICAL: run read-only greps to determine whether any file under src/ imports anything from AI_WORKFORCE_BUILD/, agent/, or scripts/, and whether package.json scripts wire any of them into build/start/test. Report the exact findings. This is the line between 'old autonomous-build machinery' and 'product-runtime machinery'.
3. Identify AI_WORKFORCE_BUILD/source/ORIGINAL_WORKFORCE_SPEC.md and any other genuine product-requirement source documents — these are requirement authority, not disposable.
4. Read scripts/autonomy-kernel-commission.ts and scripts/production-autonomy-commission.ts enough to say what they actually do and whether they write to PostgreSQL or to JSON ledgers.
5. Read scripts/workforce-migrate.ts and workforce-rollback.ts to describe the actual schema migration mechanism.
6. Assess the AI_WORKFORCE_BUILD/reef-integration/ code: is it a live integration or a parked experiment?
7. Report disk usage per top-level area (du -sh, read-only) so the salvage plan knows what is bulk.

For each area give: purpose; current data authority; dependencies; state read/written; functional vs partial; contract mismatches; classification KEEP/ADAPT/REPLACE/LEGACY/PRESERVE; confidence; evidence paths.

Output ONLY the audit report.

===== 2026-09-22 13:34 | session 20260922_132919_24b945 | Extract atomic requirements for Empirium Studio =====
I want to prepare a clean source pack for a separate Claude Opus requirements-extraction chat.

Do NOT modify product code, do NOT start implementation, and do NOT alter the canonical Stage-0 plan.

Search the VPS thoroughly and locate the following source materials:

Original Empirium Studio Part A — Version 4 protocol
Original Empirium Studio Part B — Version 4 protocol
EMPIRIUM_STUDIO_COMPLETE_PRODUCT_BRIEF
EMPIRIUM_HERMES_S0-S9_OWNER_ANSWERS_2026-09-22-2.md
stage-0-pack-v3.md
Empirium OS AI Workforce — Hardened Autonomous Completion Protocol v2-2.md
FORENSIC_RETROSPECTIVE.md
The 5 Empirium Studio design-reference mockups

Search:

/home/ash/.hermes/attachments/
/home/ash/empirium-studio/
/home/ash/empirium-studio/AI_WORKFORCE_BUILD/
/home/ash/work/empirium-desktop/mockups/
/home/ash/audits/
/home/ash/Documents/
any obvious project/source/archive directories

For the V4 Part A/B documents, do not rely only on filename. Search contents for markers such as:

VERSION 4
AUTONOMOUS AI WORKFORCE BUILD
MASTER META-ORCHESTRATION PROTOCOL
EMPIRIUM STUDIO
section numbering matching the original two-part protocol

If you find likely V4 files under generic names such as Pasted content (...), compare contents and establish whether they are the exact Part A/B documents or content-equivalent copies.

Then create a folder:

/home/ash/empirium-opus-source-pack/

Copy ONLY the relevant source files into it. Do not move or delete originals.

Use clear names:

01_V4_PART_A.md
02_V4_PART_B.md
03_COMPLETE_PRODUCT_BRIEF.md
04_S0-S9_OWNER_ANSWERS.md
05_STAGE_0_PACK_V3.md
06_HARDENED_COMPLETION_PROTOCOL.md
07_FORENSIC_RETROSPECTIVE.md
mockups/01...05

Also create:

/home/ash/empirium-opus-source-pack/SOURCE_MANIFEST.md

For each file record:

original absolute path;
copied filename;
file size;
SHA-256;
source type;
authority level;
whether exact, inferred, or content-equivalent;
any uncertainty.

CRITICAL:

If exact V4 Part A/B cannot be found, say so clearly.
Do not rename some older V1/V2/V3 document as V4.
If you believe another file is content-equivalent, prove it by comparing content and explain the evidence.
Do not include unrelated Tron Bonne / ROM-R&D material in the AI Workforce source pack.
Do not start requirements extraction yet.

Return a concise report with:

which files were found;
exact paths;
whether V4 A/B were found exactly;
any missing files;
the final source-pack directory path.



once you have all of this, finish the task form the first prompt i gave you in this chat

===== 2026-09-22 13:56 | session 20260922_132919_24b945 | Extract atomic requirements for Empirium Studio =====
these are taking too long, use sonnet from claude subscription to speed up

===== 2026-09-22 14:03 | session 20260922_132919_24b945 | Extract atomic requirements for Empirium Studio =====
switch to link 3.0 flash

===== 2026-09-22 14:03 | session 20260922_132919_24b945 | Extract atomic requirements for Empirium Studio =====
the free one right

===== 2026-09-22 14:04 | session 20260922_132919_24b945 | Extract atomic requirements for Empirium Studio =====
inclusionai/ling-3.0-flash-vl:free

===== 2026-09-22 14:06 | session 20260922_132919_24b945 | Extract atomic requirements for Empirium Studio =====
inclusionai/ling-3.0-flash-vl:free



stop all of the sub agents, make sure they use this free model via open router ffs

===== 2026-09-22 14:09 | session 20260922_132919_24b945 | Extract atomic requirements for Empirium Studio =====
What do you see in this image?
@image:/home/ash/.hermes/images/upload_20260922_140927_1.png

===== 2026-09-22 14:14 | session 20260922_132919_24b945 | Extract atomic requirements for Empirium Studio =====
yes

===== 2026-09-22 14:15 | session 20260922_132919_24b945 | Extract atomic requirements for Empirium Studio =====
no they havent, i can still see them

===== 2026-09-22 14:16 | session 20260922_132919_24b945 | Extract atomic requirements for Empirium Studio =====
sitch to open router:free and instead of wating over 6 minutes, if it fails within 20 seconds, then try agian

===== 2026-09-22 14:30 | session 20260922_132919_24b945 | Extract atomic requirements for Empirium Studio =====
switch to sonnet 5 via the claude subscription to do this quickly]

===== 2026-09-22 14:30 | session 20260922_132919_24b945 | Extract atomic requirements for Empirium Studio =====
no, i meant ifor the subagents, to get the work done now