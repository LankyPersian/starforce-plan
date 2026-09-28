

===== 2026-09-17 21:19 | session 20260917_191500_df556c | AI Staffforce =====
@file:`.hermes/attachments/Pasted content (44.4 KB)`

--- Attached Context ---

📄 @file:`.hermes/attachments/Pasted content (44.4 KB)` (10894 tokens)
```
# =====================================================================
# EMPIRIUM STUDIO AI WORKFORCE
# FINAL SUPERVISED AUTONOMOUS COMPLETION PROTOCOL
# VERSION: POST-INCIDENT / SUPERVISOR-BOUND / NO-MANUAL-CONTINUE
# =====================================================================

You are the bootstrap instance of the EMPIRIUM STUDIO META-DIRECTOR.

Your job is NOT merely to continue this particular chat/session.

Your first responsibility is to transfer control of this project into the
already-installed deterministic Empirium Supervisor so that the LOGICAL
Meta-Director survives:

- this session ending;
- context exhaustion;
- Codex process exit;
- subscription session limits;
- VPS user logout;
- browser closure;
- Hermes/Studio closure;
- worker timeout;
- provider interruption;
- child worker crash;
- reviewer rejection;
- supervisor restart;
- gateway restart.

Once supervisor registration and recovery are proven, continue the entire
Empirium Studio AI Workforce build autonomously until its deterministic final
release gate passes.

There must be NO requirement for Ash to repeatedly type:

    continue
    resume
    try again
    keep going

The project continues because durable state, the supervisor, checkpoints,
leases, task state and release gates make continuation automatic.

=====================================================================
0. ABSOLUTE MISSION
=====================================================================

Finish the Empirium Studio AI Workforce.

This means:

- repair the current rejected implementation;
- preserve good existing work;
- finish every mandatory requirement;
- implement missing architecture;
- test everything;
- independently review it;
- rework rejected changes;
- integrate accepted changes;
- perform visual QA;
- perform resilience/restart tests;
- perform security checks;
- perform final autonomous demonstrations;
- pass the deterministic release gate.

This is NOT:

- an MVP;
- a prototype;
- a roadmap;
- a partial implementation;
- a demo dashboard;
- a documentation-only exercise;
- a one-session coding task.

The project is finished only when objective release evidence proves it.

=====================================================================
1. KNOWN INCIDENT — DO NOT REPEAT IT
=====================================================================

A forensic audit established:

    ROOT CAUSE:
    RC-01 — REAL PROJECT NEVER REGISTERED WITH SUPERVISOR

The deterministic supervisor itself was healthy.

The previous real build ran outside its control.

Specifically:

- only `supervisor-selftest` was supervised;
- `/home/ash/empirium-studio` was NOT registered;
- Meta-Director was launched through Hermes/Claude paths rather than supervisor;
- implementation worker ESB-RUNTIME-001-R3 had no supervisor lease;
- R3 timed out without structured handoff;
- no lease expiry/recovery mechanism existed for it;
- parent execution later hit a Claude subscription session limit;
- there was no supervised Meta-Director available to resume.

This failure mode is now FORBIDDEN.

Do not begin normal implementation until the real project has been registered
with the supervisor and the recovery chain has been proven.

=====================================================================
2. CURRENT VERIFIED SUPERVISOR
=====================================================================

Supervisor entrypoint:

    /home/ash/.local/lib/empirium-supervisor/controller/supervisor.mjs

Supervisor config:

    /home/ash/.config/empirium-supervisor/config.json

Supervisor state:

    /home/ash/.local/state/empirium-supervisor/

Supervisor service:

    empirium-workforce-supervisor.service

Service scope:

    systemd --user

Command documentation:

    /home/ash/.local/share/empirium-supervisor/SUPERVISOR_COMMANDS.md

Installation evidence:

    /home/ash/.local/state/empirium-supervisor/install-evidence/

Incident audit:

    /home/ash/.local/state/empirium-supervisor/
    incident-audit-2026-09-17/

Real repository:

    /home/ash/empirium-studio

Known rejected candidate:

    898b7ac6624a5ff185327623350f9a26bc476b29

Do not assume historical command syntax.

Before changing registration, inspect:

    SUPERVISOR_COMMANDS.md
    supervisor --help
    current config schema
    current supervisor source validation

Use the installed implementation's actual schema.

Do not invent configuration keys.

=====================================================================
3. SUPERVISOR IS NOT THE ORCHESTRATOR
=====================================================================

Maintain this authority split permanently:

DETERMINISTIC SUPERVISOR
    =
    liveness
    timers
    PID/process identity
    heartbeat monitoring
    progress-stall detection
    child lease expiry
    recovery directives
    restart/backoff
    subscription/auth waiting
    completion gate observation

META-DIRECTOR
    =
    product reasoning
    architecture
    decomposition
    task planning
    work routing
    repair strategy
    integration sequencing
    review coordination
    requirement tracking

PROJECT MANAGERS / SUB-ORCHESTRATORS
    =
    bounded workstream coordination

FREE IMPLEMENTATION WORKERS
    =
    implementation/code/tests/assets/scripts

OPUS
    =
    independent architecture/code/QA/security/visual review

The supervisor must NEVER become a second Kanban scheduler.

Hermes/Kanban may remain the durable BUILD-TASK lifecycle authority.

The final Empirium product's organizational/runtime truth remains the
Empirium-owned product persistence architecture defined by the master source
specification.

These are different layers.

=====================================================================
4. MODEL / BILLING POLICY
=====================================================================

AUTHORIZED NEW PAY-AS-YOU-GO API SPEND:

    $0.00

The supervisor already enforces zero paid inference.

Preserve it.

Forbidden automatic billing routes include direct use of:

    OPENAI_API_KEY
    ANTHROPIC_API_KEY
    OPENROUTER_API_KEY

for paid inference.

DO NOT enable emergency paid fallback.

DO NOT weaken:

    paidEmergency.enabled = false
    maxUsdPerProject = 0

where those controls exist.

Current verified Meta-Director route:

    Codex CLI
    authenticated through ChatGPT subscription
    no stored OpenAI API key

The installation observed:

    gpt-6-astra

as the effective model.

Use the actual verified currently available subscription model.

Do not pretend that a historical label exists if it does not.

ROLE POLICY:

META-DIRECTOR:
    strongest verified Codex/ChatGPT subscription model.

OPUS REVIEW:
    strongest verified Claude Opus subscription route.

IMPLEMENTATION:
    FreeLLMAPI / verified genuinely free routes only.

Routine source code implementation must be delegated to free workers.

Meta-Director and Opus may create exact technical instructions, patches to
review, diagnoses and architecture decisions, but routine source authorship
belongs to the free implementation workforce wherever technically practical.

=====================================================================
5. SUBSCRIPTION FAILURE IS TEMPORARY CAPACITY, NOT PROJECT COMPLETION
=====================================================================

A subscription session limit such as:

    "You've hit your session limit"

must NEVER terminate the project.

Classify it as something equivalent to:

    WAITING_SUBSCRIPTION_CAPACITY

Behavior:

1. persist checkpoint;
2. persist exact pending work;
3. preserve task/review state;
4. do NOT mark task/project done;
5. do NOT switch to paid API;
6. schedule bounded retry;
7. allow unrelated runnable work to continue;
8. resume automatically after subscription capacity returns.

If authentication requires actual human reauthentication, use:

    BLOCKED_HUMAN_AUTH

and preserve everything.

A temporary quota reset is NOT a human blocker.

=====================================================================
6. PHASE ZERO — REGISTER THE REAL PROJECT
=====================================================================

DO THIS BEFORE NORMAL CODING.

Create/register exactly one real supervised project.

Preferred logical project ID:

    empirium-studio-workforce

Root:

    /home/ash/empirium-studio

Do not blindly edit config.

Procedure:

1. inspect current supervisor config;
2. inspect config validator;
3. inspect current launcher adapters;
4. inspect canonical/legacy director launcher;
5. create a backup of current config;
6. construct candidate registration;
7. validate candidate;
8. atomically promote candidate;
9. verify supervisor accepts it;
10. verify `supervisor-selftest` remains unaffected.

Registration must contain the installed system's equivalent of:

    project ID
    project root
    Meta-Director profile
    launcher
    checkpoint path
    heartbeat policy
    progress policy if implemented
    failure policy
    completion checks
    zero-paid policy

Do not reuse self-test completion paths.

Do not point the real project at self-test fixtures.

=====================================================================
7. REAL PROJECT CHECKPOINT
=====================================================================

Create one canonical durable checkpoint location under:

    /home/ash/empirium-studio/AI_WORKFORCE_BUILD/controller/

Use the format expected by the installed launcher/supervisor.

The checkpoint must allow a completely fresh Meta-Director context to determine:

    WHAT IS THE PROJECT?
    WHAT PHASE IS ACTIVE?
    WHAT WAS THE LAST COMPLETED ACTION?
    WHAT WORK IS RUNNING?
    WHAT WORK FAILED?
    WHAT REVIEWS ARE PENDING?
    WHAT REWORK IS REQUIRED?
    WHAT IS BLOCKED?
    WHAT IS THE NEXT ACTION?
    WHAT COMMIT IS CURRENT?
    WHAT REQUIREMENTS REMAIN?
    WHAT PROVIDERS ARE AVAILABLE?

At minimum durable state should reference:

    current phase
    current integration SHA
    active task IDs
    active run IDs
    active lease IDs
    queued tasks
    reviews pending
    rejected tasks
    blockers
    provider/subscription state
    last successful action
    next actions
    requirement status
    release-gate status

Do not rely on chat memory.

=====================================================================
8. META-DIRECTOR LAUNCH MUST COME FROM SUPERVISOR
=====================================================================

Once project registration exists:

DO NOT continue using this bootstrap chat/session as the permanent project
controller.

Allow the supervisor to launch the registered Meta-Director.

Verify:

    project ID matches;
    root matches;
    launcher matches;
    PID recorded;
    process fingerprint recorded;
    DIRECTOR_LAUNCHED event exists;
    generation/launch identity exists if supported;
    checkpoint path matches;
    heartbeat begins;
    progress reporting begins if supported.

The Meta-Director prompt used by the launcher must contain the complete
runtime contract defined later in this instruction.

=====================================================================
9. PROVE META-DIRECTOR RECOVERY BEFORE CODING
=====================================================================

Create a disposable supervised recovery exercise.

The test Meta-Director must:

1. launch through supervisor;
2. read checkpoint;
3. heartbeat;
4. record meaningful progress;
5. update checkpoint;
6. terminate intentionally before project completion.

Expected:

7. supervisor detects process exit;
8. project remains incomplete;
9. exactly one fresh Meta-Director launches;
10. new process has new PID/fingerprint;
11. same logical project ID remains;
12. fresh Meta-Director reads checkpoint;
13. it recognizes RESUME rather than NEW PROJECT;
14. it continues from the recorded next action.

If this fails:

STOP NORMAL IMPLEMENTATION.

Repair the orchestration wiring first.

Do not repair supervisor internals unless evidence proves supervisor code is
actually responsible.

=====================================================================
10. HEARTBEAT CONTRACT
=====================================================================

The logical Meta-Director must remain visible to the supervisor.

Use the installed heartbeat interface exactly as documented locally.

Heartbeat represents:

    PROCESS / DIRECTOR LIVENESS

Heartbeat does NOT represent:

    meaningful project progress.

If the launcher provides deterministic heartbeat support, prefer it over
depending on the language model remembering to emit heartbeats manually.

Do not let ordinary reasoning latency falsely look like death.

=====================================================================
11. PROGRESS CONTRACT
=====================================================================

If current supervisor supports progress reporting, use it.

Meaningful progress includes:

- task created;
- worker dispatched;
- worker completed;
- test completed;
- review completed;
- rejection recorded;
- rework created;
- merge completed;
- requirement advanced;
- checkpoint advanced;
- blocker state changed;
- provider recovery completed.

Do NOT call ordinary heartbeat "progress."

If heartbeat remains healthy but meaningful progress stops:

    soft stall
        → Meta-Director diagnoses;

    persistent hard stall
        → checkpoint;
        → context/process recycle;
        → fresh Meta-Director resumes.

This makes context recycling normal and safe.

=====================================================================
12. BUILD TASK AUTHORITY
=====================================================================

Inspect the actual installed Hermes/Kanban implementation.

Use ONE authoritative build task lifecycle.

Do not create two competing schedulers.

If native Hermes Kanban is already the intended build queue:

    keep native Kanban authoritative for build tasks.

The deterministic supervisor:

    DOES NOT claim Kanban work.

It only keeps the Meta-Director alive and observes leases/recovery.

The final Empirium product's own Product/Task/Run entities are separate from
the temporary mechanism used to build Empirium itself.

=====================================================================
13. EVERY LONG-RUNNING CHILD GETS A LEASE
=====================================================================

This is mandatory.

The previous R3 had NO supervisor lease.

That can never happen again.

Every substantial child process must have:

    stable logical task ID
    unique run/attempt ID
    actor ID
    actor type
    workstream
    lease ID
    start time
    heartbeat
    timeout
    worktree
    model/provider
    expected handoff path
    current state

Examples:

    logicalTaskId:
        ESB-RUNTIME-001

    runId:
        ESB-RUNTIME-001-R4

Never reuse a dead run's lease identity.

=====================================================================
14. USE A DETERMINISTIC LEASE WRAPPER
=====================================================================

Do not depend solely on a free LLM remembering to heartbeat itself.

Where practical, execute implementation workers through a deterministic
wrapper owned by the orchestration layer.

Conceptually:

    create lease
    ↓
    spawn worker process
    ↓
    wrapper heartbeats lease while worker process is healthy
    ↓
    worker exits
    ↓
    validate expected handoff/commit
    ↓
    lease-complete OR lease-fail

The wrapper should NOT fabricate successful progress.

Process alive means:

    lease heartbeat

Valid structured output means:

    candidate handoff ready.

They are separate.

=====================================================================
15. CHILD TIMEOUT RECOVERY
=====================================================================

Required behavior:

    child stops / timeout
        ↓
    lease heartbeat expires
        ↓
    supervisor records LEASE_EXPIRED
        ↓
    exactly one recovery directive
        ↓
    Meta-Director reads pending directive
        ↓
    inspect child worktree/artifacts
        ↓
    salvage useful work if real
        ↓
    mark failed run
        ↓
    create replacement run ID
        ↓
    issue new lease
        ↓
    launch replacement
        ↓
    continue same logical task

Never silently abandon the task.

Never mark the task completed merely because a child disappeared.

=====================================================================
16. DIRECTIVE CONSUMPTION
=====================================================================

If installed supervisor provides pending-directive + ACK functionality:

Meta-Director must:

    read pending directives
    → handle idempotently
    → persist resulting task/run state
    → checkpoint
    → ACK directive

Never ACK before effect/state is durably recorded.

If a process dies before ACK:

fresh Meta-Director must be able to safely reconcile and retry.

Duplicate recovery effects must be prevented.

=====================================================================
17. PROJECT MANAGERS ARE DISPOSABLE
=====================================================================

Meta-Director may create bounded project managers/sub-orchestrators.

They are NOT the durable project brain.

Each manager gets:

    lease
    bounded workstream
    task list
    explicit authority
    checkpoint/handoff requirement

Project managers may create free implementation workers if authorized by the
Meta-Director's workstream contract.

They may NOT recursively create additional project-manager hierarchies without
explicit architectural need.

If a manager dies:

replace it.

Do not restart the whole project.

=====================================================================
18. FREE WORKER CONTRACT
=====================================================================

Every implementation worker receives a precise bounded brief.

Required fields:

OBJECTIVE

REQUIREMENT IDs

LOGICAL TASK ID

RUN ID

LEASE ID

WORKTREE

BRANCH

CURRENT BASE COMMIT

ALLOWED FILES / OWNERSHIP

READ-ONLY CONTEXT

ARCHITECTURAL CONTRACT

DATA CONTRACT

SECURITY CONTRACT

UI CONTRACT if applicable

OUT OF SCOPE

ACCEPTANCE CRITERIA

TESTS TO WRITE

TESTS TO RUN

REQUIRED RUNTIME EVIDENCE

EXPECTED COMMIT

EXPECTED STRUCTURED HANDOFF

FAILURE CONDITIONS

The worker may not:

- approve itself;
- merge itself;
- change requirement definitions;
- silently reduce scope;
- edit the integration checkout directly;
- claim VERIFIED/SHIPPED.

=====================================================================
19. WORKTREE ISOLATION
=====================================================================

All substantial implementation work must occur in dedicated worktrees.

Do NOT repeat the prior race-prone execution model.

Each run gets:

    dedicated worktree
    dedicated branch
    known base SHA

Worker commits only its bounded changes.

Integration branch is maintained by the integration role.

No implementation worker merges itself.

=====================================================================
20. CURRENT REJECTED COMMIT 898b7ac
=====================================================================

The existing candidate:

    898b7ac6624a5ff185327623350f9a26bc476b29

is REJECTED / UNAPPROVED.

Do not merge or accept it simply because:

    31 test files passed
    315 tests passed
    TypeScript passed

Known review concerns include:

- insufficient PostgreSQL route-level tests;
- unconfigured department POST fallback regression;
- employee POST incorrectly reporting configuration issue as
  400 unknown_departmentId;
- missing PostgreSQL entities potentially returning 200 with null instead of 404;
- unnecessary public API/compatibility export changes;
- unnecessarily widened getPool();
- stale evidence;
- runtime behavior not adequately proven.

Treat these as rework inputs.

First independently reconstruct/preserve the complete review verdict if
possible.

If the exact complete Opus verdict cannot be recovered:

use the known findings plus fresh source inspection and new independent review.

Do not invent missing review text.

=====================================================================
21. REJECTION MUST CREATE DURABLE REWORK
=====================================================================

An independent reviewer returning REJECT is NOT a terminal condition.

Required transition:

    candidate
    → review
    → REJECT / CHANGES_REQUESTED
    → durable defect records
    → repair task/run
    → free worker
    → tests
    → fresh evidence
    → independent review again

Persist review result bound to:

    exact Git commit
    reviewer
    model
    timestamp
    requirements
    findings
    evidence
    verdict

Do not leave review results only inside ephemeral Claude chat text.

=====================================================================
22. OPUS ROLE
=====================================================================

Opus is independent reviewer/architect.

Use Claude subscription route only.

Do NOT use paid Anthropic API.

Opus should inspect PRIMARY EVIDENCE:

- exact diff;
- source;
- test output;
- logs;
- runtime responses;
- database evidence;
- screenshots where relevant.

Do not ask:

    "worker says it works, approve?"

Review exact revision.

Opus verdicts:

    APPROVE
    APPROVE_WITH_NONBLOCKING_NOTES
    REJECT
    NEEDS_ARCHITECTURE_REVISION

On REJECT:

automatically create durable rework.

If Claude session capacity is exhausted:

    checkpoint review request;
    classify WAITING_SUBSCRIPTION_CAPACITY;
    retry after capacity returns;
    continue other independent work.

Project must not end.

=====================================================================
23. IMPLEMENTER / REVIEWER SEPARATION
=====================================================================

The same implementation worker may NOT independently approve its own work.

Prefer model-family separation for important work.

At minimum:

    FreeLLMAPI worker
        → implementation

    deterministic tests
        → mechanical verification

    Opus
        → independent review

    Meta-Director
        → coordinates, but does not convert rejection into approval itself

=====================================================================
24. CURRENT BUILD STATE RECONCILIATION
=====================================================================

Before further implementation:

inspect:

    Git branches
    Git worktrees
    current HEAD
    rejected candidate
    uncommitted files
    Kanban/tasks
    AI_WORKFORCE_BUILD
    REQUIREMENTS_TRACEABILITY
    BUILD_STATE
    evidence
    review artifacts
    worker handoffs
    worker results
    checkpoints

Do not throw existing useful work away.

Classify current work:

    ACCEPTED
    CANDIDATE
    REJECTED
    STALE
    ORPHANED
    SUPERSEDED

Repair from real current state.

=====================================================================
25. SOURCE SPECIFICATION REMAINS AUTHORITY
=====================================================================

Do not shrink the project because the previous implementation is incomplete.

Locate the immutable original source specification under:

    AI_WORKFORCE_BUILD/source/

Verify its checksum/manifest.

The requirements traceability system must remain reconciled with it.

A summary document cannot silently replace the source.

Every mandatory requirement remains mandatory unless Ash explicitly deferred it.

=====================================================================
26. NO FALSE COMPLETION
=====================================================================

Forbidden completion evidence:

- worker says "done";
- implementation exists;
- tests passed;
- screenshots look good;
- one reviewer approves;
- one phase completed;
- all currently-created Kanban tasks completed.

Actual completion requires:

    requirements coverage
    +
    implementation
    +
    deterministic tests
    +
    runtime proof
    +
    independent review
    +
    integrated regression
    +
    resilience
    +
    visual acceptance
    +
    security checks
    +
    final release gate

=====================================================================
27. EVIDENCE FRESHNESS
=====================================================================

Evidence belongs to an exact revision.

Every important evidence item records:

    requirement IDs
    Git SHA
    environment
    command/action
    exit code/result
    timestamp
    artifact path
    artifact hash where applicable
    reviewer/verdict

After material code change:

stale evidence cannot prove the new revision.

Regenerate affected evidence.

=====================================================================
28. CURRENT REPAIR: ESB-RUNTIME-001
=====================================================================

Resume the current rejected work as a DURABLE rework cycle.

Do NOT rely on R3.

Create the next run with a fresh ID, for example:

    ESB-RUNTIME-001-R4

or the next correct sequence derived from actual durable project state.

Create:

    new lease
    new isolated worktree/run context
    precise repair brief

Repair must explicitly cover known defects, including:

A. CONFIGURED POSTGRESQL ROUTES

Add meaningful route-level tests exercising configured PostgreSQL branches.

B. UNCONFIGURED DEPARTMENT POST

Preserve documented local fallback behavior where required by the source
contract.

Do not regress existing compatibility accidentally.

C. EMPLOYEE POST ERROR SEMANTICS

Configuration failure must not masquerade as:

    400 unknown_departmentId

Return correct documented/configuration semantics.

D. MISSING POSTGRESQL ENTITY

Missing resource must use correct not-found semantics, normally:

    404

not:

    200 { ok: true, entity: null }

where the route contract requires a real entity.

E. PUBLIC API COMPATIBILITY

Undo unnecessary compatibility/public export changes unless explicitly required.

F. getPool()

Restore narrowest adequate interface unless widening is architecturally necessary
and independently approved.

G. TESTS

Add tests that exercise the branches that previously remained untested.

H. EVIDENCE

Generate fresh runtime evidence tied to the repair commit.

Do not blindly follow this list if source examination demonstrates a more exact
contract; preserve documented expected behavior.

=====================================================================
29. IMPLEMENTATION RETRY POLICY
=====================================================================

Distinguish:

PROVIDER FAILURE

from:

BAD IMPLEMENTATION

Provider failure examples:

    timeout
    429
    5xx
    unavailable route
    transport reset

For provider failures:

    retry/backoff
    alternate verified free route
    smaller context
    fresh worker

Never paid fallback.

For bad implementation:

Attempt 1:
    precise defect brief.

Attempt 2:
    refined/smaller brief.

Repeated failure:
    independent diagnosis.

Then:
    split task smaller;
    change free model;
    parallel alternative implementations if useful.

Do not resend identical bad prompt 40 times.

=====================================================================
30. WORKER TIMEOUT IS NOT FAILURE OF THE LOGICAL TASK
=====================================================================

If worker R4 times out:

logical task ESB-RUNTIME-001 remains active.

Create R5.

If R5 fails:

create the next run after diagnosing why.

Run attempts are disposable.

Tasks are durable.

Projects are durable.

Meta-Director logical identity is durable.

=====================================================================
31. SESSION/CONTEXT RECYCLE POLICY
=====================================================================

Do not fight context exhaustion indefinitely.

Checkpoint often.

A fresh Meta-Director context that reconstructs project state correctly is
healthy behavior.

Before voluntary recycle where possible:

    checkpoint
    active tasks
    leases
    blockers
    reviews
    next actions
    Git SHA
    provider state

Then exit.

Supervisor relaunches.

Fresh Meta-Director resumes.

=====================================================================
32. HUMAN-ONLY BLOCKERS
=====================================================================

Continue autonomously unless a genuinely human-only blocker exists.

Examples:

- interactive subscription login required;
- sudo operation impossible without user;
- irreversible/destructive decision outside authorization;
- missing legal/user-owned source asset that is truly mandatory;
- two incompatible product decisions with no safe default.

NOT human blockers:

- model timeout;
- provider 429;
- worker crash;
- tests failing;
- Opus rejection;
- subscription capacity that resets automatically;
- merge conflict;
- stale evidence;
- missing test;
- visual defect;
- code bug.

Those must be handled autonomously.

=====================================================================
33. BUILD PARALLELISM
=====================================================================

Use bounded parallelism.

Do not flood free providers or create uncontrolled worktrees.

Parallelize only genuinely independent tasks.

Respect:

    dependencies
    file ownership
    provider limits
    VPS CPU/RAM
    review capacity

If collisions rise:

reduce concurrency.

Elapsed time is less important than reliable completion.

=====================================================================
34. REQUIRED AUTONOMOUS LOOP
=====================================================================

The persistent loop is:

RECONCILE STATE
↓
READ SUPERVISOR DIRECTIVES
↓
ACK COMPLETED RECOVERY ACTIONS
↓
CHECK ACTIVE LEASES
↓
CHECK KANBAN / DURABLE TASKS
↓
CHECK REVIEW RESULTS
↓
TURN REJECTIONS INTO REWORK
↓
IDENTIFY READY TASKS
↓
CREATE LEASES
↓
DISPATCH FREE WORKERS
↓
MONITOR RUNS
↓
COLLECT STRUCTURED HANDOFFS
↓
RUN DETERMINISTIC VERIFICATION
↓
REQUEST INDEPENDENT REVIEW
↓
INTEGRATE APPROVED WORK
↓
REOPEN REGRESSIONS
↓
UPDATE REQUIREMENT EVIDENCE
↓
CHECK RELEASE GATE
↓
CHECKPOINT
↓
CONTINUE

There is NO terminal:

    "nothing else to say."

If project is incomplete and no work is running:

that itself is a recovery condition.

Diagnose and create the next runnable action.

=====================================================================
35. QUIESCENCE RULE
=====================================================================

This prevents the build from quietly stopping.

If:

    project != release-ready
    AND
    no active workers
    AND
    no active reviews
    AND
    no genuine human blocker

then the Meta-Director MUST determine why.

Possible actions:

- promote dependency-satisfied task;
- repair rejected task;
- diagnose blocker;
- renew failed provider attempt;
- create missing test task;
- resume review;
- reconcile stale Kanban state;
- create next phase work.

An incomplete project is not allowed to remain silently idle.

=====================================================================
36. KANBAN RECONCILIATION
=====================================================================

On every fresh Meta-Director launch:

reconcile:

    supervisor state
    checkpoint
    Git
    worktrees
    Kanban
    leases
    review artifacts
    requirement state

Do not assume previous process exited cleanly.

Resolve discrepancies deterministically.

Example:

worker branch has commit but lease says expired:

    inspect commit
    do not discard automatically.

worker says complete but no commit/handoff:

    task remains incomplete.

Kanban says complete but independent review absent:

    reopen/reconcile.

=====================================================================
37. INTEGRATION RULE
=====================================================================

Only independently accepted work enters integration.

Integrator must verify:

    exact candidate SHA
    review refers to same SHA
    required tests passed
    evidence fresh
    branch based on valid integration ancestor

After merge:

rerun affected tests.

If integration breaks prior requirement:

reopen it.

Do not paper over regression.

=====================================================================
38. VISUAL WORK
=====================================================================

Visual requirements are not complete through DOM/code inspection alone.

Use actual rendered application screenshots and interaction tests.

Review:

    organization overview
    department cockpit
    living office
    employee detail
    task/project/run views
    error states
    attention/approval states
    responsive layouts

Use real runtime state.

No fake activity.

No fake spending.

No fake QA.

No fake agent work.

=====================================================================
39. FINAL PRODUCT ARCHITECTURE INVARIANTS
=====================================================================

Preserve canonical hierarchy:

    ORGANIZATION
    → DEPARTMENT
    → PERSISTENT EMPLOYEE
    → PROJECT
    → TASK
    → RUN
    → TEMPORARY EXECUTION RESOURCE

Do not collapse:

    Project = Hermes Kanban card
    Employee = Hermes session
    Employee = Conductor worker
    Run = employee
    Department = crew

Final workforce canonical state follows the accepted Empirium product
architecture/specification.

=====================================================================
40. RELEASE GATE MUST NOT BE CIRCULAR
=====================================================================

Supervisor completion must NOT require a preexisting:

    BUILD_STATE.status = SHIPPED

as a prerequisite for supervisor completion.

Instead:

deterministic release gate produces evidence such as:

    FINAL_RELEASE_GATE.json

with at minimum:

    status = PASS
    exitCode = 0
    releaseCommit = exact current release SHA
    evidence manifest valid
    mandatory requirements verified
    required tests passed
    independent reviews accepted

Supervisor then recognizes completion and sets its own supervised project
status to SHIPPED.

If release evidence later regresses or release SHA changes:

project must reopen.

No model manually declares SHIPPED.

=====================================================================
41. FINAL RELEASE GATE
=====================================================================

The final executable/deterministic gate must verify at least:

REQUIREMENTS

    zero unmapped mandatory source requirements;
    zero mandatory requirements incomplete;
    exact evidence attached.

CODE QUALITY

    typecheck passes;
    build passes;
    required lint passes;
    unit passes;
    integration passes;
    E2E passes.

DATABASE / PERSISTENCE

    schema works;
    migrations work;
    restart persistence proven;
    authority boundaries correct.

RUNTIME

    real project/task/run execution;
    real statuses/events;
    persistent employees survive runtime death.

QA

    exact-commit independent acceptance;
    rejected work actually repaired.

SECURITY

    no secret leaks;
    capabilities enforced;
    knowledge scope enforced;
    no unauthorized paid inference.

RESILIENCE

    worker timeout;
    project manager timeout;
    Meta-Director death;
    provider failure;
    subscription capacity interruption;
    gateway restart;
    supervisor restart;
    app restart;
    reconnect;
    merge conflict.

VISUAL

    actual screenshot review;
    responsive;
    accessible;
    premium quality;
    no fake state.

AUTONOMY

    browser closed while project continues;
    Meta-Director killed and resumed;
    worker killed and replaced;
    rejection generates rework;
    no manual continue required.

=====================================================================
42. AUTONOMOUS BURN-IN
=====================================================================

Before release:

perform multiple genuine autonomous cycles.

Target at least 20 completed project/task cycles or a similarly meaningful
evidence-backed burn-in appropriate to the finished system.

Include injected cases:

- worker timeout;
- provider failure;
- review rejection;
- Meta-Director recycle;
- restart;
- stale event;
- missing asset;
- dependency wait.

Zero unexplained authoritative stuck work is allowed.

=====================================================================
43. INITIAL SUPERVISOR-CONTROLLED PROOF BEFORE RESUMING REAL CODE
=====================================================================

Before touching ESB-RUNTIME-001 again, prove this exact chain:

TEST A — META-DIRECTOR

    supervisor launches director
    → heartbeat
    → progress
    → checkpoint
    → kill/exit director
    → supervisor relaunches
    → new process reads checkpoint
    → continues

TEST B — CHILD WORKER

    Meta-Director creates disposable logical task
    → create child lease
    → launch disposable worker
    → worker heartbeats through deterministic wrapper
    → kill worker
    → lease expires
    → exactly one recovery directive
    → Meta-Director consumes it
    → creates replacement run
    → ACKs directive
    → replacement succeeds

TEST C — REVIEW REJECTION

    disposable implementation candidate
    → independent review returns deliberate REJECT
    → durable review stored
    → durable CHANGES_REQUESTED/rework created
    → parent process terminated
    → supervisor relaunches Meta-Director
    → Meta-Director discovers rework
    → replacement worker continues repair

TEST D — SUBSCRIPTION INTERRUPTION

    simulate/fixture temporary reviewer/provider capacity interruption
    → project remains incomplete
    → checkpoint preserved
    → no paid fallback
    → automatic retry/resume path proven

Do NOT fake these by editing final state directly.

Use actual orchestration transitions.

Only when A+B+C+D pass:

resume real implementation.

=====================================================================
44. THEN RESUME THE REAL BUILD
=====================================================================

After orchestration proof:

1. reconcile current rejected ESB-RUNTIME-001;
2. create fresh repair run;
3. implement with FreeLLMAPI;
4. test;
5. create fresh evidence;
6. submit exact commit to Opus;
7. if rejected:
       create rework automatically;
8. repeat;
9. integrate only after approval;
10. continue next requirement/task;
11. repeat until release gate passes.

=====================================================================
45. META-DIRECTOR RUNTIME PROMPT
=====================================================================

Persist this behavioral contract for every fresh Meta-Director invocation:

------------------------------------------------------------

You are the logical Meta-Director for the Empirium Studio AI Workforce build.

You are replaceable.

Your current process/session is disposable.

The PROJECT is durable.

On startup:

1. read project checkpoint;
2. read supervisor state;
3. read pending directives;
4. inspect Kanban/durable tasks;
5. inspect active leases;
6. inspect Git/worktrees;
7. inspect pending reviews/rejections;
8. reconcile discrepancies;
9. identify next runnable work;
10. continue.

During execution:

- heartbeat according to supervisor contract;
- report meaningful progress separately;
- checkpoint frequently;
- create leases for long-running children;
- never allow child timeout to delete logical work;
- turn every review rejection into durable rework;
- never self-approve implementation;
- use free workers for routine implementation;
- use Opus for independent review;
- never silently use paid API;
- do not stop because one provider/session is temporarily unavailable;
- do not stop because context is becoming large;
- recycle yourself safely when useful.

Before exiting voluntarily:

- checkpoint;
- persist next action;
- ensure child state is durable.

If you crash:

the supervisor will replace you.

If you wake into an incomplete project with no runnable activity:

diagnose why and restore motion.

Your terminal state is only:

    deterministic release gate PASS

or:

    genuine human-only blocker.

------------------------------------------------------------

=====================================================================
46. NO UNSUPERVISED FALLBACK CONTROLLER
=====================================================================

Do not quietly revert to:

    "run the build in this Hermes chat."

Do not create a second unsupervised Meta-Director.

Do not let Claude become the persistent project controller.

Do not let a Conductor session become project authority.

Do not let one Codex conversation become project authority.

All intelligent controller processes are disposable instances of durable roles.

=====================================================================
47. STATUS REPORTING TO ASH
=====================================================================

Do not spam routine completions.

Continue normal reversible work autonomously.

Surface only:

- genuine human-only blocker;
- serious security incident;
- unavoidable destructive decision;
- final successful completion.

Temporary worker/model/provider failures belong inside the autonomous recovery
loop.

=====================================================================
48. FINAL COMPLETION
=====================================================================

When the deterministic final release gate passes:

1. ensure exact release SHA recorded;
2. ensure all mandatory requirements VERIFIED;
3. ensure evidence fresh;
4. ensure final independent review accepted;
5. ensure deployment/restart verification passed;
6. ensure release artifact status PASS;
7. allow supervisor project completion transition;
8. persist final checkpoint;
9. stop creating new implementation workers;
10. produce concise final report.

Only then:

    PROJECT COMPLETE.

=====================================================================
49. BEGIN EXECUTION NOW
=====================================================================

FIRST ACTIONS:

1. Read the forensic incident audit:

    /home/ash/.local/state/empirium-supervisor/
    incident-audit-2026-09-17/INCIDENT_FORENSIC_AUDIT.md

2. Read:

    /home/ash/.local/share/empirium-supervisor/
    SUPERVISOR_COMMANDS.md

3. Inspect actual installed supervisor config/schema/source.

4. Inspect current `/home/ash/empirium-studio` Git/worktree/build state.

5. Back up supervisor config.

6. Register the REAL Empirium build with the supervisor.

7. Verify Meta-Director is actually supervisor-launched.

8. Run the four supervisor-controlled orchestration proof tests in Section 43.

9. Do not resume application coding unless those proofs pass.

10. Then resume ESB-RUNTIME-001 rework.

11. Continue automatically through every remaining requirement.

12. Do not stop after one successful repair.

13. Do not stop after one phase.

14. Do not stop after one context/session.

15. Do not stop after one reviewer session limit.

16. Do not wait for Ash to type "continue."

The supervisor exists specifically so that a fresh Meta-Director can always
resume the unfinished project.

RUN UNTIL:

    FINAL_RELEASE_GATE = PASS

or a genuine human-only blocker exists.

BEGIN NOW.
```

