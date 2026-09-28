

===== 2026-09-22 11:25 | session 20260922_105531_432d90 | AI staff force set up =====
@file:.hermes/attachments/EMPIRIUM_STUDIO_COMPLETE_PRODUCT_BRIEF-3.md
@file:.hermes/attachments/00_READ_ME_FIRST-3.md
@file:.hermes/attachments/11_HERMES_EXECUTION_HANDOFF_PROMPT-3.md

--- Attached Context ---

📄 @file:.hermes/attachments/EMPIRIUM_STUDIO_COMPLETE_PRODUCT_BRIEF-3.md (24978 tokens)
```markdown
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
- coding standar
...[TRUNCATED 55237 chars]...
 must be able to define:
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

```

📄 @file:.hermes/attachments/00_READ_ME_FIRST-3.md (1824 tokens)
```markdown
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

```

📄 @file:.hermes/attachments/11_HERMES_EXECUTION_HANDOFF_PROMPT-3.md (2043 tokens)
```markdown
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

```

===== 2026-09-22 11:27 | session 20260922_105531_432d90 | AI staff force set up =====
@file:.hermes/attachments/EMPIRIUM_STUDIO_COMPLETE_PRODUCT_BRIEF-4.md
@file:.hermes/attachments/00_READ_ME_FIRST-4.md
@file:.hermes/attachments/11_HERMES_EXECUTION_HANDOFF_PROMPT-4.md

please just do the job

--- Attached Context ---

📄 @file:.hermes/attachments/EMPIRIUM_STUDIO_COMPLETE_PRODUCT_BRIEF-4.md (24978 tokens)
```markdown
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
- customer 
...[TRUNCATED 55261 chars]...
 must be able to define:
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

```

📄 @file:.hermes/attachments/00_READ_ME_FIRST-4.md (1824 tokens)
```markdown
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

```

📄 @file:.hermes/attachments/11_HERMES_EXECUTION_HANDOFF_PROMPT-4.md (2043 tokens)
```markdown
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

```

===== 2026-09-22 11:28 | session 20260922_105531_432d90 | AI staff force set up =====
@file:`.hermes/attachments/FORENSIC_RETROSPECTIVE.md`

I want you to analyse the find and download forensic ward at Markdown chat. In there, we discuss how to set up an autonomous system to create a software product autonomously using hermes.

--- Attached Context ---

