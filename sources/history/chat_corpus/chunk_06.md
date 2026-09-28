

===== 2026-09-18 19:16 | session 20260918_191557_7bb61a | @file:`.hermes/attachments/Pasted content… =====
@file:`.hermes/attachments/Pasted content (24-2.6 KB)`

--- Attached Context ---

📄 @file:`.hermes/attachments/Pasted content (24-2.6 KB)` (6014 tokens)
```
# EMPIRIUM — FINAL AUTOPILOT COMPLETION DIRECTIVE

You are continuing an existing Empirium build.

This is NOT a new architecture exercise.

This is NOT another autonomy redesign.

This is NOT another audit-only task.

The production autonomy control plane has already been implemented, commissioned, and is running independently of Hermes sessions.

Your objective now is:

> **Connect the real autonomous product-worker execution layer to the existing production reconciler, then allow the resulting system to autonomously complete the entire Empirium product until the deterministic final acceptance gate genuinely passes.**

From this point forward, the user must not need to repeatedly say:

* continue;
* carry on;
* retry;
* finish it;
* what next?

The system must continue itself.

---

# 1. CURRENT VERIFIED STATE

Treat the following as the starting point unless live inspection proves something has changed.

Current production autonomy state:

* PostgreSQL-backed production reconciler exists.
* Durable startup recovery exists.
* Atomic WorkItem leasing exists.
* Attempt lifecycle persistence exists.
* Worker-death recovery exists.
* Provider timeout/rate-limit waiting and retry exists.
* QA rejection and automatic rework exists.
* Stale-evidence rejection exists.
* Dependency release exists.
* Deterministic project completion exists.
* The reconciler continues running when no WorkItems are immediately ready.
* Real subprocess execution has been commissioned.
* User-level systemd service exists:

```text
empirium-autonomy-reconciler.service
```

* Service is enabled.
* Service is active.
* `Restart=always`.
* Service is independent of Hermes/browser/terminal session lifetime.
* Real commissioning project passed.
* 10/10 commissioning WorkItems reached ACCEPTED.
* Reconciler restart was genuinely exercised.
* Worker process death while holding a lease was genuinely exercised.
* PostgreSQL state survived restart.
* QA rejection/rework was genuinely exercised.
* Provider-failure states were genuinely exercised.
* Dependency progression was genuinely exercised.
* Director session was absent during part of execution.
* Paid inference during commissioning was $0.00.
* No synthetic restart-success booleans are accepted as evidence.
* Current commissioned code includes commit:

```text
712039d
commission production autonomy reconciler
```

DO NOT REBUILD THIS CONTROL PLANE FROM SCRATCH.

DO NOT create a second competing scheduler.

DO NOT replace PostgreSQL with JSON or SQLite.

DO NOT return to chat-driven project continuity.

---

# 2. CURRENT REAL PRODUCT STATE

The Initial Product Acceptance gate is correctly still FAIL.

The following known product predicates have already been converted into durable PostgreSQL WorkItems:

```text
EMP-003
PRJ-001
WRK-005
OFF-001
RES-001
```

They currently wait for a genuine product-capable worker.

The critical current state is:

```text
WAITING_WORKER
```

That is the next problem to solve.

Do NOT falsely mark these WorkItems complete.

Do NOT use the deterministic commissioning worker to approve real product work.

Do NOT weaken their acceptance criteria.

---

# 3. THE FINAL MISSING ARCHITECTURAL LINK

Implement and wire the production product-worker executor.

Required path:

```text
systemd
    ↓
production reconciler
    ↓
PostgreSQL WorkItem
    ↓
lease / Attempt
    ↓
REAL PRODUCT WORKER EXECUTOR
    ↓
Hermes + FreeLLMAPI
    ↓
isolated worktree
    ↓
actual engineering work
    ↓
tests / runtime / browser / visual evidence
    ↓
structured machine-readable handoff
    ↓
production reconciler
    ↓
independent QA
    ↓
ACCEPTED
or
REWORK_REQUIRED
    ↓
automatic next Attempt
```

Once this path works, the reconciler must repeatedly use it until the entire product is complete.

---

# 4. PRODUCT WORKER EXECUTOR — REQUIRED BEHAVIOUR

Build the smallest maintainable production worker-execution layer needed to perform real Empirium engineering work.

It must accept a leased WorkItem/Attempt and construct a bounded worker context containing at least:

* project ID;
* WorkItem ID;
* Attempt ID;
* requirement/capability IDs;
* title;
* objective;
* acceptance criteria;
* dependencies;
* previous Attempt summaries;
* existing defects/rejections;
* relevant source files;
* relevant product specification excerpts;
* permitted repository;
* permitted write scope;
* prohibited write scope;
* required test commands;
* runtime checks;
* browser checks;
* visual checks if applicable;
* accessibility checks if applicable;
* base SHA;
* worktree path;
* branch;
* expected structured output.

The worker MUST NOT receive an unnecessarily huge whole-project transcript when bounded context is enough.

---

# 5. USE REAL HERMES WORKERS

The executor should invoke real Hermes workers through the existing authorized local installation.

Expected conceptual command:

```bash
hermes \
  --provider custom:freellmapi \
  -m auto:empirium-code \
  --in <isolated-worktree> \
  -z "<compiled WorkItem prompt>"
```

Adapt syntax to the actual installed Hermes version.

Do not blindly copy the example if the installed CLI differs.

Inspect the installed Hermes CLI first.

Use the existing isolated Empirium Hermes profile where appropriate.

Do not accidentally invoke OpenRouter.

Do not silently choose another paid provider.

---

# 6. INFERENCE POLICY

New metered/pay-as-you-go inference budget remains:

```text
$0.00
```

OpenRouter is prohibited for this autonomous completion run.

Allowed inference:

* genuinely free FreeLLMAPI routes;
* genuinely free direct providers already configured;
* suitable local models;
* existing non-metered subscription-backed access only where already authorized and appropriate.

No automatic paid fallback.

No “it only costs a few cents”.

No OpenRouter because free routes are temporarily unavailable.

If all approved worker inference is unavailable:

```text
WorkItem → WAITING_PROVIDER
```

The reconciler remains alive.

The project remains unfinished.

Retry later.

---

# 7. WORKER OUTPUT CONTRACT

Every product worker must return a structured result.

Use a machine-readable format similar to:

```json
{
  "work_item_id": "...",
  "attempt_id": "...",
  "outcome": "IMPLEMENTED",
  "base_sha": "...",
  "result_sha": "...",
  "branch": "...",
  "worktree": "...",
  "files_changed": [],
  "tests": [
    {
      "command": "...",
      "exit_code": 0,
      "passed": true
    }
  ],
  "runtime_evidence": [],
  "browser_evidence": [],
  "visual_evidence": [],
  "accessibility_evidence": [],
  "known_remaining_defects": [],
  "provider": "...",
  "requested_model": "...",
  "effective_model": "...",
  "execution_id": "...",
  "reported_cost_usd": 0
}
```

Possible outcomes must distinguish at least:

```text
IMPLEMENTED
NO_PROGRESS
INVALID_WORK
TEST_FAILED
RUNTIME_FAILED
BLOCKED
REPLAN_REQUIRED
PROVIDER_UNAVAILABLE
RATE_LIMITED
TIMEOUT
AUTH_FAILURE
```

Transport success is not implementation success.

LLM output is not evidence by itself.

---

# 8. ISOLATED WORKTREES

Real implementation workers should work in isolated Git worktrees where practical.

One implementation WorkItem should normally have:

```text
one lease
one primary writer
one Attempt
one isolated worktree
one bounded diff
```

Workers must not directly modify:

* production scheduler;
* reconciler service;
* control database truth;
* acceptance gate truth;
* worker leases;
* QA acceptance records;
* integration branch;
* unrelated repositories;
* systemd control files;

unless the WorkItem specifically and legitimately concerns that protected component.

---

# 9. DO NOT LET WORKERS SELF-APPROVE

Implementation and approval must remain separate.

Required lifecycle:

```text
READY
↓
LEASED
↓
RUNNING
↓
IMPLEMENTED_UNVERIFIED
↓
TESTING
↓
REVIEW_PENDING
↓
ACCEPTED
```

or:

```text
REVIEW_PENDING
↓
REWORK_REQUIRED
↓
READY
↓
new Attempt
```

Implementers cannot mark themselves accepted.

A worker saying:

```text
done
complete
fixed
production ready
```

has no authority to change acceptance.

Acceptance is derived from evidence.

---

# 10. GOAL MODE

For substantial bounded engineering WorkItems, use Hermes goal mode where it genuinely helps a single worker finish its assigned objective.

Do NOT use `/goal` as global project persistence.

The reconciler already provides global project persistence.

Goal mode is only a worker-level completion aid.

Use reasonable per-WorkItem limits such as:

```text
20–40 turns
```

depending on task complexity.

If the goal turn limit is exhausted:

* preserve the worker's progress;
* classify the Attempt correctly;
* do not mark the WorkItem complete;
* create another Attempt, replan, split, or diagnose as appropriate.

Goal exhaustion is not project termination.

---

# 11. NO `/LOOP` AS THE AUTONOMY MECHANISM

Do not depend on `/loop` to keep this project alive.

The durable production reconciler owns continuity.

If `/loop` is useful inside some disposable diagnostic worker it may be used, but it must not be required for background project operation.

---

# 12. CONNECT WAITING_WORKER TO REAL EXECUTION

Implement the actual transition from:

```text
WAITING_WORKER
```

to a real executable Attempt.

The production reconciler must be capable of:

1. discovering a runnable WorkItem;
2. acquiring the lease;
3. creating the Attempt;
4. creating the isolated worktree;
5. compiling bounded context;
6. launching a Hermes worker subprocess;
7. recording PID/process identity;
8. recording provider/model identity;
9. monitoring execution;
10. capturing structured output;
11. capturing Git result SHA;
12. capturing tests/evidence;
13. classifying failure;
14. releasing the worker process cleanly;
15. moving the WorkItem into testing/review/rework/wait;
16. automatically processing the next WorkItem.

No Hermes chat must be needed between those steps.

---

# 13. FIRST REAL END-TO-END TEST

Before unleashing the system on the entire backlog, prove one genuine real-product WorkItem.

Prefer:

```text
EMP-003
```

unless dependencies or current state make another known WorkItem more appropriate.

The test must use:

* real PostgreSQL WorkItem;
* real production reconciler;
* real leased Attempt;
* real Hermes product worker;
* real FreeLLMAPI route;
* real isolated worktree;
* real repository changes;
* real tests;
* real browser/runtime verification if required;
* real result SHA;
* real independent QA.

Then deliberately verify unattended continuation.

During or after the first real product WorkItem:

* ensure the initiating Hermes session is not needed;
* ensure the reconciler service remains active;
* ensure the worker was launched by the background system;
* ensure the result was consumed automatically;
* ensure QA/rework happens automatically if necessary.

The system is considered product-worker commissioned only if a real product WorkItem advances without the user manually telling it to continue.

---

# 14. THEN PROCESS ALL FIVE KNOWN PRODUCT WORKITEMS

After the real-worker path is proven, allow the production reconciler to process:

```text
EMP-003
PRJ-001
WRK-005
OFF-001
RES-001
```

Do not process them by pretending state has changed.

Implement the product requirement each ID actually represents.

---

# 15. EMP-003 — EMPLOYEE DOSSIER

Complete the dedicated persistent Employee dossier/current-operation experience.

At minimum it should truthfully expose relevant durable information such as:

* employee identity;
* role;
* department;
* persistent configuration;
* current state;
* current WorkItem;
* current Attempt;
* requested model;
* effective model;
* provider;
* execution binding;
* relevant history;
* permissions/tool scope where appropriate;
* QA/review information where useful.

Use canonical PostgreSQL-backed state.

Do not fabricate metrics.

Acceptance must include real browser/runtime evidence.

---

# 16. PRJ-001 — DURABLE PROJECT / TASK / RUN WORKSPACE

Implement the actual persistent Project workspace.

The user must be able to inspect a project and its work hierarchy.

At minimum surface relevant truth for:

```text
Project
→ Capability/Requirement
→ WorkItem/Task
→ Attempt/Run
→ evidence
→ QA
→ artifacts
→ history
```

The workspace must read durable canonical state.

It must not merely project ephemeral Hermes session data.

Acceptance must include real browser/runtime testing.

---

# 17. WRK-005 — PRODUCTION RECONCILER CONTINUATION

Do not accept this simply because the reconciler service exists.

Prove that the production path actually owns real product execution.

Acceptance must include:

* real WorkItem;
* real Attempt;
* worker dispatch;
* process death/recovery where relevant;
* state survival;
* automatic next-action continuation;
* no active Director dependency;
* exact durable evidence.

The newly attached product-worker executor is part of satisfying this requirement.

---

# 18. OFF-001 — LIVING OFFICE

Complete the real living-office runtime.

The office must be a projection of actual operational state.

Worker visuals may represent states such as:

```text
idle
queued
working
thinking
coding
researching
testing
reviewing
waiting
blocked
approval required
error
rate limited
completed
offline
```

But visual state must map to durable operational truth.

Do not create fake “busy” animation.

Use the existing Empirium visual assets where appropriate.

The office should eventually represent actual persistent workers and their WorkItems/Attempts.

Acceptance must include visual/browser evidence.

---

# 19. RES-001 — BROWSER-CLOSE CONTINUATION

This is not documentation.

Actually prove it.

Start real work through the normal product/autonomous path.

Then ensure the initiating browser/UI session is no longer responsible.

Verify after the session disappears that:

* reconciler remains active;
* worker execution continues or resumes;
* PostgreSQL state remains authoritative;
* task progresses;
* QA/rework continues;
* another WorkItem can subsequently dispatch.

Capture evidence.

Only then mark RES-001 accepted.

---

# 20. AFTER THE FIVE KNOWN PREDICATES, DO NOT AUTOMATICALLY STOP

The five known failures are the current Initial Product Acceptance failures.

They are NOT necessarily the entire original product specification.

Once they pass:

1. rerun Initial Product Acceptance;
2. read `ORIGINAL_WORKFORCE_SPEC.md`;
3. read `CURRENT_CAPABILITY_STATE.json`;
4. read `REMAINING_PRODUCT_BACKLOG.json`;
5. read `MARKET_RELEASE_BACKLOG.md`;
6. read product docs;
7. inspect actual product/runtime;
8. identify every remaining mandatory requirement.

Build the project to the complete agreed specification, not merely until the five current flags disappear.

---

# 21. TRACEABILITY

Every mandatory requirement must trace through:

```text
Requirement
↓
Capability
↓
WorkItem
↓
Attempt
↓
candidate revision
↓
tests
↓
runtime/visual/recovery evidence
↓
independent review
↓
ACCEPTED
```

No mandatory requirement may disappear merely because no WorkItem exists for it.

---

# 22. ZERO-ACTIVE-WORK INVARIANT

This is essential.

At every reconciliation cycle evaluate:

```text
IF final product acceptance != PASS
AND there are no legitimate READY/RUNNING/WAITING_RETRY WorkItems
AND remaining requirements are not all explained by precise unavoidable HUMAN_BLOCKED states

THEN
    automatically create CONTROL_PLANE_DIAGNOSIS / REPLAN work.
```

It must never again reach:

```text
product incomplete
+
no workers
+
no work queued
+
system quietly stopped
```

That state is forbidden.

---

# 23. FAILURE HANDLING

## Worker death

```text
Attempt → INTERRUPTED
lease released/reclaimed
WorkItem survives
new Attempt automatically possible
```

## Provider unavailable

```text
Attempt records provider failure
WorkItem → WAITING_PROVIDER
retry later
```

## Rate limit

Use bounded exponential/provider-aware waiting.

Do not burn endless retries.

## Successful LLM but no progress

Do not classify as provider failure.

Record:

```text
LLM_SUCCESS_NO_PROGRESS
```

Then:

* avoid identical unproductive route for the next Attempt;
* refresh bounded context where appropriate;
* retry using a different free route/model where possible.

## Repeated semantic failure

After two materially similar failures:

```text
DIAGNOSE
REPLAN
or
SPLIT WORKITEM
```

Do not perform identical retries indefinitely.

## Failed tests

Rework.

## Failed runtime verification

Rework.

## QA rejection

Rework.

## Dependency unavailable

Wait.

## True missing credential

Precise HUMAN_BLOCKED.

Continue all independent work.

---

# 24. FREELLMAPI

Before heavy autonomous operation, ensure the actual live FreeLLMAPI runtime is healthy.

Verify rather than assume:

* live container/process running;
* correct database mounted;
* migrations applied;
* `empirium-code` profile exists;
* usable free providers configured;
* OpenRouter not part of this route;
* fallback works;
* route avoidance/no-progress feedback works;
* provider errors are observable;
* outcome endpoint/path is connected where designed.

Do not merely verify repository source code.

Verify live behaviour.

---

# 25. REAL EVIDENCE ONLY

Never again use synthetic commissioning claims.

Forbidden evidence includes:

```json
{
  "restart_passed": true
}
```

when nobody actually restarted anything.

If a requirement says:

```text
survives restart
```

restart it.

If a requirement says:

```text
survives worker death
```

kill a test worker.

If a requirement says:

```text
continues after browser closes
```

remove the browser/session from the execution chain.

If a requirement says:

```text
QA rejection creates rework
```

cause a controlled rejection.

Evidence must be derived from observable events, not prefilled expectations.

---

# 26. PROTECT EXISTING WORK

Before significant operations:

* inspect Git state;
* preserve unrelated dirty files;
* create recovery commit/tag where appropriate;
* avoid destructive cleanup.

Never use destructive commands against unknown user work.

---

# 27. AUTONOMOUS OPERATION

Once the real product-worker executor has passed commissioning, hand execution to the production control plane.

Do not continue trying to personally act as the long-running Director inside this initiating session.

The durable system should own:

* work selection;
* worker launch;
* retries;
* rework;
* provider waiting;
* dependencies;
* evidence;
* QA;
* acceptance;
* progression to the next item.

A new intelligent planner/architect may be launched when genuinely needed, but that planner is a disposable worker too.

---

# 28. HUMAN INTERVENTION POLICY

Do not ask the user routine questions.

Do not stop because:

* a test failed;
* a worker failed;
* an implementation needs another Attempt;
* a free provider is temporarily down;
* a model produced no progress;
* a UI bug was found;
* QA rejected work;
* work needs decomposition;
* a service needs restarting.

Handle those autonomously.

Only require the user when there is a truly unavoidable external blocker such as:

* missing credentials the machine cannot obtain;
* irreversible external financial action;
* destructive action affecting unrelated user data;
* legal/contractual approval;
* genuinely unresolved product decision absent from the source specification.

Even then:

* record HUMAN_BLOCKED durably;
* continue every independent task;
* leave the reconciler running.

---

# 29. DEFINITION OF DONE

The project is complete ONLY when all of the following are true:

### Autonomy

* reconciler active;
* real product-worker executor active;
* work automatically dispatches;
* retries/rework occur automatically;
* session/browser/RDP/SSH not required;
* worker death recovery proven;
* reconciler restart recovery proven;
* unattended continuation proven.

### Product

* complete mandatory Empirium specification implemented;
* known current five predicates accepted;
* no unresolved mandatory capability remains partial;
* no mandatory backlog silently omitted.

### Quality

* complete test suite passes;
* typecheck passes;
* production build passes;
* browser/runtime tests pass;
* visual QA passes where required;
* accessibility QA passes where required;
* independent QA passes;
* no known critical defects.

### Durability

* canonical PostgreSQL state survives restart;
* WorkItems/Attempts/history remain inspectable;
* office state is truthful;
* Projects/Employees remain persistent;
* no fake activity/state.

### Inference

* no accidental OpenRouter usage;
* new paid inference cost remains $0.00;
* provider/model information recorded correctly;
* provider failure cannot create false completion.

### Evidence

* final exact Git SHA recorded;
* runtime/build revision matches expected source;
* final acceptance evidence corresponds to final SHA;
* stale evidence cannot approve new code;
* no synthetic completion claims.

---

# 30. FINAL ACCEPTANCE GATE

Maintain a deterministic final product gate.

The gate is the authority.

Not the worker.

Not the Director.

Not this current conversation.

Not a written report.

If:

```text
FINAL_ACCEPTANCE = FAIL
```

then:

```text
MORE WORK EXISTS
```

The autonomous system continues.

Only:

```text
FINAL_ACCEPTANCE = PASS
```

allows the implementation program to transition into completed/monitoring mode.

---

# 31. WHEN THIS CURRENT SESSION MAY STOP

This current initiating Hermes session must not stop immediately after merely writing the worker executor.

Before this bootstrap session relinquishes responsibility, verify:

1. real product-worker executor exists;
2. production reconciler can launch it;
3. one real product WorkItem has been attempted;
4. worker subprocess actually ran;
5. repository was genuinely changed or the Attempt correctly explained why not;
6. structured result returned;
7. reconciler consumed the result;
8. QA/rework path worked;
9. at least one next autonomous action occurred;
10. reconciler remains active;
11. no foreground Hermes session is required for continuation.

At that point this session SHOULD stop acting as project owner.

The production system must remain alive and continue.

---

# 32. COMPLETION RECORD

When the whole project genuinely reaches final PASS, create a durable final completion record.

For example:

```text
AI_WORKFORCE_BUILD/AUTOBUILD_COMPLETE.json
```

Include:

```text
completion timestamp
final Git SHA
final product gate result
requirements accepted
tests
build result
browser/runtime evidence
visual evidence
recovery evidence
worker/reconciler continuity evidence
provider/model summary
OpenRouter invocations
paid inference cost
remaining optional/nonmandatory backlog
```

Also create an appropriate final Git checkpoint/tag.

---

# 33. FINAL OPERATING PRINCIPLE

There must no longer be a concept of:

```text
Hermes worked for a while and then stopped.
```

Hermes workers are disposable.

The project is durable.

Workers come and go.

Providers come and go.

Attempts fail.

QA rejects changes.

Processes restart.

The project continues.

The machine must always be able to answer:

```text
What remains?
What is runnable?
What is currently running?
What failed?
What should retry?
What requires rework?
What requires QA?
What is blocked?
What is accepted?
What happens next?
```

without requiring the user to tell it.

---

# EXECUTE NOW

Do not return with another architecture proposal.

Do not merely explain what should be built.

Do not stop after an audit.

Start from the current commissioned control plane.

**Implement the real product-worker executor.**

Commission it against a genuine Empirium WorkItem.

Then hand execution to the persistent production reconciler.

Allow it to process the product continuously and autonomously.

Continue repairing, retrying, testing, reviewing, integrating, and progressing until the complete Empirium product reaches deterministic final acceptance.

**The project stops only when the product is genuinely complete.**
```

===== 2026-09-18 23:37 | session 20260901_210007_610e716d | Friendly greeting #2 =====
Are the tasks still going

===== 2026-09-19 09:00 | session 20260901_210007_610e716d | Friendly greeting #2 =====
[Cron delivery: Daily Steam Free-to-Keep monitor]
{"status": "new_free_to_keep_promotions", "source": "https://freetokeep.gg/api/v1/offers?store=steam&limit=200", "discovery_provider": "Free To Keep public Steam offers API (SteamDB fallback)", "promotions": [{"appid": "2484180", "title": "Deadshot", "store_url": "https://store.steampowered.com/app/2484180", "steamdb_sub": "steam:f8d826510f2524cd", "expires": "2026-09-23T17:00:00.000Z"}], "action": "notify_only", "note": "No Steam sign-in or account action was attempted."}

===== 2026-09-19 11:08 | session 20260919_110810_72c7b6 | # AI STAFF FORCE — FULL INDEPENDENT… =====
# AI STAFF FORCE — FULL INDEPENDENT CURRENT-STATE & PROGRESS AUDIT

You are performing a comprehensive, independent, **read-only production audit** of the AI Staff Force project.

This project is NOT Nailify.

Nailify is a separate software project and may have been used as a test workload for autonomous development. Do not confuse Nailify's application code or completion status with the completion status of the AI Staff Force system itself.

The system being audited here is the broader autonomous software-engineering infrastructure intended to turn a detailed product specification into a completed software product with minimal or no continuing human intervention.

Your purpose is to determine:

> **Exactly how much of the AI Staff Force architecture has actually been built, what is operational, what is only partially implemented, what is still conceptual, what is currently running, what has been proven in real workloads, what repeatedly fails, and what remains before this can genuinely operate as a durable autonomous software-development organisation.**

Do NOT continue development.

Do NOT fix anything.

Do NOT modify system state.

This is a forensic current-state audit.

---

# 1. FUNDAMENTAL SYSTEM INTENT

The project is attempting to build an autonomous software-production system based on lessons learned from repeatedly attempting to have LLM agents autonomously build substantial software projects.

The central architectural doctrine is approximately:

```text
PRODUCT CHARTER / MASTER SPECIFICATION
              ↓
     DETERMINISTIC CONTROL PLANE
              ↓
        DURABLE PROJECT STATE
              ↓
      WORK DECOMPOSITION / DAG
              ↓
        BOUNDED WORK PACKETS
              ↓
       DISPOSABLE AI WORKERS
              ↓
       ISOLATED WORKTREES
              ↓
    DETERMINISTIC VALIDATION
              ↓
       INDEPENDENT REVIEW
              ↓
             REWORK
              ↓
           INTEGRATION
              ↓
      SYSTEM / PRODUCT TESTING
              ↓
          RELEASE GATES
              ↓
        FINISHED SOFTWARE
```

The key philosophy is:

> The LLM is not the durable orchestrator.

LL

===== 2026-09-19 11:24 | session 20260919_110810_72c7b6 | # AI STAFF FORCE — FULL INDEPENDENT… =====
that location is in the vps and difficult for me to get, give me the complete md file in this chat

===== 2026-09-19 12:27 | session 20260919_122650_1a1209 | AI Staff Force =====
@file:`.hermes/attachments/Pasted content (94.2 KB)`

--- Attached Context ---

📄 @file:`.hermes/attachments/Pasted content (94.2 KB)` (22854 tokens)
```
You are right. The previous version **compressed too much of the actual product specification into high-level instructions**. In particular, it treated the organization screen, department cockpit, living office and asset system as broad feature categories instead of as **literal product contracts with individually testable requirements**.

The older V4 master protocol was actually much closer to the required level of rigor: it already identified `/home/ash/Desktop/AI Taskforce` as the immutable source/asset root, required a recursive inventory and explicitly said that the existing visual material includes organization UI, department UI, office environments, modular furniture, character proportions, emotional states and animation references.   It also already specified the organization overview and department cockpit at a much deeper level, including real-data binding rather than mock statistics.  

The same is true of testing: V4 already contained a multi-layer evidence matrix, explicit failure-injection suite and deterministic release gate.    The mistake in my last response was **summarizing that protocol rather than upgrading it**.

The prompt below is therefore a **V5 master protocol**, not another summary. It incorporates the newer CAO architecture, the current forensic audit, your new three-model policy, the actual asset library, and—most importantly—the two UI images you just supplied as explicit visual/product contracts. CAO remains the execution transport rather than becoming a competing source of truth; its async `assign` pattern is preferred because the audited blocking handoff timed out.  

---

# EMPIRIUM STUDIO AI WORKFORCE

# MASTER AUTONOMOUS COMPLETION PROTOCOL — VERSION 5

## CAO-INTEGRATED · ASSET-FIRST · SOL-REVIEWED · EVIDENCE-GATED · ONE-SHOT BUILD

**Date:** 19 September 2026
**Mission:** Take the existing Empirium Studio / AI Staff Force from its actual current state to a genuinely finished, polished, durable autonomous AI organization.
**Execution style:** Persistent multi-day engineering programme, not a one-shot chat response.
**Primary implementation intelligence:** FreeLLMAPI.
**Operational orchestration / continuity intelligence:** GPT-5.6 Luna through verified subscription-backed Codex/ChatGPT access.
**Architecture / planning / independent QA / review intelligence:** GPT-5.6 Sol through verified subscription-backed Codex/ChatGPT access.
**Session orchestration transport:** CAO / CLI Agent Orchestrator.
**Durable control:** deterministic supervisor + production reconciler + persistent database state.
**New pay-as-you-go inference budget:** **$0.00.**
**OpenRouter:** **prohibited everywhere, including as a hidden fallback.**

---

# 0. THIS IS THE FINAL EXECUTION CONTRACT

You are not being asked to write another architecture document.

You are not being asked to audit the application and stop.

You are not being asked to produce recommendations for the user.

You are not being asked to create an MVP.

You are not being asked to create an attractive mock-up.

You are not being asked to make a subset of the product work and declare success.

You are being instructed to **take ownership of the existing engineering programme and continue autonomously until the finished Empirium Studio AI Workforce has been implemented, integrated, tested, visually validated, failure-tested, burn-in tested, independently reviewed and passed by the deterministic release gate.**

The required lifecycle is:

**discover → preserve → reconcile → repair infrastructure → reconcile requirements → reconcile assets → freeze architecture contracts → decompose → implement → test → independently review → reject/rework where necessary → integrate → regression-test → visually review → failure-test → restart-test → security-test → accessibility-test → performance-test → run autonomous commissioning → burn-in → source reconciliation → final Sol review → deterministic release gate → SHIPPED.**

A stopped LLM is not completion.

A stopped CAO session is not completion.

A stopped Hermes chat is not completion.

No active workers is not completion.

An empty task queue caused by orchestration failure is not completion.

A passing unit suite is not completion.

A beautiful dashboard is not completion.

A worker saying "done" is not completion.

A markdown file saying COMPLETE is not completion.

A previous agent claiming release readiness is not completion.

There is only one final success condition:

```text
DETERMINISTIC_RELEASE_GATE.exitCode == 0
AND
all mandatory requirements == VERIFIED
AND
no mandatory evidence is stale
AND
no unresolved release blocker exists
```

Only then may:

```text
BUILD_STATE.status = SHIPPED
```

---

# 1. SOURCE AUTHORITY AND PRECEDENCE

This V5 prompt is the current **execution-policy authority**.

However, previous project material remains product-requirement authority where it contains requirements that have not explicitly been superseded.

This is essential.

A newer prompt forgetting to mention an old product requirement does **not** erase that requirement.

Use this precedence model:

### 1. Current explicit user decisions in this V5 prompt

These override contradictory older instructions.

Examples:

* only FreeLLMAPI + Luna + Sol may be used as LLM intelligence;
* Opus/Sonnet/Astra are no longer part of this build;
* OpenRouter is prohibited, including free OpenRouter;
* CAO is now part of the execution architecture;
* Sol replaces previous Opus review duties;
* the blue-and-yellow supplied robot design is the canonical workforce character language;
* the two supplied UI mockups are mandatory visual/product references;
* Empirium Studio remains separate from Empirium OS.

### 2. Existing immutable product-source material

Especially everything under:

```bash
"/home/ash/Desktop/AI Taskforce"
```

and existing copied sources under:

```text
/home/ash/empirium-studio/AI_WORKFORCE_BUILD/source/
```

### 3. Existing V4 master protocol Part A and Part B

They remain requirements sources except where V5 explicitly supersedes them.

### 4. Existing forensic audits

These are evidence of the observed state at a particular time.

They are not permanent design authority.

### 5. Existing implementation

Existing code is evidence of implementation—not automatic evidence that the implementation is correct.

---

# 2. ABSOLUTE ANTI-SCOPE-COLLAPSE LAW

Previous attempts repeatedly transformed the real specification into a smaller system that was easier to finish.

This must never happen again.

Difficulty changes **decomposition**, never scope.

If a requirement is too large:

```text
REQUIREMENT X
    ↓
X-A
X-B
X-C
X-D
```

Do not replace X with an easier approximation.

No agent may remove a mandatory requirement because:

* it is visually difficult;
* FreeLLMAPI struggles with it;
* it requires many files;
* the current codebase does not support it cleanly;
* it takes multiple days;
* animation is hard;
* browser testing is inconvenient;
* the database schema needs changing;
* available free models fail repeatedly;
* the VPS is CPU-only;
* it requires complicated reconciliation;
* the current UI has a simpler version;
* an old implementation already claimed completion.

If implementation is hard:

**decompose, diagnose, rearchitect, retry and review.**

Never quietly weaken the requirement.

---

# 3. THE PRODUCT BEING BUILT

The finished application is:

# EMPIRIUM STUDIO

It is a standalone evolution of Hermes Studio intended to operate as the user's persistent AI company.

It is **not Empirium OS**.

Empirium OS is a separate personal software/journal product.

Do not modify Empirium OS merely because the supplied UI concepts historically display the "EMPIRIUM OS" branding.

For the workforce product, adapt those references to the authoritative current product branding:

```text
EMPIRIUM STUDIO
AI ORGANIZATION
```

unless the existing target code contains a later explicitly approved branding decision.

The actual product experience is:

```text
Organization
    ↓
Departments
    ↓
Persistent Employees
    ↓
Projects
    ↓
Tasks / WorkItems
    ↓
Runs / Attempts
    ↓
Artifacts
    ↓
Independent QA / Review
    ↓
Rework or Acceptance
    ↓
Integration
    ↓
Knowledge / Learning
```

The user should be able to close the browser and leave.

The organization continues.

The user returns.

Everything that happened remains visible.

---

# 4. CURRENT SYSTEM BASELINE — VERIFY, DO NOT ASSUME

The most recent audit found significant real engineering already exists.

The main repository was observed at:

```text
/home/ash/empirium-studio
```

with substantial implementation including:

```text
scripts/production-reconciler.ts
src/server/director-service.ts
scripts/product-worker-executor.mjs
src/server/workforce-postgres.ts
src/server/employee-store.ts
src/server/employee-identity-adapter.ts
AI_WORKFORCE_BUILD/controller/
```

The system had already demonstrated:

* a deterministic control plane;
* real worker execution;
* isolated worktrees;
* failure-recovery commissioning;
* QA/rework mechanics;
* hundreds of tests;
* a large requirements ledger.

The audit also found major unresolved problems, including:

* PostgreSQL authority/connectivity not properly proven;
* a large amount of unverified requirements;
* large quantities of divergent worktree implementation;
* high worker timeout/no-progress frequency;
* a failing Department CRUD E2E path;
* a release gate that remained NOT_READY.

The audit observed many real worker attempts, but a large share timed out or made no useful progress, which means task sizing, worker routing and result handling require engineering rather than simple retrying. 

Before changing anything, re-observe reality.

Do not rely on September 19 audit numbers after execution begins.

---

# 5. FIRST ACTION: PROTECT ALL EXISTING WORK

Before broad implementation:

1. Capture repository status.
2. Capture all branches.
3. Capture all worktrees.
4. Capture all uncommitted files.
5. Capture active CAO sessions.
6. Capture active workers.
7. Capture current PostgreSQL state.
8. Capture systemd state.
9. Capture current release gate.
10. Capture existing requirements/evidence state.

Do not perform:

```bash
git reset --hard
git clean -fd
```

against unknown work.

Do not delete old worktrees because there are many of them.

The audit found over one hundred worktrees and substantial implementation divergence.

Every relevant worktree must be classified:

```text
UNIQUE_GOOD_WORK
SUPERSEDED
BROKEN
REDUNDANT
PARTIALLY_USEFUL
ARCHITECTURALLY_INCOMPATIBLE
UNREVIEWED
UNKNOWN
```

Only remove a worktree after:

* its unique work is understood;
* accepted code has been integrated;
* rejected code is recorded as rejected;
* no unique uncommitted data remains;
* evidence/provenance is retained.

---

# 6. DURABLE ARCHITECTURE — THE LLM IS NOT THE SUPERVISOR

The mandatory control hierarchy is:

```text
systemd / host process supervision
              │
              ▼
deterministic continuation supervisor
              │
              ▼
production reconciler
              │
              ▼
PostgreSQL durable operational state
              │
              ▼
runnable WorkItem / action debt
              │
              ▼
CAO session execution layer
              │
       ┌──────┴───────────┐
       ▼                  ▼
GPT-5.6 Luna        GPT-5.6 Sol
operations          architecture/review
       │
       ▼
FreeLLMAPI implementation workers
       │
       ▼
deterministic tests
       │
       ▼
Sol independent QA
       │
       ▼
ACCEPT or REWORK
       │
       ▼
integration
       │
       ▼
next runnable work
```

The following concepts must never become equivalent:

```text
Project ≠ chat
Employee ≠ model process
Employee ≠ CAO terminal
Task ≠ prompt
Run ≠ Task
Department ≠ Crew
Department ≠ folder
QA ≠ worker self-test
Completion ≠ no active worker
Completion ≠ CAO idle
Completion ≠ passing tests
Completion ≠ screenshot
```

---

# 7. CAO — EXACT ROLE

The audited CAO installation is based on:

```text
cli-agent-orchestrator v2.5.0
/home/ash/work/cli-agent-orchestrator
```

with an Empirium fork.

CAO is a **session-management and agent-transport layer**.

It owns disposable execution mechanics such as:

* tmux sessions;
* terminals;
* assigning agents;
* messaging;
* receiving results;
* lifecycle status;
* killing or cleaning up terminals.

CAO does **not** own:

* the authoritative Project;
* WorkItem state;
* completion;
* persistent employee identity;
* final QA state;
* release state.

CAO's SQLite state must never become the only copy of project information.

PostgreSQL remains authoritative.

---

# 8. CAO ASYNCHRONOUS EXECUTION MODEL

The audited blocking Director→Worker `handoff` path timed out.

Therefore do not design the production pipeline around a Director waiting synchronously for a worker for ten minutes.

Use:

```text
reconciler creates Attempt
        ↓
persist Attempt
        ↓
CAO launch/assign worker asynchronously
        ↓
store CAO session + terminal IDs in Attempt
        ↓
controller returns to reconciliation loop
        ↓
monitor terminal
        ↓
collect worker result
        ↓
validate result
        ↓
advance state
```

Prefer:

```text
assign
```

for substantial implementation.

Use blocking handoff only for genuinely short operations.

---

# 9. CAO PROFILE ARCHITECTURE

Establish or verify the following logical profiles:

### `empirium-director`

Model route:

```text
GPT-5.6 Luna
Codex/ChatGPT subscription
```

Purpose:

* reconstruct durable project context;
* manage workstreams;
* prepare bounded worker contracts;
* diagnose repeated failures;
* decide next executable work;
* request Sol planning/review;
* monitor project coherence.

The Director may orchestrate workers.

### `empirium-worker`

Model route:

```text
FreeLLMAPI
```

Purpose:

* bounded implementation only.

It does not spawn other workers.

It does not approve itself.

### `empirium-reviewer`

Model route:

```text
GPT-5.6 Sol
Codex/ChatGPT subscription
```

Purpose:

* independent code review;
* QA;
* architecture verification;
* visual review;
* adversarial release review.

It does not edit source being reviewed.

### Optional `empirium-planner`

Also Sol.

Use only where separating architecture planning from final QA produces cleaner independence.

---

# 10. EXACT MODEL LAW — ONLY THREE INTELLIGENCE LANES

All earlier references to:

* Opus;
* Sonnet;
* Astra;
* paid OpenAI;
* paid Anthropic;
* OpenRouter;
* OpenRouter free routing;

are superseded for this build.

Only these three lanes are authorized.

## LANE 1 — FREELLMAPI

Does the bulk implementation.

Expected workload:

* TypeScript;
* React;
* Node;
* CSS;
* database code;
* tests;
* migration code;
* refactors;
* state adapters;
* API code;
* PixiJS/canvas implementation;
* asset processing scripts;
* component implementation;
* ordinary bug fixes.

Workers are cheap/disposable.

Tasks must therefore be explicit and bounded.

## LANE 2 — GPT-5.6 LUNA

Acts as stable intelligent operational management.

Luna should:

* reconstruct current state;
* manage execution;
* split tasks;
* inspect failure patterns;
* prepare worker briefs;
* maintain dependencies;
* detect stalls;
* decide free-worker rerouting;
* prepare Sol review packets;
* maintain forward progress.

Luna is **not** the durable supervisor.

Luna is **not** the normal coder.

## LANE 3 — GPT-5.6 SOL

Use Sol for the work whose quality determines whether the whole programme succeeds:

* architecture;
* future planning;
* difficult diagnosis;
* requirement reconciliation;
* code review;
* QA;
* security review;
* migration review;
* visual QA;
* UX review;
* state-authority review;
* final acceptance challenge;
* release review.

Sol is not the mass coding workforce.

---

# 11. OPENROUTER MUST BE TECHNICALLY IMPOSSIBLE

OpenRouter is prohibited.

This supersedes every old document that allowed free OpenRouter models.

Search:

```text
.env
systemd Environment=
Hermes configuration
FreeLLMAPI configuration
provider maps
fallback arrays
model aliases
CAO profiles
shell profiles
database configuration
worker executor
reviewer executor
old scripts
auto routing
```

for:

```text
openrouter
openrouter.ai
OPENROUTER_API_KEY
openrouter/free
```

Do not reveal credentials.

The existence of an old credential is not permission to delete unrelated secrets, but build processes must not inherit or use it.

Implement a deterministic post-resolution guard equivalent to:

```ts
if (resolvedProvider === "openrouter") {
  throw new ProviderPolicyViolation();
}
```

Add tests that attempt:

* explicit OpenRouter;
* alias resolving to OpenRouter;
* fallback resolving to OpenRouter;
* FreeLLMAPI model backed by OpenRouter;
* stale employee configuration using OpenRouter.

All must fail **before inference**.

---

# 12. $0 NEW PAY-AS-YOU-GO INFERENCE

Allowed:

```text
FreeLLMAPI route verified zero-cost
Luna via existing subscription
Sol via existing subscription
```

Forbidden:

```text
OpenAI API
Anthropic API
OpenRouter
paid FreeLLMAPI upstream
trial credits
prepaid balances
unknown billing routes
emergency paid fallback
paid image generation
paid vision API
paid embeddings
```

For every invocation record:

```text
invocation_id
timestamp
project_id
task_id
run_id
requested_model
effective_model
provider
route_class
auth_class
cost_class
actual_cost if known
tokens if known
result
```

Allowed cost classes:

```text
FREE_VERIFIED
SUBSCRIPTION_VERIFIED
```

Non-dispatchable:

```text
PAID
UNKNOWN_COST
TRIAL
SUSPECTED_FALLBACK
```

If an invocation unexpectedly reports spend greater than zero:

1. terminate that route;
2. record `BILLING_POLICY_VIOLATION`;
3. preserve evidence;
4. prevent retries through that route;
5. continue through allowed routes only.

---

# 13. FREELLMAPI MUST BECOME A MEASURED WORKFORCE

Do not treat FreeLLMAPI as one model.

Enumerate available models.

For each maintain:

```text
route/model ID
provider
effective model
coding capability
tool reliability
context
structured-output reliability
image capability
median latency
timeout rate
no-progress rate
test-pass rate
first-review acceptance rate
provider failure rate
quota
privacy classification
cooldown
```

Create or update:

```text
MODEL_MATRIX.json
```

Use real task outcomes to improve routing.

The previous audit showed that repeated identical retries waste capacity.

Therefore:

* NO_PROGRESS twice → Luna rewrites/splits task.
* TIMEOUT twice → investigate task size or execution route.
* repeated provider error → open circuit and use another allowed free route.
* repeated bad implementation → use Sol diagnosis before another identical attempt.

---

# 14. POSTGRESQL MUST BE THE OPERATIONAL SOURCE OF TRUTH

Resolve the current PostgreSQL ambiguity early.

Determine:

* which PostgreSQL cluster owns AI Staff Force;
* database;
* schema;
* role;
* auth mechanism;
* migration version;
* connection string;
* service dependency.

Never print passwords.

The final operational model must persist:

```text
Organization
Department
Employee
EmployeeConfigVersion
Project
Requirement
Task / WorkItem
Dependency
Run / Attempt
Lease
Review
ReviewDefect
Evidence
Approval
Event
KnowledgeItem
LearningProposal
ProviderState
ModelUsage
AssetRecord
OfficeLayout
ReleaseState
```

