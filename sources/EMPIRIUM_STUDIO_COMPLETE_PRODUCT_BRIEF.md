# EMPIRIUM STUDIO / AI STAFF FORCE — COMPLETE CONSOLIDATED PRODUCT BRIEF
**Generated:** 2026-09-22

This file concatenates the modular product-definition package. The modular files remain easier to navigate, but this single file can be supplied to Hermes when one document is preferable.



---

<!-- SOURCE MODULE: 00_READ_ME_FIRST.md -->

# EMPIRIUM STUDIO / AI STAFF FORCE — FINAL PRODUCT BRIEF
## Source-of-truth index and reconciliation rules
**Version:** 2026-09-22  
**Purpose:** Canonical product-definition package for Hermes and future implementation agents.

---

## 1. What this package is

This package is a consolidated product charter for the application currently referred to as **Empirium Studio AI Workforce**, **AI Staff Force / AI Star Force**, and in several visual mockups as **Empirium OS**.

It exists because the intended product has been described across:
- the original two-part Empirium Studio autonomous-workforce master protocol;
- visual mockups of the organization and department experiences;
- project conversations about the AI Staff Force;
- later clarifications about repetitive work, workflows, schedules, calendars, MCPs, model choice, individual agent memory, reporting, voice/receptionist use cases, personal automations, and reuse of existing open-source orchestration technology.

This package is intended to remove ambiguity about **what the product is**.

It is not merely an implementation plan. It is the product contract that implementation plans must preserve.

---

## 2. Authority order when sources conflict

Use the following precedence for PRODUCT meaning:

1. **The user's latest explicit clarifications in the 2026-09-22 product-definition conversation.**
2. **This consolidated product package**, because it incorporates those clarifications.
3. **The original Empirium Studio Part A + Part B protocol**, for product requirements not contradicted here.
4. **The supplied visual mockups**, for visual direction, information architecture, density, and interaction intent.
5. **Earlier project conversations and notes**, where they add requirements not subsequently removed.

For EXECUTION POLICY used to build the application, the existing hardened Part A + Part B build protocol remains relevant unless a later build-system decision explicitly supersedes it.

Never allow a newer implementation shortcut to erase an older product requirement accidentally.

---

## 3. Naming / product-boundary conflict

There is an explicit historical conflict:

- The original master protocol defines the product as **Empirium Studio AI Workforce**, a standalone evolution/fork of Hermes Studio, and says it is **not** to be implemented inside the existing Empirium OS.
- Several later visual mockups display the brand **EMPIRIUM OS**.

Therefore:

- Treat **Empirium Studio AI Workforce** as the canonical working product identity for architecture and repository boundaries until the user explicitly changes it.
- Treat **Empirium OS** in the mockups as visual/branding reference, not permission to merge this application into another existing Empirium OS codebase.
- Keep branding configurable enough that a later rename does not alter the domain model or execution architecture.
- Do not let the branding conflict block product development.

---

## 4. The single most important clarification

The product is **not primarily an AI-agent dashboard**.

It is a **persistent AI workforce operations platform** for assigning real recurring or project-based human work to highly specialized AI employees.

The app combines:

- organization and department structure;
- permanent AI employee identities;
- recurring routines and scheduled jobs;
- event-driven and manually initiated workflows;
- durable handoffs between employees;
- project/task/run execution;
- calendars, timers, deadlines, and dependencies;
- different LLMs for different jobs;
- per-agent MCP/tool access;
- individual and shared memory;
- knowledge and controlled learning;
- human approvals and permissions;
- independent QA/review where appropriate;
- reporting, observability, history, costs, and evidence;
- an animated living-office interface that truthfully visualizes the real system.

A user should be able to replace work that previously required a human employee or small team with one or more specialized AI employees, while retaining visibility and control.

---

## 5. Product mantra

> **Define the work once. Give the right AI employee the right tools, model, memory and permissions. Let the system perform, hand off, repeat, learn and report.**

---

## 6. Required companion documents

Read these documents as one product specification:

1. `01_PRODUCT_VISION_AND_OPERATING_MODEL.md`
2. `02_DOMAIN_MODEL_AND_AI_EMPLOYEES.md`
3. `03_WORKFLOWS_SCHEDULING_CALENDAR_AND_HANDOFFS.md`
4. `04_MEMORY_KNOWLEDGE_LEARNING_AND_IMPROVEMENT.md`
5. `05_MODELS_MCPS_TOOLS_AND_CAPABILITIES.md`
6. `06_UI_UX_LIVING_OFFICE_AND_INFORMATION_ARCHITECTURE.md`
7. `07_REPORTING_OBSERVABILITY_QA_AND_APPROVALS.md`
8. `08_ARCHITECTURE_REUSE_AND_HERMES_INTEGRATION.md`
9. `09_REFERENCE_DEPARTMENTS_AND_END_TO_END_WORKFLOWS.md`
10. `10_ACCEPTANCE_CRITERIA_AND_PRODUCT_TESTS.md`
11. `11_HERMES_EXECUTION_HANDOFF_PROMPT.md`

`EMPIRIUM_STUDIO_COMPLETE_PRODUCT_BRIEF.md` concatenates the package into one file for systems that prefer a single source.

---

## 7. Rules for Hermes and future agents

Hermes must not:
- reduce the system to chats with avatars;
- reduce a department to a folder or crew;
- reduce a permanent employee to a model session;
- reduce a workflow to a one-off prompt;
- treat the living office as decorative fiction;
- hardcode dashboard metrics;
- assume every worker must use the same LLM;
- grant every employee every MCP/tool;
- store operational state only in model memory;
- ask the user to babysit ordinary retries and failures;
- build generic infrastructure from scratch before evaluating existing mature/open-source components;
- conflate the temporary AI workforce building Empirium with the product employees inside Empirium.

Hermes must preserve the product as a durable system that can continue operating while the browser is closed.

---

## 8. Design references

The supplied mockups establish the intended visual language:
- dark navy premium command-center UI;
- cyan/blue primary accents with controlled role/status colors;
- dense but legible dashboards;
- organization overview composed of department cards;
- miniature department-office representations;
- a large living office as the visual anchor of a department;
- side/global navigation plus department-local navigation;
- cards for active work, upcoming work, completed work, QA, knowledge, learning, costs, and activity;
- inspectable named workers with role/status overlays;
- clean, low-clutter rooms in which roughly 3–7 visible workers are easy to identify at a glance;
- strong hierarchy and clear operational state.

Mockup numbers are illustrative only unless backed by real data.

---

## 9. Product completion standard

A visually impressive dashboard is not completion.

The product is only behaving as intended when:
- workflows actually execute;
- schedules actually fire;
- agents actually use the tools they are permitted to use;
- handoffs actually preserve context and artifacts;
- durable state survives restarts;
- agents retain appropriate memory;
- models can be changed without deleting employee identity;
- reports accurately describe what happened;
- office visuals match real operational state;
- and a user can leave the system running and return later to an intelligible, truthful history of work performed.


---

<!-- SOURCE MODULE: 01_PRODUCT_VISION_AND_OPERATING_MODEL.md -->

# 01 — PRODUCT VISION AND OPERATING MODEL

## 1. Product definition

Empirium Studio is a **persistent AI workforce and workflow operations platform**.

It allows a user to build an organization made of departments and specialized AI employees, define the recurring and one-off work those employees should perform, provide each employee with suitable models, tools, MCP integrations, memory, knowledge and permissions, and then allow work to move through reliable workflows with schedules, handoffs, approvals, QA, reporting and recovery.

The closest conceptual analogue is not "a chatbot app."

It is closer to:
- a small-company operating system;
- a workflow automation platform;
- an AI agent runtime;
- a scheduler and calendar;
- an integration/MCP control plane;
- a knowledge and memory system;
- and an operations dashboard

combined into one coherent product.

---

## 2. Why departments exist

A department represents a durable **area of responsibility**.

Departments are not merely containers for a one-off project. They exist because real organizations have continuing bodies of work.

Examples:
- Personal Software;
- Marketing & Content;
- Infrastructure / DevOps;
- Business & Growth;
- Research & Learning;
- Finance;
- Personal Operations;
- Customer Service / Reception.

Each department can contain:
- permanent AI employees;
- reusable workflows;
- recurring routines;
- projects;
- queues;
- schedules;
- department-specific tools and MCPs;
- knowledge;
- policies;
- budgets;
- QA rules;
- reports;
- a living-office scene.

A department should be able to keep functioning month after month.

---

## 3. Why employees exist

An AI employee is a **persistent specialist identity** designed to do a narrow, understandable job that could previously have been given to a human worker.

Examples:
- Researcher;
- Copywriter;
- SEO analyst;
- Social media scheduler;
- Database health analyst;
- Server maintenance operator;
- QA engineer;
- Developer;
- Customer-service receptionist;
- Appointment booking agent;
- Finance reconciliation assistant;
- Personal deal/freebie monitor.

The system should encourage specialization rather than making every bot a generic "do anything" assistant.

A specialized employee has:
- a role;
- responsibilities;
- known inputs;
- expected outputs;
- job rules;
- default tools;
- allowed MCPs;
- model preferences;
- memory;
- knowledge access;
- escalation rules;
- approval requirements;
- performance history.

The employee persists even when the underlying LLM changes.

---

## 4. Three fundamental kinds of work

The product must support all three at the same time.

### A. Recurring operational work

This is the most important clarification added after the original product brief.

Examples:
- check servers every morning;
- query Supabase health several times per day;
- generate and schedule content every weekday;
- reconcile a report on the first day of every month;
- check free games once per day;
- send a weekly performance summary;
- clean stale data every Friday subject to approval.

This work has:
- a definition;
- cadence;
- inputs;
- ownership;
- output destination;
- history;
- success/failure state;
- next scheduled run.

### B. Event-driven workflows

Examples:
- inbound lead arrives;
- form submitted;
- phone call received;
- support message received;
- deployment completed;
- database alert fires;
- new file appears;
- webhook arrives.

The event starts a workflow automatically.

### C. One-off projects

Examples:
- build a mobile app;
- research a market;
- prepare a campaign;
- migrate a database;
- create a new reporting dashboard.

Projects can be decomposed into tasks, assigned across employees, independently reviewed, and completed with evidence.

---

## 5. The normal operating loop