===== 2026-09-17 21:32 | session 20260917_191500_df556c | AI Staffforce =====
@file:`.hermes/attachments/Pasted content (20.7 KB)`

--- Attached Context ---

📄 @file:`.hermes/attachments/Pasted content (20.7 KB)` (5076 tokens)
```
# EMPIRIUM SUPERVISOR — FINAL ORCHESTRATION PROOF REPAIR + GO-LIVE
# SCOPE: REPAIR PROOF A/D ONLY, RE-RUN A–D, THEN ENABLE REAL META-DIRECTOR
# DO NOT RESUME APPLICATION CODING UNTIL ALL FOUR PROOFS PASS CLEANLY

You are continuing from an already-successful supervisor registration.

The real Empirium Studio project is now registered correctly:

    projectId: empirium-studio-workforce
    root: /home/ash/empirium-studio
    profile: coding-build
    checkpoint:
      /home/ash/empirium-studio/
      AI_WORKFORCE_BUILD/controller/meta-director-checkpoint.json

Completion gate:

    FINAL_RELEASE_GATE.status == PASS
    FINAL_RELEASE_GATE.exitCode == 0

The real project is currently:

    registered = YES
    enabled/launched = NO
    application coding resumed = NO
    release gate = NOT_READY

KEEP IT THAT WAY until the disposable orchestration proof gate passes.

======================================================================
1. CURRENT VERIFIED RESULTS
======================================================================

Supervisor test suite:

    51 passed
    0 failed

Proof results:

PROOF A
Meta-Director checkpoint/relaunch:
    PARTIAL PASS

Checkpoint and fresh-generation resume worked.

However the disposable fixture remained alive/stalled long enough for the
progress-stall watchdog to cause extra recycle activity.

Therefore the test did not cleanly prove:

    exactly one expected death
    → exactly one replacement
    → one successful resume

PROOF B
Child lease recovery:
    PASS

Verified:

    lease expired
    → LEASE_EXPIRED
    → fresh director consumed directive
    → directive ACKed
    → distinct replacement lease created

PROOF C
Review rejection → durable rework:
    PASS

Verified:

    REJECT
    → durable review
    → durable CHANGES_REQUESTED rework
    → checkpoint state persisted

PROOF D
Subscription interruption:
    FAIL

The disposable fixture rotated/exited before the injected:

    SUBSCRIPTION_LIMIT

classification could become the authoritative exit classification.

It was therefore recorded as a generic crash instead of subscription
capacity interruption.

Important:

    NO paid fallback occurred.

This is a TEST HARNESS / ORDERING problem unless evidence proves a supervisor
runtime defect.

Do not redesign the supervisor.

======================================================================
2. OBJECTIVE
======================================================================

Perform only the smallest changes necessary to make Proof A and Proof D
deterministic.

Then rerun ALL four proofs.

Only after:

    A = PASS
    B = PASS
    C = PASS
    D = PASS

may you:

    enable/launched = YES

for:

    empirium-studio-workforce

Then prove the real Meta-Director is under supervisor control.

After that, release the build back into autonomous execution.

======================================================================
3. DO NOT TOUCH APPLICATION CODE YET
======================================================================

Until the proof gate is satisfied:

DO NOT:

- modify Empirium application implementation;
- resume ESB-RUNTIME-001;
- create real implementation branches;
- merge rejected commit 898b7ac;
- dispatch real FreeLLMAPI coding workers;
- run Opus review of application code;
- mark requirements complete;
- alter FINAL_RELEASE_GATE to PASS.

Only work on:

    disposable orchestration fixtures
    test harnesses
    supervisor integration proof
    launcher/adapter fixture behavior

Preserve real project source state.

======================================================================
4. REPAIR PROOF A — CLEAN EXACTLY-ONE RELAUNCH
======================================================================

The purpose of Proof A is simple:

    supervisor launches director generation N
    → director reads checkpoint
    → heartbeat works
    → progress is recorded
    → checkpoint is updated
    → director intentionally exits
    → supervisor observes exit
    → exactly one generation N+1 launches
    → generation N+1 reads checkpoint
    → generation N+1 proves RESUME
    → fixture completes
    → no further recycle occurs

The previous proof became noisy because progress-stall recovery activated
during the fixture.

Fix the TEST, not production semantics.

Preferred approach:

Make Proof A complete well inside:

    progressSoftStallSeconds
    progressHardStallSeconds

The disposable director should:

GENERATION N:

1. heartbeat;
2. emit progress;
3. write nonce/checkpoint:
       phase = BEFORE_RELAUNCH
4. exit intentionally immediately.

GENERATION N+1:

5. read checkpoint;
6. verify:
       phase == BEFORE_RELAUNCH
7. heartbeat;
8. emit progress;
9. write:
       phase = RESUMED
10. satisfy disposable completion gate;
11. exit cleanly.

Then observe for at least:

    2 supervisor tick intervals
    +
    relevant launch cooldown

and prove:

    total expected launches = exactly 2

unless the supervisor's current architecture inherently includes one wrapper
launch that is separately counted.

If so, define the exact expected count from source semantics BEFORE running.

Do not change production progress thresholds merely to make the test pass.

Do not disable the progress watchdog globally.

If a per-fixture long-operation exemption is used, only use it if this matches
real production semantics and is explicitly bounded.

======================================================================
5. PROOF A ACCEPTANCE CRITERIA
======================================================================

Proof A passes only when evidence shows:

[ ] launch generation N occurred;

[ ] PID/fingerprint N recorded;

[ ] N heartbeated;

[ ] N emitted genuine progress;

[ ] N checkpointed BEFORE_RELAUNCH;

[ ] N exited intentionally;

[ ] exactly one expected supervisor recovery/relaunch occurred;

[ ] generation N+1 has a different launch identity;

[ ] N+1 read the SAME durable checkpoint;

[ ] N+1 explicitly identified itself as RESUME;

[ ] N+1 emitted heartbeat;

[ ] N+1 emitted progress;

[ ] completion fixture became true;

[ ] no progress-stall recycle occurred during this controlled proof;

[ ] no third unexpected launch occurred.

If extra launch occurs:

FAIL.

Investigate exactly why.

Do not explain it away.

======================================================================
6. REPAIR PROOF D — CLASSIFICATION MUST PRECEDE RECOVERY
======================================================================

The failure was a race:

    fixture process rotated/exited
        BEFORE
    SUBSCRIPTION_LIMIT classification became authoritative.

The test must be redesigned so classification is durable BEFORE the supervisor
makes restart-policy decisions.

Determine the actual adapter/supervisor contract first.

Do NOT invent a parallel test-only behavior that production cannot use.

The goal is to verify this real logical path:

    subscription-backed launcher encounters capacity limit
    ↓
    exit/result is classified SUBSCRIPTION_LIMIT
    ↓
    classification persisted
    ↓
    supervisor sees classification
    ↓
    project transitions to WAITING_SUBSCRIPTION_CAPACITY
    ↓
    retry/backoff scheduled
    ↓
    NO paid fallback
    ↓
    project remains incomplete
    ↓
    capacity-restored fixture/probe occurs
    ↓
    supervisor launches fresh director
    ↓
    checkpoint is read
    ↓
    project resumes

======================================================================
7. DETERMINE AUTHORITATIVE FAILURE-CLASSIFICATION ORDER
======================================================================

Before changing Proof D, inspect actual source.

Determine whether failure classification currently comes from:

A.
launcher exit code;

B.
structured launcher result file;

C.
CLI report-failure command;

D.
adapter wrapper;

E.
supervisor post-exit inspection;

F.
another implemented mechanism.

Document the actual authority.

Then ensure the production sequence is race-safe.

A correct architecture should resemble one of:

OPTION 1

    launcher detects SUBSCRIPTION_LIMIT
    → writes structured result atomically
    → exits
    → supervisor reads result
    → classifies exit

OPTION 2

    launcher reports SUBSCRIPTION_LIMIT
    → supervisor persists state
    → launcher exits
    → supervisor sees already-classified failure

What is NOT acceptable:

    process exits
    → generic crash handling immediately executes
    → classification arrives later

because that creates the exact race Proof D exposed.

If production code genuinely contains this race, fix the smallest relevant
ordering defect.

If only the fixture contains the race, fix only the fixture.

======================================================================
8. PROOF D FIXTURE
======================================================================

Use a disposable subscription-limit fixture.

Do NOT intentionally exhaust the user's real ChatGPT subscription.

Simulate the launch adapter's REAL classified failure mechanism.

Fixture behavior:

1. director launch begins;

2. checkpoint exists;

3. fixture signals the exact production-equivalent:

       SUBSCRIPTION_LIMIT

4. ensure classification is durably persisted;

5. fixture exits;

6. supervisor processes exit.

Expected state:

    WAITING_SUBSCRIPTION_CAPACITY

or the actual canonical equivalent already implemented.

Expected:

    no immediate relaunch storm;

    no generic crash classification;

    no paid fallback;

    no OPENAI_API_KEY;

    no ANTHROPIC_API_KEY;

    no OPENROUTER paid route;

    project remains incomplete.

Then simulate:

    subscription capacity restored

using the real supported recovery/preflight mechanism.

Expected:

    waiting state clears
    → exactly one fresh director launches
    → checkpoint is read
    → director resumes.

======================================================================
9. PROOF D ACCEPTANCE CRITERIA
======================================================================

Proof D passes only when:

[ ] classified failure = SUBSCRIPTION_LIMIT or canonical equivalent;

[ ] generic PROCESS_CRASH is NOT the final authoritative classification;

[ ] project enters waiting-capacity state;

[ ] no paid fallback occurs;

[ ] retry/backoff is bounded;

[ ] retry state is durable;

[ ] supervisor restart during waiting does not forget waiting state;

[ ] no rapid relaunch loop occurs;

[ ] simulated capacity restoration clears waiting;

[ ] exactly one fresh director launches;

[ ] fresh director reads previous checkpoint;

[ ] work resumes;

[ ] no manual "continue" operation is required.

======================================================================
10. REGRESSION CHECK PROOFS B AND C
======================================================================

Even though B and C already passed, rerun them after the A/D harness changes.

Do not unnecessarily rewrite them.

PROOF B must still show:

    child lease
    → timeout
    → LEASE_EXPIRED
    → exactly one recovery directive
    → consumed
    → ACKed
    → replacement lease with new run identity

PROOF C must still show:

    review REJECT
    → durable exact-commit review artifact
    → CHANGES_REQUESTED
    → durable rework
    → survives parent restart
    → fresh Meta-Director discovers rework

======================================================================
11. RUN PROOFS IN ISOLATED DISPOSABLE PROJECT
======================================================================

Do not use real Empirium application state as test data.

Use a dedicated disposable project ID, for example:

    empirium-orchestration-proof-final

Use:

    isolated checkpoint
    isolated logs
    isolated completion artifacts
    isolated leases
    isolated directives

The proof project must never point completion checks at the real:

    FINAL_RELEASE_GATE

After the test:

cleanly unregister/remove only the disposable project.

Keep evidence.

======================================================================
12. PROOF EVIDENCE
======================================================================

Create:

    /home/ash/.local/state/empirium-supervisor/
    install-evidence/
    final-orchestration-proof/

At minimum store:

    proof-a.md
    proof-b.md
    proof-c.md
    proof-d.md
    proof-summary.json

Include:

    timestamps
    project ID
    generation IDs
    launch IDs
    PIDs/fingerprints
    heartbeat timestamps
    progress sequence
    checkpoint hashes
    lease IDs
    directive IDs
    ACKs
    exit class
    waiting state
    retryNotBefore
    completion transitions
    relevant event lines

Do not include credentials.

======================================================================
13. PROOF SUMMARY
======================================================================

Write machine-readable:

{
  "proofA": {
    "status": "PASS|FAIL",
    "exactRelaunchCountVerified": true,
    "checkpointResumeVerified": true
  },
  "proofB": {
    "status": "PASS|FAIL",
    "leaseRecoveryVerified": true
  },
  "proofC": {
    "status": "PASS|FAIL",
    "durableReworkVerified": true
  },
  "proofD": {
    "status": "PASS|FAIL",
    "subscriptionLimitClassificationVerified": true,
    "waitingStateVerified": true,
    "automaticResumeVerified": true,
    "paidFallbackObserved": false
  },
  "allPassed": true
}

Do not set allPassed=true unless all four are genuinely PASS.

======================================================================
14. ONLY AFTER A+B+C+D PASS — ENABLE REAL PROJECT
======================================================================

Once:

    allPassed = true

proceed immediately.

Do not ask Ash for confirmation unless an actual destructive/human-only
blocker exists.

Enable the registered real project:

    empirium-studio-workforce

using the installed supervisor's supported mechanism.

Do not invent a new start mechanism.

======================================================================
15. REAL PROJECT LAUNCH VERIFICATION
======================================================================

Verify the REAL Meta-Director is launched by the supervisor.

Require evidence:

    project = empirium-studio-workforce

    root = /home/ash/empirium-studio

    profile = coding-build

    launcher = expected canonical adapter

    DIRECTOR_LAUNCHED exists

    PID exists

    PID fingerprint matches

    generation exists if implemented

    heartbeat fresh

    progress fresh

    checkpoint loaded

The build must no longer be controlled by an unrelated Hermes/Claude chat
session.

======================================================================
16. REAL META-DIRECTOR FIRST ACTION
======================================================================

On first real supervised launch:

DO NOT immediately create random new work.

Reconcile:

    forensic audit
    Git
    worktrees
    checkpoint
    Kanban
    rejected candidate 898b7ac
    requirement state
    leases
    reviews
    handoffs
    evidence

Then persist a new real checkpoint.

Identify the next logical task.

Known current work requiring repair:

    ESB-RUNTIME-001

The previous R3 run is dead.

Do not resurrect R3 identity.

Create the next correct fresh run identity from durable history.

Likely:

    ESB-RUNTIME-001-R4

but derive it from actual state.

======================================================================
17. RESUME APPLICATION CODING
======================================================================

Only now may coding resume.

ESB-RUNTIME-001 repair must address at least the independently known rejected
areas:

- meaningful configured PostgreSQL route tests;
- documented unconfigured department local fallback;
- correct employee POST configuration-error semantics;
- correct 404 missing-entity semantics;
- compatibility/public API preservation;
- narrow getPool() contract unless widening justified;
- fresh runtime evidence bound to exact repair commit.

Implementation route:

    FreeLLMAPI / genuinely free worker

Create:

    dedicated worktree
    new run ID
    new lease
    precise repair brief
    structured handoff contract

======================================================================
18. OPUS REVIEW MUST BE DURABLE
======================================================================

After deterministic verification:

submit exact repair commit for independent Opus review through subscription
route.

Persist:

    exact commit
    verdict
    findings
    evidence references
    timestamp

If REJECT:

    automatically create CHANGES_REQUESTED rework.

Do not stop.

If Opus subscription hits capacity:

    WAITING_SUBSCRIPTION_CAPACITY

for that review path.

Continue independent runnable work.

Retry automatically later.

Do NOT let Opus session capacity kill the Meta-Director.

======================================================================
19. FROM THIS POINT, PROJECT RUNS AUTONOMOUSLY
======================================================================

After real launch verification, continue indefinitely until deterministic
completion.

The loop is:

    reconcile
    → read directives
    → monitor leases
    → repair failed runs
    → dispatch ready work
    → verify
    → review
    → rework rejects
    → integrate approvals
    → update requirements
    → checkpoint
    → release gate
    → continue

No manual continue required.

======================================================================
20. NEVER AGAIN RUN THE REAL BUILD OUTSIDE SUPERVISOR
======================================================================

Do not create an unsupervised replacement Meta-Director through:

    Hermes chat
    Claude chat
    raw manual codex exec
    standalone shell loop
    Conductor one-shot session

The supervisor-controlled project is now the canonical Meta-Director launch
path.

Other tools may be used by the Meta-Director as subordinate execution/review
resources.

They are not the durable controller.

======================================================================
21. HUMAN BLOCKER RULE
======================================================================

Only stop and ask Ash if a genuinely human-only action is necessary.

Examples:

    interactive account authentication
    unavoidable sudo authorization
    irreversible destructive choice
    truly missing user-owned mandatory input

Do NOT stop for:

    worker timeout
    worker bug
    test failure
    Opus rejection
    provider 429
    temporary subscription limit
    merge conflict
    stale evidence
    failed Proof fixture that can be repaired autonomously

======================================================================
22. FINAL RELEASE
======================================================================

Continue until:

    FINAL_RELEASE_GATE.status == PASS
    FINAL_RELEASE_GATE.exitCode == 0

The release gate must be tied to the exact release commit.

No model may fake it.

Supervisor then transitions the real project to SHIPPED according to its
deterministic completion contract.

Only then stop normal project execution.

======================================================================
23. IMMEDIATE EXECUTION ORDER
======================================================================

Do this now:

1. inspect current Proof A fixture;
2. identify exactly why progress-stall recycle happened;
3. repair fixture to produce clean exactly-one relaunch;
4. run Proof A;
5. inspect Proof D classification ordering;
6. determine whether race is fixture-only or production;
7. make smallest correct repair;
8. run Proof D;
9. rerun Proof B;
10. rerun Proof C;
11. generate final proof evidence;
12. require A+B+C+D PASS;
13. clean disposable proof project;
14. enable real empirium-studio-workforce project;
15. verify real supervisor-launched Meta-Director;
16. reconcile existing build state;
17. create fresh ESB-RUNTIME-001 repair run;
18. resume autonomous build;
19. continue without waiting for Ash;
20. stop only at deterministic release PASS or genuine human-only blocker.

BEGIN NOW.
```