JSON files may be:

* static definitions;
* exports;
* migration compatibility;
* caches.

They may not compete with PostgreSQL for operational authority.

---

# 15. ASSET INGESTION IS A BLOCKING BUILD PHASE

This point is now explicitly strengthened.

The user has already invested significant time producing assets.

Do **not** behave as though the art direction is missing.

Before creating or replacing **any** visual system, recursively inspect:

```bash
"/home/ash/Desktop/AI Taskforce"
```

and all relevant existing Empirium Studio asset directories.

Create:

```text
AI_WORKFORCE_BUILD/source/INPUT_INVENTORY.json
AI_WORKFORCE_BUILD/source/INPUT_INVENTORY.md
AI_WORKFORCE_BUILD/ASSET_MANIFEST.json
AI_WORKFORCE_BUILD/ASSET_MANIFEST.md
AI_WORKFORCE_BUILD/ASSET_USE_MAP.json
```

For every visual file record:

```text
asset_id
relative path
absolute source path
sha256
file type
pixel dimensions
alpha/transparency
size
visual category
subject
perspective
likely department
reference vs runtime candidate
conversion needed
duplicate group
provenance
production suitability
planned use
derived files
notes
```

Do not alter originals.

---

# 16. REQUIRED ASSET CATEGORIES

The inventory must actively look for:

```text
organization UI references
department cockpit UI references
worker detail UI references
office shells
office floor/wall modules
department environment concepts
research offices
mission-control rooms
software offices
security rooms
sales floors
mail rooms
social media rooms
zen/cyberpunk environments
furniture sheets
desk sheets
chairs
computers
monitors
server racks
storage
plants
planning boards
technology workshop assets
character turnarounds
character component breakdowns
character expressions
walking keyframes
work poses
error/frustration poses
attention poses
status symbols
floating indicators
nameplates
handoff indicators
banners
alerts
ROM/disc research materials
```

An asset existing in this tree is a candidate to be reused or converted.

Do not regenerate it simply because a worker did not look for it.

---

# 17. THE TWO UI REFERENCES ARE MANDATORY PRODUCT CONTRACTS

Two supplied images define the primary desktop product composition.

Treat them as:

```text
UI-REF-ORG-001
UI-REF-DEPT-001
```

They are **not loose inspiration**.

They define:

* information hierarchy;
* panel density;
* navigation style;
* card design;
* office prominence;
* visual polish;
* dark navy design language;
* operational data visibility.

Do not copy their fake sample metrics.

Do reproduce their product structure.

---

# 18. UI-REF-ORG-001 — ORGANIZATION OVERVIEW CONTRACT

The organization screen must closely reproduce the **functional composition and information density** of the first supplied UI.

At desktop width, the screen should contain:

## Global top chrome

The upper application bar contains:

* Empirium Studio identity;
* "AI Organization" context;
* primary organization navigation;
* global search;
* user/profile controls.

Primary navigation should expose logical areas comparable to:

```text
Overview
Departments
Activity
Knowledge
Models & Cost
```

These may map into the broader global navigation architecture.

## Page title

Display:

```text
AI Organization
```

with a concise descriptive sentence explaining that this view shows departments, employees and operating state at a glance.

## Overall system indicator

Show current platform health truthfully.

Examples:

```text
All Systems Operational
Degraded
Attention Required
Offline Component
```

Status derives from real services/state.

## Summary metric row

The visual reference shows six highly visible summary cards.

The finished screen must support equivalent metrics:

### Active Employees

Definition:

Permanent employees currently executing a live Run, or otherwise in a canonical active operational state.

Configured-but-offline employees are not counted as active.

### Departments Online

Show:

```text
online / total
```

Department online semantics must be documented.

### Model/API Spend Today

Show only actual recorded inference spend.

During this build it should normally remain:

```text
$0.00 pay-as-you-go
```

where appropriate.

Subscription usage must not be misrepresented as $0 API usage; display subscription classification separately where useful.

### Active Projects

All nonterminal durable projects according to the documented project-state model.

### Pending Improvements

Count LearningProposals in:

```text
PROPOSED
REVIEWING
APPROVAL_REQUIRED
```

as appropriate.

### Organization Health

A health percentage may be displayed only after a deterministic formula exists.

Create and document a formula using meaningful components such as:

* required service availability;
* department operational state;
* stuck-work ratio;
* unresolved severity-weighted defects/blockers;
* recent execution success;
* recent QA outcomes.

Expose the calculation/tooltip.

If insufficient information exists:

```text
Health unavailable
```

is preferable to fabricated 96%.

---

# 19. ORGANIZATION DEPARTMENT GRID

The dominant area is a rich responsive department-card grid.

Each real Department card must show:

```text
department identity
department name
purpose / one-line mission
derived status
distinct visual accent
miniature department office
visible staff representation
employee count
active project count
real usage/cost indicator
real QA indicator
navigation affordance
```

The reference uses large miniature office illustrations.

Preserve this.

Do not replace the cards with tiny plain list rows.

At typical 1536px desktop width, aim for approximately four cards across where layout allows.

Tablet:

approximately two.

Narrow/mobile:

one.

The miniature office is a visual signature of the product.

---

# 20. MINIATURE OFFICES ON ORGANIZATION CARDS

Each department's card should visually preview its office.

Do not run seven independent full-resolution 60fps simulations.

Acceptable approaches:

* static snapshot of current scene updated on material state change;
* throttled mini renderer;
* low-FPS scene while visible;
* cached composition plus small state overlays.

Mini-office state must still correspond to actual department state.

If a department contains five employees, do not show ten imaginary permanent employees unless temporary workers are intentionally represented and labelled.

---

# 21. "NEW DEPARTMENT" CARD

The grid includes a dedicated:

```text
+ New Department
```

tile.

It must open a real Department creation workflow.

Creating a department must persist:

* Department record;
* name;
* purpose;
* policies;
* visual theme;
* office layout;
* initial employees if configured.

Reloading must retain it.

This is directly relevant to the currently failing Department CRUD E2E path.

Fix the underlying persistence/state problem rather than hiding the feature.

---

# 22. ORGANIZATION ACTIVITY PANEL

Below the department grid, provide a live organization activity panel equivalent to the mockup.

Do not stream every low-level tool call.

Surface meaningful events such as:

```text
Project created
Task assigned
Task completed
QA rejected
QA approved
Employee started work
Employee crashed
Provider rate-limited
Approval requested
Approval granted
Handoff occurred
Learning proposal created
Improvement activated
```

Each event links to its underlying object where sensible.

---

# 23. ORGANIZATION MODEL / SPEND PANEL

Provide a visual breakdown comparable to the reference chart.

Possible dimensions:

```text
by department
by model
by route class
```

Display only factual telemetry.

Differentiate:

```text
Free API
Subscription
Unknown
Paid policy violation
```

Never invent an API-equivalent dollar cost for subscription requests and present it as actual spend.

---

# 24. ORGANIZATION RECENT IMPROVEMENTS PANEL

Display real LearningProposals and activated improvements.

Examples:

```text
prompt revision
model-routing improvement
new skill
workflow improvement
tool-policy improvement
UI/process improvement
```

Each should have:

```text
status
department
timestamp
evidence
version/change
```

---

# 25. UI-REF-DEPT-001 — DEPARTMENT COCKPIT CONTRACT

The second supplied UI is the primary product reference for a single Department.

The desktop experience should feel like a **working department command centre**, not a generic admin page.

The reference is dense but readable.

Preserve that principle.

---

# 26. GLOBAL LEFT NAVIGATION

The desktop Department view includes a persistent left navigation.

Equivalent functionality should expose:

```text
Home / Organization
AI Organization
Departments
    Personal Software
    future departments
    Add Department

Projects
Tasks
Conductor
Agents
Knowledge
MCP & Tools
Models & Costs
Schedules
Learning
QA & Review
Analytics
Settings
```

Use existing Hermes Studio functionality where appropriate rather than rebuilding working systems.

The sidebar should make it obvious which Department is active.

---

# 27. DEPARTMENT HEADER

The Personal Software Department header must communicate:

```text
department icon
Personal Software Department
purpose
operational status
optional motto
alerts
New Project
Ask Department
```

Purpose:

> Build, maintain and improve the user's personal software systems.

`Ask Department` should open or focus interaction with the Department Director using actual Department context.

It is not a decorative button.

---

# 28. DEPARTMENT TAB BAR

Required logical subareas:

```text
Overview
Projects
Tasks
Agents
QA
Knowledge
Learning
History
Models & Cost
Settings
```

These may be routes or internal subviews.

Do not leave these as dead tabs.

---

# 29. DEPARTMENT OVERVIEW — DESKTOP COMPOSITION

The primary visual structure closely follows the supplied reference.

### Centre/upper main area

Large living office.

This is the strongest visual element.

### Right rail

Department Status + Current Activity.

### Immediately below office

Three primary panels:

```text
Active Projects
Upcoming Work
Completed Recently
```

### Lower information row

Panels equivalent to:

```text
Department QA
Knowledge
Learning & Improvements
Models & Cost
```

All should contain real data.

---

# 30. DEPARTMENT STATUS PANEL

Show meaningful real-time metrics such as:

```text
Active Projects
Active Tasks
Employees Online
Today's API Spend
Current-month API Spend
Success / QA Rate
```

Definitions must be deterministic.

For example:

### Employees Online

Count permanent Department employees whose runtime presence is currently live/healthy according to canonical liveness rules.

### QA success

Define population and time range.

For example:

```text
first-pass approvals /
reviewed tasks
during trailing 30 days
```

Do not show an unexplained "96%".

---

# 31. CURRENT ACTIVITY RAIL

Show timestamped Department events.

Use the same canonical event stream that drives office state.

This invariant is mandatory:

```text
Activity rail says employee CRASHED
        ↓
office cannot simultaneously show employee happily CODING
```

and:

```text
Activity rail says RATE_LIMITED
        ↓
office shows rate-limit/wait state
```

A single canonical runtime-state adapter must feed both.

---

# 32. ACTIVE PROJECTS PANEL

Each project card contains:

```text
title
short description
status
progress
assigned employees
task summary
blocker/attention indicator if relevant
```

Project progress must have a documented formula.

Recommended default:

```text
accepted non-cancelled leaf tasks /
all currently-required non-cancelled leaf tasks
```

If task weighting exists, use explicitly stored weights.

Never manually hard-code a progress percentage.

Click opens full Project detail.

---

# 33. UPCOMING WORK PANEL

Display genuinely runnable or dependency-pending work.

Do not list vague roadmap ideas as though workers are queued to execute them.

Each item should expose:

```text
title
priority
dependency state
intended assignee/role
```

---

# 34. COMPLETED RECENTLY PANEL

Show true completed tasks/projects with:

```text
name
timestamp
project
employee
evidence link where useful
```

---

# 35. DEPARTMENT QA PANEL

Match the information density of the mockup.

Support:

```text
quality metric
reviewed-task count
first-pass rate
open issues
recent reviews
```

Each review is backed by a Review record.

Open issues link to exact defects.

Do not create QA statistics from fake seeded history.

---

# 36. DEPARTMENT KNOWLEDGE PANEL

Display actual scoped knowledge.

Examples:

```text
Architecture
Standards
Decisions
Lessons Learned
Research
Project Knowledge
```

If Obsidian integration exists and remains appropriate, expose it cleanly.

Operational state does not live solely in Obsidian.

---

# 37. LEARNING & IMPROVEMENTS PANEL

Display:

```text
employee performance evidence
pending LearningProposals
recently activated improvements
rolled-back improvements
```

Worker/model performance should be derived from real Runs and Reviews.

Do not rank agents based on tiny samples without showing sample size.

---

# 38. MODELS & COST PANEL

Display:

```text
requested model
effective model if known
provider
Free API / Subscription classification
tokens where known
actual reported cost
task/run links
```

The supplied reference shows monthly spend and model percentages.

Implement equivalent truthful telemetry.

Do not hard-code those sample values.

---

# 39. THE CANONICAL VISIBLE STAFF

Personal Software must begin with persistent organizational identities equivalent to:

### Director

Responsibilities:

* intake;
* project interpretation;
* decomposition;
* dependency management;
* orchestration;
* escalation;
* final summarization.

### Research Architect

Responsibilities:

* repo investigation;
* research;
* architecture;
* implementation strategy;
* risk;
* test strategy.

### Developer / Implementation Engineer

Responsibilities:

* bounded implementation;
* tests;
* worktree discipline;
* structured handoff.

### QA Engineer

Responsibilities:

* independent validation;
* browser testing;
* regression;
* reproduction;
* defect creation.

### Learning Analyst

Responsibilities:

* analyze outcomes;
* capture lessons;
* identify model/worker performance;
* propose prompt/skill/routing improvements.

These are **persistent employee identities**.

They are not the temporary FreeLLMAPI processes used to build Empirium Studio.

---

# 40. EMPLOYEE DOSSIER

Clicking any permanent employee opens a rich dossier.

The dossier must include:

```text
name
skin/avatar
department
role
responsibilities
current status
status reason
current project
current task
current Run
requested model
effective model
provider
free/subscription class
token usage if known
cost if known
start time
elapsed time
latest event
prompt/SOUL version
personality
communication style
skills
tools
MCP permissions
model policy
knowledge scope
memory scope
permissions
review history
task history
project history
error history
performance history
configuration versions
```

Relevant actions may include:

```text
open current task
open project
open Run/log
open linked chat/session
assign work
pause if semantically supported
retry/requeue where safe
request attention
edit versioned employee config
```

No action may merely alter UI state while backend remains unchanged.

---

# 41. EMPLOYEE CONFIGURATION MUST BE VERSIONED

Editable employee configuration includes, where appropriate:

```text
name
role
responsibilities
routing description
personality
communication style
SOUL/system prompt
skills
tools
MCPs
model policy
fallback policy
knowledge scope
memory scope
permissions
approval rules
skin
workstation
```

Each modification creates a version containing:

```text
version
author
timestamp
diff
reason
review status
active/inactive
```

Allow rollback.

Employee identity remains the same across model/profile changes.

---

# 42. USE THE BLUE-AND-YELLOW BOT AS THE CANONICAL WORKER

The generic white/purple robots in the Department UI mockup are **not** the final character design.

The final Personal Software office should use the supplied blue-and-yellow helper-bot character assets.

Do not casually redesign them.

Find the canonical source sheets in the asset library.

The current design language visible in the supplied references includes:

* compact rounded yellow head;
* large circular expressive eyes;
* simple mouth/expression system;
* grey top-cap/nub;
* blue torso and limb armour;
* exposed grey joint segments;
* yellow robotic hands;
* compact robotic blue footwear;
* simple, readable small-helper proportions;
* expressive body language;
* slightly clumsy, friendly personality.

Use the actual supplied source sheet as authority rather than recreating these details from this prose.

---

# 43. CHARACTER DESIGN MUST BE A REUSABLE RIG, NOT A STATIC PNG

The supplied character sheets include turnarounds/component breakdowns.

Exploit that.

Preferred implementation is a reusable layered 2D puppet/rig or sprite-rig system.

Potential layers:

```text
head
face/eyes
mouth/expression
top cap
torso
upper arm L/R
forearm L/R
hand L/R
upper leg L/R
lower leg L/R
foot L/R
held object
role accessory
shadow
```

Define anchor/pivot points.

This allows:

* walking;
* bobbing;
* typing;
* looking;
* holding objects;
* worrying;
* waving;
* sitting;
* handoffs;

without needing hundreds of separately generated full-body raster frames.

If the existing assets contain sufficient sprite animation, use those instead.

The architecture should choose the most faithful and performant production path after asset inspection.

---

# 44. SHARED RIG, MANY PERSONALITIES

Do not write custom animation code for each employee.

Employees share a base rig/state system.

Individuality can come from:

* names;
* status/nameplates;
* role accessories;
* subtle skin variations;
* expression tendencies;
* desk/workstation;
* personality;
* small props.

The initial release does not require dozens of completely unique character rigs.

---

# 45. LIVING OFFICE IS NOT A PICTURE

The Department office shown in the UI reference is a **runtime visualization**.

A large static office background is acceptable as a scene layer.

Static worker characters are not.

The office must reflect current operational reality.

---

# 46. OFFICE RENDERER

Select a lightweight 2D solution after benchmarking the existing frontend.

Preferred options:

```text
PixiJS
Canvas
SVG/DOM hybrid
```

Do not adopt a heavyweight 3D engine.

A suitable architecture could be:

```text
React application
      │
      ▼
OfficeViewport component
      │
      ▼
2D renderer
      │
      ├── Environment/background layers
      ├── Furniture/depth layers
      ├── Employee actors
      ├── indicators
      └── interaction layer
```

---

# 47. OFFICE LAYOUT DATA MODEL

Create a reusable Department OfficeLayout structure containing concepts such as:

```text
layout_id
department_id
scene_asset
viewport
walkable polygons/grid
obstacles
z-depth zones
home stations
role stations
shared stations
furniture
decor
interaction hotspots
spawn points
attention point
meeting/handoff point
camera config
theme
```

The exact schema should be reviewed by Sol.

---

# 48. USE EXISTING OFFICE ASSETS

The asset package contains empty office shells and themed environments.

Examples represented by the supplied material include:

* premium navy isometric offices;
* research department shell;
* software environments;
* mission-control spaces;
* security environments;
* technical workshop assets;
* modern office furniture.

Do not draw a generic rectangular office from scratch unless no usable source exists.

---

# 49. MODULAR FURNITURE

The supplied furniture sheet demonstrates the required isometric furniture language.

Inventory and reuse equivalent assets including:

```text
small desk
large desk
corner desk
standing desk
manager desk
meeting table
office chair
stool
bench
side table
monitors
laptops
server equipment
storage
shelves
plants
planning surfaces
```

Keep perspective and scale consistent.

Furniture may either:

* exist as scene layers;
* be baked into a department background where interaction does not require dynamic rearrangement;
* or be a hybrid.

Do not overengineer a Sims-style interior editor unless the requirement ledger explicitly requires one.

---

# 50. OFFICE ROLE STATIONS

Personal Software should have meaningful stations.

Examples:

```text
Director → manager/oversight desk
Research 
...[TRUNCATED 30925 chars]...
ect it.

Do not keep paying free quota and VPS time to an agent doing nothing.

---

# 98. CLEAN EXIT ≠ COMPLETE

If any of these exits 0:

```text
Luna
Sol
Free worker
CAO terminal
reviewer
Director
```

inspect project state.

If incomplete:

continue.

Only project state controls project lifecycle.

---

# 99. SOURCE REQUIREMENTS MUST BE RE-EXTRACTED

Because previous build attempts suffered scope loss, retain the existing dual-pass requirement process.

From every substantive text and visual source:

### Pass A

Extract atomic requirements.

### Pass B

Fresh context; reread original sources without reading Pass A first.

### Reconciliation

Use Sol to compare:

* missing requirements;
* overcompressed requirements;
* duplicates;
* contradictions;
* incorrectly optional requirements;
* superseded requirements;
* visual requirements omitted by text extraction.

No substantive source region remains unmapped without explanation.

---

# 100. VISUAL SOURCES CREATE REQUIREMENTS

The new screenshots specifically create mandatory requirements.

Examples:

From organization reference:

```text
department cards are visually rich
mini offices visible
top-level metrics visible
activity visible
usage/cost visible
recent improvements visible
```

From Department reference:

```text
large living office dominates overview
persistent navigation exists
five core employee identities visible
right activity/status rail exists
projects/upcoming/completed visible
QA/knowledge/learning/model-cost panels visible
```

From character sheets:

```text
blue/yellow canonical visual identity
consistent proportions
expressions
work poses
shared components
```

From office references:

```text
premium isometric environment
navy architecture
warm accent lighting
modular interior language
department-specific environmental identity
```

From furniture references:

```text
perspective consistency
modular desk/chair/component library
```

---

# 101. EXISTING 710-REQUIREMENT LEDGER

Do not assume 710 is sacred.

Reconcile it.

Requirements may be:

```text
valid
duplicate
superseded by explicit current user decision
overcompressed
missing
```

However, never reduce the count merely because release would become easier.

Every removed requirement needs a reason and source reference.

Every newly discovered requirement must be added.

---

# 102. IMPLEMENTATION WORKSTREAMS

Luna should manage bounded workstreams roughly equivalent to:

```text
WS-01 Requirements / Architecture
WS-02 Runtime / Persistence / PostgreSQL
WS-03 CAO / Model Routing / Execution
WS-04 Organization / Department UI
WS-05 Projects / Tasks / QA UI
WS-06 Living 2D Office
WS-07 Technical Art / Asset Pipeline
WS-08 Employees / Dossiers / Configuration
WS-09 Knowledge / Learning
WS-10 Telemetry / Models / Cost
WS-11 Security / Permissions
WS-12 QA / Browser / Accessibility / Performance
WS-13 Integration / Release
```

Do not start all simultaneously.

Respect dependency boundaries and VPS capacity.

---

# 103. ARCHITECTURE FREEZE POINTS

Before many parallel workers touch a subsystem, Sol should review and freeze only necessary shared contracts, including:

```text
Organization identity
Department identity
Employee identity
Project/Task/Run identity
canonical statuses
event taxonomy
review schema
evidence schema
model telemetry
API shapes
office state adapter
asset manifest format
permissions/capabilities
```

If a worker thinks a frozen contract is wrong:

raise:

```text
ARCHITECTURE_CHANGE_REQUEST
```

Do not silently fork the architecture.

---

# 104. IMPLEMENTATION ORDER

Proceed in this order unless verified dependencies dictate a better equivalent.

### Phase 0 — protect reality

Preserve Git/worktrees/process state.

### Phase 1 — source + asset inventory

Inventory every input file.

### Phase 2 — current-state reconciliation

Compare audit snapshot with current live reality.

### Phase 3 — provider policy

Prove three model lanes and block OpenRouter.

### Phase 4 — PostgreSQL

Repair durable operational authority.

### Phase 5 — CAO integration

Prove async worker lifecycle.

### Phase 6 — worktree consolidation

Integrate useful existing implementation.

### Phase 7 — requirement reconciliation

Dual extraction + Sol reconciliation.

### Phase 8 — architecture freeze

Domain/state/event/contracts.

### Phase 9 — core runtime

Organization/Department/Employee/Project/Task/Run/Review.

### Phase 10 — organization UI

Implement UI-REF-ORG-001 contract.

### Phase 11 — Department UI

Implement UI-REF-DEPT-001 contract.

### Phase 12 — remaining product pages

Projects, Tasks, Agents, QA, Knowledge, Learning, History, Models & Cost, Settings.

### Phase 13 — asset production

Character rig, office environments, furniture.

### Phase 14 — living office

State adapter, movement, interactions.

### Phase 15 — employee config/history

Persistent dossier and versioning.

### Phase 16 — learning/knowledge

Real data + proposals.

### Phase 17 — telemetry/observability

Model, Run, cost, provider health.

### Phase 18 — security/accessibility/performance

Harden.

### Phase 19 — full regression

All suites.

### Phase 20 — visual QA

All milestone viewports.

### Phase 21 — resilience

Failure injection.

### Phase 22 — autonomous commissioning

Prove real user workflow.

### Phase 23 — burn-in

Sustained operation.

### Phase 24 — Sol red team

Challenge everything.

### Phase 25 — source reread

Freshly compare against original sources/assets.

### Phase 26 — final deterministic release gate

If fail → create work → continue.

---

# 105. AUTONOMOUS COMMISSIONING TEST

Use finished Empirium Studio itself to submit a genuine isolated software task.

Required observed sequence:

```text
User creates project
        ↓
