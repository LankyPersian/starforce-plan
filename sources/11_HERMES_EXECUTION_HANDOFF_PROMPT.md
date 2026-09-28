# 11 — HERMES EXECUTION HANDOFF PROMPT

Use the following as the instruction wrapper when giving this product package to Hermes.

---

You are being given the final consolidated product charter for the project referred to as **Empirium Studio AI Workforce / AI Staff Force / AI Star Force**.

Your job is to build the product described by the attached product-brief package without collapsing its scope.

## AUTHORITY

Read every file in this package before proposing broad implementation.

The package clarifies and extends the earlier Empirium Studio Part A + Part B master protocol.

Where PRODUCT meaning conflicts:
1. latest explicit user clarifications represented in this package win;
2. this package wins;
3. older Part A + Part B requirements remain binding where not contradicted;
4. visual mockups define design direction but not fake production data.

Where BUILD EXECUTION POLICY is not changed here, preserve the hardened durability, evidence, review, recovery and anti-false-completion rules from the existing master protocol.

## CRITICAL PRODUCT INTERPRETATION

Do not interpret this as merely:
- a multi-agent chat UI;
- an AI dashboard;
- a Kanban board;
- a coding orchestrator;
- a robot animation demo.

The application is a persistent AI workforce operations system.

The center of the product is:
- specialized permanent AI employees;
- departments representing ongoing areas of work;
- reusable workflows;
- recurring scheduled jobs;
- event-driven work;
- durable bot-to-bot handoffs;
- calendars/timing;
- individual agent memory and learning;
- per-agent LLM selection;
- per-agent MCP/tool permissions;
- project/task/run execution;
- approvals;
- QA;
- reporting and observability;
- a truthful living-office UI.

## FIRST ACTION: INGEST AND RECONCILE

Before broad coding:

1. Inventory the current Empirium target repository and current Hermes capabilities.
2. Identify existing functionality that already satisfies product requirements.
3. Build a requirement ledger from this package.
4. Map each requirement to KEEP / ADAPT / BUILD / REPLACE.
5. Identify source-of-truth conflicts.
6. Confirm the repository/product boundary.
7. Create a domain model that preserves Organization, Department, Employee, Workflow Definition, Schedule, Workflow Run, Task, Run/Attempt, Handoff, Artifact, Review, Approval, Memory, Knowledge, Learning Proposal, Report and Event as distinct concepts.
8. Define one canonical authority for each mutable lifecycle.
9. Do not launch mass implementation before the core identity/state/workflow contracts are coherent.

## REUSE-FIRST REQUIREMENT

The user prefers tested open-source/existing technology over writing generic infrastructure from scratch.

Therefore:

- inspect Hermes/Hermes Studio built-ins;
- inspect existing scheduler/dispatcher/Kanban/Conductor/Crew/MCP/model-routing features;
- evaluate relevant existing orchestration/workflow engines already available or previously discussed;
- reuse or wrap mature components when they satisfy the contract;
- custom-build only missing product-specific behavior.

Do not rebuild a generic scheduler, durable retry system, queue, or MCP framework simply because you can.

However, do not allow a third-party engine to redefine Empirium's domain model.

## ARCHITECTURE RULE

Empirium owns:
- departments;
- employee identity;
- workflow definitions;
- schedules;
- permissions;
- memory;
- learning;
- reporting;
- product UI.

Execution engines may back those concepts.

For example:
- a Hermes profile may back an Employee, but Profile is not Employee;
- a Kanban card may back a Task, but card is not Project;
- a Crew is not Department;
- a Conductor mission is not persistent employee lifetime.

## WORKFLOW REQUIREMENT

Treat Workflow as a first-class product entity.

Users must be able to define:
- manual;
- scheduled;
- recurring;
- event-driven

processes in which work passes between specialized employees.

Workflows require:
- steps;
- triggers;
- schedules;
- assignments;
- per-step model/tool/MCP policy;
- structured inputs/outputs;
- branch rules;
- waits/timers;
- retries;
- timeouts;
- human approvals;
- QA;
- reporting;
- version history.

The system must support jobs that happen several times per day as well as monthly jobs.

## MEMORY REQUIREMENT

Each persistent employee requires a durable memory system appropriate to its job.

Memory must:
- survive sessions/restarts;
- be scoped;
- have provenance;
- be governed;
- support correction/expiry;
- feed evidence-backed improvement.

Do not equate memory with a long chat transcript.

## MODEL REQUIREMENT

Different jobs may use different LLMs/providers.

Model selection must be configurable by organization/department/employee/workflow step.

Employee identity must persist across model changes.

Record requested/effective model and usage where available.

## MCP REQUIREMENT

MCP/tool access is first-class and per employee.

Do not grant every employee every tool.

Implement:
- integration registry;
- connection health;
- scoped permissions;
- secret isolation;
- workflow dependency visibility;
- audit.

## LIVING OFFICE REQUIREMENT

The supplied mockups establish the visual quality/direction.

The office is not decorative fiction.

Operational visual states must derive from real semantic runtime state.

The activity feed, employee dossier and bot state should agree.

Keep rooms legible; roughly 3–7 visible workers is the preferred visual density before introducing grouping/multiple rooms.

## REPORTING REQUIREMENT

The user must be able to return later and understand:
- what ran;
- what completed;
- what failed;
- what retried;
- what was handed off;
- what needs approval;
- what is scheduled next;
- which employee/model/tool performed the work;
- what artifacts were produced.

## EXAMPLES THAT MUST BE POSSIBLE

The architecture must support all of the following without custom product rewrites:

1. Personal Software department completing a software project through Research → Development → QA → Learning.
2. Marketing department running recurring content pipelines.
3. Infrastructure bots querying server/Supabase health several times per day.
4. A realtime AI receptionist using voice, CRM and calendar capabilities.
5. A simple personal bot checking Epic Games Store and Steam for free games and notifying the user.
6. Monthly finance/reconciliation routines.
7. Cross-department handoffs.

These are reference scenarios, not hardcoded departments.

## DATA TRUTH

Do not populate production dashboards with fake:
- progress;
- spend;
- health;
- QA;
- active employees;
- activity.

Every metric must have a defined source/formula.

## DURABILITY

The user must be able to close the browser and return later.

Workflows, schedules, employees, memory, runs and history must persist.

Ordinary worker/provider failures must not erase work.

## SECURITY

Use least privilege.

High-impact external actions must honor approval policy server-side.

No UI-only permission enforcement.

## DELIVERABLES BEFORE LARGE IMPLEMENTATION

Produce:
1. source/requirement reconciliation;
2. current-system audit;
3. reuse-vs-build matrix;
4. canonical domain model;
5. workflow/scheduler architecture;
6. employee/model/MCP permission architecture;
7. memory/knowledge architecture;
8. event/observability contract;
9. UI route/page map;
10. staged implementation plan tied to acceptance criteria.

Then execute implementation through the project's established durable orchestration/review process.

## COMPLETION

Do not declare the project complete because:
- pages exist;
- agents can chat;
- tests pass for a subset;
- the office looks good;
- a one-off demo works.

Completion requires the product-level acceptance behaviors in `10_ACCEPTANCE_CRITERIA_AND_PRODUCT_TESTS.md`.

Your recurring question must be:

> Can a real user define ongoing work once, assign it to specialized AI employees with the correct models/tools/memory/permissions, leave the system running, and later see trustworthy evidence that the work was performed, handed off, recovered, learned from and reported correctly?

If the answer is no, the product is not complete.