A typical loop is:

**Trigger or user request**
→ determine department/workflow
→ create a durable work instance
→ assign first employee
→ employee receives the correct context, tools, memory and model
→ employee performs work
→ system records run and artifacts
→ output is validated
→ handoff to next employee or branch
→ optional human approval
→ downstream work continues
→ final result is delivered
→ report is written
→ useful lessons enter controlled memory/knowledge
→ recurring workflow schedules its next execution.

This loop must be visible in the UI and durable in the backend.

---

## 6. Work must pass between bots

The product is explicitly designed around **handoffs**.

A handoff is not "start a new chat and hope the next model understands."

A proper handoff identifies:
- what job is being handed over;
- source employee;
- target employee;
- why the handoff is occurring;
- artifacts produced;
- structured facts/variables;
- decisions already made;
- unresolved issues;
- constraints;
- required next action;
- acceptance criteria;
- provenance and timestamps.

The next employee should receive the minimum complete context required to continue correctly.

---

## 7. Rules matter

This is not unrestricted autonomous behavior.

A workflow can contain deterministic rules such as:
- only publish after QA;
- never spend money without approval;
- do not email a customer outside permitted hours;
- retry twice after a transient API error;
- after three failures escalate to an operator;
- if server memory exceeds threshold, run diagnostics;
- if diagnostics show production risk, require approval before restart;
- if research confidence is low, request a second source;
- if calendar has no availability, offer alternative dates.

Rules are first-class configuration.

---

## 8. Time is first-class

The application must understand:
- exact scheduled times;
- recurring schedules;
- time zones;
- daylight-saving changes;
- delays and timers;
- "wait until";
- deadlines;
- service-level expectations;
- allowed work windows;
- calendar availability;
- recurring series;
- dependencies that unlock later work.

The user should be able to inspect what the workforce intends to do today, this week, this month and later.

---

## 9. The system can contain more than ordinary text LLM agents

An employee may be backed by:
- a text LLM;
- a multimodal model;
- a voice agent;
- a realtime receptionist;
- a deterministic script;
- a browser automation runner;
- a database query tool;
- a server operator;
- a hybrid process combining deterministic and LLM steps.

The product model is "AI employee / work capability," not "one chat model per bot."

A receptionist could answer a real phone call, qualify the caller, update a CRM, book a calendar slot, and hand the resulting record to another employee.

---

## 10. Small jobs and serious jobs belong in the same platform

The platform must not assume every workflow is enterprise-critical.

Examples at the lightweight end:
- check Steam and Epic Games for current free games and notify the user;
- monitor a price;
- summarize a daily feed;
- remind the user of an expiring item.

Examples at the serious end:
- maintain infrastructure;
- run customer-facing reception;
- process leads;
- build and test software;
- publish marketing;
- perform finance administration.

The difference is permissions, risk, tool access, QA and approval policy—not a different product.

---

## 11. The user should manage outcomes rather than sessions

The product should minimize "prompt babysitting."

The user should not have to:
- keep browser tabs open;
- manually restart every failed model call;
- transfer text between bots;
- remember where a workflow left off;
- repeatedly explain the same role;
- manually inspect logs to determine whether routine work happened.

The system should surface exceptions and decisions, while handling ordinary execution autonomously.

---

## 12. Core user promise

The product promise can be expressed as:

> "Turn repeatable human work into transparent, controllable AI operations."

The user defines:
- who does the work;
- what success means;
- when it happens;
- what resources the worker may use;
- how work is handed off;
- where humans retain control.

Empirium takes responsibility for durable execution, reporting and continuity.

---

## 13. What this product is not

It is not:
- merely a pretty dashboard;
- a roleplay simulation;
- a collection of independent chat windows;
- a Kanban board with robot graphics;
- a prompt library;
- a single coding orchestrator;
- a one-shot "multi-agent swarm";
- an LLM benchmark application;
- a scheduler with no agent intelligence;
- a generic automation builder with no persistent employee identity.

It deliberately combines employee identity and memory with structured workflow automation.

---

## 14. Product qualities

The finished system should feel:
- dependable;
- legible;
- alive;
- extensible;
- safe;
- inspectable;
- easy to configure;
- capable of running unattended;
- capable of both personal and business use;
- model-agnostic;
- integration-friendly;
- open-source/reuse-friendly;
- truthful about what it knows and what happened.

---

## 15. First-class design tension

The product must balance two modes:

### Human metaphor
Departments, employees, offices, desks, roles, handoffs, calendars, performance and learning make the product intuitive.

### Machine precision
Underneath, work must use durable IDs, state machines, explicit schedules, permissions, retries, data contracts and audit history.

The human metaphor must never be allowed to make machine state ambiguous.

The office is a representation of the state machine, not a replacement for it.


---

<!-- SOURCE MODULE: 02_DOMAIN_MODEL_AND_AI_EMPLOYEES.md -->

# 02 — DOMAIN MODEL AND AI EMPLOYEES

## 1. Canonical hierarchy

The product domain should support:

**Organization**
→ **Department**
→ **Employee**
→ **Workflow / Project / Routine**
→ **Work Instance**
→ **Step / Task**
→ **Run / Attempt**
→ **Artifact / Handoff / Review / Approval**
→ **History / Reporting / Learning**

The exact database schema may differ, but these concepts must remain distinct.

---

## 2. Organization

Represents the entire AI workforce.

Suggested responsibilities:
- identity and branding;
- global policies;
- user membership;
- department registry;
- organization-level integrations;
- global schedules;
- global knowledge;
- model/provider registry;
- cost and budget rules;
- security defaults;
- alerting;
- organization-wide reports.

Organization status must derive from real backend state.

---

## 3. Department

A department is a persistent organizational unit.

Required conceptual fields:
- `department_id`;
- name;
- purpose;
- description;
- motto/identity;
- status;
- member employees;
- workflows;
- routines;
- projects;
- queues;
- schedules;
- local integrations;
- knowledge scope;
- model policy;
- tool policy;
- QA policy;
- approval policy;
- budget/cost limits;
- working hours;
- reports;
- office layout/theme;
- history.

A department is not a Hermes Crew. A Crew may be an execution convenience backing some work.

---

## 4. Employee

An Employee is a permanent named work identity.

It survives:
- individual sessions;
- model calls;
- task attempts;
- process restarts;
- provider changes;
- model upgrades;
- browser closure;
- routine/job repetitions.

Suggested fields:

### Identity
- employee ID;
- display name;
- avatar/robot skin;
- department;
- job title;
- role description;
- responsibilities;
- seniority/authority class where useful;
- workstation / office position.

### Job contract
- "use this employee when..." routing description;
- accepted input types;
- required output format;
- definition of success;
- prohibited work;
- escalation path;
- handoff destinations;
- SLA / urgency policy;
- QA requirements.

### Intelligence
- preferred model(s);
- fallback model policy;
- reasoning level where supported;
- multimodal requirements;
- context limits;
- latency preference;
- quality preference;
- privacy constraints.

### Capabilities
- tools;
- MCP servers;
- browser access;
- file access;
- databases;
- voice/telephony;
- shell/server access;
- CRM;
- email;
- calendar;
- social networks;
- search;
- code repositories;
- custom APIs.

### Memory
- personal working memory policy;
- long-term employee memory;
- learned preferences;
- prior-task lessons;
- performance history;
- retrieval scope;
- write policy;
- retention policy.

### Governance
- permissions;
- approval requirements;
- allowed side effects;
- budget limits;
- secret scopes;
- working hours;
- concurrency limits;
- data-class restrictions.

### History
- projects;
- workflow runs;
- task runs;
- failures;
- reviews;
- output quality;
- model usage;
- cost;
- configuration versions;
- learning proposals.

---

## 5. Execution profile

Separate the enduring employee from runtime implementation.

An Execution Profile can map the employee to:
- a Hermes profile;
- another orchestrator agent definition;
- a model/provider route;
- allowed tools;
- environment variables;
- workspace;
- sandbox;
- runtime class.

This allows an employee to switch from one model/provider to another without "becoming a new employee."

---

## 6. Employee types

The platform should not force one runtime style.

Possible employee classes include:

### Knowledge worker
Research, analysis, writing, planning.

### Operator
Uses APIs, MCPs or deterministic tools to perform actions.

### Builder
Creates or edits code, documents, designs or assets.

### Reviewer / QA
Independently validates another employee's output.

### Realtime conversational worker
Receptionist, sales agent, customer-service voice agent.

### Monitor
Watches systems or external sources and acts when conditions are met.

### Coordinator
Routes work and manages a bounded process.

An employee can combine types, but job contracts should remain comprehensible.

---

## 7. Temporary worker

The system may create temporary subagents/contractors for bounded work.

Temporary workers:
- have explicit parent work;
- are visually distinguished from permanent employees;
- have limited lifetime;
- inherit only necessary permissions;
- do not automatically acquire permanent memory or identity;
- do not replace the permanent employee model.

---

## 8. Workflow Definition

A Workflow Definition is a reusable process.

Suggested fields:
- workflow ID;
- name;
- department;
- purpose;
- owner;
- version;
- status: draft/test/active/paused/retired;
- trigger definitions;
- schedule;
- workflow graph;
- input schema;
- variables;
- step definitions;
- employee assignments;
- tool permissions;
- model overrides;
- branch conditions;
- retries;
- timeouts;
- approvals;
- output/report rules;
- failure/escalation rules;
- calendar behavior;
- cost budget;
- history.

This is one of the most important domain entities and should be first-class in the product.

---

## 9. Routine / Recurring Job

A Routine is a workflow whose defining characteristic is repeated execution.

Examples:
- every weekday 08:00;
- every four hours;
- first business day of month;
- every Friday after 17:00;
- on server-health alert.

A Routine should show:
- next run;
- last run;
- recent result;
- current health;
- recurrence rule;
- owner;
- downstream dependencies;
- recent failures;
- average duration;
- current version.

---

## 10. Workflow Run / Work Instance

A Workflow Run is one durable instance of a workflow.

For recurring jobs, each occurrence creates its own run identity.

Example:
- Definition: "Daily free-game scan"
- Run: "2026-09-22 08:00 occurrence"

