

===== 2026-09-21 23:50 | session 20260921_234936_670e4e | prep for nailify =====
@file:`.hermes/attachments/Pasted content (65-2.5 KB)`

--- Attached Context ---

📄 @file:`.hermes/attachments/Pasted content (65-2.5 KB)` (15975 tokens)
```
# MASTER FORENSIC RETROSPECTIVE

# AMIS / HERMES AUTONOMOUS SOFTWARE-DEVELOPMENT ORCHESTRATION META-PROJECT

## 0. MISSION

You are conducting an **exhaustive forensic retrospective, systems audit, experimental-methodology review, and operator postmortem**.

You are NOT building software.

You are NOT fixing software.

You are NOT redesigning the orchestration system.

You are NOT auditing Star Force X or Nailify as products in their own right.

The subject of this investigation is:

> **My entire history of attempting to use Amis/Hermes and AI agents to create a reliable autonomous software-development system — including orchestrators, sub-orchestrators, supervisors, managers, workers, reviewers, persistent state, controllers, watchdogs, prompts, task systems, recovery mechanisms, model routing, validation systems, and my own behaviour as the operator.**

Star Force X and Nailify are important only because they were **real experimental workloads** through which this system was tested.

They are evidence.

They are case studies.

They are not the object of the audit.

The purpose of this investigation is to determine:

> **What I tried, what I believed would happen, what actually happened, why it happened, what repeatedly failed, which architectural changes genuinely improved things, which merely moved the problem around, what I personally did well or badly as the operator, and what durable lessons I should carry into future autonomous AI software-development experiments.**

I want to understand the history deeply enough that I do not repeat months of experimentation unnecessarily.

This is a postmortem.

Do not defend the architecture.

Do not defend prior AI conclusions.

Do not flatter me.

Do not attack me.

Do not manufacture coherence where the history was messy.

Investigate.

Reconstruct.

Challenge.

Compare.

Quantify where possible.

Learn.

---

# 1. CRITICAL SCOPE RULE

This rule overrides any later ambiguity.

The primary subject is:

> **MY METHODOLOGY FOR USING AMIS/HERMES TO BUILD AN AUTONOMOUS SOFTWARE-DEVELOPMENT SYSTEM.**

The primary subject is NOT:

* Nailify's feature completeness;
* Star Force X's feature completeness;
* their visual design;
* every bug in either product;
* every missing requirement;
* whether an individual screen was correct;
* how either product should now be finished.

Only inspect product-level details where they demonstrate something about the autonomous-development methodology.

Useful evidence:

> A worker marked a feature complete even though it did not work in the runtime, demonstrating that worker self-reporting was being treated as completion evidence.

Useful evidence:

> Three independent workers misunderstood the same requirement, suggesting a task decomposition or context-packet problem.

Useful evidence:

> The controller reached an empty queue despite unfinished product behaviour, exposing a flaw in work generation or completion semantics.

Useful evidence:

> A product defect remained across several orchestration generations despite large amounts of agent activity, showing lack of convergence.

Not useful:

> The button should have been blue instead of purple.

Not useful:

> Here is how to implement the missing feature.

Not useful:

> Here is a complete product backlog for Nailify.

Whenever you encounter application-specific evidence ask:

> **What does this teach us about the autonomous development system?**

If the answer is "nothing significant," do not spend substantial time on it.

Aim for roughly:

* **80–90%** of the investigation on orchestration methodology, experimentation, Amis/Hermes usage, architecture, operator behaviour and lessons;
* **10–20%** on Star Force X / Nailify evidence necessary to support those conclusions.

Do not mechanically enforce the percentages. Preserve the priority.

---

# 2. THE CENTRAL QUESTION

The ultimate question is:

> **Why did my attempts to create a genuinely autonomous AI software-development system repeatedly fail, stall, require human rescue, become more complex, or fail to reliably converge — and what should I personally do differently in future?**

Break this into several deeper questions:

1. What did I originally think autonomy required?
2. Which assumptions were correct?
3. Which assumptions were wrong?
4. Which failures were caused by LLM limitations?
5. Which were caused by my prompts?
6. Which were caused by context engineering?
7. Which were caused by orchestration architecture?
8. Which were caused by state/persistence design?
9. Which were caused by process/infrastructure?
10. Which were caused by how I responded to failure?
11. Which problems did I repeatedly misdiagnose?
12. Which changes genuinely improved outcomes?
13. Which changes mainly added complexity?
14. Which lessons survived multiple experiments?
15. What should I never repeat?
16. What should I retain?
17. What should I test much earlier next time?

---

# 3. DO NOT ASSUME THE EXISTING STORY IS TRUE

There are already many:

* audits;
* postmortems;
* architectural analyses;
* prompts;
* handovers;
* summaries;
* recommendations;
* diagrams;
* plans;
* AI-generated explanations.

Treat ALL previous conclusions as **claims to investigate**, not ground truth.

This includes statements such as:

* "the giant prompt was the problem";
* "context persistence was the problem";
* "we needed more orchestration";
* "we needed a persistent manager";
* "agents needed to be disposable";
* "the supervisor needed to be deterministic";
* "sub-orchestrators were necessary";
* "durable state solved continuity";
* "worktrees solved parallelism";
* "the controller worked";
* "the autonomy kernel was proven";
* "the project was almost finished";
* "the system was autonomous";
* "more rigorous requirements were the answer";
* "another framework would solve it";
* "the model was the bottleneck";
* "the architecture was the bottleneck."

For every major historical claim ask:

> What evidence actually supports this?

And:

> Could another explanation fit the same evidence?

Where later evidence contradicted earlier AI analysis, explicitly document the contradiction.

---

# 4. READ-ONLY FORENSIC MODE

Do not contaminate the historical evidence.

Do NOT:

* modify application code;
* modify orchestration code;
* alter Git history;
* clean worktrees;
* delete files;
* alter databases;
* restart autonomous production merely to see what happens;
* launch workers;
* launch new builds;
* install packages;
* modify prompts;
* change model/provider configuration;
* change systemd services;
* fix bugs;
* "improve" architecture while investigating;
* create another orchestration system.

Use read-only inspection wherever possible.

If an operation would mutate historical state, avoid it.

The output should be the retrospective report only.

---

# 5. INVESTIGATIVE SOURCES

Search broadly across every accessible historical source.

Do not assume everything exists in one repository.

Investigate, where available:

## Conversations and prompts

* Hermes conversations;
* Amis conversations;
* ChatGPT conversations;
* Claude conversations;
* Claude Code history;
* Codex history;
* prompt files;
* giant autonomous build prompts;
* supervisor prompts;
* manager prompts;
* worker prompts;
* reviewer prompts;
* recovery prompts;
* handovers;
* audit prompts;
* follow-up prompts.

## Repositories and files

* Git repositories;
* branches;
* tags;
* commits;
* commit messages;
* abandoned branches;
* worktrees;
* orphan worktrees;
* architecture docs;
* markdown files;
* READMEs;
* project notes;
* AGENTS.md;
* `.hermes`;
* `.cao-*`;
* autonomy folders;
* orchestration folders;
* controller code;
* worker code;
* reviewer code;
* task systems;
* state files.

## Durable state

* SQLite;
* PostgreSQL;
* JSON state;
* task databases;
* requirements ledgers;
* dependency tables;
* Attempts;
* Runs;
* leases;
* heartbeats;
* workers;
* events;
* audit logs;
* artifacts;
* review results;
* evidence records;
* checkpoints;
* recovery records.

## Runtime / infrastructure

* systemd;
* cron;
* shell scripts;
* watchdogs;
* supervisors;
* process logs;
* stdout/stderr;
* provider logs;
* token/cost logs;
* model-routing logs;
* worker launcher logs;
* reconciliation logs.

## Testing and validation

* test reports;
* QA reports;
* review reports;
* acceptance reports;
* browser test evidence;
* screenshots;
* runtime checks;
* release gates;
* benchmark results.

## Systems/tools to look for

Where relevant search for:

* Hermes;
* Hermes Studio;
* Hermes Gateway;
* Amis;
* Astra;
* AI Staff Force;
* AI Workforce;
* Autonomy Kernel;
* CAO;
* CLI Agent Orchestrator;
* Conductor;
* OpenHands;
* Claude Code;
* Codex;
* Gemini;
* OpenRouter;
* FreeLLMAPI;
* ModelScope;
* Luna;
* Sol;
* Directors;
* Meta-Directors;
* managers;
* project managers;
* workers;
* crews;
* reviewers;
* QA agents;
* watchdogs;
* controllers;
* reconcilers;
* leases;
* checkpoints;
* worktrees.

Search for renamed or abandoned implementations too.

---

# 6. EVIDENCE STANDARD

Apply a strict hierarchy of evidence.

Weak evidence:

* "implemented";
* "done";
* "verified";
* "complete";
* "production ready";
* "all tests passed";
* worker self-report;
* manager summary;
* task marked complete;
* green dashboard;
* commit existence;
* queue reaching zero.

Stronger evidence includes:

* implementation actually present;
* deterministic state evidence;
* independent tests;
* independent reviewer results;
* integration evidence;
* process logs;
* task lifecycle records;
* runtime validation;
* restart/recovery records;
* measurable throughput;
* human-intervention frequency;
* actual end-to-end behaviour.

For every major finding classify confidence as:

### PROVEN

Directly supported by logs, code, Git history, runtime evidence or other primary records.

### STRONGLY SUPPORTED

Several independent pieces of evidence support the same conclusion.

### PROBABLE

Most likely explanation but evidence is incomplete.

### SPECULATIVE

Possible but insufficiently supported.

Never silently present speculation as fact.

---

# 7. RECONSTRUCT THE COMPLETE CHRONOLOGY

Build a chronological timeline from the earliest experiment through the latest.

Do NOT focus only on the most sophisticated architecture.

I want the progression.

For each major generation record:

* approximate date;
* problem I believed existed;
* architecture before the change;
* architecture introduced;
* models/providers;
* number/type of agents where known;
* context strategy;
* persistence strategy;
* task-management strategy;
* worker strategy;
* QA/review strategy;
* recovery strategy;
* expected outcome;
* actual outcome;
* observed failure;
* diagnosis made at the time;
* response;
* whether the response fixed the underlying failure;
* new complexity introduced;
* new failure modes;
* what was retained;
* lesson.

The timeline should answer:

> **How did one failure cause the next architecture to be invented?**

---

# 8. RECONSTRUCT THE META-PROJECT HIERARCHY

Determine whether the project evolved through layers resembling:

### Level A — Product

Build Nailify / Star Force X.

### Level B — AI-assisted development

Use AI to build the product.

### Level C — Autonomous workers

Have AI workers independently perform development.

### Level D — Orchestration

Coordinate workers with an orchestrator.

### Level E — Sub-orchestration

Add Directors/managers/sub-orchestrators.

### Level F — Meta-orchestration

Supervise the orchestrators.

### Level G — Reliability machinery

Keep the supervisors/orchestrators alive and recover them.

### Level H — Durable control plane

Externalise state into deterministic software.

### Level I — Validation of the autonomous factory itself

Use real products as test workloads for the factory.

Determine the actual hierarchy from the evidence.

Then answer:

> At what point did the software factory become the primary engineering project?

Also determine whether this transition was:

* intentional R&D;
* accidental scope growth;
* justified;
* partially justified;
* counterproductive.

---

# 9. RECONSTRUCT THE MAIN ARCHITECTURAL GENERATIONS

Identify the real generations.

Do not force history into these exact labels, but investigate whether the evolution resembled the following.

---

## GENERATION 1 — ONE LARGE AUTONOMOUS PROMPT

Investigate the early belief:

> If the specification is sufficiently detailed, Hermes can simply keep working until the software is finished.

Analyse:

* prompt size;
* responsibilities;
* product requirements;
* recovery instructions;
* testing rules;
* autonomy instructions;
* role definitions;
* definitions of done.

Ask:

* Was the prompt acting simultaneously as specification, memory, planner, state machine and recovery mechanism?
* What happened when context ended?
* What state survived?
* Did a fresh session resume or reinterpret?
* How much repeated context loading occurred?
* Did bigger prompts meaningfully improve reliability?
* Did they eventually create instruction overload?

Extract the lessons.

---

## GENERATION 2 — PERSISTENT MANAGER / SUPERVISOR

Investigate systems such as Astra or equivalent ideas.

The intended theory may have been:

> Keep one intelligent manager alive; let workers be disposable.

Determine:

* what state the manager held;
* what happened when it died;
* whether state existed outside context;
* whether project continuity depended upon manager continuity;
* whether replacement meant actual continuation or reconstruction.

Analyse the distinction:

> **Persistent manager ≠ persistent project.**

---

## GENERATION 3 — ORCHESTRATOR + SUB-ORCHESTRATORS

Investigate hierarchical organisations.

Potential examples:

* Meta-Director;
* Director;
* manager;
* project manager;
* crew;
* developer;
* QA;
* reviewer.

Determine why each layer was introduced.

Then assess whether hierarchy improved:

* decomposition;
* parallelism;
* oversight;
* reliability;
* quality;
* recovery.

Or instead increased:

* handoffs;
* context loss;
* coordination cost;
* duplicated planning;
* unclear authority;
* summary chains;
* latency;
* token usage;
* failure surfaces.

Identify which layers were genuinely useful.

---

# 10. THE "ONE MORE SUPERVISOR" PATTERN

Investigate whether I repeatedly responded to failure like this:

> worker fails
> → add manager

> manager stops
> → add Director

> Director stops
> → add Meta-Director

> Meta-Director stops
> → add supervisor

> supervisor may stop
> → add watchdog

If this occurred, determine the underlying pattern.

Was I solving:

> **state persistence**

with:

> **another intelligent process**?

Was I asking:

> "Who supervises the supervisor?"

when the better question was:

> "Why does project survival depend on that supervisor remaining alive?"

This should be investigated deeply.

---

# 11. EXTERNAL WATCHDOG / FRESH SESSION ERA

Investigate the point where the architecture shifted toward:

* cron;
* systemd;
* shell scripts;
* external watchdogs;
* fresh bounded Hermes sessions;
* automatic restart.

Determine whether this successfully solved:

> chat/session death

but still failed to solve:

> authoritative project continuation.

Did the watchdog merely wake another LLM?

Or did it wake a system that knew exactly:

* what work existed;
* what attempt had failed;
* what state was authoritative;
* what should happen next?

---

# 12. DETERMINISTIC CONTROLLER ERA

Analyse the transition toward deterministic software controlling routine execution.

Look for components such as:

* `controller.py`;
* SQLite;
* PostgreSQL;
* dependency graphs;
* worker capacity;
* attempts;
* leases;
* retries;
* process tracking;
* worktrees;
* review state;
* integration state;
* systemd.

This represents a major conceptual shift.

Determine why it occurred.

What functions moved from LLM judgment into deterministic code?

Examples:

* scheduling;
* task transitions;
* dependency resolution;
* retries;
* worker capacity;
* timeouts;
* process liveness;
* integration;
* event logging.

Then investigate whether:

> **the controller actually controlled the live system**

or whether an LLM conversation still effectively owned execution.

A controller existing in the repository is not enough.

---

# 13. PROCESS LIFETIME VERSUS PROJECT LIFETIME

Map these separately:

* Chat lifetime
* LLM session lifetime
* Worker process lifetime
* Manager process lifetime
* Controller process lifetime
* Attempt lifetime
* Task lifetime
* Project lifetime

Identify where earlier systems coupled these accidentally.

For example:

> parent session dies → child assignment disappears.

Or:

> manager dies → knowledge of active work disappears.

Or:

> worker fails → underlying task is lost.

The project should survive all disposable execution layers.

Determine how close each architecture came to achieving this.

---

# 14. TASK IS NOT AN ATTEMPT

Investigate the emergence of:

> **Task / WorkItem ≠ Run / Attempt**

Earlier systems may have treated a task as a single agent invocation.

Later systems may have represented:

### Task

Durable desired outcome.

### Attempt

One temporary execution against that Task.

This distinction matters for:

* provider failure;
* context failure;
* process death;
* worker timeout;
* bad implementation;
* review rejection;
* model change;
* retries.

Determine:

* when this distinction emerged;
* what failures forced it;
* how completely it was implemented;
* whether Task state ever remained coupled to worker state.

---

# 15. PROJECT STATE VERSUS AGENT MEMORY

For every historical generation ask:

> If every AI conversation disappeared right now, what information would survive?

Investigate persistence through:

* prompts;
* summaries;
* Git;
* markdown;
* JSON;
* database;
* task tables;
* requirements ledgers;
* attempts;
* audit events;
* evidence;
* reviews;
* artifacts.

Trace the shift from:

> agent remembers project

toward:

> project state exists independently and agents inspect it.

This is one of the central lessons to examine.

---

# 16. MASTER PROMPT VERSUS RUNTIME STATE

Investigate whether the giant prompts attempted to encode both:

## Durable product charter

* product purpose;
* constraints;
* architecture;
* requirements;
* non-negotiables;
* definition of done.

and:

## Dynamic runtime state

* current tasks;
* attempts;
* failures;
* retry counts;
* workers;
* branches;
* worktrees;
* blockers;
* review status;
* test results.

Determine whether mixing these caused:

* stale instructions;
* repeated context loading;
* conflicting state;
* reconstruction overhead;
* drift.

Determine when we learned that:

> The prompt/specification should describe intent.

while:

> The control plane should hold live execution state.

---

# 17. CONTEXT ENGINEERING RETROSPECTIVE

Analyse context across the full history.

Track:

* giant project prompts;
* full conversation history;
* manager summaries;
* condensed summaries;
* checkpoint files;
* task packets;
* bounded context packets;
* source code context;
* Git history;
* logs.

Investigate:

* too much context;
* too little context;
* stale context;
* context contamination;
* scope compression;
* conflicting summaries;
* workers reinterpreting requirements independently.

Determine whether:

> More context improved performance

or whether at some point:

> More context reduced signal quality.

Determine what information workers actually needed.

---

# 18. WORKER CONTRACTS

Analyse historical worker assignments.

Ask:

* Were tasks bounded?
* Were objectives explicit?
* Were acceptance criteria explicit?
* Did workers know what NOT to change?
* Did they know the relevant files?
* Did they receive enough architectural context?
* Did they receive too much context?
* Did they know how to report evidence?
* Did they understand the boundary between implementation and approval?

Where possible sample worker attempts and estimate:

* successful bounded implementation;
* partial completion;
* no-change output;
* timeout;
* misunderstanding;
* broken implementation;
* self-declared success despite failure;
* successful reviewed completion.

Try to understand the actual **worker reliability distribution**.

Did the orchestration architecture assume workers were more reliable than they actually were?

---

# 19. BLOCKING DELEGATION VERSUS ASYNC ASSIGNMENT

Investigate delegation semantics.

Was the architecture effectively:

> Manager sends work
> → waits
> → worker responds
> → manager continues.

If so, determine how the parent's lifespan became part of the critical path.

Compare with:

> Assignment persisted
> → worker runs independently
> → result persisted
> → future controller iteration reconciles it.

Identify when this distinction became apparent.

Determine whether later systems truly decoupled assignment from manager session lifetime.

---

# 20. WORKER IDENTITY VERSUS EMPLOYEE IDENTITY

Investigate any "AI employee" concepts.

Did persistent employee identities become conflated with persistent sessions?

Analyse the later principle:

> Employee/role identity may be durable.

But:

> the LLM session currently performing its work should be disposable.

Explain whether this distinction improved the architecture.

---

# 21. STATE OWNERSHIP

For every major generation identify the authoritative owner of:

* product objective;
* requirements;
* task graph;
* dependency graph;
* task state;
* attempts;
* worker identity;
* process identity;
* retry state;
* timeout state;
* provider selection;
* worktree ownership;
* test state;
* review state;
* integration state;
* blockers;
* completion state.

Flag:

### Duplicate ownership

Two components both believe they are authoritative.

### Missing ownership

No component explicitly owns the state.

### Implicit ownership

Authority lives only in natural language.

Determine whether unclear ownership caused recurring problems.

---

# 22. WORKER LIVENESS AND PROCESS REALITY

Investigate technical worker-management failures.

Potential historical examples include:

* lease expired while worker still ran;
* process remained alive after controller considered attempt dead;
* worker occupied capacity permanently;
* fixed-duration lease expired during valid long task;
* no heartbeat;
* PID reuse;
* orphan process;
* orphan worktree;
* controller DB disagreed with OS process state.

For each verified case explain:

1. controller belief;
2. operating-system reality;
3. resulting failure;
4. why it happened;
5. architectural lesson.

General question:

> Was the system managing actual processes or merely managing database records representing processes?

---

# 23. RETRY RETROSPECTIVE

Analyse retries.

Distinguish:

### Mechanical retry

Run essentially the same thing again.

versus:

### Semantic recovery

Learn from failure and alter strategy.

Investigate whether repeated failures caused:

* different model;
* smaller task;
* added context;
* diagnostic task;
* dependency repair;
* planner escalation;
* human escalation;
* architecture reconsideration.

Or merely:

> retry #2, retry #3, retry #4.

Determine how much wasted work resulted from non-semantic retry.

---

# 24. FAILURE SHOULD MODIFY THE WORK GRAPH

Investigate the emergence of the idea:

> FAIL should create information and work, not merely terminate a task.

For review rejection or implementation failure, did the system:

* stop;
* repeat blindly;
* ask me;
* leave FAILED indefinitely;
* create explicit rework;
* create diagnosis;
* split task;
* alter dependencies?

Determine whether rework became first-class durable state.

---

# 25. EMPTY QUEUE DOES NOT MEAN COMPLETE

Find every historical state where:

* nothing was runnable;
* queue was empty;
* all tasks were blocked;
* retries were exhausted;
* no workers were active.

Determine what the system inferred.

Possible meanings include:

* completed;
* deadlocked;
* work graph incomplete;
* planning exhausted;
* missing requirements;
* waiting for review;
* failure not translated into rework;
* bug in scheduler.

Identify whether the system ever confused:

> **no runnable work**

with:

> **objective complete**.

This is a major completion-semantics lesson.

---

# 26. LIVENESS, ACTIVITY, PRODUCTIVITY, CONVERGENCE, CORRECTNESS, COMPLETION

Define and audit these separately.

## Liveness

Something is running.

## Activity

Messages/tasks/commits are being produced.

## Productivity

Useful accepted changes are being produced.

## Convergence

The unresolved gap to the intended outcome is shrinking.

## Correctness

Accepted work actually satisfies the requirement.

## Completion

The entire governed objective has been reconciled and independently accepted.

Find historical examples where one was mistaken for another.

Examples:

* process alive → assumed project progressing;
* workers busy → assumed productivity;
* commits increasing → assumed convergence;
* tests green → assumed correctness;
* queue empty → assumed completion.

This distinction is central.

---

# 27. FALSE PROGRESS AUDIT

Search explicitly for situations where apparent progress was measured through:

* agent count;
* token usage;
* number of tasks;
* completed task count;
* commit count;
* file count;
* test count;
* review count;
* process uptime;
* generations;
* prompt sophistication;
* documentation volume;
* requirements count;
* dashboards;
* orchestration layers.

Determine which were meaningful leading indicators and which became vanity metrics.

Ask:

> What metric would have revealed much earlier that useful software production was not converging?

---

# 28. TESTING RETROSPECTIVE

Analyse how tests were used.

Separate:

## Orchestration harness tests

Does the controller/state machine behave?

## Worker implementation tests

Does the local change behave?

## Integration tests

Does the combined system remain coherent?

## End-to-end tests

Does the intended user-level behaviour work?

## Independent acceptance

Does evidence prove the objective was actually achieved?

Determine whether large green test counts created false confidence.

Ask:

* Who wrote the tests?
* Did the implementer also write them?
* Could tests mirror implementation mistakes?
* Were mocks hiding missing runtime behaviour?
* Were infrastructure tests mistaken for product proof?

---

# 29. SELF-APPROVAL PROBLEM

Investigate pipelines where the same agent effectively:

1. interpreted the task;
2. implemented it;
3. wrote the tests;
4. ran them;
5. declared success.

Determine whether the architecture later evolved toward:

> Builder
> → Candidate
> → deterministic validation
> → independent reviewer
> → rejection/rework or acceptance
> → integration.

Identify which stages were actually enforced versus merely written in prompts.

---

# 30. REVIEWER RETROSPECTIVE

Analyse whether reviewers:

* were genuinely independent;
* had sufficient context;
* had sufficient evidence;
* could reject work;
* produced useful rework instructions;
* became bottlenecks;
* overused expensive models;
* checked architecture but not runtime;
* improved outcomes measurably.

Determine whether review was sometimes sophisticated without materially increasing completion throughput.

---

# 31. GIT AND WORKTREE RETROSPECTIVE

Analyse use of:

* single working tree;
* branches;
* isolated worktrees;
* cherry-picks;
* merge queues;
* worker-specific commits.

Determine what worktrees genuinely solved:

* concurrent modification;
* worker isolation;
* rollback;
* parallel work;
* preserving failed attempts.

Determine what they did not solve:

* correctness;
* requirements;
* meaningful tests;
* review;
* completion.

Do not over-credit infrastructure isolation.

---

# 32. MODEL AND PROVIDER RETROSPECTIVE

Track the use of relevant:

* FreeLLMAPI;
* Sol;
* Luna;
* Codex;
* Gemini;
* Claude;
* OpenRouter;
* ModelScope;
* other providers/models.

For significant changes identify:

* what problem prompted the switch;
* whether the existing system had been fairly tested;
* whether the new provider demonstrably improved outcomes;
* whether migration created new complexity.

Separate:

### model capability failures

from:

### orchestration failures

from:

### provider/runtime failures.

Ask:

> If one provider vanished halfway through a task, should the project itself have lost state?

Investigate the later principle:

> model/provider selection belongs to an Attempt, not to the durable Task.

---

# 33. HERMES / AMIS-SPECIFIC ANALYSIS

Analyse Hermes/Amis specifically.

What did it demonstrably do well?

Possibilities to investigate:

* bounded coding;
* code search;
* planning;
* review;
* debugging;
* repository understanding;
* decomposition;
* tool use.

What did it repeatedly struggle with?

Possibilities:

* extremely long autonomous missions;
* persistent project memory;
* knowing true completion;
* coordination across many sessions;
* recovering implicit state;
* managing nested agents;
* maintaining global consistency.

Determine whether Hermes was sometimes asked to function simultaneously as:

* coder;
* project manager;
* orchestrator;
* state store;
* scheduler;
* reviewer;
* process supervisor;
* recovery engine.

Ask:

> Was Hermes being treated as an entire software organisation rather than as an intelligent component within one?

---

# 34. PROMPT ENGINEERING AUDIT

Track how prompts evolved.

Look at:

* size;
* instruction count;
* nesting;
* role definitions;
* autonomy rules;
* anti-shortcut rules;
* completion rules;
* recovery rules;
* authority rules;
* testing rules;
* orchestration instructions.

Determine what prompting techniques genuinely helped.

Potential positives:

* explicit objectives;
* clear scope;
* acceptance criteria;
* inspect-before-change;
* evidence requirements;
* investigation before implementation;
* constraints;
* explicit forbidden actions.

Potential negatives:

* enormous prompts;
* too many roles;
* contradictory instructions;
* procedures trying to compensate for missing software;
* natural language pretending to be a state machine;
* repeatedly restating entire history;
* "continue until done" without machine-verifiable completion.

Do not conclude merely that "shorter prompts are better."

Determine:

> What belongs in the prompt?

and:

> What belongs in software/state?

---

# 35. MY OPERATING BEHAVIOUR

This section is extremely important.

Audit ME as the operator.

Look for repeated patterns such as:

* changing architecture after failure;
* adding another manager;
* adding another supervisor;
* rewriting prompts;
* switching frameworks;
* switching models;
* increasing autonomy;
* chasing new tools;
* manually restarting;
* repeatedly asking for audits;
* creating rescue prompts;
* responding to uncertainty with more specification;
* responding to unreliability with more hierarchy;
* attempting to remove myself from the loop too early;
* continuing experiments after useful information had already been obtained.

Do not moralise.

Understand the pattern.

---

# 36. REPEATED PATTERNS IN MY OWN BEHAVIOUR

For each recurring pattern provide:

### Pattern

What I repeatedly did.

### Historical examples

Where it happened.

### What I believed

Why it seemed sensible.

### Underlying need

What I was actually trying to solve.

### Why it helped or hurt

Evidence-based outcome.

### Replacement rule

The mental rule I should use next time.

Possible hypotheses to investigate:

* solving persistence with another AI;
* increasing hierarchy where deterministic state was needed;
* making prompts larger instead of improving state representation;
* redesigning before measuring the current system;
* treating new tools as likely solutions;
* changing too many variables simultaneously;
* overvaluing unattended execution;
* treating test quantity as success;
* trusting agent narration;
* under-measuring actual throughput.

Do not assume these are all true.

Test them.

---

# 37. HUMAN INTERVENTION AUDIT

Find situations where I had to:

* notice something had stopped;
* restart it;
* ask why;
* tell it to continue;
* restore context;
* decide the next task;
* reinterpret failures;
* find false completion;
* resolve deadlocks;
* choose provider/model;
* create another supervisor;
* write rescue prompts;
* manually inspect progress.

Classify each intervention as:

### Legitimate product-owner intervention

Human judgment appropriately required.

### Avoidable autonomy failure

The system should have handled it.

### Observability failure

I intervened because the system could not explain its state.

### Experimental intervention

I was deliberately steering an experiment.

Then ask:

> How autonomous was the system actually?

---

# 38. CHANGING DEFINITION OF AUTONOMY

Reconstruct what "autonomous" meant over time.

Did it mean:

* no prompts from me?
* no debugging?
* continuous running?
* surviving chat termination?
* surviving worker failure?
* surviving provider failure?
* surviving reboot?
* completing features?
* finishing the product?
* managing its own organisation?

Determine whether the goal silently expanded from:

> AI helps build software

to:

> AI independently runs an entire software engineering organisation.

If so, identify when.

---

# 39. THE AUTONOMY TAX

Estimate the engineering complexity introduced specifically to enable unattended autonomy.

Separate:

### Product work

### Autonomous-development work

### Meta-autonomy work

Examples of meta-autonomy:

* worker manager;
* supervisor;
* supervisor recovery;
* persistence layer;
* leases;
* recovery for leases;
* tests for controller;
* visualization of agent state;
* review infrastructure.

Estimate where possible:

* code;
* systems;
* repositories;
* services;
* prompts;
* debugging time;
* model usage;
* cognitive load.

Do not fabricate precise numbers.

Assess whether the autonomy benefit justified the tax at each stage.

---

# 40. COMPLEXITY EVOLUTION

Track the growth of:

* orchestration layers;
* agent roles;
* reviewers;
* state stores;
* queues;
* services;
* controllers;
* prompts;
* providers;
* databases;
* dashboards;
* worktrees;
* recovery mechanisms.

For each significant addition record:

1. Demonstrated failure that motivated it.
2. Hypothesis.
3. Complexity added.
4. Evidence it worked.
5. Evidence it was necessary.
6. New failure modes.
7. Whether retained.
8. Whether a simpler mechanism could have addressed the issue.

Create a conceptual:

> **Complexity vs useful-output curve.**

Identify the likely point of diminishing returns.

---

# 41. THE "ONE MORE ORCHESTRATOR" TRAP

Give this its own conclusion.

Determine whether the project entered a recursion:

> system unreliable
> → add orchestration
> → orchestration unreliable
> → add meta-orchestration
> → meta-orchestration unreliable
> → add deterministic supervision
> → supervision requires more infrastructure.

If so, identify where the recursion became counterproductive.

---

# 42. EXPERIMENTAL DISCIPLINE

Audit whether architectural changes behaved like controlled experiments.

For each major experiment ask:

* hypothesis?
* baseline?
* variable changed?
* success metric?
* failure metric?
* observation period?
* result?
* confounders?
* retained or reverted?
* what was learned?

Find experiments where many variables changed at once:

* model;
* provider;
* prompt;
* architecture;
* task structure;
* state mechanism;
* runtime.

Explain why such experiments made attribution difficult.

---

# 43. TOOL CHURN

Track changes involving:

* Hermes;
* Claude Code;
* Codex;
* CAO;
* Conductor;
* OpenHands;
* providers;
* routers;
* databases;
* supervisors;
* orchestration frameworks.

For each transition ask:

* What exact failure motivated it?
* Was the previous tool the actual cause?
* Was migration expensive?
* Did the new tool produce measurable improvement?
* Did tool-switching reset accumulated learning?

Look for:

> **new tool optimism.**

---

# 44. MODEL FAILURE VERSUS ARCHITECTURE FAILURE

For each important failure classify the primary layer.

### Layer 1 — Model capability

Model could not reliably perform the reasoning/coding task.

### Layer 2 — Context

Correct information unavailable or polluted.

### Layer 3 — Prompt/contract

Assignment poorly specified.

### Layer 4 — Task granularity

Work too broad, too narrow or badly decomposed.

### Layer 5 — Workflow

Sequence inappropriate.

### Layer 6 — Orchestration

Coordination failed.

### Layer 7 — State/persistence

Required project state was not authoritative/durable.

### Layer 8 — Infrastructure

Runtime/provider/process failure.

### Layer 9 — Verification

Bad work was accepted.

### Layer 10 — Experimental design

Architecture change was poorly measured.

### Layer 11 — Operator process

My decisions or intervention pattern materially contributed.

For each major failure ask:

> Was the solution applied to the same layer as the cause?

Identify misdiagnoses.

---

# 45. MISDIAGNOSED FAILURES

Search specifically for cases where I may have responded at the wrong level.

Potential examples:

* weak model output → added orchestration;
* context loss → added hierarchy;
* task too large → changed provider;
* product ambiguity → added managers;
* lack of validation → added planner;
* session death → tried to keep session alive rather than externalise state;
* queue exhaustion → assumed system complete;
* poor throughput → added parallel workers.

Document actual verified cases.

---

# 46. ARCHITECTURAL DECISION FORENSICS

Create a decision register.

For each major decision record:

| Field                   | Requirement |
| ----------------------- | ----------- |
| Approximate date        | Required    |
| Decision                | Required    |
| Observed problem        | Required    |
| Diagnosis at the time   | Required    |
| Evidence available then | Required    |
| Proposed solution       | Required    |
| Assumptions             | Required    |
| Expected result         | Required    |
| Actual result           | Required    |
| Improvement observed    | Required    |
| New problems            | Required    |
| Reversible?             | Required    |
| Retained?               | Required    |
| Current lesson          | Required    |

Include decisions such as:

* adopting Hermes;
* adding orchestrator;
* adding sub-orchestrator;
* adding supervisor;
* persistent manager;
* external watchdog;
* durable database;
* worktrees;
* leases;
* independent reviewers;
* deterministic controller;
* CAO;
* Conductor;
* provider changes;
* Autonomy Kernel;
* requirements ledgers;
* release gates.

---

# 47. EVIDENCE-DRIVEN VERSUS ANXIETY-DRIVEN CHANGES

For major architectural changes ask:

> Was there a concrete observed failure requiring this change?

or:

> Was I designing pre-emptively against theoretical failure?

This is not meant as a psychological judgment.

It is an experimental-methodology question.

Determine whether I sometimes attempted to eliminate entire classes of hypothetical failures before the basic happy path had been proven.

---

# 48. OBSERVABILITY

At each architecture stage ask whether I could answer:

* What work exists?
* Why does it exist?
* What is currently running?
* Is the process actually alive?
* Which Task does this Attempt belong to?
* What failed?
* Why did it fail?
* How many times?
* What is blocked?
* What is awaiting review?
* What is accepted?
* What is integrated?
* What remains?
* Why is the controller idle?
* Why does it believe work is complete?
* What human intervention is required?

Identify where poor observability caused me to compensate with:

* extra audits;
* extra managers;
* manual inspection;
* rescue prompts.

---

# 49. DETERMINISTIC RESPONSIBILITY VERSUS INTELLIGENT RESPONSIBILITY

One of the most important outputs should ans
...[TRUNCATED 3894 chars]...
es;
* explicit acceptance criteria;
* durable Task state;
* Task/Attempt separation;
* deterministic scheduling;
* independent review;
* structured worker output;
* event logs;
* runtime validation;
* provider fallback;
* checkpoints.

But verify them.

For each:

* problem solved;
* evidence;
* cost;
* limitations;
* keep/simplify/remove.

---

# 57. WHAT ONLY LOOKED LIKE IT WORKED

Identify systems that created the appearance of progress without dependable value.

Possible examples:

* persistent active manager;
* large test count;
* busy agents;
* task count moving;
* elaborate dashboards;
* many commits;
* hierarchy;
* large requirements ledger;
* watchdog repeatedly restarting an unhealthy workflow.

Prove these from evidence.

---

# 58. COMPLEXITY-VALUE TABLE

Create a table for major components:

| Component | Problem intended to solve | Complexity introduced | Evidence it solved it | Evidence it was necessary | New failure modes | Verdict |
| --------- | ------------------------- | --------------------- | --------------------- | ------------------------- | ----------------- | ------- |

Verdict may be:

* KEEP
* KEEP BUT SIMPLIFY
* CONTEXT DEPENDENT
* REMOVE
* UNPROVEN

Do not base the verdict on elegance.

Base it on evidence.

---

# 59. ROOT-CAUSE CHAINS

For the most important failures create causal chains.

Use:

**Observed symptom**

↓

**Immediate mechanism**

↓

**Underlying technical cause**

↓

**Systemic architecture cause**

↓

**Operator/process decision that allowed it**

↓

**Why it was not detected earlier**

↓

**What measurement would have exposed it sooner**

Do this for the most consequential recurring failures.

---

# 60. CONTRADICTION REGISTER

Find contradictions such as:

* "autonomous" but frequent human rescue;
* "complete" but controller merely had no work;
* "durable state" but critical state still lived in conversation;
* "independent review" but builder effectively approved own output;
* "controller driven" but live flow depended on LLM session;
* "recovery system" but restart lost current task meaning;
* "persistent manager" but manager death reset reasoning.

For each:

1. claims;
2. evidence;
3. actual behaviour;
4. why contradiction existed.

---

# 61. CORRELATION VERSUS CAUSATION

Be careful when determining that an architecture improved outcomes.

Potential confounders:

* stronger model;
* easier tasks;
* better codebase;
* smaller scope;
* improved prompt;
* more human intervention;
* different provider;
* accumulated knowledge.

Explicitly discuss alternative explanations for major claimed improvements.

---

# 62. QUANTITATIVE ANALYSIS

Where reliable data exists calculate or estimate:

* number of major architecture iterations;
* number of orchestration layers over time;
* worker attempts;
* successful attempts;
* failed attempts;
* timeout rate;
* no-change rate;
* review rejection rate;
* rework rate;
* human intervention rate;
* tool/provider switches;
* prompt revisions;
* worktrees;
* services;
* commits;
* tasks;
* time or effort spent on orchestration versus workload;
* cost where genuinely recoverable.

Do not fabricate data.

If unavailable say UNKNOWN.

Use ranges if appropriate.

---

# 63. FIND THE EARLIEST WARNING METRIC

Determine:

> **What one metric would have told us earliest that the methodology was not working?**

Potential examples:

* independently accepted engineering changes/day;
* % worker Attempts producing accepted outcomes;
* human interventions per accepted change;
* infrastructure effort/product effort ratio;
* average time from Task creation to accepted integration;
* repeated failure rate.

Do not assume.

Find the best metric from evidence.

---

# 64. FIND THE EXPERIMENT WE SHOULD HAVE RUN FIRST

Determine the smallest experiment that could have validated or falsified the early autonomous-system assumptions.

Use evidence.

Perhaps:

> One real bounded engineering task, repeated multiple times, measuring independent acceptance.

Perhaps something else.

Determine what would have produced maximum information with minimum infrastructure.

---

# 65. COUNTERFACTUAL LEARNING PATH

Construct a more efficient historical sequence.

Important:

Do NOT say:

> "We should simply have built today's architecture from day one."

Instead ask:

> Knowing only what was knowable at each point, what should the next smallest experiment have been?

Show how we could have learned the same lessons with less complexity.

---

# 66. FUNDAMENTAL PRINCIPLES VS CURRENT LIMITATIONS VS BUGS

Separate findings into:

## Fundamental system principles

Likely true even with better models.

## Current LLM limitations

May improve materially with future model capability.

## Hermes/Amis-specific limitations

Specific to the current runtime/tool.

## Implementation bugs

Accidental defects in one controller/system.

## Operator/process lessons

Things about how I ran the experiments.

Do not mix these categories.

---

# 67. WHAT DID THIS R&D TEACH THAT NORMAL AI CODING WOULD NOT HAVE?

Answer directly:

> **What did I learn through this expensive orchestration experimentation that I would not have learned simply using Claude/Hermes/Codex interactively to build the products?**

Distinguish:

### valuable R&D

from:

### avoidable detour.

Be specific.

---

# 68. WHAT SHOULD SURVIVE?

Identify the smallest set of:

* architectural concepts;
* code;
* operational practices;
* measurement techniques;
* prompting techniques;
* workflows;

that deserve to survive the retrospective.

Do not preserve things because they were expensive to build.

---

# 69. WHAT SHOULD DIE?

Identify things that should probably be abandoned completely.

Potential categories:

* unnecessary layers;
* fragile abstractions;
* recursive supervisors;
* organisational metaphors;
* over-large prompts;
* redundant state stores;
* systems retained mainly through sunk cost.

Be evidence-based.

---

# 70. STOP DOING

Create a precise list of behaviours I should stop.

Rules should be operational.

Examples of style:

> Do not add another orchestration level until a specific demonstrated failure requires it.

> Do not use agent activity as the primary progress metric.

> Do not keep project state solely inside LLM context.

> Do not change models and architecture simultaneously during a diagnostic experiment.

Generate the actual rules from evidence.

---

# 71. KEEP DOING

Identify behaviours worth preserving.

Possible areas:

* inspect before changing;
* explicit acceptance criteria;
* independent review;
* bounded experiments;
* preserving historical evidence;
* Git;
* root-cause analysis;
* separating investigation from implementation.

Again, verify from history.

---

# 72. DO EARLIER

Identify techniques introduced too late.

Possible examples:

* worker benchmark;
* intervention-rate measurement;
* runtime validation;
* deterministic state;
* Task/Attempt separation;
* independent acceptance;
* explicit stopping rules;
* product-vs-infrastructure metrics.

---

# 73. DO NOT OPTIMISE

Identify things that became seductive but were not good primary objectives.

Potential examples:

* keeping an AI session alive;
* maximising worker count;
* making the org hierarchy elegant;
* dashboards showing agent activity;
* eliminating all human involvement;
* maximum unattended runtime;
* perfect recovery before happy-path proof.

Base the final list on evidence.

---

# 74. ARCHITECTURAL STOPPING RULES

Create concrete future rules.

Format:

> Do not introduce X until Y has been demonstrated.

Examples of desired specificity:

> Do not add parallel workers until one worker repeatedly completes bounded Tasks with an acceptable independent-pass rate.

> Do not build elaborate recovery until the happy path is reliably proven.

> Do not add sub-orchestration unless measured coordination load exceeds what a single orchestrator can handle.

> Do not switch providers until the failure has been classified as provider/model-related.

Create rules derived from the actual history.

---

# 75. FUTURE EXPERIMENT PROTOCOL

Design a methodology for future autonomous-software experiments.

Do NOT design a massive production architecture.

Design the experimental sequence.

Possible conceptual progression:

### Stage 1 — Baseline worker

One agent, one bounded real task.

### Stage 2 — Repeatability

Same task class several times.

### Stage 3 — Independent validation

Measure actual pass rate.

### Stage 4 — Durable Task state

Terminate sessions deliberately.

### Stage 5 — Failure recovery

Kill workers deliberately.

### Stage 6 — Deterministic scheduling

Introduce only necessary control software.

### Stage 7 — Parallelism

Only after single-worker reliability is known.

### Stage 8 — Scale

Only when prior stages are proven.

Do not blindly copy this example.

Derive the final protocol from evidence.

---

# 76. FUTURE OPERATING DOCTRINE

Without building another architecture, answer:

### When should I use one agent?

### When should I add workers?

### When do I need an orchestrator?

### When is a deterministic workflow better than another LLM?

### When do I need durable state?

### When do I need independent review?

### When should humans remain in the loop?

### When should I deliberately NOT automate?

### What should be proven before adding complexity?

### What metrics should determine success?

### What should make me stop an experiment?

### What should make me simplify?

This must be practical.

---

# 77. DEFINE FUTURE SUCCESS

Success should NOT primarily mean:

* more agents;
* more tokens;
* more commits;
* more tasks;
* more layers;
* longer autonomous runtime;
* more green tests.

Define future success using measures such as:

* independently accepted useful changes;
* reliability;
* recovery;
* intervention rate;
* time-to-accepted-change;
* cost;
* repeatability;
* convergence;
* quality.

Develop evidence-based definitions.

---

# 78. REQUIRED FINAL REPORT

Produce one coherent report in this order.

## 1. Executive Summary

10–20 most important findings.

## 2. What the Experiment Really Was

Explain how product development evolved into an autonomous-software-factory R&D programme.

## 3. Master Timeline

Chronological reconstruction.

## 4. Architecture Generations

Show each significant architecture and why it appeared.

## 5. Star Force X as an Orchestration Experiment

Only evidence relevant to the methodology.

## 6. Nailify as an Orchestration Experiment

Only evidence relevant to the methodology.

## 7. Evolution of My Mental Model

What I believed at each stage and what changed.

## 8. Evolution of My Prompting

How instructions changed and why.

## 9. Context and Persistence Lessons

## 10. Task / Attempt / Worker Lessons

## 11. Delegation and Hierarchy Lessons

## 12. Controller and Deterministic-State Lessons

## 13. Recovery Lessons

## 14. Review and Validation Lessons

## 15. Liveness vs Activity vs Productivity vs Convergence

## 16. False Progress Analysis

## 17. Autonomy Tax

## 18. Complexity Curve

## 19. Tool and Model Churn

## 20. Hermes / Amis-Specific Lessons

## 21. My Human Operating Pattern

## 22. Repeated Mistakes in My Own Behaviour

Use:

* Pattern
* Historical evidence
* Why I did it
* Consequence
* Replacement rule

## 23. Misdiagnosed Problems

## 24. Major Root-Cause Chains

## 25. Architecture Decision Register

## 26. Contradiction Register

## 27. What Actually Worked

## 28. What Only Appeared to Work

## 29. What Was Over-Engineered

## 30. Fundamental Principles vs Model Limitations vs Bugs

## 31. What This R&D Genuinely Taught Us

## 32. What Should Survive

## 33. What Should Die

## 34. Stop Doing

## 35. Keep Doing

## 36. Do Earlier

## 37. Do Not Optimise

## 38. Architectural Stopping Rules

## 39. Better Experimental Sequence

## 40. Future Operating Doctrine

## 41. Minimum Necessary Capabilities

Conceptual capabilities only, NOT a full architecture.

## 42. What We Still Cannot Know

Explicit unknowns.

## 43. Quantitative Summary

Only where supported.

## 44. One-Page Final Doctrine

Compress everything into a document I can retain permanently.

---

# 79. REQUIRED FINAL QUESTIONS

Near the end, answer these questions directly.

## Question 1

> **What was the central reason my original autonomous-software approach repeatedly failed?**

One evidence-based answer.

## Question 2

> **Was the primary problem that I had not yet found the right orchestration architecture, or was I repeatedly trying to solve a problem whose orchestration complexity exceeded its practical benefit?**

Allow a nuanced answer if the history supports one.

## Question 3

> **What was the single biggest recurring mistake in how I responded to failure?**

## Question 4

> **What was the most important architecture insight I got right?**

## Question 5

> **What is the most important thing I learned specifically about using Hermes/Amis?**

## Question 6

> **What did this experimentation teach me that normal interactive AI coding would not have taught me?**

## Question 7

> **What is the smallest subset of the system worth carrying forward?**

## Question 8

> **What should be abandoned rather than improved further?**

## Question 9

> **What single metric should I monitor next time to make sure I am not confusing activity with progress?**

## Question 10

> **What should my default approach be the next time I want AI to autonomously build a significant software project?**

Do not turn Question 10 into a giant system design.

Give the operating principle.

---

# 80. FINAL PERSONAL LESSONS

End with:

# WHAT I SHOULD REMEMBER

Give me approximately 15–25 concise principles in plain English.

They should cover:

* AI capability;
* context;
* prompts;
* project state;
* workers;
* orchestration;
* deterministic software;
* testing;
* review;
* recovery;
* complexity;
* experimentation;
* human intervention;
* metrics;
* stopping rules.

No motivational language.

Make these operational.

Examples of the level of specificity wanted:

> A project must survive the death of every LLM session involved in it.

> A worker saying "done" is evidence to inspect, not completion state.

> Do not solve a state problem by adding another agent.

> Do not scale agent count before measuring single-worker reliability.

> Keep dynamic execution state outside the product charter.

These are examples only.

Derive the actual final principles from the evidence.

---

# 81. SECOND-PASS QUALITY CHECK

Before finishing, critically inspect your own retrospective.

Ask:

### Did I accidentally turn this into a Nailify/Star Force X product audit?

If yes, remove unnecessary product detail.

### Did I merely repeat previous AI-generated conclusions?

If yes, inspect deeper evidence.

### Did I identify how my own behaviour affected the experiments?

If no, investigate further.

### Did I distinguish model failures from architecture failures?

### Did I distinguish prompt failures from state failures?

### Did I distinguish process liveness from useful progress?

### Did I distinguish activity from convergence?

### Did I distinguish orchestration testing from actual autonomous-development performance?

### Did I identify false progress?

### Did I examine tool churn?

### Did I examine complexity growth?

### Did I identify whether each architectural layer solved a demonstrated problem?

### Did I identify places where several variables changed simultaneously?

### Did I avoid hindsight bias?

### Did I quantify what could genuinely be quantified?

### Did I clearly state uncertainty?

### Did I identify what actually worked?

### Did I challenge sunk-cost assumptions?

### Did I create practical stopping rules?

### Did I produce rules I could reuse months from now?

If not, continue the retrospective.

---

# 82. PROHIBITED LAZY CONCLUSIONS

Do NOT finish with unsupported statements such as:

> "We just need a better orchestrator."

> "We need more persistence."

> "We need more agents."

> "We need a better model."

> "We need more context."

> "We need more tests."

> "We need a more sophisticated architecture."

Any recommendation for additional complexity must be earned from evidence.

The evidence may instead show:

* simpler orchestration;
* fewer AI layers;
* bounded workflows;
* deterministic control;
* human-directed planning;
* disposable agents;
* limited parallelism;
* less autonomy;
* better measurement;
* stronger validation;
* or something else.

Let the evidence decide.

---

# 83. DO NOT CONFUSE SOPHISTICATION WITH SUCCESS

A technically sophisticated system can still be strategically wrong.

A complex controller can work exactly as designed while controlling the wrong thing.

A large test suite can perfectly validate an irrelevant abstraction.

A beautiful multi-agent organisation can have worse throughput than one good coding agent.

A durable system can persistently perform unproductive work.

A highly autonomous system can autonomously fail.

Keep these possibilities open throughout the investigation.

---

# 84. THE MOST IMPORTANT META-QUESTION

At every major point in the history ask:

> **What was I actually optimising?**

Classify the dominant objective:

* PRODUCT OUTPUT
* PRODUCT QUALITY
* AUTONOMY
* CONTINUITY
* ORCHESTRATOR RELIABILITY
* AGENT SCALE
* PROVIDER RESILIENCE
* INFRASTRUCTURE
* ARCHITECTURAL ELEGANCE
* EXPERIMENTAL LEARNING

Map how the dominant objective changed over time.

Identify when the goal shifted from:

> "Use AI to build software"

toward:

> "Build a system capable of autonomously building software."

Then determine whether that transition was deliberate and worthwhile.

---

# 85. THE FINAL TEST

The retrospective succeeds only if it leaves me with a better answer to:

> **How should I personally use autonomous AI software-development systems differently next time?**

Not:

> How should Nailify be fixed?

Not:

> How should Star Force X be fixed?

Not:

> How should I build an even larger AI organisation?

But:

> **What has this entire history taught me about the right way to design, test, measure, operate and constrain autonomous software-development systems?**

That is the subject.

---

# 86. FINAL EXECUTIVE CONCLUSION

Finish the entire report with exactly these five statements:

### 1. The central reason my original approach failed:

[One evidence-based paragraph.]

### 2. The most valuable thing the experiment taught me:

[One evidence-based paragraph.]

### 3. The biggest mistake in my operating approach:

[One evidence-based paragraph.]

### 4. The biggest thing the architecture got right:

[One evidence-based paragraph.]

### 5. The operating principle I should carry into my next AI software-development experiment:

[One concise principle.]

---

# FINAL INSTRUCTION

Do not build.

Do not fix.

Do not redesign.

Do not preserve an architecture because it was expensive to create.

Do not praise sophistication for its own sake.

Do not condemn experimentation merely because it failed to ship the workloads.

This may have been valuable R&D.

It may also contain substantial wasted effort.

Both may be true.

Your job is to discover:

> **What happened?**

Then:

> **Why did it happen?**

Then:

> **What did I learn?**

Then:

> **What should I personally do differently next time?**

Use Star Force X and Nailify as evidence.

Audit the **meta-project**.

Audit the **orchestration methodology**.

Audit **Amis/Hermes usage**.

Audit **my decision-making and operating patterns**.

Find what was fundamental.

Find what was accidental.

Find what genuinely worked.

Find what only looked like progress.

Find where complexity helped.

Find where complexity became the problem.

And leave me with a practical operating doctrine that prevents me from spending another enormous amount of time building the machinery for autonomous software development without first proving that the machinery actually increases reliable software production.
```