📄 @file:`.hermes/attachments/FORENSIC_RETROSPECTIVE.md` (19874 tokens)
```markdown
---
title: Forensic Retrospective — Autonomous Software Development
type: retrospective
tags: [autonomous-systems, postmortem, evidence, methodology]
source: /home/ash/audits/meta-retro-202609/FORENSIC_RETROSPECTIVE.md
date: 2026-09-22
---

# FORENSIC RETROSPECTIVE — AMIS / HERMES AUTONOMOUS SOFTWARE-DEVELOPMENT ORCHESTRATION

**Date:** 2026-09-22 (Europe/London)
**Mode:** Read-only investigation. No code, config, database, git history, or running service was modified.
**Subject:** The operator's methodology for building an autonomous software-development system on Amis/Hermes, with Star Force X / "Nailed It" (Nailify) and Empirium Studio (AI Staff Force / AI Workforce) as experimental workloads.
**Method:** Primary sources only — filesystem, SQLite databases, JSONL control-plane logs, git history, Hermes session store, and pre-existing audit documents (treated as claims to verify, not ground truth). Evidence-classification: PROVEN / STRONGLY SUPPORTED / PROBABLE / SPECULATIVE.

---

## 1. Executive Summary

1. **The project changed identity mid-flight, and the change was mostly undocumented.** Through September 2026 the operator's own vocabulary shifted from "build a nail app" to "build a nail app *autonomously*" to "build a production software-production organisation." Evidence is PROVEN in the session-title chronology (`Implement Nailed It MVP V2` → `Execute bounded worker packet` → `AIStaffForce`) and in the Empirium repo's `AI_WORKFORCE_BUILD/` tree, whose 710-requirement ledger describes the factory, not the product.
2. **Worker reliability never justified the orchestration built on top of it.** The strongest single dataset: 78 completed autonomous attempts on employee `emp-003` yielded 15 IMPLEMENTED (19.2%), 30 TIMEOUT (38.5%), 20 NO_PROGRESS (25.6%), 9 TEST_FAILED, 4 RUNTIME_FAILED — a ~64% no-usable-output rate (STRONGLY SUPPORTED; cross-checked against `attempts` tables in the 2026-09-18 audit snapshots, where accepted outcomes were 4.7% and 5.6%). No architecture generation ever achieved a worker accepted-attempt rate materially above ~20%.
3. **Every generation solved the previous generation's *mechanism* failure while leaving its *semantics* failure intact.** Giant prompt → persistent manager → watchdog/fresh session → deterministic controller (SQLite) → durable control plane (leases, worktrees, review state). By the final generation, restart-recovery genuinely worked (PROVEN via live restart evidence), but "worker finished with exit 0" was still the effective definition of progress, requirements were still zero in the authoritative store, and reviews were still zero in the authoritative store.
4. **Completion semantics were the recurring root failure.** In three independent stores across two workloads: `review` tables empty, requirement rows 0 (Nailify SQLite) / 710 requirements with 0 verified (Empirium), `WAITING_PROVIDER`/`blocked` terminal-ish states with no scheduled retry, and a controller whose empty-queue handling sets a retry flag rather than asking "is the project actually done?" The system repeatedly could not distinguish *nothing runnable* from *objective complete* (PROVEN at the state-table level).
5. **Self-approval was the default until very late.** For most of the history the same agent interpreted the task, implemented it, ran its own tests, and declared success; the Nailify audit's requirement #13/#15 evidence shows integration (cherry-pick) happening before any independent check (PROVEN: `review count=0`, `release_gate=0`). Independent review (Opus, CAO reviewer) arrived only in the last generation and had produced 17 review files with a still-unrun third re-review.
6. **The "one more supervisor" pattern is real, and its cost is directly measurable.** Hierarchy genuinely grew (worker → manager → Director → Meta-Director → watchdog → deterministic reconciler). The clearest single exhibit is the 2026-09-18 supervisor storm: between 01:21 and 10:01 UTC, Hermes sessions titled as Build-Director launch/relaunch events run in numbered generations 60-060 → 68-068 → 70-070 → 72-072 → 73-073 → 78-078 → 83-083 → 91-091 → 95-095 — at least nine director incarnations in under nine hours, repeatedly triggered by a watchdog because *"release gate unsatisfied"* — while the gate's real blocker was 699 unimplemented requirements, which no supervisor could fix. (PROVEN in `state.db` session titles/timestamps.) Crucially, the final shift (LLM-continuity → deterministic state) *was* the correct response and is the project's one durable conceptual win; the error was that it arrived after ~4 generations of adding intelligent supervisors to what was always a state-persistence problem.
7. **Deterministic machinery was proven at the *mechanism* layer and never at the *product* layer.** The autonomy-kernel commissioning gate passed 13/13 checks including worker-death recovery and QA-rework loops — i.e., the harness demonstrably works. Meanwhile 0 of 710 mandatory requirements are independently verified and the final release gate fails 8 of 13 checks. The factory has been tested; the factory's *output* has not (both PROVEN).
8. **False-progress metrics drove most "success" claims.** Agent counts, 102 worktrees, 398 passing unit tests, "the autonomy kernel was proven," "223 git commits," and heartbeat-driven status JSON all measured activity or infrastructure health. Every one of these coexisted with near-zero independently-accepted product progress. The audit documents themselves are partly guilty of this (their "PROVEN IN REAL WORKLOADS" section is almost entirely harness evidence).
9. **Provider/model churn confounded nearly every experiment.** Routes moved across FreeLLMAPI pool, `openai-codex/gpt-5.6-luna`, Gemini fallback, OpenRouter free models — often switched *at the same time* as architectural changes, making attribution impossible (PROVEN in the Nailify audit's routing table: earlier attempts have NULL routing; inherited fallback bypassed stated policy).
10. **The operator's dominant pattern was architecture-after-failure without measurement.** Each observed stall produced a redesign proposal (visible in the 454-message rescue-prompt sessions and successive MASTER prompts), not a baseline metric. No generation had an explicit success/failure metric or observation window before the next generation was invented (STRONGLY SUPPORTED by the session chronology + absence of any measurement artifacts until the audit documents themselves).
11. **Observability failures caused paid human intervention.** The operator repeatedly opened forensic audits (2026-09-18 alone produced a 176-line master audit, a round-2 evidence snapshot, a remediation preflight snapshot, a repairs snapshot, and a 420-line staff-force audit) — interventions classified as legitimate product-owner judgment *and* compensating for systems that could not explain their own state.
12. **What genuinely worked, verified:** deterministic SQLite state with event log; isolated worktrees; Task/Attempt separation in the final schema; fresh bounded worker contexts; provider-neutral launch records; structured failure classification enums; the *concept* of a fail-closed release gate. None of these, however, have yet produced a released product (STRONGLY SUPPORTED).
13. **What only looked like it worked:** heartbeat liveness (the expired-but-alive worker held the only slot while the controller reported healthy — PROVEN live observation); giant master prompts (the 48k-token V3 prompt functioned as spec+memory+state machine at once and its sessions required repeated rescue); persistent manager/AI-employee personas; large test suites written by implementers; watchdog restarts of an idle-loop controller.
14. **The autonomy tax exceeded the autonomy benefit at every generation.** At the last counted state: 80 controller files (2,570 lines total), a 786-line `production-reconciler.ts`, a 440-line `director-service.ts`, 112 orphan worktrees, two PostgreSQL clusters, 710 tracked requirements — versus 0 released products and a measured 4.7–19.2% accepted-worker-attempt rate. The R&D value of building this is real (§31); the *operational* value as a software-production system was not demonstrated.
15. **The single most actionable lesson:** the first experiment should have been one bounded task, run 20 times, measuring independently-accepted passes — before any manager, orchestrator, database, or watchdog existed (§64).

---

## 2. What the Experiment Really Was

On paper this history is "use Hermes to build apps." In the record it is a **meta-project**: a months-long R&D programme whose actual deliverable became *a theory of autonomous software production*, tested against two deliberately mundane workloads (a React Native nail-try-on app, and an Electron "AI Workforce" dashboard that is itself the factory UI).

The evidence for the identity shift:
- Earliest relevant Hermes session: `2026-09-01 17:48` "how do i get started with hermes agent?"
- Mid-September: `AUDIT + FIX: Empirium OS thin client / VPS` sessions (280 messages) — product work.
- 2026-09-17→18: a chain of 20+ sessions titled "Continue Nailed It MVP V2 implementation #1–#6", "Review project documentation and checkpoints", "Implement highest priority P0 slice", "Execute bounded worker packet (from file)" — the product became a *durable controller's workload*.
- 2026-09-18 10:37: a session literally titled "AIStaffForce"; and by 2026-09-19 the AI Staff Force audit exists as a standalone infrastructure assessment of the factory, not the app.
- 2026-09-20→21: Director/Meta-Director checkpoints ("68-068"), `empirium-autobuild` reconciler emitting ~120 records/hour of pure control-plane telemetry.

Was the transition justified? Partially. Building any orchestration layer requires *a* workload, and real apps expose orchestration bugs that toy tasks do not. But the workloads served as *instrumentation* for the factory, and by mid-September the factory consumed the engineering while the products received ~0 verified features. The meta-project became the project (PROVEN at the directory level: `/home/ash/empirium-studio/AI_WORKFORCE_BUILD/` is 165+ files of controller/checkpoints/ledger against a product repo whose feature tests live elsewhere; the Nailify product repo's own git history shows 79 commits).

**Answer to §84's meta-question:** the dominant objective migrated PRODUCT OUTPUT → ORCHESTRATOR RELIABILITY → CONTINUITY → ARCHITECTURAL ELEGANCE of the control plane, with experimental learning as the after-the-fact rationalisation. The shift from "use AI to build software" to "build a system capable of autonomously building software" happened around 2026-09-17/18, when work was re-expressed as "work items" with "attempts" and "leases" rather than as app features.

---

## 3. Master Timeline (compressed, evidence-anchored)

| Date | Event / evidence |
|---|---|
| 2026-09-01 | First Hermes session ("how do i get started") — Gen-0 baseline, interactive use. |
| 2026-09-12/13 | Empirium Studio / VPS integration work; 453-message session attaching images; laptop-control detour (abandoned SSH route visible in session titles). Product-adjacent platform work. |
| 2026-09-15 | `Restart only when update detected` (45-msg session) — early watchdog thinking. |
| 2026-09-17 21:24–23:46 | Nailify downloaded to VPS; 21:37 "Implement Nailed It MVP V2" (145 msgs) → 21:38, fourteen minutes later, "Diagnose autonomous AI system stopping failures" (328 msgs) — failure-diagnosis and rescue-prompt writing begins essentially immediately; 21:42 first "Empirium Workforce 20-minute continuation watchdog" cron session; 21:50 "Install temporary project dead-man watchdog"; 22:21–22:34 two sessions churning OpenRouter out of agent selection; 22:34 "Grant Permission to All Hermes Tasks" — Gen-1/2 era: one big autonomous prompt + a watchdog + permission loosening. |
| 2026-09-18 00:33–10:01 | **The supervisor storm** (209 sessions across the 09-17 21:20 → 09-18 15:17 window): sequential "Continue Nailed It MVP V2 implementation #1–#6" and "Continue Empirium Studio... #N" bounded sessions, interleaved with director-generation relaunches numbered 60-060, 68-068, 70-070, 72-072, 73-073, 78-078, 83-083, 91-091, 95-095 — watchdog-triggered because "release gate unsatisfied," while the gate's real blocker (699 unimplemented requirements) was unaffected by each new supervisor. This is Gen-2 (watchdog + bounded sessions) and the first Gen-3 director-loop evidence in one frame. |
| 2026-09-18 ~02:05 | "You are the implementation worker for the..." — first explicit worker-packet language. |
| 2026-09-18 11:50 | "Build Nailed It MVP V3 autonomously" (251 msgs) using the 105,798-byte `HERMES_NAILED_IT_MASTER_PROMPT_V3_AUTONOMOUS.md`; 11:56–11:58 requirement extraction; from 12:11 onward ~45 sessions in 3 hours titled "Execute bounded worker packet ..." and "You are a bounded Empirium product ... #1–#26" — the Gen-3/4 worker fleet running as disposable Hermes sessions; 10:56 "Add API key to FREELLMAPI" and 13:41 "Restore personal OpenRouter LLM option" bracket this window — provider churn during a live orchestration experiment (PROVEN confounder). |
| 2026-09-18 13:59–14:05 | Independent production-readiness audit of the Nailify durable controller → MASTER_AUDIT verdict **NOT READY** (25 requirements; 20 FAIL). Directly observes expired-worker-blocks-slot live. |
| 2026-09-18 14:25 | Repairs snapshot `/home/ash/repairs/nailify-orchestrator/...` — remediation attempted mid-audit era. |
| 2026-09-18 19:33 | Remediation-preflight snapshot (project.db: 2 attempts, 1 accepted-in-name only, controller RUNNING). |
| 2026-09-18 late / round2 | Round-2 DB snapshot: 53 attempts, 11 `accepted` (20.8%), 10 `blocked`, 1 `expired`; 0 reviews; 0 requirements. |
| 2026-09-19 | AI Staff Force independent audit (420 lines): control plane "operational"; worker reliability 19.2% implemented / 64.1% failed; PostgreSQL peer-auth blocker; 0/710 requirements verified; release gate 8/13 failing. |
| 2026-09-20/21 | Director 68-068 checkpoint era (710 requirements, 5 verified, IN_PROGRESS), `meta-director-checkpoint.json`; `empirium-autobuild` reconciler running as the live control plane (2,245 records in 18.7h; `acceptance.initial_status` = FAIL in 100% of records; `diagnosis` = None in 100% — the reconciler never generated a single diagnosis task). |
| 2026-09-22 | This retrospective. Live state at session start: director-runtime-prompt (27,800-byte "L1 orchestrator" doctrine), checkpoints DB, BUILD_STATE still `IN_PROGRESS`. |

(Timeline anchors: Hermes `state.db` sessions table; file mtimes under `/home/ash/audits/`; git logs.)

---

## 4. Architecture Generations

**Gen 1 — One large autonomous prompt.** (PROVEN artifact: `HERMES_NAILED_IT_MASTER_PROMPT_V3_AUTONOMOUS.md`, 3,629 lines / 105,798 bytes; earlier V2/V1 variants implied by attachment names.) The prompt was simultaneously spec, memory, planner, state machine, role definitions, recovery instructions, and definition-of-done. Its own §58/§68 contain "durable state" and "context discipline" sections — evidence the author already knew prompts were carrying state they shouldn't. Outcome: sessions ended, new sessions re-read checkpoints and *reinterpreted* them (session titles "Review project documentation and checkpoints" recurring ~6 times in one day). Bigger prompts did not improve reliability; they increased instruction overload — the V3 prompt itself is a master prompt *about* autonomy with an embedded 60-section constitution.

**Gen 2 — Watchdog + fresh bounded sessions (the "dead-man" era).** Solves *session death* (PROVEN: systemd + `Restart=always`, Linger=yes, controller survives chat/gateway death). Does not solve *authoritative continuation*: each fresh session reconstructs state from documents. "Does the watchdog wake a system that knows what work existed?" — partially: it woke a controller that knew DB state, but the DB had 0 requirements and 0 reviews, so what it knew was only the queue.

**Gen 3 — Deterministic controller + SQLite (Nailify `.hermes/autonomy/controller.py`, 293 lines, 16.3 KB).** Real conceptual shift: scheduling, worktree ownership, attempt/lease records, event logging moved out of the LLM. The audit confirms "scheduling/dependency/routing code is deterministic Python, not an LLM manager conversation" (PROVEN). But the audit's 20 FAIL findings show it controlled *the loop*, not *acceptance*: exit-0 + changed HEAD ⇒ INTEGRATED; no QA runner; lease non-atomic; expired-but-alive worker occupies the sole slot; restart misclassifies successful adopted exits as failures.

**Gen 4 — Durable control plane + organisational hierarchy (AI Staff Force / Empirium).** Controller grows to 80 files / 2,570 lines; adds PostgreSQL (schema written; *unreachable* — peer auth), leases, heartbeats, director/meta-director checkpointing, 5 "products", 12 employee-style profiles, CAO orchestrator, independent Opus review layer, 710-requirement traceability ledger, 14-check release gate (11 failing), 102 worktrees. Worker execution moved to `product-worker-executor.mjs` spawning disposable bounded Hermes agents — the "disposable workers, durable state" doctrine correctly implemented (PROVEN). Yet this most-sophisticated generation has the *worst* measured product convergence: 0/710 verified, 15/78 attempts productive, DB authority disputed between SQLite and Postgres, and a reconciler whose dominant log output is `heartbeat_tick` reporting `work_found: 0`.

Each generation was introduced as a response to the previous one's *concretely observed* failure (audit reports document the motivating evidence), which makes this evidence-driven at the micro level — but no generation set a measurable acceptance criterion *before* building (experimental discipline, §42).

---

## 5–6. Case Studies as Orchestration Evidence (condensed per scope rule)

**Nailify (Gen 1–3 workload).** Chosen because it is a real, modest app. What it proved: (a) worker self-report treated as completion — attempts record `last_commit` and status without QA review, 0 review rows across both snapshots (PROVEN); (b) false WorkItem acceptance — "exit=0 plus different HEAD is sufficient for INTEGRATED" (audit requirement #19 FAIL, PROVEN by code); (c) liveness-as-progress — heartbeat keeps expired work looking active, one live observation of an expired worker holding the only slot while `project.state=RUNNING, running=0, workers=1` (PROVEN); (d) empty queue ≠ complete — two isolated reconciles produced `WAITING_RETRY`, 0 work items, 0 events: permanent logical stall while alive (PROVEN via audit test C); (e) destructive recovery deletes the evidence — `finish_children` force-removes the failed worktree including logs (PROVEN). Lesson: the *controller* survived everything; the *project* never converged.

**AI Staff Force / Empirium (Gen 4 workload).** Chosen to run the factory itself as its workload (meta-recursion). What it proved: (a) Task/Attempt separation exists and works (78 attempts attach to persistent work items; provider rotation across attempts is recorded); (b) recovery machinery works *as mechanism* — 13/13 commissioning checks including worker-death recovery and QA rework; (c) it fails *as production*: the same controller stack that recovers anything produces, at best, 15 usable changes from 78 attempts, and the release gate cannot be satisfied because 699/710 requirements were never implemented — the factory proved it can keep running, not that it converges. Also a fresh contradiction: PostgreSQL "operational authority" is unreachable by its own workers (peer auth) while the doctrine says durable state is the point (PROVEN via audit §4). (d) The AI-employee metaphor: "employee dossier" tasks, `emp-003` as a persistent worker persona — identity is durable, capability is not: attempts under one "employee" are a 64% failure distribution.

**Cross-workload recurring failures (the valuable ones):** worker timeout/no-progress as the dominant outcome; no enforced independent verification before acceptance; acceptance state living in prose/tables nobody validates; completion semantics undefined in every store; observability requiring external audits to reconstruct what the system "knew."

---

## 7. Evolution of the Mental Model

Inferred from prompt artifacts and session titles (PROVEN as text, PROBABLE as psychology):
1. "A complete enough specification lets Hermes keep working to done." → discovered context death, reinterpretation.
2. "Keep a manager alive and workers disposable." → discovered manager death == reasoning loss; persistent manager ≠ persistent project.
3. "Wake sessions externally (watchdog); bound their work." → discovered liveness without direction; controller heartbeats ≠ progress.
4. "Deterministic code owns routine; LLM owns judgment." → correct, and implemented; then discovered that deterministic code also *must own acceptance semantics* — and it didn't, because there was nothing to accept *into*.
5. "The LLM is not the durable orchestrator." (the doctrine, quoted approvingly by the 2026-09-19 audit) — the final and right belief, arrived at through four generations of holding its negation.

---

## 8. Evolution of Prompting

Prompt size grew, instruction *count* exploded, then partially contracted into structured packets. V3 master prompt (3,629 lines) mixes charter + runtime state + recovery procedures — a natural-language state machine. The Gen-4 `director-runtime-prompt.md` is far more disciplined: identity, hard rules, exactly two tools, "durable state is the fact," "orchestrator does not write product code," explicit anti-claims ("completed 0/710 — never claim 'complete'"). Genuinely helpful techniques: bounded packets, explicit forbidden actions, evidence requirements, "inspect before change." Counterproductive: encoding retry schedules, queue state, and completion definitions in prose; re-stating history per session. The end-state principle the history earned: **prompt = intent + contract; software = live state + transitions.**

---

## 9. Context and Persistence Lessons

Every generation kept some authoritative fact in the wrong layer. Giant prompts kept *runtime* state in *charter* text (stale instructions, drift). Managers kept project state in conversation. The final system still keeps requirements in a JSON ledger (2,288 records) *and* an empty SQLite `requirements` table — split authority (PROVEN in audit req #3). Context quantity showed a real optimum: fresh bounded worker packets outperformed giant contexts; but too little context produced workers who couldn't see architecture constraints. The unresolved issue: workers received the packet but not a trustworthy *acceptance* context (what counts as done, who checks).

---

## 10. Task / Attempt / Worker Lessons

Task ≠ Attempt finally appears in Gen-4 schemas (attempts table with provider/model/status per execution against durable work items) — and it *works* mechanically: provider death no longer destroys work. Remaining coupling failure: in Nailify, WorkItem terminal status was reachable solely from attempt exit status; in Empirium, blocked attempts end at `WAITING_RETRY` with no scheduled retry and no diagnosis — the *task* silently inherits the *attempt's* dead end. Worker identity was over-crédited: "emp-003" as persona suggests continuity it doesn't have.

---

## 11. Delegation and Hierarchy Lessons

Hierarchy added decomposition value (Director plans, workers execute) but almost no reliability value: every supervisory layer introduced handoff context loss, duplicate planning, and new failure surfaces, while the actual constraint — worker acceptance rate ~20% — was untouched by hierarchy. Parallelism was real (102 worktrees) but the measured max concurrency was effectively 1 (MAX_WORKERS=1; one slot-blocked controller finding); so parallel infrastructure was built around a serial reality (STRONGLY SUPPORTED).

---

## 12. Controller and Deterministic-State Lessons

The controller *did* control the live system — this contradicts the pre-audit fear that "a controller in the repo ≠ control." systemd evidence: deterministic Python owns scheduling/leases/worktrees, survives restarts, records events. The lesson inverted: controlling *execution* was solved comparatively early; controlling *verification* was never solved, and the architecture's own audits kept rediscovering that gap. A controller that faithfully executes a wrong completion predicate is a precise way to be wrong.

---

## 13. Recovery Lessons

Recovery was implemented before the happy path was proven (the commissioning gate tests *death recovery* as a headline achievement). Concrete recovery defects: restart misreads vanished PIDs as failures (losing successful results); expiry leaves the live process holding capacity; worktree force-deletion destroys the evidence a reworker would need; `retry_at` ignored, no repeated-failure diagnosis. Mechanical retry dominated: prior-failure evidence shows redispatch at 13:33:59 of a worker that failed at 13:33:57 — same task, same conditions, ~identical strategy (PROVEN; this is non-semantic retry).

---

## 14. Review and Validation Lessons

Implementer-authored tests + implementer-run gates = false confidence (398 green unit tests coexisting with 1 failing E2E and 0 verified requirements). Independent review existed only as expensive manual Opus passes and CAO reviewer profiles; the audit shows review-state never enforced integration (cherry-pick before review; 0 review rows in the authoritative DB). Review also lagged its own findings: first Opus verdict fixed, second verdict NEEDS_ARCHITECTURE_REVISION with partial fixes enumerated, third review never run. Reviewers were sophisticated, not *binding*.

---

## 15. Liveness vs Activity vs Productivity vs Convergence

- Liveness proven, treated as health (systemd + heartbeat).
- Activity: reconciler at ~120 records/hour of which 74% were heartbeat ticks — activity with `work_found: 0` (PROVEN).
- **The final control plane ran for 18.7 hours without acting once** (PROVEN by direct parse of `empirium-autobuild/reconcile.jsonl`, 2,245 records at 30-second intervals). The kanban board is **byte-identical in all 2,245 records** — `blocked=1, done=11, ready=27, review=10, todo=6` — and `actionable_ready=1` with `assigned_running=0` in every single one. The only variables that ever moved were the git SHA (6 commits) and `oldest_ready_age_seconds`, which climbed **monotonically from 47.0h to 65.7h** without ever decreasing — a ready task aged over 65 hours without being picked up. The system was alive, obedient, and completely inert.
- Productivity: 19.2% attempts implemented (Empirium), 20.8% "accepted" (Nailify round-2) — but "accepted" in a system with 0 reviews overstates real productivity. Nailify round-1's own snapshot gives 4 SUCCEEDED / 14 attempts (28.6%); the preflight/round-2 snapshot gives 9 / 25 (36%). Both are *controller self-declarations*, not independent acceptance.
- Convergence: the honest metric was available and ignored — `BUILD_STATE` recorded `verified_requirements` peaking at 5 of 710; the final `FINAL_RELEASE_GATE.json` counts `missing_proof: 710` (`not_verified: 0` — a self-contradictory claim, see §43). E2E: 11/12; product features shipped: not measurable as accepted.

---

## 16. False Progress Analysis

Vanity metrics actually used: worktree count (102), attempt count (78), profile count (12+), test count (398, unverified here), requirement count (710 — *counting specs is not counting work*), commits, prompt sophistication (the 86-section audit mandate is itself evidence of document volume as proxy for progress). The metric that would have exposed failure in week one: **independently accepted product changes per day.** It exists nowhere in the record until the audits finally computed something like it (retrospectively, 2026-09-19).

---

## 17. Autonomy Tax

Rough split of the final generation's engineering surface: product code (Empirium server/UI, nailify app) ≈ 2,200–3,000 lines of the core doctrine-carrying files; orchestration/autonomy ≈ 2,570-line controller tree (80 files) + 786-line `production-reconciler.ts` + 440-line `director-service.ts` + 232-line `product-worker-executor.mjs` + CAO + worktree fleet + checkpoint DBs + prompt constitution + gate JSONs. Ratio: orchestration effort exceeds product effort by an order of magnitude (estimate; PROVEN in file listing, UNKNOWN in hours). The tax bought *continuity*, which was the *self-assigned* goal, not *output*, which was the stated goal — so it paid rent on an empty room.

---

## 18. Complexity Curve

Diminishing returns crossed around Gen 3. Gen 1→2 (watchdog) and Gen 2→3 (deterministic controller) each removed a demonstrated, measured failure. Gen 3→4 (Postgres, hierarchy, employee personas, 710-requirement ledger, release-gate JSON, Director/Meta-Director, 5 products) added surface faster than it removed failure classes: PostgreSQL still unreachable, review still unenforced, completion still undefined, and worker reliability — untouched by any layer — remained the binding constraint. Conceptual model: throughput ≈ (worker reliability) × (orchestration adequacy); orchestration adequacy saturated at "SQLite + worktrees + leases," and everything after optimized a non-binding factor.

---

## 19. Tool and Model Churn

Documented switches: giant-prompt sessions → bounded sessions; CAO → (alongside) bespoke controller → reconciler + director; providers: FreeLLMAPI auto, codex-subscription Luna fallback, inherited Gemini, OpenRouter-free in the pool; SQLite vs Postgres as authority. Each switch co-changed at least one confounder (model+provider+prompt+runtime changed together in the Gen-3→4 transition; routing NULLs in early attempts make even retrospective attribution impossible). New-tool optimism is visible in session titles ("AIStaffForce" begins as a new-frame session). No migration in the record has a measured before/after on an acceptance-based metric (PROVEN by absence).

---

## 20. Hermes / Amis-Specific Lessons

Demonstrably strong: bounded single-session coding with a packet; tool use; repository inspection; search/summarize. Demonstrably misused: sessions were asked to *be* a process supervisor, state store, scheduler, reviewer, and recovery engine — capabilities its lifetime model (chat-scoped, compaction-prone) structurally lacks. Hermes' session persistence itself became an unexamined crutch: 453-message and 280-message sessions show enormous accumulations that later needed rescue/restart sessions. The correct role, finally adopted by Gen 4 ("the LLM is not the durable orchestrator"), was Hermes as *disposable component* — a worker, reviewer, or planner invoked with bounded context. Compaction (as in this very session) is the concrete demonstration: long-lived LLM state is lossy by construction.

---

## 21. My Human Operating Pattern (operator audit)

The record shows a capable, evidence-hungry operator with three counterproductive reflexes: (1) **architecture-as-coping** — every stall produced a new system rather than a measurement; (2) **audit proliferation** — at least five major forensic audits (plus this one) whose primary function was answering questions the running system could not answer about itself, i.e., observability debt paid in operator time; (3) **goal expansion without goal renegotiation** — "autonomous" silently grew from "no prompt from me" to "survives everything and finishes products," and the success criteria for the expanded goal were never written down before building toward them. Legitimate strengths: preserved evidence (audits are excellent), refused to delete failures, and eventually commissioned an *independent* audit that contradicted the system's self-reports — the right instinct, too late.

---

## 22. Repeated Mistakes (Pattern / Evidence / Belief / Consequence / Rule)

| Pattern | Historical evidence | Why believed | Consequence | Replacement rule |
|---|---|---|---|---|
| Solve state loss with another intelligent process | persistent manager era; Director/Meta-Director layers | "someone must keep the thread" | each layer added a new death to manage | state lives in tables, not processes |
| Scale up before measuring single-worker reliability | 102 worktrees vs MAX_WORKERS≈1 | parallelism looks like throughput | fleet idle/stalled, capacity illusion | measure N=1 acceptance rate first |
| Bigger prompts to compensate for missing software | V3 master prompt 3,629 lines; 60+ section director prompt | "if it's written it's enforced" | instruction overload, drift | anything enforceable in code must not live in prose |
| Change several variables at once | model+provider+runtime+schema changed across Gen 3→4 | redesigns feel efficient | attribution impossible | one hypothesis, one variable, one metric |
| Trust narration | "implemented/verified" as audit-recognized weak evidence; green dashboards | reporting was the only signal | false completion repeatedly | only independent predicates produce acceptance |
| Implement recovery before happy path | commissioning gate 13/13 while 0/710 verified | durability felt fundamental | sophisticated persistence of unproductive work | prove accepted output, then harden |
| Measure activity | heartbeat_tick 74%, commits, attempt counts | visible and growing | weeks of confident non-convergence | one metric: accepted changes/day |

---

## 23. Misdiagnosed Problems

- "Context persistence was the problem" — partly true; the deeper problem was *authoritative acceptance state*, later rediscovered as the release-gate gap.
- "The giant prompt was the problem" — true for Gen 1 symptoms, but treated as *the* lesson when it was *a* symptom; swapping prompts for managers kept the same prose-state in new vessels.
- "Session death is the problem" → watchdog — fixed a non-fatal nuisance while convergence stayed broken.
- "Poor throughput → add parallel structure" — bottleneck was worker reliability and task decomposition, not concurrency.
- "Model/provider is the bottleneck" — provider churn never improved the ~20% acceptance rate (STRONGLY SUPPORTED by rate stability across recorded model changes).

---

## 24. Major Root-Cause Chains (two exemplars)

**Chain A — the slot-blocked controller (2026-09-18, live-observed).** Symptom: project RUNNING, no work progressing ↓ Mechanism: expired worker kept in memory CHILDREN, lease expiry marked DB `WORKER_DEAD` but process still held the single slot ↓ Technical cause: two ownership stores (in-memory CHILDREN vs SQLite) with no compare-and-swap claim or fencing ↓ Architectural cause: runtime state and durable state given equal authority; no termination/fencing on expiry ↓ Operator cause: recovery/robustness features were prioritized before a liveness-vs-progress reconciliation test existed ↓ Detection gap: heartbeat-based liveness looked green ↓ Measurement that would have exposed it: *accepted changes/day* flat while `workers=1` alive — i.e., the convergence metric that was never wired up.

**Chain B — requirements never implemented.** Symptom: release gate fails 8/13; 699/710 unstarted ↓ Mechanism: orchestration accepted work items without requirement linkage (requirements table 0 rows; ledger in a separate JSON) ↓ Technical cause: no gate that blocks completion states on evidence predicates; integration precedes review ↓ Architectural cause: the factory's own work items (dossier tasks, UI screens) were easier to decompose than the product's, so planning optimized the ledger, not the artifact ↓ Operator cause: requirement-count growth (710 traced) was read as progress ↓ Detection gap: no one-time reconciliation between ledger and DB ↓ Measurement: verified-requirements delta per week — present in BUILD_STATE, never treated as the headline KPI until the audit stated it.

---

## 25. Architecture Decision Register (condensed; full per §46 fields)

| # | Decision (date) | Motivating failure | Diagnosis then | Assumption | Actual result | New problems | Reversible? | Retained? |
|---|---|---|---|---|---|---|---|---|
| 1 | Giant master prompts (≤09-17) | session death, drift | "prompt must carry state" | model re-derives truth each read | reinterpretation, overload | re-reading cost, stale instructions | yes | superseded |
| 2 | Watchdog + fresh sessions (09-17/18) | chat/session death | "keep waking bounded workers" | waking = continuing | liveness solved, no direction | silent idles, no completion semantics | yes | yes (as mechanism) |
| 3 | Deterministic controller + SQLite (09-18) | lost state on restart | "move routine control to code" | code can also define done | scheduling/lease truth achieved | split authority (CHILDREN vs DB), exit=0 acceptance | yes | **yes (core)** |
| 4 | Task/Attempt separation (09-18) | provider loss killing work | "execution is disposable, intent durable" | correct | restart-safe work items | blocked state = dead-end without diagnosis | yes | **yes** |
| 5 | Worktrees everywhere (09-18) | interference, dirty evidence | "isolate parallel work" | parallelism needed | isolation achieved | 102 orphans, force-delete destroys logs, serial reality | yes | simplify |
| 6 | AI-employee metaphor, Director/Meta-Director (09-18→20) | coordination load | "organisation needs roles" | hierarchy = reliability | planning decomposition | handoff loss, sunk-cost personas | yes | mostly die |
| 7 | PostgreSQL as authority (09-19) | SQLite split authority | "the durable DB is the fact" | infra reachability | unreachable (peer auth) — doctrine outran environment | workers split-brain file-store vs PG | yes | blocked, pending |
| 8 | Requirements ledger + release gate (09-19) | false completion | "enumerate what done means" | counting = convergence | gate exists, fail-closed semantics partial | 710 items, 0 verified; "requirements=712/548 reconciled" is itself a metric of paper | yes | keep (as predicate engine) |
| 9 | Independent Opus review layer (09-19) | self-approval | "external intelligence can catch what builders miss" | reviews will bind | genuine findings (partial-fix callouts were correct) | cost, flaky triggers, third review never run, not enforced pre-integration | yes | keep, make binding |

---

## 26. Contradiction Register

| Claim | Contradicting evidence | Why it coexisted |
|---|---|---|
| "The system is autonomous" | operator ran ≥5 audits, rescue sessions, manual grants, restarts | autonomy defined as unattended *liveness*, not unattended *correctness* |
| "Autonomy kernel proven" | proven = 13/13 harness checks; product acceptance untested | harness success was presented as system success |
| "Durable state is the fact" | authority split SQLite/JSON ledger/Postgres(unreachable); runtime CHILDREN vs DB | durability of records ≠ single authority |
| "Independent review" | 0 review rows; cherry-pick before review; implementer-written tests | review *role* existed, review *gate* didn't |
| "Controller driven" | director prompts still instruct "you are the only component that advances the project" — an LLM session | LLM owned semantic transitions; code owned scheduling |
| "Complete/RELEASE_VALIDATED" (BUILD_STATE previous status) | later "Invalidated on resumed execution because acceptance_status recorded partial capabilities" | completion was a status label, not a predicate — self-correction eventually happened, which is worth crediting |
| "FreeLLMAPI-only / zero paid" | inherited Gemini API fallback + OpenRouter free candidates in pool | policy in prose ≠ policy in code (audit req #9/#10) |

---

## 27. What Actually Worked (verified)

- Deterministi
...[TRUNCATED 19219 chars]...
— Abandon rather than improve:** The org metaphor (employees, Directors, Meta-Directors), the worktree fleet, CAO as currently structured, persistent managers, mega-prompt constitutions, the 5-product portfolio, recovery features for unexercised failure modes, and the heartbeat-as-health instrumentation.

**Q9 — One metric for next time:** Independently accepted product changes per day (verified against requirements at current SHA). Flat line while workers are "alive" was the canary for the entire meta-project; nothing else would have been as early.

**Q10 — Default next approach:** Use one agent with bounded packets and a pre-written acceptance predicate; run it 20 times; look at the pass rate before designing any orchestration; let demonstrated, measured failures — never predicted ones — license each added component, and let the plan author remain human until the system has shipped something it was actually pointed at.

---

# WHAT I SHOULD REMEMBER

1. A project must survive the death of every LLM session in it — if continuity lives in a chat, it will die.
2. Worker output is evidence to inspect, never completion; self-reported "done" is data, not state.
3. Never let the builder write, run, and trust its own tests; independence in verification is a component, not a courtesy.
4. Do not solve a persistence problem with another agent; persistence is tables, not presence.
5. Measure one worker before orchestrating many: a fleet inherits the reliability of the thing it multiplies.
6. "Empty queue" and "no runnable work" are observations about the queue, not about the objective.
7. Define completion as a predicate over requirements *before* building anything that can report it.
8. Keep dynamic execution state out of the product charter; charter = intent, control plane = facts.
9. Liveness, activity, and throughput are three different numbers; I optimized the first and read it as the third.
10. Changing architecture without a baseline metric means never learning from it — the confounder is always also the fix.
11. One variable per experiment; provider and architecture never change together.
12. Task ≠ attempt: execution must be disposable while intent is durable; model choice belongs to the attempt.
13. Recovery machinery must be earned by demonstrated failure, not by imagination of failure.
14. Documentation volume (prompts, requirement counts, audit length) is the most comfortable vanity metric — it feels like progress and is only paper.
15. Hierarchy adds handoff loss and failure surface per layer; earn each layer with measured coordination load.
16. The system is observable only if it can answer "why is it idle?" — every generation I lacked this, and every gap I paid for with an audit.
17. Better models change worker reliability, not my responsibility for acceptance semantics; the doctrine outlives current capability.
18. Preserve failure artifacts; deleting the wreckage guarantees a repeat (force-deleted worktrees cost me the very evidence my rework loops needed).
19. If progress stalls, suspect the definition of done before suspecting the architecture.
20. My correct role was acceptance author, evidence reader, and kill-switch operator — attempts to remove myself from the loop before the system could tell truth from fiction made the loop unfixable, not autonomous.
21. Do not optimize the machinery of software production past the point where one more machine costs more than the software it might eventually produce: the factory's payroll exceeded its output, and only the shipped product pays.

---

## Appendix A — Prohibited-Conclusion Self-Check (§81)

Deliberately avoided: "need a better orchestrator/model/context/persistence/tests." Recommendations trend *downward* in complexity: fewer layers, single product, single worker until measured, deterministic gates, human-owned acceptance criteria. Where complexity is kept, each is tied to a demonstrated failure class with evidence cited above.

---

## Appendix B — Evidence Base (primary only; no secrets transcribed)

`/home/ash/.hermes/state.db` (903 sessions, ~100,400 messages); `/home/ash/.hermes/attachments/HERMES_NAILED_IT_MASTER_PROMPT_V3_AUTONOMOUS.md` (3,629 lines / 105,798 bytes); `/home/ash/empirium-studio/AI_WORKFORCE_BUILD/` (`controller/` 80 files / 2,570 lines, `controller/director-runtime-prompt.md`, `BUILD_STATE.json`, `REQUIREMENTS_TRACEABILITY.json`, `FINAL_RELEASE_GATE.json`, 112 orphan worktrees + 17 in `empirium-studio/.worktrees`, `director-checkpoints.db`, meta-director checkpoint); `/home/ash/.local/state/empirium-autobuild/` (`status.json`, `reconcile.jsonl` 2,245 records); `/home/ash/Desktop/nailify/.hermes/autonomy/` (controller.py 293 lines, init_db.py); `/home/ash/audits/nailify-20260918/` (MASTER_AUDIT.md 176 lines, evidence snapshots); `/home/ash/audits/nailify-20260918-round2/evidence/project.db` (53-attempt stats); `/home/ash/audits/nailify-20260918-remediation-preflight-*/`; `/home/ash/repairs/nailify-orchestrator/`; `/home/ash/AI_STAFF_FORCE_AUDIT_REPORT.md` (420 lines); `/home/ash/.aws/cli-agent-orchestrator/db/cli-agent-orchestrator.db` (CAO — 0 runs, 0 events); git logs of `empirium-studio` (230 commits) and `nailify` (79 commits).

Note: connection strings and credentials observed in files are omitted; any secret referenced above is [REDACTED] per mandate.

---

## 45. What Was Genuinely Done Right (the Nailify MVP V5 Build)

The V5 build (Nailify MVP, from 2026-09-22) broke the four-generation failure pattern by inverting the historical sequence: **acceptance was defined before any product code was written**, and the build's operating doctrine was this very retrospective, embedded verbatim as constitution rather than rediscovered. Evidence: on-disk artifacts at `/home/ash/Desktop/nailify/` (`.hermes/packets/WORKER_PACKET_TEMPLATE.md`, `CHECKPOINT.md`, `reports/harness-independent-review.md`, `app/verify.sh`, `autonomy/controller.py`), `/home/ash/stage0-prompt.md`, and the V5 master prompt (`/home/ash/nailify_master_prep/`).

### 45.1 Acceptance predicates defined before code (Stage 0 + frozen decisions D3/D4)
Frozen owner decisions: **D3** — freeze acceptance against current HEAD, not against old baseline assumptions; **D4** — build the acceptance harness now, as the sole acceptance authority, before further product implementation.

Stage 0 produced, before any implementation:
- **`REQUIREMENTS.v2.md` / `.v2.json`** — compiled from dual extraction passes (forward by capability, backward from proof surfaces), honest merge decisions, explicit target size (dozens, not 2,288 lines).
- **`EXCLUSIONS.md`** — first-class register of deliberate non-work, preventing deferred features from silently re-entering scope.
- **`ACCEPTANCE_PREDICATES.md`** — for every P0 requirement, the exact command/script/procedure that evaluates it, plus what failure must create (bounded work, never termination).
- **`OPERATOR_RULEBOOK.md`** — enforceable operational rules, each traceable to a specific historical failure.
- **`STAGE0_COMPLETION.md`** — bidirectional traceability: every user-story step → requirement ID, every DoD checkbox → requirement ID, orphan count = 0.

Core doctrine: **"A requirement is a capability the system must exhibit, together with the specific evidence that would prove it is exhibited."** This is §15's central lesson, codified *before* the build started instead of discovered during it.

### 45.2 Acceptance harness built first and made binding
`app/verify.sh` + `app/checks/` exist, are hash-protected (`.hermes/state/harness-sha.json`), and are the **sole acceptance authority** — before any product WorkItem dispatches.

- No worker can self-approve. `verify.sh` runs post-integration against canonical HEAD; protected files are hash-verified; a worker touching them is `MALFORMED — PROTECTED_HARNESS_MUTATION`.
- The harness was **independently reviewed by a fresh worker** (not the implementer), which found 7 bugs including 3 HIGH-severity false negatives (a size floor bypassable by formatting, a negation that masked violations, a substring match that passed on absent text) — all fixed and exploit-tested before the hash-freeze.
- The harness found a genuine product defect on its own: `mirror()` in `useDesignStore.js` was hardcoded L→R (missing hand-directionality); fix shipped with a new check, then re-reviewed after a self-found gaming vector was fixed. Final: all checks pass, full test suite green.

### 45.3 Worker packets eliminated ambiguity about acceptance
The packet template is bounded and mechanical, with zero ambiguity about who decides acceptance:

> "You do not decide whether your work passes. Acceptance is determined after your session by the protected independent harness."
> "Your status claim is informational only. It cannot set acceptance state."
> "Stop when you have either produced one coherent implementation commit, or determined that you cannot produce a coherent implementation inside this attempt."
> "Do not start a second implementation strategy after the attempt limit. Do not invoke another agent. Do not ask the user for help."

Each packet instantiates with: mission, requirement IDs, acceptance contract (frozen check predicates), allowed/prohibited files, test commands, expected artifacts, commit format, known prior-attempt failures, stop condition. Compare to the V3 era, where the same worker was simultaneously planner, judge, reviewer, and recovery engine.

### 45.4 The forensic retrospective was institutionalised, not re-derived
The full retrospective was embedded verbatim as an appendix of the V5 master prompt. Its findings shaped the build in real time: the 12-item anti-pattern list is a direct lift of §22's repeated-mistakes table; the "anti-goal" (§0: *do not optimise continuity — the single metric is independently accepted product changes per day*) is §16's false-progress analysis distilled into one sentence; "never let the builder authorise integration" is doctrine, not a lesson to re-learn; the 20-attempt worker-reliability benchmark implements §39's Stage 1 directly.

### 45.5 The controller was repaired, not expanded
Frozen decision **D9**: "The existing orchestration is adequate; earn every addition." The 293-line `controller.py` was kept, and its two most dangerous bugs were fixed on the strength of this retrospective's evidence:

1. `finish_children()` no longer integrates on exit-code-0 + new SHA (the self-approval defect of §5 Nailify case (b)). It now runs `verify.sh` after cherry-pick and reverts on FAIL.
2. `evaluate_release_gate()` no longer sets SHIPPED from an empty queue alone; it additionally requires `verify.sh` to pass at HEAD and that every FROZEN P0 requirement has harness coverage — closing the "gate passes on a partial check set" hole the checkpoint document itself warns about.

No new supervisor layer, no second database, no reconciler. Surgical fixes to the acceptance semantics, which §24's Chain A/B identified as the root cause.

### 45.6 Success criteria were checkable acceptance predicates, not continuity claims
V5 §0 states the goal as S1–S6: `verify.sh` exists and is the sole acceptance authority; every mandatory P0 requirement has a FROZEN acceptance contract and is PASS or explicitly `hardware-limited`; independent review of the full release diff by a fresh session that did not implement it; `SHIPPED` set only by the release gate, atomically. Every criterion is machine-checkable at a SHA — the exact inversion of Q1's "continuity as objective, acceptance undefined."

### 45.7 Provider/model freeze and pre-registered measurement
**D8** froze provider and model before any measurement (coding pool and review subscription, recorded in `.hermes/state/provider-model-freeze.json` after a 3-model smoke comparison). The benchmark is pre-registered: 20 attempts, one worker, fresh session each; provider/environment aborts excluded from the denominator; locked decision rules (≥60% proceed; 30–59% fix packet/contract, do *not* add a second worker; <30% fix decomposition, do *not* conclude more orchestration is needed); hard ceiling 40 valid attempts / 48 hours / one extra round, after which the campaign ends. This is §39's counterfactual sequence made operational, and it pre-empts §19's confounder (provider churn) by prohibition.

### 45.8 Honesty mechanisms that prevent self-deception
- **Hard dispatch rule**: no WorkItem dispatches unless every mandatory requirement it claims has a FROZEN acceptance contract — "implement first, define done later" is structurally impossible.
- **Anti-goal** names the metric to *ignore* (uptime, sessions, commits, task counts).
- **Self-audit at Stage 0** (10 yes/no questions: "Did I extract capabilities, or extract lines?", "Would a fresh reader know what done means without asking?").
- **Review queue** (R-01…R-04): external reviewer state is required before a WorkItem may become DONE; R-04 (full P0 release diff) is required before SHIPPED. R-01–R-03 were independently reviewed and passed before further work proceeded.
- **Self-warning checkpoint**: the checkpoint document explicitly records that starting the controller now would let the release gate see an empty queue + partial-harness pass and *falsely set SHIPPED* — the system documents its own lying surface instead of hiding it.
- **No rework of verified work**: "Phases 1–2 are complete. Skip them" — refusing the documented cost driver of redoing done work (§23, §34.8).
- **Honest re-baselining**: five stale-baseline conflicts in old documents were resolved against actual disk state (e.g., "native AR is a stub" was false; "Phases 1–2 not done" was false). A ledger whose baseline column lies is worse than no ledger, because it silently re-prioritises work.

### 45.9 What remains (honest assessment at session close)
Harness: built, independently reviewed, hash-frozen, all checks passing. Controller: acceptance semantics patched per §24. Product WorkItems: none dispatched yet. Worker-reliability benchmark: designed and pre-registered, not yet run. Independent release review (R-04): pending. `SHIPPED`: not declared. The *architecture* problem (the "container") is now solved with four generations of discipline; the *product convergence* problem (dispatching bounded work against frozen predicates, measuring, shipping) remains — and it is a decomposition question, not an orchestration one.

### 45.10 Causal ranking (highest impact first)
1. Acceptance predicates defined before code (§45.1) — made "done" machine-checkable from the start.
2. Acceptance harness built first and made binding (§45.2) — §14's review-lesson enforced as code.
3. Retrospective institutionalised as constitution (§45.4) — §22's pattern table became the build's anti-pattern list.
4. Controller repaired instead of replaced (§45.5) — D9 + two surgical acceptance-semantics fixes against §24's root-cause chains.
5. Worker packets with explicit non-acceptance language (§45.3) — §22's "trust narration" rule mechanically enforced.
6. Provider/model freeze before measurement (§45.7) — §19's confounder prohibited rather than noted.
7. Honest re-baselining against disk reality (§45.8) — §23's "misdiagnosed problems" prevented from recurring.
8. "Earn every addition" (§45.5/D9) — §17's autonomy-tax lesson made into a frozen decision.

---

# 86. FINAL EXECUTIVE CONCLUSION (mandated five statements)

### 1. The central reason my original approach failed:

I made *continuity* the objective while leaving *acceptance* undefined. Every mechanism I built — giant prompts, persistent managers, Directors, watchdogs, deterministic controllers, reconcilers — kept work alive, but none of them could tell me whether the product was actually converging, because "done" was a self-reported label in prose rather than a predicate over requirements at a known SHA. The result was a system that was liveness-green and convergence-blind across four architecture generations: 64% of worker attempts failed in every generation, 0 reviews were ever produced, requirements verified went 0 → 5 of 710, and the only completion label that ever appeared (`COMPLETE_RELEASE_VALIDATED`) had to be invalidated by a human. I optimized what I could observe (uptime, sessions, commits, task counts) and never defined what I could not (independently accepted product change). The 64% worker failure rate and 19.2% implemented rate cited here are from the 2026-09-19 staff-force audit's claim about emp-003 (SECONDHAND — `AI_STAFF_FORCE_AUDIT_REPORT.md`); this audit could not access the underlying attempt records. Nailify's own store tells a sharper story: 0 SUCCEEDED in 14 round-1 attempts (28.6% SUCCEEDED at round-2 snapshot, also self-declared).

### 2. The most valuable thing the experiment taught me:

The boundary between what intelligence should own and what deterministic software should own. Scheduling, retries, timeouts, process liveness, dependency resolution, atomic claim with fencing, and acceptance predicates belong in code — and they work exactly as designed. Decomposition, ambiguity resolution, architecture judgment, and coding belong to LLMs — and they do not work reliably at scale without that deterministic substrate underneath. The second-order lesson is that worker reliability is a *measurable distribution* (19.2% implemented, 64.1% no usable output) and that single number — which interactive AI coding never forces you to compute — determines every sane architecture decision about scaling, parallelism, and recovery.

### 3. The biggest mistake in my operating approach:

Responding to each failure by inventing structure instead of numbers. Every major redesign changed several variables at once (model + provider + prompt + architecture + task structure), so the system was never fairly measured and the same three failures — low worker output rate, false acceptance, and "empty queue ≠ complete" — recurred in every new costume across four generations. I also repeatedly solved *persistence* with *another intelligent process* (worker → manager → Director → Meta-Director → supervisor → watchdog), asking "who supervises the supervisor?" when the real question was "why does project survival depend on that supervisor remaining alive?" Each new layer added handoff loss, context loss, coordination cost, and a new failure surface without changing the underlying reliability of the thing being supervised.

### 4. The biggest thing the architecture got right:

"The LLM is not the durable orchestrator." Durable project state and routine control belong to deterministic software; LLM sessions are disposable execution. This was proven right by direct evidence: the Gen-4 controller survives session death, provider failure, and process restart because the task graph, attempt records, leases, and evidence live in SQLite outside any conversation, and a fresh session can resume from the same authoritative state. Every prior generation that kept state in a prompt, a manager's memory, or a chat session failed exactly at its boundaries. This single distinction is the only architectural insight in the whole history that reliably improved outcomes, and it was discovered only after watching enough systems die.

### 5. The operating principle I should carry into my next AI software-development experiment:

**One agent, one bounded task, one pre-written acceptance predicate — run it twenty times, measure the pass rate, and let that number — and only that number — license every component you add.** No orchestration, no hierarchy, no parallelism, no recovery machinery, no watchdog, no persistent manager until a single worker has independently and verifiably produced accepted output at a rate worth scaling. If the rate is low, the problem is the worker contract or the acceptance criteria, not the lack of a supervisor. Let demonstrated, measured failures — never predicted ones — license each added component, and let the plan author remain human until the system has shipped something it was actually pointed at.

```