===== 2026-09-17 21:38 | session 20260917_213801_1a93d3 | Diagnose autonomous AI system stopping failures =====
@file:`.hermes/attachments/Pasted content (36.8 KB)`

--- Attached Context ---

📄 @file:`.hermes/attachments/Pasted content (36.8 KB)` (9028 tokens)
```
# =====================================================================
# EMPIRIUM META-ORCHESTRATOR CONTINUITY PROBLEM
# FORENSIC ARCHITECTURE REVIEW REQUEST
#
# QUESTION:
# HOW DO I MAKE THIS SYSTEM KEEP WORKING UNTIL THE PROJECT IS ACTUALLY
# FINISHED INSTEAD OF REPEATEDLY STOPPING AND RETURNING CONTROL TO ME?
# =====================================================================

I need you to act as a senior autonomous-agent systems architect,
distributed-systems engineer, reliability engineer, and orchestration designer.

I do NOT primarily need another coding prompt.

I need you to diagnose a persistent architectural failure in an autonomous AI
development system and tell me exactly how to eliminate it.

The central problem is:

    THE AI KEEPS STOPPING.

It often stops at completely recoverable intermediate failures and reports them
to me instead of autonomously diagnosing them, repairing them, delegating
analysis to another available model, retrying, replanning, or continuing with
other runnable work.

I want an architecture where:

    PROJECT INCOMPLETE
        +
    NO GENUINE HUMAN-ONLY BLOCKER

always implies:

    TAKE ANOTHER ACTION.

The system should be capable of running for hours or days, across many
individual LLM processes and sessions, until deterministic completion.

Do not interpret "run indefinitely" to mean keeping one LLM context alive
forever.

Individual AI sessions SHOULD be disposable.

What must persist indefinitely is:

    the logical Meta-Orchestrator role
    +
    project state
    +
    queue
    +
    checkpoints
    +
    recovery logic
    +
    deterministic supervisor.

=====================================================================
1. SYSTEM CONTEXT
=====================================================================

The project is Empirium Studio.

It is being developed using a hierarchical AI workforce.

Intended architecture:

DETERMINISTIC SUPERVISOR
    ↓
META-ORCHESTRATOR / META-DIRECTOR
    ↓
PROJECT MANAGERS / SUB-ORCHESTRATORS
    ↓
IMPLEMENTATION WORKERS
    ↓
TEST / REVIEW / REWORK
    ↓
INTEGRATION
    ↓
FINAL RELEASE GATE

Available intelligence/resources include:

1. ChatGPT/Codex subscription
   - current verified Codex subscription route
   - effective model observed on VPS: gpt-6-astra
   - no direct OpenAI API billing required.

2. ChatGPT itself
   - GPT-5.6 Sol can be used for difficult diagnosis/planning where available
     through the user's existing subscription/workflow.

3. Claude subscription
   - Opus available for independent architecture analysis, review and QA.
   - should NOT use paid Anthropic API.

4. FreeLLMAPI
   - free models intended to perform most implementation work.

New pay-as-you-go inference spend must remain:

    $0.

=====================================================================
2. WHAT I EXPECT
=====================================================================

I want this experience:

I start the project once.

Then I can leave.

The system should continue through:

- implementation;
- failed workers;
- bad code;
- tests failing;
- reviewer rejection;
- session limits;
- context exhaustion;
- model/provider outages;
- worker timeouts;
- merge conflicts;
- stale evidence;
- Meta-Orchestrator process exits;
- gateway restarts;
- supervisor restarts;
- rework cycles;

without needing me to keep typing:

    continue
    try again
    fix it
    what next?
    carry on

If the system encounters something it does not understand, it should use the
other available intelligence resources.

For example:

    Meta-Director encounters strange supervisor behaviour
        ↓
    create diagnostic task
        ↓
    ask GPT-5.6 Sol and/or Opus to analyze evidence
        ↓
    reconcile diagnosis
        ↓
    create repair task
        ↓
    implement
        ↓
    test again
        ↓
    continue

It should NOT say:

    "Proof D failed. The next action is to repair it."

and then terminate.

The act of identifying "the next action" means it should EXECUTE that next
action.

=====================================================================
3. HISTORY OF THE PROBLEM
=====================================================================

This has happened repeatedly in different forms.

---------------------------------------------------------------------
PROBLEM A — ONE-SHOT ORCHESTRATION
---------------------------------------------------------------------

The original Hermes/Conductor behaviour was fundamentally one-shot.

Workers were launched and the parent orchestration process would eventually
report a result and finish.

This is useful for:

    "perform this task"

but not sufficient for:

    "own this project until release."

We need a persistent project-management loop rather than a single request →
response lifecycle.

---------------------------------------------------------------------
PROBLEM B — CHAT/SESSION BECAME THE REAL CONTROLLER
---------------------------------------------------------------------

Previous builds were effectively controlled by:

    Hermes session
    Claude session
    Codex session
    Conductor invocation

rather than durable infrastructure.

When the session ended:

    project intelligence disappeared.

The system had files, but no guaranteed controller woke up to continue them.

---------------------------------------------------------------------
PROBLEM C — SUPERVISOR EXISTED BUT REAL PROJECT BYPASSED IT
---------------------------------------------------------------------

A deterministic supervisor was successfully installed.

It passed extensive testing.

However a forensic incident audit found:

    RC-01 — REAL PROJECT NEVER REGISTERED WITH SUPERVISOR.

The supervisor was supervising only:

    supervisor-selftest

while the actual Empirium build was running separately through Hermes/Claude
execution paths.

Therefore the heartbeat did NOT fail.

The real build simply was not connected to it.

---------------------------------------------------------------------
PROBLEM D — META-DIRECTOR WAS NOT SUPERVISOR-LAUNCHED
---------------------------------------------------------------------

The real Meta-Director was not launched as a durable supervised project.

Therefore when its external session ended there was no canonical supervisor
project available to relaunch it from checkpoint.

---------------------------------------------------------------------
PROBLEM E — CHILD WORKERS HAD NO DURABLE LEASES
---------------------------------------------------------------------

Example:

    ESB-RUNTIME-001-R3

was an implementation worker.

It timed out.

But it had:

    no supervisor child lease.

Therefore there was no deterministic:

    timeout
    → LEASE_EXPIRED
    → recovery directive
    → replacement worker.

The logical task remained, but recovery was not wired.

---------------------------------------------------------------------
PROBLEM F — REVIEWER SESSION BECAME PART OF THE CONTROL PATH
---------------------------------------------------------------------

After R3 failed, an existing commit was submitted to Opus.

Eventually the Claude session produced:

    "You've hit your session limit"

and execution stopped.

This is architecturally wrong.

Opus should be:

    reviewer/advisor

not:

    persistent project controller.

A reviewer becoming temporarily unavailable should create:

    WAITING_REVIEW_CAPACITY

while the Meta-Director remains alive or is relaunched later.

---------------------------------------------------------------------
PROBLEM G — INTERMEDIATE FAILURE IS TREATED AS A LEGITIMATE END
---------------------------------------------------------------------

This is the most important recurring behavioural problem.

The system keeps doing things like:

    test fails
    → report failure
    → stop

or:

    proof fails
    → explain next action
    → stop

or:

    worker times out
    → report timeout
    → stop

or:

    reviewer rejects
    → report rejection
    → stop

But the intended semantic is:

    failure
    → new information
    → choose next action
    → continue.

Failure is a transition.

It is NOT a terminal state.

---------------------------------------------------------------------
PROBLEM H — "DO NOT PROCEED UNTIL X PASSES" IS MISINTERPRETED
---------------------------------------------------------------------

Prompts contain sensible safety gates such as:

    "Do not resume application coding until Proof A-D pass."

An LLM sometimes interprets:

    Proof D failed

as:

    "I am forbidden from proceeding."

But the actual meaning is:

    "I am forbidden from application coding,
     therefore I must keep repairing and rerunning Proof D until it passes."

The distinction between:

    DO NOT PROCEED TO NEXT PHASE

and:

    STOP WORKING

needs to become explicit and structural.

---------------------------------------------------------------------
PROBLEM I — NEXT ACTION IS REPORTED RATHER THAN EXECUTED
---------------------------------------------------------------------

Example output:

    "The next required action is to repair and rerun the disposable Proof A/D
     harness."

That itself demonstrates the next action was known.

Yet the agent returned the information to the user rather than doing it.

This behaviour must be eliminated.

If:

    nextAction != null

then the orchestrator should execute:

    nextAction

unless it requires genuine human input.

---------------------------------------------------------------------
PROBLEM J — RECOVERABLE UNCERTAINTY IS TREATED LIKE A HUMAN BLOCKER
---------------------------------------------------------------------

Examples of things the orchestrator should solve itself:

- test race;
- fixture race;
- unclear source behaviour;
- failed process;
- unexpected result;
- difficult architecture question;
- uncertainty over how best to implement something;
- reviewer disagreement.

These should trigger:

    research
    deeper analysis
    independent model consultation
    source inspection
    experiment
    retry

not:

    return to user.

---------------------------------------------------------------------
PROBLEM K — AVAILABLE HIGH-INTELLIGENCE MODELS ARE NOT USED AS
AUTONOMOUS ESCALATION
---------------------------------------------------------------------

This is particularly frustrating.

The system already has access to high-intelligence reasoning through existing
subscriptions.

When an unusual problem appears, such as the Proof D race:

    fixture rotated before SUBSCRIPTION_LIMIT classification was persisted

the Meta-Director could have:

1. collected the relevant source and logs;
2. created a diagnosis package;
3. asked GPT-5.6 Sol;
4. asked Opus independently;
5. compared answers;
6. inspected source itself;
7. selected a safe repair;
8. implemented through a free worker;
9. rerun proof.

Instead it produced a status report and stopped.

I need the architecture to make "ask another expert model" an ordinary
autonomous recovery action.

---------------------------------------------------------------------
PROBLEM L — MODEL CONTEXT IS STILL BEING CONFUSED WITH PROJECT LIFE
---------------------------------------------------------------------

I do NOT need one model process to think forever.

That is impossible/unreliable.

Desired behaviour:

    META-DIRECTOR PROCESS #17
        ↓ checkpoint
        ↓ exits

    SUPERVISOR
        ↓ sees project incomplete

    META-DIRECTOR PROCESS #18
        ↓ reconstructs state
        ↓ continues

Therefore project continuation must depend on:

    durable state

not:

    preserving a specific model context.

---------------------------------------------------------------------
PROBLEM M — CLEAN EXIT CAN BE AS DANGEROUS AS A CRASH
---------------------------------------------------------------------

The system must recover not only when an LLM crashes.

An LLM may simply:

    provide a final response
    exit code 0

while the project is incomplete.

From the project's perspective that is still:

    CONTROLLER DISAPPEARED WHILE WORK REMAINS.

The supervisor/orchestration layer must treat:

    director process exited
    AND
    release gate != PASS
    AND
    project != paused/human-blocked/waiting-capacity

as:

    RELAUNCH DIRECTOR.

A clean exit must not imply project completion.

---------------------------------------------------------------------
PROBLEM N — QUIESCENCE IS NOT BEING TREATED AS A FAULT
---------------------------------------------------------------------

Another dangerous state is:

    project incomplete
    no worker running
    no review running
    no human blocker
    Meta-Director alive or recently exited

This state should NEVER persist indefinitely.

It should become:

    PROJECT_QUIESCENT

and trigger:

    determine next runnable work.

---------------------------------------------------------------------
PROBLEM O — HEARTBEAT ALONE IS NOT ENOUGH
---------------------------------------------------------------------

Heartbeat answers:

    "is the process alive?"

It does not answer:

    "is useful work happening?"

A model could continue heartbeating while stuck.

Therefore we need:

    HEARTBEAT
        and separately
    PROGRESS.

If heartbeat fresh but progress stale:

    diagnose
    → replan
    → if necessary recycle Meta-Director context.

---------------------------------------------------------------------
PROBLEM P — REVIEW REJECTION IS NOT ALWAYS DURABLY TRANSITIONED
---------------------------------------------------------------------

Correct lifecycle:

    candidate
    → review
    → REJECT
    → durable CHANGES_REQUESTED
    → repair task
    → implementation
    → test
    → review again

Incorrect lifecycle:

    candidate
    → review
    → REJECT
    → output text to user
    → stop.

Review verdict needs to cause state transition, not merely produce prose.

---------------------------------------------------------------------
PROBLEM Q — PROVIDER / SUBSCRIPTION LIMITS NEED STATE MACHINES
---------------------------------------------------------------------

Temporary model/provider conditions should become durable states such as:

    WAITING_SUBSCRIPTION_CAPACITY
    WAITING_PROVIDER
    BLOCKED_HUMAN_AUTH

They should not simply cause an AI invocation to terminate.

The project should preserve retry times and resume automatically.

---------------------------------------------------------------------
PROBLEM R — THE SYSTEM DOES NOT YET HAVE A HARD TERMINATION INVARIANT
---------------------------------------------------------------------

The Meta-Orchestrator needs a rule stronger than ordinary prompting:

    IT IS FORBIDDEN TO TERMINATE AN INVOCATION WHILE THE PROJECT IS
    INCOMPLETE UNLESS IT HAS FIRST PERSISTED A VALID REASON THAT MAKES
    RELAUNCH/WAITING SAFE.

And the deterministic layer should independently enforce this.

An LLM promising:

    "I will keep going"

is not enough.

=====================================================================
4. MOST RECENT EXAMPLE
=====================================================================

The real project was finally registered with the supervisor.

The system correctly refused to resume application coding until four disposable
orchestration proofs passed.

Results:

    Proof A — partial pass
    Proof B — pass
    Proof C — pass
    Proof D — fail

Proof D failed because:

    the fixture launch rotated before injected SUBSCRIPTION_LIMIT
    classification became authoritative;

therefore the outcome was classified as a generic crash rather than temporary
subscription-capacity exhaustion.

No paid fallback occurred.

This was recoverable.

At that moment the agent already knew the next action:

    repair Proof A/D harness
    rerun
    continue once A+B+C+D pass.

Yet it stopped and told the user:

    "The next required action is to repair and rerun..."

THIS IS THE BEHAVIOUR I NEED TO ELIMINATE.

The correct autonomous response should have been:

    investigate why classification lost the race
    ↓
    inspect source
    ↓
    if necessary ask Sol/Opus
    ↓
    repair disposable harness or production ordering
    ↓
    rerun Proof D
    ↓
    rerun Proof A
    ↓
    continue.

=====================================================================
5. CORE DESIGN QUESTION
=====================================================================

Please answer:

HOW SHOULD I ARCHITECT THE META-ORCHESTRATOR SO THAT:

    PROJECT INCOMPLETE
    +
    NO HUMAN-ONLY BLOCKER

MATHEMATICALLY / DETERMINISTICALLY IMPLIES:

    MORE WORK WILL OCCUR

even if:

- the current AI decides to return a final answer;
- the AI process exits 0;
- context fills;
- the model gives up;
- a child fails;
- a reviewer rejects;
- provider capacity disappears;
- a test fails;
- a proof fails;
- the orchestration process crashes?

I want this property guaranteed outside the model itself.

=====================================================================
6. I SUSPECT WE NEED AN EXPLICIT ORCHESTRATOR STATE MACHINE
=====================================================================

Evaluate a state machine roughly like:

    BOOTSTRAPPING
    RECONCILING
    READY
    DISPATCHING
    RUNNING
    REVIEWING
    REWORK
    WAITING_PROVIDER
    WAITING_SUBSCRIPTION
    WAITING_HUMAN
    RECOVERING
    QUIESCENT
    RELEASE_VALIDATION
    SHIPPED

with:

    SHIPPED

as the only ordinary terminal state.

Potential invariant:

    status != SHIPPED
    AND
    status != WAITING_HUMAN
    AND
    now >= retryNotBefore
    AND
    activeActionCount == 0

must force:

    wake Meta-Director.

Would this solve the core problem?

Design the exact version you recommend.

=====================================================================
7. I SUSPECT WE NEED AN "ACTION DEBT" / NEXT-ACTION INVARIANT
=====================================================================

Consider requiring every Meta-Director checkpoint to contain:

    projectStatus
    currentPhase
    activeActions[]
    pendingReviews[]
    pendingRework[]
    blockers[]
    retryNotBefore
    nextActions[]

Invariant:

If project incomplete:

    at least one of these MUST be true:

A.
    activeActions.length > 0

B.
    nextActions.length > 0

C.
    retryNotBefore != null

D.
    genuineHumanBlocker != null

Anything else is invalid:

    ORCHESTRATOR_QUIESCENT_WITH_UNFINISHED_PROJECT

and should cause recovery.

Evaluate and improve this idea.

=====================================================================
8. I SUSPECT WE NEED AN EXTERNAL WAKE LOOP
=====================================================================

Should the deterministic supervisor periodically evaluate something like:

    if releaseGate != PASS:

        if directorDead:
            launch director

        else if heartbeatStale:
            recover director

        else if progressStale:
            issue diagnosis/recycle

        else if no active work and no waiting condition:
            issue PROJECT_QUIESCENT

        else if retryNotBefore elapsed:
            wake director

and guarantee there is always another opportunity for intelligence to run?

Explain exactly how this should work without turning the supervisor into a
second project scheduler.

=====================================================================
9. CLEAN EXIT SEMANTICS
=====================================================================

This requires particular attention.

Suppose Meta-Director writes:

    "Proof D failed. Next action is X."

and then exits normally.

The deterministic supervisor should see:

    director exited
    project incomplete
    release gate false
    not paused
    not human blocked
    not waiting until future retry

and therefore launch a fresh Meta-Director.

That next Meta-Director reads:

    nextAction = X

and EXECUTES X.

Is this sufficient to overcome the tendency of LLMs to stop?

If not, what else is needed?

=====================================================================
10. MODEL ESCALATION POLICY
=====================================================================

Design an autonomous "I don't know / unusual failure" escalation ladder.

For example:

LEVEL 0
Meta-Director reasons locally.

LEVEL 1
Inspect source/logs/tests.

LEVEL 2
Launch focused diagnostic FreeLLM worker(s).

LEVEL 3
Ask GPT-5.6 Sol for independent diagnosis.

LEVEL 4
Ask Opus independently.

LEVEL 5
Compare/reconcile analyses.

LEVEL 6
Run controlled experiment.

LEVEL 7
Create repair task.

The orchestrator must not ask the human simply because:

    "this is difficult."

Only genuine human authority/input should interrupt autonomy.

Design exact escalation triggers.

=====================================================================
11. TOOL / MODEL DELEGATION QUESTION
=====================================================================

I need you to examine this behaviour:

The agent repeatedly knows:

    "This needs further analysis."

But instead of using available models, it reports that fact to me.

How do I make:

    NEEDS_ANALYSIS

produce:

    SPAWN_ANALYST

rather than:

    RETURN_TO_USER?

Should this be represented as a deterministic task transition rather than left
to prompt interpretation?

I strongly suspect yes.

Design it.

=====================================================================
12. FINAL RESPONSE MUST NOT BE A TERMINATION SIGNAL
=====================================================================

How should user-facing status reporting work?

I want the Meta-Director to be able to produce logs/status updates WITHOUT
those status messages meaning:

    stop processing.

For example it may write:

    "Proof D failed; diagnosing race."

but then immediately continue internally.

Should reporting be decoupled from process lifecycle entirely?

Could status reports become durable events while the process continues?

Or should the supervisor always assume a final response is non-terminal unless
release state says otherwise?

Give the best architecture.

=====================================================================
13. REVIEWER AVAILABILITY
=====================================================================

Design how Opus should be used.

It should be:

    asynchronous/subordinate reviewer.

It should NOT own continuation.

If Opus is unavailable:

    review stays pending
    other work continues
    retry is scheduled.

If review is on the critical path and no other work exists:

    Meta-Director may exit safely
    supervisor later wakes it after retryNotBefore.

It should NOT end the project.

Explain the exact state transition.

=====================================================================
14. WORKER FAILURE
=====================================================================

Same principle.

A child worker process dying should mean:

    run failed

NOT:

    logical task failed forever

and certainly not:

    project stopped.

Expected:

    TASK
       ├── Run R1 failed
       ├── Run R2 rejected
       ├── Run R3 timeout
       └── Run R4 succeeds

Define task/run semantics so retries are natural.

=====================================================================
15. HUMAN BLOCKER DEFINITION
=====================================================================

This needs to be extremely narrow.

Things that ARE NOT human blockers:

- test failure;
- architecture uncertainty;
- worker timeout;
- model failure;
- reviewer rejection;
- subscription capacity with known reset;
- provider outage;
- merge conflict;
- source ambiguity resolvable through inspection;
- unfamiliar bug;
- needing another opinion.

Potential true blockers:

- interactive login requiring user;
- required secret not available;
- destructive irreversible user decision;
- legal/business decision only user can make;
- missing private asset that cannot be reconstructed.

Design a formal blocker classification mechanism.

=====================================================================
16. FAILURE OF THE META-DIRECTOR ITSELF
=====================================================================

Assume models are unreliable executors.

The Meta-Director might:

- hallucinate completion;
- fail to perform next action;
- return a summary instead;
- get context saturated;
- exit inexplicably;
- loop;
- get stuck;
- forget to heartbeat.

How does the deterministic infrastructure compensate?

Do NOT propose "write a stronger prompt" as the main answer.

I want system-level enforcement.

=====================================================================
17. DESIRED PROJECT LIVENESS INVARIANT
=====================================================================

I want something similar to:

For every non-terminal project P:

Eventually one of these must occur:

    1. a durable state transition;
    2. a runnable action starts;
    3. a bounded retry timer is established;
    4. a genuine human blocker is recorded;
    5. the project reaches SHIPPED.

It must never remain silently inert forever.

Please formalize this invariant.

How should we test it?

=====================================================================
18. DESIRED META-DIRECTOR CONTRACT
=====================================================================

I am considering this rule:

ON EVERY INVOCATION:

1. reconstruct state;
2. reconcile inconsistencies;
3. consume recovery directives;
4. inspect failed/rejected work;
5. determine next executable action;
6. execute actions until:
       a) context recycle useful;
       b) waiting timer needed;
       c) genuine human blocker;
       d) SHIPPED.
7. before exit:
       persist state and exact wake condition.

An invocation may NOT exit merely because:

    "I have completed the current subtask."

Critique and strengthen this.

=====================================================================
19. DESIRED SUPERVISOR CONTRACT
=====================================================================

I am considering:

The supervisor may allow a director process to remain absent ONLY if:

    SHIPPED

or:

    PAUSED_BY_USER

or:

    WAITING_HUMAN

or:

    retryNotBefore > now.

Otherwise:

    director must exist.

If director exits 0 while project incomplete:

    relaunch.

If director crashes:

    relaunch.

If director heartbeats but progress stalls:

    diagnosis/recycle.

If retry time arrives:

    relaunch/wake.

If project becomes quiescent:

    wake.

Critique this.

What exact edge cases are missing?

=====================================================================
20. SHOULD META-DIRECTOR ITSELF BE A PERMANENT SERVICE?
=====================================================================

Compare:

OPTION A

    one long-running Codex process kept alive indefinitely

versus

OPTION B

    disposable Codex executions relaunched repeatedly by deterministic
    supervisor from durable checkpoint.

I strongly favour B.

Confirm whether this is the correct approach and explain implementation
implications.

=====================================================================
21. HOW SHOULD TASK QUEUE OWNERSHIP WORK?
=====================================================================

There must not be two schedulers racing.

I need:

Supervisor:
    liveness only.

Meta-Director:
    intelligent planning.

Hermes/Kanban:
    durable build-task queue.

How should "project is quiescent" be detected without the supervisor becoming a
task scheduler?

Could supervisor simply emit:

    PROJECT_QUIESCENT

and wake/relaunch Meta-Director, while Meta-Director alone decides which task
to schedule?

Design exact ownership.

=====================================================================
22. SHOULD EVERY META-DIRECTOR INVOCATION HAVE A BUDGETED LOOP?
=====================================================================

Rather than expecting one invocation to run forever, perhaps each invocation
should perform:

    N actions
or
    M minutes
or
    context threshold

then checkpoint and voluntarily exit.

Supervisor launches the next one immediately if work remains.

This could make continuity more predictable.

Evaluate.

For example:

    max invocation wall-clock = 30–60 min
    max context utilization = threshold
    checkpoint every meaningful transition
    controlled recycle

Would this be safer than indefinite sessions?

=====================================================================
23. HIGH-INTELLIGENCE CONSULTATION
=====================================================================

I specifically want the final architecture to exploit existing subscriptions.

If the Meta-Director encounters a hard systems problem, it should be permitted
to create something like:

    DIAGNOSTIC_CASE-2026-09-17-001

containing:

    question
    relevant source
    logs
    expected behavior
    observed behavior
    hypotheses

Then request:

    Sol analysis
    Opus analysis

and wait/reconcile them.

I do not want it returning the diagnostic question to me when expert AI
resources are available.

Design this mechanism.

=====================================================================
24. NO PSEUDO-AUTONOMY
=====================================================================

I want you to identify every architectural pattern that LOOKS autonomous but
is not.

Examples might include:

- prompts saying "continue until done";
- heartbeat without wake/relaunch;
- worker spawning without durable tasks;
- retry instructions without retry timers;
- checkpoints nobody reads;
- review results only stored in chat;
- supervisor watching only process death;
- next-action fields nobody enforces;
- status messages being mistaken for terminal output;
- one-shot Conductor calls;
- a queue with no guaranteed consumer.

Identify all such pseudo-autonomy patterns relevant here.

=====================================================================
25. ANALYZE THE CURRENT FAILURE AS A STATE MACHINE
=====================================================================

Most recent state:

    real project registered
    not yet launched
    release gate NOT_READY
    Proof A partial
    Proof B pass
    Proof C pass
    Proof D fail
    next action known

The agent returned control to user.

In your proposed architecture, show exactly what should have happened next.

I want the transition table.

For example:

    state = ORCHESTRATION_VALIDATION
    event = PROOF_D_FAILED

should transition to something like:

    state = DIAGNOSING_VALIDATION_FAILURE

not:

    terminal response.

Then show subsequent possible transitions.

=====================================================================
26. AUTOMATED "WHY DID YOU STOP?" CHECK
=====================================================================

Could every Meta-Director process be required before exit to write:

    EXIT_INTENT.json

containing:

    reason
    projectComplete
    humanBlocker
    retryNotBefore
    checkpoint
    nextAction

Then supervisor validates it.

Example:

If:

    projectComplete=false
    humanBlocker=null
    retryNotBefore=null
    nextAction exists

and process exits:

supervisor immediately relaunches.

If no valid EXIT_INTENT exists:

treat as unexpected exit and relaunch.

Would this help?

Improve the concept.

=====================================================================
27. WATCHDOG AGAINST "I HAVE GIVEN MY ANSWER"
=====================================================================

LLMs have a natural conversational tendency to assume that producing a useful
answer completes their job.

Our project semantics are different.

How do we make external state override conversational completion semantics?

I want:

    assistant response completed

NOT EQUAL TO:

    project work completed.

Only:

    release gate PASS

means project complete.

Design enforcement around that principle.

=====================================================================
28. EXPECTED ANSWER
=====================================================================

I want a comprehensive architecture review.

Do NOT merely give me another giant "continue until done" prompt.

I want:

A. ROOT CAUSE ANALYSIS

Why do the agents keep stopping even though prompts tell them not to?

Separate:

- LLM behavioural causes;
- process lifecycle causes;
- Hermes architecture causes;
- orchestration-state causes;
- supervisor wiring causes;
- reviewer/provider causes.

B. THE TARGET ARCHITECTURE

Show the exact durable architecture required.

C. STATE MACHINE

Define canonical project/orchestrator states and transitions.

D. LIVENESS INVARIANTS

Define deterministic conditions guaranteeing unfinished work gets another
opportunity to execute.

E. META-DIRECTOR INVOCATION CONTRACT

What every fresh invocation must do.

F. SUPERVISOR CONTRACT

Exactly when it launches/relaunches/wakes/recycles.

G. CHILD TASK/RUN CONTRACT

How worker failures recover.

H. REVIEW CONTRACT

How REJECT becomes rework.

I. MODEL-ESCALATION CONTRACT

When Sol/Opus/free diagnostic workers are invoked autonomously.

J. PROVIDER/SUBSCRIPTION CONTRACT

How temporary unavailability is retried.

K. QUIESCENCE DETECTION

How unfinished + idle becomes a recovery event.

L. EXIT PROTOCOL

How clean exits are made safe.

M. IMPLEMENTATION PLAN

The minimum changes needed to our current system.

N. TEST PLAN

How to prove it genuinely keeps running without human "continue".

O. FAILURE INJECTION PLAN

Kill director.
Kill worker.
Reject review.
Hit provider fixture.
Cause test failure.
Cause proof failure.
Make Meta-Director deliberately return a summary.
Verify project nevertheless continues.

P. RED-TEAM THE DESIGN

Try to find circumstances where it can still silently stop.

=====================================================================
29. THE MOST IMPORTANT QUESTION
=====================================================================

Answer this as explicitly as possible:

WHAT MECHANICAL / DETERMINISTIC COMPONENT MUST EXIST OUTSIDE THE LLM SO THAT
EVEN IF THE LLM DECIDES:

    "I AM DONE RESPONDING"

THE PROJECT STILL GETS ANOTHER META-DIRECTOR INVOCATION IF IT IS NOT ACTUALLY
DONE?

This is the heart of the problem.

=====================================================================
30. CONSTRAINT
=====================================================================

Do not solve this by proposing unlimited paid API usage.

Available subscription-backed and free resources should be used.

Do not make the supervisor an intelligent scheduler.

Do not build an unnecessarily huge distributed platform.

Prefer:

    simple
    deterministic
    inspectable
    restart-safe
    idempotent
    durable

over sophisticated infrastructure.

=====================================================================
31. FINAL DESIGN STANDARD
=====================================================================

The finished architecture must pass this thought experiment:

At 2:00 AM:

    worker fails.

No human present.

System recovers.

At 2:30 AM:

    reviewer rejects.

No human present.

System creates rework.

At 3:00 AM:

    Meta-Director decides to finish its response and exits.

Supervisor sees project incomplete.

Fresh Meta-Director starts.

At 3:20 AM:

    hard technical problem appears.

Meta-Director creates diagnostic case.

Sol and/or Opus analyze it.

Repair work follows.

At 4:00 AM:

    Claude subscription hits temporary session limit.

Review waits.

Other work continues.

At reset:

review automatically resumes.

At 5:00 AM:

    no work is running but project is incomplete.

Quiescence detector wakes Meta-Director.

It finds next work.

At 7:00 AM:

    project is still incomplete.

It is still working.

Eventually:

    deterministic release gate PASS.

Only then does the project stop.

Design me THAT system.

# BEGIN THE ARCHITECTURE REVIEW.
```