A run records:
- start trigger;
- version used;
- step states;
- employees used;
- models;
- tool/MCP use;
- artifacts;
- handoffs;
- approvals;
- timings;
- retries;
- errors;
- final outcome;
- report;
- cost/usage.

---

## 11. Project

A Project represents a larger durable user objective.

It can contain:
- requirements;
- milestones;
- tasks;
- workflows;
- ad-hoc runs;
- dependencies;
- artifacts;
- approvals;
- evidence;
- completion gate.

A Project may instantiate reusable workflows but is not itself required to be recurring.

---

## 12. Task / Step

A Task is bounded work.

A workflow Step may map to a Task.

Task state must be distinct from Run state.

A task can be:
- waiting;
- ready;
- queued;
- in progress;
- waiting on dependency;
- waiting on provider;
- waiting on human;
- waiting on scheduled time;
- under review;
- changes requested;
- failed;
- completed;
- cancelled.

---

## 13. Run / Attempt

A Run is one actual attempt by a worker/runtime.

One task can have multiple attempts.

A run should record:
- task;
- employee;
- runtime profile;
- requested model;
- effective model;
- provider;
- timestamps;
- status;
- logs/events;
- tool calls;
- MCP interactions;
- tokens;
- reported cost;
- artifacts;
- errors;
- retry relationship.

Never overwrite previous attempt history just because a later retry succeeded.

---

## 14. Artifact

Anything produced by work should be referencable:
- text;
- document;
- image;
- code commit;
- report;
- database result;
- screenshot;
- audio;
- call transcript;
- calendar event;
- CRM record;
- social post;
- structured JSON;
- external URL.

Artifacts need provenance.

---

## 15. Handoff

A Handoff connects steps/employees.

Minimum handoff record:
- source step;
- source employee;
- target step;
- target employee;
- timestamp;
- reason;
- data payload;
- artifact references;
- summarized context;
- unresolved issues;
- next expected action;
- acceptance criteria.

Handoff context should be structured rather than relying solely on raw transcript.

---

## 16. Review

A Review is independent validation of work.

It should identify:
- what artifact/revision/run was reviewed;
- reviewer identity/model;
- criteria;
- evidence;
- verdict;
- defects;
- required repair.

QA review is separate from human permission to perform a risky action.

---

## 17. Approval

An Approval is authorization.

Examples:
- publish publicly;
- send external communication;
- spend money;
- delete data;
- restart production;
- deploy;
- change security policy;
- make an irreversible database change.

Approval state can pause only the dependent step while unrelated work continues.

---

## 18. Schedule

A Schedule is a durable temporal contract.

It should support:
- one-off future time;
- interval recurrence;
- cron-like recurrence;
- calendar recurrence;
- weekdays/monthly rules;
- time zone;
- daylight-saving correctness;
- start/end date;
- blackout windows;
- catch-up behavior after downtime;
- missed-run policy;
- overlap policy.

---

## 19. Calendar Item

The calendar should represent meaningful planned work:
- workflow runs;
- deadlines;
- approvals;
- appointments;
- human events;
- bot work windows;
- recurring routines.

It is not merely decorative.

---

## 20. Trigger

Trigger classes should include at minimum:
- manual;
- scheduled;
- webhook;
- external event;
- incoming message/email;
- phone/voice event;
- database change where supported;
- monitoring threshold;
- completion of another workflow;
- approval;
- file creation/change;
- API call.

---

## 21. Notification

A Notification is a user-facing event, not the same as a raw system event.

Examples:
- action required;
- work complete;
- recurring job failed;
- risky condition found;
- free games found;
- call escalated;
- budget threshold reached.

Notifications should be deduplicated and severity-aware.

---

## 22. Report

Reports make the work comprehensible.

Reports can exist at:
- workflow-run level;
- daily department level;
- weekly organization level;
- monthly performance level;
- agent performance level;
- model/cost level.

A report should link back to source runs/evidence.

---

## 23. Knowledge item

Durable information intended for reuse.

Scopes:
- global;
- department;
- project/workflow;
- employee.

Operational state must not live only as a knowledge note.

---

## 24. Memory item

Memory is worker-oriented retained context.

Memory items should have:
- scope;
- source;
- content;
- confidence;
- timestamp;
- retention;
- sensitivity;
- evidence;
- write author.

Memory must be editable/reviewable where appropriate.

---

## 25. Learning proposal

A Learning Proposal is a suggested change based on evidence.

Examples:
- change prompt;
- change model preference;
- add or remove a tool;
- alter a workflow;
- add a memory rule;
- adjust QA criteria;
- change retry behavior.

Critical proposals require review before activation.

---

## 26. Versioning

Version these items where changes can materially alter behavior:
- employee prompt/SOUL;
- employee capabilities;
- workflow definitions;
- model policy;
- tool/MCP policy;
- approval rules;
- memory policy;
- report templates.

The system should retain:
- author;
- timestamp;
- diff;
- reason;
- active version;
- rollback target.

---

## 27. Identity invariants

These distinctions must not collapse:

- Employee ≠ model call.
- Employee ≠ Hermes profile.
- Employee ≠ temporary worker.
- Department ≠ crew.
- Workflow definition ≠ workflow run.
- Project ≠ workflow.
- Task ≠ run.
- Review ≠ approval.
- Memory ≠ current operational state.
- Knowledge ≠ model context window.
- Scheduled time ≠ active execution.
- "Bot moving" ≠ actual work.


---

<!-- SOURCE MODULE: 03_WORKFLOWS_SCHEDULING_CALENDAR_AND_HANDOFFS.md -->

# 03 — WORKFLOWS, SCHEDULING, CALENDAR AND HANDOFFS

## 1. Workflows are a central product surface

The app must allow the user to define repetitive work without writing custom orchestration code.

The workflow builder is not an optional developer tool hidden behind settings. It is a major end-user capability.

A user should be able to answer:
- what starts this process?
- who does the first job?
- what does that worker receive?
- which tools can it use?
- what constitutes success?
- where does the output go?
- who receives it next?
- what happens if something fails?
- when does it run again?
- when does a human need to approve?

---

## 2. Workflow creation modes

At minimum support:

### Visual builder
Node-and-edge or structured step builder.

### Form-based/simple builder
For straightforward routines that do not need a complex graph.

### Template-based creation
Preconfigured common patterns that the user can edit.

A future conversational builder may be added, where the user describes the process in natural language and the system proposes a workflow. If implemented, it must still produce a visible, editable workflow definition rather than hiding behavior in a prompt.

---

## 3. Core node types

The workflow runtime should be able to express:

- Agent step;
- Deterministic tool/script step;
- MCP action;
- HTTP/API step;
- database query/action;
- browser automation step;
- voice/call step;
- wait/delay;
- wait-until time;
- condition/branch;
- merge/join;
- loop/repeat with explicit bounds;
- human approval;
- human input;
- QA/review;
- notification;
- report generation;
- calendar lookup/create/update;
- webhook emit;
- file/document action;
- sub-workflow.

---

## 4. Triggers

A workflow can begin because:
- user clicks Run;
- user creates a project;
- a schedule fires;
- another workflow completes;
- a webhook arrives;
- a monitored condition changes;
- a phone call arrives;
- an email/message arrives;
- a file changes;
- a database event occurs;
- a calendar event approaches;
- a human approves a paused step.

---

## 5. Scheduling requirements

Support jobs occurring:
- multiple times per day;
- daily;
- weekdays only;
- weekly;
- monthly;
- on selected dates;
- at an exact future time;
- after a delay;
- after another task;
- only during allowed windows.

The scheduler must be durable. Closing the browser cannot cancel work.

---

## 6. Calendar management

The product should include a real planning/calendar view.

It should expose:
- upcoming bot work;
- recurring routines;
- next-run time;
- deadlines;
- human appointments created by agents;
- pending approvals with due dates;
- workflow dependencies with planned timing;
- department workload by day/week.

Calendar interactions should allow:
- rescheduling a run;
- pausing one occurrence;
- pausing a recurring series;
- changing recurrence;
- viewing run history;
- detecting conflicts where relevant.

Time zones and daylight saving must be explicit.

---

## 7. Work cascades

A workflow can be a cascade such as:

Researcher
→ Strategist
→ Writer
→ Reviewer
→ Publisher
→ Analyst.

Each stage can:
- transform the output;
- reject it;
- send it backward;
- wait for another input;
- branch;
- perform a tool action;
- request approval.

The visual builder should make this understandable without reading code.

---

## 8. Cross-department workflows

Work may cross organizational boundaries.

Example:
Marketing identifies a campaign need
→ Research supplies market data
→ Business approves target segment
→ Marketing creates content
→ Finance validates budget
→ Publishing agent schedules release.

Cross-department handoffs must retain provenance and ownership.

---

## 9. Data contracts between steps

Each step should support defined inputs/outputs.

Examples:
- typed fields;
- JSON schema;
- artifact references;
- required/optional fields;
- file types;
- confidence score;
- status;
- evidence references.

A downstream worker should not need to parse an entire free-form conversation when the important information can be passed structurally.

---

## 10. Context packet

When a step is assigned, the runtime should assemble a bounded context packet containing:
- task objective;
- workflow purpose;
- relevant input variables;
- required artifacts;
- previous step summary;
- required source artifacts;
- applicable rules;
- employee role;
- tools and permissions;
- selected memories;
- selected knowledge;
- output contract;
- acceptance criteria;
- deadline/urgency.

Do not automatically dump the entire organization history into every worker.

---

## 11. Handoff semantics

The system must know the difference between:
- work completed and handed off;
- work completed with no next step;
- work rejected;
- work waiting on human;
- work waiting on time;
- work waiting on dependency;
- work waiting on provider/tool;
- work failed and retrying.

This distinction should be visible.

---

## 12. Retries

Retry policy can be configured per step.

A good retry system distinguishes:
- transient network error;
- provider rate limit;
- malformed response;
- tool unavailable;
- validation failure;
- genuine business-rule failure.

Retries must not create duplicate external side effects.

Use idempotency controls where applicable.

---

## 13. Failure paths

Every workflow should define or inherit:
- retry count;
- backoff;
- fallback worker/model if permitted;
- escalation employee;
- user alert threshold;
- terminal failure behavior;
- partial-completion behavior.

Failure should create history, not disappear.

---

## 14. Timeout and stale execution