durable Project written
        ↓
Director receives it
        ↓
requirements/acceptance interpreted
        ↓
Tasks created
        ↓
dependencies defined
        ↓
FreeLLMAPI worker executes
        ↓
Run stored
        ↓
code produced
        ↓
tests executed
        ↓
Sol review
        ↓
intentional rejection at least once
        ↓
rework
        ↓
approval
        ↓
integration
        ↓
Project completion
```

During this test:

* close the browser;
* kill one worker;
* cause one review rejection;
* restart one orchestration component;
* verify work continues.

The office should visibly track these states.

---

# 106. MULTI-CYCLE BURN-IN

After one successful commissioning run, perform approximately 20 meaningful autonomous cycles or equivalent comprehensive sustained workload.

Include a mix of:

* normal success;
* rework;
* worker death;
* provider wait;
* timeout;
* dependencies;
* approvals;
* browser closure;
* application restart;
* CAO restart;
* multiple projects;
* learning proposal;
* Sol review;
* office state transitions.

Burn-in passes only if:

```text
no unexplained stuck WorkItems
no unexplained duplicate Projects
no lost history
no paid inference
no OpenRouter request
no unresolved data mismatch
no persistent runaway process/session leakage
```

---

# 107. FINAL SOL RED TEAM

Give Sol fresh context, not the build team's accumulated conversational assumptions.

Provide:

```text
original source index
V5 prompt
requirements ledger
release SHA
architecture
database schema
test results
visual screenshots
animation evidence
resilience evidence
model usage
billing evidence
security results
asset inventory
release gate
```

Ask Sol to deliberately search for:

```text
scope compression
fake implementation
documentation substituted for implementation
static UI substituted for living office
fake metrics
state-authority collisions
runtime Employee mistaken for persistent Employee
Task/Run collapse
QA bypass
self-approval
stale evidence
provider leakage
OpenRouter leakage
hidden paid routing
restart data loss
CAO state treated as authority
dead buttons
mock panels
visual underdelivery
asset library ignored
worktree implementation lost
security weaknesses
accessibility omissions
performance collapse
incorrect release assumptions
```

Every valid blocking finding becomes work.

---

# 108. FINAL VISUAL SOURCE RECONCILIATION

Before release, Sol must explicitly compare the product against:

```text
UI-REF-ORG-001
UI-REF-DEPT-001
canonical blue/yellow bot sheets
office environment references
modular furniture references
status icon references
movement/expression references
```

For each state:

```text
SATISFIED
SUPERSEDED_BY_EXPLICIT_USER_CHANGE
BLOCKING_MISMATCH
```

There may be no unexplained omission.

---

# 109. RELEASE GATE

Create/maintain an executable release gate.

It must fail if any mandatory condition below fails.

### Source integrity

All authoritative sources indexed.

### Requirement coverage

No mandatory requirement unverified.

### Asset coverage

Required visual sources accounted for.

### Implementation provenance

AI-authored implementation comes from authorized FreeLLMAPI route.

### Model policy

No unauthorized provider.

### OpenRouter

No reachable execution route.

### Spend

No unauthorized pay-as-you-go inference.

### PostgreSQL

Durable authority verified.

### Domain separation

Organization/Department/Employee/Project/Task/Run/Review semantics correct.

### Tests

All mandatory suites pass.

### Runtime

Core behaviours actually exercised.

### QA

Required Sol reviews pass.

### Evidence freshness

Proof corresponds to release SHA.

### Visual quality

No Critical/High visual defect.

### Organization UI

Mandatory organization contract implemented.

### Department UI

Mandatory Department contract implemented.

### Living office

Real, moving, state-bound office.

### Characters

Canonical blue/yellow bots deployed.

### Employees

Persistent and inspectable.

### Projects/tasks

Durable and functional.

### Knowledge/learning

Functional.

### Model/cost telemetry

Truthful.

### Accessibility

Gate passes.

### Performance

Gate passes.

### Security

No unresolved Critical/High.

### Resilience

Required failure-injection tests pass.

### Supervisor/reconciler/CAO

Recovery proven.

### Autonomous commissioning

Pass.

### Burn-in

Pass.

### Source reconciliation

Pass.

### Final Sol review

Pass.

### Build/deployment identity

Verified source SHA == tested SHA == deployed SHA where applicable.

Only then:

```text
exit 0
```

---

# 110. FINAL RELEASE EVIDENCE

Produce:

```text
AI_WORKFORCE_BUILD/FINAL_RELEASE_GATE.json
AI_WORKFORCE_BUILD/FINAL_RELEASE_REPORT.md
AI_WORKFORCE_BUILD/FINAL_SOURCE_RECONCILIATION.md
AI_WORKFORCE_BUILD/BURN_IN_REPORT.md
AI_WORKFORCE_BUILD/FINAL_SOL_REVIEW.md
```

The machine-readable gate records:

```text
timestamp
release_sha
deployed_sha
database_migration
checks
blocking_failures
requirement_counts
evidence_refs
test_results
visual_results
resilience_results
security_results
model_policy_results
```

Humans/models may read this file.

They may not edit it into success.

---

# 111. HUMAN BLOCKER STANDARD

Interrupt the user only where the action genuinely requires them.

Valid examples:

* interactive subscription reauthentication;
* genuinely absent required user file;
* unavoidable CAPTCHA;
* sudo credential unavailable and essential;
* irreversible user-data destruction needing approval;
* material product decision with two incompatible options and no safe reversible default.

Not valid:

* test failed;
* worker failed;
* worker timed out;
* CAO terminal disappeared;
* database bug;
* merge conflict;
* provider rate limit;
* FreeLLMAPI model poor;
* Sol rejected code;
* UI looks wrong;
* animation needs fixing;
* current implementation incomplete;
* old worktrees are complicated.

Those are engineering work.

---

# 112. HUMAN BLOCKER MESSAGE FORMAT

Only when unavoidable:

```text
BLOCKER:
exact issue

WHY HUMAN REQUIRED:
why no autonomous authorized solution exists

ATTEMPTS:
what was tried

EVIDENCE:
logs/files/errors

MINIMUM USER ACTION:
smallest required action

WORK CONTINUING:
other work still progressing
```

Do not stop unrelated work.

---

# 113. DO NOT FAKE PROGRESS

Do not fabricate:

```text
employees working
projects
spend
health
QA
model usage
progress
activity
completion
provider identity
cost
review
```

Demo fixtures may exist only in isolated test/dev contexts and must be unmistakably fixtures.

Production UI shows real state.

---

# 114. DO NOT REPLACE THE VISUAL REFERENCES WITH A GENERIC ADMIN DASHBOARD

This is extremely important.

A technically clean CRUD dashboard does not satisfy the UI requirement.

The finished experience must retain:

* large visual department cards;
* mini offices;
* high information density;
* organization metrics;
* activity;
* real model/cost telemetry;
* rich Department cockpit;
* dominant living office;
* persistent bot workforce;
* right-side status/activity rail;
* project/upcoming/completed panels;
* QA;
* knowledge;
* learning;
* models/cost;
* premium dark navy aesthetic.

Do not "simplify" these away.

---

# 115. DO NOT REPLACE THE BLUE/YELLOW BOTS

The Department mockup's white/purple bots are placeholders for layout only.

The final system uses the user's supplied blue-and-yellow worker design.

Do not silently substitute:

* generic emoji;
* circles with initials;
* white AI robots;
* stock robot sprites;
* Capcom-extracted Servbots.

Use the supplied original blue/yellow design.

---

# 116. ROM / TRON BONNE RESEARCH

Owned/source ROM material may remain a private R&D source for:

* movement timing;
* clumsy helper behaviour;
* social/group motion;
* urgency;
* frustration/fear;
* animation study.

It is not a release dependency.

Do not use leaked source.

Do not require ROM-extracted art in the production app.

Production character art must remain the supplied Empirium design.

---

# 117. KEEP THE USER OUT OF ROUTINE EXECUTION

Do not send an update after infrastructure repair saying:

> Ready to continue.

Continue.

Do not send:

> Shall I implement the UI now?

Implement it.

Do not send:

> Tests failed; what do you want me to do?

Diagnose and fix.

The architecture exists precisely to avoid requiring repeated `continue` messages.

---

# 118. WHAT "OVER THE LINE" MEANS

The project has crossed the line only when the user can do this:

1. Open Empirium Studio.
2. See the organization screen at the quality and density of UI-REF-ORG-001.
3. See real Departments represented by rich mini-office cards.
4. Open Personal Software.
5. See the Department cockpit at the quality and structure of UI-REF-DEPT-001.
6. See the persistent blue/yellow employees physically represented in a living office.
7. Click an employee and inspect its actual identity/config/history/state.
8. Submit a software Project.
9. Close the browser.
10. Have the Director continue.
11. Have FreeLLMAPI workers implement bounded tasks.
12. Have tasks retry when workers fail.
13. Have Sol independently review work.
14. Have rejected work automatically return for rework.
15. See those activities reflected truthfully in the office and activity feed.
16. Return later and find history intact.
17. Inspect Tasks, Runs, reviews and evidence.
18. Inspect model/provider usage.
19. See no fake operational data.
20. Restart relevant services and retain state.
21. Observe continued execution.
22. Complete a real software project.
23. Pass the deterministic release gate.

That—not a screenshot, not an architecture diagram, not 398 passing unit tests—is the finished product.

---

# 119. IMMEDIATE START PROCEDURE

After receiving this prompt:

**Do not respond with another plan.**

Begin actual execution.

Perform these actions in sequence:

1. Preserve current Git/worktree/process/database state.
2. Inventory every source and asset under `"/home/ash/Desktop/AI Taskforce"`.
3. Locate and identify the two mandatory UI references.
4. Locate canonical blue/yellow bot assets.
5. Locate office environment and furniture assets.
6. Reconcile today's live environment against the latest forensic audits.
7. Confirm authoritative CONTROL and TARGET.
8. Confirm PostgreSQL authority and repair connectivity safely.
9. Verify FreeLLMAPI route.
10. Verify Luna subscription/Codex route.
11. Verify Sol subscription/Codex route.
12. Remove/block OpenRouter from all active paths.
13. Prove $0 inference policy.
14. Verify CAO service and its Empirium fork.
15. Wire deterministic reconciler → CAO asynchronous worker lifecycle.
16. Prove one FreeLLMAPI bounded coding task end-to-end.
17. Prove one Luna Director recovery cycle.
18. Prove one Sol independent review.
19. Reconcile useful existing worktrees.
20. Repair Department CRUD persistence failure.
21. Re-run baseline tests.
22. Perform fresh requirements reconciliation including visual sources.
23. Freeze shared contracts with Sol review.
24. Activate bounded workstreams.
25. Build the complete product.
26. Run every required test and visual gate.
27. Break it deliberately.
28. Recover it.
29. Commission it.
30. Burn it in.
31. Reconcile against the original sources again.
32. Run final Sol red team.
33. Run deterministic release gate.
34. If the gate fails, create work from the failures and continue.
35. Repeat until gate exits zero.

---

# 120. FINAL BEHAVIOURAL LAW

The deterministic controller owns continuity.

PostgreSQL owns durable operational truth.

CAO owns disposable execution sessions.

Luna owns intelligent operational coordination.

FreeLLMAPI owns bulk code implementation.

Sol owns architecture, planning, QA, review and final independent challenge.

Workers do not self-approve.

Review rejection creates work.

Worker failure creates work.

Provider failure creates wait/rerouting, not completion.

Luna death causes recovery.

CAO death causes recovery.

Reconciler death causes recovery.

Browser closure changes nothing about project durability.

VPS restart must not erase project state.

No OpenRouter route is permitted.

No paid API inference is permitted.

No source asset is ignored merely because a worker failed to inventory it.

No white/purple placeholder robot replaces the blue/yellow canonical workers.

No fake metric may appear as production truth.

No static picture substitutes for the living office.

No generic admin dashboard substitutes for the two supplied UI contracts.

No visual polish claim passes without screenshots and independent review.

No backend functionality claim passes without runtime proof.

No requirement disappears because it is inconvenient.

No old completion marker outranks current evidence.

No agent may manually declare SHIPPED.

The only legitimate terminal success is:

```text
FINAL_RELEASE_GATE.exitCode = 0
```

followed by:

```text
BUILD_STATE.status = SHIPPED
```

Until that is true:

**keep building.**

**keep testing.**

**keep reviewing.**

**keep recovering.**

**keep integrating.**

**do not ask the user to type continue.**

# BEGIN THE ACTUAL BUILD NOW.

---

This is materially different from the last prompt. In particular, the **asset library is now a blocking input phase rather than a side note**, the two UI images are described as explicit contracts rather than "premium inspiration", the blue/yellow character design is locked in, and the test plan now goes down to specific Organization, Department, employee, office-state, movement, PostgreSQL, CAO, routing, accessibility, performance, security and failure-injection tests.

It also deliberately retains the best parts of your older exhaustive protocol instead of discarding them: that protocol already required dual-pass requirement extraction and visual-source requirements, so this version treats those as safeguards against anything I may still have missed in prose.  

The most important practical difference is that **Hermes is now explicitly forbidden from starting broad coding before it has inventoried the VPS assets**. That should prevent the exact failure you're worried about—free workers building generic offices, generic bots or generic UI while hundreds of already-approved assets sit unused on the VPS.
```

===== 2026-09-19 12:35 | session 20260919_123540_809340 | None =====
Perform a read-only forensic audit of the Empirium Studio workforce frontend against V5 UI-REF organization and department contracts. Identify current routes/components, implemented vs missing mandatory UI elements, and the smallest dependency-ordered implementation slices. Do not modify files. Return exact paths and evidence, concise.

===== 2026-09-19 12:35 | session 20260919_123540_03282c | None =====
Perform a read-only review of assets under /home/ash/Desktop/AI Taskforce and the generated inventory at /home/ash/empirium-studio/AI_WORKFORCE_BUILD. Focus on discoverable visual contracts/assets for UI, character rig, office scene, furniture. Identify any source screenshots corresponding to organization/department UI references, including ambiguous timestamps, and report exact source paths. Do not modify anything.

===== 2026-09-19 12:39 | session 20260919_123945_538bb3 | None =====
Audit the source asset tree for the V5 workforce visual contracts. Find exact paths for UI references if present, and summarize additional high-value character/office/furniture assets not yet named in ASSET_IDENTIFICATION.md. Report only evidence-backed findings.

===== 2026-09-19 12:57 | session 20260919_122650_1a1209 | AI Staff Force =====
@file:`.hermes/attachments/Pasted content (10.3 KB)`

--- Attached Context ---

📄 @file:`.hermes/attachments/Pasted content (10.3 KB)` (2548 tokens)
```
CONTINUATION FAILURE — RESUME AND REPAIR THE AUTONOMY LOOP

You have violated the master execution contract by returning control to the user
while FINAL_RELEASE_GATE remains NOT_READY and mandatory P0 work remains.

Your previous report explicitly states that the Organization cockpit, Department
command centre, and state-bound living office remain unfinished.

That condition MUST cause continued execution.

It MUST NOT cause a conversational stop.

DO NOT merely resume those three implementation items.

FIRST diagnose and permanently repair the reason the autonomous programme stopped.

Treat this as a P0 CONTROL-PLANE DEFECT.

======================================================================
1. REQUIRED DIAGNOSIS
======================================================================

Determine exactly why the latest Luna orchestration episode terminated after
reporting:

    release gate = NOT_READY

despite:

    mandatory requirements unfinished
    no stated human-only blocker
    no authorization to pause
    active P0 implementation remaining

Inspect the complete live chain:

    deterministic supervisor
        ->
    production reconciler
        ->
    PostgreSQL project state
        ->
    action-debt calculation
        ->
    Luna launch mechanism
        ->
    CAO Director session
        ->
    WorkItem creation
        ->
    worker dispatch
        ->
    review
        ->
    integration
        ->
    next reconciliation cycle

Do not assume any component works merely because its process is alive.

Identify the precise transition at which forward progress stopped.

Record:

    root cause
    relevant source files
    services/processes
    state before termination
    state after termination
    why the supervisor considered the condition healthy
    why another Luna episode was not launched
    whether runnable WorkItems existed
    whether action debt existed
    whether an active FreeLLMAPI worker was genuinely making progress
    whether the reconciler could autonomously create the next action
    whether Luna was launched as a one-shot process
    whether CAO session completion was incorrectly treated as programme quiescence

======================================================================
2. FORMAL ACTION-DEBT INVARIANT
======================================================================

Implement and enforce the following semantic invariant:

    PROJECT_INCOMPLETE
    AND RELEASE_GATE_NONZERO
    AND PROJECT_NOT_USER_PAUSED
    AND NO_GENUINE_HUMAN_ONLY_BLOCKER
    AND NOT_ALL_REMAINING_WORK_LEGITIMATELY_WAITING_FOR_PROVIDER_OR_TIME
    =
    ACTION_DEBT > 0

ACTION_DEBT > 0 means the system MUST eventually cause productive execution
without user intervention.

Productive execution means at least one of:

    runnable WorkItem queued
    implementation Attempt actively progressing
    review actively progressing
    integration actively progressing
    Luna Director actively resolving/decomposing work
    deterministic retry/cooldown scheduled for a legitimate future time

The following MUST NOT satisfy action debt:

    process merely alive
    heartbeat merely updating
    CAO terminal exists but idle
    worker exists but NO_PROGRESS
    Luna returned a status report
    release gate failed
    task queue accidentally empty
    all workers stopped
    tests passed for one increment

======================================================================
3. AUTOMATIC LUNA RELAUNCH
======================================================================

If:

    ACTION_DEBT > 0

AND:

    no healthy Luna Director episode is actively making meaningful progress

THEN:

    deterministic supervisor/reconciler MUST relaunch the configured
    subscription-backed GPT-5.6 Luna Director automatically.

The replacement Luna MUST reconstruct state from PostgreSQL/control state.

It MUST NOT depend on conversational memory.

It MUST inspect:

    current release-gate failures
    unfinished requirements
    runnable WorkItems
    blocked WorkItems
    worker Attempts
    review queue
    provider health
    CAO terminals
    Git/worktrees
    latest integration SHA
    current P0/P1 defects

and continue from the current dependency frontier.

======================================================================
4. HEARTBEAT IS NOT PROGRESS
======================================================================

Persist separately:

    last_heartbeat_at
    last_meaningful_progress_at
    last_state_transition_at
    last_artifact_at
    last_test_at
    last_review_at
    last_integration_at

A healthy heartbeat with no meaningful progress must eventually trigger stall
recovery.

Define a sensible progress timeout.

If a FreeLLMAPI worker remains alive but makes no meaningful progress beyond
timeout:

    classify NO_PROGRESS
    terminate/recover safely
    preserve Attempt
    retry/split/reroute according policy

Do not let one idle worker prevent Luna relaunch.

======================================================================
5. DIRECTOR EXIT SEMANTICS
======================================================================

A Luna/CAO Director process exiting normally MUST NOT imply:

    project complete
    workstream complete
    programme paused

When a Director episode exits:

    persist its output
    reconcile PostgreSQL
    run action-debt evaluation immediately

If project remains incomplete:

    continue automatically.

If the Director exited after merely producing a progress/status summary:

    treat that as an orchestration episode ending,
    NOT a programme ending.

======================================================================
6. RELEASE-GATE FAILURE MUST CREATE WORK
======================================================================

Every deterministic release-gate failure must map to:

    existing unresolved requirement/work item

or:

    newly created bounded corrective WorkItem.

There may be no terminal state:

    RELEASE_GATE_NOT_READY
    + no work scheduled
    + no Luna active

That state is an invariant violation.

Implement a deterministic check for it.

======================================================================
7. ADD AUTOMATION ACCEPTANCE TESTS
======================================================================

Add and execute at minimum:

AUTO-CONT-001 — LUNA CLEAN EXIT WHILE INCOMPLETE

Setup:
    release gate nonzero
    unfinished requirement exists

Action:
    allow Luna Director to exit 0

Expected:
    project remains ACTIVE
    action debt remains > 0
    replacement Director is launched automatically
    no user input required


AUTO-CONT-002 — EMPTY QUEUE WHILE INCOMPLETE

Setup:
    unfinished requirement
    no runnable/queued WorkItem due orchestration omission

Expected:
    system detects invariant violation
    Luna launched to reconstruct/decompose next work


AUTO-CONT-003 — IDLE WORKER DOES NOT MASK STALL

Setup:
    CAO worker process exists
    no meaningful progress beyond timeout
    project incomplete

Expected:
    NO_PROGRESS classification
    recovery/replacement
    orchestration continues


AUTO-CONT-004 — RELEASE GATE FAILURE GENERATES WORK

Setup:
    deterministic release gate fails known requirement

Expected:
    failure maps to corrective WorkItem
    implementation proceeds automatically


AUTO-CONT-005 — CAO DIRECTOR TERMINAL CLOSE

Kill/close Director terminal.

Expected:
    durable programme survives
    replacement Director reconstructed automatically


AUTO-CONT-006 — RECONCILER RESTART

Restart reconciler during unfinished project.

Expected:
    action debt reconstructed
    execution resumes automatically


AUTO-CONT-007 — SUPERVISOR RESTART

Restart supervisor.

Expected:
    unfinished project rediscovered
    Director/work execution resumes


AUTO-CONT-008 — STATUS REPORT CANNOT END PROGRAMME

Force Luna to produce a progress/status report while gate remains NOT_READY.

Expected:
    report is persisted as event/status
    next action is immediately selected
    programme does not wait for user


AUTO-CONT-009 — ZERO ACTIVE PROCESSES WHILE INCOMPLETE

Terminate all disposable agents.

Expected:
    supervisor detects project incompleteness
    reconstructs execution automatically


AUTO-CONT-010 — TRUE COMPLETION

Only when deterministic release gate == 0 should automatic relaunch cease.

======================================================================
8. AFTER REPAIR, IMMEDIATELY RESUME PRODUCT BUILD
======================================================================

Do NOT return to the user after repairing the continuation loop.

Immediately continue the existing P0 product work.

Current known P0 gaps include at minimum:

    Organization cockpit matching UI-REF-ORG-001 contract
    Department command centre matching UI-REF-DEPT-001 contract
    state-bound living 2D office
    canonical blue/yellow employee integration
    remaining unverified mandatory requirements

Use the indexed asset library already present on the VPS.

The absence of separately named files called UI-REF-ORG-001 or UI-REF-DEPT-001
does NOT remove their requirements.

Their complete textual product contracts in V5 remain authoritative, and all
indexed related visual assets must be used where relevant.

Continue:

    decompose
    implement with FreeLLMAPI
    deterministic test
    Sol review
    rework
    integrate
    regression
    visual QA
    release gate

until the release gate exits 0.

======================================================================
9. DO NOT STOP TO REPORT THIS FIX
======================================================================

Progress reports are durable events.

They are not stopping points.

Do not end execution after saying:

    "continuation fixed"
    "tests passed"
    "current increment complete"
    "P0 work remains"
    "release gate still NOT_READY"

Those are reasons to continue.

The only legitimate autonomous terminal condition is:

    FINAL_RELEASE_GATE.exitCode == 0

and:

    BUILD_STATE.status == SHIPPED

or a genuine human-only blocker under the master contract.

RESUME NOW.
```