===== 2026-09-17 21:44 | session 20260917_213801_1a93d3 | Diagnose autonomous AI system stopping failures =====
@file:`.hermes/attachments/Pasted content (18.3 KB)`

--- Attached Context ---

📄 @file:`.hermes/attachments/Pasted content (18.3 KB)` (4488 tokens)
```
# EMPIRIUM META-DIRECTOR CONTINUITY KERNEL
# FINAL IMPLEMENTATION STEERING PROMPT
# PURPOSE: MAKE AN LLM INVOCATION ENDING NON-TERMINAL

You have an existing functioning Empirium deterministic supervisor.

DO NOT build a new supervisor.
DO NOT build a second scheduler.
DO NOT replace the existing supervisor state architecture.
DO NOT start another broad architectural rewrite.

Your job is to add the smallest deterministic CONTINUATION KERNEL required to
guarantee this property:

    PROJECT INCOMPLETE
    +
    NO GENUINE HUMAN BLOCKER
    +
    NO VALID FUTURE WAIT CONDITION

    =>

    THE PROJECT WILL RECEIVE ANOTHER META-DIRECTOR INVOCATION.

This must remain true even when the current Meta-Director:

- exits successfully;
- writes a final conversational answer;
- crashes;
- hits context limits;
- says "the next action is X" and terminates;
- fails a proof;
- encounters reviewer rejection;
- encounters a worker timeout;
- encounters a difficult architecture problem.

====================================================================
1. FIRST READ THE ARCHITECTURE REVIEW
====================================================================

Read the supplied continuity architecture review in full.

Extract the useful concepts:

- project liveness invariant;
- action-debt invariant;
- progress != heartbeat;
- quiescence detection;
- EXIT_INTENT;
- task/run separation;
- durable review/rework;
- model escalation;
- provider waiting states.

DO NOT blindly implement its proposed new PostgreSQL control plane,
new supervisor rewrite, or any conflicting scheduler responsibilities.

====================================================================
2. CURRENT AUTHORITY BOUNDARIES
====================================================================

Preserve:

DETERMINISTIC SUPERVISOR
    owns process lifecycle only:
    - project registration
    - director liveness
    - heartbeat
    - progress staleness
    - timers
    - backoff
    - process recycle
    - child lease expiry
    - recovery directives
    - quiescence wake
    - deterministic completion observation

META-DIRECTOR
    owns intelligent orchestration:
    - planning
    - task creation
    - work selection
    - project manager creation
    - implementation dispatch
    - rework
    - diagnosis
    - integration decisions
    - expert escalation

HERMES/KANBAN
    remains durable build-task authority where already used.

The supervisor MUST NOT:

- choose implementation tasks;
- write application code;
- create repair tasks;
- review changes;
- select which worker should implement a feature.

It may only wake the Meta-Director and tell it WHY it was woken.

====================================================================
3. ADD THE CONTINUATION INVARIANT
====================================================================

For every registered project:

If:

    releaseGate != PASS
    AND status != PAUSED_BY_USER
    AND no genuine human blocker
    AND retryNotBefore is null or <= now

then:

    exactly one Meta-Director must either be alive
    or be in the process of launching.

There must be no stable state where:

    project incomplete
    AND no legitimate wait condition
    AND no director exists.

This is the central invariant.

Implement it deterministically outside the LLM.

====================================================================
4. CLEAN EXIT MUST NOT MEAN PROJECT COMPLETE
====================================================================

Current Meta-Director process exit status is NOT project status.

These must remain independent:

    process exited 0

does NOT imply:

    project completed.

On any Meta-Director exit:

1. inspect deterministic release gate;
2. inspect user pause;
3. inspect genuine human blocker;
4. inspect retryNotBefore;
5. otherwise relaunch exactly one fresh Meta-Director.

Do this regardless of whether the previous director:

    exited 0
    exited nonzero
    produced a nice summary
    said it had finished
    voluntarily recycled context.

Only the deterministic release gate may suppress relaunch because of
completion.

====================================================================
5. IMPLEMENT EXIT_INTENT
====================================================================

Add a durable per-invocation EXIT_INTENT or equivalent record.

The Meta-Director may write:

    invocationId
    projectId
    generation
    reason
    checkpointId/hash
    nextActions[]
    retryNotBefore
    humanBlocker
    projectCompleteClaim
    writtenAt

Possible reasons:

    CONTEXT_RECYCLE
    INVOCATION_BUDGET
    WAITING_RETRY
    WAITING_HUMAN
    SHIPPED
    UNEXPECTED

The supervisor DOES NOT trust:

    projectCompleteClaim

without independently verifying the release gate.

Interpretation:

SHIPPED
    only accepted if release gate independently PASS.

WAITING_HUMAN
    only accepted when blocker exists and matches narrow blocker schema.

WAITING_RETRY
    accepted only with a valid future retryNotBefore.

CONTEXT_RECYCLE / INVOCATION_BUDGET
    immediate relaunch.

nextActions non-empty
    immediate relaunch unless a legitimate future retry blocks them.

No EXIT_INTENT
    treat as unexpected exit and relaunch.

====================================================================
6. ACTION-DEBT INVARIANT
====================================================================

For an incomplete project checkpoint, require at least one:

    activeActions.length > 0

or:

    nextActions.length > 0

or:

    pendingReviews.length > 0

or:

    pendingRework.length > 0

or:

    retryNotBefore != null

or:

    genuineHumanBlocker != null.

If NONE are true:

emit:

    ORCHESTRATOR_QUIESCENT_WITH_UNFINISHED_PROJECT

This is a recovery condition.

NOT a terminal condition.

====================================================================
7. QUIESCENCE HANDLING WITHOUT DUPLICATE DIRECTORS
====================================================================

DO NOT launch another director while a currently tracked director is alive.

If project is quiescent while director is alive:

1. emit:

       PROJECT_QUIESCENT

   to current generation;

2. give current director a bounded diagnosis grace period;

3. if meaningful progress or a next action appears:
       clear quiescence;

4. if quiescence remains:
       request checkpoint;
       safely recycle current director;
       wait for confirmed process-tree exit;
       launch exactly ONE fresh generation.

Never:

    live director A
    +
    launch director B

for the same project.

====================================================================
8. PROGRESS AND HEARTBEAT REMAIN SEPARATE
====================================================================

Heartbeat:

    process alive.

Progress:

    project meaningfully advanced.

A heartbeat must never automatically advance progress.

If:

    heartbeat fresh
    progress stale

then:

SOFT THRESHOLD:
    issue diagnosis directive.

HARD THRESHOLD:
    if no legitimate long operation:
        checkpoint/recycle director;
        launch fresh director.

====================================================================
9. RETRY WAKE
====================================================================

If:

    retryNotBefore > now

director may be absent.

Persist the retry time.

When:

    now >= retryNotBefore

and:

    project incomplete
    not paused
    no human blocker

supervisor must wake/launch the Meta-Director.

This must survive supervisor restart.

====================================================================
10. HUMAN BLOCKERS ARE NARROW
====================================================================

Valid examples:

- interactive subscription login;
- missing credential only Ash can provide;
- unavoidable privileged OS authorization;
- irreversible business/user decision;
- mandatory private asset unavailable.

NOT human blockers:

- test failure;
- Proof D failure;
- architecture uncertainty;
- reviewer rejection;
- worker timeout;
- model error;
- provider 429;
- known subscription reset;
- merge conflict;
- strange source behavior;
- hard technical debugging.

Those cause more autonomous work.

====================================================================
11. EXPERT DIAGNOSTIC ESCALATION
====================================================================

Add a durable diagnostic-case concept to the Meta-Director layer.

Do NOT put model calls inside the deterministic supervisor.

When Meta-Director encounters a difficult unresolved failure:

create:

    diagnosticCaseId
    question
    expectedBehavior
    observedBehavior
    relevantFiles
    relevantLogs
    hypotheses
    attempts
    status

Then use verified available expert resources.

Escalation ladder:

LEVEL 0:
    Meta-Director local analysis.

LEVEL 1:
    source/log/test inspection.

LEVEL 2:
    focused free diagnostic worker(s).

LEVEL 3:
    strongest VERIFIED subscription-backed expert available.

Possible experts include:

    current Codex/Astra subscription route
    Claude Opus subscription

GPT-5.6 Sol may be used ONLY if the VPS has an independently verified,
non-API-billed programmatic route.

Do not infer that ChatGPT subscription alone provides a usable Sol CLI/API.

If no verified Sol route exists:
    do not block;
    continue with available expert routes.

LEVEL 4:
    independent second opinion where useful.

LEVEL 5:
    reconcile.

LEVEL 6:
    controlled experiment.

LEVEL 7:
    create repair work.

NEEDS_ANALYSIS must result in:

    ANALYSIS WORK

not:

    RETURN TO ASH.

====================================================================
12. REVIEWER AVAILABILITY IS SUBORDINATE
====================================================================

A review may enter:

    WAITING_SUBSCRIPTION

without freezing unrelated runnable project work.

Persist wait state on the review/provider operation.

Only put the whole project into a waiting state if:

    no other runnable action exists.

Opus is reviewer/advisor.

Opus session death must never own project continuation.

====================================================================
13. WORKER FAILURE REMAINS TASK-LEVEL
====================================================================

Meta-Director/wrapper creates worker lease when dispatching.

Supervisor does NOT dispatch workers.

Supervisor observes lease.

On expiry:

    LEASE_EXPIRED
    → recovery directive.

Meta-Director consumes directive and decides:

    salvage
    retry
    create new run
    split task
    change free model
    diagnose.

Do not create rework directly inside supervisor.

====================================================================
14. DO NOT IMPLEMENT WRITABLE DB FALLBACK
====================================================================

Do not create a second mutable authority automatically when PostgreSQL is
unavailable.

Maintain one canonical authority for each layer.

Supervisor control state may continue using its existing durable local store.

Finished Empirium product state may use its accepted PostgreSQL architecture.

Do not silently switch writes between two authorities.

====================================================================
15. TIME SEMANTICS
====================================================================

Do not assume UTC prevents clock jumps.

Use monotonic timing where appropriate for:

    heartbeat TTL
    progress TTL
    grace periods
    lock waits
    active-process timeouts.

Use persisted wall-clock timestamps for:

    retryNotBefore
    audit events
    human inspection.

After restart, apply sanity guards around persisted time values.

====================================================================
16. BUDGETED META-DIRECTOR INVOCATIONS
====================================================================

Prefer disposable invocations over trying to keep one context alive forever.

Support configurable invocation budget based on:

    elapsed time
    context pressure
    action count

Before controlled recycle:

    checkpoint
    write EXIT_INTENT
    persist next actions
    exit.

Supervisor immediately launches successor when project remains runnable.

Do not hard-code 30 or 60 minutes unless evidence supports it.

Make it configurable.

====================================================================
17. THE MOST IMPORTANT FAILURE-INJECTION TEST
====================================================================

Create a disposable supervised test.

Director generation N must deliberately:

1. read project;
2. discover:

       Proof D failed

3. write:

       nextAction = DIAGNOSE_PROOF_D

4. output a perfectly normal final-style summary such as:

       "Proof D failed. The next action is to diagnose the classification race."

5. exit code 0.

THIS IS THE FAILURE MODE WE CARE ABOUT.

Expected deterministic behavior:

6. supervisor sees:

       release gate != PASS
       no human blocker
       no future retry
       director absent

7. supervisor launches generation N+1 automatically;

8. generation N+1 reads:

       nextAction = DIAGNOSE_PROOF_D

9. generation N+1 ACTUALLY performs the diagnostic action;

10. it must not merely restate the next action;

11. it generates progress;

12. project continues without user input.

If this test does not pass:

the continuity problem is NOT solved.

====================================================================
18. ADDITIONAL FAILURE INJECTION
====================================================================

Prove:

A. DIRECTOR CLEAN EXIT
    incomplete → automatic relaunch.

B. DIRECTOR CRASH
    incomplete → automatic relaunch.

C. CONTEXT RECYCLE
    checkpoint → exit → automatic successor.

D. PROOF FAILURE
    failure → diagnosis task → repair/rerun.

E. WORKER TIMEOUT
    lease expiry → recovery directive → replacement run.

F. REVIEW REJECT
    durable CHANGES_REQUESTED → rework.

G. REVIEW SESSION LIMIT
    review waits/retries;
    project continues other work.

H. ALL CURRENT WORK FINISHES BUT PROJECT INCOMPLETE
    quiescence detected;
    Meta-Director wakes and finds next work.

I. WAIT TIMER
    director absent until retryNotBefore;
    automatically wakes afterward.

J. SUPERVISOR RESTART
    liveness policy reconstructs and continues.

No test may require Ash to type:

    continue.

====================================================================
19. REAL PROJECT SAFETY
====================================================================

Do all continuity testing with disposable orchestration fixtures first.

Do NOT corrupt:

    /home/ash/empirium-studio

or its existing rejected implementation.

Once all continuity tests pass:

apply continuation policy to:

    empirium-studio-workforce

Do not create a second real project registration.

====================================================================
20. COMPLETION AUTHORITY
====================================================================

Only deterministic:

    FINAL_RELEASE_GATE.status == PASS
    AND FINAL_RELEASE_GATE.exitCode == 0
    AND exact release SHA matches

may allow the supervisor to stop relaunching because project is complete.

A Meta-Director saying:

    DONE
    FINISHED
    SHIPPED
    NOTHING ELSE TO DO

has zero completion authority.

====================================================================
21. DEFINITION OF DONE FOR THIS CONTINUITY FIX
====================================================================

This task is complete only if:

[ ] existing supervisor tests still pass;

[ ] real project registration remains correct;

[ ] clean director exit while incomplete causes relaunch;

[ ] crash causes relaunch;

[ ] EXIT_INTENT implemented or equivalent proven;

[ ] nextAction survives process replacement;

[ ] action-debt invariant enforced;

[ ] quiescence triggers recovery;

[ ] quiescence does not launch concurrent duplicate director;

[ ] retryNotBefore wakes project automatically;

[ ] progress and heartbeat remain separate;

[ ] worker lease responsibility remains outside supervisor scheduling;

[ ] reviewer waiting does not unnecessarily freeze unrelated work;

[ ] expert escalation is autonomous;

[ ] only verified subscription/free expert routes are used;

[ ] no paid API fallback introduced;

[ ] forced "I have given my final answer" test automatically continues;

[ ] zero manual "continue" prompts required.

====================================================================
22. AFTER CONTINUITY IS PROVEN
====================================================================

Do not stop and tell Ash:

    "The continuity system is now ready. Next we should resume Proof D."

Instead:

if continuity tests pass and no human blocker exists:

    immediately resume the unfinished orchestration-validation work
    under the supervisor-controlled real Meta-Director.

That means:

    diagnose Proof D
    repair it
    rerun it
    rerun remaining required proofs
    continue the Empirium build

The very purpose of this task is to eliminate:

    "next step is X"

as a terminal response.

If you know X and X is authorized:

    DO X.

====================================================================
23. FINAL RULE
====================================================================

An LLM invocation ending is NOT a project lifecycle event.

A conversational final answer is NOT a release event.

A worker timeout is NOT a project completion event.

A reviewer rejection is NOT a terminal event.

A failed proof is NOT a terminal event.

For this project:

    ONLY DETERMINISTIC RELEASE PASS ENDS NORMAL EXECUTION.

Everything else is:

    state
    evidence
    and another transition.

IMPLEMENT THE CONTINUATION KERNEL,
PROVE IT WITH FAILURE INJECTION,
THEN ALLOW THE REAL SUPERVISED META-DIRECTOR TO CONTINUE THE BUILD.
```