Steps may have:
- execution timeout;
- no-progress timeout;
- external-wait timeout;
- human-approval expiry;
- scheduled window.

Timeout should lead to an explicit state and defined next action.

---

## 15. Concurrency

Some steps can run in parallel.

The system should support:
- fan-out;
- fan-in;
- concurrency limits;
- employee capacity limits;
- shared resource locks;
- non-overlapping recurring runs where required.

Example:
A monthly research report can launch five independent research branches and merge them before review.

---

## 16. Recurring overlap policy

For each recurring workflow specify behavior if the previous occurrence is still running:
- skip new occurrence;
- queue;
- run concurrently;
- merge;
- alert.

Never allow accidental duplicate work due to missing policy.

---

## 17. Human approvals

A workflow can pause for human authorization.

Approval UX should show:
- requested action;
- reason;
- employee requesting;
- evidence;
- consequence;
- deadline;
- approve/reject/modify;
- downstream steps affected.

Only the dependent path should pause.

---

## 18. Workflow testing

Before activation, users should be able to:
- validate configuration;
- run with sample inputs;
- dry-run external side effects where supported;
- inspect expected path;
- confirm MCP/tool connectivity;
- identify missing credentials;
- verify output contracts.

A workflow should have Draft → Test → Active lifecycle.

---

## 19. Workflow versions

Editing an active workflow creates a version.

Historical runs remain linked to the version that actually executed.

Support:
- diff;
- activate new version;
- rollback;
- clone;
- retire.

---

## 20. Workflow templates

Templates should eventually cover common patterns:
- research → write → review → publish;
- monitor → diagnose → notify;
- inbound lead → qualify → CRM → schedule;
- incoming call → receptionist → booking/escalation;
- data fetch → analyze → report;
- software task → implement → test → review;
- monthly reconciliation;
- personal monitor → alert.

Templates must remain editable and not become hardcoded special cases.

---

## 21. Workflow health

Each active workflow should show:
- enabled/paused;
- next run;
- last success;
- last failure;
- recent success rate;
- average duration;
- active run count;
- unresolved issues;
- latest version;
- responsible department/employee;
- recent cost where known.

---

## 22. Calendar examples

### Multiple times per day
Server/Supabase health scan at 08:00, 13:00 and 18:00.

### Monthly
Financial reconciliation on the first business day.

### Daily personal task
Steam/Epic free-game monitor at a chosen local time.

### Event driven
Receptionist workflow starts whenever a supported inbound call event arrives.

### Chained timing
Research completes by 10:00 → writing by 12:00 → human approval before 14:00 → publish at 15:00.

---

## 23. Workflow creation UX principle

The system should make simple workflows simple.

A user should not need to understand:
- queues;
- leases;
- distributed locks;
- event sourcing;
- provider APIs

to create:
"Every morning, check whether there are new free games and tell me."

Those implementation details belong below the product surface.

---

## 24. Advanced users still need control

For advanced workflows expose:
- exact step settings;
- model overrides;
- MCP/tool scopes;
- structured variables;
- conditions;
- retries;
- concurrency;
- timeouts;
- approvals;
- version history;
- logs.

The product should progressively disclose complexity.

---

## 25. Scheduler durability acceptance rule

A schedule is only real if:
- it persists;
- it fires without an open browser;
- missed-run policy is deterministic;
- result history exists;
- duplicates are prevented;
- next run is calculable and visible.


---

<!-- SOURCE MODULE: 04_MEMORY_KNOWLEDGE_LEARNING_AND_IMPROVEMENT.md -->

# 04 — MEMORY, KNOWLEDGE, LEARNING AND IMPROVEMENT

## 1. Individual employee memory is mandatory

A core clarified requirement is that each persistent employee has its own memory system so it can improve at its job.

This must not mean "the current LLM conversation is long."

Employee identity and memory must survive:
- session end;
- provider change;
- model change;
- restart;
- repeated workflow runs.

---

## 2. Memory layers

Use conceptually distinct memory layers.

### Working context
Temporary context for the current run.

### Episodic memory
Relevant history of things the employee did:
- task outcomes;
- prior interactions;
- failures;
- exceptional cases;
- user feedback.

### Learned job memory
Reusable lessons such as:
- preferred formats;
- known pitfalls;
- effective strategies;
- validated customer/business facts;
- recurring edge cases.

### Performance memory
Metrics and evidence about how the employee performs.

### Personal style/config memory
Versioned role-specific preferences that are explicitly allowed.

---

## 3. Knowledge is different from memory

Knowledge represents shared durable information.

Examples:
- company standards;
- infrastructure architecture;
- brand voice;
- customer policy;
- coding standards;
- business rules;
- research library;
- project documentation.

Memory is more directly connected to a worker's history and learned experience.

---

## 4. Knowledge scopes

At minimum:
- Global / Organization;
- Department;
- Project or Workflow;
- Employee.

Retrieval must respect scope and permissions.

---

## 5. Employee-specific improvement

Example:

A Social Copywriter repeatedly receives reviewer feedback that generated posts are too long.

The system can:
1. retain the evidence;
2. identify a repeated pattern;
3. create a learning proposal;
4. propose an update to the employee's prompt/style rule;
5. review the change;
6. activate a new version;
7. compare subsequent results.

It should not silently rewrite critical behavior from one anecdotal failure.

---

## 6. Controlled learning loop

Preferred lifecycle:

Observe
→ collect evidence
→ extract lesson
→ propose change
→ review
→ activate
→ measure
→ retain or roll back.

Learning is deliberate operational improvement, not uncontrolled self-modification.

---

## 7. Learning proposal types

Examples:
- prompt change;
- workflow change;
- model routing change;
- tool/MCP change;
- memory-rule change;
- QA-rule change;
- timeout/retry change;
- report change;
- skill addition;
- job-contract clarification.

---

## 8. Evidence

A lesson should identify:
- source runs;
- source reviews;
- frequency;
- confidence;
- affected employee/workflow;
- observed outcome;
- proposed change.

Avoid unsupported statements such as:
"Model X is bad."

Prefer:
"Across N runs of this task class, route X produced these measurable failure types."

---

## 9. Memory writes should be governed

Not every model output should become permanent memory.

Memory write policy should consider:
- usefulness;
- confidence;
- duplication;
- sensitivity;
- freshness;
- evidence;
- scope;
- retention.

Low-confidence guesses should not silently become organizational facts.

---

## 10. Memory correction

The UI should allow authorized users to:
- inspect important memories;
- correct them;
- mark obsolete;
- delete where policy allows;
- change scope;
- see provenance.

---

## 11. Forgetting and expiry

Some information becomes stale.

Support:
- expiration;
- supersession;
- recency weighting;
- archival;
- manual invalidation.

Example:
A provider API behavior learned nine months ago may no longer be safe to treat as current truth.

---

## 12. Retrieval

A worker should receive relevant memory, not every memory.

Retrieval can consider:
- employee;
- task type;
- workflow;
- entities mentioned;
- recency;
- confidence;
- security scope;
- relevance.

---

## 13. Shared lessons

Some employee lessons should remain employee-specific.

Others can be promoted:
Employee → Department → Organization

only when evidence and policy justify broader application.

---

## 14. Memory privacy

Memory must respect:
- secret boundaries;
- department permissions;
- personal/private data policy;
- external provider privacy policy;
- tool access.

Sensitive data must not be sent to a model route that is not authorized for that data class.

---

## 15. Obsidian / human-readable knowledge

The original product direction includes a human-readable knowledge repository such as Obsidian or compatible storage.

Suitable content:
- architecture decisions;
- standards;
- lessons;
- research;
- project knowledge;
- procedures;
- policies.

Operational workflow state must remain in authoritative structured storage.

---

## 16. Agent performance

Track performance by meaningful dimensions, for example:
- task class;
- success rate;
- review pass rate;
- rework frequency;
- error categories;
- latency;
- cost;
- model route;
- tool reliability;
- user feedback.

Avoid a single simplistic "employee score" unless the formula and population are meaningful.

---

## 17. Model learning

The system may learn that different models work better for different tasks.

Example:
- one model performs better at research;
- one is faster at simple extraction;
- one is better at code review;
- one is cheaper for high-volume classification.

Routing improvements should be evidence-driven.

---

## 18. User feedback

User feedback should be able to attach to:
- employee;
- output;
- workflow run;
- report;
- review;
- memory;
- workflow version.

Feedback can become evidence for future learning proposals.

---

## 19. Learning Analyst role

A department may have a Learning Analyst employee responsible for:
- reviewing completed work;
- identifying repeated defects;
- summarizing lessons;
- comparing model performance;
- proposing prompt/workflow/tool changes;
- maintaining useful knowledge;
- reviewing whether improvements actually helped.

The Learning Analyst does not bypass governance.

---

## 20. Memory acceptance criteria

A persistent employee should be demonstrably able to:
1. perform a task;
2. retain an approved useful lesson;
3. end the model session;
4. change/restart runtime;
5. perform a later related task;
6. retrieve the relevant lesson;
7. use it appropriately;
8. expose provenance/history to the user.


---

<!-- SOURCE MODULE: 05_MODELS_MCPS_TOOLS_AND_CAPABILITIES.md -->

# 05 — MODELS, MCPs, TOOLS AND CAPABILITIES

## 1. The product must be model-agnostic

Different LLMs are appropriate for different jobs.

The system must not assume one model or one provider powers every employee.

An employee can have:
- default model;
- permitted alternatives;
- task-class preferences;
- fallback policy;
- speed/quality/cost preference;
- context requirements;
- multimodal requirement;
- privacy restrictions.

The user's examples include using a research-oriented system such as Perplexity for research work and a fast model such as ByteDance Seed 2.0 mini for latency-sensitive work. These examples illustrate the routing principle; actual runtime availability must remain configurable.

---

## 2. Model policy levels

Model policy may exist at:
- organization default;
- department default;
- employee default;
- workflow step override;
- emergency/fallback rule.

More specific policy can override broader policy subject to permissions and cost/security constraints.

---

## 3. Requested vs effective model

Record separately:
- requested model;
- actual/effective model where provider exposes it;
- provider;
- route type;
- latency;
- tokens;
- reported cost;
- fallback reason.

Do not display configured model as verified actual model when the provider does not reveal it.

---

## 4. Routing factors