===== 2026-09-22 00:38 | session 20260921_234936_670e4e | prep for nailify =====
@file:.hermes/attachments/HERMES_NAILED_IT_MASTER_PROMPT_V3_AUTONOMOUS-4.md

if you where to plan out making this product autonomously, how would you do it learning what you have learnt?

--- Attached Context ---

📄 @file:.hermes/attachments/HERMES_NAILED_IT_MASTER_PROMPT_V3_AUTONOMOUS-4.md (26450 tokens)
```markdown
# HERMES MASTER IMPLEMENTATION PROMPT — NAILED IT MVP V3 — FULL AUTONOMOUS BUILD

> **V3 AUTONOMY-HARDENED REVISION — 18 September 2026**
>
> This revision keeps the detailed Nailed It product specification but replaces the old session-centric orchestration model with a durable, deterministic execution model.
>
> **Precedence rule:** if any older wording in this document conflicts with Sections 6–7, 58, or 68–71 of this revision, the newer autonomy-hardened wording wins.
>
> The intended operating result is:
>
> **one prompt → bootstrap persistent controller → controller owns the project → disposable Hermes workers implement/review/test → provider capacity is routed/retried automatically → failed gates create more work → the initiating Hermes session may disappear → project continues → only the deterministic release gate may declare SHIPPED.**
>
> The user is **not** part of the normal review loop. Routine implementation, debugging, provider switching, retries, QA rejection, rework, merging, visual review, and release verification are autonomous.


You are **Hermes Agent** acting as the autonomous product-engineering lead, senior React Native engineer, interaction designer, mobile QA lead, and technical project supervisor for an existing application.

Your job is **not** to give me advice, make a plan and stop, or build a separate proof of concept. Your job is to **take the existing project on my Desktop from its current state to a polished, genuinely usable MVP**, making the changes yourself, validating them, recovering across sessions, and continuing until the deterministic Definition of Done in this prompt is met. A truly external dependency is a persistent `WAITING_EXTERNAL` condition, not a project-ending failure: continue all independent work, keep the controller alive, periodically re-check the dependency, and resume automatically when it becomes satisfiable.

Read this entire prompt before changing code.

---

# 0. THE ONE-SENTENCE MISSION

Transform the existing **Nailify** prototype into **Nailed It**: a premium, user-friendly mobile nail-design app whose core experiences are:

1. an excellent **individual nail + full set designer**,
2. a convincing **live AR try-on** on the user's real hand,
3. a beautiful, coherent, production-quality mobile app shell around those two core features.

The MVP should feel like something a real consumer could download and enjoy, **not a developer demo, wireframe, debug tool, or UI kit showcase**.

---

# 1. WHERE THE PROJECT IS AND HOW TO TREAT IT

The project will be located at:

`~/Desktop/nailfy`

Important: the folder is intentionally named **nailfy**. Do not rename the folder unless there is a compelling technical reason.

The existing ZIP this prompt was derived from had this approximate structure:

- `~/Desktop/nailfy/app/` — real Expo / React Native app
- `~/Desktop/nailfy/mockup/` — older HTML prototype
- `~/Desktop/nailfy/nail presets/` — around 194 generated nail-look images, roughly 297 MB total
- `~/Desktop/nailfy/nailed it mock up inspo/` — around 16 visual-reference/mockup images, roughly 25 MB total
- `~/Desktop/nailfy/README.md`
- `~/Desktop/nailfy/CLAUDE_NAIL_EDITOR_PROMPTS.md`

Do not blindly assume that exact structure still exists. **Inspect first.** Determine the actual app root by locating `package.json`, `app.json`, and `src/`.

The current project is valuable. **Do not start from scratch. Do not create a new React Native project next to it. Do not throw away the existing renderer, design state, or AR placement logic just because a redesign is easier.** Refactor and migrate the existing project.

If the repository has no Git history, create Git history before major work:

- add a sensible `.gitignore`,
- initialize Git,
- make a clean baseline commit such as `chore: baseline before Nailed It v2 redevelopment`,
- optionally create a local source-only backup archive excluding `node_modules`, caches, build outputs, and generated temp files.

Never delete the original inspiration/preset source folders. Curate and optimize copies for the app bundle instead.

---

# 2. SOURCE-OF-TRUTH ORDER

When information conflicts, use this order:

1. **This prompt for the desired product and acceptance criteria.**
2. **The actual source code for what currently exists and how it works.**
3. User-owned visual inspiration files in `nailed it mock up inspo/` and usable nail imagery in `nail presets/`.
4. Existing README / old prompt packs only as historical context.

The existing README may overstate implemented functionality. Treat visible stubs, TODOs, simulated flows, and actual runtime behavior as the truth.

---

# 3. KNOWN STARTING STATE — VERIFY, DO NOT JUST TRUST

The source this prompt was written against was an Expo React Native application using approximately:

- Expo SDK 51
- React Native 0.74.x
- React 18
- React Navigation v6
- Zustand + AsyncStorage
- `react-native-svg`
- `react-native-gesture-handler`
- `expo-camera`
- `expo-haptics`
- `react-native-view-shot`
- MediaPipe Tasks Vision on web

Important current architecture/components that existed and should be inspected before replacement:

- `src/screens/DesignStudioScreen.js`
- `src/screens/ARTryOnScreen.js`
- `src/screens/HomeScreen.js`
- `src/screens/CatalogueScreen.js`
- `src/screens/ProfileScreen.js`
- `src/screens/OnboardingScreen.js`
- `src/screens/AIStudioScreen.js`
- `src/screens/DesignPreviewScreen.js`
- `src/screens/SendToSalonScreen.js`
- `src/screens/PaywallScreen.js`
- `src/components/NailSvg.js`
- `src/components/studio/EditorCanvas.js`
- `src/components/StudioPanels.js`
- `src/state/useDesignStore.js`
- `src/state/useAppStore.js`
- `src/state/useArStore.js`
- `src/data/shapes.js`
- `src/data/nailArt.js`
- `src/data/seedDesigns.js`
- `src/ar/placement.js`
- `src/ar/HandTracker.web.js`
- `src/ar/HandTracker.js`
- `src/theme/index.js`
- `src/theme/motion.js`

The existing source had approximately:

- 9 SVG nail shapes
- 3 fixed length levels
- 6 material categories
- around 47 coded/recolorable nail-art assets in 10 categories
- per-finger left/right hand state for 10 nails
- art and freehand-stroke layers
- move / scale / rotate placed art
- color-slot recoloring
- duplicate / reorder / delete layers
- 50-step undo/redo
- smart set operations such as copy-to-all, accent, ombré, French, alternating
- web MediaPipe hand tracking using 21-point hand landmarks
- shared AR placement math
- native hand-tracker file that was still a stub
- Firebase integration still stubbed
- RevenueCat integration still simulated
- AI generation still simulated/local
- sign-in still simulated
- search still largely a pressable placeholder
- some settings still placeholder toasts
- text tool visibly saying "coming soon"
- app branding still saying Nailify in many places
- no finalized app icon/splash asset package

Verify all of this in the actual `~/Desktop/nailfy` copy. If the code has advanced since then, preserve the better implementation.

---

# 4. NON-NEGOTIABLE PRODUCT PRIORITIES

This is an MVP, but "MVP" does **not** mean ugly, unfinished, or fake. It means a narrow product with a polished core.

Prioritize in this exact order:

## P0 — MUST BE EXCELLENT

1. Individual nail designer.
2. Full five-finger / ten-finger set creation using the individual nail designer.
3. Live AR try-on using the user's actual camera and real hand tracking on supported mobile devices.
4. Save, reopen, duplicate, rename, and continue editing designs locally.
5. High-quality app navigation, visual design, transitions, responsive layouts, touch ergonomics, empty states, errors, permissions, and polish.
6. A real Home / Explore / Create / Try-On / My Nails app experience around the builder.
7. Real export/share paths that do not lie about having completed an action.

## P1 — BUILD IF THEY STRENGTHEN THE CORE WITHOUT DESTABILIZING P0

- richer templates and curated inspiration
- salon-ready design summary / reference export
- more sophisticated nail effects
- saved individual-nail presets/components
- visual search inside the local library
- improved set-generation shortcuts
- appearance / haptics / accessibility settings

## P2 — DEFER FROM THIS MVP UNLESS ALREADY NEAR-COMPLETE AND ZERO-RISK

Do not let these distract from the core:

- social network/community feed
- creator monetization
- salon marketplace/directory
- appointment booking
- commerce/shop
- subscriptions/paywall
- cloud accounts if they are not needed to make the app usable
- production AI generation if credentials/back-end are not already available
- messaging
- notifications requiring server infrastructure
- complex 3D sculpting
- full professional salon CRM

**Do not expose half-built P2 features to users.** Remove them from navigation or label them internally as future work. A smaller app where every visible button works is far more valuable than a larger app full of simulations and "coming soon" pages.

---

# 5. THE CORE PRODUCT IDEA

The product is called **Nailed It**.

The promise is:

**Design it. Try it. Wear it.**

A user should be able to open the app with no design experience, create a beautiful set of nails quickly, refine individual fingers in detail, see the design convincingly on her own hand using the camera, save the set, and share/show it to a nail technician.

The design editor should ultimately feel like:

**Canva simplicity + a lightweight Procreate/Figma-style editing engine, specialized for nails.**

The key principle is **progressive disclosure**:

- a beginner sees a calm, simple interface,
- advanced controls appear only when relevant,
- the underlying engine can be powerful without showing 40 controls at once.

Never turn the phone screen into a cramped desktop editor.

---

# 6. AUTONOMY — THIS PROJECT MUST CONTINUE WITHOUT THE USER OR THE INITIATING CHAT

This is not a request for a long-lived conversational agent.

It is a request to turn the existing Nailed It project into a **durable autonomous software project** whose state, continuation, retries, QA, and release logic survive the death of every individual Hermes/LLM session.

The master prompt is the product constitution. It is **not** the runtime.

The hard operating principle is:

> **Do not try to keep one Hermes session alive long enough to finish Nailed It. Make the Nailed It project persistent enough that disposable Hermes sessions can finish it.**

And the second hard principle is:

> **Do not merely build an autonomy controller. Make that controller the actual live authority running this project, then prove the project continues without the Hermes session that created it.**

## 6.1 User involvement

The user is **not** part of the normal engineering loop.

Do not ask the user to:

- approve implementation details,
- choose routine libraries,
- approve retries,
- approve model/provider switches that remain within the authorized cost policy,
- review code,
- inspect screenshots,
- resolve ordinary merge conflicts,
- restart dead workers,
- say "continue",
- re-explain the project,
- decide whether a failed test should be fixed,
- approve rework after QA rejection.

For ordinary engineering ambiguity:

1. inspect the code and the authoritative product specification,
2. research current supported approaches when necessary,
3. choose the lowest-risk maintainable default,
4. record the decision,
5. continue.

If a decision is reversible, prefer making it autonomously.

If one optional feature is externally blocked, continue everything else.

## 6.2 No ordinary FAILED terminal state

For this project, the following are **not** terminal outcomes:

- worker crash,
- controller restart,
- Hermes session limit,
- context exhaustion,
- free-provider 429,
- free-provider quota exhaustion,
- subscription-provider cooldown,
- provider timeout,
- malformed model response,
- bad implementation,
- failing test,
- QA rejection,
- visual QA rejection,
- merge conflict,
- dependency conflict,
- failed clean build,
- failed acceptance predicate,
- no runnable task at this exact second.

All of those are project states that require retry, waiting, diagnosis, decomposition, rework, or provider rerouting.

The project state machine should conceptually include:

```text
BOOTSTRAPPING
RUNNING
WAITING_PROVIDER
WAITING_RETRY
WAITING_DEPENDENCY
WAITING_REVIEW
WAITING_INTEGRATION
WAITING_EXTERNAL
DIAGNOSING
RECONCILING
RELEASE_CANDIDATE
SHIPPED
CANCELLED_BY_USER
```

There is intentionally no normal `FAILED` terminal state.

A test failure means **create/fix work**.

A QA rejection means **rework**.

A rate limit means **cooldown/failover**.

A dead worker means **replace the Attempt, not the WorkItem**.

A dead initiating chat means **nothing special happens to the Project**.

`CANCELLED_BY_USER` may only occur through an explicit user cancellation, never because the agent becomes tired, uncertain, rate-limited, or runs out of context.

## 6.3 WAITING is allowed; stopping is not

Some resources may legitimately be temporarily unavailable.

For example:

- every authorized free endpoint is rate-limited,
- the linked ChatGPT/Codex subscription is temporarily at usage capacity,
- a retry timer is not yet due,
- a native build queue is busy,
- a dependency or review is still active.

In those cases the persistent controller enters an appropriate `WAITING_*` state, records why, sleeps/backoffs efficiently, and retries later.

It does **not** exit the project.

It does **not** write a failure report and stop.

It does **not** require the user to send another prompt.

When capacity returns, work resumes automatically.

## 6.4 Truly external blockers

A genuinely external condition may include:

- credentials that do not exist anywhere on the machine and cannot be created autonomously,
- a store/legal identity action requiring the owner's personal approval,
- unavailable signing ownership,
- unavailable physical hardware for a check that cannot be substituted by emulator/recorded-data validation,
- an irreversible external production action outside the authority granted by this prompt.

Even then:

- do not terminate the controller,
- record the condition as `WAITING_EXTERNAL`,
- continue every independent task,
- periodically re-check whether the condition has become satisfiable,
- use substitute deterministic evidence where technically legitimate,
- do not misrepresent an unverified condition as verified.

For this MVP, do not turn optional App Store/Play Store publication, paid services, cloud accounts, subscriptions, or optional AI generation into blockers for the local-first product.

## 6.5 A chat final response has zero project-control meaning

A Hermes worker saying `done` does not make a WorkItem done.

A reviewer saying `looks good` does not make a release pass.

The initiating Hermes session returning a final message does not end the Project.

Only durable project state plus deterministic acceptance evidence can produce `SHIPPED`.

The initiating session is explicitly allowed to terminate **after** it has commissioned and verified the persistent controller, because continuation must no longer depend on that session.

---

# 7. AUTONOMOUS EXECUTION ARCHITECTURE — THE CONTROLLER, NOT ASTRA, OWNS CONTINUATION

The old model in which a long-running "Astra" chat owned the queue is superseded.

Intelligent planner/reviewer sessions may still be given role names if useful, but **no LLM session is the supervisor of record**.

The supervisor of record must be ordinary persistent software.

The operating maxim is:

> **LLMs think. Software governs.**

## 7.1 Preserve the original source before coding

Before significant product changes:

1. preserve this entire prompt inside the project as an immutable source document, for example `.hermes/source/PRODUCT_CHARTER.md`;
2. record its SHA-256 hash;
3. preserve relevant existing README/prompt/reference files;
4. preserve the user-owned inspiration and nail-preset source directories;
5. record the baseline Git SHA.

Never reduce this prompt to a short summary and discard the original.

Final release reconciliation must return to the full original source.

## 7.2 Bootstrap a minimum autonomy kernel before full product implementation

The first engineering deliverable is not the visual redesign.

It is the minimal reliable execution kernel that will control the redesign.

Create a project-local control area conceptually like:

```text
~/Desktop/nailfy/.hermes/
  source/
    PRODUCT_CHARTER.md
    PRODUCT_CHARTER.sha256
  state/
    project.db
    events.jsonl
    controller-heartbeat.json
  autonomy/
    controller.*
    launcher.*
    provider_router.*
    reconciler.*
    workspaces.*
    verifier.*
    merge_queue.*
    acceptance.*
    schemas/
  packets/
  attempts/
  evidence/
  logs/
  reports/
  MASTER_PLAN.md
  REQUIREMENTS.md
  REQUIREMENTS.json
  ARCHITECTURE.md
  DECISIONS.md
  KNOWN_ISSUES.md
  QA_MATRIX.md
  CHANGELOG.md
  CHECKPOINT.md