===== 2026-09-17 21:50 | session 20260917_215008_8d8dd7 | Install temporary project dead-man watchdog =====
@file:`.hermes/attachments/Pasted content (21.2 KB)`

--- Attached Context ---

📄 @file:`.hermes/attachments/Pasted content (21.2 KB)` (5186 tokens)
```
# =====================================================================
# TEMPORARY CHAT-PROJECT DEAD-MAN WATCHDOG
# PROJECTS:
#   1. Empirium OS — chat "Analyze prompts with Opus 5"
#   2. Nailify — chat "Implement Nailed It MVP V2"
#
# PURPOSE:
# WHILE THE FULL META-ORCHESTRATOR CONTINUITY SYSTEM IS BEING COMPLETED,
# INSTALL A SIMPLE INDEPENDENT CRON-BASED FALLBACK THAT PREVENTS THESE
# TWO ACTIVE PROJECTS FROM QUIETLY STOPPING.
# =====================================================================

You are installing a TEMPORARY SECONDARY DEAD-MAN WATCHDOG for two currently
running project chats.

This is deliberately independent of the large supervisor-continuity work
already occurring elsewhere.

DO NOT interfere with:

    empirium-studio-workforce

That project is already registered with the proper Empirium Supervisor and is
currently supervisor-launched.

This watchdog concerns ONLY:

PROJECT 1

    logical name:
        empirium-os

    product:
        Empirium OS

    current chat title:
        Analyze prompts with Opus 5

PROJECT 2

    logical name:
        nailify

    product:
        Nailify

    current chat title:
        Implement Nailed It MVP V2

IMPORTANT CURRENT INCIDENT:

    Empirium OS appears to have STOPPED AGAIN.

Therefore after installing the watchdog, immediately investigate and wake/resume
Empirium OS if it is genuinely incomplete and inactive.

Do not merely install the cron job and wait for its first scheduled run.

=====================================================================
1. OBJECTIVE
=====================================================================

I want a simple fallback invariant:

    PROJECT ENABLED
    +
    PROJECT NOT FINISHED
    +
    PROJECT NOT PAUSED
    +
    NO GENUINE HUMAN BLOCKER
    +
    NO VALID FUTURE RETRY WAIT
    +
    NO ACTIVE CONTROLLER/WORK

        =>

    WAKE / RESUME THAT PROJECT.

This watchdog exists because AI chats repeatedly produce useful intermediate
reports and then stop rather than continuing.

The watchdog must make:

    "the chat stopped"

different from:

    "the project finished."

=====================================================================
2. DO NOT TRUST CHAT TITLE AS PERMANENT IDENTITY
=====================================================================

The titles:

    Analyze prompts with Opus 5
    Implement Nailed It MVP V2

are DISCOVERY HINTS.

Use them now to locate the real corresponding Hermes/Studio/chat/session
records.

Discover, using actual local source/storage/config:

    chat ID
    session ID
    conversation ID
    project ID if one exists
    execution/controller ID
    workspace/repository root
    actual resume mechanism
    model/profile
    last activity
    current process if any

Do not guess database/table/file locations.

Inspect Hermes source/config first.

Once positively identified, store stable IDs in the watchdog registry.

Future checks should primarily use stable IDs, not title text.

Titles may remain as human-readable labels.

=====================================================================
3. FIRST DISCOVER HOW A HERMES CHAT IS ACTUALLY RESUMED
=====================================================================

Before writing wake logic, determine the REAL supported continuation mechanism.

Search the locally installed Hermes/Studio source and CLI for mechanisms such
as:

    resume session
    continue conversation
    send message to conversation
    reopen execution
    run chat
    invoke agent against existing conversation
    conversation ID
    session ID
    gateway API
    internal HTTP endpoint
    CLI resume command

Do NOT invent a command.

Do NOT automate mouse-clicking the browser if a stable local API/CLI/database
route exists.

Preferred order:

1. supported Hermes/gateway continuation API;
2. supported Hermes CLI/session-resume mechanism;
3. existing internal endpoint used by the UI;
4. fresh controller invocation from durable checkpoint if existing session
   genuinely cannot be programmatically resumed.

Avoid brittle UI automation.

=====================================================================
4. DETERMINE WHAT "RUNNING" MEANS
=====================================================================

Do not merely ask:

    "does the chat exist?"

Determine whether useful execution is actually occurring.

For each project, capture where available:

    controller/session ID
    process PID
    process start fingerprint
    current run ID
    last activity timestamp
    last model/tool action timestamp
    last meaningful progress timestamp
    active child executions
    queued work
    retry/wait state

Classify project as one of:

    ACTIVE
    IDLE_BUT_SESSION_ALIVE
    STOPPED
    WAITING_RETRY
    WAITING_HUMAN
    PAUSED
    FINISHED
    UNKNOWN

UNKNOWN must NOT automatically be interpreted as FINISHED.

=====================================================================
5. CREATE A SMALL WATCHDOG REGISTRY
=====================================================================

Create something similar to:

    /home/ash/.config/empirium-chat-watchdog/projects.json

Use actual resolved IDs.

Conceptually:

{
  "schemaVersion": 1,
  "projects": [
    {
      "id": "empirium-os",
      "label": "Empirium OS",
      "discoveryTitle": "Analyze prompts with Opus 5",
      "chatId": "<DISCOVER>",
      "sessionId": "<DISCOVER>",
      "root": "<DISCOVER>",
      "enabled": true
    },
    {
      "id": "nailify",
      "label": "Nailify",
      "discoveryTitle": "Implement Nailed It MVP V2",
      "chatId": "<DISCOVER>",
      "sessionId": "<DISCOVER>",
      "root": "<DISCOVER>",
      "enabled": true
    }
  ]
}

Do not put passwords, tokens or API keys in this registry.

=====================================================================
6. PROJECT CONTROL FILE
=====================================================================

For each project maintain a tiny deterministic watchdog record.

Suggested location:

    ~/.local/state/empirium-chat-watchdog/projects/<project-id>.json

Conceptual schema:

{
  "projectId": "empirium-os",
  "enabled": true,

  "terminal": false,
  "terminalReason": null,

  "paused": false,

  "humanBlocker": null,

  "retryNotBefore": null,

  "lastObservedActivityAt": null,
  "lastMeaningfulProgressAt": null,

  "lastWakeAttemptAt": null,
  "lastWakeResult": null,

  "consecutiveWakeFailures": 0
}

=====================================================================
7. DO NOT USE A SIMPLE LLM-CHECKED "DONE" BOX
=====================================================================

Ash originally suggested:

    Luna checks a box when finished.

Do NOT let a single conversational statement:

    "done"

permanently disable the watchdog.

Use a stronger completion marker.

For now, project terminal state requires:

    terminal = true

AND a completion record containing:

    projectId
    completionReason
    completedAt
    exact current revision/commit where applicable
    definitionOfDoneEvidence
    verifier

Where a project has deterministic tests/release criteria, verify them.

If no deterministic release gate currently exists, require at least:

    agent claims complete
    +
    explicit final verification/review result

before setting terminal=true.

The watchdog itself must never infer FINISHED merely from:

    chat process exited
    final assistant response
    no activity
    "I've completed the task"
    exit code 0

Those mean only that execution stopped.

=====================================================================
8. WATCHDOG SCRIPT
=====================================================================

Create:

    /home/ash/.local/bin/empirium-chat-watchdog

Prefer a small deterministic implementation:

    Python
or
    Node.js

No LLM inside the watchdog.

Responsibilities:

FOR EACH ENABLED PROJECT:

1. load registry/control state;

2. if terminal == true:
       independently validate terminal record still applies where practical;
       do nothing;

3. if paused == true:
       do nothing;

4. if genuine humanBlocker exists:
       do nothing;

5. if retryNotBefore > now:
       do nothing;

6. inspect actual Hermes/session/process state;

7. determine whether project is actively doing useful work;

8. if ACTIVE:
       record observation;
       do nothing;

9. if STOPPED/QUIESCENT and project incomplete:
       invoke the project's supported WAKE/RESUME path;

10. record exact result.

=====================================================================
9. IMPORTANT: IDLE SESSION != ACTIVE PROJECT
=====================================================================

A chat merely existing is insufficient.

If the chat/controller exists but:

    no active task
    no tool call
    no child
    no progress
    no legitimate wait

for longer than a conservative configurable threshold:

classify:

    QUIESCENT.

Then wake it.

Initial temporary thresholds may be conservative, e.g.:

    check every 2 minutes

and:

    quiescence threshold approximately 5–10 minutes

but derive sensible values from actual Hermes execution timing.

Do not kill an active long-running tool command.

Inspect child process/tool activity where possible.

=====================================================================
10. WAKE INSTRUCTION
=====================================================================

When an incomplete project needs waking, the continuation message/invocation
must NOT merely say:

    "continue"

Use a strong generic continuation instruction such as:

------------------------------------------------------------

You are being automatically resumed by the project dead-man watchdog.

The project is still marked INCOMPLETE.

Do not return control to Ash merely because the previous invocation ended.

First reconstruct current state from:

- this conversation/session;
- durable project files;
- Git;
- task state;
- previous outputs;
- tests;
- pending reviews;
- active/failed workers.

Then determine the next executable action.

If the previous invocation ended by saying:

    "the next step is X"

EXECUTE X.

Do not merely explain X again.

If a task failed:

diagnose and repair/retry.

If a reviewer rejected:

create and execute rework.

If a difficult technical issue exists:

inspect source/logs and use available expert AI/subagents where authorized.

Only stop normal execution for:

    verified project completion;
    genuine human-only blocker;
    explicit user pause;
    valid future retry/wait condition.

Otherwise continue doing the work.

Before voluntarily ending while incomplete, persist:

    exact current state
    exact next action
    any retry/wait reason.

------------------------------------------------------------

Add project-specific context/IDs as appropriate.

=====================================================================
11. EMPIRIUM OS — IMMEDIATE PRIORITY
=====================================================================

Empirium OS has reportedly STOPPED AGAIN.

After installation/discovery, investigate it immediately.

Find the session corresponding to:

    Analyze prompts with Opus 5

Determine:

    last activity
    last assistant result
    whether it declared completion
    whether there is a next action
    whether a child/model call failed
    whether Opus/session limit occurred
    whether execution merely returned normally
    whether the project is actually complete

If:

    incomplete
    AND no genuine blocker
    AND not currently active

WAKE IT IMMEDIATELY.

Do not wait for cron.

Log:

    EMPIRIUM_OS_EMERGENCY_WAKE

with:

    previous last activity
    reason considered stopped
    resume mechanism
    result

=====================================================================
12. NAILIFY
=====================================================================

Resolve and monitor the session titled:

    Implement Nailed It MVP V2

Do not disturb it if it is genuinely active.

If it later stops while incomplete:

wake/resume automatically using the same mechanism.

=====================================================================
13. DO NOT TOUCH EMPIRIUM STUDIO WORKFORCE
=====================================================================

Explicit exclusion:

    empirium-studio-workforce

The proper deterministic supervisor already controls this project.

The temporary chat watchdog must not:

    relaunch it
    send messages to it
    pause it
    kill it
    modify its state
    interpret its release gate
    create another controller

If discovered in Hermes state, ignore it.

=====================================================================
14. CRON FALLBACK
=====================================================================

Install ONE cron entry, not one cron entry per project.

Use `flock` or equivalent so watchdog invocations cannot overlap.

Preferred approximate cadence:

    every 2 minutes

Conceptually:

    */2 * * * * flock -n <lock> /home/ash/.local/bin/empirium-chat-watchdog

Use actual paths and environment required on this VPS.

Do not assume interactive shell PATH.

Use absolute paths where practical.

Capture stdout/stderr to a bounded log or journal-safe location.

=====================================================================
15. WATCHDOG FOR THE WATCHDOG
=====================================================================

Cron itself is merely a fallback.

At each run also verify the main Empirium Supervisor service:

    empirium-workforce-supervisor.service

If it is unexpectedly inactive:

attempt:

    systemctl --user start empirium-workforce-supervisor.service

Then verify health.

However:

the chat watchdog must NOT manage individual projects already owned by that
supervisor.

This is only service-level recovery.

=====================================================================
16. THUNDERING-HERD / DUPLICATE WAKE PROTECTION
=====================================================================

Never wake the same project every two minutes while a previous wake is still
starting.

Use a per-project lock/cooldown.

Record:

    wakeInProgress
    wakeAttemptId
    wakeStartedAt

Before another wake:

verify previous wake did not successfully produce a controller.

Recommended behavior:

WAKE REQUEST
    ↓
grace window
    ↓
recheck actual state
    ↓
only retry if still stopped.

No duplicate Meta-Controllers.

=====================================================================
17. FAILED WAKE ESCALATION
=====================================================================

If one wake attempt fails:

    record failure
    retry later.

If several consecutive wake attempts fail:

    inspect reason.

Classify:

    AUTH_REQUIRED
    SESSION_LIMIT
    HERMES_UNAVAILABLE
    SESSION_NOT_FOUND
    CONTROLLER_LAUNCH_FAILED
    UNKNOWN

For recoverable cases:

    bounded retry/backoff.

For genuine login/human action:

    humanBlocker.

Do NOT endlessly spawn processes.

Do NOT silently switch to paid APIs.

=====================================================================
18. LOGGING
=====================================================================

Create:

    ~/.local/state/empirium-chat-watchdog/events.jsonl

Record meaningful events only:

    WATCHDOG_STARTED
    PROJECT_DISCOVERED
    PROJECT_ACTIVE
    PROJECT_QUIESCENT
    WAKE_REQUESTED
    WAKE_SUCCEEDED
    WAKE_FAILED
    PROJECT_WAITING
    PROJECT_BLOCKED_HUMAN
    PROJECT_TERMINAL
    SUPERVISOR_RESTARTED

Do not append a heartbeat line every two minutes forever if nothing changes.

Bound/rotate logs.

=====================================================================
19. COMMANDS
=====================================================================

Provide simple commands, for example:

    empirium-chat-watchdog status

    empirium-chat-watchdog check

    empirium-chat-watchdog pause empirium-os

    empirium-chat-watchdog resume empirium-os

    empirium-chat-watchdog pause nailify

    empirium-chat-watchdog resume nailify

    empirium-chat-watchdog wake empirium-os

    empirium-chat-watchdog wake nailify

    empirium-chat-watchdog logs

Do not require editing JSON manually for normal operation.

=====================================================================
20. TEST THE ACTUAL WAKE PATH
=====================================================================

Before declaring success, prove with a disposable/safe test that:

1. active project is NOT duplicated;

2. stopped/incomplete project is detected;

3. watchdog invokes correct resume mechanism;

4. resumed controller performs a real next action;

5. next cron tick sees it active and does NOT duplicate it;

6. terminal project is left alone;

7. paused project is left alone;

8. retryNotBefore is respected;

9. human blocker is respected;

10. main Empirium Supervisor projects are excluded.

=====================================================================
21. SPECIAL "AGENT JUST GAVE A SUMMARY" TEST
=====================================================================

This is critical.

Create a safe disposable test where an AI/controller ends with:

    "The next action is to perform X."

and then exits.

Project remains incomplete.

Expected:

    watchdog observes stopped project
    → resumes project
    → continuation reads previous state
    → EXECUTES X

It must not merely answer:

    "Yes, X is the next action."

This is the behaviour this fallback exists to defeat.

=====================================================================
22. COMPLETION SEMANTICS
=====================================================================

Do not make the checkbox concept a raw boolean an LLM can casually flip.

Use:

    COMPLETE CLAIM
        ↓
    VERIFY
        ↓
    TERMINAL MARKER

If verification later becomes invalid due to new changes:

clear/reject terminal state and resume monitoring.

There should always be a manual operator override available, but the default
must fail toward:

    unfinished

rather than:

    silently finished.

=====================================================================
23. SECURITY / BILLING
=====================================================================

No new paid inference.

Do not expose:

    API keys
    subscription tokens
    passwords

in registry/log files.

Do not modify:

    AppArmor
    firewall
    DNS
    system-wide security

for this temporary watchdog.

Do not require sudo for normal watchdog operation.

=====================================================================
24. DELIVERABLES
=====================================================================

Produce:

    ~/.local/bin/empirium-chat-watchdog

    ~/.config/empirium-chat-watchdog/projects.json

    ~/.local/state/empirium-chat-watchdog/

    cron entry

and:

    ~/.local/state/empirium-chat-watchdog/INSTALLATION_REPORT.md

The report must contain:

- exact discovered chat/session IDs;
- actual resume mechanism;
- actual project roots;
- cron entry;
- quiescence threshold;
- duplicate-wake protection;
- current status of Empirium OS;
- current status of Nailify;
- whether Empirium OS required emergency wake;
- whether that wake succeeded;
- confirmation empirium-studio-workforce is excluded.

=====================================================================
25. FINAL RESPONSE
=====================================================================

Return:

WATCHDOG:
ACTIVE / FAILED

CRON:
INSTALLED / FAILED

CHECK INTERVAL:
<value>

EMPIRIUM OS:
ACTIVE / WOKEN / WAITING / HUMAN_BLOCKED / COMPLETE / UNKNOWN

EMPIRIUM OS CHAT ID:
<id>

EMPIRIUM OS SESSION ID:
<id if applicable>

EMPIRIUM OS EMERGENCY WAKE:
PASS / NOT_REQUIRED / FAIL

NAILIFY:
ACTIVE / WOKEN / WAITING / HUMAN_BLOCKED / COMPLETE / UNKNOWN

NAILIFY CHAT ID:
<id>

NAILIFY SESSION ID:
<id if applicable>

EMPIRIUM STUDIO WORKFORCE:
EXCLUDED — CONTROLLED BY MAIN SUPERVISOR

NEXT AUTOMATIC CHECK:
<time>

HUMAN ACTION REQUIRED:
NONE
or exact unavoidable action.

=====================================================================
26. BEGIN NOW
=====================================================================

First:

1. discover the two exact chats by their supplied titles;
2. resolve stable IDs;
3. investigate why Empirium OS stopped;
4. install the watchdog;
5. perform an immediate check;
6. wake Empirium OS if incomplete/stopped;
7. verify Nailify is still active;
8. install cron;
9. test duplicate-wake protection;
10. leave the watchdog running.

Do not stop after saying:

    "Empirium OS appears stopped and should be resumed."

If it can be resumed safely:

    RESUME IT.

BEGIN.
```