Model selection can consider:
- task type;
- expected reasoning difficulty;
- speed target;
- context size;
- image/audio requirements;
- tool calling;
- structured output;
- privacy;
- current provider health;
- cost;
- quota;
- prior performance on that task class.

---

## 5. Employees are not tied permanently to models

Changing a backing model must not erase:
- employee identity;
- memory;
- job history;
- performance;
- workflow membership;
- permissions;
- appearance.

The model is a capability implementation detail behind the employee.

---

## 6. MCP is a core capability system

MCP access is a major product requirement.

Each employee should have a deliberate capability set rather than global access.

The product needs an MCP registry that shows:
- MCP server/integration name;
- purpose;
- connection state;
- available tools/capabilities;
- required credentials;
- scopes;
- data sensitivity;
- rate limits if known;
- employees allowed to use it;
- workflows using it;
- recent failures;
- audit history.

---

## 7. Per-employee MCP permissions

Example:
- Infrastructure Health Bot can use server-monitoring and Supabase MCP.
- Social Publisher can use social-platform MCP.
- Researcher can use web/research tools but not production database mutation.
- Receptionist can use telephony, CRM and calendar.
- Developer can use repository and test tools.
- Finance employee can access finance systems under stricter approval rules.

There should be no assumption that all bots receive all integrations.

---

## 8. Tool permission states

For each employee/tool:
- Allowed;
- Denied;
- Approval required;
- Allowed read-only;
- Allowed only in specific workflow;
- Allowed only for selected resources.

Server-side enforcement is required.

---

## 9. Integration types

The platform should be capable of integrating with categories such as:
- web/search;
- browser;
- email;
- calendar;
- CRM;
- telephony/voice;
- messaging;
- social media;
- file storage;
- Git/code repositories;
- databases;
- Supabase;
- servers/SSH/monitoring;
- analytics;
- finance/accounting;
- ecommerce;
- project management;
- custom APIs.

This is an extensibility contract, not a requirement to ship every connector on day one.

---

## 10. Voice and receptionist capability

A receptionist employee may need:
- inbound voice connection;
- realtime conversational model;
- speech-to-text;
- text-to-speech;
- call-state management;
- CRM lookup/update;
- calendar access;
- transfer/escalation;
- call summary;
- consent/compliance controls;
- after-call workflow.

Voice agents should still participate in the same employee/workflow/memory/reporting model.

---

## 11. Tool execution provenance

Every meaningful side effect should record:
- employee;
- workflow/run;
- tool/MCP;
- action;
- target resource;
- timestamp;
- result;
- approval reference where required.

Sensitive raw payloads can be redacted in user-facing views while audit identity remains.

---

## 12. Credentials

Credentials belong in a secure secret mechanism.

They must not be:
- copied into prompts;
- stored in plain logs;
- embedded in employee memory;
- rendered in screenshots;
- committed to Git.

Employees should receive scoped capability, not raw secret disclosure.

---

## 13. Connection health

Integrations should expose:
- connected/disconnected;
- authentication expired;
- permission error;
- rate limited;
- unavailable;
- last successful use.

A workflow should fail clearly when a required integration is unavailable.

---

## 14. Tool schemas and validation

Tool calls should use explicit schemas where available.

Untrusted model text should not be directly turned into privileged shell/API actions without validation.

For high-impact operations:
model intent
→ structured action proposal
→ schema validation
→ policy check
→ approval where required
→ deterministic execution
→ audit record.

---

## 15. Deterministic tools before LLM calls

If a task can be solved reliably by deterministic code, the product should not require an LLM merely for aesthetic consistency.

Examples:
- checking a numeric threshold;
- parsing known JSON;
- comparing timestamps;
- executing a safe predefined query;
- scheduling;
- retry/backoff;
- deduplication.

LLMs should be used where semantic judgment or generation adds value.

---

## 16. Skills

Reusable multi-step tool techniques can become Skills.

A skill might package:
- instructions;
- tools;
- schemas;
- examples;
- safety rules;
- tests.

Skills can be assigned to selected employees.

---

## 17. Capability discovery UX

From an employee dossier the user should be able to answer:
- What can this employee access?
- What can it change?
- Which MCPs are connected?
- Which model will it normally use?
- What requires approval?
- Which workflows rely on it?

---

## 18. Cost controls

Allow:
- per-run budget;
- workflow budget;
- department budget;
- organization budget;
- model class restrictions;
- no-paid-route policy where desired.

If actual provider cost is unknown, display unknown rather than fabricate.

---

## 19. Provider failure

A provider outage should not erase work.

A step can become:
- waiting provider;
- retry scheduled;
- rerouted to approved fallback;
- escalated.

Fallback must respect:
- privacy;
- cost;
- capability;
- user policy.

---

## 20. Open-source / reuse-first tool doctrine

The user strongly prefers mature open-source or already-tested infrastructure over writing generic plumbing from scratch.

Therefore:
- inspect Hermes built-ins first;
- evaluate existing workflow/orchestration/scheduling components;
- reuse mature libraries and engines where they satisfy the contract;
- wrap external engines behind Empirium's domain model;
- do not let a third-party engine become the user-facing product identity;
- do not custom-build generic schedulers, retry engines, queue systems or MCP plumbing merely because custom code is possible.

Integration quality is preferable to reinvention when product requirements remain intact.


---

<!-- SOURCE MODULE: 06_UI_UX_LIVING_OFFICE_AND_INFORMATION_ARCHITECTURE.md -->

# 06 — UI/UX, LIVING OFFICE AND INFORMATION ARCHITECTURE

## 1. Design objective

The interface should feel like a **premium operational command center for an AI organization**, not a developer console and not a toy.

The living-office metaphor should make the system intuitive while every important state remains available as normal text/data UI.

---

## 2. Visual direction from supplied mockups

Preserve:
- dark navy background;
- clean luminous blue/cyan highlights;
- controlled accent colors for departments/status;
- crisp cards and borders;
- strong typography hierarchy;
- high information density;
- large central office imagery;
- character/bot identity;
- real-time status chips;
- modern technical office environments;
- side navigation and tabbed local navigation;
- premium polished feel.

Avoid:
- excessive clutter;
- unreadably tiny metrics;
- too many bots overlapping;
- decorative values that look real but are fabricated.

The user specifically preferred offices with roughly **3–7 visible bots per room** so individual workers remain legible. Larger departments can use multiple rooms, scrolling, floors, tabs, zoom states or summarized workers rather than cramming every employee into one scene.

---

## 3. Global information architecture

Recommended global areas:

- Home / Organization Overview;
- Departments;
- Workflows;
- Calendar / Schedules;
- Projects;
- Tasks / Runs;
- Employees / Agents;
- Approvals;
- Knowledge;
- MCPs & Tools / Integrations;
- Models & Costs;
- Learning;
- QA & Review;
- Reports / Analytics;
- Activity / History;
- Settings.

The exact navigation can be refined, but workflow and schedule/calendar surfaces must not disappear behind developer-only menus.

---

## 4. Organization Overview

Purpose: understand the whole workforce at a glance.

Show:
- organization identity;
- operational status;
- active employees;
- active workflows/runs;
- projects;
- approvals requiring attention;
- scheduled work;
- significant alerts;
- model/cost summary;
- department cards;
- recent activity;
- recent improvements.

Department cards can include:
- name;
- purpose;
- status;
- number of employees;
- current work;
- next scheduled work;
- recent quality indicator;
- miniature office view;
- alert badge.

Clicking opens the department.

---

## 5. Department Overview / Cockpit

The department cockpit is the central operational surface.

Header:
- department name;
- purpose;
- status;
- motto/description;
- alert state;
- New Work / New Project;
- New Workflow;
- Ask/Open Director;
- pause/maintenance control where appropriate.

Primary visual anchor:
- living office.

Supporting panels:
- Active Work;
- Today's / Upcoming Scheduled Work;
- Completed Recently;
- Workflow Health;
- Current Activity;
- QA;
- Approvals;
- Knowledge;
- Learning;
- Models/Cost;
- Alerts.

---

## 6. Department tabs

The original mockups include:
Overview, Projects, Tasks, Agents, QA, Knowledge, Learning, History, Models & Cost, Settings.

The clarified product requires adding/ensuring first-class access to:
- Workflows;
- Schedules / Calendar;
- Reports;
- Integrations / Tools where department-scoped.

A suitable final arrangement can group some functions, but none should be functionally omitted.

---

## 7. Living office

The office is an **operational visualization**.

It may contain ambient personality, but operational animation must be truthful.

A canonical state adapter should map real state to visuals.

Candidate states:
- Offline;
- Idle;
- Queued;
- Planning;
- Thinking;
- Researching;
- Coding/Building;
- Tool Use;
- Calling;
- Writing;
- Testing;
- Reviewing;
- Learning;
- Waiting Dependency;
- Waiting Time;
- Waiting Approval;
- Waiting Provider;
- Rate Limited;
- Handoff;
- Blocked;
- Error;
- Crashed;
- Completed.

---

## 8. Office behavior examples

If an employee is researching:
- move to research desk/tablet/board;
- show "Researching";
- status detail links to current run.

If testing:
- QA station/checklist/console.

If on a call:
- headset/phone animation;
- current call status visible subject to privacy.

If waiting approval:
- attention indicator;
- potentially move to attention area;
- clicking opens approval.

If rate limited:
- waiting/timer state;
- not a dramatic crash animation.

If work completes:
- brief celebration;
- return to current real state.

---

## 9. Ambient animation vs operational animation

Ambient:
- blink;
- small movement;
- bounded wander;
- stretch;
- glance around.

Operational:
- typing;
- research;
- call;
- QA;
- handoff;
- approval request;
- failure;
- recovery.

Ambient can be stochastic.
Operational cannot lie.

---

## 10. Employee interaction

Click an employee to open a dossier.

At a glance show:
- name;
- role;
- department;
- current state;
- why;
- current workflow/project;
- current task;
- current run;
- model/provider;
- tool/MCP activity;
- elapsed time;
- latest event.

Deeper sections:
- job description;
- memory;
- skills;
- tools/MCPs;
- model policy;
- permissions;
- workflows;
- schedule;
- history;
- QA;
- performance;
- costs;
- learning;
- configuration versions.

---

## 11. Workflow Builder page

Major end-user page.