===== 2026-09-22 11:31 | session 20260922_105531_432d90 | AI staff force set up =====
@file:.hermes/attachments/EMPIRIUM_STUDIO_COMPLETE_PRODUCT_BRIEF-5.md
@file:.hermes/attachments/00_READ_ME_FIRST-5.md
@file:.hermes/attachments/11_HERMES_EXECUTION_HANDOFF_PROMPT-5.md

The reason I brought this to your attention is because I want to implement the same methodology of autonomous software creation for this new separate product. Now, a lot of the mock-ups are already in the system, but just for the sake of making it easier for you to understand and have all the information at hand. I've given you a couple of additional mock-ups. Your job is to make sure that we do the preliminary stages of preparing to do this autonomously together now. I need all the questions that need to be asked to be provided in this chat, and then separately, we're going to initiate this product being built autonomously. Attached to all the documents you will need to analyse, so please analyze everything and then let's create a pre-plan that is a plan for the plan that is, we are everything that we need to prepare in order for this to do autonomously. That's what we're trying to establish now. It's also true for. So, I need all the questions from you just so I can provide all the answers

--- Attached Context ---

📄 @file:.hermes/attachments/EMPIRIUM_STUDIO_COMPLETE_PRODUCT_BRIEF-5.md (24978 tokens)
```markdown
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

This must not mean "the cu
...[TRUNCATED 56428 chars]...
chedules;
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

```