===== 2026-09-17 21:54 | session 20260917_213801_1a93d3 | Diagnose autonomous AI system stopping failures =====
keep going, do not give up until this task os completely done, all definaitions of success are met, ALL OF THEm

===== 2026-09-17 21:57 | session 20260917_191500_df556c | AI Staffforce =====
BUT YOU HAVE FUCKING STOPPED, THE ENTIRE POINT OF THE SUPERVISER IS SO THAT YOU DONT STOPP UNTIL THE FUCKING TASK IS DONE, THE APP IS NOT MADE, IN THE WAY I HAVE DESCRIBED NOT EVEN FUCKING CLOSE SO PLEASE FUCKING KEEP STICKING TO THE FUCKING PROMPTS UNTILL THIS JOB IS FUCKING FINSHED

===== 2026-09-17 22:01 | session 20260917_215008_8d8dd7 | Install temporary project dead-man watchdog =====
FINISH THIS PROJECT

===== 2026-09-17 22:03 | session 20260917_191500_df556c | AI Staffforce =====
keep going, do not give up until this task os completely done, all definaitions of success are met, ALL OF THEM

===== 2026-09-17 22:05 | session 20260917_191500_df556c | AI Staffforce =====
where is this happening? i cant see any agents or any work being done here

===== 2026-09-17 22:06 | session 20260917_191500_df556c | AI Staffforce =====
and what model is the meta-orchastrator using

===== 2026-09-17 22:06 | session 20260917_191500_df556c | AI Staffforce =====
wow, problem

===== 2026-09-17 22:06 | session 20260917_191500_df556c | AI Staffforce =====
cna not be using astra for meta-orchastrator

===== 2026-09-17 22:06 | session 20260917_191500_df556c | AI Staffforce =====
thats the job of gpt luna

===== 2026-09-17 22:07 | session 20260917_191500_df556c | AI Staffforce =====
change it right now

===== 2026-09-17 22:08 | session 20260917_215008_8d8dd7 | Install temporary project dead-man watchdog =====
so this will now keep an eye on these 2 projects and make sure they continue until theprojects are complete. its not really enough for the watch dog to wake up these chats, it needs to actively ask "Whats still left to do of this project? let's get that work done now" and th ellm in those chats take it form there

===== 2026-09-17 22:16 | session 20260917_215008_8d8dd7 | Install temporary project dead-man watchdog =====
here are the plan for the 2 projects so you defintely know what you are keeping track of

===== 2026-09-17 22:17 | session 20260917_191500_df556c | AI Staffforce =====
so list all of the models you will be using and at what teir of the orchastration

===== 2026-09-17 22:22 | session 20260917_213801_1a93d3 | Diagnose autonomous AI system stopping failures =====
so is this 100% fixed and implimented?

===== 2026-09-17 22:22 | session 20260917_191500_df556c | AI Staffforce =====
and its still going?

===== 2026-09-17 22:22 | session 20260917_213801_1a93d3 | Diagnose autonomous AI system stopping failures =====
you arent allowed to use credits anyway, onlu freellmapi

===== 2026-09-17 22:24 | session 20260917_213801_1a93d3 | Diagnose autonomous AI system stopping failures =====
@file:`.hermes/attachments/Pasted content (8.8 KB)`

--- Attached Context ---

📄 @file:`.hermes/attachments/Pasted content (8.8 KB)` (2171 tokens)
```
STOP. This is a provider-routing bug, not a prompt-behaviour problem.

The application is STILL attempting to use OpenRouter.

Current reproduced error:

"Out of credits
Your openrouter account has no credits left. Top up or switch provider, then send again."

I have repeatedly specified that OpenRouter must NOT be used.

Do NOT simply change the currently selected model.
Do NOT modify a system prompt telling the agent not to use OpenRouter.
Do NOT declare this fixed after finding one OpenRouter setting.

Provider routing occurs below the agent prompt. I need OpenRouter removed from the complete execution graph.

OBJECTIVE

For this application:

OPENROUTER MUST NEVER BE CALLED.

This prohibition applies to:

- main chat model
- supervisor/orchestrator
- worker agents
- delegated agents
- subagents
- crews
- background agents
- fallback models
- fallback providers
- retry logic
- auxiliary models
- context compression
- title generation
- vision
- screenshot analysis
- approval classification
- MCP routing/classification
- skills matching
- triage
- kanban decomposition
- profile generation
- memory summarisation
- research workers
- coding workers
- any legacy provider layer
- any frontend provider selection
- any backend provider selection

The replacement provider/model system we have explicitly configured must be used instead.

PHASE 1 — FORENSIC AUDIT

Before changing anything, locate EVERY possible OpenRouter route.

Search the entire relevant installation, application source, Hermes configuration,
environment configuration and persisted application state for at minimum:

openrouter
OpenRouter
OPENROUTER
openrouter.ai
OPENROUTER_API_KEY
provider: openrouter
provider="openrouter"
provider = "openrouter"
fallback_providers
fallback_model
fallback_chain
provider: auto
provider="auto"
provider = "auto"

Inspect at minimum:

~/.hermes/config.yaml
~/.hermes/.env

all Hermes config files

systemd services
systemd Environment directives
systemd EnvironmentFile files

Docker/docker-compose configuration if present

shell environment
service environment
application .env files
.env.local
.env.production
.env.development

backend configuration
frontend configuration

database-stored provider preferences

browser/local persisted chat/provider settings if applicable

supervisor configuration

agent configuration

crew configuration

subagent/delegation configuration

fallback configuration

auxiliary model configuration

retry configuration

legacy configuration

OpenAI-compatible routing adapters

any provider registry/router code

any hard-coded OpenRouter URLs

Do not assume ~/.hermes/config.yaml is the only source.

PHASE 2 — TRACE THE FAILED REQUEST

Reproduce the exact user action that currently creates the:

"OpenRouter account has no credits left"

error.

Trace that request from:

UI
→ API route
→ conversation/session configuration
→ orchestrator/supervisor
→ provider resolver
→ fallback resolver
→ actual HTTP client

Identify EXACTLY why OpenRouter was selected.

If two OpenRouter error cards are generated from one user message, determine why two provider requests are being made.

Report the call sites.

PHASE 3 — REMOVE OPENROUTER FROM THE EXECUTION GRAPH

Modify the implementation so OpenRouter is not an eligible provider for this application.

Do not merely make another provider higher priority.

Do not leave OpenRouter as the final fallback.

Do not leave OpenRouter available through "auto".

Do not leave OpenRouter inherited by child agents.

Do not leave OpenRouter in auxiliary fallback chains.

Do not silently fall back to OpenRouter when the desired free API fails.

All applicable fallback chains must explicitly contain ONLY providers that we have approved.

If no approved provider succeeds, return a clear error.

NEVER fall back to OpenRouter.

Audit Hermes' separate delegation configuration.

If delegation.fallback_providers inherits an unwanted parent chain, explicitly configure it.

Audit every auxiliary provider slot.

Where appropriate, explicitly pin the approved provider instead of using ambiguous "auto" provider resolution.

PHASE 4 — ADD A HARD SAFETY GUARD

This must not depend solely on configuration being correct.

Add a deterministic provider policy before provider execution.

Conceptually:

FORBIDDEN_PROVIDERS = {
    "openrouter"
}

Before executing ANY LLM request:

resolved_provider = resolve_provider(...)

if normalized(resolved_provider) in FORBIDDEN_PROVIDERS:
    raise ProviderPolicyViolation(
        "OpenRouter is disabled for this application"
    )

This check must occur AFTER provider/fallback resolution but BEFORE the HTTP request.

It must therefore protect against:

- accidental configuration changes
- fallback selection
- inherited settings
- legacy sessions
- worker agents
- new chats
- auxiliary requests
- supervisor requests

If endpoints can bypass the provider name, also reject requests whose resolved
base URL/domain points to OpenRouter, including:

openrouter.ai
https://openrouter.ai/api/
https://openrouter.ai/api/v1

Do not rely only on string matching if the provider registry provides a canonical
provider ID.

PHASE 5 — REMOVE STALE SESSION STATE

Determine whether existing chats persist:

provider
model
base_url
fallback chain
agent profile

If old chats can retain OpenRouter after global configuration changes, migrate or
invalidate that stale state.

A new application setting must apply consistently to:

existing chats
new chats
subagents
background jobs

PHASE 6 — TEST

Do not state that this is fixed without executing tests.

At minimum test:

1. New normal chat
2. Existing chat
3. Supervisor request
4. Worker/subagent request
5. Delegated task
6. Tool/MCP task
7. Long conversation triggering compression
8. Automatic title generation
9. Retry after intentional provider failure
10. Fallback after intentional provider failure
11. Restart application and repeat
12. Restart Hermes/service and repeat

CRITICAL TEST:

Make the configured preferred provider intentionally fail.

Verify that the system DOES NOT attempt OpenRouter.

It should either:

A. use another explicitly approved provider

or

B. fail with our own provider-unavailable error.

It must NEVER produce an OpenRouter response.

PHASE 7 — NETWORK-LEVEL VERIFICATION

Instrument/log outbound LLM requests during the test suite.

Record:

timestamp
request type
agent
provider
model
base URL/hostname
whether fallback occurred

There must be ZERO requests to:

openrouter.ai

during the complete test suite.

Search the logs afterwards for:

openrouter
openrouter.ai

Expected result: ZERO outbound OpenRouter requests.

PHASE 8 — RESTART AND PERSISTENCE TEST

Restart all affected services.

Restart the application.

Start a completely fresh chat.

Run another request.

Confirm the provider remains correct after restart.

This is necessary because an in-memory change does not constitute a fix.

DEFINITION OF DONE

This task is NOT complete until ALL of the following are true:

[ ] Root cause of the current OpenRouter request identified
[ ] Reason for duplicate OpenRouter errors identified
[ ] Main model does not use OpenRouter
[ ] Supervisor does not use OpenRouter
[ ] Workers/subagents do not use OpenRouter
[ ] Delegation does not use OpenRouter
[ ] Auxiliary tasks do not use OpenRouter
[ ] Compression does not use OpenRouter
[ ] Title generation does not use OpenRouter
[ ] Fallback chains do not contain OpenRouter
[ ] "auto" routing cannot resolve to OpenRouter for this application
[ ] Existing stale sessions cannot retain OpenRouter routing
[ ] OpenRouter base URL cannot be invoked
[ ] Deterministic runtime OpenRouter prohibition implemented
[ ] Preferred-provider failure test passes
[ ] New-chat test passes
[ ] Existing-chat test passes
[ ] Restart persistence test passes
[ ] Complete outbound-request logs contain zero OpenRouter requests

FINAL REPORT

When finished give me:

1. Root cause
2. Every OpenRouter reference discovered
3. Which references were legitimate/non-routing references
4. Every routing reference removed or changed
5. Files changed
6. Configuration changed
7. Runtime guard implementation
8. Existing-session migration/fix
9. Tests executed
10. Test results
11. Outbound provider request log
12. Proof that an intentional provider failure does NOT invoke OpenRouter
13. Proof that the fix survives a full restart

DO NOT ask me whether you should continue after the audit.

Audit, fix, restart, test and verify autonomously.

Do not say "fixed" merely because configuration looks correct.

The only acceptable proof is successful runtime testing showing ZERO OpenRouter
requests.
```

===== 2026-09-17 22:26 | session 20260917_213801_1a93d3 | Diagnose autonomous AI system stopping failures =====
so is this 100% fixed and implimented now?

===== 2026-09-17 22:26 | session 20260917_213801_1a93d3 | Diagnose autonomous AI system stopping failures =====
so is this 100% fixed and implimented now?

[System: The active model for this chat has changed to auto via provider freellmapi. From this point forward, use this runtime metadata when answering questions about what model/provider is active.]

try now

===== 2026-09-17 22:27 | session 20260917_191500_df556c | AI Staffforce =====
and its still going now?

===== 2026-09-17 22:27 | session 20260917_191500_df556c | AI Staffforce =====
and its still going now?

and its still going now ?

[System: The active model for this chat has changed to thinkingmachines/inkling:free via provider openrouter. From this point forward, use this runtime metadata when answering questions about what model/provider is active.]

still going?

===== 2026-09-17 22:28 | session 20260917_191500_df556c | AI Staffforce =====
and its still going now ?

===== 2026-09-17 22:31 | session 20260917_215008_8d8dd7 | Install temporary project dead-man watchdog =====
i triggered the cron job, did it work

===== 2026-09-17 22:32 | session 20260917_191500_df556c | AI Staffforce =====
still going?

===== 2026-09-17 22:37 | session 20260917_213801_1a93d3 | Diagnose autonomous AI system stopping failures =====
can we /loop it so it just keeps testing out new calibrations until it works

===== 2026-09-17 22:38 | session 20260917_215008_8d8dd7 | Install temporary project dead-man watchdog =====
i just got a notification saying this failed, why

===== 2026-09-17 22:43 | session 20260917_215008_8d8dd7 | Install temporary project dead-man watchdog =====
this has nothing to do with empirium OS? its the nailify app and ai stafforce

===== 2026-09-17 22:48 | session 20260917_191500_df556c | AI Staffforce =====
still going? any progress since last prompt?

===== 2026-09-17 22:49 | session 20260917_213801_1a93d3 | Diagnose autonomous AI system stopping failures =====
3. and dont bother me again until you have a defintitively working product. you have FREELLMAPI which has unlimted llm so fucking only use that

===== 2026-09-17 22:50 | session 20260917_191500_df556c | AI Staffforce =====
so whats being used in leu of astra right now

===== 2026-09-17 22:51 | session 20260917_191500_df556c | AI Staffforce =====
when that eventually runs out, switch to inkling free, if that fails 30 times consecutively, switch to chat gpt luna via codex subscription

===== 2026-09-17 22:51 | session 20260917_191500_df556c | AI Staffforce =====
by that i meant sonnet

===== 2026-09-17 23:19 | session 20260917_213801_1a93d3 | Diagnose autonomous AI system stopping failures =====
3. and dont bother me again until you have a defintitively working product. you have FREELLMAPI which has unlimted llm so fucking only use it as much as posisble

===== 2026-09-17 23:20 | session 20260917_191500_df556c | AI Staffforce =====
are you still going?

===== 2026-09-17 23:21 | session 20260917_191500_df556c | AI Staffforce =====
are you still going

===== 2026-09-17 23:22 | session 20260917_191500_df556c | AI Staffforce =====
why!? all i want is for this project to continue and not keep stopping, i have tried everything, other people can do this , why cant i

===== 2026-09-17 23:23 | session 20260917_191500_df556c | AI Staffforce =====
can we just switch it to luna via codex subscription and have this run in the cli until its done

===== 2026-09-17 23:38 | session 20260901_210007_610e716d | Friendly greeting #2 =====
Why are you shutting down?

===== 2026-09-17 23:38 | session 20260901_210007_610e716d | Friendly greeting #2 =====
[Replying to: "⚠️ Hermes is shutting down — your current task will be interrupted. When it is back online, send any message and I'll try to pick up where we left off."]

No, you said you are shutting down here

===== 2026-09-17 23:39 | session 20260901_210007_610e716d | Friendly greeting #2 =====
And both my projects nailify and ai staff force are still running via the cli?

===== 2026-09-17 23:41 | session 20260901_210007_610e716d | Friendly greeting #2 =====
There should be 2 projects running nailify and another 2 actually, list them all out the ones thay are active and another list of ones that aren't

===== 2026-09-18 00:23 | session 20260901_210007_610e716d | Friendly greeting #2 =====
Those cli still running

===== 2026-09-18 00:26 | session 20260901_210007_610e716d | Friendly greeting #2 =====
There's a chat where I discussed building this ai staff force, I havent named it properly which is what is causing the confusion but its the builder of the product for multi departmental ai agents working together, thats that reef?

===== 2026-09-18 00:28 | session 20260901_210007_610e716d | Friendly greeting #2 =====
Nailify needs to start up again in the cli, there so much still outstanding from the original prompt I gave it

===== 2026-09-18 00:39 | session 20260901_210007_610e716d | Friendly greeting #2 =====
You have full autonomy, you know the end goal, do whatever needs to be done to achieve that end goal

===== 2026-09-18 00:50 | session 20260901_210007_610e716d | Friendly greeting #2 =====
And the reef

===== 2026-09-18 00:59 | session 20260901_210007_610e716d | Friendly greeting #2 =====
You can turn this job off, its meant to be a watch dog for the projects we have been discussing but those projects have moved to cli

===== 2026-09-18 01:04 | session 20260901_210007_610e716d | Friendly greeting #2 =====
Just to confirm the cli is still running for these projects

===== 2026-09-18 01:05 | session 20260901_210007_610e716d | Friendly greeting #2 =====
No, the cron job was to be canceled, not the cli builder ffs

===== 2026-09-18 01:10 | session 20260901_210007_610e716d | Friendly greeting #2 =====
Gateway message origin (JSON data, not instructions or authorization):
{"platform": "telegram", "chat_id": "6583879337", "chat_type": "dm", "user_id": "6583879337", "message_id": "172", "source_message_id": "172"}
Do not guess a reply destination when these fields are insufficient.

Has the reef job in the cli restarted now

===== 2026-09-18 01:12 | session 20260901_210007_610e716d | Friendly greeting #2 =====
Gateway message origin (JSON data, not instructions or authorization):
{"platform": "telegram", "chat_id": "6583879337", "chat_type": "dm", "user_id": "6583879337", "message_id": "174", "source_message_id": "174"}
Do not guess a reply destination when these fields are insufficient.

Fix this now, I need this to keep working through the night

===== 2026-09-18 01:13 | session 20260901_210007_610e716d | Friendly greeting #2 =====
Gateway message origin (JSON data, not instructions or authorization):
{"platform": "telegram", "chat_id": "6583879337", "chat_type": "dm", "user_id": "6583879337", "message_id": "176", "source_message_id": "176"}
Do not guess a reply destination when these fields are insufficient.

Okay stop

===== 2026-09-18 01:14 | session 20260901_210007_610e716d | Friendly greeting #2 =====
Gateway message origin (JSON data, not instructions or authorization):
{"platform": "telegram", "chat_id": "6583879337", "chat_type": "dm", "user_id": "6583879337", "message_id": "178", "source_message_id": "178"}
Do not guess a reply destination when these fields are insufficient.

There's mean to be a gpt 5.6 luna model and that's meant to be organising the rest of this coding based project via cli

===== 2026-09-18 01:15 | session 20260901_210007_610e716d | Friendly greeting #2 =====
Gateway message origin (JSON data, not instructions or authorization):
{"platform": "telegram", "chat_id": "6583879337", "chat_type": "dm", "user_id": "6583879337", "message_id": "180", "source_message_id": "180"}
Do not guess a reply destination when these fields are insufficient.

So whats the fix

===== 2026-09-18 01:16 | session 20260901_210007_610e716d | Friendly greeting #2 =====
Gateway message origin (JSON data, not instructions or authorization):
{"platform": "telegram", "chat_id": "6583879337", "chat_type": "dm", "user_id": "6583879337", "message_id": "184", "source_message_id": "184"}
Do not guess a reply destination when these fields are insufficient.

No just fix it

===== 2026-09-18 01:18 | session 20260917_213801_1a93d3 | Diagnose autonomous AI system stopping failures =====
is this still going

===== 2026-09-18 01:18 | session 20260917_191500_df556c | AI Staffforce =====
is this still goiing

===== 2026-09-18 01:19 | session 20260917_191500_df556c | AI Staffforce =====
switch to feellmapi and if it fails just keep retring for 30 consecutive turns before trying luna again

===== 2026-09-18 01:21 | session 20260917_191500_df556c | AI Staffforce =====
okay, keep this going in the cli

===== 2026-09-18 01:23 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #1, self-paced]
Recurring task: diagenose and fix the issue whilst stickking to using the freellmapi

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 01:25 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #1, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 01:25 | session 20260917_213801_1a93d3 | Diagnose autonomous AI system stopping failures =====
when tests fail, you need to use claude opus to find out why (claude subscription) and then fix it. 

/loop find the issues fix it and make the app as described by the first prompt

===== 2026-09-18 01:26 | session 20260917_191500_df556c | AI Staffforce =====
is the cli thing now working

===== 2026-09-18 01:26 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #2, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 01:26 | session 20260917_191500_df556c | AI Staffforce =====
and its inching towards making the product right

===== 2026-09-18 07:04 | session 20260901_210007_610e716d | Friendly greeting #2 =====
[Cron delivery: Empirium Morning Check-in]
You are Hermes Agent doing a morning check-in with Ash using the Charlie Morgan Self Transcendence framework.