Should include:
- workflow name/purpose;
- status/version;
- trigger;
- visual step graph;
- step inspector;
- employee assignment;
- model override;
- MCP/tool permissions;
- input/output mapping;
- rules/conditions;
- retries/timeouts;
- approval gates;
- schedule;
- test button;
- activation;
- history;
- run list.

The visual design should remain approachable enough for a non-developer.

---

## 12. Calendar / Schedule page

Views:
- Day;
- Week;
- Month;
- Agenda;
- recurring routines list.

Show:
- scheduled workflow occurrences;
- deadlines;
- human appointments;
- approval deadlines;
- bot workload;
- next run;
- status.

Actions:
- run now;
- reschedule occurrence;
- pause;
- edit recurrence;
- inspect workflow;
- inspect previous occurrences.

---

## 13. Workflow Runs page

Provide an execution timeline:
Trigger
→ Step 1
→ Handoff
→ Step 2
→ Approval
→ Step 3
→ Completion.

Each node shows:
- status;
- employee;
- start/end;
- model;
- tools;
- artifacts;
- errors/retries;
- evidence.

---

## 14. Activity feed

Surface meaningful events, not every token/tool packet.

Examples:
- workflow started;
- scheduled job completed;
- employee handed work off;
- QA rejected output;
- approval requested;
- provider rate limited;
- employee recovered;
- call booked meeting;
- server check found issue;
- workflow version activated.

Allow filtering and drill-down.

---

## 15. Approvals inbox

Dedicated page for human attention.

Group by:
- urgent;
- due soon;
- department;
- risk type.

Each approval card includes:
- requested action;
- requester;
- workflow;
- reason;
- evidence;
- effect;
- approve/reject/modify.

---

## 16. Reports / Analytics

Show:
- workflow success;
- recurring-job health;
- employee performance;
- QA;
- cost/usage;
- time;
- failures;
- model performance by task class;
- department trends.

Do not invent percentages without formulas.

---

## 17. Integrations / MCP UI

Global registry and employee assignment UX.

The user should be able to:
- connect integration;
- see connection status;
- inspect exposed capabilities;
- grant access to selected employees;
- set read/write/approval scope;
- see which workflows depend on it;
- test connection;
- revoke access.

---

## 18. Models & Cost page

Support:
- provider registry;
- model registry;
- employee routing;
- task-class routing;
- usage history;
- tokens;
- reported cost;
- unknown cost;
- fallback events;
- provider health.

The page should help the user understand why a model was used.

---

## 19. Knowledge UI

Browse by:
- organization;
- department;
- employee;
- project/workflow.

Support:
- source/provenance;
- search;
- freshness;
- version/history;
- linked runs.

---

## 20. Learning UI

Show:
- learning proposals;
- evidence;
- affected employee/workflow;
- current vs proposed behavior;
- expected benefit;
- approval/review;
- activated changes;
- measured result;
- rollback.

---

## 21. Responsive design

Desktop:
- full living office and dense panels.

Tablet:
- compact office plus operational cards.

Mobile:
- status, tasks, approvals, employee details, alerts, runs, calendar.
- full office animation can be reduced.

Operational functionality cannot depend on the large desktop scene.

---

## 22. Accessibility

Every status represented visually in the office must have textual/semantic equivalent.

Support:
- keyboard navigation;
- visible focus;
- accessible buttons/links;
- text status, not color only;
- reduced motion;
- screen-reader employee list;
- adequate contrast.

---

## 23. Truthful metrics

Mockup values such as "96% health" are illustrative.

Every production metric requires:
- source;
- formula;
- time window;
- freshness;
- fallback.

Unknown must display as unknown.

---

## 24. Search

Global search should eventually find:
- departments;
- employees;
- workflows;
- projects;
- tasks/runs;
- knowledge;
- reports;
- integrations;
- history.

---

## 25. Empty state

Fresh install may have only one department.

Do not populate fake departments or fake active work to make the dashboard look full.

---

## 26. Alerts

Distinguish:
- informational;
- warning;
- action required;
- critical.

Avoid alert fatigue.

---

## 27. Office performance

The living office must be lightweight.

Mini-office cards should use static/throttled rendering rather than running full independent simulations.

When offscreen:
- pause or significantly throttle animation.

---

## 28. Aesthetic objective

The application should feel like:
- a premium SaaS operations suite;
- an approachable AI company;
- a coherent world of workers;
- a professional control system.

Not:
- a children's game;
- a generic admin template;
- a developer debug page;
- a noisy "agent swarm" visualization.


---

<!-- SOURCE MODULE: 07_REPORTING_OBSERVABILITY_QA_AND_APPROVALS.md -->

# 07 — REPORTING, OBSERVABILITY, QA AND APPROVALS

## 1. "Report everything" is a core requirement

The user should be able to understand:
- what was supposed to happen;
- what actually happened;
- who/what performed it;
- when;
- with which model;
- with which tools/MCPs;
- what was produced;
- what failed;
- what was retried;
- what was handed off;
- what required approval;
- what the next action is.

The product must support both live monitoring and historical audit.

---

## 2. Observability levels

### Organization
Overall workload, status, alerts, costs, approvals.

### Department
Workflows, routines, employees, current activity, quality.

### Workflow
Definition, schedule, versions, health, run history.

### Workflow Run
Step-by-step execution timeline.

### Employee
Current state, task history, performance, tools/models, memory/learning.

### Task / Run
Logs, tool use, artifacts, errors, tokens, costs, evidence.

---

## 3. Event taxonomy

Use structured meaningful events such as:
- WORKFLOW_SCHEDULED;
- WORKFLOW_STARTED;
- STEP_READY;
- TASK_ASSIGNED;
- RUN_STARTED;
- TOOL_CALLED;
- TOOL_FAILED;
- HANDOFF_CREATED;
- REVIEW_REQUESTED;
- REVIEW_REJECTED;
- APPROVAL_REQUESTED;
- APPROVAL_GRANTED;
- PROVIDER_RATE_LIMITED;
- RETRY_SCHEDULED;
- RUN_FAILED;
- RUN_RECOVERED;
- WORKFLOW_COMPLETED;
- REPORT_CREATED;
- LEARNING_PROPOSED;
- CONFIG_VERSION_ACTIVATED.

Exact names can differ, but semantics must be consistent.

---

## 4. Run timeline

Each run should render as an intelligible timeline.

The user should not need to inspect raw logs to understand the main story.

Offer raw technical detail as drill-down.

---

## 5. Reports

Potential report types:

### Daily digest
What ran, what completed, what failed, what needs attention.

### Department report
Work completed, upcoming work, quality, failures, cost.

### Workflow health report
Success rate, duration, recent changes, error classes.

### Employee performance report
Job-class outcomes, QA, retries, latency, cost.

### Model report
Usage and outcome by task class.

### Monthly operations report
Trends, improvements, repeated issues, upcoming routines.

---

## 6. User notifications

The system should notify the user when:
- action/approval is needed;
- meaningful failure persists;
- a monitored condition is important;
- a requested result is ready;
- a workflow is repeatedly degrading;
- a personal alert condition is met.

Routine success need not generate noisy push alerts if it is already visible in reports, unless user requests it.

---

## 7. Example: free-game workflow report

A completed run might say:

- Checked Epic Games Store source at 08:00.
- Checked Steam source at 08:02.
- Found N qualifying free items.
- Deduplicated against previously reported items.
- Notification created with title, store, claim-by time and source link.
- Next run tomorrow at 08:00.

If nothing is found:
- record successful "no match" outcome;
- avoid treating it as failure.

---

## 8. Example: infrastructure report

- Checked server CPU/memory/disk.
- Queried application health.
- Queried Supabase health/configured diagnostics.
- Detected issue X.
- Diagnostics run by Infrastructure Analyst.
- Restart not attempted because approval policy requires human authorization.
- Approval created.
- Other unrelated checks completed.

---

## 9. QA

Some workflows need independent review.

Examples:
- software changes;
- external publication;
- high-stakes research;
- financial outputs;
- important customer-facing content.

QA should be configurable by workflow/step risk.

---

## 10. Independent review

Where independence matters:
- reviewer is not the same run that produced the output;
- reviewer sees acceptance criteria;
- review targets exact artifact/version;
- defects are recorded;
- rejected work returns for rework;
- approval is linked to specific revision.

---

## 11. QA is not always mandatory

A daily low-risk free-game monitor does not need a heavyweight code-review process on every occurrence.

The product should allow risk-appropriate validation:
- schema check;
- deterministic validation;
- second model;
- human review;
- no review.

---

## 12. Human approval vs QA

Keep separate:

**QA**
"Is this output correct/good enough?"

**Approval**
"May the system take this consequential action?"

An output may pass QA and still require human approval to publish/delete/spend/restart.

---

## 13. Evidence

Important operations should link evidence:
- logs;
- screenshots;
- API responses;
- source links;
- database records;
- Git SHA;
- artifacts;
- review verdicts.

Evidence should correspond to the actual run/revision.

---

## 14. Audit trail

Record significant configuration changes:
- employee prompt/model/tool;
- workflow version;
- permissions;
- schedules;
- approvals;
- memory corrections;
- integration changes.

Audit should identify who/what changed it and when.

---

## 15. Status reasons

Do not show only:
"Blocked."

Show:
- Waiting for user approval to restart production service.
- Waiting for calendar availability.
- Provider rate-limited until retry window.
- Required MCP connection expired.
- Waiting for Researcher's artifact.

---

## 16. Cost and usage

Where available record:
- provider;
- requested/effective model;
- input/output/cache tokens;
- cost;
- subscription/free/paid/unknown class.

Attribute usage to:
Organization → Department → Employee → Workflow/Project → Task → Run.

---

## 17. Metrics must have formulas

Examples:

### Workflow success rate
successful terminal runs / terminal runs during time window.

### First-pass review rate
work accepted without rework / reviewed work.

### Employee active
has actual current execution or recently confirmed runtime activity, not merely configured.

### Project progress
derived from task/milestone state.

Avoid decorative "health 96%" without a defined meaning.

---

## 18. Staleness

When telemetry is stale:
- say so;
- show last successful update;
- do not silently continue displaying it as live.

---

## 19. Data retention

Retention can vary by:
- raw logs;
- summaries;
- artifacts;
- tool payloads;
- calls/audio;
- memories;
- compliance needs.