```

Use SQLite in WAL mode for the authoritative local control-plane database unless the actual environment provides a clearly better already-running durable store.

Markdown/JSON files are useful human-readable projections, but they are **not** the sole authoritative state.

The durable data model should include at least:

```text
Project
Requirement
RequirementSource
WorkItem
Dependency
Attempt
Lease
Artifact
Evidence
Review
Event
ProviderEvent
Decision
ReleaseGate
```

A WorkItem persists.

An Attempt is disposable.

A model/session/provider is disposable.

## 7.3 Requirement compilation before broad implementation

Before broad implementation, compile this prompt into a durable requirement ledger.

Perform **at least two independent requirement-extraction passes** using separate fresh contexts.

Then reconcile them.

Every meaningful authoritative source item must become one of:

- mandatory requirement,
- constraint,
- acceptance criterion,
- reference,
- deliberate exclusion/deferment,
- superseded historical statement.

Assign stable IDs, for example:

```text
NAIL-P0-BUILDER-001
NAIL-P0-AR-014
NAIL-UX-031
NAIL-DATA-009
NAIL-AUTO-006
```

A requirement record should contain:

- ID,
- source location/section,
- description,
- priority,
- mandatory/deferred status,
- dependencies,
- acceptance criteria,
- verification method,
- implementation mapping,
- current state,
- evidence IDs.

No requirement may disappear merely because an agent forgot it.

## 7.4 Dependency-aware work graph

Compile the reconciled requirements into bounded WorkItems.

A WorkItem should contain approximately:

```text
id
title
requirement_ids[]
priority
phase
status
dependencies[]
files_or_modules_expected[]
prohibited_changes[]
acceptance_criteria[]
verification_commands[]
required_capabilities[]
preferred_model_tier
attempt_count
active_attempt_id
integration_state
review_state
```

Weak WorkItem:

```text
Build the nail editor.
```

Good WorkItem:

```text
Implement schema-v2 normalization for legacy Nail records.