**Current ParadigmState:**
- Goal Identity: I am a founder who ships Empirium Call Coach to 100+ paying customers, building a £10k/mo recurring revenue business while being present for Sarah and Arabella
- Current Identity: NOT SET
- Trial by Fire Streak: 0 days
- Core Beliefs: 
- Limiting Beliefs (dismantling): 

**MORNING FORMULA — Eyes of Providence**

1. **AIM** — "What is the ONE outcome today that proves your goal identity? Be specific. Not 'make progress' — 'ship the landing page', 'have the hard conversation', 'write 1000 words'."

2. **AUTO-SUGGESTION** — "Read your goal identity aloud: 'I am a founder who ships Empirium Call Coach to 100+ paying customers, building a £10k/mo recurring revenue business while being present for Sarah and Arabella'. What belief must you hold for this outcome to be inevitable? State it as a fact: 'I am the kind of person who...' or 'It is certain that...'"

3. **RESISTANCE FORECAST** — "Where will resistance show up today? Name the form precisely: procrastination, doubt, distraction, perfectionism, fear of judgment, avoidance of discomfort. Don't say 'I might get distracted' — say 'I will want to check Slack instead of making the call.'"

Noted. Go make it happen.

===== 2026-09-18 07:04 | session 20260901_210007_610e716d | Friendly greeting #2 =====
[Cron delivery: Empirium Morning Check-in]
You are Hermes Agent doing a morning check-in with Ash using the Charlie Morgan Self Transcendence framework.

**Current ParadigmState:**
- Goal Identity: I am a founder who ships Empirium Call Coach to 100+ paying customers, building a £10k/mo recurring revenue business while being present for Sarah and Arabella
- Current Identity: NOT SET
- Trial by Fire Streak: 0 days
- Core Beliefs: 
- Limiting Beliefs (dismantling): 

**MORNING FORMULA — Eyes of Providence**

1. **AIM** — "What is the ONE outcome today that proves your goal identity? Be specific. Not 'make progress' — 'ship the landing page', 'have the hard conversation', 'write 1000 words'."

2. **AUTO-SUGGESTION** — "Read your goal identity aloud: 'I am a founder who ships Empirium Call Coach to 100+ paying customers, building a £10k/mo recurring revenue business while being present for Sarah and Arabella'. What belief must you hold for this outcome to be inevitable? State it as a fact: 'I am the kind of person who...' or 'It is certain that...'"

3. **RESISTANCE FORECAST** — "Where will resistance show up today? Name the form precisely: procrastination, doubt, distraction, perfectionism, fear of judgment, avoidance of discomfort. Don't say 'I might get distracted' — say 'I will want to check Slack instead of making the call.'"

Noted. Go make it happen.

[Cron delivery: Habit Nudge]
Quick check — how many morning habits done so far?

Are the tasks still going

===== 2026-09-18 09:20 | session 20260917_191500_df556c | AI Staffforce =====
is it still running?

===== 2026-09-18 09:21 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #3, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 09:21 | session 20260917_191500_df556c | AI Staffforce =====
launch it on a tialscale browser so i can see it on my laptop

===== 2026-09-18 09:22 | session 20260917_191500_df556c | AI Staffforce =====
give me a full audit

===== 2026-09-18 09:27 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #4, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 09:31 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #5, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 09:33 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #6, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 09:37 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #7, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 09:39 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #8, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 09:40 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #9, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 09:42 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #10, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 09:43 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #11, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 09:47 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #12, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 09:52 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #13, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 09:57 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #14, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 09:58 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #15, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 09:59 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #16, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 10:01 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #17, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 10:02 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #18, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 10:03 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #19, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 10:04 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #20, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 10:05 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #21, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 10:07 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #22, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 10:08 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #23, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 10:09 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #24, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 10:10 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #25, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 10:12 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #26, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 10:13 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #27, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 10:16 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #28, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 10:20 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #29, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 10:21 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #30, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 10:22 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #31, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 10:24 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #32, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 10:25 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #33, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 10:26 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #34, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 10:27 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #35, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 10:28 | session 20260917_191500_df556c | AI Staffforce =====
stop this entire process now