User-facing reports should remain useful even if low-level logs expire.

---

## 20. Completion

A workflow is not complete merely because no process is running.

Completion requires its defined terminal state and success/acceptance conditions.

The product must distinguish:
- completed successfully;
- completed with warning;
- no result/match;
- failed;
- cancelled;
- waiting;
- partially completed.


---

<!-- SOURCE MODULE: 08_ARCHITECTURE_REUSE_AND_HERMES_INTEGRATION.md -->

# 08 — ARCHITECTURE, REUSE AND HERMES INTEGRATION

## 1. Architecture objective

Build the product as a stable domain/control layer above swappable execution engines.

Empirium should own:
- organization;
- departments;
- employees;
- workflows;
- schedules;
- permissions;
- memory;
- learning;
- reporting;
- product state;
- product UI.

Execution engines can help perform work but should not redefine those product concepts.

---

## 2. Recommended logical layers

### Layer 1 — Product UI
Organization, departments, living office, workflow builder, calendar, reports.

### Layer 2 — Product domain
Employees, workflows, tasks, runs, approvals, artifacts, knowledge.

### Layer 3 — Workflow/scheduling control
Triggers, timers, dependencies, state transitions, retries, concurrency.

### Layer 4 — Agent runtime
Model invocation, context assembly, agent sessions, voice agents.

### Layer 5 — Tools/integrations
MCPs, APIs, browser, DB, telephony, servers.

### Layer 6 — Memory/knowledge/learning
Retrieval, retention, proposals, versions.

### Layer 7 — Observability/event layer
Events, logs, activity, costs, audit.

### Layer 8 — Durable persistence
Canonical database/state.

---

## 3. Hermes relationship

Hermes/Hermes Studio is an important existing substrate and should be audited for reuse.

Potential reusable concepts include:
- profiles;
- durable task/Kanban primitives;
- dispatcher;
- crews;
- Conductor;
- goal mode;
- tool integration;
- MCP support;
- model routing;
- session management.

Do not assume every Hermes concept maps one-to-one to the product.

Examples:
- Hermes Profile can back Employee, but Profile ≠ Employee.
- Crew can group workers, but Crew ≠ Department.
- Kanban card can back Task, but Card ≠ Project.
- Conductor can coordinate bounded work, but Conductor mission ≠ persistent organization.

---

## 4. Reuse-first engineering doctrine

The user explicitly prefers using mature open-source/tested software to rebuilding generic systems from scratch.

Before implementing a generic subsystem:
1. inspect Hermes built-ins;
2. inspect already-installed tools;
3. evaluate mature open-source components;
4. evaluate the third-party orchestrator options already discussed by the user;
5. compare against the exact product contract;
6. integrate if fit is strong;
7. custom-build only the missing product-specific layer.

This is especially important for:
- workflow orchestration;
- durable scheduling/timers;
- queueing;
- retries;
- job leases;
- event handling;
- MCP connectivity;
- secrets;
- observability;
- browser automation.

---

## 5. External orchestration engine evaluation contract

Any external orchestrator should be assessed for:

### Durability
Can work survive process/browser restart?

### Scheduling
Recurring schedules, delayed jobs, timers, missed-run policy.

### State
Explicit durable workflow state.

### Dependencies
DAG/graph support or equivalent.

### Handoffs
Structured data between steps.

### Retries
Configurable backoff and error classification.

### Idempotency
Protection from duplicate external actions.

### Human-in-the-loop
Pause/resume/approval.

### Long-running work
Hours/days/months without relying on one model context.

### Dynamic routing
Different worker/model/tool per step.

### Observability
Run history and events.

### Self-hostability / control
Where required by product policy.

### Licensing
Compatible with intended use.

### Extensibility
Can Empirium domain IDs and metadata be attached?

### MCP/tool interoperability
Does not block per-agent capabilities.

If an engine is strong on generic workflow mechanics, Empirium should wrap it rather than copy it.

---

## 6. Do not let the orchestrator become the product

The user experience should remain Empirium's.

A backend engine can own technical execution primitives while Empirium owns:
- employee identity;
- department meaning;
- workflow design;
- memory;
- reports;
- UI;
- policies.

This reduces vendor/engine lock-in.

---

## 7. One canonical authority per mutable state

Avoid two systems both writing the same truth.

For each entity determine:
- canonical store;
- creator;
- updater;
- projections;
- recovery behavior.

Especially:
- workflow definition;
- run state;
- task state;
- employee config;
- schedule;
- approval;
- memory;
- event history.

---

## 8. Durable execution

No critical workflow should depend on:
- one browser tab;
- one chat context;
- one long-running LLM response;
- one process remaining alive indefinitely.

Use persistent state and reconstructable execution.

---

## 9. Deterministic control vs LLM judgment

Deterministic code should own:
- schedule firing;
- lease/claim;
- retry counters;
- timeouts;
- state transitions;
- permission checks;
- idempotency;
- budget enforcement;
- schema validation.

LLMs should own:
- semantic interpretation;
- generation;
- planning within policy;
- classification where deterministic rules are insufficient;
- research/reasoning.

---

## 10. Event system

Use a canonical semantic event layer so:
- activity feed;
- living office;
- reports;
- alerts

do not independently invent state.

Example:
provider rate-limit event
→ task state
→ employee visible state
→ activity feed
→ retry scheduler
→ run history.

---

## 11. Persistence

Operational state should be stored in durable structured storage.

Human-readable knowledge repositories are complementary, not authoritative for workflow status.

The system must be able to reconstruct after restart:
- employees;
- workflow definitions;
- schedules;
- queued work;
- active/waiting runs;
- approvals;
- history;
- memory;
- model/tool policy.

---

## 12. Idempotency

Recurring/event workflows can be triggered more than once.

Use stable identifiers and idempotency keys where applicable.

Examples:
- webhook event ID;
- schedule occurrence ID;
- email message ID;
- call ID.

---

## 13. Recovery

Expected recoverable failures include:
- worker crash;
- model timeout;
- provider 429;
- tool failure;
- integration authentication expiry;
- gateway restart;
- app restart;
- network outage;
- review rejection.

These should create states and recovery actions, not silently abandon work.

---

## 14. Build-time workforce vs product workforce

Do not confuse:
- the temporary orchestrators/workers being used to build Empirium;
with
- the permanent employees that Empirium's users will configure and operate.

Build tools can inspire architecture, but product employees have their own stable domain identity.

---

## 15. Open interfaces

Prefer adapters for:
- model providers;
- MCP servers;
- workflow engine;
- voice provider;
- scheduler;
- database;
- notification provider.

This supports future replacement.

---

## 16. Security boundary

The orchestration engine must not bypass Empirium permission policy.

A step cannot gain capability merely because the underlying engine technically supports it.

---

## 17. Performance

The UI should subscribe to summarized semantic state, not stream every low-level token/tool event into every component.

Use:
- event aggregation;
- pagination;
- bounded histories;
- offscreen throttling;
- selective subscriptions.

---

## 18. Architecture success test

The architecture is sound when an employee can:
- keep the same ID and memory;
- change model provider;
- change execution engine/profile;
- remain assigned to the same workflows;
- preserve history;
- preserve permissions;
- continue to appear as the same employee.

That proves the product model is above the runtime implementation.


---

<!-- SOURCE MODULE: 09_REFERENCE_DEPARTMENTS_AND_END_TO_END_WORKFLOWS.md -->

# 09 — REFERENCE DEPARTMENTS AND END-TO-END WORKFLOWS

These examples are not intended to hardcode the product. They clarify the flexibility required.

---

# A. PERSONAL SOFTWARE DEPARTMENT

## Purpose
Build, maintain and improve the user's software systems.

## Example permanent employees
- Director;
- Research Architect;
- Developer / Implementation Engineer;
- QA Engineer;
- Learning Analyst;
- optional Designer;
- optional Documentation Specialist;
- optional DevOps specialist.

## Example project flow
User: "Build a small mobile productivity app."

Director
→ creates durable Project
→ requests architecture/research
→ Research Architect creates plan
→ Developer implements bounded tasks
→ QA validates
→ rejected work goes back to Developer
→ accepted work integrates
→ Documentation worker records changes
→ Learning Analyst extracts evidence-backed lessons
→ final report to user.

The user can close the browser while work continues.

---

# B. MARKETING & CONTENT DEPARTMENT

## Purpose
Produce, review, publish and analyze marketing.

## Employees
- Trend Researcher;
- Content Strategist;
- Copywriter;
- Designer / Creative Generator;
- SEO Specialist;
- Reviewer;
- Publisher;
- Analytics Analyst.

## Recurring workflow
Every weekday:
1. Researcher collects relevant topics.
2. Strategist chooses suitable content.
3. Copywriter drafts.
4. Reviewer checks brand/risk.
5. Creative step prepares assets.
6. Human approval if configured.
7. Publisher schedules social content.
8. Analyst later gathers performance.
9. Learning proposal adjusts future strategy.

Each employee may use different models and different MCPs.

---

# C. INFRASTRUCTURE DEPARTMENT

## Purpose
Monitor and maintain servers, databases and services.

## Employees
- Health Monitor;
- Infrastructure Analyst;
- Database/Supabase Analyst;
- Incident Responder;
- Change Reviewer.

## Scheduled workflow
At 08:00, 13:00 and 18:00:
1. Monitor queries permitted health sources.
2. Deterministic threshold checks run.
3. If healthy: record success.
4. If degraded: Analyst diagnoses.
5. If safe read-only repair exists: execute according to policy.
6. If restart/destructive action is required: create approval.
7. Incident summary is produced.
8. Repeated failures become learning/maintenance proposal.

The visible office should show workers checking systems when the run is active.

---

# D. AI RECEPTION / CUSTOMER SERVICE DEPARTMENT

## Purpose
Handle incoming calls and customer contact.

## Employees
- Realtime Receptionist;
- Qualification Agent;
- Booking Agent;
- CRM Administrator;
- Escalation Coordinator;
- QA/Call Reviewer.

## Inbound call flow
Call event
→ Receptionist answers
→ identifies intent
→ retrieves permitted CRM context
→ handles routine request
→ if appointment needed, checks calendar
→ books slot
→ updates CRM
→ produces call summary
→ if specialist required, creates handoff or transfer
→ QA samples/reviews according to policy
→ memory/knowledge updated only under governed rules.