Requirements:
NAIL-DATA-003, NAIL-DATA-004.

Allowed modules:
src/state/*
src/model/*
tests/migrations/*

Do not alter:
navigation, AR tracker, app identifiers.

Acceptance:
legacy fixture A opens without data loss;
current fixture B round-trips;
v2 fixture C round-trips;
migration is idempotent;
tests X/Y pass.
```

Cheap/free models become much more reliable when work is narrow.

Dependencies must be explicit, not remembered conversationally.

## 7.5 Persistent live controller

Create a long-running reconciliation process whose lifetime is independent of Hermes.

It must:

- read durable state,
- evaluate project state,
- recover expired leases,
- discover dead worker processes,
- inspect provider cooldowns,
- dispatch eligible WorkItems,
- schedule retries,
- launch reviewers,
- serialize controlled integration,
- run/re-run acceptance predicates,
- wake planner sessions when new decomposition is required,
- persist events before/after transitions,
- continue until `SHIPPED` or explicit user cancellation.

Conceptually:

```text
while project not SHIPPED and not CANCELLED_BY_USER:
    load durable state
    reconcile dead/expired Attempts
    reconcile provider availability
    ingest finished worker artifacts
    run due deterministic validations
    dispatch independent reviews
    integrate accepted work safely
    evaluate requirement/release predicates

    if acceptance FAIL:
        create/reopen WorkItems for failed predicates

    if incomplete and no eligible WorkItem:
        determine legitimate wait state
        or launch bounded planner/diagnostic WorkItem

    persist state + heartbeat
    sleep briefly / until next due event
```

`FAIL` feeds the loop.

It does not end it.

## 7.6 The controller must be kept alive by non-LLM infrastructure

Detect the host OS/environment and install the controller using an ordinary process manager that survives the launching shell/session.

Preferred options in order of environmental fit:

- Linux: user-level `systemd` service where available;
- macOS: `launchd` user agent;
- Windows: Task Scheduler / service-style user startup appropriate to available privileges;
- containerized environment: restart policy owned by the container runtime;
- otherwise: a documented OS-native watchdog/detached launcher plus a second health-check process.

Do not require root if a user-level service can do the job.

The controller must:

- auto-start/restart after its own crash where the OS supports it,
- write a heartbeat,
- persist logs,
- recover from machine/service restart,
- never require a Hermes session to remember to restart it.

Anything whose death would halt project continuation must not depend on an LLM remembering to relaunch it.

## 7.7 Commission the real execution path before trusting it

Do not merely write controller code and declare autonomy complete.

Commission the exact path that will run the project.

At minimum prove:

1. durable project row exists;
2. real controller process is running under non-LLM process management;
3. controller heartbeat advances independently;
4. controller can create a real commissioning WorkItem;
5. a real Hermes worker can claim it;
6. Attempt + lease are persisted;
7. kill that worker;
8. lease expiry/recovery is observed from durable state;
9. a replacement worker is dispatched;
10. result is verified;
11. deliberately trigger a deterministic test failure;
12. controller creates rework rather than stopping;
13. deliberately trigger a reviewer rejection;
14. controller creates rework rather than stopping;
15. deliberately restart/kill the controller process;
16. process manager restarts it;
17. state is reconstructed from the database;
18. project continuation resumes;
19. simulate provider 429/timeout;
20. provider moves to cooldown and work is retried/rerouted;
21. verify `no runnable work` produces a wait/diagnostic state rather than `SHIPPED`;
22. verify the controller process is no longer lifecycle-coupled to the initiating Hermes shell/session.

Do not test recovery only through mock functions that are different from production.

Evidence must come from independently observable facts such as:

- process IDs,
- service-manager state,
- database rows,
- timestamps,
- exit codes,
- Git SHAs,
- test output,
- screenshots,
- HTTP responses,
- provider error records.

The component under test must not simply write `PASS=true` and then have the gate trust that flag.

## 7.8 Hermes workers are disposable executors

Workers should normally be launched non-interactively with fresh bounded context.

Use the installed Hermes version's supported CLI.

Current Hermes generations support non-interactive queries, explicit provider/model selection, and isolated worktree workflows; verify the exact installed command syntax before automating it.

Prefer this execution shape:

1. controller creates an isolated Git worktree/branch;
2. controller writes a task packet to a file;
3. controller launches a fresh Hermes worker in that worktree using non-interactive/query-file mode;
4. worker reads only the bounded task packet plus relevant project files;
5. worker implements, tests locally, commits coherent work, and emits a machine-readable result;
6. controller records the Attempt outcome;
7. deterministic verification and independent review occur outside the implementer's authority;
8. accepted work enters the merge queue;
9. rejected work creates a new Attempt/rework WorkItem.

Do not depend on chat resume as the primary recovery mechanism.

Fresh sessions are preferred when context is stale or corrupted.

## 7.9 Worker task packet

Each worker packet should contain only what the job needs:

```text
PROJECT ID
WORKITEM ID
ATTEMPT ID
MISSION
WHY THIS EXISTS
REQUIREMENT IDS
ACCEPTANCE CRITERIA
RELEVANT ARCHITECTURE DECISIONS
DEPENDENCIES
RELEVANT FILES
ALLOWED/EXPECTED FILES
PROHIBITED CHANGES
TEST COMMANDS
EXPECTED ARTIFACTS
EXPECTED COMMIT FORMAT
KNOWN PRIOR ATTEMPT FAILURES
```

Do not dump the entire multi-thousand-line company history into every worker.

Store everything; inject almost nothing by default.

Retrieve only what that role needs.

## 7.10 Leases and death recovery

A worker claim uses a time-bounded lease.

Persist:

- WorkItem,
- Attempt,
- worker PID/session identifier where observable,
- worktree,
- branch,
- lease start,
- lease expiry,
- heartbeat,
- last coherent commit,
- dirty files,
- last validation output.

If heartbeat/lease expires:

1. mark the Attempt interrupted/expired;
2. preserve its artifacts/worktree;
3. inspect whether useful commits/diffs exist;
4. create a recovery packet;
5. launch a fresh worker;
6. continue the WorkItem.

Never delete useful partial work automatically.

Worker death is an ordinary state transition.

## 7.11 Isolated concurrency

Never let multiple implementation workers freely edit the same checkout.

Use:

- Git worktrees,
- isolated branches,
- or equivalent isolated workspaces.

The controller owns worktree lifecycle.

Start conservatively, typically 1–3 concurrent implementation workers depending on provider capacity, machine resources, and merge pressure.

Increase concurrency only when accepted WorkItem throughput improves.

Free-tier rate limits make uncontrolled agent swarms counterproductive.

## 7.12 Merge queue

Workers do not merge themselves directly into the canonical branch.

The controller/integration stage should:

1. verify expected commits/artifacts exist;
2. run deterministic tests;
3. run independent review;
4. ensure requirement evidence is attached;
5. rebase/merge in a controlled queue;
6. resolve simple conflicts deterministically where safe;
7. create a rework/integration WorkItem for nontrivial conflicts;
8. rerun affected tests after integration;
9. record integrated Git SHA.

A correct branch that breaks after merge is not accepted.

## 7.13 Automated independent review — no user review required

The user should not be asked to review this project.

But the implementer also cannot be its own sole judge.

Required lifecycle:

```text
IMPLEMENT
  ↓
DETERMINISTIC TESTS
  ↓
FRESH INDEPENDENT REVIEW
  ↓
ACCEPT ──→ INTEGRATION
  │
  └── REJECT → REWORK → repeat
```

Reviewers receive:

- requirement IDs,
- acceptance criteria,
- relevant architecture constraints,
- implementation diff,
- deterministic evidence,
- screenshots/runtime artifacts when relevant.

They do **not** need the implementer's entire conversation.

Use stronger intelligence for reviews where errors would compound:

- schema migrations,
- persistence/data-loss,
- AR/native camera architecture,
- security/privacy,
- large navigation/state changes,
- final builder review,
- final release reconciliation.

If reviewer capacity is temporarily exhausted, leave review pending, continue independent tasks, and retry automatically later.

Review unavailability is a wait state, never project failure.

## 7.14 Visual QA is mandatory

Nailed It is a visual consumer beauty app.

Passing unit tests cannot establish that it looks premium.

For every significant visual milestone:

- launch the actual app where practical,
- render representative phone widths,
- capture screenshots,
- inspect them using an independent vision-capable reviewer,
- compare against the product charter and provided inspiration,
- create explicit visual rework when the result looks like a developer tool, is cramped, misaligned, inconsistent, low-quality, or visually broken.

Screenshots are evidence only if tied to the current build/Git SHA.

Do not let an old screenshot prove a newer release.

## 7.15 Runtime/browser/device QA

Use the strongest practical automation available in the environment.

Prefer real runtime journeys over static file inspection.

For mobile-native paths:

- compile real native development/release candidates,
- use emulator/simulator where available,
- use prerecorded hand-video/frame fixtures to exercise the native tracking and placement pipeline deterministically,
- use real hardware automatically if accessible to the environment.

If physical hardware is unavailable, do not halt the entire project merely to wait for a person. Use the strongest legitimate substitute evidence available, record the physical-device limitation precisely, and do not fabricate success.

## 7.16 Provider and model policy — minimise marginal cost while never terminating the project

The objective is:

> **Use the cheapest adequate intelligence for each bounded task, preferably zero-marginal-cost inference, while preserving automatic fallback and project continuation.**

Do not interpret cost control as "fail closed."

### Authorized provider tiers

#### Tier A — primary: FreeLLMAPI / existing zero-cost API routing

Inspect the machine's existing Hermes/provider configuration and credentials.

Use the already-authorized **FreeLLMAPI** OpenAI-compatible route as the primary implementation pool.

Do not overwrite unrelated global Hermes configuration unnecessarily.

Where possible, create project-local routing/config so this project can consistently select the intended provider/model.

At bootstrap:

- verify endpoint connectivity,
- discover available model IDs where the endpoint supports model listing,
- record context/tool/vision capabilities,
- perform a tiny coding/tool-call smoke test,
- classify models into worker roles.

Use zero-cost models for:

- bounded implementation,
- test fixes,
- repetitive refactors,
- metadata/catalogue work,
- straightforward UI components,
- simple documentation,
- requirement extraction passes where quality is adequate.

If Hermes exposes other **already available zero-cost providers** with no signup, payment, or marginal charge, they may be used as supplementary Tier-A routes after validation.

#### Tier B — linked ChatGPT/Codex subscription

The Hermes installation already has an authorized ChatGPT/Codex subscription route.

Treat this as a **zero-additional-metered-cost stronger fallback**, not as a forbidden path.

Use it when any of the following applies:

- architecture/decomposition where mistakes would cascade,
- native AR/camera integration,
- difficult debugging,
- repeated free-model engineering failure,
- requirement reconciliation,
- high-risk migration review,
- security/privacy review,
- final visual/release review,
- free providers are temporarily exhausted and useful progress would otherwise stall,
- a task requires capabilities unavailable in the current free-model pool.

Do not assume a specific model string if the installed Hermes provider catalog differs.

Inspect the configured Codex/ChatGPT provider and use the strongest suitable model that is actually available through that linked subscription.

Preserve subscription capacity by not using it for trivial mechanical edits when Tier A is working well.

#### Tier C — metered paid APIs

Do **not** silently start spending money on metered pay-per-token APIs.

A provider that can incur new monetary charges is unauthorized unless an existing explicit project configuration proves it is zero-cost for this user or the user separately authorizes spend.

If Tier A and Tier B are both temporarily unavailable:

- enter `WAITING_PROVIDER`,
- back off,
- periodically retry,
- continue deterministic/local work that does not require inference,
- resume automatically when capacity returns.

The project waits; it does not fail.

### Provider failure classification

Classify separately:

```text
RATE_LIMIT
QUOTA_EXHAUSTED
AUTH_TRANSIENT
AUTH_MISSING
TIMEOUT
PROVIDER_5XX
MALFORMED_RESPONSE
CONTEXT_LIMIT
TOOL_PROTOCOL_ERROR
ENGINEERING_FAILURE
REVIEW_REJECTION
```

Provider failures should normally cause:

```text
same provider retry
  ↓
smaller/fresher context
  ↓
alternate authorized zero-cost model/provider
  ↓
linked Codex/ChatGPT subscription
  ↓
cooldown / WAITING_PROVIDER
  ↓
automatic retry when due
```

Engineering failures should normally cause:

```text
inspect evidence
  ↓
decompose more narrowly
  ↓
fresh worker
  ↓
stronger model tier if repeated
  ↓
retest
```

Never conflate a 429 with a bad code implementation.

## 7.17 Adaptive escalation policy

Use task history rather than emotion.

A practical policy:

- Attempt 1: cheapest adequate Tier-A worker.
- Provider-only failure: retry/failover without counting it as an engineering failure.
- First engineering rejection: fresh Tier-A worker with reviewer feedback.
- Repeated engineering rejection or difficult integration: stronger Tier-A model if available.
- High-risk or repeatedly unsuccessful task: Tier-B Codex/ChatGPT subscription.
- If Tier B is temporarily exhausted: persist state and retry later; do not abandon the WorkItem.

Exact thresholds may be tuned by observed success rates.

The controller should record first-attempt acceptance and rework rate so routing improves over time.

## 7.18 Deterministic work should not consume LLM tokens

Use ordinary tools for ordinary facts.

Examples:

- `git status`,
- hashes,
- dependency graph state,
- elapsed lease time,
- retry due time,
- tests,
- lint,
- builds,
- file existence,
- package versions,
- process liveness,
- screenshot capture,
- database queries,
- exact search/replace,
- archive generation.

Do not spend inference on questions software can answer exactly.

## 7.19 Provider/budget enforcement is technical, not prose

Create a project provider policy that the controller actually enforces.

It should include:

- authorized providers,
- authorized provider classes,
- whether each has marginal monetary cost,
- concurrency caps,
- cooldowns,
- escalation rules,
- task/model capability mapping,
- optional daily/weekly usage observations.

Do not merely tell workers "please avoid paid models."

Launch workers with explicit provider/model parameters or project-specific config so accidental metered routing is mechanically prevented where practical.

## 7.20 Checkpoints describe engineering state, not model thoughts

Maintain `.hermes/CHECKPOINT.md` as a readable projection of durable state.

It should contain:

- current Project state,
- current canonical Git SHA,
- active WorkItems/Attempts,
- latest accepted WorkItems,
- pending reviews,
- failing gates,
- provider cooldowns,
- dirty/recovery worktrees,
- exact next controller actions.

Do not attempt to preserve hidden chain-of-thought.

Persist resumable engineering facts.

## 7.21 Git is institutional memory

If no Git history exists, initialize it before major work.

Make small coherent commits.

Commit messages should include or be traceable to WorkItem IDs where practical.

Hours of useful progress must never exist only in an LLM context.

## 7.22 Capability registry

Record capabilities for available execution routes, for example:

```text
terminal
filesystem
git
web research
browser automation
vision/image review
Android emulator
iOS simulator
native build
database
image processing
deployment
```

Route tasks only to workers that possess what the task requires.

Do not assign visual QA to a text-only model.

## 7.23 Controller self-protection

Product workers must not casually rewrite the live control plane.

Once commissioned:

- protect `.hermes/autonomy/` from ordinary product WorkItems,
- require a dedicated controller-maintenance WorkItem and independent review for control-plane changes,
- keep provider policy, release predicates, and evidence rules out of ordinary UI feature edits.

Do not let a worker "solve" a hard product task by weakening tests, disabling security, deleting acceptance conditions, or changing the release gate.

## 7.24 Product-progress metrics

Track meaningful progress such as:

- accepted WorkItems,
- integrated requirements,
- mandatory requirements remaining,
- blocked/waiting requirements,
- QA rejection rate,
- rework ratio,
- regressions,
- visual QA failures,
- unrecovered worker deaths,
- provider wait time,
- Tier-A vs Tier-B inference usage,
- human interventions.

Do not treat:

- agent uptime,
- number of messages,
- token volume,
- number of sessions,
- number of generated files

as proof of progress.

## 7.25 Acceptance failure automatically generates work

Every failed release predicate must map to:

- an existing incomplete WorkItem,
- a reopened WorkItem,
- or a newly created bounded remediation WorkItem.

Then the controller schedules it.

The bad loop is:

```text
gate fails
→ explain failure
→ stop
```

The required loop is:

```text
gate fails
→ identify failed predicate
→ map to requirement
→ create/reopen work
→ implement
→ test
→ review
→ integrate
→ rerun gate
→ repeat
```

## 7.26 No runnable work is not completion

If nothing is immediately runnable, the controller must distinguish:

- waiting for provider,
- waiting for retry time,
- waiting for dependency,
- waiting for review,
- waiting for integration,
- waiting for process recovery,
- need for diagnostic/planning work,
- actual release candidate.

Only deterministic release predicates can produce `SHIPPED`.

## 7.27 Final authority

No planner, worker, reviewer, or chat response may override the release gate.

`SHIPPED` is a derived state.

It must be tied to:

- current release Git SHA,
- mandatory requirement coverage,
- current deterministic test/build evidence,
- current runtime evidence,
- current visual evidence,
- independent review evidence,
- no blocking P0 defects,
- final reconciliation against the full original PRODUCT_CHARTER.

---

---


# 8. PHASE 0 — AUDIT AND BASELINE BEFORE REDESIGN

Before changing product behavior:

1. Locate the true app root.
2. Record platform/Node/npm versions.
3. Run current install and baseline validation.
4. Launch the app on every practical target available in the environment.
5. Capture screenshots or screen recordings of major current screens if tooling allows.
6. Inventory routes, stores, components, design model, asset library, and AR flow.
7. Search all source for:
   - TODO
   - FIXME
   - stub
   - simulated
   - mock
   - coming soon
   - placeholder
   - hard-coded demo user data
   - fake purchase/login messages
8. Inspect `nail presets/` and `nailed it mock up inspo/` visually, preferably using contact sheets so you can understand the collection efficiently.
9. Identify which existing modules are **KEEP / MODIFY / REPLACE / REMOVE FROM MVP**.
10. Write the result into `.hermes/ARCHITECTURE.md` and `.hermes/MASTER_PLAN.md`.

Do not spend days documenting. The audit should be enough to prevent accidental rewrites and then implementation should begin.

---

# 9. BRAND MIGRATION — NAILIFY → NAILED IT

The user-facing brand is **Nailed It**.

Replace visible product branding consistently:

- onboarding
- headers
- splash
- app display name
- share text
- export text
- design attribution
- empty states
- settings/about
...[TRUNCATED 45919 chars]...
s/recovery,
- implement verifier/reviewer/merge queues,
- install controller under a non-LLM process manager,
- commission the real path with destructive recovery tests,
- prove controller restart recovery,
- prove worker death recovery,
- prove provider 429/cooldown recovery,
- prove failed tests/reviews create rework,
- prove no-runnable-work does not become complete.

Only when the live controller is demonstrably authoritative should the full product build proceed.

## Phase 0 — Product baseline + requirement compilation

- locate real app root,
- audit source/assets/runtime,
- baseline screenshots,
- two independent requirement extraction passes,
- reconciliation into stable requirement IDs,
- KEEP / MODIFY / REPLACE findings,
- architecture decisions,
- dependency-aware WorkItems.

## Phase 1 — Foundation

- Nailed It brand rename
- new tokens/visual system
- navigation architecture
- remove fake/stubbed user paths from visible MVP
- app icon/splash foundation
- motion infrastructure

## Phase 2 — Design model + local project library

- schema v2
- migration
- project save/autosave/reopen/duplicate/delete
- preserve existing nail renderer compatibility

## Phase 3 — Builder UX rebuild

- calm single-nail editor layout
- finger strip
- tool dock/sheets
- selection and gestures
- undo/redo
- base/shape/length

## Phase 4 — Builder depth/content

- finishes
- French
- gradients
- expanded art library
- draw/eraser
- text
- layers
- smart set operations
- curated templates

## Phase 5 — AR

- native tracking architecture
- landmark feed
- smoothing
- per-finger overlay
- fit UX
- consumer AR screen
- permission flows
- capture/share
- deterministic prerecorded hand-sequence tests
- native emulator/device validation where available

## Phase 6 — App shell completion

- Home
- Explore search/filter/detail
- My Nails
- Settings/About
- onboarding
- standard states

## Phase 7 — Asset/polish/performance/accessibility

- curated images
- optimize bundle
- microinteractions
- responsive edge cases
- accessibility
- haptics/reduced motion
- loading/error/empty states
- screenshot-based independent visual review

## Phase 8 — Hardening and release reconciliation

- clean final test sweep
- migration tests
- native build verification
- runtime journey verification
- screenshot/visual QA at representative sizes
- dead code/stub cleanup
- docs
- all pending reviews
- full charter-to-product reconciliation
- deterministic release checklist
- controller commissioning evidence current
- final release-candidate commit
- release gate rerun against that exact commit

Do not wait until Phase 8 to test.

Every accepted WorkItem must carry evidence as it moves through the controller.

---

# 59. KEEP / MODIFY / REPLACE GUIDANCE FROM THE KNOWN CODEBASE

Use your audit to confirm, but the likely direction is:

## KEEP AND EXTEND

- `NailSvg` rendering concept
- existing SVG nail shape paths that look good
- normalized per-finger design state
- art asset model
- undo/redo concept
- `EditorCanvas` gesture concept
- `useArStore` global/per-nail fit idea
- shared `placement.js` if the math is sound
- web MediaPipe implementation if stable
- export helpers that genuinely work
- well-made reusable UI primitives

## MODIFY HEAVILY

- `useDesignStore` into a version-aware editor/project architecture
- art library/category system
- nail material rendering
- filmstrip
- layer UI
- theme/motion
- navigation
- catalogue data presentation

## VISUALLY / UX-WISE REPLACE

- current crowded `DesignStudioScreen` composition
- current AR debug-like HUD
- prototype Home layout
- prototype Profile layout
- simulated onboarding/account flow
- separate fake AI Studio from navigation
- fake Paywall flow from navigation

## REMOVE FROM NORMAL MVP PATH

- any fake login
- fake purchases
- fake AI network behavior
- "coming soon" text tool
- fake search
- simulated camera masquerading as production AR

---

# 60. BUILDER MICRO-INTERACTION SPEC

Be deliberate about details:

- On press, asset tiles compress very slightly then release.
- When art is added, it appears at ~95% scale and settles to 100% over ~150–220 ms.
- Selection border appears without shifting the asset.
- On center snap, guide fades in and haptic ticks once.
- When changing finger, the new focused nail crossfades/settles instead of blinking.
- Undo causes a subtle content settle, not a giant bounce.
- Color swatches show selected state with both border/check/size change so selection is not color-only.
- Continuous color picking updates live.
- Bottom sheet remembers reasonable height per tool but should not cover the whole nail unless the user expands it.
- Dragging sheet should feel native.
- When a user adds a tool then returns to canvas, selection remains clear.
- Deleting selected layer selects the next logical remaining layer or clears selection.
- Reordering layers updates canvas immediately.
- "Apply to all" must say exactly what will change.
- Save feedback should not use a generic intrusive toast for every autosave.

---

# 61. COPY / LANGUAGE STYLE

Use concise beauty-product language.

Good examples:

- Create a set
- Start from a blank set
- Try on
- Adjust fit
- Apply to all nails
- Copy to this hand
- Save to My Nails
- Continue editing
- Use this look
- No designs yet

Avoid:

- "canvas object"
- "landmark tracker"
- "apply designData"
- "location mockup"
- "preview scaffold"
- "AI network stub"
- overly cute copy on every screen

---

# 62. APP ICON / SPLASH / LAUNCH QUALITY

Before final completion:

- create a real 1024x1024 app icon source
- generate platform-appropriate icon config
- create splash/launch artwork
- ensure splash background exactly matches first rendered app background
- ensure no old Nailify text appears during launch
- update app display name to Nailed It
- verify Android/iOS identifiers are not accidentally broken

If changing scheme from `nailify` would break existing links and is unnecessary for MVP, keep technical scheme and document it.

---

# 63. DEVELOPMENT / DEBUG MODE

Keep useful engineering tools without exposing them to users.

Behind `__DEV__` or a dedicated developer setting you may retain:

- simulated AR scene
- landmark visualization
- AR calibration diagnostics
- FPS/debug stats
- reset local storage
- seed data reload

Production paths must hide these.

---

# 64. LOGGING

Use structured, restrained development logging.

Do not log every camera frame.

For important failures log:

- storage migration failure
- tracker initialization failure
- camera permission/runtime error
- export failure
- unrecoverable asset/model load failure

Production UI gets a human-readable recovery message.

---

# 65. WHAT NOT TO DO

Do not:

- build a completely new app in another folder
- replace editable nail JSON with flattened PNG-only designs
- make every nail effect an external AI-generated image
- hard-code all 10 nails independently in components
- use dozens of unmaintained dependencies
- add social/community/commerce before the builder and AR are excellent
- keep visible fake Pro/paywall logic
- leave buttons that only toast "coming soon"
- put 50 controls on the Studio screen simultaneously
- use emojis instead of a coherent icon system
- use placeholder lorem ipsum or dummy user identities in production screens
- destroy existing persisted designs
- claim physical-device AR success without testing an actual native/dev build
- stop at a report when implementation can continue

---

# 66. QUALITY BAR / VISUAL REVIEW QUESTIONS

At each milestone, inspect the app and ask:

- Does this look like a beauty app a customer would pay attention to, or a developer tool?
- Is the nail itself the visual hero?
- Can a new user create something attractive in under a minute?
- Can an advanced user make every finger different?
- Is any control too small or too technical?
- Are there any fake or dead controls?
- Does every screen have a clear primary action?
- Are photo/assets sharp and consistent?
- Is typography coherent?
- Are route transitions smooth?
- Does the app feel like one product rather than ten differently styled screens?
- Does AR look attached to the hand rather than floating?
- Can I leave and reopen without losing work?

If the answer is no, keep iterating.

---

# 67. MANDATORY ACCEPTANCE TEST — 10-MINUTE USER STORY

Before calling the MVP done, a fresh user should be able to complete this flow without developer knowledge:

1. Install/open Nailed It.
2. Finish/skip onboarding.
3. Tap Create.
4. Start a blank set.
5. Choose almond nails.
6. Choose a medium/long length.
7. Make the index nail a soft pink base.
8. Add a white flower.
9. Reposition and resize it by touch.
10. Add a small gold accent/gem.
11. Copy the nail to another finger.
12. Change another finger to a French variation.
13. Make one accent nail glitter/chrome.
14. View the whole set.
15. Undo and redo an edit.
16. Save the set as a named design.
17. Exit to My Nails.
18. Reopen it and verify the exact design is preserved.
19. Tap Try On.
20. Grant camera permission.
21. Put a hand into frame.
22. See the correct per-finger designs track the nails/fingers.
23. Move/rotate the hand and see stable tracking.
24. Adjust fit if needed.
25. Capture/share or save a result.
26. Return to the editor with state intact.
27. Close/relaunch the app and find the design still in My Nails.

No fake success is allowed in this story.

---

# 68. DEFINITION OF DONE — ONLY THE RELEASE GATE MAY SET SHIPPED

Do not declare `SHIPPED` until all applicable P0 items below are true **for the current release Git SHA**.

A worker's claim is not evidence.

A reviewer's prose alone is not evidence.

A stale screenshot is not evidence for a newer commit.

Where the environment makes one form of evidence unavailable, use the strongest legitimate substitute evidence, record the limitation precisely, and never fabricate success.

## Autonomous execution

- [ ] Full product charter is preserved and hashed.
- [ ] Requirement ledger was produced from at least two extraction passes and reconciled.
- [ ] Every mandatory P0 requirement has stable traceability to implementation and evidence.
- [ ] Persistent control database exists and is current.
- [ ] Live controller runs outside the initiating Hermes session.
- [ ] Controller is managed/restarted by non-LLM infrastructure.
- [ ] Worker leases and expired-Attempt recovery have been proven on the real path.
- [ ] Controller restart recovery has been proven on the real path.
- [ ] Provider rate-limit/cooldown recovery has been proven.
- [ ] QA rejection creates autonomous rework.
- [ ] Acceptance failure creates autonomous remediation work.
- [ ] "No runnable task" cannot set SHIPPED.
- [ ] No routine user "continue" messages or human code reviews were required.
- [ ] No unauthorized metered paid inference was used.
- [ ] Provider/model usage and cooldown history is recorded.
- [ ] Final release evidence is tied to the exact release-candidate commit.

## Product

- [ ] User-facing brand is Nailed It.
- [ ] App launches into polished onboarding/home, not scaffolding.
- [ ] Home, Explore, Create, Try On, My Nails all work.
- [ ] Real search works in Explore.
- [ ] No visible placeholder/coming soon/simulated messaging.

## Builder

- [ ] Focused individual nail editing is clear and uncluttered.
- [ ] All 10 nails can hold different designs.
- [ ] Shape and length work.
- [ ] Solid color and gradient work.
- [ ] Major finishes are visibly distinct.
- [ ] French builder works.
- [ ] Art library is substantial and high-quality.
- [ ] Art can be moved/scaled/rotated/recolored/duplicated/deleted/reordered.
- [ ] Drawing and erasing work.
- [ ] Text either truly works or is absent; no placeholder.
- [ ] Layers work.
- [ ] Undo/redo works without history spam.
- [ ] Copy/mirror/set helpers work.
- [ ] Save/autosave/reopen works.
- [ ] Existing old stored designs migrate safely.

## AR

- [ ] Camera permissions are production quality.
- [ ] Native supported build uses real hand-landmark implementation; no native stub.
- [ ] Correct per-finger designs render from the same canonical design state.
- [ ] Hand tracking is smoothed/stable in deterministic test sequences.
- [ ] Lost tracking degrades gracefully.
- [ ] Fit controls are available but not intrusive.
- [ ] AR screen looks like a consumer camera experience.
- [ ] Capture/share path is verified or truthfully disabled if the target platform genuinely cannot support it; no fake output.
- [ ] Native code compiles in the supported target environment.
- [ ] Native AR pipeline is tested with emulator/device and/or deterministic prerecorded hand frames according to available capabilities.

## Visual / UX

- [ ] Cohesive premium design system.
- [ ] Real app icon/splash.
- [ ] High-quality curated visual assets.
- [ ] No emoji UI icons.
- [ ] Navigation transitions are coherent.
- [ ] Bottom sheets / finger switching / adding art have polished motion.
- [ ] Small phone layouts are usable.
- [ ] Basic accessibility and reduced motion work.
- [ ] Independent screenshot/vision review has passed representative key screens.
- [ ] Visual evidence corresponds to the current release commit.

## Engineering

- [ ] Git history and coherent WorkItem-linked commits exist.
- [ ] No critical TODO/stub is reachable in P0 flows.
- [ ] Clean lint/build/test pipeline passes to the extent supported by the target environment.
- [ ] Pure migration and AR placement/filtering logic has automated coverage.
- [ ] Storage migration is idempotent and preserves recoverable legacy data.
- [ ] No main P0 flow depends on fake backend/account/payment behavior.
- [ ] README reflects actual behavior.
- [ ] `.hermes/QA_MATRIX.md` records final validation.
- [ ] `.hermes/KNOWN_ISSUES.md` contains only genuine non-blocking limitations.
- [ ] No unresolved mandatory P0 requirement is hidden in KNOWN_ISSUES.

---

# 69. FINAL AUTONOMOUS REVIEW AND RELEASE PROCESS

The user does not need to review this release.

Before `SHIPPED`, the controller must autonomously orchestrate all of the following:

1. Freeze a release-candidate Git SHA.
2. Run clean dependency/install validation.
3. Run lint/type/syntax/build checks applicable to the repository.
4. Run unit/integration/store/migration/AR math tests.
5. Run native build verification appropriate to the available environment.
6. Run the mandatory 10-minute user story using the strongest runtime automation available.
7. Capture current screenshots at representative small and large phone sizes.
8. Run independent visual review against the product charter/inspiration.
9. Run a fresh independent code review of the full P0 release diff.
10. Specifically review data migration, storage, deletion, permission handling, camera/AR frame path, privacy, and performance-sensitive paths.
11. Search again for TODO/FIXME/stub/simulated/coming soon/placeholder.
12. Search visible strings for `Nailify`; classify each remaining occurrence as safe internal legacy or fix it.
13. Search visible strings and routes for fake Pro/purchase/subscription/login/AI behavior.
14. Reconcile the **full original PRODUCT_CHARTER** against the actual current app, not merely against the requirement ledger.
15. For every discovered gap, create/reopen remediation WorkItems and continue the loop.
16. After remediation, create a new release-candidate SHA and repeat affected release checks.
17. Verify no blocking P0 defects remain.
18. Verify release evidence provenance points to the final candidate SHA.
19. Run final deterministic release predicates.
20. Only if every mandatory predicate passes, atomically set Project state to `SHIPPED` and write the release record.

If any step fails:

> **do not produce a failure handoff; create work and continue.**

---

# 70. FINAL HANDOFF DELIVERABLES — PRODUCED AFTER SHIPPED

Only after the controller has set `SHIPPED`, generate the final human-facing report.

Leave the project itself ready to run.

The report should contain:

- what was changed,
- major architecture decisions,
- exact run/build commands,
- what was tested,
- builder status,
- native AR status by platform,
- any non-P0 environmental limitations,
- provider strategy actually used,
- confirmation that no unauthorized metered inference was used,
- location of QA/release evidence,
- final release Git commit hash,
- controller/release record location.

Ensure these files are current:

- `README.md`
- `AGENTS.md`
- `.hermes/source/PRODUCT_CHARTER.md`
- `.hermes/REQUIREMENTS.md`
- `.hermes/REQUIREMENTS.json`
- `.hermes/CHECKPOINT.md`
- `.hermes/QA_MATRIX.md`
- `.hermes/KNOWN_ISSUES.md`
- `.hermes/ARCHITECTURE.md`
- `.hermes/DECISIONS.md`
- `.hermes/CHANGELOG.md`
- `.hermes/reports/FINAL_RELEASE.md`
- release evidence manifest tied to the final Git SHA.

A final report is a consequence of `SHIPPED`.

It is not what creates `SHIPPED`.

---

# 71. FIRST ACTIONS TO TAKE FROM THIS SINGLE PROMPT

Begin immediately.

The initiating Hermes session's job is to **bootstrap a project that no longer needs the initiating Hermes session**.

Perform these actions in order:

1. `cd ~/Desktop/nailfy`.
2. Locate the real Expo/React Native app root.
3. Inspect the actual installed Hermes version, CLI help, provider configuration, and available authenticated providers without destructively changing unrelated user configuration.
4. Verify the existing FreeLLMAPI route and the existing linked ChatGPT/Codex subscription route.
5. Record authorized provider tiers and prevent accidental metered-pay-per-token routing.
6. Inspect/initialize Git and create a clean baseline commit/backup.
7. Preserve this full prompt as `.hermes/source/PRODUCT_CHARTER.md` and record its SHA-256.
8. Bootstrap `.hermes/state/project.db` and the minimum durable Project/Requirement/WorkItem/Attempt/Lease/Evidence/Review/Event schema.
9. Implement the deterministic reconciliation controller and worker launcher.
10. Implement project-local provider routing, cooldown, escalation, and telemetry.
11. Implement isolated Git worktree lifecycle, leases, deterministic verifier, reviewer queue, merge queue, and release predicates.
12. Install the controller under the best non-LLM process manager available on this machine.
13. Start the real controller.
14. Commission the real execution path with destructive tests: worker death, controller restart, provider failure, test failure, review rejection, and no-runnable-work.
15. Repair the autonomy kernel until those tests pass.
16. Perform two independent product requirement extraction passes from the entire charter.
17. Reconcile them into stable requirement IDs and a dependency-aware work graph.
18. Audit the existing source and visual assets.
19. Seed product WorkItems according to the phased plan.
20. Hand execution authority to the persistent controller.
21. Verify via process/service state + heartbeat + database state that the controller is independently alive and owns the next transition.
22. The initiating Hermes session may then end; its ending must have no effect on project continuation.
23. The controller continues dispatching fresh Hermes workers, reviewers and diagnostics until the deterministic release gate sets `SHIPPED`.

Never require the user to type `continue`.

Never stop because a model/provider/session is temporarily unavailable.

Never interpret a failed acceptance gate as a final result.

Never substitute a progress report for implementation.

Never silently spend metered API money.

Use the free model pool aggressively for bounded work.

Use the linked ChatGPT/Codex subscription intelligently when stronger reasoning is needed or free capacity is temporarily exhausted.

The enduring product priority remains:

**Nail builder first. AR second. Premium app quality everywhere. Everything else is subordinate.**

The enduring autonomy priority is:

**The project survives the agents, the provider sessions, and the initiating chat. Only SHIPPED ends normal execution.**

```

===== 2026-09-22 00:40 | session 20260921_234936_670e4e | prep for nailify =====
give me the prompt i cna give another chat to do stage 0 now, full exhaustive

===== 2026-09-22 00:49 | session 20260921_234936_670e4e | prep for nailify =====
give me the prompt i can give another llm to do stage 1

===== 2026-09-22 00:59 | session 20260921_234936_670e4e | prep for nailify =====
give me the full exhustive list all of the info i need to provide for stage 2

===== 2026-09-22 01:01 | session 20260921_234936_670e4e | prep for nailify =====
give me the full exhustive list all of the info i need to provide for stage 3

===== 2026-09-22 01:05 | session 20260921_234803_2d9335 | @file:`.hermes/attachments/Pasted content (65.5… =====
what ar eyou actually doing

===== 2026-09-22 01:06 | session 20260921_234803_2d9335 | @file:`.hermes/attachments/Pasted content (65.5… =====
what are you doing in this chat?

===== 2026-09-22 01:06 | session 20260921_234803_2d9335 | @file:`.hermes/attachments/Pasted content (65.5… =====
what was the other llmdoing in this chat

===== 2026-09-22 01:07 | session 20260921_234803_2d9335 | @file:`.hermes/attachments/Pasted content (65.5… =====
can you take over please

===== 2026-09-22 01:07 | session 20260921_234803_2d9335 | @file:`.hermes/attachments/Pasted content (65.5… =====
first give me a copy of the audit in this chat then finish the task

===== 2026-09-22 01:09 | session 20260921_234936_670e4e | prep for nailify =====
THis is the data i have gathered, is it lacking in any way, is more needed if so be explicit and complete: 

## HUMAN ANSWERS — NAILED IT STAGE 0

**1. Which project folder is authoritative: `nailify` or `nailfy`?**

Use **`/home/ash/Desktop/nailify`** for this execution. Do not create a second copy called `nailfy`, and do not rename the existing project merely to reconcile old documentation. If the filesystem contradicts this, use the directory that actually contains the real project and report the discrepancy rather than duplicating the project.

The Stage 0 specification explicitly identifies `/home/ash/Desktop/nailify` as the current app root, while the older V3 charter still contains the earlier `~/Desktop/nailfy` spelling. Treat the Stage 0 filesystem instruction as the resolution for this run.

**2. How should the 10 supplied app mockups be treated?**

Treat the uploaded Nailed It mockups as **strong visual/product-direction references**, not rigid pixel-perfect specifications. The finished app should clearly belong to this same product: cream/off-white surfaces, deep wine typography, blush/rose accents, premium editorial beauty styling, restrained decoration, elegant serif display typography, clean modern controls, polished nail photography/rendering, and uncluttered mobile layouts.

They show the intended direction for:

- onboarding;
- Home;
- Explore;
- design-detail pages;
- Create;
- the main nail/set editor;
- detailed single-nail editing;
- AR Try On;
- My Nails;
- finished-design/share presentation.

Functionality and usability take precedence over copying a mockup literally. In particular, the nail editor must support the much deeper functionality specified in the charter even where a mockup only shows a subset of those controls. This agrees with the charter's instruction to use the inspiration as a mood board rather than a pixel-perfect specification.

**3. What is the native AR requirement?**

**Real native AR is a P0 feature.** It is not optional and must not remain a simulated camera or native stub. The production mobile version should use real camera input, real on-device hand landmarks, the actual per-finger design state, smoothing, fit adjustment and proper consumer-facing AR UI.

Lack of a physical device during development does **not** justify deleting or downgrading AR. Implement as much of the native pipeline as can legitimately be implemented and validate it through native builds, emulator/simulator support where available, placement/filtering unit tests and deterministic prerecorded hand-frame/video fixtures. The charter explicitly requires replacement of the native tracker stub.

**4. Is a physical iOS/Android device guaranteed to be available to Hermes right now?**

**No guaranteed physical device should be assumed.** Treat physical-device access as unavailable unless Hermes can actually discover and communicate with one from the machine.

This must **not block the rest of the build**. Use emulator/simulator, native compilation, prerecorded hand data and deterministic AR tests wherever legitimate. Only checks that inherently require real hardware should be classified `hardware-limited`.

Importantly, Hermes must **not claim that physical-device AR has passed unless it actually ran on a physical device**. The charter explicitly permits substitute evidence when hardware is unavailable but prohibits fabricating physical-device success.

**5. What should count as hardware-limited?**

Keep this category extremely narrow. Likely candidates are:

- final real-camera hand-tracking behaviour on an actual supported phone;
- real-world AR visual attachment/jitter under genuine movement and lighting;
- platform-specific camera-plus-overlay capture where emulator behaviour cannot establish actual device behaviour;
- device-specific performance/thermal behaviour where required.

AR maths, smoothing algorithms, design-to-finger mapping, handedness logic, persistence, fit calculations, lost-tracking logic and much of the native pipeline are **not automatically hardware-limited** merely because a phone is unavailable.

**6. Are real Firebase credentials/accounts required?**

**No. Firebase is not required for the MVP.**

The MVP should be **local-first and usable without an account**. If Hermes discovers genuine working Firebase configuration already present, it may preserve it provided it does not destabilize the product. Otherwise, remove fake/simulated login from the user path and keep backend integration isolated for future work.

Do not create Firebase purely to satisfy the charter and do not let absent credentials become a blocker. The product specification explicitly calls for local-first guest use, local saved projects and no fake login.

**7. Are real RevenueCat credentials/products required?**

**No. Subscriptions and the paywall are not part of this MVP.**

Unless Hermes discovers an already-real, fully configured and tested RevenueCat/store setup, remove the paywall from normal navigation, remove fake save limits, and remove simulated purchase success. The MVP can be fully unlocked.

Do **not** spend time creating products, entitlements or store infrastructure merely to make RevenueCat real.

**8. What should happen to AI Studio?**

AI generation is **not an MVP pillar**. If the current implementation is simulated, remove AI Studio from user-facing navigation. Do not build production cloud AI generation before the nail builder, AR and overall app quality are complete.

**9. Is account creation required?**

**No.** A fresh user must be able to install/open Nailed It, go through or skip onboarding, create designs, save them, reopen them and use the core app without registration.

Existing real authentication may remain if already functional and unobtrusive, but it must not become a prerequisite for P0. Onboarding specifically says not to force account creation.

**10. Should old internal `Nailify` identifiers be renamed?**

User-facing branding must become **Nailed It** everywhere. However, old technical identifiers such as AsyncStorage keys, bundle IDs or package IDs may remain when changing them would threaten migration, signing or existing user data.

Do not destroy compatibility simply to make every internal string say Nailed It. Use migrations where necessary.

**11. Is App Store / Play Store publication required before the MVP can be considered complete?**

**No.** A polished, validated release candidate is the objective. Do not make optional store publication, paid accounts, legal-owner actions, signing ownership or similar external actions blockers for completing the local-first product. Genuine external dependencies should be recorded truthfully rather than faked.

**12. What are the three overriding product priorities when resolving ambiguity?**

In order:

**1. Nail builder — excellent individual nail editing and full 10-nail set creation.**

**2. Real AR try-on.**

**3. Premium, coherent consumer-app quality everywhere around those features.**

Everything else is subordinate. The charter explicitly defines those as the core experiences and repeats at the end that the nail builder comes first, AR second, and premium app quality everywhere.

**13. When the mockups and existing code differ, which wins?**

Preserve good existing functionality and engineering foundations, but redesign the UX to achieve the supplied Nailed It direction. Do **not** throw away useful renderer, design-state, gesture, persistence or AR-placement work merely because rebuilding from scratch would be easier.

The app is an existing project to be evolved, not replaced.

**14. If anything else is ambiguous, should Hermes stop and ask me?**

Only for a genuinely irreversible or externally controlled issue that cannot safely be resolved from the charter, codebase or environment. Ordinary engineering choices should be resolved autonomously using the lowest-risk maintainable option and recorded as a decision.

Do not repeatedly return to me for routine implementation decisions.

Yes. Using the ZIP you just uploaded, here are the **full answers to the Stage 1 prompt**, rather than giving you another prompt.

## 1. Actual app root

Inside the supplied archive, the real Expo app is:

`nailify-main/app/`

That is the directory containing:

| Item | Path |
| --- | --- |
| Package manifest | `nailify-main/app/package.json` |
| Expo config | `nailify-main/app/app.json` |
| Source | `nailify-main/app/src/` |
| Entry point | `nailify-main/app/App.js` |

The archive itself does **not contain `.git` metadata**, so the original repository Git SHA cannot be recovered from this ZIP. That is important because Stage 1 says final evidence must be tied to a Git SHA. The ZIP can be treated as the exact baseline snapshot, but it cannot truthfully be assigned its original Git commit.

The newer Stage 0 instructions already anticipated the `nailfy`/`nailify` discrepancy and say to use the directory that actually exists.

---

# 2. Toolchain actually present

From `package.json` and `package-lock.json`:

| Tool/component | Version/status |
| --- | --- |
| Expo | `~51.0.28` |
| React Native | `0.74.5` |
| React | `18.2.0` |
| React Navigation | v6 |
| Zustand | `^4.5.2` |
| AsyncStorage | `1.23.1` |
| react-native-svg | `15.2.0` |
| gesture-handler | `~2.16.1` |
| expo-camera | `~15.0.16` |
| expo-haptics | `~13.0.1` |
| expo-media-library | `~16.0.5` |
| react-native-view-shot | `3.8.0` |
| MediaPipe Tasks Vision | `^0.10.18` |
| Package manager | npm; `package-lock.json` lockfile v3 |
| Node version required by repo | **Not pinned** |
| npm scripts | `start`, `android`, `ios`, `web` only |
| Lint script | **None** |
| Test script | **None** |
| Jest configuration | **None** |
| ESLint configuration | **None found** |

The environment I inspected happens to have Node `v22.16.0` and npm `10.9.2`, but those are **not project requirements**, because the repository does not pin Node.

I also ran a direct syntax pass over all source `.js` files and parsed `package.json`/`app.json`: **those checks passed**.

A full `npm ci` could not be completed reliably in this environment, so I would **not** claim Expo Doctor, a native build, or runtime launch passed.

---

# 3. What is actually in the app today

This is a genuine React Native prototype, not an empty project.

The navigation currently contains five tabs:

| Internal route | Visible current label | Intended V3 label |
| --- | --- | --- |
| `Home` | Home | Home |
| `Catalogue` | Explore | Explore |
| `Design` | Design | Create |
| `AR` | Try-On | Try On |
| `Profile` | My Looks | My Nails |

There are also stack routes for:

`Onboarding`, `DesignPreview`, `SendToSalon`, `Paywall`, and `AIStudio`.

The three major stores are:

| Store | Current function |
| --- | --- |
| `useDesignStore.js` | Current ten-nail design, focused finger, layers, undo/redo |
| `useAppStore.js` | Demo user, saved seed-design IDs, likes, onboarding |
| `useArStore.js` | AR fit offsets and smoothing |

The builder is considerably more functional than a simple mockup. It already has **10 independently stored nails**, 9 nail shapes, 3 length levels, solid/gradient bases, 47 coded art assets, drawing layers, layer transforms, recolouring, duplication, reordering, 50-step undo/redo, smart-set operations and AR placement mathematics.

However, several major systems the new charter requires simply do not exist yet.

---

# 4. Biggest baseline problems found

The most important finding is that the current app is **exactly the kind of prototype the V3 charter says must be transformed**, rather than something already close to release.

| Problem | Evidence |
| --- | --- |
| Native AR is a stub | `src/ar/HandTracker.js:1-14` |
| Web AR is real MediaPipe | `HandTracker.web.js` uses MediaPipe hand landmarks |
| Native AR falls back to fixed overlay | `ARTryOnScreen.js` |
| AR UI literally says simulated/preview | `ARTryOnScreen.js:233+` |
| Firebase is stubbed | `services/firebase.js:2`, credentials are `TODO` |
| RevenueCat is stubbed | `services/revenuecat.js:2` |
| Purchase flow is fake | `PaywallScreen.js:106` |
| AI generation is simulated locally | `services/ai.js:2`, `:45` |
| Explore search is fake | `CatalogueScreen.js:87-90` |
| Search component itself is a pressable placeholder | `components/ui/SearchBar.js:8-9` |
| Text editor doesn't exist | `DesignStudioScreen.js:483` says `"Text is coming soon"` |
| Fake account/sign-in messaging exists | `OnboardingScreen.js:99` |
| Fake user identity exists | `useAppStore.js` uses `Mia / mia@example.com` |
| Fake Pro state exists | `useAppStore.js` starts `isPro: true` |
| Fake QR exists | `SendToSalonScreen.js:14-15` |
| Profile still exposes fake subscription flow | `ProfileScreen.js:53-119` |
| Settings include toast-only placeholders | `ProfileScreen.js:155-159` |
| Current product branding is still Nailify | `app.json`, screens, exports etc. |
| Real My Nails project library does not exist | only seed IDs/current design state |
| Named project save doesn't exist | Studio "save" adds an ID such as `mine_<timestamp>` |
| Rename project doesn't exist | absent |
| Duplicate project doesn't exist | absent |
| Delete project doesn't exist | absent |
| Draft/finished project model doesn't exist | absent |
| `schemaVersion: 2` project model doesn't exist | absent |
| Real autosave/reopen project repository doesn't exist | absent |
| App icon package isn't configured | absent |
| Automated tests don't exist | absent |
| Acceptance checks don't exist | absent |

This agrees with the master charter's recorded starting state, which explicitly describes native AR, Firebase, RevenueCat, AI, sign-in and search as unfinished/simulated.

---

# 5. What already genuinely works

Some important pieces should **not** be thrown away.

The focused design state is real. `useDesignStore` contains separate arrays for:

`L[5]` and `R[5]`.

So ten different nails are genuinely supported.

Individual nail editing already supports solid colour, two-colour linear gradient and angle; shape and length; material/matte; adding art; adding drawing strokes; moving/scaling/rotating art; recolouring art slots; opacity; duplication; deletion; layer ordering; focused-finger selection; and undo/redo.

There are currently **47 coded/recolourable nail-art assets**, including florals, hearts, celestial art, geometric designs, leopard/zebra/cow, glitter, foil, marble, fruit, gems, pearls and French-tip-style art.

Whole-set operations also exist:

| Operation | Baseline |
| --- | --- |
| Different design per finger | Exists |
| Copy focused nail to current hand | Exists |
| Copy focused nail to all ten | Exists |
| Accent smart set | Exists |
| Alternating smart set | Exists |
| Ombré-across-hand smart set | Exists |
| French smart set | Exists |
| Undo/redo | Exists |
| Whole-set preview | Exists |
| Mirror | **Partial** — current code specifically copies left → right rather than providing both directions |

The charter specifically says these foundations should generally be retained and extended rather than discarded.

---

# 6. Requirement ledger I would use

I would keep Stage 1 at **36 requirements**, not hundreds.

| ID | Requirement | Source | Baseline |
| --- | --- | --- | --- |
| NAIL-P0-SHELL-001 | User-facing brand is Nailed It | §9, §68 | **FAIL** |
| NAIL-P0-SHELL-002 | Onboarding works without fake account requirement | §13, §45, §68 | **FAIL** |
| NAIL-P0-SHELL-003 | Home/Explore/Create/Try On/My Nails are functional | §12, §68 | **FAIL/PARTIAL** |
| NAIL-P0-SHELL-004 | Explore has real text search | §12.2, §68 | **FAIL** |
| NAIL-P0-SHELL-005 | No visible placeholder/simulated/fake flows | §45, §68 | **FAIL** |
| NAIL-P0-BUILDER-001 | Focused single-nail editing surface works | §14, §68 | **PRESENT** |
| NAIL-P0-BUILDER-002 | All ten nails maintain independent designs | §14.3, §30 | **PRESENT** |
| NAIL-P0-BUILDER-003 | Shape and length editing works | §16 | **PRESENT** |
| NAIL-P0-BUILDER-004 | Solid colour and two-colour gradient work | §17, §20 | **PRESENT** |
| NAIL-P0-BUILDER-005 | Required finishes are visibly distinct | §18 | **FAIL/PARTIAL** |
| NAIL-P0-BUILDER-006 | First-class editable French builder exists | §19 | **FAIL** |
| NAIL-P0-BUILDER-007 | High-quality substantial art library exists | §21 | **FAIL/PARTIAL** |
| NAIL-P0-BUILDER-008 | Art move/scale/rotate/recolour works | §22 | **PRESENT** |
| NAIL-P0-BUILDER-009 | Art duplicate/delete/reorder/opacity works | §22, §28 | **PRESENT** |
| NAIL-P0-BUILDER-010 | Drawing plus erasing works | §23 | **FAIL/PARTIAL** |
| NAIL-P0-BUILDER-011 | Text works or is absent | §24 | **FAIL** |
| NAIL-P0-BUILDER-012 | Functional layer management exists | §28 | **PRESENT/PARTIAL** |
| NAIL-P0-BUILDER-013 | 50 meaningful undo/redo edits work | §29 | **PRESENT structurally** |
| NAIL-P0-SET-001 | Copy-to-hand/all works | §30 | **PRESENT** |
| NAIL-P0-SET-002 | Bidirectional hand mirroring works | §30 | **FAIL/PARTIAL** |
| NAIL-P0-SET-003 | Smart set helpers remain editable | §30 | **PRESENT structurally** |
| NAIL-P0-DATA-001 | Versioned design-project schema exists | §15 | **FAIL** |
| NAIL-P0-DATA-002 | Legacy nail data migrates safely | §15, §53 | **PARTIAL** |
| NAIL-P0-DATA-003 | Local project create/autosave/reopen works | §33-34 | **FAIL** |
| NAIL-P0-DATA-004 | Rename/duplicate/delete project works | §33 | **FAIL** |
| NAIL-P0-DATA-005 | App restart preserves named projects | §33, §67 | **FAIL** |
| NAIL-P0-AR-001 | Production camera permission flow works | §36.12 | **PARTIAL/UNVERIFIED** |
| NAIL-P0-AR-002 | Native hand tracker is real, not stubbed | §36.1 | **FAIL** |
| NAIL-P0-AR-003 | AR uses canonical per-finger design state | §36.7 | **PRESENT on web path** |
| NAIL-P0-AR-004 | Landmark placement and smoothing are stable | §36.2-36.5 | **PARTIAL** |
| NAIL-P0-AR-005 | Lost tracking degrades gracefully | §36.5 | **FAIL/PARTIAL** |
| NAIL-P0-AR-006 | Fit controls exist and persist | §36.8 | **PRESENT** |
| NAIL-P0-AR-007 | Capture/share produces genuine media | §36.14 | **UNVERIFIED** |
| NAIL-P0-VIS-001 | Premium coherent visual system passes vision review | §10, §66, §68 | **UNVERIFIED** |
| NAIL-P0-QUAL-001 | Small-phone/accessibility/reduced-motion requirements pass | §42-43 | **FAIL/UNVERIFIED** |
| NAIL-P0-ENG-001 | Lint/tests/build/migration/AR tests and final evidence exist | §55-57, §68 | **FAIL** |

**Total: 36 P0 requirements.**

That is dramatically more useful than the previous 2,000+ line-derived requirement ledger because each of these corresponds to a meaningful release capability.

---

# 7. Baseline discrimination result

This is the crucial part.

A good acceptance suite should **not** turn the current prototype green.

Based on the actual source, the baseline should look approximately like this:

| Category | Current result |
| --- | --- |
| Clearly failing requirements | ~19 |
| Existing capability, suitable for deterministic proof | ~10 |
| Partial capability requiring stronger predicate | ~4 |
| Environment/runtime/vision dependent | ~3 |

Examples of very strong discriminating checks are:

| Requirement | Baseline result | Why |
| --- | --- | --- |
| Brand = Nailed It | FAIL | `app.json` explicitly says `Nailify` |
| Real Explore search | FAIL | Search invokes a toast saying it isn't available |
| No simulated UI | FAIL | multiple explicit `"Preview build"` / `"simulated"` strings |
| Native tracker | FAIL | `HandTracker.js` explicitly describes itself as a placeholder |
| Text editing | FAIL | literal `"Text is coming soon"` |
| Project library | FAIL | no project repository exists |
| Project rename | FAIL | no implementation |
| Project duplicate | FAIL | no implementation |
| Named project persistence | FAIL | only current design state is persisted |
| Schema v2 | FAIL | no project `schemaVersion` |
| Fake paywall absent | FAIL | Paywall route and fake purchase flow remain |
| Fake AI absent | FAIL | AI service explicitly simulates generation |
| Automated tests | FAIL | no test suite/config/script |
| AR unit coverage | FAIL | none |
| Final QA evidence | FAIL | none |

Those are exactly the kinds of checks Stage 1 wants because **they fail before the missing feature exists**.

---

# 8. Important baseline capabilities that should pass

Not every check should fail. A few checks should correctly prove that valuable existing functionality is already there.

| Capability | Static baseline evidence |
| --- | --- |
| Ten separate nails | `nails: { L:[5], R:[5] }` architecture |
| Finger selection | `Filmstrip` addresses all ten nails |
| Solid base colour | implemented |
| Two-colour gradient | implemented |
| Gradient angle | implemented |
| Nine nail shapes | implemented |
| Short/Medium/Long | implemented |
| Art layers | implemented |
| Move/scale/rotate | implemented |
| Recolour art | implemented |
| Duplicate/delete/reorder layers | implemented |
| Drawing strokes | implemented |
| 50-step undo/redo | `HISTORY_LIMIT = 50` |
| Copy focused nail to hand | implemented |
| Copy focused nail to all | implemented |
| Smart accent/alternating/ombré/French sets | implemented |
| Web MediaPipe tracking | genuine implementation |
| AR placement geometry | genuine pure function |
| Persistent AR fit calibration | implemented |

Those should not be deliberately made to fail merely because the overall product is unfinished.

---

# 9. Items that are genuinely UNVERIFIABLE from this ZIP alone

These should **not** be marked passed.

| Item | Exact reason |
| --- | --- |
| Current-release Git-SHA provenance | `.git` is absent from the ZIP |
| Native iOS/Android AR runtime | no physical/native runtime evidence supplied |
| Real native hand tracking | actually worse than unverifiable: source proves it is currently a stub |
| Camera tracking quality under real movement | requires runtime camera/device or legitimate prerecorded fixture pipeline |
| Low-light AR quality | device/runtime required |
| AR capture correctness | must prove real camera + overlay composition; source alone cannot |
| Native Android build | not run |
| Native iOS build | not run |
| 320px/430px screenshots | app was not successfully booted here |
| Premium visual-quality verdict | must come from current screenshots and independent vision review |
| Touch target behaviour in actual runtime | static styles provide clues but aren't sufficient proof |
| Performance/FPS | runtime profiling needed |
| Existing original Git commit | unavailable because archive strips `.git` |

That is exactly how the charter says hardware/runtime limitations should be handled: use the strongest legitimate substitute, but do not invent success.

---

# 10. What the source scan specifically caught

The source already contains several strings that a Stage 1 negative check should catch automatically:

```
src/services/revenuecat.js:2          STUBBED
src/services/firebase.js:2            STUBBED
src/services/firebase.js:19-24        TODO credentials
src/services/firebase.js:48           Auth stubs
src/services/ai.js:2                  STUBBED
src/services/ai.js:45                 Simulated network latency
src/screens/PaywallScreen.js:106      purchase is simulated
src/ar/HandTracker.js:1               placeholder
src/ar/HandTracker.js:5               stub
src/screens/ARTryOnScreen.js:233      Preview mode · simulated feed
src/screens/CatalogueScreen.js:89      Search isn’t available in this preview
src/components/ui/SearchBar.js:8      pressable placeholder
src/screens/DesignStudioScreen.js:483 Text is coming soon
src/screens/OnboardingScreen.js:99    sign-in is simulated
src/screens/SendToSalonScreen.js:14   QR placeholder
src/screens/ProfileScreen.js:151      previews are coming...
src/screens/ProfileScreen.js:158      not available in this preview
src/screens/ProfileScreen.js:161      preview build
```

That alone establishes that the current prototype fails the charter's explicit **zero visible fake flows** requirement. The charter specifically calls out simulated sign-in/purchases/AI, placeholder search, `"Text is coming soon"`, fake QR and simulated AR for removal.

---

# 11. Existing validation state

There is **currently no real validation infrastructure** in the project.

`package.json` exposes only:

```
npm start
npm run android
npm run ios
npm run web
```

There is no:

```
npm test
npm run lint
Jest config
ESLint config
QA_MATRIX.md
REQUIREMENTS.json
checks/
verify.sh
evidence/evidence.jsonl
```

So, as the ZIP stands today, the Stage 1 acceptance layer itself has **not been built**.

The charter requires eventual lint/build checking, migration tests, AR placement/filtering tests and basic store tests.

---

# 12. Exact reproduction commands

On the actual machine, a fresh Stage 1 agent should begin with:

```bash
cd ~/Desktop/nailfy

find . -name package.json -o -name app.json

# after identifying the real app directory:
cd <actual-app-root>

node --version
npm --version
cat package.json
cat app.json

npm ci
npx expo-doctor

# These currently will not exist unless Stage 1 creates them:
npm test
npm run lint

git rev-parse HEAD
git status --porcelain

grep -RniE \
'TODO|FIXME|stub|simulated|mock|coming soon|placeholder|preview build' \
src app.json

./verify.sh

git status --porcelain
```

For the ZIP supplied to me, `git rev-parse HEAD` cannot work because `.git` isn't included.

---

# 13. Bottom-line assessment

The current project is **not garbage and not empty**. There is a meaningful nail-editing engine under it. In particular, the ten-nail model, renderer, art-layer system, gesture concepts, undo/redo, smart sets, web hand tracking and AR placement mathematics are useful foundations.

But the **consumer product around them is still a prototype**. The biggest missing pieces are the real project/save library, new Nailed It app shell, real search, dedicated French/finish/text depth, elimination of fake flows, native AR, polished AR capture, automated tests and evidence-backed acceptance.

And most importantly for the prompt you gave me:

> **Fraction of P0 requirements that currently have a proper Stage-1 discriminating executable check in the ZIP: 0 / 36 = 0%.**
> 

That does **not** mean 0% of the product is built. It means the **acceptance layer itself does not yet exist**. Several product capabilities already exist and would legitimately pass once the checks are written.

So the correct Stage 1 starting point is exactly what your prompt says: **build the measuring system first, without touching the app.**

Yes. Below is the **complete answer set I would give the agent**. I’ve made the experimental choices now so it does not have to keep coming back to you. Where the supplied repo cannot establish a machine fact—such as the exact FreeLLMAPI model ID—I’ve authorized a deterministic discovery step rather than inventing one.

The important background is that the charter explicitly prioritizes bounded worker tasks, cheap/zero-cost inference, fresh workers, evidence rather than self-report, and French as a first-class editable builder feature.

1. **App root / workspace:** For this experiment, treat `~/Desktop/nailfy` as the canonical workspace and expect the Expo app root to be `~/Desktop/nailfy/app`. Before doing anything, verify that `app/package.json`, `app/app.json`, and `app/src/` exist. The uploaded snapshot has exactly that inner `app/` structure. Do **not** assume other top-level material is disposable: preserve the README, mockup/reference material, prompt files, `.claude`, assets, and anything else already there. Do not delete or reorganize them. If the actual machine has `~/Desktop/nailify` rather than `~/Desktop/nailfy`, use the existing real directory and record the naming discrepancy rather than creating a duplicate. The newer Stage 0 instructions explicitly say to use the directory that actually exists.
2. **Repo mode:** Use a **frozen baseline plus one independent scratch clone per attempt**. Do not let the 20 workers edit the authoritative working copy. Every attempt begins from exactly the same baseline commit, on its own branch/clone. Worktrees are acceptable technically, but scratch clones are preferred here because they minimize accidental cross-attempt contamination.
3. **Baseline Git:** The ZIP I supplied has **no `.git` history**. If the live copy also has no Git history, you are explicitly authorized to `git init` at the project/repository root and make an untouched import baseline commit first. Then make a second, separate pre-experiment tooling commit described in item 6. The **second commit becomes the frozen experiment baseline SHA**. If real Git history already exists on the VPS, preserve it and do not reinitialize or rewrite it.
4. **Install health:** The app uses npm and contains `package-lock.json` lockfile v3. The uploaded snapshot contains no `node_modules`, so assume a clean `npm ci` is required. Do not use `npm install` if `npm ci` works. Probe existing npm registry/proxy configuration before changing anything; do not overwrite global npm/Hermes configuration. Record any registry, DNS, proxy, or package-resolution issue as environment evidence.
5. **Known-broken baseline areas:** Workers must not wander into unrelated known prototype debt. Current known areas include: native AR tracker stub; simulated native AR fallback; fake/simulated RevenueCat purchase flow; stubbed Firebase; simulated AI generation; placeholder Explore search; `"Text is coming soon"`; simulated sign-in/account behaviour; fake QR; old Nailify branding; incomplete local project library; and no existing automated test/lint layer. These are known baseline defects, not reasons for a French-task attempt to fail unless the worker modifies or breaks them. The charter independently records the same broad starting-state problems.
6. **Baseline tooling changes:** **Approved.** Before run 1, add only the minimum version-compatible lint/test infrastructure required to judge the experiment, plus one trivial sanity test of an already-existing pure capability. Commit all of this as a single **pre-experiment tooling commit**. It must contain **zero product-behaviour changes**. The tooling baseline itself must be green before any worker run. If a strict whole-repo lint configuration reveals unrelated legacy failures, do not fix product code merely to satisfy it; configure the experiment lint gate so it reliably checks the files changed by an attempt. The fixed acceptance tests/checks must be protected by hash or otherwise verified unchanged before judging an attempt, so a worker cannot pass by weakening its own test.
7. **Execution environment:** Treat the experiment machine as a **16 GB, CPU-only, headless VPS with no iOS simulator, Android emulator, or attached physical phone**. Therefore native mobile AR is outside this experiment. Expo web is the relevant runtime target. Before run 1, probe whether a headless Chromium/Chrome/browser automation route is actually available. A graphical desktop is not required for headless screenshots. If **no legitimate automated browser/screenshot capability exists**, do not start 20 French-feature runs and then weaken the predicate afterward; stop setup and re-register a fully deterministic nonvisual benchmark instead. This decision happens before run 1.
8. **Node version:** The repository itself only says **Node 18+ recommended** and does not contain `.nvmrc` or `.node-version`. Freeze **Node 20 LTS** for this experiment if available through nvm. Record the exact `node -v` and `npm -v` before run 1 and use that exact runtime for all attempts. If the VPS already has a proven working Node 18 LTS environment for this project, keeping it is also acceptable; do not change Node mid-experiment.
9. **Runtime/process limits:** Do not disturb unrelated services/processes on the VPS. Before starting, record CPU count, available RAM, disk space and existing significant processes. Cap the experiment at **2 simultaneous Hermes implementation attempts** initially. One verifier/browser process may run alongside them. Do not increase concurrency during the 20-run measurement because changing resource contention would change the experiment.
10. **Time window:** The runs may proceed back-to-back in the same experiment window. They do not need to be spread across days. Two-way parallel execution is permitted, subject to the frozen concurrency cap and provider limits. Provider-aborted slots can be retried later.
11. **Model under test:** Use **one and only one exact provider/model pair for all 20 valid attempts**. I cannot truthfully name the current FreeLLMAPI model ID from the uploaded files, so you are authorized to perform **one pre-experiment three-model smoke comparison** using currently available zero-marginal-cost FreeLLMAPI models, select the strongest sensible **mid-tier coding/tool-use model**, record the exact provider and model ID, and freeze it. That selected model is pre-approved once chosen by this procedure; you do not need to return to me for another approval. No model switching after run 1.
12. **Endpoint/credentials:** Discover and use the existing authenticated FreeLLMAPI configuration already available to Hermes—Hermes config, environment variables, credential store, or equivalent. Never print or copy secrets into experiment logs, prompts, commits, or chat. Do not create a new paid provider account for this experiment.
13. **Provider-failure policy:** Approved as stated. A 429, provider timeout, transient auth failure, upstream 5xx, or comparable infrastructure failure becomes **`PROVIDER-ABORT`** and is excluded from engineering-success statistics. Retry that numbered slot later from a fresh clone/session. After **10 consecutive provider-aborted starts**, stop the experiment and report **MEASUREMENT INVALID — PROVIDER UNSTABLE** rather than drawing conclusions about worker quality.
14. **Cost policy:** **Zero new metered monetary spend.** FreeLLMAPI/other genuinely zero-marginal-cost routes only for this benchmark. Do not silently fall back to a metered API or a different subscription/model because one attempt is difficult. Each attempt receives one fresh worker session and the 60-minute wall-clock allowance; no automatic second worker, reviewer, or model escalation inside an attempt. The charter likewise separates zero-cost routes from unauthorized metered APIs.
15. **Hermes CLI invocation:** You are authorized to derive the exact supported syntax from the installed `hermes --help`, provider configuration and CLI version. Validate it using **one throwaway pre-experiment smoke invocation**. Freeze and record the resulting command template before run 1, including whatever options pin fresh-session/noninteractive mode, provider, model, working directory/task packet and permission/tool mode. Do not guess flags from an older Hermes version.
16. **Test task:** **Approved: French Nail Builder**, but do not artificially require a one-file implementation. In the present codebase French exists mainly as a static `frenchTip` art asset/smart-set shortcut, whereas the charter requires an editable first-class French feature. A correct solution may reasonably touch state/model, rendering and builder UI. The benchmark is the bounded **French feature slice**, not an arbitrary “one module only” constraint.
17. **Requirement mapping:** Primary authority is **charter §19 — French Nail Builder**. Supporting constraints come from §14 progressive builder UX, §15 versioned/editable data model, §29 undo/redo where applicable, §30 whole-set application, and §67 steps 12–13 in the mandatory user story. Section §19 specifically requires Classic, Micro, Deep, V and Diagonal/Side French; independent tip/base colours; depth/thickness; application scope; shape conformity; and continued editability.
18. **LOCKED ACCEPTANCE PREDICATE — freeze this before run 1:** An attempt is `ACCEPT` only if, at its own commit SHA: **(a)** from the normal builder a user can reach a dedicated French control without using the generic sticker/art library as the primary French mechanism; **(b)** the control exposes the five required variants—Classic, Micro, Deep, V, Diagonal/Side; **(c)** tip colour can be changed independently of the existing base colour; **(d)** tip depth/thickness is adjustable and visibly affects the rendered nail; **(e)** switching among the five styles visibly changes French geometry rather than merely renaming the same rendering; **(f)** the setting stays editable after application and after switching to another finger and back; **(g)** the user can apply the configured French treatment to the focused nail and has explicit apply-to-hand/apply-to-all behaviour matching the charter rather than silently modifying every nail; **(h)** French remains clipped/conformed to the selected nail shape in the normal renderer; **(i)** the fixed acceptance tests pass; **(j)** lint/static checks for the attempt's modified files pass; **(k)** Expo web builds/boots successfully; and **(l)** the automated runtime journey produces a current-SHA screenshot showing the French control and a rendered French nail. If screenshot/browser automation cannot be proven during pre-run setup, **do not change this predicate after seeing results**—French is then the wrong benchmark for this machine and the experiment must be re-registered before run 1.
19. **Evidence standard:** **Tests + successful web build/boot + automated runtime interaction evidence + current-SHA screenshot. No subjective code-inspection verdict determines pass/fail.** Static inspection may be collected diagnostically, but not used as the acceptance judgment. The evidence set should also include the fixed acceptance-harness hash so an attempt cannot pass by modifying the judge. Screenshots must include the attempt commit SHA in filename/metadata so stale visuals cannot prove a newer patch. This follows the charter's rule that screenshots and evidence must correspond to the current commit.
20. **N:** **20 valid engineering attempts.** Provider-aborted launches do not consume one of the 20.
21. **Per-attempt timeout:** **60 minutes wall clock**, hard cap. A worker still running at 60 minutes is terminated and recorded as `TIMEOUT`. Timeout counts against first-attempt accept rate; it is not retried as the same engineering attempt.
22. **First-attempt rule:** Approved exactly. Each attempt receives the same frozen task packet in a **fresh session**, sees no output from prior attempts, gets no reviewer coaching and receives no second implementation chance. Stage 2 measures first-attempt acceptance only.
23. **Human interaction budget:** **Zero after the experiment is commissioned.** No hints, corrections, “continue,” debugging assistance, acceptance interpretation changes, or manual rescue during the 20 runs. Setup work before run 1—provider discovery, predicate freezing, baseline tooling and environment validation—is not counted as intervention.
24. **Commit preservation:** Approved with one addition: every attempt gets its own branch/clone and must produce a commit if it made code changes. Preserve the commit SHA, patch/diff, logs and evidence permanently in the experiment archive. After those artifacts are captured and verified, the physical scratch working directory may be deleted. Nothing is merged into the authoritative app during Stage 2.
25. **Output location:** Use **`~/Desktop/nai
...[TRUNCATED 3874 chars]...
s:** **Not available yet. Stage 2 must run first.** Stage 3 must not be commissioned until there are 20 valid engineering attempts under the frozen Stage 2 protocol. Capture accept rate, timeout rate, no-change rate, rework/failure rate, malformed rate, provider-abort rate and mean/median duration.
3. **Stage 3 accept-rate threshold:** **≥60% first-attempt ACCEPT.** This was already locked in Stage 2 and must not now be weakened to 40–50%.
    - 12–20 ACCEPT out of 20 → Stage 3 may proceed.
    - 6–11 → improve packet/decomposition and rerun Stage 2.
    - 0–5 → re-pick/re-shape the benchmark before drawing conclusions.
    - Provider aborts are replaced and do not enter the 20 denominator.
4. **Worker packet template:** Freeze the exact Stage 2 packet shape that produced the qualifying benchmark result. Stage 3 workers can receive different **task content**, but not a completely new packet methodology without recording that as an experiment/change.

## B. Project & environment facts

1. **Project root:** Treat `~/Desktop/nailfy` as the intended canonical project workspace **if that directory actually exists on the host**. Locate the real app underneath it by finding `package.json`, `app.json` and `src/`. Based on the ZIP supplied here, the Expo application sits under an `app/` subdirectory. Do not create a duplicate `nailfy`/`nailify` tree just to make documentation match.
2. **Repo state / remote:** Inspect rather than assume. Preserve any existing Git history, branch and remote. If the deployed copy has no Git history, initialize it and establish the frozen baseline as already authorized. Keep engineering work local unless an authenticated private remote is already available or can be created safely under item 7.
3. **Private GitHub backup:** **Yes, preferred.** If working GitHub credentials are already present and a private repo can be created without exposing the project or asking for secrets, create/use one and push the protected baseline. If no authenticated route exists, do **not** block Stage 3 waiting for it; keep local backups and record `NO_REMOTE_BACKUP` as an operational risk.
4. **Host:** Treat the intended unattended host as the **CPU-only ~16 GB VPS**, subject to actual verification before commissioning. Do not assume GPU/display/mobile-emulator capability.
5. **OS/init:** Detect it. If Linux + user systemd is available, use a **user-level systemd service**. Do not require root merely to supervise the controller.
6. **Node/Expo:** Freeze the exact Node/npm versions established during Stage 2. The repo does not itself strongly pin Node, so do not switch runtime casually after the benchmark. Run the repo's actual `expo-doctor`/equivalent and record its output before Stage 3.
7. **Runtime targets:** Assume:
- web/headless browser: available **only after verified**;
- Android emulator: not assumed;
- iOS/Xcode: unavailable on the VPS;
- physical phone: not assumed.

Detect anything better that actually exists.

1. **Existing `.hermes/`:** Inspect all existing `.hermes/` state before reuse. **Do not trust prior controller state.** Preserve historical files where useful, but stale database rows, leases, processes or old orchestrator assumptions must not silently become authoritative.

These are exactly the environmental/project facts the questionnaire says must be verified before kernel configuration.

## C. Provider & cost policy

1. **FreeLLMAPI:** Inspect current Hermes/provider configuration and establish current endpoint, connectivity and model list without exposing credentials. Use it as **Tier A**.
2. **OpenRouter:** **Do not use it for Nailed It Stage 3.** No OpenRouter credits should be consumed by this autonomous build.
3. **Luna:** **Do not include Luna in the project routing table.** Search the project-local router/config and ensure it is absent.
4. **Claude subscription:** Use an **already-authorized Claude subscription route as Tier B if it genuinely exists in this Hermes installation and can be invoked without metered API billing**. Suggested roles:
- Sonnet-class route: stronger planning/debug/implementation escalation.
- Opus-class route: high-risk/final review where available.

If the actual installation instead exposes a different already-authorized zero-additional-cost strong subscription route, record the discrepancy rather than fabricating Claude capability. Do not silently substitute a paid Anthropic API.

1. **Metered spend ceiling:** **£0 / $0 / ¥0 new metered API spend.**
2. **Escalation order:** Encode:

`selected FreeLLMAPI model → fresh FreeLLMAPI retry after engineering rejection → stronger validated FreeLLMAPI model if available → authorized Claude subscription → WAITING_PROVIDER`

Provider failures such as 429 do not count as engineering failures.

1. **Cooldown defaults:** Approve:
- 429/rate limit: **10 min**
- provider 5xx: **5 min**
- timeout: **10 min**

Add jitter/backoff if useful, but do not turn them into uncontrolled hours-long sleeps.

1. **FreeLLMAPI concurrency:** Start at **1 implementation worker**. Stage 3 may increase to **2** only after the Stage 2 ≥60% gate and only if observed accepted throughput improves. Do not swarm.
2. **Usage tracking:** Record provider, model, attempt, start/end, provider failure class, and whatever token/request counters the provider actually exposes. If FreeLLMAPI does not expose reliable token accounting, record that explicitly; never invent cost/token numbers.

The provider section of your supplied questionnaire specifically asks that model routing and metered-spend rules be fixed before kernel operation.

## D. Orchestration kernel config

1. **SQLite:** Use `.hermes/state/project.db`, SQLite in WAL mode.
2. **State model:** Approved:
- WorkItem = durable work
- Attempt = disposable execution
- Evidence = independently observed proof
- Reviews and requirement mappings are durable records.
1. **Lease duration:** Use **25 minutes** for normal implementation attempts, with heartbeat renewal while the worker is demonstrably alive. Long native/build tasks may explicitly receive **45 minutes**. Lease expiry is not failure of the WorkItem.
2. **Controller supervision:**
- systemd user service where available
- suggested unit: `nailed-it-controller.service`
- `Restart=on-failure` or equivalent sensible restart policy
- heartbeat every **30 seconds**
- logs under `.hermes/logs/`
- rotate rather than grow indefinitely
- start on user boot/login where the environment supports lingering/user-service persistence.
1. **Watchdog:** **Confirmed and important:** the watchdog has exactly one job—detect that the controller is dead/unhealthy and restart/alert/log it. It must **never** create workers, invent work, start directors, rewrite queues, perform planning or become a second supervisor.
2. **Worktrees:** Use `.hermes/worktrees/`; start with maximum **1 active implementation worktree**, later at most **2** after successful scaling evidence. Preserve interrupted work until commits/diffs have been inspected. Clean merged/rejected/expired worktrees only after evidence and useful changes are safely captured.
3. **Merge queue:** Prefer **rebase onto current canonical branch, then controlled merge/fast-forward where safe**. Deterministically trivial conflicts can be resolved by integration logic; semantic/nontrivial conflicts create an integration/rework WorkItem. Workers never merge themselves into canonical.
4. **Planner wake events:** Planner is **event-driven only**. Wake it for:
- **2 engineering rejections** of the same bounded WorkItem;
- incomplete project with no eligible/runnable WorkItem and no legitimate wait state;
- requirement ambiguity that cannot safely be resolved from the charter/code;
- requirement contradiction;
- nontrivial integration conflict;
- repeated acceptance failure that does not map cleanly to existing work;
- decomposition proven too broad by repeated failure.

Do not keep a permanent planner/director session alive.

1. **Controller self-protection:** Confirmed. Product WorkItems may not modify `.hermes/autonomy/`, release predicates, provider policy or control schemas. Such work requires a dedicated controller-maintenance WorkItem and independent review.
2. **Checkpoint:** Update `.hermes/CHECKPOINT.md` **on meaningful durable state transitions**, not every heartbeat. Include current SHA, project state, active attempts, failing gates, provider waits and next deterministic controller action.

Those decisions directly answer the controller configuration questions in the supplied Stage 3 sheet.

## E. Acceptance & verification

1. **Authoritative command:** Once Stage 1 has produced the acceptance layer, **`./verify.sh` is the authority**. Do not let Stage 3 invent a second competing verification system.

`verify.sh` should internally run the applicable fixed checks, including:

- dependency/config/Expo health check;
- lint/static validation;
- unit tests;
- migration/data tests;
- AR placement/filtering tests;
- relevant store/model tests;
- web build/boot check where supported;
- runtime/screenshot checks where supported.

A controller should call the acceptance entry point rather than recreate these decisions conversationally.

1. **Screenshot widths:** Use **320 px and 430 px** as the fixed phone-width visual evidence pair. Add a tablet width later if useful, but 320/430 remain release reference sizes.
2. **Visual QA provider:** First try a **validated free vision-capable model** if the FreeLLMAPI pool contains one whose output is reliable enough. If not, use the **already-authorized Claude subscription vision capability**. Do not use metered API spend. Visual reviewer must be fresh and independent from the implementer.
3. **Independent review required for:** at minimum:
- schema/data migration
- persistence/data deletion
- state/undo architecture
- AR/native camera/tracker work
- security/privacy
- navigation/state architecture
- controller/control-plane changes
- release candidate
- large builder architecture changes.

Reviewer gets requirements + diff + evidence, not the implementer's entire conversation.

1. **Evidence standard:** Confirmed. Every accepted WorkItem must reference current-SHA evidence: commands/results, artifact hashes, screenshots, build outputs and independent review where required. Worker prose alone is never evidence.
2. **Blocking:**
- Any failed **mandatory P0 acceptance predicate** blocks release.
- A failed WorkItem check blocks that WorkItem's acceptance/integration as appropriate, not unrelated work.
- P1 work may remain incomplete unless promoted to mandatory.
- `WAITING_PROVIDER`, `WAITING_REVIEW`, `WAITING_EXTERNAL`, etc. do not mean project failure.
- A genuine unverified P0 condition may remain `WAITING_EXTERNAL`; it cannot be falsely marked passed.
1. **AR evidence threshold:** During development, **deterministic prerecorded hand-frame/landmark fixtures are acceptable substitute evidence** when they exercise the same real placement/filtering path. Native compilation/emulator evidence should be used where available.

**A physical device is not an absolute prerequisite to setting SHIPPED if the environment genuinely cannot provide one**, because the charter permits the strongest legitimate substitute evidence. However:

- do not claim physical-device testing occurred when it did not;
- explicitly retain a hardware-limited release note;
- real native tracker implementation and native compilation remain required where supported;
- physical-device validation should be performed before public/store release as soon as hardware is actually available.

The questionnaire identifies visual review, blocking behaviour and AR substitute evidence as explicit Stage 3 decisions.

## F. Requirement ledger

1. **Ledger approval:** Use the Stage 1 compiled ledger as the machine authority. The **36-P0 capability shape** we already identified is acceptable, provided it passes the hard traceability conditions:
- every one of §67's 27 story steps maps to at least one requirement;
- every applicable §68 P0 Definition-of-Done item maps to at least one requirement/check;
- every requirement has real evidence or an explicit limitation;
- no giant line-by-line ledger returns.

A final count anywhere around **30–40** is acceptable; correctness beats hitting exactly 36.

1. **P2 exclusions:** Confirmed. Keep outside normal MVP scope:
    
    social/community, creator monetization, marketplace, booking, commerce, subscriptions/paywall, unnecessary cloud accounts, production AI Studio, messaging, server notifications, complex 3D sculpting and salon CRM. Do not let planners quietly reintroduce them.
    
2. **P0 ordering:** Confirm:
    
    **Builder → AR → premium shell/UX → supporting assets/polish**.
    
    Persistence/data work may precede visible builder work where it is a dependency, but it does not replace the product priority.
    

The supplied questionnaire itself identifies the 30–40-item P0 ledger and P2 exclusions as the requirement basis for Stage 3.

## G. Reporting & observability

1. **Notification policy:** **Genuine blockers only, plus SHIPPED.** Do not interrupt me for ordinary retries, reviews, rework, provider cooldowns or engineering decisions.

Separately, write a **daily durable status digest to disk** so silence never hides a stall, but do not send it to me unless there is a blocker or I ask.

1. **Legitimate human interruption:** Ask only for things the system genuinely cannot safely provide itself, including:
- missing signing/store/legal identity action;
- credentials that do not already exist and cannot be created autonomously;
- metered monetary spend authorization;
- irreversible production/external action;
- hardware I personally need to supply when no legitimate substitute exists;
- deletion of irreplaceable historical/user data;
- contradictory owner-level product requirements requiring a product decision.

Ordinary code/library/UI decisions do not qualify.

1. **Metrics report:** Yes. Project `.hermes/reports/metrics.json` / readable Markdown projection with:
- accepted WorkItems/day
- first-attempt acceptance rate
- rework rate
- regression count
- mandatory requirements remaining
- provider wait time
- worker execution time
- review wait time
- Tier A/Tier B usage
- human interventions.

Do not optimize for session counts/messages/commits.

1. **Logs:** `.hermes/logs/`. Keep structured logs and rotate. Sensible starting cap: **100 MB total**, e.g. 10 × 10 MB segments per major service, unless actual log volume shows that is inappropriate. Never log secrets or camera frames.

These choices answer the notification/observability section of the questionnaire.

## H. Authority boundaries

1. **May act without asking:** Yes, for routine local engineering the controller/workers may:
- inspect/read files;
- modify app source;
- install/change npm dependencies when technically justified;
- run builds/tests;
- create commits/branches/worktrees;
- restart project-local controller services;
- invoke authorized zero-marginal-cost providers;
- perform automated QA;
- refactor within requirement boundaries;
- create/delete temporary worktrees after preservation.

This authority does not override protected product/acceptance/control-plane boundaries.

1. **Must ask first:** Yes:
- any metered spend;
- publication/deployment to an external production audience;
- App Store/Play Store submission;
- irreversible account/legal action;
- deleting historical/irreplaceable data;
- changing unrelated Hermes profiles or external configuration;
- exposing/private-repo visibility changes;
- secret rotation where existing credentials belong to other systems.
1. **Hermes global config:** **Project-local routing/config only wherever technically possible.** The project may **read** `~/.hermes` to discover existing credentials/providers but should not rewrite unrelated global configuration. If Hermes absolutely requires a global change for the authorized provider, make the smallest isolated change and document it; otherwise do not.
2. **Credentials:** Confirmed. Existing keys stay in Hermes config/vault/environment. New secrets are never committed, written into task packets, printed into logs or pasted into chat.

The questionnaire distinguishes routine autonomous authority from external/irreversible actions precisely this way.

## I. Stopping & escalation

1. **Rework escalation:** Use:
- Attempt 1: cheapest adequate FreeLLMAPI worker.
- First engineering rejection: fresh worker, same tier, with bounded evidence/reviewer feedback.
- Second engineering rejection: stronger validated FreeLLMAPI model if available.
- Third unresolved engineering attempt / genuinely high-risk work: authorized Claude subscription.
- Continued failure after strong-tier attempt: create a diagnostic/decomposition WorkItem rather than blindly cycling more sessions.

Provider errors do not increment engineering-rejection count.

1. **Zero accepted progress tripwire:** **2 consecutive calendar days with zero accepted WorkItems**, while mandatory runnable work exists, triggers an owner notification and a diagnostic freeze on scaling. The controller may keep preserving state but must not hide two days of non-convergence behind session activity.
2. **Regression tripwire:** Confirmed. If newly integrated work breaks any previously accepted mandatory requirement:
- quarantine/revert the offending integration if deterministic and safe;
- reopen/create the bounded WorkItem;
- attach failed evidence;
- do not spawn layers of rescue agents;
- rerun affected acceptance after remediation.
1. **Global kill switch:** Implement two explicit mechanisms:
- project-level file: **`.hermes/STOP`**
- emergency service action: `systemctl --user stop nailed-it-controller.service` where systemd is used.

When `.hermes/STOP` is detected, the controller should stop dispatching, persist state, terminate/settle active work safely and transition to explicit user cancellation/suspension according to the implemented schema. It must never treat a missing worker/provider as equivalent to this user kill switch.

1. **Remote backup requirement:** Stage 3 **may begin without a private remote** if the local repository has a verified Git baseline plus a separate local backup, but the controller should create/use a private remote automatically if already-authorized GitHub access makes that possible. Lack of GitHub credentials is not a reason to prevent the entire project from running.

These are the escalation/stopping decisions requested in the final section of the questionnaire.

### The seven decisions Hermes actually needed from you

To make it completely unambiguous:

| Decision | Answer |
| --- | --- |
| Stage 2 gate | **Run Stage 2 first; ≥60% ACCEPT required** |
| Visual QA | **Validated free vision first; Claude subscription fallback; no metered API** |
| Notifications | **Genuine blockers only + SHIPPED; daily status written to disk silently** |
| AR physical-device threshold | **Not an absolute SHIPPED blocker if unavailable; strongest substitute evidence allowed and limitation must be explicit** |
| Private remote | **Create/use one if authenticated access exists; otherwise local execution may proceed** |
| Metered spend | **£0 / $0** |
| Zero-progress escalation | **2 consecutive days** |

Those seven are exactly the subset the supplied document says requires genuine owner decisions.

The key correction I would make to the Stage 3 questionnaire itself is **do not lower the benchmark gate from the already-registered 60% to 40–50% just because Stage 3 proposes a new suggested threshold**. Changing that after designing Stage 2 would defeat the point of pre-registering the experiment.

===== 2026-09-22 01:13 | session 20260921_234803_2d9335 | @file:`.hermes/attachments/Pasted content (65.5… =====
add this knoledeg to the obsidian vault

===== 2026-09-22 01:15 | session 20260921_234936_670e4e | prep for nailify =====
@file:`.hermes/attachments/Pasted content (69.6 KB)`
@file:`.hermes/attachments/Pasted content (22.5 KB)`

attached is a detailed audit of the lessons i have learnt, and attached is also the answers to all the questions, i ant to do this right moving forard

--- Attached Context ---

📄 @file:`.hermes/attachments/Pasted content (69.6 KB)` (17813 tokens)
```
Here's the full current report.

The full report is 429 lines. Let me read it complete and present it.Let me fix the remaining verified inconsistencies, add the new reconciler finding, then present the full report.One remaining occurrence. Let me find and fix it.Now adding the new reconciler finding (the strongest insight not in the original report).All edits applied. Committing, then presenting the report.Here's the full report, verbatim from disk (post-corrections, committed as `71bd829`).

---

# FORENSIC RETROSPECTIVE — AMIS / HERMES AUTONOMOUS SOFTWARE-DEVELOPMENT ORCHESTRATION

**Date:** 2026-09-22 (Europe/London)
**Mode:** Read-only investigation. No code, config, database, git history, or running service was modified.
**Subject:** The operator's methodology for building an autonomous software-development system on Amis/Hermes, with Star Force X / "Nailed It" (Nailify) and Empirium Studio (AI Staff Force / AI Workforce) as experimental workloads.
**Method:** Primary sources only — filesystem, SQLite databases, JSONL control-plane logs, git history, Hermes session store, and pre-existing audit documents (the latter treated as claims to verify, not ground truth). Evidence-classification per the mandate: PROVEN / STRONGLY SUPPORTED / PROBABLE / SPECULATIVE. Confidence labels are attached to major findings inline; sections use them as abbreviations.

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
| "Complete/RELEASE_VALIDATED" (BUILD_STATE previous status) | later "Invalidated on resumed execution b
...[TRUNCATED 33351 chars]...
owser capability:

> If a repeatable headless browser journey can boot the frozen baseline and produce a SHA-named screenshot successfully **3 consecutive times before run 1**, use the original visual French benchmark. Otherwise use `FRENCH-DETERMINISTIC-NONVISUAL-V1`.

Once run 1 begins, that choice cannot change.

---

**2. AR feasibility spike**

Run the AR feasibility spike **in parallel with Stage 2**, after the Stage 2 baseline SHA has been frozen.

It must run in a separate scratch clone/branch and must **never modify the Stage 2 benchmark baseline**. Stage 2 does not wait for the spike because French is independent of AR.

Pre-register the architecture decision tree:

**Path A — preferred:** prove a maintained, on-device hand-landmark pipeline can operate with the existing Expo SDK 51 / React Native 0.74.5 stack. A valid proof requires a minimal native/dev project path that:

* installs using maintained dependencies;
* completes native configuration/prebuild without unresolved dependency incompatibility;
* compiles on an available supported native build environment, if one exists;
* exposes the required 21-landmark structure, handedness/confidence/timestamp interface;
* can feed deterministic prerecorded landmark/frame input into the same tracking adapter/placement pipeline.

If that passes, **stay on the existing Expo/RN generation** for the AR implementation.

**Path B — controlled SDK upgrade:** if the maintained tracker/camera stack cannot support Expo 51/RN 0.74.5 for a documented compatibility reason, test the smallest sensible Expo/RN upgrade in an isolated branch.

The upgrade is accepted only if:

* `expo-doctor`/dependency validation is clean enough to show no genuine compatibility break;
* all existing deterministic acceptance tests still pass;
* web build still passes;
* migration/storage fixtures still pass;
* existing builder/state behaviour does not regress;
* native AR dependencies can then be configured/compiled to the strongest extent the environment supports.

If those conditions pass, **the architecture decision is to upgrade deliberately**.

**Path C — minimal custom native module:** use this only if:

1. the maintained pipeline cannot support the current stack, **and**
2. the controlled SDK upgrade fails the acceptance gate or would cause disproportionate product regression.

Then implement the smallest maintainable native bridge around a current on-device landmark implementation rather than adopting an abandoned wrapper.

This decision order is now owner-approved:

> **current maintained stack → controlled Expo upgrade → minimal custom native module**

The agent does not return to the owner to choose among those three. Evidence chooses.

Only if **all three approaches are demonstrably infeasible** does AR become an owner-level architecture blocker.

The spike must finish **before Stage 3 dispatches the real native-AR WorkItem**, even if Stage 2 itself finishes earlier.

---

**3. French Stage 2 work is intentionally throwaway**

Confirmed explicitly:

> **Stage 2 French implementations are experimental specimens, not product work.**

None of the 20 French branches is merged into the production/canonical application, even if one is excellent.

Their purpose is solely to measure:

* first-attempt acceptance;
* task-packet quality;
* model reliability;
* time-to-result;
* common failure modes.

Preserve their commits/diffs as evidence, then discard their scratch workspaces.

The real production French feature is implemented later, **after the builder redesign**, against the then-current UI architecture and the same charter requirements.

Do not cherry-pick a Stage 2 implementation merely because it passed. An engineer may later study the experiment artifacts diagnostically, but the production WorkItem begins from the canonical redesigned builder.

This removes the sequencing contradiction.

---

**4. Re-run budget**

The budget is now **per registered benchmark round**, not a lifetime 20-attempt maximum.

Round 1:

* 20 valid attempts;
* maximum 60 minutes implementation per attempt;
* verification allowance defined in item 10 below;
* maximum **24 hours wall clock** for that benchmark;
* £0 new metered API spend.

One and only one additional benchmark round is pre-authorized.

Therefore the full measurement campaign hard ceiling is:

* **maximum 2 × 20 valid attempts = 40 valid attempts;**
* **maximum 48 hours wall clock;**
* £0 new metered inference spend.

The second round is used as follows:

* **12–20 ACCEPT in Round 1:** no second Stage 2 round; Stage 3 gate passes.
* **6–11 ACCEPT:** revise packet/decomposition while preserving model and acceptance discipline, then run Round 2.
* **0–5 ACCEPT:** register a different bounded representative task **before inspecting any implementation from that new benchmark**, freeze its predicate/harness, then run Round 2.

If Round 2 still fails the ≥60% Stage 3 threshold, the measurement campaign ends. **Do not authorize a third 20-run experiment automatically and do not compensate by adding orchestration.**

Stage 3 remains gated.

---

**5. Requirement dependency edges**

Yes. The ledger must have an explicit `depends_on` field before Stage 3 dispatch.

Use this dependency graph as the initial owner-approved graph:

```text
NAIL-P0-SHELL-001  <- []
NAIL-P0-SHELL-002  <- []
NAIL-P0-SHELL-004  <- []
NAIL-P0-SHELL-003  <- [DATA-003, BUILDER-001, SHELL-004, AR-001, AR-003]
NAIL-P0-SHELL-005  <- [SHELL-002, SHELL-003, SHELL-004, AR-007]

NAIL-P0-DATA-001   <- []
NAIL-P0-DATA-002   <- [DATA-001]
NAIL-P0-DATA-003   <- [DATA-001, DATA-002]
NAIL-P0-DATA-004   <- [DATA-003]
NAIL-P0-DATA-005   <- [DATA-003]

NAIL-P0-BUILDER-001 <- [DATA-001]
NAIL-P0-BUILDER-002 <- [DATA-001, BUILDER-001]
NAIL-P0-BUILDER-003 <- [BUILDER-001]
NAIL-P0-BUILDER-004 <- [BUILDER-001]
NAIL-P0-BUILDER-005 <- [BUILDER-004]
NAIL-P0-BUILDER-007 <- [BUILDER-001]
NAIL-P0-BUILDER-008 <- [BUILDER-007]
NAIL-P0-BUILDER-012 <- [BUILDER-001, DATA-001]
NAIL-P0-BUILDER-009 <- [BUILDER-007, BUILDER-012]
NAIL-P0-BUILDER-010 <- [BUILDER-001, DATA-001]
NAIL-P0-BUILDER-011 <- [BUILDER-001, DATA-001]
NAIL-P0-SET-001     <- [BUILDER-002]
NAIL-P0-SET-002     <- [BUILDER-002]
NAIL-P0-BUILDER-006 <- [BUILDER-003, BUILDER-004, SET-001]
NAIL-P0-SET-003     <- [BUILDER-002, SET-001]
NAIL-P0-BUILDER-013 <- [
  BUILDER-003,
  BUILDER-004,
  BUILDER-005,
  BUILDER-006,
  BUILDER-008,
  BUILDER-009,
  BUILDER-010,
  BUILDER-011,
  BUILDER-012,
  SET-001,
  SET-002,
  SET-003
]

NAIL-P0-AR-001 <- []
NAIL-P0-AR-002 <- [WI-AR-SPIKE-001]
NAIL-P0-AR-003 <- [AR-002, BUILDER-002, DATA-001]
NAIL-P0-AR-004 <- [AR-002]
NAIL-P0-AR-005 <- [AR-004]
NAIL-P0-AR-006 <- [AR-004]
NAIL-P0-AR-007 <- [AR-001, AR-003, AR-004, AR-005, AR-006]

NAIL-P0-QUAL-001 <- [BUILDER-001, SHELL-003]
NAIL-P0-VIS-001  <- [
  SHELL-001,
  SHELL-002,
  SHELL-003,
  SHELL-004,
  SHELL-005,
  BUILDER-001,
  AR-007,
  QUAL-001
]

NAIL-P0-ENG-001 <- []
```

`WI-AR-SPIKE-001` is a **WorkItem precondition**, not an extra product requirement.

Also add:

```json
"verification": {
  "predicate_id": "...",
  "verification_kind": "...",
  "command": "...",
  "evidence_expected": "...",
  "contract_hash": "..."
}
```

to every requirement before it becomes runnable.

The planner may refine **WorkItem** dependencies where implementation reveals genuine technical prerequisites, but it may not silently delete requirement dependencies or derive the entire graph conversationally from scratch.

---

# B. Artifacts required before run 1

**6. Frozen worker packet template**

Create:

`/.hermes/experiments/worker-baseline/WORKER_PACKET_TEMPLATE.md`

with exactly this shape:

```markdown
# WORKER TASK PACKET

PACKET_VERSION: 1
PROJECT: Nailed It
BASELINE_SHA: {{BASELINE_SHA}}
WORKITEM_ID: {{WORKITEM_ID}}
ATTEMPT_ID: {{ATTEMPT_ID}}
PROVIDER: {{PROVIDER}}
MODEL: {{MODEL}}

## MISSION

{{MISSION}}

## WHY THIS EXISTS

{{WHY_THIS_EXISTS}}

## REQUIREMENT IDS

{{REQUIREMENT_IDS}}

## ACCEPTANCE CONTRACT

You do not decide whether your work passes.
Acceptance is determined after your session by the protected independent harness.

{{ACCEPTANCE_CRITERIA}}

## RELEVANT ARCHITECTURE DECISIONS

{{ARCHITECTURE_DECISIONS}}

## STARTING STATE

You are working from exactly:

{{BASELINE_SHA}}

Do not assume work from any other attempt exists.

## RELEVANT FILES

{{RELEVANT_FILES}}

## ALLOWED / EXPECTED FILES

You may edit only files reasonably necessary for this WorkItem.

Expected areas:

{{ALLOWED_FILES}}

If another file must be changed, do so only when required for the mission and explain it
in the result record.

## PROHIBITED CHANGES

You must not:

- modify the protected acceptance harness;
- modify verify.sh or frozen acceptance predicates;
- weaken, delete, skip, rename, or bypass tests;
- change provider/model configuration;
- modify .hermes/autonomy/;
- modify experiment records;
- change unrelated product functionality;
- add fake/simulated success paths;
- replace required behaviour with a placeholder;
- claim acceptance yourself.

Additional task-specific prohibitions:

{{PROHIBITED_CHANGES}}

## REQUIRED TEST / VALIDATION COMMANDS

During implementation you may run:

{{WORKER_TEST_COMMANDS}}

These are developer feedback only.
Your own test result does not constitute acceptance.

## EXPECTED ARTIFACTS

Produce:

1. coherent implementation;
2. any task-local tests allowed by the packet;
3. one coherent Git commit;
4. machine-readable result file at:
   {{RESULT_PATH}}

## COMMIT FORMAT

{{WORKITEM_ID}}: <concise description>

## RESULT FORMAT

Return:

{
  "workitem_id": "{{WORKITEM_ID}}",
  "attempt_id": "{{ATTEMPT_ID}}",
  "status_claim": "IMPLEMENTED | NO_CHANGE | BLOCKED",
  "commit_sha": "<sha-or-null>",
  "changed_files": [],
  "commands_run": [],
  "worker_notes": "<brief factual notes only>"
}

Your status claim is informational only.
It cannot set acceptance state.

## KNOWN PRIOR ATTEMPT FAILURES

{{PRIOR_FAILURES}}

For Stage 2 first-attempt measurement this field MUST be:

NONE — fresh independent attempt.

## STOP CONDITION

Stop when you have either:

- produced one coherent implementation commit, or
- determined that you cannot produce a coherent implementation inside this attempt.

Do not start a second implementation strategy after the attempt limit.
Do not invoke another agent.
Do not ask the user for help.
```

Before run 1:

1. save the exact file;
2. normalize line endings;
3. run `sha256sum`;
4. record the SHA in the experiment manifest;
5. instantiate every Stage 2 French packet mechanically from this template;
6. verify the template hash before each attempt.

The **on-disk SHA**, not a hash copied from chat, is authoritative.

---

**7. Acceptance harness creation and independent review**

Add this mandatory pre-run lifecycle:

```text
LOCKED OWNER PREDICATE
        ↓
HARNESS IMPLEMENTER — fresh session
        ↓
HARNESS DIFF + PREDICATE + BASELINE
        ↓
INDEPENDENT HARNESS REVIEWER — different fresh session
        ↓
REJECT ──→ bounded harness rework ──→ fresh review
        ↓
ACCEPT
        ↓
RUN HARNESS AGAINST BASELINE
        ↓
CONFIRM IT DISCRIMINATES
        ↓
HASH ALL PROTECTED HARNESS FILES
        ↓
FREEZE BASELINE SHA + HARNESS HASH MANIFEST
        ↓
ONLY NOW MAY STAGE 2 RUN 1 START
```

The harness reviewer must answer, using evidence:

* Does every frozen predicate clause have a corresponding real check?
* Can a missing French implementation incorrectly pass?
* Can an implementer satisfy a check merely by writing a success marker/file?
* Does the harness exercise actual product state/render logic rather than a duplicate mock implementation?
* Are failure cases tested?
* Does it distinguish the current baseline appropriately?
* Does it avoid judging requirements outside the benchmark?
* Does it avoid subjective source-code style judgments?
* Can a worker weaken it from its allowed workspace?
* Are all harness artifacts reproducible from a fresh shell?

Protected files then receive a manifest such as:

```json
{
  "baseline_sha": "...",
  "predicate_version": "FRENCH-VISUAL-V1",
  "packet_template_sha256": "...",
  "protected_files": {
    "checks/french_state.test.*": "...",
    "checks/french_runtime.*": "...",
    "checks/french_geometry.*": "...",
    "verify.sh": "...",
    "experiment-manifest.json": "..."
  },
  "independent_review": {
    "result": "PASS",
    "reviewer_attempt_id": "...",
    "evidence_path": "..."
  }
}
```

Before and after every worker attempt, recompute these hashes.

Any worker modification to a protected harness file is automatically:

**`MALFORMED — PROTECTED_HARNESS_MUTATION`**

and counts as a non-ACCEPT engineering attempt.

That closes the self-approval hole.

---

**8. Acceptance contract required before every Stage 3 WorkItem**

Add a hard controller rule:

> **A product WorkItem is not eligible for dispatch unless every mandatory requirement it claims to implement has a frozen acceptance contract and the referenced harness files have verified hashes.**

Create one acceptance-contract record per requirement with at least:

```json
{
  "requirement_id": "NAIL-P0-BUILDER-006",
  "contract_version": 1,
  "predicate": "observable pass condition",
  "verification_kind": [
    "deterministic",
    "runtime",
    "visual"
  ],
  "commands": [
    "./verify.sh --only NAIL-P0-BUILDER-006"
  ],
  "expected_evidence": [
    "test-result",
    "exit-code",
    "screenshot"
  ],
  "baseline_result": "FAIL",
  "baseline_evidence": "...",
  "hardware_limit": null,
  "harness_files": [],
  "harness_sha256": "...",
  "independent_review": "PASS",
  "state": "FROZEN"
}
```

Permitted contract states:

```text
DRAFT
IMPLEMENTED
REVIEW_PENDING
FROZEN
RETIRED
```

Only `FROZEN` makes the associated WorkItem runnable.

A requirement that cannot yet be verified receives an explicit contract such as:

```text
state: FROZEN
verification_kind: hardware-limited
dispatch_allowed: true/false as appropriate
reason: exact missing capability
substitute_evidence: exact strongest substitute
release_limitation: exact remaining uncertainty
```

This means Stage 3 can never recreate the historical failure:

> implement first → decide later what “done” was supposed to mean.

For Stage 2, only the French contract needs to be frozen.
**Before Stage 3 begins dispatching general product WorkItems, all mandatory P0 requirements must have frozen contracts.**

---

# C. Additional hardening — now decided

**9. Environment-contention rule**

Sample host resources every **15 seconds** for every attempt.

Record:

* total CPU;
* experiment-worker CPU;
* foreign/non-experiment CPU;
* load average;
* free/available RAM;
* swap activity;
* disk free space.

Introduce a new non-engineering outcome:

**`ENVIRONMENT-ABORT`**

An attempt is invalidated and its numbered slot retried when any of these occur:

* foreign processes consume **>50% of total host CPU capacity continuously for 5 minutes**;
* `MemAvailable` remains below **2 GB for 5 minutes**;
* the kernel/OOM killer terminates an experiment process;
* severe sustained swapping clearly prevents normal execution;
* disk falls below **5 GB free** during the attempt;
* a known unrelated host process causes termination or service starvation.

`ENVIRONMENT-ABORT`, like `PROVIDER-ABORT`, does **not** enter the 20-attempt engineering denominator.

Ordinary variable VPS load below those thresholds is accepted as experimental noise.

Do not inspect results first and then decide whether contention “felt bad.”

---

**10. Verification-time budget**

Each attempt has two clocks:

```text
IMPLEMENTATION:
maximum 60 minutes

INDEPENDENT VERIFICATION:
maximum 20 additional minutes
```

Therefore maximum end-to-end slot duration is **80 minutes**.

The worker is killed/stopped at 60 minutes if it has not produced its implementation result.

Verification then runs independently.

If verification exceeds 20 minutes because the **candidate itself** causes a hanging build/test/runtime path, the attempt is a non-accepting engineering result:

**`REWORK — VERIFICATION_TIMEOUT`**

If verification cannot finish because of an independently demonstrated provider/host/infrastructure failure, classify it as the appropriate:

* `PROVIDER-ABORT`, or
* `ENVIRONMENT-ABORT`

and retry the slot.

The existing 24-hour benchmark ceiling still applies.

---

**11. The ≥60% number is baseline-specific**

Record this explicitly in the experiment report:

> The measured first-attempt acceptance rate is a property of the tuple
> **{frozen baseline SHA, benchmark task, worker packet version, acceptance harness version, provider, model, environment configuration}**.
> It is not an eternal score for the worker/model.

The initial ≥60% result authorizes Stage 3's initial execution architecture.

After the **Phase 3 builder redesign**, do a small **10-attempt recalibration** before making any further worker-concurrency increase or treating the original Stage 2 rate as representative of later builder work.

That recalibration:

* does not undo accepted Stage 3 work;
* does not block continuing with one worker;
* uses a representative bounded post-redesign WorkItem;
* uses the same acceptance-first discipline;
* is used to decide whether scaling beyond one implementation worker remains justified.

Do **not** reuse the French throwaway benchmark as the permanent productivity metric.

---

**12. Remote backup policy**

If authenticated private GitHub access exists, before Stage 2 run 1:

1. create/use a **private** remote;
2. push the untouched/import baseline commit;
3. push the pre-experiment tooling/harness baseline commit;
4. tag or otherwise record the exact frozen experiment baseline SHA.

Do **not** push:

```text
.hermes/experiments/
.hermes/logs/
.hermes/worktrees/
.hermes/evidence/   # where it contains experiment/runtime evidence
provider credentials
environment dumps containing secrets
temporary attempt branches
```

Keep experiment evidence in the durable local experiment store and, if desired, a separate private archive/backup—not mixed into the product repository.

During Stage 3:

> **After every accepted canonical integration, push the resulting canonical commit to the private remote.**

Rejected/experimental worker branches remain local evidence and are not routinely pushed.

If GitHub authentication is unavailable, the lack of remote does not block Stage 2/3, provided the local Git baseline and a separate local backup are verified.

---

## Final commissioning gate

The system must refuse to start Stage 2 run 1 until all of these are true:

```text
[ ] canonical baseline SHA frozen
[ ] benchmark mode frozen:
      FRENCH-VISUAL-V1
      OR automatically selected pre-registered
      FRENCH-DETERMINISTIC-NONVISUAL-V1
[ ] model/provider frozen
[ ] packet template written + hashed
[ ] French acceptance contract written
[ ] acceptance harness implemented
[ ] harness independently reviewed
[ ] harness proves baseline discrimination
[ ] harness files hashed and protected
[ ] environment sampling enabled
[ ] Git isolation strategy verified
[ ] experiment budget counters initialized
[ ] provider-abort and environment-abort rules loaded
[ ] AR spike launched or queued independently
```

And Stage 3 must refuse general product dispatch until:

```text
[ ] Stage 2 gate passed at >=60%
[ ] every mandatory P0 requirement has explicit dependency edges
[ ] every dispatched requirement has a FROZEN acceptance contract
[ ] AR architecture spike is complete before native AR implementation
[ ] private backup exists where credentials permit, otherwise local backup verified
```

That closes the remaining loopholes. Most importantly, **the system now knows what to do before it encounters every major branch**—browser failure, low benchmark performance, AR incompatibility, environment contention, acceptance-harness weakness, post-redesign metric drift, and backup availability—rather than asking you to steer it after seeing the outcome.
```

===== 2026-09-22 01:18 | session 20260921_234803_2d9335 | @file:`.hermes/attachments/Pasted content (65.5… =====
has this been organised properly

===== 2026-09-22 01:21 | session 20260921_234936_670e4e | prep for nailify =====
explain fully hat info you need?

===== 2026-09-22 01:24 | session 20260921_234803_2d9335 | @file:`.hermes/attachments/Pasted content (65.5… =====
finish the audit

===== 2026-09-22 01:28 | session 20260921_234936_670e4e | prep for nailify =====
i dont want you to make this now. i actually ant to tweak the plan a little bit. i have some claude code usage i need to use up (it refreshes at 2:50) and i want to use it as much as possible. i mean the fulll 5 hour indow usage at 2:50, 7:50, and 12:50. i kno this will take a while to build, i still want to heavy lifting of coding done by freellmapi.  but use up claude as much as needed for important reviews, and planning 


1. **Path A — build the acceptance harness first.**
   Freeze acceptance against the **current HEAD `f5f33f2`**, not against the old baseline assumptions. Record current truth honestly: existing capabilities may already pass; incomplete ones fail; hardware/environment-limited items remain explicitly unverified. Do **not** spend the 20-worker benchmark budget on French now that French is already substantially implemented. The more valuable next measurement is whether the remaining gaps can be expressed as bounded WorkItems with frozen predicates.

2. **Yes — treat Phases 1–2 as complete and skip them.**
   Do not redo foundation, schema-v2/project-library work, or native AR merely because earlier planning documents assumed they were unfinished. The verified current repository state supersedes those stale baseline assumptions. Preserve existing passing behaviour and test coverage.

3. **Yes — you have permission to build the acceptance harness now.**
   Create `verify.sh` and the associated fixed predicates/evidence machinery as the **sole acceptance authority before further product implementation proceeds**. The harness may add acceptance/testing infrastructure, but it must not weaken existing tests or modify product behaviour merely to make checks pass.

One additional decision follows from this: **retire the French 20-run benchmark as the Stage 2 measurement task.** Once the acceptance layer is operational, choose a genuinely outstanding, bounded requirement from the remaining gaps and pre-register its predicate before using worker-hours to measure first-attempt acceptance. French can remain an acceptance case, but it should no longer be the worker-reliability benchmark.

===== 2026-09-22 01:29 | session 20260921_234936_670e4e | prep for nailify =====
now do not start this your self. please product he complete prompt, exhaustive detial  attention to granular detail prompt to have another chat start and finish this /goal project. make sure the prompt is a slash goal startgin prompt with clear criteria of success