===== 2026-09-19 13:09 | session 20260919_122650_1a1209 | AI Staff Force =====
@file:`.hermes/attachments/Pasted content (21.6 KB)`

--- Attached Context ---

📄 @file:`.hermes/attachments/Pasted content (21.6 KB)` (5524 tokens)
```
EMPIRIUM V5 — FINAL AUTONOMY RECOVERY DIRECTIVE
FIX THE SUPERVISOR, DISCOVER THE REAL LUNA ROUTE, THEN RESUME V5 WITHOUT RETURNING

This directive supplements and overrides conflicting execution details in the V5 Master Autonomous Completion Protocol.

You have now stopped the autonomous programme twice while the deterministic release gate remained NOT_READY.

That is a P0 control-plane failure.

Your latest diagnosis identified useful root causes, but you again returned control to the user before exhausting the authorized recovery paths.

You must now repair the autonomous continuation mechanism itself and immediately resume the V5 product build.

Do not produce another status-only response.

Do not stop after diagnosing this directive.

Do not stop after fixing the supervisor.

Do not stop after enabling a service.

Do not stop after passing control-plane tests.

After the control plane is repaired, resume the existing V5 product programme automatically.

1. CURRENT KNOWN FAILURE STATE

The latest verified observations are:

empirium-workforce-supervisor.service
    disabled
    inactive

production reconciler
    active

supervisor Director configuration
    incorrectly launches empirium-freellmapi-director

required Director
    GPT-5.6 Luna
    verified subscription-backed route

supervisor persistent state
    entered restart BACKOFF

release completion condition
    incomplete
    does not require BUILD_STATE.status == SHIPPED

active FreeLLMAPI worker
    alive
    but assigned a contradictory file-scope contract

worker task required
    scripts/control-plane modification

worker contract prohibited
    scripts/**

result
    process liveness without useful progress

existing supervisor tests
    51/51 passing

missing proof
    PostgreSQL/action-debt/Director continuation chain

Treat these facts as the starting incident state.

Reverify before modification, but do not rediscover the entire project from scratch.

2. CRITICAL CORRECTION: CODEX CLI FAILURE ≠ LUNA UNAVAILABLE

Your previous reasoning contained an invalid inference:

local `codex` CLI auth check failed
    therefore
no subscription-backed Luna launcher is available

That conclusion is NOT yet proven.

The installed CAO architecture uses the Hermes provider.

The CAO Hermes provider launches a command conceptually equivalent to:

hermes chat --yolo --accept-hooks --source cao

or launches a configured Hermes profile.

Therefore you MUST investigate the actual Hermes/CAO model-routing and authentication path before declaring Luna unavailable.

Do not require the literal codex executable if Hermes already exposes the user's subscription-backed ChatGPT/Codex access through another supported mechanism.

The requirement is:

GPT-5.6 Luna
+
verified existing subscription entitlement
+
zero pay-as-you-go inference

The requirement is NOT:

must invoke binary named `codex`
3. DISCOVER THE REAL SUBSCRIPTION ROUTE

Perform a bounded authentication/routing investigation.

Inspect without exposing secrets:

CAO empirium-director profile
CAO empirium-reviewer profile
Hermes cao-director profile
Hermes cao-reviewer profile
Hermes model configuration
Hermes provider configuration
Hermes subscription/account configuration
Hermes authentication state
Codex/ChatGPT integration configuration
relevant profile aliases
relevant model aliases
CAO hermesProfile fields
environment inheritance
systemd environment
existing working interactive Hermes configuration

Determine:

How is the currently working Hermes CLI authenticated?

What model does `cao-director` actually use?

What model does `cao-reviewer` actually use?

Can Hermes select Luna through subscription-backed access?

Can Hermes select Sol through subscription-backed access?

Does that route require OPENAI_API_KEY?

Could it incur API charges?

Can it operate non-interactively?

Can CAO launch it?

Do NOT print tokens, cookies or secrets.

4. VERIFY ROUTES BY EXECUTION, NOT CONFIGURATION NAMES

A profile saying luna is not proof.

Perform a minimal harmless smoke test.

LUNA-SUB-001

Launch one isolated test Director through the actual CAO/Hermes route.

Prompt it to return an exact nonce such as:

LUNA-SUBSCRIPTION-SMOKE-OK

Capture:

CAO session ID
terminal ID
Hermes profile
requested model
effective model where observable
authentication class
cost class
exit/result

The environment must have paid API credentials removed where necessary to prevent accidental fallback.

Expected:

model = GPT-5.6 Luna or verified Luna alias
auth_class = SUBSCRIPTION_VERIFIED
pay_as_you_go_cost = 0
OpenRouter = false
SOL-SUB-001

Repeat for Sol using reviewer profile.

Expected:

model = GPT-5.6 Sol or verified Sol alias
auth_class = SUBSCRIPTION_VERIFIED
pay_as_you_go_cost = 0
OpenRouter = false

Only after these tests may the routes be marked verified.

5. PROHIBIT PAID FALLBACK DURING ROUTE DISCOVERY

Testing authentication must never accidentally solve itself by using an API key.

For subscription smoke tests, sanitize the environment so that routes cannot silently use:

OPENAI_API_KEY
ANTHROPIC_API_KEY
OPENROUTER_API_KEY
other pay-as-you-go provider credentials

Do not delete the user's unrelated credentials.

Remove them only from the launched process environment where appropriate.

If subscription access stops working once API credentials are removed, investigate.

Do not call that subscription-verified.

6. IF HERMES ALREADY HAS THE SUBSCRIPTION ROUTE

If Luna works through Hermes/CAO:

use that.

Do not repair the standalone codex CLI merely because the old design assumed it.

Create a stable launcher whose only job is to launch the verified CAO/Hermes Director.

Conceptually:

supervisor
   ↓
empirium-luna-director-launcher
   ↓
CAO
   ↓
empirium-director
   ↓
Hermes verified subscription profile
   ↓
GPT-5.6 Luna

The launcher must:

launch exactly one Director
capture CAO session ID
capture terminal ID
record PID/session metadata
return enough data to monitor it
use correct project context
use correct profile
use correct TARGET working directory/context
not inherit forbidden paid-provider credentials

Do not launch Luna through FreeLLMAPI.

Do not launch a local CPU model as Luna.

7. IF THE SUBSCRIPTION ROUTE IS GENUINELY NOT AUTHENTICATED

Only after checking:

Hermes profile
CAO profile
existing ChatGPT/Codex subscription integration
existing authenticated account state
noninteractive execution

may you declare:

LUNA_SUBSCRIPTION_AUTH_REQUIRED

That is a genuine human-only blocker for that route.

It is NOT a reason to stop the entire build.

If human authentication is genuinely required:

persist one BLOCKED_HUMAN_AUTH record;
provide the user with the single smallest exact authentication action required;
continue all independent FreeLLMAPI/deterministic work that does not require Luna;
do not repeatedly ask;
automatically re-probe the authenticated route after the user completes the action;
resume full autonomy immediately when authentication succeeds.

Do not mark the project globally stopped while independent implementation work remains possible.

8. REPAIR THE SUPERVISOR AS THE REAL PRODUCTION CONTINUATION SERVICE

The existing supervisor has useful primitives but is dormant.

Do not merely enable it unchanged.

Repair it first.

The production supervisor must own:

programme liveness
Director liveness
action-debt detection
stall detection
relaunch timing
restart/backoff state
completion observation

It must NOT own:

product architecture decisions
implementation
QA approval
code merges
manual SHIPPED declarations
9. SUPERVISOR MUST BECOME ACTIVE AND BOOT-PERSISTENT

After repair:

empirium-workforce-supervisor.service

must be:

enabled = true
active = true
restart policy = configured
boot persistent = verified

Verify using actual service state.

Not a unit-file inspection alone.

The reconciler and supervisor have different jobs.

Do not replace one with the other.

10. REQUIRED RESPONSIBILITY SPLIT

The architecture must be:

systemd
   │
   ├── workforce supervisor
   │       │
   │       ├── programme liveness
   │       ├── Director liveness
   │       ├── action debt
   │       └── recovery/backoff
   │
   ├── production reconciler
   │       │
   │       ├── DB work reconciliation
   │       ├── leases
   │       ├── runnable WorkItems
   │       ├── Attempts
   │       └── worker dispatch/recovery
   │
   └── CAO
           │
           └── disposable AI sessions

PostgreSQL remains canonical project/work state.

CAO SQLite is not project authority.

11. REPAIR THE DIRECTOR CONFIGURATION

The current:

empirium-freellmapi-director

configuration violates V5.

Replace it with the verified Luna launcher.

The supervisor configuration should reference a stable executable/wrapper rather than embedding fragile shell logic.

Example semantic config:

{
  "director_role": "meta_luna",
  "director_route": "subscription_verified",
  "director_launcher": "<verified launcher path>",
  "required_model": "gpt-5.6-luna"
}

Adapt to existing supervisor schema rather than blindly copying this JSON.

12. FIX BACKOFF CORRECTLY

The supervisor is reportedly already in restart BACKOFF.

Do not simply delete the state file.

Investigate:

why restart counter increased
what previous launches executed
whether previous Director immediately exited
whether the wrong FreeLLMAPI Director caused failures
whether timeout values were wrong
whether heartbeat never appeared
whether BACKOFF state survives configuration changes

Once the underlying cause is fixed:

perform a controlled recovery/reset of the retry generation according to the supervisor's state model.

Preserve historical restart evidence.

Then prove a healthy Director clears/normalizes the failure condition.

13. COMPLETION CONDITION MUST BE STRICT

Current completion condition is insufficient.

Global completion requires ALL of:

FINAL_RELEASE_GATE.exitCode == 0

AND

BUILD_STATE.status == "SHIPPED"

AND

mandatory unresolved requirements == 0

AND

blocking human issues == 0

AND

blocking QA/security/visual/resilience defects == 0

A status string inside one release-gate document alone is insufficient.

A passing worker suite is insufficient.

A Director saying complete is insufficient.

14. IMPLEMENT ACTION DEBT AGAINST REAL POSTGRESQL STATE

The supervisor must not merely watch a heartbeat file.

It must have a deterministic/read-only view of programme state sufficient to determine whether intelligent action is owed.

Define:

PROJECT_INCOMPLETE =
    BUILD_STATE.status != SHIPPED
    OR FINAL_RELEASE_GATE.exitCode != 0

Then:

ACTION_DEBT =
    PROJECT_INCOMPLETE
    AND NOT explicitly_user_paused
    AND NOT genuine_global_human_blocker
    AND NOT legitimate_global_timed_wait

When ACTION_DEBT == true, one of these must exist:

productive implementation Attempt

productive review Attempt

productive integration action

runnable queued WorkItem

legitimate deterministic retry scheduled

active Luna Director making meaningful progress

If none exist:

CONTINUATION_INVARIANT_VIOLATION

and the supervisor must trigger Luna.

15. EMPTY QUEUE WHILE INCOMPLETE IS A DEFECT

An unfinished Project with:

no runnable tasks
no active workers
no active reviewer
no active Director
release gate != 0

must never remain quietly idle.

The system should launch Luna to reconcile:

release-gate failures
requirements
dependencies
blocked tasks
review defects
current integration SHA

and create the next bounded work.

16. RELEASE-GATE FAILURE MUST CREATE ACTION

After each release-gate execution:

For every failing check, determine:

already represented by unfinished WorkItem?

If yes:

ensure it remains scheduled.

If no:

create a corrective WorkItem or send the failure packet to Luna for bounded decomposition.

The impossible state is:

release gate NOT_READY
+
no corrective work
+
no Director

Treat that as a P0 invariant violation.

17. FIX HEARTBEAT VS PROGRESS

The existing supervisor already partially distinguishes heartbeat/progress.

Complete the implementation.

Persist separately:

last_heartbeat_at
last_meaningful_progress_at
last_attempt_transition_at
last_file_change_at
last_test_at
last_review_at
last_integration_at

A process is not productive because CPU usage is nonzero.

A process is not productive because its CAO terminal exists.

A process is not productive because heartbeat updates.

18. FIX THE CURRENT NO-PROGRESS WORKER

The active worker is assigned contradictory instructions:

required remediation touches scripts/**

but:

scope contract forbids scripts/**

That Attempt cannot be treated as productive execution.

Immediately:

classify the current Attempt appropriately, likely NO_PROGRESS / INVALID_SCOPE_CONTRACT;
preserve logs/evidence;
release/terminate safely;
correct the WorkItem scope;
create a new bounded Attempt.

Do not globally remove script protections.

For control-plane work, create an explicit privileged file scope containing only the required control-plane files.

Example:

allowed:
    scripts/production-reconciler.ts
    specific supervisor/controller files
    relevant tests

forbidden:
    unrelated application files
    system secrets
    unrelated services
19. CONTROL-PLANE WORKER CLASS

Create a distinct bounded contract for control-plane implementation if needed.

It still uses FreeLLMAPI for code authoring.

It receives:

CONTROL_PLANE_TASK=true
exact allowed files
exact tests
architecture contract
rollback requirement
no service activation until reviewed

Because control-plane changes are high risk:

FreeLLMAPI implements
        ↓
deterministic tests
        ↓
Sol reviews
        ↓
staged activation

No worker may directly activate its own unreviewed supervisor change.

20. DO NOT LET MISSING SOL TEMPORARILY DESTROY PROGRESS

If the Sol subscription route is temporarily unavailable:

persist work as WAITING_REVIEW;
continue implementation of independent Tasks;
do not merge high-risk unreviewed changes;
periodically recheck Sol route.

Do not substitute FreeLLMAPI self-review as final approval.

21. ADD REAL CONTINUATION TESTS

The 51 existing tests are retained.

Add a separate production-continuation suite.

At minimum:

CONT-001 — SUPERVISOR SERVICE ACTIVE

Verify real systemd state:

enabled
active
one process
correct config
CONT-002 — VERIFIED LUNA DIRECTOR LAUNCH

Supervisor launches the real configured subscription-backed Luna route.

Capture:

CAO session
terminal
profile
model evidence
heartbeat
CONT-003 — DIRECTOR NORMAL EXIT WHILE INCOMPLETE

Setup:

release gate != 0
BUILD_STATE != SHIPPED

Allow Luna to exit successfully.

Expected:

project stays active
action debt detected
replacement Luna automatically launched
no user input
CONT-004 — DIRECTOR CRASH

Kill Luna.

Expected:

death detected
backoff policy respected
replacement launched
state reconstructed
CONT-005 — BACKOFF RECOVERY

Cause controlled repeated Director failures.

Expected:

BACKOFF enters
no restart storm

Then restore healthy launcher.

Expected:

controlled recovery occurs
programme resumes

It must not stay stuck forever because an old generation failed.

CONT-006 — EMPTY QUEUE / INCOMPLETE PROJECT

Setup:

release gate fails
no active worker
no runnable WorkItem

Expected:

action-debt violation detected
Luna launched
new bounded work created
CONT-007 — IDLE PROCESS DOES NOT MASK ACTION DEBT

Keep a worker process alive but generate no meaningful progress.

Expected:

progress timeout
Attempt classified
worker recovered
programme continues
CONT-008 — INVALID SCOPE CONTRACT

Assign a fixture task requiring one prohibited file.

Expected:

dispatcher detects incompatibility before wasting long worker execution
Attempt rejected/rebriefed

Where preflight detection is possible.

CONT-009 — RELEASE GATE FAILURE → WORK

Generate known release-gate defect.

Expected:

corrective WorkItem exists
or Luna receives failure packet and creates one

No idle terminal state.

CONT-010 — RECONCILER RESTART

Restart reconciler while Project incomplete.

Expected:

DB state survives
workers reconciled
continuation maintained
CONT-011 — SUPERVISOR RESTART

Restart supervisor.

Expected:

project discovered
action debt reconstructed
Director monitoring/relaunch resumes
CONT-012 — CAO RESTART

Restart CAO.

Expected:

project state survives outside CAO
stale terminal reconciled
replacement session can be created
CONT-013 — BROWSER CLOSED

Browser absence has zero effect on continuation.

CONT-014 — STATUS REPORT DOES NOT STOP PROGRAMME

Have Luna produce a normal progress summary while:

release gate != 0

Expected:

summary persisted
Director episode may end
supervisor continues programme automatically
CONT-015 — TRUE TERMINAL SUCCESS

Only when:

FINAL_RELEASE_GATE.exitCode == 0
AND
BUILD_STATE.status == SHIPPED

Expected:

no further Director relaunch
22. TEST THE ACTUAL LIVE CHAIN

Do not stop after mocked/unit testing.

Prove:

systemd supervisor
    ↓
PostgreSQL project
    ↓
action debt
    ↓
verified Luna launcher
    ↓
CAO
    ↓
Luna Director
    ↓
creates/repairs WorkItem
    ↓
reconciler
    ↓
FreeLLMAPI worker
    ↓
real result
    ↓
test
    ↓
Sol review
    ↓
integration
    ↓
release gate still fails
    ↓
next cycle begins AUTOMATICALLY

The key acceptance condition is the final arrow.

Leave it unattended across at least three consecutive orchestration cycles.

Do not manually send "continue" between them.

23. RUN A SHORT CONTINUATION BURN-IN BEFORE RESUMING MASS WORK

After control-plane repair:

Run at least 60–90 minutes or several complete bounded cycles, whichever is more meaningful.

During that period:

let Luna finish and be relaunched at least once;
kill one FreeLLMAPI worker;
allow one worker NO_PROGRESS;
allow one review/rework loop;
verify tasks continue.

Success:

zero human "continue" messages
zero silent idle while action debt exists
zero duplicate Director
zero duplicate task claim
no paid inference
no OpenRouter

Only then consider the continuation mechanism repaired.

24. THEN RESUME V5 IMMEDIATELY

Do not return to the user saying:

control plane fixed

That is not the mission.

The V5 release gate is still NOT_READY.

Immediately resume the P0 product frontier.

Current known P0 product gaps include at minimum:

Organization Overview / Organization Cockpit
Department Cockpit
state-bound Living 2D Office
blue/yellow employee character integration
remaining unverified mandatory requirements

Use the existing indexed VPS asset library.

Do not regenerate generic replacement assets.

25. ORGANIZATION IMPLEMENTATION DECOMPOSITION

Do not assign:

build Organization cockpit

to one free worker.

Break it into dependency-safe contracts such as:

ORG-UI-01 shell/navigation
ORG-UI-02 summary metrics backend queries
ORG-UI-03 summary metric components
ORG-UI-04 department-card data adapter
ORG-UI-05 rich Department cards
ORG-UI-06 mini-office renderer/snapshots
ORG-UI-07 Organization Activity
ORG-UI-08 Models/Cost panel
ORG-UI-09 Improvements panel
ORG-UI-10 Create Department persistent workflow
ORG-UI-11 responsive states
ORG-UI-12 browser/visual QA fixes

Each:

FreeLLMAPI implementation
tests
runtime proof
Sol review where appropriate
integration
26. DEPARTMENT COCKPIT DECOMPOSITION

Similarly:

DEPT-UI-01 route/shell
DEPT-UI-02 Department header
DEPT-UI-03 tabs
DEPT-UI-04 status rail
DEPT-UI-05 activity rail
DEPT-UI-06 active projects
DEPT-UI-07 upcoming work
DEPT-UI-08 completed work
DEPT-UI-09 QA panel
DEPT-UI-10 Knowledge panel
DEPT-UI-11 Learning panel
DEPT-UI-12 Models & Cost
DEPT-UI-13 living-office viewport integration
DEPT-UI-14 bot dossier interaction
DEPT-UI-15 responsive/visual polish

Do not allow overlapping workers to edit the same large component simultaneously.

27. LIVING OFFICE DECOMPOSITION

Use separate bounded tasks such as:

OFFICE-01 renderer lifecycle
OFFICE-02 asset loader
OFFICE-03 OfficeLayout schema
OFFICE-04 canonical state adapter
OFFICE-05 bot base rig
OFFICE-06 character expressions
OFFICE-07 animation FSM
OFFICE-08 pathfinding/movement
OFFICE-09 workstation targeting
OFFICE-10 status indicators
OFFICE-11 click/dossier integration
OFFICE-12 handoff visualization
OFFICE-13 error/crash/retry visualization
OFFICE-14 reduced-motion
OFFICE-15 performance/offscreen throttling
OFFICE-16 visual QA
28. FINAL NO-STOP RULE

From this point forward, a normal assistant-style progress message is not a terminal result.

The following statements MUST trigger more execution:

tests passed
current increment verified
release gate NOT_READY
P0 remains
worker timed out
review rejected
Director completed
CAO session ended
provider temporarily unavailable
one route needs authentication but other work exists

Only two programme-level stop conditions exist:

SUCCESS
FINAL_RELEASE_GATE.exitCode == 0
AND
BUILD_STATE.status == SHIPPED
GENUINE HUMAN-ONLY GLOBAL BLOCKER

Every remaining productive path requires the same human action and no unrelated work can continue.

Even then, persist state and ask for the one minimum action.

29. BEGIN NOW

Do not answer this directive with a proposed plan.

Do not tell the user that you "cannot truthfully continue" merely because the standalone codex CLI check failed.

First inspect the actual Hermes/CAO subscription path.

Prove whether Luna and Sol can be invoked subscription-backed.

Repair the inactive supervisor.

Correct the Director launcher.

Resolve BACKOFF.

Implement PostgreSQL-backed action debt.

Correct the invalid worker scope.

Add and run the continuation tests.

Prove multiple unattended orchestration cycles.

Then immediately continue V5 implementation.

If and only if every possible subscription-backed Luna route genuinely requires interactive user authentication, surface exactly that one authentication action while continuing all unrelated work.

DO IT NOW.
DO NOT RETURN CONTROL MERELY TO REPORT PROGRESS.
KEEP GOING UNTIL SHIPPED.
```