This proves employees can be realtime voice systems, not just background text LLMs.

---

# E. PERSONAL DEPARTMENT — FREE-GAME MONITOR

## Purpose
Simple personal automation.

## Employee
Deals / Freebie Monitor.

## Daily workflow
1. Schedule fires once per day.
2. Employee checks configured Epic Games Store source.
3. Checks configured Steam source.
4. Normalizes candidates.
5. Determines which qualify as free according to workflow rule.
6. Deduplicates items already reported.
7. If matches exist, sends concise alert.
8. If none exist, records successful no-match result.
9. Updates next-run state.

## Report contents
- store;
- game/item name;
- current free status;
- claim-by time where known;
- source link;
- date checked.

This is intentionally small. The platform should not require a complex project ceremony for it.

---

# F. RESEARCH DEPARTMENT

## Purpose
Perform recurring and project research.

## Employees
- Source Finder;
- Research Analyst;
- Fact Checker;
- Synthesizer;
- Research Librarian.

## Workflow
Question/topic
→ Source Finder
→ Analyst
→ Fact Checker
→ Synthesizer
→ Knowledge repository
→ report.

A research-oriented model may be preferred for some steps; other models can handle synthesis.

---

# G. BUSINESS & GROWTH DEPARTMENT

## Purpose
Leads, sales operations and commercial work.

## Example lead workflow
Lead arrives
→ Enrichment employee
→ Qualification employee
→ Research employee
→ Outreach drafter
→ approval if required
→ sending tool
→ CRM update
→ follow-up schedule
→ reporting.

Permissions prevent research employees from sending emails simply because they can see the lead.

---

# H. FINANCE DEPARTMENT

## Purpose
Routine analysis, reconciliation and reporting.

## Monthly workflow
Schedule on first business day
→ gather permitted data
→ deterministic reconciliation
→ Finance Analyst investigates exceptions
→ Reviewer validates
→ user approval for consequential actions
→ monthly report.

High-risk money movement is not automatically authorized by the existence of the workflow.

---

# I. CROSS-DEPARTMENT CAMPAIGN

Business identifies target
→ Research validates market
→ Marketing develops campaign
→ Finance validates budget
→ user approves spend
→ Marketing publishes
→ Analytics tracks performance
→ Learning proposes improvement.

The product must support handoffs across department boundaries.

---

# J. SOFTWARE + INFRASTRUCTURE INCIDENT

Monitoring detects app error
→ Infrastructure diagnoses
→ determines code defect
→ creates Personal Software task
→ Developer fixes
→ QA reviews
→ deploy approval requested
→ deployment executes
→ Infrastructure verifies health
→ incident report closes.

This illustrates workflows that dynamically create work in another department.

---

## Reference principle

Departments and employee roles are templates, not hardcoded ceilings.

A user should be able to create:
- a new department;
- new specialized employees;
- new workflows;
- new tools;
- new schedules;
without editing product source code.


---

<!-- SOURCE MODULE: 10_ACCEPTANCE_CRITERIA_AND_PRODUCT_TESTS.md -->

# 10 — ACCEPTANCE CRITERIA AND PRODUCT TESTS

This document defines product-level proofs. Exact automated test implementation can vary.

---

## AC-001 — Persistent employee identity
Create employee → run work → restart relevant services → employee keeps same ID, config, memory references and history.

## AC-002 — Model replacement
Change an employee's backing model → later runs use new route → employee identity/history remains continuous.

## AC-003 — Per-agent MCP access
Give Employee A an MCP and deny Employee B → A can use allowed capability → B is denied server-side.

## AC-004 — Recurring daily schedule
Create daily routine → close browser → schedule fires → run history appears on return.

## AC-005 — Multiple-times-per-day schedule
Create three daily occurrences → verify each has distinct occurrence/run identity and no accidental duplicate.

## AC-006 — Monthly schedule
Create first-business-day job → verify next occurrence calculation and persistence.

## AC-007 — Missed-run handling
Stop runtime through scheduled time → restart → configured missed-run policy is followed exactly.

## AC-008 — Workflow handoff
Employee A produces artifact → structured handoff to B → B receives correct artifact/context without manual copying.

## AC-009 — Handoff provenance
Open B's run → trace source back to A's exact artifact/run.

## AC-010 — Branch condition
Workflow takes correct deterministic branch based on validated condition.

## AC-011 — Parallel work
Two independent steps run concurrently → join waits correctly.

## AC-012 — Retry
Inject transient error → retry occurs according to policy → prior attempt remains visible.

## AC-013 — Idempotent external action
Force retry after side-effect boundary → system prevents duplicate external action.

## AC-014 — Approval
Workflow requests risky action → only dependent step pauses → unrelated work continues → action cannot execute before approval.

## AC-015 — Rejection
Reject approval → workflow follows configured rejection path.

## AC-016 — QA rework
Reviewer rejects artifact → task returns to appropriate employee with defects → new attempt links to review.

## AC-017 — Personal memory
Employee learns approved job-specific lesson → later related run retrieves and uses it.

## AC-018 — Memory survives restart
Restart runtime after learning → memory remains retrievable.

## AC-019 — Memory isolation
Employee A private memory is not automatically exposed to Employee B.

## AC-020 — Department knowledge sharing
Approved department knowledge is retrievable by authorized department employees.

## AC-021 — Learning proposal governance
Learning Analyst proposes prompt/tool/workflow change → critical change does not activate without required review/approval.

## AC-022 — Workflow versioning
Run old workflow version → edit/activate new version → old run remains linked to old definition.

## AC-023 — Workflow rollback
Rollback active definition → next run uses restored version.

## AC-024 — Calendar
Upcoming scheduled jobs appear at correct local time and recurrence.

## AC-025 — Browser independence
Start real work → close browser → work continues → reopen → state/history reconstructs.

## AC-026 — Worker crash
Kill worker process → task remains durable → replacement can retry/continue.

## AC-027 — Provider rate limit
Inject 429 → employee visual status shows rate-limited/waiting → retry policy engages → task is not falsely completed.

## AC-028 — Tool outage
Disconnect required MCP → workflow shows clear dependency/tool failure and does not fabricate success.

## AC-029 — Integration re-authentication
Expire credentials → user sees actionable connection state → reconnect restores future runs.

## AC-030 — Truthful living office
For each canonical state, backend event → semantic state → bot animation/status → text dossier all agree.

## AC-031 — Idle honesty
Idle bot may animate ambiently but must not appear to be performing productive work.

## AC-032 — Realtime receptionist
Inbound test call/event → receptionist executes supported flow → output enters same workflow/history system.

## AC-033 — Free-game monitor
Scheduled run checks configured sources → reports qualifying items or valid no-match → deduplicates previous alerts.

## AC-034 — Infrastructure monitor
Scheduled health workflow queries permitted systems → detects injected issue → creates correct diagnosis/approval/report path.

## AC-035 — Model diversity
Two employees in one workflow use different configured model routes.

## AC-036 — Cost attribution
Where provider reports usage, usage is attributable to employee/workflow/run.

## AC-037 — Unknown cost honesty
Missing cost metadata renders as unknown, not guessed actual spend.

## AC-038 — Global reporting
User can answer what ran today, what failed, what needs attention, and what is scheduled next.

## AC-039 — Run timeline
A multi-step run can be reconstructed from trigger through final output.

## AC-040 — Audit configuration change
Change employee tool permission → audit history identifies change and version.

## AC-041 — Search
Search can locate core entities without requiring knowledge of internal IDs.

## AC-042 — Simple workflow creation
A non-developer can create "every morning check X and notify me" without writing orchestration code.

## AC-043 — Complex workflow creation
Advanced user can configure branches, retries, approvals, per-step employee/model/tool settings.

## AC-044 — Workflow pause
Pause recurring workflow → future occurrences do not execute → history remains.

## AC-045 — One-occurrence skip
Skip one scheduled occurrence without deleting the recurring definition.

## AC-046 — Department creation
Create new department → persists → can add employees/workflows/knowledge → appears in organization overview.

## AC-047 — Employee configuration versioning
Edit employee SOUL/job config → version stored → rollback restores prior behavior contract.

## AC-048 — Least privilege
Attempt unauthorized production action from employee → server denies and records it.

## AC-049 — Approval cannot be bypassed by UI
Direct backend attempt of approval-required action is denied without authorization.

## AC-050 — No fake production data
Fresh organization contains no fabricated employees, work, spend, QA or health metrics.

## AC-051 — Responsive operational access
Core status, approvals, employee detail and alerts remain usable without full desktop office.

## AC-052 — Reduced motion
Reduced-motion mode removes unnecessary animation but retains all state information.

## AC-053 — Room legibility
Department office does not cram workers so densely that identity/status becomes unreadable; visual grouping handles larger teams.

## AC-054 — Cross-department handoff
Work can move from one department to another while preserving ownership/provenance.

## AC-055 — Workflow creates downstream work
A monitoring workflow can create a task/project in another department subject to policy.

## AC-056 — Human notification
Actionable condition produces a deduplicated user notification with direct link to relevant run/approval.

## AC-057 — Routine no-result is success
A monitor that finds no qualifying items records successful no-result rather than failure.

## AC-058 — Scheduler time zone
Time-zone and DST test produces correct next-run time.

## AC-059 — Concurrent recurring overlap
When prior occurrence is still active, configured overlap policy is followed.

## AC-060 — External engine replaceability
Where practical, runtime execution profile/engine can change without changing Empirium employee/workflow identities.

---

# Release blockers

The product should not be called finished if any of these remain fundamentally false:

- browser closure stops intended background work;
- recurring schedules are only UI placeholders;
- employees lose identity/memory across sessions;
- MCP permissions are not enforced;
- handoffs rely on manual copy/paste;
- workflow history is missing;
- dashboard metrics are fabricated;
- the office shows states unrelated to runtime truth;
- one model/provider is hardwired into the employee domain;
- destructive actions can bypass approval;
- ordinary failures cause work to disappear;
- users cannot determine why a workflow failed;
- workflows cannot be created/edited without source-code modification.


---

<!-- SOURCE MODULE: 11_HERMES_EXECUTION_HANDOFF_PROMPT.md -->

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