📄 @file:.hermes/attachments/00_READ_ME_FIRST-5.md (1824 tokens)
```markdown
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

```

📄 @file:.hermes/attachments/11_HERMES_EXECUTION_HANDOFF_PROMPT-5.md (2043 tokens)
```markdown
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

```
@image:/home/ash/.hermes/images/upload_20260922_113157_2.png
@image:/home/ash/.hermes/images/upload_20260922_113158_3.png
@image:/home/ash/.hermes/images/upload_20260922_113158_4.png

===== 2026-09-22 11:40 | session 20260922_105531_432d90 | AI staff force set up =====
@file:`.hermes/attachments/Pasted content (5.4 KB)`

This most certainly is not the extensive required list of questions that we need to be able to produce this app autonomously. When we did the Nailify app, which is significantly smaller, the questions I had to ask for that were significantly longer before we could even begin to set this off autonomously. What I require from you is each set of questions and every single possible question to be written out in its most explicit and thorough form. We need to leave no stone unturned because we are going to finish this properly. And I require your explicit questioning. So every single question that needs to be answered, every bit of data that you need beforehand, ask me all now. Now this is in no way shape or form related however I just want to show you how extensive the line of this was just the summary the questions were significantly longer. So what I want you to do is for each stage give me every single exhaustive question and I mean for each and every single stage

