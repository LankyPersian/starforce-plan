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