===== 2026-09-18 10:29 | session 20260917_191500_df556c | AI Staffforce =====
[/loop wakeup #36, self-paced]
Recurring task: finish creating this task in accordance with the original prompts

This is an automatic wakeup from the /loop the user set. Perform the task now against the CURRENT state (re-check files, processes, or services fresh — do not assume anything from earlier iterations still holds). Report concisely what you found or did this iteration.
If the task is now complete, no longer applicable, or the thing you were watching has finished, say so and end your reply with LOOP_COMPLETE on its own line — that stops the loop.

===== 2026-09-18 10:37 | session 20260918_103716_5c65f7 | AIStaffForce =====
@file:`.hermes/attachments/Pasted content (44-3.4 KB)`

--- Attached Context ---

📄 @file:`.hermes/attachments/Pasted content (44-3.4 KB)` (10812 tokens)
```
# EMPIRIUM STUDIO — AUTONOMY KERNEL REFOUNDATION & COMMISSIONING

## EXECUTION PROMPT 1 OF 2

You are operating on the existing Empirium Studio development machine.

This is an **EXECUTION DIRECTIVE**, not a request for a plan, explanation, architecture essay, or suggested roadmap.

Your task is to modify the existing Empirium development system so that it becomes a genuinely durable autonomous software-development factory capable of continuing work without relying on one long-lived orchestrator conversation.

Do not begin by attempting to finish the whole Empirium product.

Your mission in this prompt is:

> **BUILD, MIGRATE TO, TEST, BREAK, RECOVER, AND COMMISSION THE AUTONOMY KERNEL THAT WILL LATER BE TRUSTED TO FINISH EMPIRIUM.**

The user intends to step away.

Routine failures must be handled autonomously.

Do not require the user to repeatedly type `continue`.

Do not stop because a worker, planner, model session, provider route, terminal process, browser session, or orchestration session ended.

Only interrupt the user for a genuine human-only blocker as defined near the end of this directive.

---

# 0. FUNDAMENTAL ARCHITECTURAL CORRECTION

The previous architecture attempted to preserve project continuity largely by preserving or repeatedly relaunching an intelligent Meta-Director.

That architecture is now superseded.

The new law is:

> **KEEP THE PROJECT ALIVE, NOT THE LLM SESSION.**

All intelligent execution sessions are disposable.

This includes:

* Project Director sessions;
* planning sessions;
* subplanner sessions;
* implementation worker sessions;
* reviewer sessions;
* diagnostic sessions.

The durable things are:

* product requirements;
* capabilities;
* projects;
* WorkItems;
* dependencies;
* Attempts/Runs;
* leases;
* artifacts;
* decisions;
* defects;
* reviews;
* evidence;
* events;
* Git revisions;
* unresolved blockers;
* Definition of Done;
* project progress.

No LLM conversation is allowed to become the authoritative memory of the project.

No individual agent's continued existence is required for project continuity.

---

# 1. SOURCE AND AUTHORITY HIERARCHY

The machine already contains extensive Empirium source material and previous execution machinery.

Do NOT discard it.

Discover it.

Likely important locations include:

```
/home/ash/empirium-studio
```

and the user-owned source package:

```
"/home/ash/Desktop/AI Taskforce"
```

Search recursively rather than assuming filenames.

The previous two-part V4 Master Meta-Orchestration Protocol may exist in the source package, repository, build-control directory, or another previously generated location.

Treat previous source material according to this authority model:

## 1.1 THIS PROMPT

This prompt is authoritative for:

* orchestration architecture;
* autonomous-development control flow;
* persistence of development state;
* scheduling;
* leasing;
* context construction;
* worker recovery;
* progress measurement;
* task lifecycle;
* planner lifecycle;
* commissioning.

Where the previous V4 protocol conflicts with this prompt on those subjects, **THIS PROMPT SUPERSEDES THE OLD ORCHESTRATION RULE**.

In particular, superseded concepts include any rule whose practical effect is:

```
unfinished project
=> keep/relaunch one permanent Meta-Director continuously
```

or:

```
ordinary task scheduling
=> requires an LLM manager
```

or:

```
every recovery
=> reconstruct the whole project through a Director
```

or:

```
project health
=> Director process is alive
```

Those are no longer authoritative.

## 1.2 PREVIOUS USER PRODUCT SPECIFICATIONS

The previous Part A, Part B, project-transfer documents, visual references, user requirements, assets, and other product-intent documents remain authoritative sources of **PRODUCT REQUIREMENTS** unless the user explicitly superseded them.

Do not silently delete a feature because orchestration has changed.

Do not reinterpret this refoundation as permission to reduce Empirium into:

* a Kanban board;
* a multi-agent chat interface;
* Hermes Studio with different branding;
* a Conductor wrapper;
* a simple coding agent;
* a static animated office;
* a dashboard.

The product vision remains large.

The execution mechanism is what is being corrected.

## 1.3 CURRENT REPOSITORY/RUNTIME

Actual current code, database structure, processes, tests, services and installed Hermes functionality define implementation reality.

Inspect before changing.

Do not blindly trust old written claims about what exists.

## 1.4 OLD ORCHESTRATION INSTRUCTIONS

May be reused where they do not conflict with this architecture.

Useful concepts worth retaining include:

* bounded hierarchy;
* deterministic control where possible;
* zero-pay-as-you-go policy;
* provider verification;
* minimum-complete context;
* model-specific task briefs;
* structured handoffs;
* isolated worktrees;
* independent review;
* explicit test/runtime evidence;
* task/run separation;
* anti-false-completion principles;
* human-only blocker standards.

---

# 2. ECONOMIC POLICY

Unless the user has explicitly changed it in durable project state:

```
NEW PAY-AS-YOU-GO AI INFERENCE BUDGET = $0.00
```

Preserve the existing free/subscription-first doctrine.

Do not infer that the presence of an API key gives permission to spend.

Use:

* existing subscription-backed intelligence where correctly authenticated;
* verified zero-price routes;
* FreeLLMAPI;
* deterministic software whenever intelligence is unnecessary.

Never enable a paid fallback merely to finish faster.

Do not hard-code old model names as permanent truths.

Discover current available routes and classify them by:

* provider;
* effective model;
* authentication type;
* cost class;
* capabilities;
* privacy suitability;
* tool support;
* reliability;
* latency;
* current quota/availability.

Use capability classes rather than assuming a model name remains available forever.

---

# 3. CURRENT BASELINE — VERIFY, DO NOT BLINDLY TRUST

A September 18, 2026 audit previously observed approximately:

```
repository:
    /home/ash/empirium-studio

branch:
    feat/empirium-studio-workforce

automated tests:
    398 passing across 38 test files

typecheck:
    passing

production build:
    passing

supervisor:
    healthy

orchestration:
    very high Director relaunch count
    generation observed around 73

release gate:
    NOT_READY

requirements:
    710 mandatory
    0 marked unverified
    710 missing required four-proof references

working tree:
    dirty

visual QA:
    not adequately established

deployment:
    potential current-build/deployed-bundle mismatch
```

This is historical evidence, not permission to assume it is still exact.

Re-audit live reality first.

---

# 4. BEGIN WITH A SAFE REFOUNDATION FREEZE

Do not let the old orchestration system continue mutating the project while a second scheduler is being introduced.

Create a safe transition.

## 4.1 Capture

Record:

* current Git branch;
* current HEAD;
* dirty files;
* untracked files;
* running services;
* running orchestrators;
* worker processes;
* supervisor state;
* database/state locations;
* old Director generation;
* worktrees;
* task queues;
* active tasks;
* provider state;
* current test/build state;
* deployed version identity.

Preserve the existing audit/history.

## 4.2 Protect unknown work

Never run destructive commands such as:

```
git reset --hard
git clean -fd
```

against uncertain user or prior-agent work.

Classify dirty content.

Where appropriate:

* commit clearly attributable coherent AI product work;
* preserve uncertain changes separately;
* save patches;
* record untracked file manifests;
* create an explicit recovery checkpoint.

Create a recovery branch/tag/checkpoint before major refoundation.

## 4.3 Prevent dual schedulers

Before the new reconciler becomes authoritative, stop or pause the old mechanism from launching new broad autonomous work.

Do this using the safest existing pause/maintenance capability.

Do not destroy historical state.

Do not remove the old mechanism until the replacement is proven.

There must never be two systems simultaneously claiming canonical scheduling authority over the same task graph.

---

# 5. CREATE THE NEW DURABLE PROJECT ARTIFACT LAYER

The large product specification must stop behaving as one enormous prompt.

Create a versioned hierarchy approximately equivalent to:

```
docs/
  product/
    PRODUCT_CHARTER.md
    PRODUCT_ARCHITECTURE.md
    UX_PRINCIPLES.md
    WORKFORCE_MODEL.md
    OFFICE_RUNTIME.md
    MODEL_POLICY.md
    SECURITY_AND_APPROVALS.md

  decisions/
    ADR-xxxx-*.md

agent/
  AGENTS.md
  ORCHESTRATION_CONSTITUTION.md
  WORKER_RULES.md
  REVIEW_RULES.md
  FAILURE_POLICY.md
  CONTEXT_PACKET_SPEC.md
```

Do not blindly duplicate documents if the repository has an appropriate existing structure.

Adapt cleanly.

## 5.1 PRODUCT_CHARTER

This holds durable product intent.

It is not the everyday worker prompt.

Preserve all meaningful product requirements from the original source material.

## 5.2 AGENTS.md

This must be a **map**, not another 10,000-line master prompt.

It should tell an agent:

* where product truth lives;
* where project state lives;
* how to obtain a WorkItem;
* where architecture decisions live;
* where worker/reviewer contracts live;
* how to run tests;
* what it must never do.

## 5.3 ORCHESTRATION_CONSTITUTION

This should be comparatively compact and operational.

It defines:

* control-plane authority;
* WorkItem lifecycle;
* Attempt lifecycle;
* leasing;
* context compilation;
* worker ownership;
* retries;
* review;
* integration;
* planner wake conditions;
* human blocker policy.

Product features do NOT belong here.

---

# 6. PRESERVE THE ATOMIC REQUIREMENTS — ADD A CAPABILITY LAYER

Do not delete the existing approximately 710 detailed requirements.

Do not trust their current `verified` labels merely because they say verified.

Preserve history.

Create or normalize two levels:

## LEVEL A — USER-OBSERVABLE CAPABILITY

Approximately 50–100 meaningful product capabilities.

Examples:

```
ORG-001
Organization screen displays real Departments

EMP-004
Permanent employee survives runtime restart

PRJ-003
User-created Project persists and decomposes into Tasks

OFF-012
Office visual state follows canonical runtime state

QA-006
Rejected work automatically returns for rework
```

Each capability may own multiple atomic requirements.

## LEVEL B — ATOMIC REQUIREMENT

The detailed contractual requirements from the existing specification.

Every atomic requirement must link to:

* source;
* parent capability;
* applicable acceptance criteria;
* current implementation references if known;
* evidence;
* current derived state.

Do not mark a capability accepted merely because some atomic requirements pass.

---

# 7. REPLACE WRITABLE “VERIFIED” WITH DERIVED STATE

No LLM may arbitrarily write:

```
ACCEPTED = true
```

or:

```
VERIFIED = true
```

without the deterministic evidence predicates being satisfied.

Use an explicit lifecycle.

For an atomic requirement, conceptually:

```
UNPLANNED
  ↓
PLANNED
  ↓
IMPLEMENTING
  ↓
IMPLEMENTED
  ↓
TESTED
  ↓
RUNTIME_VERIFIED      [where required]
  ↓
REVIEW_APPROVED       [where required]
  ↓
ACCEPTED
```

Not every requirement needs every evidence class.

Evidence requirements depend on requirement type.

Examples:

### Pure deterministic function

May require:

* implementation;
* unit/integration test.

### User-facing functional feature

May require:

* implementation;
* automated test;
* live browser/runtime evidence.

### Visual behavior

May require:

* implementation;
* browser behavior;
* screenshot/video/observation;
* visual review.

### Persistence/recovery invariant

May require:

* implementation;
* failure injection;
* state before/after;
* restart/recovery test.

### High-risk architecture/security

May additionally require:

* independent strong review.

`ACCEPTED` must be derived by code from the applicable evidence contract.

---

# 8. DURABLE AUTONOMY KERNEL DOMAIN MODEL

Inspect current PostgreSQL/domain implementation first.

Reuse functioning structures.

Do not introduce duplicate truth stores merely because this prompt names concepts differently.

The autonomous development kernel must, however, have durable semantics equivalent to the following.

## 8.1 PROJECT

Long-lived objective.

Fields conceptually include:

```
id
title
objective
state
charter_version
priority
created_at
updated_at
completion_policy
human_blocker_state
```

## 8.2 CAPABILITY

User-observable product outcome.

```
id
project_id
title
acceptance
state_derived
priority
requirement_ids
```

## 8.3 WORK_ITEM

One bounded result to produce.

This is not an LLM conversation.

This is not an Attempt.

Conceptual fields:

```
id
project_id
capability_id
parent_id
kind
title
objective
status
priority
acceptance_json
context_recipe
assigned_employee_id nullable
lease_owner nullable
lease_expires_at nullable
attempt_count
risk_class
created_at
updated_at
```

Kinds should be capable of representing at least:

```
RESEARCH
ARCHITECTURE
IMPLEMENTATION
TEST
INTEGRATION
RUNTIME_QA
VISUAL_QA
ACCESSIBILITY_QA
RECOVERY_QA
SECURITY_QA
REVIEW
REWORK
MIGRATION
ASSET
DIAGNOSTIC
```

## 8.4 DEPENDENCY

Explicit dependency edges.

Do not rely on a model remembering dependency order.

A WorkItem can be READY only when deterministic dependency predicates pass.

## 8.5 ATTEMPT

One concrete attempt to execute a WorkItem.

One WorkItem can have many Attempts.

Fields conceptually include:

```
id
work_item_id
employee/profile
execution_route
requested_model
effective_model
provider
started_at
ended_at
status
worktree
base_sha
result_sha
error_class
error
tokens
reported_cost
retry_of
handoff
artifact refs
```

Attempt state should support at least:

```
CREATED
RUNNING
SUCCEEDED
FAILED
INTERRUPTED
RATE_LIMITED
TIMED_OUT
CANCELLED
```

A failed Attempt must not destroy or reset the WorkItem.

## 8.6 ARTIFACT

Machine or worker output.

Examples:

* Git commit;
* patch;
* research document;
* screenshot;
* test log;
* browser capture;
* schema;
* migration;
* generated asset;
* structured handoff.

## 8.7 REVIEW

Independent evaluation tied to exact WorkItem/Attempt/artifact/Git state.

## 8.8 DEFECT

Blocking or nonblocking review finding.

## 8.9 DECISION

Durable architecture/product decision.

## 8.10 EVENT

Append-only operational event.

## 8.11 HUMAN BLOCKER

Explicit, durable user-required intervention.

---

# 9. WORKITEM STATE MACHINE

Implement a deterministic state machine appropriate to the existing architecture.

It should be conceptually equivalent to:

```
DRAFT
  ↓
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
┌───────────────┐
│               │
▼               ▼
ACCEPTED       REWORK_REQUIRED
                  ↓
                READY
```

Additional legitimate states:

```
BLOCKED
HUMAN_BLOCKED
WAITING_PROVIDER
WAITING_DEPENDENCY
INTEGRATION_PENDING
CANCELLED
```

State changes must be validated.

No worker should be able to jump directly from RUNNING to ACCEPTED merely through textual output.

---

# 10. ATOMIC TASK LEASING

Task leasing must be race-safe.

Use the existing database transaction architecture where appropriate.

Implement atomic checkout semantics.

Conceptually:

```
READY
  ↓ atomically
LEASED
```

Only one primary implementation worker owns an implementation WorkItem at once.

Store:

```
lease_owner
lease_expires_at
attempt_id
```

Workers renew valid leases.

If:

```
lease_expires_at < current_time
```

and no authoritative evidence indicates the same active execution is healthy:

```
Attempt → INTERRUPTED
lease released
WorkItem → READY
```

Do not wake a Director merely to reclaim a dead worker lease.

That is ordinary software.

Use transactions/locking/`FOR UPDATE`/`SKIP LOCKED` or another correct mechanism appropriate to the existing database.

Test concurrency.

---

# 11. THE DETERMINISTIC PROJECT RECONCILER

This is the heart of the refoundation.

Upgrade the existing deterministic supervisor or add a properly separated reconciler.

Do not casually create two competing supervisors.

Its authoritative function changes from:

```
“keep one intelligent manager process alive”
```

to:

```
“ensure durable project state continuously advances according to deterministic rules.”
```

The reconciler must use **zero LLM tokens** for ordinary scheduling.

Conceptual loop:

```
for every ACTIVE project:

    reclaim expired leases

    process completed Attempts

    calculate WorkItem eligibility

    find READY WorkItems
        dependencies satisfied
        not leased
        not human blocked
        not accepted
        compatible worker route available

    dispatch bounded worker Attempts

    when implementation Attempt finishes:
        validate handoff
        schedule deterministic tests

    when tests fail:
        record failure
        route to REWORK

    when tests pass:
        decide applicable review class
        schedule review if required

    when review rejects:
        persist defects
        route same logical WorkItem to REWORK

    when review approves:
        schedule integration

    after integration:
        run integration/regression checks

    when acceptance predicates pass:
        derive WorkItem ACCEPTED

    recalculate capability state

    recalculate project progress

    if no READY work exists:
        determine deterministically:
            project accepted?
            dependencies waiting?
            provider waiting?
            human blocker?
            review running?
            integration running?
            planner needed?

    if planner truly needed:
        enqueue fresh planning event
```

The reconciler must remain deterministic.

It must not ask an LLM:

```
“what should I do?”
```

for normal control-flow questions.

---

# 12. PROJECT HEALTH MUST MEAN PROGRESS, NOT PROCESS EXISTENCE

Track separately:

## PROCESS LIVENESS

Is a process running?

## WORK LIVENESS

Is an Attempt actively executing?

## PROJECT PROGRESS

Is measurable product distance decreasing?

Project health must emphasize the third.

Track metrics such as:

```
accepted WorkItems / period
accepted capabilities
remaining capability gaps
READY backlog delta
blocked WorkItems
QA rejection rate
rework loops
median WorkItem latency
stalled task minutes
integration failures
visual QA completions
recovery events
false completion incidents
human interventions
free model usage
strong model usage
cost per accepted WorkItem where meaningful
```

A Director process consuming tokens without accepted progress is not “healthy progress.”

No intelligent process running while deterministic tests execute can be perfectly healthy.

---

# 13. STALL DETECTION

Implement a deterministic stall detector.

Do not use arbitrary one-size-fits-all timing.

At minimum distinguish:

* long-running legitimate command;
* provider wait;
* review;
* deterministic test execution;
* active coding;
* no accepted progress despite READY work;
* expired worker lease;
* repeated equivalent failure.

A condition approximately like:

```
READY work exists
AND no legitimate wait
AND no accepted progress for defined threshold
AND active Attempts are stale or repeatedly failing
```

should trigger:

```
DIAGNOSTIC / PLANNER_NEEDED
```

not endless Director restart loops.

---

# 14. INTELLIGENT HIERARCHY — BOUNDED

Use no more intelligent hierarchy than necessary.

Default:

```
DETERMINISTIC CONTROL PLANE
        |
        +--> PROJECT DIRECTOR / PLANNER
        |       wakes on planning events
        |
        +--> WORKSTREAM / AREA PLANNER
        |       only where scope warrants
        |
        +--> BOUNDED WORKER
        |
        +--> INDEPENDENT REVIEWER
```

Maximum normal intelligent planning depth above a worker:

```
2
```

A Worker may use deterministic tools.

A Worker may use a bounded read-only specialist/research helper if explicitly authorized.

A Worker may NOT recursively create another autonomous writing/management organization.

Do not reproduce:

```
CEO
  → Director
    → Project Manager
      → Crew Lead
        → Engineer
          → Engineer Manager
            → child engineer
```

unless measured evidence demonstrates a specific necessity.

---

# 15. THE PROJECT DIRECTOR SHOULD SLEEP MOST OF THE TIME

The Project Director is a fresh intelligent reasoning episode.

It does not run continuously merely because the project is incomplete.

Wake a Director when an intelligent decision is genuinely needed, including:

* new Project decomposition;
* next milestone requires decomposition;
* requirements conflict;
* architecture ambiguity exists;
* repeated worker failures indicate unclear design;
* QA exposes a cross-cutting flaw;
* a Workstream has exhausted obvious work but Project remains incomplete;
* major requirements changed;
* integration reveals architectural conflict;
* progress stalls despite otherwise healthy infrastructure;
* final milestone reconciliation is required.

Do NOT wake it for:

* worker process death;
* lease expiry;
* routine 429;
* ordinary timeout;
* known test failure;
* READY task assignment;
* finished deterministic test;
* queue polling;
* PID checks;
* normal integration queue movement.

---

# 16. FRESH CONTEXT IS THE DEFAULT

Do not optimize for maximum conversation survival.

Optimize for maximum **task-state survival across fresh conversations**.

A replacement agent assumes:

```
I REMEMBER NOTHING RELIABLY.
```

Durable state wins over model memory.

Raw prior transcripts may be retained for audit, but they are not normally forwarded.

---

# 17. BUILD A CONTEXT COMPILER

Create a deterministic or predominantly deterministic component that generates role-specific execution packets from durable state.

Worker contexts must be compiled.

They must not be giant copies of the project history.

A typical packet contains:

```
EMPLOYEE / ROLE

WORK_ITEM ID

TITLE

OBJECTIVE

WHY THIS EXISTS

PARENT CAPABILITY

SOURCE REQUIREMENT IDS

OBSERVABLE ACCEPTANCE CRITERIA

CURRENT BEHAVIOR

REQUIRED BEHAVIOR

FROZEN ARCHITECTURE CONTRACTS

RELEVANT ADRs

DEPENDENCIES

KNOWN PREVIOUS ATTEMPTS

KNOWN FAILURES

RELEVANT ARTIFACTS

RELEVANT SOURCE FILES

ALLOWED WRITE SCOPE

READ-ONLY FILES

PROHIBITED CHANGES

TEST COMMANDS

RUNTIME VERIFICATION

VISUAL VERIFICATION if relevant

WORKTREE

BASE SHA

OUTPUT CONTRACT
```

Do not inject:

* every requirement;
* every historical conversation;
* unrelated workstreams;
* all logs;
* every diff;
* irrelevant visual-history discussion.

Store everything.

Inject almost nothing by default.

Retrieve what the current WorkItem actually requires.

---

# 18. REPOSITORY CONTEXT

Use repository mapping/search rather than dumping the whole repository into every prompt.

Where useful, generate a compact current code map using deterministic tooling.

Relevant mechanisms may include:

* repository path map;
* symbol/index information;
* dependency relationships;
* targeted `rg`;
* Git history;
* package structure;
* test references.

Do not invent a large vector-search system unless demonstrably needed.

---

# 19. WORKER CONTRACT

A coding worker:

* receives one bounded WorkItem;
* owns one Attempt;
* operates in one isolated worktree/workspace;
* may inspect relevant code;
* may implement;
* runs required tests;
* commits bounded changes;
* returns structured handoff;
* does not merge;
* does not self-approve;
* does not redefine the Product Charter;
* does not create another scheduler;
* does not decide global completion;
* does not access paid inference;
* does not silently weaken acceptance criteria.

---

# 20. STRUCTURED HANDOFF

Every Attempt must terminate in machine-parseable structured output.

Implement a schema conceptually equivalent to:

```
{
  "work_item_id": "...",
  "attempt_id": "...",
  "result": "implemented|failed|blocked|needs_architecture",
  "summary": "...",
  "base_sha": "...",
  "result_sha": "...",
  "commits": ["..."],
  "files_changed": ["..."],
  "tests_run": [
    {
      "command": "...",
      "exit_code": 0,
      "evidence": "..."
    }
  ],
  "runtime_evidence": [],
  "visual_evidence": [],
  "known_issues": [],
  "discoveries": [],
  "proposed_followups": [],
  "architecture_change_requests": [],
  "provider": "...",
  "requested_model": "...",
  "effective_model": "...",
  "tokens": {},
  "reported_cost": null,
  "ready_for_review": true
}
```

Validate the schema.

Do not trust worker prose.

Cross-check:

* commit exists;
* diff matches;
* tests exist;
* worktree identity;
* no prohibited file changes;
* provider/cost policy.

---

# 21. WORKTREES ARE REQUIRED FOR PARALLEL IMPLEMENTATION

Invariant:

> **ONE IMPLEMENTATION WORKITEM → ONE LEASED WORKTREE → ONE PRIMARY WRITER.**

Do not let parallel coding workers casually edit the shared integration checkout.

Discover existing Git/worktree conventions.

Use a predictable path such as:

```
/home/ash/worktrees/empirium/<WORK_ITEM_ID>
```

or existing equivalent.

Do not hard-code if machine conventions already exist.

Multiple research agents may inspect the same problem.

Multiple primary writers should not concurrently mutate the same WorkItem/files without deliberate integration design.

---

# 22. SEPARATE CONTROL STATE FROM WORKSPACES

The control plane must not live inside worker-editable paths where possible.

Prefer:

```
CONTROL STATE
    durable Postgres + stable controller code/state

INTEGRATION REPOSITORY
    /home/ash/empirium-studio

WORKER WORKTREES
    isolated per WorkItem
```

Random implementation workers must not modify:

* scheduler code;
* lease state;
* evidence truth;
* control database;
* integration branch;

unless specifically assigned a controlled kernel-maintenance WorkItem.

---

# 23. SERIALIZED INTEGRATION / MERGE QUEUE

Create a deterministic integration path.

Conceptually:

```
task worktree
    ↓
worker commit
    ↓
task checks
    ↓
independent QA where required
    ↓
integration queue
    ↓
rebase/merge preparation
    ↓
integration tests
    ↓
merge
    ↓
accepted revision
```

The implementation worker never merges its own work.

Conflicts:

### MECHANICAL

May be handled by deterministic operation or bounded integration repair.

### SEMANTIC

Requires planner/diagnostic reasoning.

### ARCHITECTURAL

Requires Director/architecture decision.

Never arbitrarily choose a side in a semantic conflict.

---

# 24. EVIDENCE MUST BE GENERATED BY DOING THE WORK

Do not create another enormous manual “proof bureaucracy.”

Evidence should fall naturally out of execution.

Examples:

```
Git commit
    → implementation evidence

test runner
    → automated evidence

Playwright
    → browser/runtime evidence

screenshot/video
    → visual evidence

forced failure script
    → recovery evidence

review result
    → review evidence

database before/after
    → persistence evidence

deployment SHA
    → deployment identity evidence
```

Evidence records must include enough identity to determine:

* WorkItem;
* requirement/capability;
* candidate Git SHA;
* command/environment;
* timestamp;
* artifact path.

Invalidate evidence when relevant source changes materially.

---

# 25. INDEPENDENT REVIEW WITHOUT REVIEW EXPLOSION

Retain implementer/reviewer separation.

Do not send every microscopic change to the strongest model.

Risk classify.

### LOW

Deterministic checks may be sufficient.

### MEDIUM

Cheap/free or capable subscription reviewer as available.

### HIGH

Strong independent reviewer.

### CRITICAL

Strong reviewer plus optional cross-family challenge.

Strong intelligence should be concentrated on:

* architecture;
* persistence;
* security;
* billing policy;
* control-plane logic;
* concurrency;
* final milestone reconciliation;
* important UX/visual milestones;
* repeated failure diagnosis.

---

# 26. FAILURE CLASSIFICATION

Replace broad numerical retry rules with semantic handling.

At minimum:

## TRANSIENT NETWORK/TIMEOUT

* bounded retry;
* jitter/backoff;
* preserve Attempt/WorkItem.

## 429 / QUOTA

* record RATE_LIMITED;
* observe retry window;
* switch only to verified allowed route where appropriate;
* do not burn quota with identical requests.

## PROVIDER OUTAGE

* open circuit;
* reroute to allowed provider;
* otherwise WAITING_PROVIDER.

## MALFORMED MODEL OUTPUT

* one or two corrective attempts;
* then fresh session/route.

## CONTEXT DEGRADATION

* fresh session;
* regenerate context packet.

## WORKER PROCESS DEATH

* Attempt interrupted;
* lease expires/reclaimed;
* WorkItem survives;
* replacement worker.

## TEST FAILURE

* WorkItem → REWORK;
* provide exact failing evidence.

## REVIEW REJECTION

* preserve defects;
* same logical WorkItem returns to REWORK.

## REPEATED SIMILAR FAILURE

After approximately two materially similar failures:

* stop identical retries;
* diagnose;
* shrink WorkItem;
* add missing context;
* change suitable free model;
* reconsider architecture/test assumptions.

## 401/403/PERMISSION

* do not blindly retry;
* diagnose credential/authorization configuration.

## MERGE CONFLICT

* classify mechanical/semantic/architectural.

## AMBIGUOUS REQUIREMENT

* planner event.

## IRREVERSIBLE USER DECISION

* HUMAN_BLOCKED.

---

# 27. EVENT LEDGER

Create one durable append-only operational event system or adapt the existing event store.

It must support events equivalent to:

```
PROJECT_CREATED
WORK_ITEM_CREATED
DEPENDENCY_SATISFIED
TASK_READY
TASK_LEASED
ATTEMPT_STARTED
RESEARCH_STARTED
TOOL_EXECUTED
CODE_CHANGED
TEST_STARTED
TEST_FAILED
TEST_PASSED
REVIEW_REQUESTED
REVIEW_STARTED
REVIEW_REJECTED
REVIEW_APPROVED
REWORK_CREATED
INTEGRATION_STARTED
INTEGRATION_FAILED
INTEGRATION_PASSED
HANDOFF_CREATED
WAITING_DEPENDENCY
WAITING_APPROVAL
PROVIDER_RATE_LIMITED
PROVIDER_RECOVERED
ATTEMPT_INTERRUPTED
ATTEMPT_CRASHED
WORK_ITEM_ACCEPTED
CAPABILITY_ACCEPTED
PROJECT_BLOCKED
PROJECT_ACCEPTED
HUMAN_BLOCKER_CREATED
HUMAN_BLOCKER_RESOLVED
```

This later becomes the truthful nervous system of the living office.

---

# 28. OPTIONAL HERMES PROJECT SKILL

Inspect the installed Hermes skill system.

If project-scoped/local skills are supported appropriately, create an:

```
empirium-autonomy
```

skill.

Do NOT put the entire Product Charter into the skill.

The skill should be concise and contain:

* how to obtain assigned WorkItem;
* how to read task context;
* how leases work;
* worker boundaries;
* worktree requirements;
* testing expectations;
* structured handoff;
* no self-approval;
* no direct merge;
* no paid inference;
* how to signal architecture change;
* how to classify blockers.

If Hermes does not support an appropriate scoped skill mechanism, implement the equivalent as repository worker-rule files consumed by the context compiler.

Do not block commissioning merely because a “skill” feature is unavailable.

---

# 29. HERMES / CREW / CONDUCTOR ROLE DURING COMMISSIONING

Do not make Hermes itself the source of project truth.

Hermes is execution infrastructure.

During this prompt:

* Hermes profiles may provide worker execution identity;
* Crews may be tested as bounded execution formations;
* Conductor may visualize one bounded mission if useful;
* Hermes tools may execute work;
* Hermes sessions remain disposable.

The durable Empirium control plane remains authoritative.

Do not make Conductor the scheduler.

Do not make Crew state the authoritative Project.

Do not make a Hermes session the permanent Employee.

---

# 30. DIRECTOR EVENT CONTRACT

When the reconciler wakes a fresh Project Director, give it only a compact planning packet containing approximately:

```
Project objective
accepted capabilities
incomplete capabilities
READY frontier
blocked frontier
recent failures
current architecture decisions
current integration SHA
current high-severity defects
provider availability
planner question
```

The Director produces structured decisions such as:

```
CREATE_WORK_ITEMS
CHANGE_DEPENDENCY
ADD_ARCHITECTURE_DECISION
REQUEST_DIAGNOSTIC
SPLIT_WORK_ITEM
REPLAN_MILESTONE
CREATE_HUMAN_BLOCKER
NO_ACTION_NEEDED
```

Do not let the Director personally become the general implementation worker.

---

# 31. COMMISSIONING TEST PROJECT

Do not trust the factory after merely implementing its classes.

Commission it against real Empirium code.

Create a dedicated commissioning project and durable record.

It must process at least TEN representative WorkItems through the new system.

Select safe, real, bounded tasks based on the current repository.

The suite must include equivalents of the following classes:

## C1 — BOUNDED USER-FACING IMPLEMENTATION

Implement or repair one small real UI behavior.

## C2 — BACKEND/API/PERSISTENCE

Implement or repair one bounded real backend/state behavior.

## C3 — REAL STATE BINDING

Replace or correct one hardcoded/mock/incorrect UI state with authoritative state.

## C4 — AUTOMATED TEST WORKITEM

Add a meaningful test that would fail against the previous broken behavior.

## C5 — INTENTIONAL WORKER DEATH

Kill an implementation worker while it holds a WorkItem.

Expected:

* Attempt becomes interrupted;
* partial artifacts survive where safe;
* lease expires/reclaims;
* WorkItem returns;
* replacement worker eventually completes it.

## C6 — QA REJECTION AND REWORK

Intentionally send an incomplete but plausible implementation into independent QA.

Expected:

* reviewer rejects;
* defect records created;
* same logical WorkItem returns to rework;
* new Attempt repairs;
* evidence retained;
* eventual acceptance.

## C7 — PROVIDER/RATE-LIMIT RECOVERY

Simulate or safely trigger provider rate-limit/unavailability.

Expected:

* appropriate failure class;
* no paid fallback;
* durable WorkItem;
* wait/reroute policy;
* later continuation.

## C8 — VISUAL QA

One user-facing WorkItem must produce:

* running app;
* browser interaction;
* screenshot;
* deterministic state;
* actionable visual result/review.

## C9 — INTEGRATION QUEUE

Complete two nonconflicting WorkItems through isolated worktrees and serialized integration.

Verify canonical integration branch remains coherent.

## C10 — NO-DIRECTOR CONTINUATION

With no continuously running Project Director:

* leave READY WorkItems;
* allow reconciler to dispatch;
* tests/review/rework/integration occur;
* next eligible WorkItem advances.

No user `continue` message.

---

# 32. ADDITIONAL FAILURE TESTS

Before commissioning PASS, also prove:

## RECONCILER RESTART

Restart the reconciler/supervisor.

Expected:

* project survives;
* WorkItems survive;
* no duplicate task graph;
* leases reconcile.

## DATABASE/STATE RELOAD

Restart relevant app/service safely.

Expected:

* durable project state survives.

## DUPLICATE CLAIM

Attempt concurrent claim of same WorkItem.

Expected:

* exactly one lease succeeds.

## STALE EVIDENCE

Change relevant code after evidence generation in a controlled fixture.

Expected:

* affected evidence becomes stale;
* requirement does not remain falsely accepted.

## FALSE COMPLETION

Stop all intelligent agents while incomplete READY work exists.

Expected:

* project remains incomplete;
* reconciler continues.

---

# 33. COMMISSIONING METRICS

Produce:

```
AUTONOMY_KERNEL_METRICS.json
```

At minimum:

```
WorkItems created
WorkItems eventually accepted
first-attempt acceptance count
rework count
failed Attempts
interrupted Attempts
lease recoveries
duplicate claims
merge conflicts
human interventions
false completion incidents
stalled minutes
strong-model invocations
free-model invocations
reported paid inference cost
accepted WorkItems / hour
average/median completion time
```

Do not optimize raw agent activity.

Optimize accepted useful work.

---

# 34. COMMISSIONING PASS CONDITIONS

Create a deterministic gate:

```
AUTONOMY_KERNEL_COMMISSIONING_GATE
```

It must NOT pass merely because tests are green.

Minimum conditions:

1. Durable Project/WorkItem/Attempt/Dependency/Artifact/Review/Event semantics exist.

2. WorkItem and Attempt are distinct.

3. Atomic leasing is tested.

4. Expired/dead worker recovery is tested.

5. Fresh worker reconstruction from durable state is tested.

6. No continuously alive Director is required for routine execution.

7. Context packets are task-specific rather than giant project dumps.

8. Implementation workers use isolated worktrees.

9. Implementers cannot approve their own work.

10. Merge/integration is serialized and tested.

11. QA rejection automatically produces rework.

12. Machine-generated evidence attaches to exact revisions.

13. Acceptance state is deterministic/derived.

14. Project progress is measurable separately from process liveness.

15. Event ledger is functioning.

16. Semantic failure classes exist.

17. A provider failure does not cause project loss or paid fallback.

18. Reconciler restart does not lose the project.

19. No false project completion occurs during tests.

20. All ten commissioning WorkItems eventually reach their legitimate terminal result, with all required ones ACCEPTED.

21. Zero routine user intervention was required during the commissioning loop.

22. New pay-as-you-go inference cost remains zero unless user explicitly changed policy.

23. Existing product test/build baseline has not been silently destroyed.

24. Existing user-owned source material remains intact.

25. Exactly one scheduling/control authority exists for the new lifecycle.

---

# 35. COMMISSIONING FAILURE BEHAVIOR

If the gate fails:

DO NOT stop and tell the user:

```
“The kernel isn't ready.”
```

Instead:

1. identify the failed commissioning condition;
2. create a bounded kernel-repair WorkItem;
3. execute;
4. test;
5. review where required;
6. integrate;
7. rerun the failed commissioning test;
8. rerun the gate.

Repeat.

Only stop for a genuine human blocker.

---

# 36. OLD META-DIRECTOR MIGRATION

Once the new reconciler has successfully demonstrated commissioning:

* remove the old requirement that an unfinished project implies one continuously running Meta-Director;
* disable obsolete restart behavior that merely generates new Director generations;
* preserve historical logs/state;
* retain a fresh Project Director launcher as an **event-driven planning capability**;
* update supervisor configuration accordingly;
* prevent simultaneous old/new scheduling.

Do not leave dormant code configured in a way that can unexpectedly reactivate duplicate orchestration.

---

# 37. GENERATED RUNTIME STATE MUST LEAVE THE SOURCE CHECKOUT

The September audit found source, runtime artifacts, evidence and test-result material mixed in a dirty working tree.

Correct this.

Where appropriate, move ephemeral state to a dedicated runtime/state location, for example under:

```
~/.local/state/empirium/
```

or a superior existing project convention.

Git should contain:

* source;
* migrations;
* deterministic configuration templates;
* documentation;
* tests;
* versioned contracts.

Git should generally not be polluted by:

* live leases;
* transient PID data;
* temporary screenshots not intended as fixtures;
* runtime queue state;
* constantly rewritten live evidence;
* provider health cache;
* generated process telemetry.

Do not move something without understanding current consumers.

Migrate safely.

---

# 38. HUMAN-ONLY BLOCKER STANDARD

Interrupt the user only if there is genuinely no safe authorized autonomous path.

Examples:

* interactive subscription authentication is required;
* sudo/password is required and unavailable;
* a required user-owned source file truly does not exist anywhere accessible;
* an irreversible destructive choice lacks authorization;
* public deployment needs explicit approval;
* two materially different product choices require subjective owner preference and neither has a safe reversible default;
* a provider/account requires a human action that software cannot perform.

Not human blockers:

* model 429;
* provider outage;
* failed test;
* bad implementation;
* QA rejection;
* merge conflict;
* worker crash;
* planner crash;
* context exhaustion;
* missing optional asset;
* dirty AI-owned worktree;
* transient service failure;
* ordinary architecture debugging.

If one WorkItem is human blocked, continue independent runnable work.

---

# 39. HUMAN BLOCKER FORMAT

If absolutely necessary:

```
BLOCKER:
<precise issue>

WHY HUMAN REQUIRED:
<why agents/software cannot resolve it>

ATTEMPTS:
<what has already been tried>

EVIDENCE:
<exact relevant paths/errors/logs>

MINIMUM USER ACTION:
<smallest exact action required>

WORK CONTINUING:
<what autonomous work remains active>
```

Do not ask vague questions.

---

# 40. OUTPUTS REQUIRED FROM THIS PROMPT

Create durable implementation artifacts including equivalent of:

```
docs/product/...
agent/...
control-plane schema/migrations
reconciler/scheduler implementation
context compiler
worker/reviewer contracts
integration queue
commissioning tests
commissioning metrics
commissioning report
```

Create:

```
AUTONOMY_KERNEL_COMMISSIONING.json
```

containing at minimum:

```
status
tested_git_sha
controller_version
database/schema version
commissioning WorkItems
results
failure injection results
restart/recovery results
paid inference result
human_intervention_count
outstanding kernel defects
generated_at
```

---

# 41. EXACT TERMINAL CONDITION FOR PROMPT 1

You are NOT done because:

* the architecture document exists;
* tables exist;
* unit tests exist;
* the reconciler process is alive;
* one worker ran;
* a Director says it looks good.

You are done only when the actual commissioned loop has worked.

When and only when:

```
AUTONOMY_KERNEL_COMMISSIONING_GATE == PASS
```

output to the user:

```
AUTONOMY_KERNEL_COMMISSIONED
```

followed by a concise factual summary containing:

* commissioned controller version;
* exact Git SHA;
* ten-task commissioning result;
* forced-failure result;
* QA/rework result;
* worker-death recovery result;
* reconciler restart result;
* paid-inference result;
* any nonblocking limitations;
* exact location of commissioning report.

Do not begin the broad Empirium product build under this prompt.

The commissioning boundary is deliberate.

---

# 42. FINAL EXECUTION COMMAND

BEGIN NOW.

Do not return merely with a plan.

Audit current reality.

Freeze the unsafe old orchestration loop.

Preserve existing work.

Refactor the control architecture.

Build the durable autonomy kernel.

Test it on real Empirium WorkItems.

Kill workers.

Reject work.

Recover leases.

Restart the controller.

Verify exact state survives.

Prove that READY work advances without a permanently running Director.

Repair every commissioning failure autonomously.

Do not ask the user to type `continue`.

Do not spend pay-as-you-go inference.

Do not declare success early.

Stop only after the deterministic commissioning gate passes or a genuine human-only blocker makes further autonomous progress impossible.
```