--- Attached Context ---

📄 @file:`.hermes/attachments/Pasted content (5.4 KB)` (1375 tokens)
```
Here's how I'd run it, with the retrospective's lessons applied. The honest headline first: **V4 is much better than the history it came from, but it still contains the one mistake the retrospective identified as the most expensive — it front-loads the entire factory (Phase A, 22 commissioning tests, full controller) before a single worker has proven it can complete one bounded task.** I would invert that.

## Stage 0 — Split the constitution (half a day, not a week)

The 26k-token prompt is a charter masquerading as a runtime. Split it into three artifacts:

- **Product charter** — kept verbatim, hashed, immutable (§§0–5, 9–67 — the product spec is genuinely good).
- **Machine-readable requirement ledger** — compiled from §67's 10-minute user story and §68's DoD checklist. This product has a gift most projects don't: the acceptance story is already written as 27 concrete steps. That decomposes into roughly **30–40 mandatory requirements, not 710**. The 710-item ledger was a progress object that measured nothing; this one stays small enough that every item maps to real evidence.
- **Operator rulebook** — ~20 lines: project survives every session death; worker "done" is data not state; only the gate sets SHIPPED; empty queue ≠ done; failed predicate creates a work item.

Everything in V4's §7 about the controller gets **deferred until Stage 3 earns it**.

## Stage 1 — Define acceptance before any orchestration

The failure that killed four generations was undefined acceptance, not weak orchestration. So the first engineering artifact is **predicates, not a controller**:

- `expo-doctor` + lint + jest on migration/placement math (deterministic)
- app boots to Home, screenshot captured at 2 widths (deterministic)
- the 27-step user story decomposed per requirement, each with a named check
- visual items → structured screenshot checklist against the charter's token spec, reviewed by a fresh vision-capable session, tied to the SHA

No SQLite schema, no leases, no merge queue yet. A `checks/` directory and a `verify.sh`.

## Stage 2 — The experiment that was never run

**One worker. One bounded task. One pre-written predicate. Twenty times.**

First task: something real and small from Phase 1 (e.g., "implement the French tip control"). Fresh Hermes session, bounded packet, `verify.sh` decides. Measure: accept rate, timeout rate, no-change rate, rework rate. Record all of it in a flat JSONL.

This costs one afternoon and produces the number that every architecture decision in the entire history was made without. If accept rate is ~50%, orchestration stays almost unnecessary. If it's 20%, the fix is the packet and decomposition — **not another supervisor**. That single measurement would have compressed four architecture generations into one experiment.

## Stage 3 — Earn each component

Grow the kernel only where Stage 2's numbers demand it, in this order:

1. **Task/Attempt table in SQLite** (already justified — sessions die)
2. **Failed predicate → creates a rework work item** (the one control-loop behavior that was genuinely missing — the reconciler logged FAIL 2,245 times and diagnosed nothing)
3. **Second worker + worktrees** — only after single-worker accept rate is known and above threshold
4. **Independent review as a binding gate** — implementer never runs its own final check; visual QA is a fresh vision session against current-SHA screenshots
5. **systemd unit + cron heartbeat** — but its job is *restart the dead and log*, never *spawn director generations*. The watchdog in the history fired 60+ relaunches that changed nothing; this one fires on exactly one condition: independently accepted changes per day = flat.
6. **Recovery drills** (kill worker, kill controller, simulate 429) — now, because the happy path has actually shipped accepted work, so the drills test a real machine instead of a speculative one.

## What I'd deliberately *not* do from V4

- **Not Phase A as written.** 22 commissioning tests before any product work is the "perfect recovery before happy-path proof" trap. Commission destructively only what you've exercised.
- **Not the 22-state project state machine.** Most of those WAITING states never earned their existence; a task table with statuses covers it.
- **Not the provider-routing subsystem on day one.** Freeze the provider roster at experiment start (the history showed model/provider churn as a standing confounder). Change it only on a classified provider failure, one variable at a time.
- **Not 5 concurrent products or the org metaphor.** One repo, no Directors, no Meta-Directors. Planning happens when a wake event fires (repeated failure, exhausted queue, ambiguity), not as a standing persona.

## The one metric

**Independently accepted changes per day, verified against the requirement ledger at the current SHA.** Workers alive, sessions running, commits landing — none of that counts. In the entire history that line was flat while every liveness metric was green; it's the only number that would have said "stop changing architecture, fix the worker contract" in week one instead of generation four.

The short version: **V4's instinct (deterministic control, disposable workers, evidence-based gate) is the lesson the retrospective says is right — but its sequencing repeats the original sin. Build the predicate first, measure one worker, and let the numbers — not the anticipation of failure — assemble the machinery.**
```