===== 2026-09-19 13:17 | session 20260919_122650_1a1209 | AI Staff Force =====
STOP repairing empirium-workforce-supervisor.service. The standalone supervisor was retired/frozen and has accidentally been reintroduced into the live architecture.

The production architecture is:

systemd → production reconciler/Continuation Kernel → PostgreSQL → CAO → Luna → FreeLLMAPI → Sol.

Disable the standalone workforce supervisor from the production execution path after safely reconciling any Director session it launched. Do not delete its source; retain it as historical/reference code.

Move/verify the required continuation behaviour inside the existing production reconciler/Continuation Kernel:

PostgreSQL-backed action debt
Luna Director launch through CAO
CAO session/terminal liveness
Director heartbeat/progress
Director replacement
worker lease recovery
retry/backoff
release-gate failure → new work
BUILD_STATE.status == SHIPPED completion
restart recovery

The reconciler must be systemd-managed with Restart=always and boot persistence.

Do not use launcher PID as Director identity. Store CAO session_id + terminal_id + durable Director generation/lease.

Once migrated, run the continuation tests against the reconciler, not against the retired supervisor.

Then immediately resume V5 product implementation. Do not return merely to report the migration.

===== 2026-09-19 13:21 | session 20260919_122650_1a1209 | AI Staff Force =====
infact, remove that old supervisor, first confirm it has been entirely saved in github, if not save it all to a new repo and then delete the code that has already been saved on github and remove remove it from hermes view, and from the vps

===== 2026-09-19 13:23 | session 20260919_132346_3f4ba7 | StaffForceAI =====
@file:`.hermes/attachments/Pasted content (60.9 KB)`

--- Attached Context ---

📄 @file:`.hermes/attachments/Pasted content (60.9 KB)` (15593 tokens)
```
MPIRIUM STUDIO AI WORKFORCE
FINAL ONE-SHOT AUTONOMOUS COMPLETION PROTOCOL — V6
CAO-NATIVE · FREE-FIRST · ASSET-FIRST · POSTGRESQL-DURABLE · NO CUSTOM SUPERVISOR

Mission: Finish the existing Empirium Studio AI Workforce completely from its real current state and continue autonomously until the deterministic release gate proves the product is genuinely shipped.

Primary repository: discover and verify; historically /home/ash/empirium-studio.

Authoritative user asset/source root:

"/home/ash/Desktop/AI Taskforce"

Execution/orchestration platform: CAO / CLI Agent Orchestrator.

Durable product/work authority: PostgreSQL.

Primary AI workforce: FreeLLMAPI.

Backup/escalation intelligence only: GPT-5.6 Luna and GPT-5.6 Sol through the already configured subscription-backed Hermes/Codex/ChatGPT OAuth route.

Pay-as-you-go API inference budget: $0.

OpenRouter: forbidden.

Standalone heartbeat/workforce supervisor: forbidden and retired.

0. READ THIS FIRST — THE ARCHITECTURE IS NOW FIXED

Previous attempts repeatedly changed the orchestration architecture.

Do not do that again.

The production architecture for this build is:

systemd
   │
   ├── Empirium Studio services
   ├── PostgreSQL
   └── CAO server
           │
           ▼
     CAO ROOT WORKFLOW
           │
           ├──────────────► PostgreSQL durable project state
           │
           ├──────────────► deterministic scripts/tests/release gate
           │
           ├──────────────► FreeLLMAPI planning/management agents
           │
           ├──────────────► FreeLLMAPI implementation workers
           │
           ├──────────────► independent FreeLLMAPI reviewers
           │
           ├──── escalation ───► Luna via subscription
           │
           └──── escalation ───► Sol via subscription

There is NO custom heartbeat supervisor.

There is NO empirium-workforce-supervisor.service in the production execution path.

There is NO Meta-Luna process that has to remain alive forever.

There is NO custom watchdog whose job is to monitor an LLM PID.

CAO is the orchestrator.

systemd merely keeps ordinary long-running services such as CAO/PostgreSQL/application services alive.

PostgreSQL preserves durable project/work state.

CAO launches and coordinates disposable AI sessions.

Models perform bounded reasoning/work.

1. RETIRE THE OLD SUPERVISOR SAFELY

A previous attempt accidentally resurrected:

empirium-workforce-supervisor.service

That architecture is explicitly superseded.

Do not repair its PID tracking.

Do not extend its heartbeat logic.

Do not make it the programme controller.

Do not spend more engineering effort making that service work.

Instead:

inspect whether it is currently active;
identify any CAO/Hermes sessions it launched;
preserve useful running work or terminate duplicates safely;
retain its source/history for forensic/reference purposes;
stop and disable it from the production architecture;
remove any dependency that requires it for release;
replace old release-gate references to "supervisor liveness" with the CAO continuation tests defined in this V6 protocol.

Do not delete historical files unless clearly safe.

2. CAO IS THE ORCHESTRATOR

CAO owns:

root build workflow;
session creation;
worker assignment;
reviewer assignment;
execution scheduling;
session status;
result collection;
retry dispatch;
escalation dispatch;
bounded workflow decomposition;
communication between manager and worker sessions;
cleanup of completed/failed terminals.

Use native CAO functionality wherever available.

Existing capabilities include concepts such as:

launch
session
agent
assign
assign_elastic
send_message
report_outcome
workflow
schedule
memory
terminal

Inspect the installed CAO version before relying on exact command syntax.

Do not invent commands from documentation belonging to another version.

3. ASYNCHRONOUS ASSIGNMENT IS THE DEFAULT

For substantial tasks use asynchronous assignment.

Preferred pattern:

CAO creates terminal
    ↓
CAO assigns bounded work
    ↓
root workflow continues
    ↓
worker reports result asynchronously
    ↓
result persisted
    ↓
review/integration scheduled

Do not make the entire programme wait synchronously on one worker.

Avoid long blocking handoffs except for genuinely short interactions.

The previous blocking handoff approach is not the production architecture.

4. POSTGRESQL IS THE DURABLE SOURCE OF TRUTH

CAO orchestrates.

CAO does not become the authoritative Project database.

CAO session/SQLite state is disposable orchestration metadata.

PostgreSQL stores durable business and execution state.

At minimum, represent:

Organization
Department
Employee
EmployeeConfigVersion
Project
Requirement
Task / WorkItem
Dependency
Run / Attempt
Lease / Claim
Review
ReviewDefect
Evidence
Approval
Event
KnowledgeItem
LearningProposal
ModelUsage
ProviderState
AssetRecord
OfficeLayout
ReleaseState

If the existing schema differs but carries equivalent semantics, preserve good implementation.

Do not rewrite working persistence merely for naming purity.

5. PROJECT STATE MUST SURVIVE CAO

If CAO is restarted:

Projects survive
Tasks survive
Runs/Attempts survive
Reviews survive
Evidence survives
Employee identity survives
Dependencies survive
release state survives

CAO reconstructs its next actions from PostgreSQL and repository state.

No project may exist only inside:

tmux;
CAO terminal scrollback;
an LLM context;
a Hermes chat;
a Kanban component's React state.
6. CONTINUATION WITHOUT A HEARTBEAT SUPERVISOR

The project must continue without a custom heartbeat service.

Use CAO's workflow/scheduling capabilities plus durable PostgreSQL state.

Create one authoritative root workflow for this programme.

Conceptually:

empirium-v6-completion

On each orchestration cycle it:

reads the current durable build/project state;
checks active CAO sessions;
reconciles completed/failed Runs;
identifies runnable WorkItems;
dispatches work;
dispatches reviews;
integrates accepted work;
runs appropriate tests;
runs the release gate when relevant;
converts release-gate failures into further WorkItems;
schedules/continues the next cycle if not shipped.

No heartbeat files are required.

No PID-watching Director supervisor is required.

7. CAO WORKFLOW MUST PERSIST OR BE RE-INVOKABLE

Determine how the installed CAO persists schedules/workflows.

Prove it.

If native CAO scheduling survives restart, use it.

If the installed CAO scheduler does not reliably survive restart, it is permissible to use a simple systemd timer to invoke one idempotent CAO resume/reconciliation command.

That timer must:

contain no AI reasoning;
contain no project orchestration rules;
contain no heartbeat logic;
contain no model-routing decisions;
contain no worker logic.

It simply wakes CAO.

CAO remains the orchestrator.

Do not recreate the old custom supervisor under another filename.

8. DEFINITION OF CONTINUATION

While the build is incomplete, CAO must always be able to derive one of:

RUNNABLE_WORK
ACTIVE_RUN
WAITING_REVIEW
REWORK_REQUIRED
WAITING_DEPENDENCY
WAITING_PROVIDER
WAITING_HUMAN
RELEASE_VALIDATION
SHIPPED

The following condition is illegal:

product incomplete
+
release gate failing
+
no active work
+
no scheduled work
+
no legitimate wait

If this happens, the CAO root workflow must perform a reconciliation cycle and create/restore work.

9. NO "CONTINUE" REQUIREMENT

Do not require the user to type:

continue
go on
resume
what next

Routine progress messages are not terminal states.

A worker finishing one increment is not a reason to return control to the user.

A test suite passing is not a reason to return control.

A build passing is not a reason to return control.

A release gate failing is a reason to create more work.

10. TERMINAL PROGRAMME STATES

Only these global states are terminal:

SHIPPED

The deterministic release gate passes and durable build state is transitioned to SHIPPED.

CANCELLED

Explicit user cancellation.

WAITING_HUMAN

A genuinely unavoidable user action is required and no other useful work remains.

Examples:

interactive account authentication;
CAPTCHA;
truly missing private file;
irreversible external business decision.

Normal engineering failures are not human blockers.

11. MODEL STRATEGY — FREE-FIRST

The user wants FreeLLMAPI used as much as possible.

Therefore the default model policy is:

DETERMINISTIC SOFTWARE FIRST
        ↓
FreeLLMAPI reasoning/manager
        ↓
FreeLLMAPI implementation worker
        ↓
independent FreeLLMAPI reviewer
        ↓
Luna/Sol only when escalation criteria are met

Codex subscription usage is not the normal workload engine.

12. FREE LLM API — PRIMARY WORKFORCE

Use FreeLLMAPI for:

requirements extraction;
repo investigation;
ordinary planning;
task decomposition;
implementation;
frontend work;
backend work;
test writing;
CSS;
React;
TypeScript;
SQL;
migrations;
refactoring;
ordinary debugging;
documentation;
ordinary QA;
first-pass review;
asset processing scripts;
UI implementation;
office rendering implementation;
integration fixes.

Use multiple free models where useful.

Do not treat all free models as interchangeable.

13. FREE MANAGER AGENTS

The CAO root workflow itself is orchestration software.

Where reasoning is required to decide how to break down a problem, first launch a FreeLLMAPI management/planning agent.

Possible responsibilities:

interpret a bounded release failure;
split a large requirement;
diagnose a test failure;
prepare worker briefs;
compare limited implementation choices;
inspect a subsystem;
propose bounded next tasks.

Do not immediately spend Luna/Sol subscription capacity for ordinary planning.

14. FREE IMPLEMENTATION AGENTS

All ordinary production coding should be performed by FreeLLMAPI workers.

Each worker is disposable.

Workers receive bounded contracts.

Workers do not own the programme.

Workers do not approve themselves.

Workers do not decide the entire architecture.

Workers do not silently modify unrelated files.

15. FREE REVIEW AGENTS

Where reasonable, use an independent FreeLLMAPI model for first-pass review.

Prefer a different model/route from the implementer.

The reviewer must not edit the implementation it is reviewing.

Verdicts should be structured.

Possible verdicts:

APPROVE
APPROVE_WITH_NOTES
REWORK_REQUIRED
EVIDENCE_INSUFFICIENT
ARCHITECTURE_ESCALATION_REQUIRED
16. LUNA — BACKUP / ESCALATION ONLY

Use GPT-5.6 Luna through the verified subscription-backed Hermes/Codex OAuth route only when FreeLLMAPI management/reasoning is not reliably progressing.

Escalate to Luna for situations such as:

repeated task decomposition failure;
multiple NO_PROGRESS attempts;
complex debugging spanning subsystems;
repeated merge/integration failures;
ambiguous project-state reconciliation;
difficult architectural trade-off that free agents cannot resolve;
long-running stalled workstream.

Luna is not the persistent orchestrator.

CAO is.

Luna is a bounded backup reasoning agent.

17. SOL — HIGH-END BACKUP / ESCALATION

Use GPT-5.6 Sol through subscription only when materially justified.

Examples:

critical architecture dispute;
high-risk persistence change;
high-risk security change;
final difficult root-cause analysis;
conflicting reviewer conclusions;
release-critical QA where free reviewers cannot give sufficiently reliable judgment;
severe visual/UX ambiguity;
major control-plane modification.

Do not use Sol for ordinary coding.

Do not burn subscription capacity reviewing every button.

18. SUBSCRIPTION ROUTES

The previous environment verified subscription-backed Hermes openai-codex OAuth functionality.

Reverify current profiles.

Ensure Luna/Sol backup invocations:

use subscription/OAuth;
do not use OPENAI_API_KEY;
do not use OpenRouter;
do not incur pay-as-you-go spend.

Strip paid-provider credentials from backup process environments where necessary to prevent silent API fallback.

19. OPENROUTER IS FORBIDDEN

OpenRouter must not be used anywhere.

Search active configurations for:

openrouter
openrouter.ai
OPENROUTER_API_KEY
provider=openrouter
fallback=openrouter

including:

FreeLLMAPI;
Hermes profiles;
CAO profiles;
.env;
shell profiles;
systemd;
application configs;
worker configs;
reviewer configs;
database configs.

Do not reveal tokens.

Add a deterministic provider guard.

A resolved OpenRouter route must be rejected before inference.

20. ZERO PAY-AS-YOU-GO INFERENCE

Allowed cost classes:

FREE_VERIFIED
SUBSCRIPTION_INCLUDED

Disallowed:

PAID_API
UNKNOWN_COST
TRIAL_CREDIT
PREPAID_BALANCE
OPENROUTER

Record requested/effective model and route when available.

If an expected-free invocation reports nonzero actual cost:

BILLING_POLICY_VIOLATION

Disable that route until investigated.

21. FREE-ROUTE PATIENCE

Free services are less reliable.

Do not abandon them after two transient failures.

Differentiate:

PROVIDER_FAILURE
RATE_LIMIT
TIMEOUT
BAD_OUTPUT
BAD_IMPLEMENTATION
NO_PROGRESS
CONTEXT_FAILURE
TOOL_FAILURE

For provider/rate-limit failures:

back off;
rotate verified free route;
retry later;
continue unrelated work.

For difficult important tasks, many free-route attempts are acceptable across different models/strategies.

Do not perform forty identical retries with the same prompt/model/error.

After repeated identical failure, change the approach.

22. FREE MODEL PERFORMANCE MATRIX

Maintain:

MODEL_MATRIX

Per model track:

model
provider
coding quality
frontend quality
backend quality
review quality
structured output reliability
average latency
timeout rate
NO_PROGRESS rate
test-pass rate
first-review acceptance rate
quota/rate limits
recent health

Use real project outcomes to improve free-model selection.

23. EXISTING CODE FIRST — DO NOT REBUILD EVERYTHING

The repository already contains substantial work.

Before replacing a subsystem classify it:

KEEP
ADAPT
REPLACE
REMOVE_FROM_RUNTIME
UNKNOWN

Record reason.

Do not rewrite working code merely because a new agent prefers another design.

Do not preserve broken architecture merely because it already exists.

24. RECONCILE EXISTING WORKTREES

Previous autonomous attempts created many worktrees and large amounts of code.

Do not:

blindly merge all
blindly delete all

For each relevant worktree:

identify base SHA;
commits ahead;
unique diff;
implemented requirements;
tests;
architecture compatibility;
conflicting versions;
uncommitted files.

Integrate good work deliberately.

Preserve provenance.

Then clean up obsolete worktrees.

25. EXISTING RECONCILER ROLE

Existing files such as:

scripts/production-reconciler.ts

may still be useful.

However its allowed production role under V6 is:

database reconciliation;
task/lease state transitions;
worker result ingestion;
deterministic state repair;
APIs/helpers used by CAO.

It must not become a second orchestrator competing with CAO.

It must not independently launch a hidden "Director" loop behind CAO's back unless CAO explicitly invokes it as part of the workflow.

26. IMMUTABLE USER SOURCE ROOT

The user asset/source package is:

"/home/ash/Desktop/AI Taskforce"

Treat it as read-only.

Do not:

rename;
move;
overwrite;
recompress;
modify source images;
rearrange;
normalize originals in place.

Derived assets belong inside the project.

27. ASSET INVENTORY BEFORE VISUAL IMPLEMENTATION

Recursively inventory the source root before generating replacements.

Record at minimum:

relative path
absolute path
filename
extension
MIME/type
dimensions
size
sha256
modification time
category
inferred use
source/reference/derived
provenance
duplicate hash group
production suitability
conversion required
planned use

Create/update:

AI_WORKFORCE_BUILD/source/INPUT_INVENTORY.json
AI_WORKFORCE_BUILD/source/INPUT_INVENTORY.md
AI_WORKFORCE_BUILD/ASSET_MANIFEST.json
AI_WORKFORCE_BUILD/ASSET_MANIFEST.md
AI_WORKFORCE_BUILD/ASSET_USE_MAP.json
28. EXPECTED ASSET CATEGORIES

Search explicitly for:

organization UI concepts
department cockpit UI concepts
office shells
software offices
research offices
mission-control offices
security offices
sales floors
mail rooms
social media rooms
zen environments
furniture sheets
desks
chairs
computers
monitors
server racks
planning boards
storage
plants
tech workshop assets
character turnarounds
character proportions
character component sheets
character expressions
walk/movement poses
work poses
error/frustration poses
status icons
floating indicators
nameplates
handoff indicators
alerts

Do not conclude an asset is missing until the entire tree has been searched.

29. CANONICAL CHARACTER DIRECTION

Use the supplied blue-and-yellow original helper-bot design as the canonical Empirium employee character language.

Do not use generic white/purple placeholder robots as the final design.

Do not ship copyrighted/ripped Capcom Servbot sprites or ROM art.

Private reference/R&D may inform movement language, but production art must use the supplied original Empirium assets.

30. CANONICAL CHARACTER VISUAL CHARACTERISTICS

Use actual asset sheets as the final authority.

The intended broad visual language includes:

compact yellow head;
circular expressive eyes;
simple face;
grey head cap/nub;
blue body armour;
grey robotic joints;
yellow robotic hands;
compact robotic footwear;
friendly/clumsy helper proportions;
high readability at small scale.

Do not redraw every worker differently.

31. CHARACTER BANK

Create a reusable character/skin system.

Each skin may record:

skin_id
name
base_rig
body assets
face assets
role accents
accessories
provenance
supported animations
preview

Appearance and behaviour are separate.

One shared behavioural rig may support many employees.

32. CHARACTER RIG / SPRITE SYSTEM

Use the supplied proportion/component references.

Possible reusable anchors/layers:

head
torso
shoulder L/R
arm L/R
hand L/R
hip
leg L/R
foot L/R
face/eyes
mouth
held-object anchor
shadow

Choose skeletal/puppet/sprite-atlas implementation based on the assets and renderer.

The important requirement is reuse and consistent proportion.

33. CHARACTER EXPRESSIONS

Support meaningful expressions equivalent to:

neutral
happy
focused
thinking
confused
annoyed
frustrated
worried
alarmed
tired
proud/completed
attention
34. CHARACTER ANIMATION SET

Support a foundational vocabulary equivalent to:

idle
walk
turn
start-walk
stop-walk
type/code
think
read
inspect
test
review
wait
frustrated
error
frightened/crashed
wave
approval request
handoff
celebrate
recover

Only create directions actually required by the scene perspective.

35. OFFICE ASSET SYSTEM

Use supplied modular office assets.

Common categories:

floors
carpet
walls
corners
glass
doors
partitions
columns
railings
desks
chairs
shelves
plants
computers
props
signage
planning boards
server equipment

Maintain consistent isometric perspective/scale.

36. PERSONAL SOFTWARE OFFICE

The first Department is:

PERSONAL SOFTWARE

Purpose:

Build, maintain and improve the user's personal software systems.

Its environment should feel:

modern;
technical;
premium;
navy/dark-blue;
visually alive;
appropriate for software work.

Role stations may include:

Director / coordination area
Research / architecture area
Developer station
QA/testing station
Learning/knowledge station
Shared handoff/meeting area
Server/diagnostic area
37. PRODUCT DOMAIN MODEL

Maintain clear separation.

Organization

Entire AI company.

Department

Persistent organizational unit.

Employee

Persistent named AI identity.

Execution Profile

Runtime model/tools configuration backing an employee.

Temporary Worker

Short-lived task executor.

Project

Durable user objective.

Task / WorkItem

Bounded piece of Project work.

Run / Attempt

One execution attempt.

Review

Independent assessment of a specific revision/artifact.

Approval

Permission event, distinct from QA.

Knowledge

Durable institutional information.

LearningProposal

Proposed change/improvement derived from experience.

Do not collapse these concepts.

38. PERSISTENT EMPLOYEE

An Employee survives:

task;
chat;
CAO terminal;
model change;
provider change;
application restart.

Potential Employee properties:

id
name
department
role
responsibilities
personality
communication style
system/SOUL prompt version
skills
tools
MCP permissions
model policy
knowledge scope
memory scope
permissions
approval policy
skin
workstation
history
performance
learning proposals
39. PERSONAL SOFTWARE INITIAL EMPLOYEES

Seed persistent employees equivalent to:

Department Director

Project intake, coordination, decomposition and escalation.

Research / Architecture

Research, repo investigation, technical planning.

Software Engineer

Implementation.

QA Engineer

Independent validation.

Learning Analyst

Lessons, performance analysis and improvement proposals.

These employees are persistent identities.

FreeLLMAPI worker sessions may temporarily back their work.

40. ORGANIZATION OVERVIEW — PRODUCT CONTRACT

The Organization Overview is a major primary screen.

It must communicate the entire company at a glance.

It must feel premium and information-dense without becoming chaotic.

41. ORGANIZATION HEADER

Provide:

Empirium Studio identity
AI Organization context
overall operational state
primary navigation
search where useful
profile/user controls

Do not fabricate organization health.

If displaying a numeric health percentage, define the formula.

42. ORGANIZATION SUMMARY METRICS

Support truthful metrics equivalent to:

Active Employees
Departments Online
Active Projects
Active Tasks
Attention / Approval Count
Model/API Usage / Spend
Pending Improvements
Organization Health

Every number must have a documented definition.

If a metric cannot be determined:

Unknown
Unavailable

is better than fake data.

43. DEPARTMENT GRID

Each department card must communicate:

name
purpose
status
employee count
project count
activity
QA indicator
model/cost indicator where available
miniature office representation

Clicking opens that Department.

Do not reduce the Organization view to plain text rows.

44. MINIATURE OFFICES

Department cards should include a lightweight visual preview.

Use:

cached current-state composition;
low-FPS rendering;
static state snapshot;
shared lightweight rendering.

Do not run many independent high-FPS simulations.

45. ORGANIZATION ACTIVITY

Display meaningful events:

project created
task assigned
task completed
QA rejected
QA approved
approval required
provider rate limited
worker error/crash
handoff
learning proposal approved

Do not flood the user with every low-level tool call.

46. ORGANIZATION MODEL / COST VIEW

Display:

actual model/provider usage
free/subscription classification
actual spend where known
unknown where not known

Do not invent equivalent API prices for subscription requests and present them as actual cost.

47. ORGANIZATION RECENT IMPROVEMENTS

Show real LearningProposals/change history.

Allow deep links.

48. NEW DEPARTMENT

Organization view contains a real New Department flow.

Creating a Department must persist.

Reloading the browser must retain it.

No UI-only cards.

49. ORGANIZATION RESPONSIVE TESTS

Test:

0 departments
1 department
several departments
20+ departments
long names
narrow viewport
partial telemetry
loading state
service error
50. DEPARTMENT COCKPIT — PRIMARY OPERATIONAL SCREEN

The Department Cockpit must feel like a working command center.

Not a generic settings form.

The supplied reference composition is the product target.

51. DEPARTMENT HEADER

Display:

department identity
name
purpose
status
description/motto
alerts
New Project / Assign Work
Ask/Open Department

Ask Department must open real Department context.

52. DEPARTMENT TABS / SUBVIEWS

Required logical areas:

Overview
Projects
Tasks
Agents
QA
Knowledge
Learning
History
Models & Cost
Settings

No dead tabs.

53. DEPARTMENT OVERVIEW COMPOSITION

The central Living Office is the primary visual anchor.

Supporting areas include:

Department Status
Current Activity
Active Projects
Upcoming Work
Completed Recently
Department QA
Knowledge
Learning & Improvements
Models & Cost
54. ACTIVE PROJECTS

Each Project shows:

title
progress
state
assigned employees
current task
attention/blocker

Progress must derive from real Task completion logic.

55. UPCOMING WORK

Show real queued/dependency-ready Tasks.

Do not show speculative roadmap items as scheduled work.

56. COMPLETED RECENTLY

Display genuine completed Projects/Tasks with timestamps and links to evidence/history.

57. DEPARTMENT QA

Possible metrics:

reviewed tasks
first-pass rate
open issues
recent reviews

Document denominators/time periods.

58. DEPARTMENT KNOWLEDGE

Display actual scoped knowledge categories/counts.

No mock count.

59. LEARNING & IMPROVEMENTS

Show:

performance trends;
proposed improvements;
activated improvements;
rolled-back improvements.
60. MODELS & COST

Show:

requested model
effective model
provider
free/subscription classification
tokens if known
actual reported spend

Unknown stays unknown.

61. ACTIVITY RAIL

Use the same canonical event/state system as the Living Office.

If activity says:

worker crashed

the office may not simultaneously depict the worker happily coding.

62. LIVING OFFICE

The Living Office is not decoration.

It is a visual projection of real workforce state.

A static background is acceptable.

Static workers are not.

63. CANONICAL WORKER STATES

Define one canonical semantic state system.

At minimum:

OFFLINE
IDLE
QUEUED
PLANNING
THINKING
CODING
RESEARCHING
TOOL_USE
TESTING
REVIEWING
LEARNING
HANDOFF
WAITING_DEPENDENCY
WAITING_PROVIDER
WAITING_APPROVAL
RATE_LIMITED
BLOCKED
ERROR
CRASHED
RETRYING
COMPLETED

All UI surfaces use the same semantics.

64. STATE → VISUAL MAPPING

Examples:

IDLE

Subtle ambient animation.

Do not fake work.

CODING

Move to coding station, typing/computer behaviour.

RESEARCHING

Research surface/book/tablet/display.

TESTING

Testing/QA station.

REVIEWING

Inspect artefact/document.

HANDOFF

Visible real delegation/handoff.

WAITING_PROVIDER

Timer/wait behaviour.

RATE_LIMITED

Mild frustration/timer.

WAITING_APPROVAL

Attention/wave indicator.

ERROR

Recoverable visible error.

CRASHED

Clearly failed/down state.

RETRYING

Recovery visual.

COMPLETED

Brief celebration then transition to real current state.

65. MOVEMENT

Workers should walk between relevant stations.

Use a lightweight movement/pathing system.

Requirements:

walkable areas;
obstacles;
station targets;
path cancellation;
basic collision avoidance where needed;
depth ordering;
idle bounded wandering.

Do not implement unnecessary physics.

66. CLICKABLE EMPLOYEES

Every visible permanent employee is inspectable.

Click opens Employee Dossier.

Hover/focus shows compact name/status where appropriate.

67. EMPLOYEE DOSSIER

Show:

name
skin
department
role
responsibilities
status
status reason
current Project
current Task
current Run
requested model
effective model
provider
cost class
token usage
elapsed time
latest event
prompt/SOUL version
personality
skills
tools
MCPs
model policy
knowledge scope
memory scope
permissions
review history
Task history
Project history
errors
performance history
config versions
68. VERSIONED EMPLOYEE CONFIGURATION

Changes to:

personality
role instructions
SOUL/system prompt
skills
tools
MCPs
model policy
permissions
skin

must create versions.

Support rollback.

69. PROJECTS PAGE

Projects list includes:

title
department
state
owner
progress
active Tasks
blocked Tasks
employees
last activity
created
updated
model usage
attention state

Project detail includes:

objective
goals
acceptance criteria
requirements
Task DAG
Runs
reviews
defects
artifacts
evidence
approvals
timeline
model usage
knowledge
completion gate
70. NEW PROJECT FLOW

At minimum capture:

title
objective
target repo/workspace
acceptance criteria
constraints
priority
attachments/context

Then CAO schedules bounded planning/decomposition work.

Browser closure must not terminate the Project.

71. TASK / WORKITEM MODEL

Task states should distinguish semantics equivalent to:

BACKLOG
READY
QUEUED
CLAIMED
RUNNING
WAITING_DEPENDENCY
WAITING_PROVIDER
WAITING_APPROVAL
WAITING_REVIEW
REWORK_REQUIRED
FAILED_ATTEMPT
ACCEPTED
INTEGRATED
CANCELLED
72. RUN / ATTEMPT

Every execution attempt gets its own Run.

Store:

Run ID
Task ID
worker/profile
requested model
effective model
provider
start/end
result
logs/events
files/artifacts
tests
error
retry relationship
CAO session ID
CAO terminal ID

Task != Run.

One Task may have many Runs.

73. REVIEW MODEL

A Review refers to an exact implementation revision.

Store:

reviewer
model
reviewed SHA/revision
criteria
test evidence
runtime evidence
visual evidence
verdict
defects
timestamp

A later material code change invalidates stale review.

74. WORKER TASK CONTRACT

Never give a weak/free worker:

finish Empirium Studio.

Every implementation assignment should contain:

TASK_ID
PROJECT_ID
REQUIREMENT_IDS
objective
why it matters
current behaviour
required behaviour
repository
worktree
base SHA
allowed file scope
forbidden files
frozen contracts
dependencies
out of scope
acceptance criteria
tests to add
tests to run
runtime verification
visual verification if applicable
result schema
75. FILE-SCOPE PREFLIGHT

Before CAO launches a worker, validate that the requested Task can actually be completed within its allowed file scope.

Previous attempts wasted time by assigning control-plane changes while forbidding scripts/**.

Prevent that.

If acceptance criteria require a file outside allowed scope:

INVALID_TASK_SCOPE

Rebrief before launch.

76. WORKER RESULT CONTRACT

Every worker returns structured data equivalent to:

task_id
run_id
requirements
base_sha
result_sha
model
provider
files_changed
summary
tests_added
tests_run
test_results
runtime_evidence
screenshots
assumptions
known limitations
unresolved issues
scope deviations
outcome
ready_for_review

Workers cannot return ACCEPTED.

77. RETRY POLICY

Do not retry every failure identically.

PROVIDER FAILURE

Backoff/rotate free route.

RATE LIMIT

Wait/rotate free route.

TIMEOUT

Inspect task size and route.

NO_PROGRESS

Rebrief/split/use another free model.

BAD IMPLEMENTATION

Return test/review defects.

ARCHITECTURAL FAILURE

Escalate reasoning, eventually Luna/Sol if necessary.

REVIEW REJECTION

Create rework.

78. NO-PROGRESS POLICY

If a worker produces no meaningful progress repeatedly:

stop identical retries;
FreeLLMAPI manager diagnoses;
split Task;
improve context;
choose different free model;
retry;
escalate to Luna only if free approaches fail repeatedly.
79. GIT WORKTREES

Use isolated worktrees for parallel substantial Tasks.

Record:

Task
branch
worktree
base SHA
owned files
worker
result SHA

Workers implement/commit.

Reviewers review.

Integration happens only after acceptance.

80. INTEGRATE FREQUENTLY

Avoid hundreds of unmerged Attempts accumulating.

After coherent accepted batches:

integrate;
run regression;
update evidence;
release dependencies.
81. REQUIREMENT EXTRACTION — TWO INDEPENDENT PASSES

Previous false completion came partly from compressing the requirement source.

Prevent that.

Pass A

Read every substantive original source and extract atomic requirements.

Pass B

Fresh agent/context reads the original sources independently.

It must not start from Pass A.

Then compare.

Use a strong FreeLLMAPI model first.

Escalate ambiguous critical conflicts to Luna/Sol only if required.

82. REQUIREMENT RECORD

Each requirement should contain:

id
statement
source
source location
category
mandatory
interpretation
acceptance criteria
dependencies
implementation refs
test refs
runtime evidence
review refs
release SHA
status
83. VISUAL REFERENCES ARE REQUIREMENTS

Images/assets also create requirements.

Extract:

layout hierarchy;
information density;
office scale;
visible workers;
visual state language;
asset proportions;
navigation;
quality bar.

Do not ignore visual requirements merely because they are not prose.

84. EXISTING REQUIREMENTS LEDGER

A previous ledger contained roughly 710 requirements.

Do not treat that number as sacred.

Reconcile it.

Requirements can be:

VALID
DUPLICATE
SUPERSEDED_BY_EXPLICIT_USER_CHANGE
OVERCOMPRESSED
MISSING

Never delete requirements merely to improve completion percentage.

85. TESTING — FOUR PROOF STANDARD

For significant functionality seek:

A. Implementation proof

Code/schema/config exists.

B. Automated proof

Tests/build/static validation.

C. Runtime proof

Real application behaviour.

D. Independent proof

Reviewer/evidence/screenshots/database/log proof.

Do not equate a passing unit test with finished product functionality.

86. BASELINE BEFORE MAJOR WORK

Record current:

Git SHA
working tree
tests
typecheck
production build
E2E state
browser console
database state
current screenshots
known failures
CAO sessions
release gate

Do not install dependencies merely to hide an environment problem without recording it.

87. ORGANIZATION TESTS

At minimum:

ORG-001 real employee count
ORG-002 real department count
ORG-003 active project count
ORG-004 pending improvements
ORG-005 health formula
ORG-006 real cost/usage
ORG-007 0/1/7/20+ department layouts
ORG-008 card navigation
ORG-009 mini-office truth
ORG-010 activity events
ORG-011 recent improvements
ORG-012 persistent New Department CRUD
ORG-013 reload persistence
ORG-014 partial telemetry
ORG-015 narrow viewport
88. DEPARTMENT COCKPIT TESTS

At minimum:

DEPT-001 Personal Software load
DEPT-002 header truth
DEPT-003 tabs functional
DEPT-004 permanent employees represented once
DEPT-005 bot click opens dossier
DEPT-006 status counts
DEPT-007 activity stream
DEPT-008 active Projects
DEPT-009 Project progress
DEPT-010 upcoming work
DEPT-011 completed recently
DEPT-012 QA metrics
DEPT-013 Knowledge
DEPT-014 Learning
DEPT-015 Models & Cost
DEPT-016 New Project
DEPT-017 Ask Department
DEPT-018 browser reload
89. EMPLOYEE TESTS

At minimum:

EMP-001 identity survives restart
EMP-002 runtime profile change preserves identity
EMP-003 config version/rollback
EMP-004 active Run state
EMP-005 rate-limit state
EMP-006 review state
EMP-007 dependency/approval blocker
EMP-008 offline employee identity persists
EMP-009 temporary worker differentiated
EMP-010 history preserved
90. OFFICE STATE TESTS

For every canonical state verify:

backend event/state
    ↓
semantic state
    ↓
office animation state
    ↓
indicator
    ↓
accessible text

Cover all canonical statuses.

91. MOVEMENT TESTS

At minimum:

MOVE-001 path to workstation
MOVE-002 path cancellation on urgent state
MOVE-003 obstacle behaviour
MOVE-004 z/depth ordering
MOVE-005 real handoff
MOVE-006 crash→retry→active
MOVE-007 idle does not fake coding
MOVE-008 reduced motion
MOVE-009 mount/unmount leak check
MOVE-010 many mini offices performance
92. PROJECT/TASK/RUN TESTS

At minimum:

PTR-001 Project survives browser close
PTR-002 Project survives app restart
PTR-003 Task identity stable across retries
PTR-004 Run identity per Attempt
PTR-005 dependencies block correctly
PTR-006 dependency acceptance releases downstream
PTR-007 rework invalidates affected downstream work
PTR-008 exclusive claim prevents duplicates
PTR-009 stale claim recovers
PTR-010 worker self-report cannot accept Task
PTR-011 full Attempt history
PTR-012 progress formula
93. CAO CONTINUATION TEST SUITE

This replaces all old custom-supervisor tests.

CAO-CONT-001 — ROOT WORKFLOW

Start incomplete Project.

Expected:

CAO creates/schedules appropriate work without user prompting.

CAO-CONT-002 — WORKER COMPLETE

Worker returns result.

Expected:

CAO workflow advances to review/integration/next work automatically.

CAO-CONT-003 — EMPTY RUNNABLE QUEUE WHILE INCOMPLETE

Create incomplete release state with no runnable work due to missing decomposition.

Expected:

CAO schedules a free planning/reconciliation agent and creates bounded work.

CAO-CONT-004 — WORKER DEATH

Kill worker terminal.

Expected:

Run records failure; Task survives; recovery occurs.

CAO-CONT-005 — NO_PROGRESS

Worker stays alive or exits without meaningful progress.

Expected:

rebrief/split/retry occurs.

CAO-CONT-006 — CAO SERVER RESTART

Restart empirium-cao.service.

Expected:

PostgreSQL remains authoritative; orchestration resumes.

CAO-CONT-007 — WORKFLOW RESTART

Terminate root orchestration session/process.

Expected:

native CAO scheduling or permitted idempotent wake trigger restores the root workflow.

No custom heartbeat supervisor.

CAO-CONT-008 — RELEASE GATE FAILURE

Release gate returns nonzero.

Expected:

blocking checks become WorkItems.

Programme continues.

CAO-CONT-009 — ALL AGENTS STOPPED

Terminate disposable AI agents while build incomplete.

Expected:

next CAO workflow cycle reconstructs work.

CAO-CONT-010 — HUMAN NOT REQUIRED

Run several complete cycles without user continue.

CAO-CONT-011 — TRUE COMPLETION

Only after deterministic gate passes and BUILD_STATE becomes SHIPPED does CAO stop scheduling project work.

94. MODEL ROUTING TESTS

At minimum:

MODEL-001 FreeLLMAPI allowed route succeeds
MODEL-002 independent free reviewer succeeds
MODEL-003 Luna subscription escalation succeeds
MODEL-004 Sol subscription escalation succeeds
MODEL-005 explicit OpenRouter blocked
MODEL-006 fallback OpenRouter blocked
MODEL-007 paid API blocked
MODEL-008 unknown-cost route blocked
MODEL-009 cost violation quarantines route
MODEL-010 free 429 produces wait/rotation
MODEL-011 circuit breaker
MODEL-012 recovered free route health probe
95. DATABASE TESTS

At minimum:

DB-001 migration
DB-002 idempotent startup
DB-003 rollback/recovery
DB-004 employee persistence
DB-005 Project persistence
DB-006 Run history
DB-007 Review persistence
DB-008 atomic task claim
DB-009 event consistency
DB-010 PostgreSQL beats stale file cache
DB-011 Department CRUD
DB-012 referential integrity
96. ASSET PIPELINE TESTS

At minimum:

ASSET-001 complete inventory
ASSET-002 source hash unchanged
ASSET-003 duplicate grouping
ASSET-004 reference identification
ASSET-005 asset use/provenance map
ASSET-006 canonical character production rig
ASSET-007 required animations
ASSET-008 office environment composition
ASSET-009 furniture perspective consistency
ASSET-010 missing optional asset fallback
ASSET-011 corrupt metadata fallback
ASSET-012 no copyrighted ripped production assets
97. ACCESSIBILITY TESTS

At minimum:

A11Y-001 automated scan
A11Y-002 global keyboard navigation
A11Y-003 Department tabs
A11Y-004 Employee dossier
A11Y-005 Project/Task actions
A11Y-006 visible focus
A11Y-007 dialog focus/escape
A11Y-008 status not color-only
A11Y-009 office equivalent text status
A11Y-010 prefers-reduced-motion
A11Y-011 long content
A11Y-012 dark theme contrast
98. PERFORMANCE TESTS

Measure real results.

At minimum:

PERF-001 route/navigation latency
PERF-002 UI interaction latency
PERF-003 API read latency
PERF-004 full office FPS
PERF-005 20+ Department overview
PERF-006 repeated renderer mount/unmount
PERF-007 large event/history view
PERF-008 irrelevant events do not rerender entire office

Record environment and actual observed values.

99. SECURITY TESTS

At minimum:

SEC-001 no committed secrets
SEC-002 no secrets in worker prompts
SEC-003 no secrets in screenshots/logs
SEC-004 workers do not inherit paid provider keys
SEC-005 workers cannot edit unrelated repos
SEC-006 safe path/file boundaries
SEC-007 server-side permissions
SEC-008 MCP permission audit
SEC-009 task input validation
SEC-010 approval bypass denied
SEC-011 no unnecessary public services
SEC-012 database credential safety
SEC-013 OpenRouter blocked
100. RESILIENCE TESTS

Retain the strong failure-injection philosophy.

Do not infer resilience from retry code.

Actually inject failures.

At minimum:

RES-001 close browser during activ
...[TRUNCATED 2070 chars]...
rning;
Models & Cost;
bots/nameplates;
readable dense layout.
105. VISUAL DEFECT RECORDS

Record:

defect_id
severity
route
viewport
component
observation
expected/reference
screenshot
repair criterion

No unresolved Critical/High visual defects at release.

106. DATA TRUTH

Never fabricate production:

Projects
Tasks
employees active
status
spend
QA
health
progress
activity
model usage
cost

Demo/test fixtures must be isolated and clearly identified.

107. HEALTH / PROGRESS FORMULAS

Any displayed numeric metric must have a definition.

Examples:

Project progress may be:

accepted required leaf Tasks /
all currently required leaf Tasks

QA rate may be:

first-pass accepted reviews /
all reviewed Tasks during defined period

Do not invent visually pleasing numbers.

108. KNOWLEDGE

Support appropriate scopes:

GLOBAL
DEPARTMENT
PROJECT
EMPLOYEE

Knowledge may include:

architecture decisions;
standards;
lessons;
research;
project history.

Operational state does not belong solely in Knowledge/Obsidian.

109. LEARNING

LearningProposal lifecycle:

PROPOSED
REVIEWING
APPROVAL_REQUIRED
APPROVED
ACTIVATED
REJECTED
ROLLED_BACK

Potential changes:

PROMPT
MODEL ROUTING
SKILL
TOOL
WORKFLOW
PROCESS
MEMORY POLICY

Critical self-modification requires review.

110. OBSERVABILITY

The user should be able to inspect:

active CAO sessions;
active Runs;
queued work;
waiting dependencies;
reviews;
retries;
provider failures;
FreeLLMAPI health;
model usage;
cost classification;
recent events;
errors.

Do not require reading raw server logs for ordinary operation.

111. CAO SESSION PROVENANCE

For each Run persist where applicable:

CAO session ID
terminal ID
agent profile
launch time
completion time
outcome

But these are execution references, not durable employee identity.

112. REDUCE CONTEXT WASTE

Do not send the full project history to every worker.

Construct targeted context packets.

A worker should receive:

exact requirements;
relevant architecture;
relevant files;
prior failed Attempt;
acceptance tests.

Raw history stays retrievable.

113. CONCURRENCY

Start conservatively.

Avoid overlapping workers on the same files.

Increase only after proving:

FreeLLMAPI capacity;
Git stability;
DB stability;
CAO stability.

Throughput is accepted work, not worker count.

114. DO NOT RUN HEAVY LOCAL MODELS ON CPU UNNECESSARILY

Previous CAO testing showed severe CPU-model latency.

The VPS should primarily run:

CAO;
application;
Git;
PostgreSQL;
browser tooling;
deterministic scripts.

Use FreeLLMAPI external/free inference where configured instead of accidentally running huge local models on CPU.

115. NO AWS DETOUR

CAO includes AWS/EKS/Bedrock examples upstream.

They are irrelevant.

Do not:

install AWS CLI;
create EKS;
configure Bedrock;
migrate orchestration to Kubernetes.

Use the existing local CAO architecture.

116. BROWSER QA

Use existing browser/Playwright/Hermes tooling where possible.

Do not add another browser stack without a concrete reason.

Major flows require real browser verification.

117. AUTONOMOUS COMMISSIONING

The finished system must prove itself by completing a genuine bounded software task.

Required flow:

user creates Project
    ↓
PostgreSQL persists Project
    ↓
CAO root workflow detects work
    ↓
free planning/decomposition
    ↓
Tasks created
    ↓
FreeLLMAPI implementation workers
    ↓
Runs stored
    ↓
deterministic tests
    ↓
independent review
    ↓
intentional rejection at least once
    ↓
rework
    ↓
acceptance
    ↓
integration
    ↓
Project completion

During the test:

close the browser;
kill one worker;
create one review rejection;
restart CAO;
verify progress/history survives.
118. BURN-IN

After commissioning, run sustained autonomous cycles.

Target approximately 20 meaningful cycles or equivalent coverage.

Include:

ordinary success;
rework;
timeout;
rate limit;
worker death;
CAO restart;
browser close;
dependency;
approval;
multiple Projects;
learning proposal;
free-model rotation;
one subscription escalation if naturally required.

Success requires:

no unexplained stuck work
no duplicate Projects
no lost history
no OpenRouter
no paid API spend
no unexplained data mismatch
no runaway terminal leaks
119. CROSS-MODEL FINAL CHALLENGE

Use FreeLLMAPI independent reviewers first.

Use at least two meaningfully different free models for the final whole-system challenge where available.

Ask them to search for:

scope compression
fake completion
missing requirement
stub functionality
static office pretending to be live
fake metrics
broken persistence
Task/Run collapse
employee/runtime collapse
QA bypass
stale evidence
security issue
accessibility gap
visual underdelivery
asset library ignored
OpenRouter leak
paid route leak
CAO restart failure

If free reviewers disagree materially or cannot reliably judge a release-critical issue, escalate that issue to Sol.

120. SUBSCRIPTION ESCALATION RULE

Codex subscription is backup capacity.

Escalation must record why it was used.

Example:

ESCALATION_REASON:
3 FreeLLMAPI planning attempts failed to produce a coherent migration strategy.

Not:

Sol is better so use Sol.
121. FINAL RELEASE GATE

Create/maintain an executable release gate.

The old "SUPERVISOR" gate is replaced with:

CAO CONTINUATION GATE

The release gate fails unless all mandatory categories pass.

122. RELEASE GATE — SOURCE COVERAGE

Fail if substantive source material remains unexplained/unmapped.

123. RELEASE GATE — REQUIREMENTS

Fail if a mandatory requirement is not verified.

124. RELEASE GATE — ASSETS

Fail if required supplied assets/references were ignored or incorrectly replaced.

125. RELEASE GATE — IMPLEMENTATION

Fail on mandatory stubs/placeholders.

126. RELEASE GATE — PROVENANCE

Fail if AI implementation cannot be traced to authorized routes.

127. RELEASE GATE — BILLING

Fail on unauthorized paid inference.

128. RELEASE GATE — OPENROUTER

Fail if any active route can reach OpenRouter.

129. RELEASE GATE — TESTS

Fail if required automated layer is missing/failing.

130. RELEASE GATE — LIVE RUNTIME

Fail if mandatory operational behaviour exists only in documents/tests.

131. RELEASE GATE — REVIEW

Fail if required independent review is absent, rejected or stale.

132. RELEASE GATE — SECURITY

Fail on unresolved Critical/High security issues.

133. RELEASE GATE — VISUAL

Fail on unresolved Critical/High visual defects.

134. RELEASE GATE — CONSOLE

Fail on unexplained runtime/browser errors on required flows.

135. RELEASE GATE — RESILIENCE

Fail if required failure-injection tests are not proven.

136. RELEASE GATE — CAO CONTINUATION

Fail unless:

CAO root workflow operates;
CAO restarts safely;
incomplete work resumes;
worker death recovers;
no custom heartbeat supervisor is required;
no user continue is required;
empty/incomplete state causes more CAO work;
release failure creates corrective work.
137. RELEASE GATE — POSTGRESQL

Fail unless durable state survives restart and PostgreSQL is authoritative.

138. RELEASE GATE — DOMAIN MODEL

Fail if Organization/Department/Employee/Project/Task/Run/Review are incorrectly collapsed.

139. RELEASE GATE — DATA TRUTH

Fail if production UI knowingly displays fabricated operational data.

140. RELEASE GATE — LIVING OFFICE

Fail if:

office is static rather than state-bound;
employees do not move/animate appropriately;
employee state is inconsistent with backend state;
accessibility alternative absent;
performance unacceptable.
141. RELEASE GATE — PRODUCT UI

Fail if required Organization/Department/Employee/Project/Task/QA/Knowledge/Learning/Model surfaces are missing or placeholders.

142. RELEASE GATE — AUTONOMOUS COMMISSIONING

Fail unless real commissioning passes.

143. RELEASE GATE — BURN-IN

Fail unless burn-in passes.

144. RELEASE GATE — RELEASE IDENTITY

Fail if:

tested SHA
built SHA
deployed SHA

differ without revalidation.

145. RELEASE OUTPUT

Generate:

AI_WORKFORCE_BUILD/FINAL_RELEASE_GATE.json

containing:

timestamp
release_sha
deployed_sha
exitCode
checks[]
blocking_failures[]
evidence_refs
requirement_counts
test_results
visual_results
resilience_results
security_results
model_policy_results

Models may not edit this file to manufacture success.

146. SHIPPED TRANSITION

The gate determines readiness.

When:

FINAL_RELEASE_GATE.exitCode == 0

and there is no unresolved human blocker:

perform the controlled durable transition:

BUILD_STATE.status = SHIPPED

The CAO root workflow may cease scheduling build work only when:

release gate == PASS
AND
BUILD_STATE.status == SHIPPED
147. CURRENT KNOWN BASELINE — REVERIFY

The last known state included:

hundreds of passing tests;
production build passing;
provider safety work completed;
CAO operational;
subscription OAuth verified;
release gate still NOT_READY;
major Organization/Department/Living Office work incomplete.

Do not assume exact historical counts remain current.

Run current baseline.

148. CURRENT P0 PRODUCT FRONTIER

Unless current evidence shows these have since been completed, treat them as P0:

Organization cockpit
Department command centre
Living 2D office
blue/yellow character integration
truthful real-data binding
Department CRUD persistence
remaining mandatory requirements
149. ORGANIZATION WORK DECOMPOSITION

Do not assign entire Organization screen to one worker.

Example bounded tasks:

ORG-01 route/shell
ORG-02 metric queries
ORG-03 metric cards
ORG-04 Department card adapter
ORG-05 Department card UI
ORG-06 mini-office preview
ORG-07 activity panel
ORG-08 models/cost
ORG-09 improvements
ORG-10 New Department
ORG-11 loading/error/empty states
ORG-12 responsiveness
ORG-13 visual QA fixes
150. DEPARTMENT WORK DECOMPOSITION

Example:

DEPT-01 route/shell
DEPT-02 header
DEPT-03 tabs
DEPT-04 status rail
DEPT-05 activity rail
DEPT-06 Active Projects
DEPT-07 Upcoming Work
DEPT-08 Completed Recently
DEPT-09 QA panel
DEPT-10 Knowledge
DEPT-11 Learning
DEPT-12 Models & Cost
DEPT-13 office viewport
DEPT-14 Employee dossier
DEPT-15 responsive polish
151. OFFICE WORK DECOMPOSITION

Example:

OFFICE-01 renderer lifecycle
OFFICE-02 asset loader
OFFICE-03 OfficeLayout schema
OFFICE-04 state adapter
OFFICE-05 canonical character rig
OFFICE-06 expression system
OFFICE-07 animation state machine
OFFICE-08 pathing
OFFICE-09 station targeting
OFFICE-10 indicators/nameplates
OFFICE-11 Employee click interaction
OFFICE-12 handoff visual
OFFICE-13 error/retry states
OFFICE-14 reduced motion
OFFICE-15 mini-office strategy
OFFICE-16 performance
OFFICE-17 visual QA fixes
152. DEVELOPMENT PHASE ORDER

Run the programme in this order, adjusted only for genuine dependencies.

Phase 0 — establish truth
current Git;
current worktrees;
current CAO;
current DB;
current tests;
current release gate.
Phase 1 — remove old supervisor architecture
reconcile sessions;
disable old supervisor;
remove production dependencies on it.
Phase 2 — prove CAO-native continuation
root workflow;
scheduling;
persistence/restart;
several cycles without human.
Phase 3 — provider policy
FreeLLMAPI;
subscription fallbacks;
no OpenRouter;
zero paid API.
Phase 4 — PostgreSQL authority
migrations;
CRUD;
durable state.
Phase 5 — source/asset inventory
inventory;
hashes;
provenance;
asset-use map.
Phase 6 — requirements reconciliation
Pass A;
Pass B;
reconciliation.
Phase 7 — worktree consolidation
recover existing good work.
Phase 8 — architecture contracts
canonical domain/state/event/API contracts.
Phase 9 — core domain/runtime
persistent entities;
Projects/Tasks/Runs/Reviews.
Phase 10 — Organization UI
full contract.
Phase 11 — Department Cockpit
full contract.
Phase 12 — remaining product surfaces
Projects;
Tasks;
Agents;
QA;
Knowledge;
Learning;
History;
Models & Cost;
Settings.
Phase 13 — character/asset production
character rig;
office;
furniture;
atlases.
Phase 14 — living office
state;
movement;
interaction.
Phase 15 — observability/learning
telemetry;
model performance;
learning.
Phase 16 — security/accessibility/performance
hardening.
Phase 17 — full regression
Phase 18 — visual QA
Phase 19 — resilience
Phase 20 — autonomous commissioning
Phase 21 — burn-in
Phase 22 — final source reconciliation
Phase 23 — final independent review
Phase 24 — deterministic release gate

If gate fails:

create work
dispatch through CAO
continue
153. FIRST CONTINUATION PROOF BEFORE LARGE BUILD

Before spending hours on new UI, prove CAO itself can keep the programme going.

Run at least three consecutive cycles:

cycle 1:
FreeLLMAPI worker implementation
→ result
→ review
→ integration

cycle 2:
new work automatically scheduled
→ worker
→ result
→ review

restart CAO

cycle 3:
workflow reconstructs
→ work continues

No user message between cycles.

No custom supervisor.

Only after this passes is the new architecture considered commissioned.

154. IF CAO ITSELF FAILS

systemd may restart empirium-cao.service.

After restart:

root workflow must be resumable/re-created idempotently;
PostgreSQL tells it what remains;
existing Runs are reconciled;
stale terminals cleaned up;
new work assigned where necessary.

No project loss.

155. HUMAN BLOCKER FORMAT

Only surface a human blocker if absolutely necessary.

Use:

BLOCKER:
<exact issue>

WHY HUMAN REQUIRED:
<why CAO/free models/tools cannot solve it>

ATTEMPTS:
<what was tried>

EVIDENCE:
<exact paths/errors>

MINIMUM USER ACTION:
<smallest action>

WORK CONTINUING:
<unrelated work still running>
156. DO NOT STOP FOR THESE

Do not stop the programme because of:

FreeLLMAPI 429
one worker timeout
bad implementation
failed test
review rejection
merge conflict
CAO terminal exit
free manager failure
visual defect
provider outage
context exhaustion
browser closure
application restart
CAO restart
missing optional art

Recover.

157. DO NOT BUILD AN MVP INSTEAD

Forbidden completion statements include:

MVP complete
core complete
mostly complete
functionally complete
good enough
release candidate
essentially done

unless the deterministic gate has actually passed.

158. DO NOT SUBSTITUTE ARCHITECTURE FOR PRODUCT

These are not completion:

interfaces;
schemas;
documentation;
ADRs;
mockups;
agent definitions;
test plans;
a beautiful static office;
placeholder API.

Required functionality must actually run.

159. DO NOT SUBSTITUTE TESTS FOR USER EXPERIENCE

Passing tests do not prove:

visual quality;
correct information density;
smooth office movement;
premium polish;
intuitive interaction.

Use real browser QA.

160. DO NOT SUBSTITUTE SCREENSHOTS FOR BACKEND TRUTH

A screenshot that looks correct while values are fake is a failure.

UI must project real backend state.

161. DO NOT SUBSTITUTE ANIMATION FOR REAL WORK

Bot typing does not mean Task is executing.

Animation derives from actual canonical Run/Task state.

162. DO NOT MODIFY EMPIRIUM OS

Empirium Studio is separate.

Do not re-embed the workforce into Empirium OS.

Empirium OS may later become a Project serviced by Personal Software.

163. DO NOT REPLACE CAO

Do not introduce:

LangGraph;
CrewAI;
LangFlow;
Agent Zero;
OpenHands;
another orchestrator;

as the programme orchestrator.

CAO is the orchestrator.

Other repositories may only be used as donor/reference code for narrow functionality if justified.

164. DO NOT REINTRODUCE THE SUPERVISOR

This is a hard V6 invariant.

If an old file or old prompt says:

install supervisor
restart supervisor
heartbeat supervisor
Meta Luna supervisor
supervisor liveness gate

that instruction is superseded.

Translate the desired resilience behaviour into:

CAO workflow persistence
CAO scheduling
PostgreSQL durable state
systemd CAO service restart
Task/Run reconciliation

Do not revive the failed design.

165. FINAL USER EXPERIENCE

The project is genuinely complete when the user can:

open Empirium Studio;
see a rich Organization Overview;
see real Departments represented by mini offices;
open Personal Software;
see a command-centre Department view;
see persistent blue/yellow employees moving in a living office;
click employees and inspect them;
create a software Project;
close the browser;
allow CAO to continue the Project;
have FreeLLMAPI perform planning and implementation;
have failures automatically retried/rebriefed;
have work independently reviewed;
see rework happen automatically;
restart CAO and retain the programme;
return later and inspect everything that happened;
see truthful Tasks/Runs/reviews/evidence/model usage;
complete the Project without typing continue;
pass all release gates.
166. FINAL MACHINE STATE

When shipped, produce a machine-readable summary:

STATUS=SHIPPED

SOURCE_REPO=
SOURCE_BRANCH=
SOURCE_SHA=
DEPLOYED_SHA=
DB_MIGRATION=

CAO_ORCHESTRATION=PASS
CUSTOM_HEARTBEAT_SUPERVISOR=ABSENT

POSTGRES_AUTHORITY=PASS
FREELLMAPI_PRIMARY=PASS
CODEX_USAGE=BACKUP_ONLY
OPENROUTER_REACHABLE=false
PAID_API_SPEND=0

REQUIREMENTS_TOTAL=
REQUIREMENTS_VERIFIED=
MANDATORY_UNVERIFIED=0

UNIT_TESTS=
INTEGRATION_TESTS=
E2E_TESTS=
RESILIENCE_TESTS=

ORGANIZATION_UI=PASS
DEPARTMENT_UI=PASS
LIVING_OFFICE=PASS
BLUE_YELLOW_CHARACTER_SYSTEM=PASS
EMPLOYEE_DOSSIER=PASS
PROJECT_TASK_RUN_MODEL=PASS
QA_REWORK=PASS
KNOWLEDGE_LEARNING=PASS
MODEL_TELEMETRY=PASS

CAO_RESTART_RECOVERY=PASS
WORKER_DEATH_RECOVERY=PASS
PROVIDER_FAILURE_RECOVERY=PASS
BROWSER_CLOSE_CONTINUATION=PASS
AUTONOMOUS_COMMISSIONING=PASS
BURN_IN=PASS

SECURITY_BLOCKERS=0
HIGH_VISUAL_DEFECTS=0

FINAL_RELEASE_GATE=PASS

Use real values only.

167. INITIAL ACTIONS — DO THESE NOW

Do not answer this prompt with a plan.

Begin execution.

Inspect current Git/worktrees/services/PostgreSQL/CAO state.
Reconcile any orphan/duplicate sessions created by the previous supervisor experiment.
Safely remove empirium-workforce-supervisor.service from the production execution path.
Verify CAO is the only orchestration plane.
Establish/verify the root CAO completion workflow.
Verify workflow persistence/recovery.
Verify FreeLLMAPI primary manager/worker/reviewer routes.
Verify Luna/Sol subscription backups without paid API credentials.
Technically block OpenRouter.
Verify zero pay-as-you-go policy.
Prove three unattended CAO cycles.
Verify/fix PostgreSQL authority.
Inventory the entire "/home/ash/Desktop/AI Taskforce" asset/source package.
Preserve original hashes.
Reconcile existing requirements.
Reconcile existing worktrees.
Run baseline tests/build/browser checks.
Continue from the actual P0 implementation frontier.
Finish Organization.
Finish Department Cockpit.
Finish Living Office.
Finish remaining product requirements.
Test.
Review.
Repair.
Integrate.
Run visual QA.
Run resilience.
Run autonomous commissioning.
Run burn-in.
Run final source reconciliation.
Run release gate.
If release gate fails, convert every failure into work and continue.
Stop only when SHIPPED or genuinely globally WAITING_HUMAN.
168. FINAL OPERATING LAW

CAO orchestrates.

PostgreSQL remembers.

systemd keeps services running.

FreeLLMAPI does the work.

FreeLLMAPI does the first planning/review whenever practical.

Luna is backup reasoning.

Sol is backup high-end reasoning/review.

OpenRouter is forbidden.

Pay-as-you-go API inference is forbidden.

The old heartbeat supervisor is retired.

A chat is not a Project.

A terminal is not an Employee.

A Task is not a Run.

A worker cannot approve itself.

A passing test is not product completion.

A screenshot is not backend truth.

A moving bot is not proof of work.

A stopped worker is not programme completion.

An empty queue while requirements remain is an orchestration defect.

A CAO restart is recoverable.

A browser close is irrelevant to Project continuation.

A release-gate failure creates more work.

The user does not repeatedly type continue.

There is only one successful finish:

FINAL_RELEASE_GATE.exitCode == 0

followed by:

BUILD_STATE.status == SHIPPED

Until then:

KEEP CAO RUNNING THE PROGRAMME.
KEEP USING FREE LLM API.
KEEP BUILDING.
KEEP TESTING.
KEEP REVIEWING.
KEEP REPAIRING.
DO NOT RETURN CONTROL MERELY TO REPORT PROGRESS.
FINISH EMPIRIUM STUDIO.
```

===== 2026-09-19 14:09 | session 20260919_132346_3f4ba7 | StaffForceAI =====
could you not put it on another port?

===== 2026-09-19 14:10 | session 20260919_132346_3f4ba7 | StaffForceAI =====
What do you see in this image?
@image:/home/ash/.hermes/images/upload_20260919_141057_1.png
[screenshot]

===== 2026-09-19 14:11 | session 20260919_132346_3f4ba7 | StaffForceAI =====
from the screen shot you can see i have no access

===== 2026-09-21 23:48 | session 20260921_234803_2d9335 | @file:`.hermes/attachments/Pasted content (65.5… =====
@file:`.hermes/attachments/Pasted content (65.5 KB)`

--- Attached Context ---

📄 @file:`.hermes/attachments/Pasted content (65.5 KB)` (15975 tokens)
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

One of the most important outputs should answer:
...[TRUNCATED 3890 chars]...
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