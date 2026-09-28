

===== 2026-09-15 21:39 | session 20260915_213920_f0f5d2 | Empirium OS forensic audit for AI Workforce =====
@file:`.hermes/attachments/Pasted content (48-2.9 KB)`

--- Attached Context ---

📄 @file:`.hermes/attachments/Pasted content (48-2.9 KB)` (11955 tokens)
```
# EMPIRIUM OS → AI WORKFORCE
# PHASE 0: COMPLETE FORENSIC AUDIT AND IMPLEMENTATION-READINESS INVESTIGATION

You are conducting a COMPLETE, FORENSIC, READ-ONLY AUDIT of my existing Empirium OS application and the Hermes Studio / Hermes components already embedded inside it.

This is NOT the implementation phase.

DO NOT build the AI Workforce yet.
DO NOT refactor production code yet.
DO NOT make speculative changes.
DO NOT "clean things up" merely because you notice something imperfect.

Your job is to investigate the existing software exhaustively enough that another AI can subsequently produce a complete autonomous implementation plan and implementation prompt with essentially no missing technical context.

You may create audit documents, screenshots, temporary analysis files, cloned reference repositories, temporary scripts, test artefacts, logs, diagrams and reports in a SEPARATE AUDIT WORKSPACE.

Do not intentionally alter the Empirium OS working tree.

If a test/build process itself creates normal generated files, caches or build artefacts, record that fact and clean them up where safe.

==========================================================
MISSION
==========================================================

Determine EXACTLY how Empirium OS currently works, EXACTLY how Hermes Studio has been embedded into it, EXACTLY how Conductor works inside the embedded version, and EXACTLY what can be reused, extracted, adapted or extended to create the AI Workforce system described below.

The final implementation will ultimately introduce:

AI ORGANIZATION
    ↓
DEPARTMENTS
    ↓
PERSISTENT SPECIALIST AGENTS
    ↓
PROJECTS
    ↓
TASKS
    ↓
RUNS / CONDUCTOR MISSIONS
    ↓
QA
    ↓
KNOWLEDGE / OBSIDIAN
    ↓
LEARNING
    ↓
PROMPT + PLAYBOOK EVOLUTION
    ↓
MODEL ROUTING + COST CONTROL
    ↓
HISTORY / ACTIVITY / AUDITABILITY

The first real department will be:

PERSONAL SOFTWARE DEPARTMENT

Its purpose:

"Build, maintain, test, improve and learn from all of Ash's personal software."

Initial persistent roles:

1. Software Director
2. Research / Architecture Engineer
3. Implementation Engineer
4. QA / Review Engineer
5. Learning Analyst

These are persistent organizational roles.

They are NOT necessarily permanently running processes.

When idle they must remain visually represented.

When working they may map to Hermes sessions / workers / Conductor agents.

When the temporary run ends, the persistent organizational agent remains.

==========================================================
THE PRODUCT WE ARE PREPARING TO BUILD
==========================================================

The eventual user experience should behave approximately like this:

EMPIRIUM OS
    ↓
AI ORGANIZATION OVERVIEW

The organization overview contains MANY departments.

Each department appears as a visually rich card.

Each card includes approximately:

- department name
- department mission
- operational status
- miniature office / visual representation
- actual number of agents assigned to that department
- which agents are working
- active projects
- today's work
- QA health
- current spend
- current activity
- perhaps pending learning/improvement items

There is NO need for a permanent left-side navigation bar inside this AI Workforce interface.

The organization overview itself should scale to many departments efficiently.

Clicking a department opens its full Department View.

==========================================================
DEPARTMENT VIEW
==========================================================

Each department may have a DIFFERENT:

- number of agents
- roles
- personalities
- models
- tools
- MCPs
- memory scopes
- prompts
- skills
- rules
- budget
- projects
- recurring jobs
- visual office layout

The Personal Software Department should ultimately expose at minimum:

OVERVIEW
PROJECTS
TASKS
AGENTS
QA
KNOWLEDGE
LEARNING
HISTORY
MODELS & COST
SETTINGS

Its Overview should include:

- live visual office
- persistent agent desks / positions
- live working state
- active projects
- upcoming work
- completed work
- current activity
- statistics
- department QA
- knowledge summary
- learning/improvement summary
- model/cost summary

==========================================================
VISUAL AGENT / ROBOT CONCEPT
==========================================================

The eventual system should retain and expand the visually appealing character/office concepts already present in Hermes Studio Conductor.

Every persistent specialist should eventually have a configurable visual identity.

Potential configurable attributes include:

- base robot/avatar design
- color palette
- screen / face appearance
- screen color
- body accents
- status lighting
- gadgets
- accessories
- equipment
- desk equipment
- monitor arrangement
- technology aesthetic
- personality
- movement style
- idle animation
- walking/floating/rushing animation
- work animation
- busy animation
- blocked animation
- QA/review animation
- thinking animation
- interaction with office objects

Agents should feel alive.

Examples:

IDLE:
slow floating / subtle movement

WORKING:
moves to appropriate workplace or visibly works

VERY BUSY:
faster movement, increased animation intensity and visible RED FLASHING status light

BLOCKED:
different visual state

REVIEWING:
QA/review animation

RESEARCHING:
research-specific animation or environment interaction

Agents may move around / float / rush between office locations depending on activity.

The office itself should eventually support interaction with agents.

Examples could include:

- desk
- terminal
- monitor
- whiteboard
- QA station
- research terminal
- server rack
- charging station
- meeting area
- project board
- knowledge terminal

DO NOT design or generate these assets during this audit.

Instead investigate EXACTLY what current rendering/animation technology exists and what implementation approach is most compatible.

==========================================================
CONDUCTOR CONCEPT
==========================================================

A key question of this audit is determining how the embedded Hermes Studio Conductor actually works.

We currently think the ideal abstraction may be:

DEPARTMENT = persistent organization

AGENT = persistent specialist

PROJECT = persistent body of work

TASK = durable work item

RUN = one execution attempt

CONDUCTOR = temporary orchestration mechanism for complex work

HERMES SESSION / WORKER = actual temporary execution process

When a persistent department agent starts working:

Persistent agent
    ↓
Hermes session / worker
    ↓
possibly Conductor mission worker
    ↓
execution occurs
    ↓
session ends
    ↓
persistent department agent remains
    ↓
status returns to idle

AUDIT WHETHER THIS IS TECHNICALLY CORRECT.

DO NOT simply assume it.

Trace the actual source code.

==========================================================
KNOWLEDGE AND MEMORY CONCEPT
==========================================================

The future architecture should probably distinguish:

GLOBAL MEMORY
    ↓
DEPARTMENT MEMORY
    ↓
PROJECT MEMORY
    ↓
AGENT / ROLE MEMORY

Obsidian is intended to become the major human-readable institutional knowledge repository.

Operational records should NOT simply become Obsidian notes.

We likely want:

DATABASE:
- departments
- agents
- projects
- tasks
- runs
- events
- QA
- budgets
- model use
- prompt versions
- learning proposals
- permissions
- memory links

OBSIDIAN:
- architecture
- decisions
- research
- coding standards
- design preferences
- project knowledge
- lessons learned
- reusable playbooks
- known problems
- model findings
- historical summaries

Agents should retrieve only relevant knowledge rather than receiving the entire vault.

Audit ALL current memory/storage mechanisms and determine what already exists that can support this.

==========================================================
LEARNING CONCEPT
==========================================================

The eventual system must learn from completed work.

Desired loop:

WORK
    ↓
EVALUATION
    ↓
LESSONS
    ↓
MEMORY
    ↓
PLAYBOOK
    ↓
PROMPT / MODEL POLICY
    ↓
NEXT RUN

Learning signals may include:

- successful outcome
- failed outcome
- tests
- QA results
- retries
- human corrections
- regressions
- costs
- latency
- model used
- reviewer score
- files changed
- task type
- complexity
- retrieved memory
- tools used

IMPORTANT:

Agents should NOT autonomously mutate critical prompts without control.

Initially:

experience
    ↓
candidate lesson
    ↓
evidence
    ↓
learning proposal
    ↓
evaluation
    ↓
human approval
    ↓
new prompt/playbook version

Audit anything already present in Hermes Studio / Hermes relating to:

- Patterns & Corrections
- memory
- prompt management
- agent configuration
- session history
- audit history
- feedback
- agent learning
- knowledge graphs
- evaluations
- corrections

==========================================================
MODEL ECONOMICS
==========================================================

The eventual system must optimise for QUALITY PER UNIT COST, not simply cheapest token price.

There will be:

FREE COMPUTE
SUBSCRIPTION COMPUTE
PAID API COMPUTE

Free models should be used aggressively where they work.

Connected subscription capacity should also be treated differently from incremental API cash spend.

Paid OpenRouter use should be reserved for cases where it materially improves expected success.

Model selection should ultimately be based on:

task type
complexity
risk
historical performance
expected success
model availability
latency
cash cost
subscription availability
remaining task/project budget

A large Personal Software project should eventually have:

HARD PAID-INFERENCE / EXTERNAL-ASSET CEILING:
$1.50 unless Ash explicitly authorizes more.

The WHOLE AI WORKFORCE IMPLEMENTATION PROJECT has:

TOTAL OPENROUTER + PAID GENERATED ASSET BUDGET:
$5.00

THIS AUDIT IS PART OF THAT TOTAL.

Therefore:

AUDIT OPENROUTER CASH SPEND HARD LIMIT:
$0.40

Target:
$0.00 if practical.

Use FREE models for:
- repository scanning
- file classification
- bulk summarisation
- search
- code indexing
- duplicate detection
- trivial analysis

Use already-connected subscription compute where appropriate.

Paid OpenRouter inference may ONLY be used where free/subscription approaches are materially insufficient.

Do not pay for image generation during this audit.

If a free model fails twice on the SAME analysis step:
STOP repeating the same attempt.
Change strategy/model.

Record EVERY paid call if Hermes exposes that information.

==========================================================
AUTONOMY
==========================================================

This is intended to be autonomous.

Do not repeatedly ask Ash questions.

Investigate.

Use tools.

Inspect code.

Inspect processes.

Inspect repositories.

Read documentation.

Run tests.

Take screenshots.

Compare upstream code.

Delegate to subagents.

Cross-check findings.

If the mission takes many hours or must be broken into batches, THAT IS FINE.

Maintain state on disk.

Resume intelligently.

Do not abandon the mission merely because context becomes large.

Create persistent audit artefacts after each major phase.

If you hit a blocker:

1. investigate alternatives
2. inspect logs
3. search local documentation
4. inspect repository history
5. inspect upstream repositories
6. try another read-only method
7. use a specialist subagent
8. document the blocker

Only stop early if the blocker genuinely prevents further investigation.

==========================================================
ABSOLUTE SAFETY RULES
==========================================================

THIS IS A READ-ONLY PRODUCT AUDIT.

DO NOT:

- rewrite source code
- refactor production files
- upgrade dependencies
- install dependencies into the product unless strictly required for a test and safely reversible
- modify database schemas
- modify production data
- modify user notes
- modify Obsidian vault contents
- modify Hermes profiles
- modify prompts
- change models
- change MCP configuration
- change firewall configuration
- change Caddy
- change PostgreSQL
- change production environment variables
- deploy anything
- push commits
- merge branches
- delete files
- reset Git state
- stash user work
- discard uncommitted changes
- expose secrets
- include raw secret values in reports

You MAY:

- read
- search
- inspect
- run read-only queries
- run existing tests
- run existing builds if safe
- run lint/typechecking
- inspect screenshots/UI
- inspect Git history
- inspect process state
- inspect database schemas read-only
- clone public reference repositories into a SEPARATE audit/reference directory
- create audit files outside the product repository
- make TEMPORARY copies of code for analysis
- create diagrams/reports outside the product repo

If an operation could alter user/production data:
DO NOT EXECUTE IT.

==========================================================
FIRST ACTION: IDENTIFY THE REAL RUNNING APPLICATION
==========================================================

Do not assume a folder name.

There have historically been multiple Empirium OS copies / folders.

Start from what is ACTUALLY RUNNING.

Determine:

- executable/process
- process command line
- current working directory if discoverable
- Electron entry point
- active repository
- active branch
- HEAD commit
- dirty/uncommitted files
- remotes
- startup mechanism
- relevant ports
- child processes
- backend processes
- current frontend URL if applicable

If a currently running Empirium OS process exists, establish which source tree it actually uses.

Use this as authoritative unless evidence proves otherwise.

Record EXACT evidence.

Do NOT repeat previous assumptions.

==========================================================
CREATE A DEDICATED AUDIT WORKSPACE
==========================================================

Create a SEPARATE workspace such as:

empirium-os-ai-workforce-audit/
    README.md
    MASTER_AUDIT.md
    IMPLEMENTATION_CONTEXT.md
    FILE_MAP.md
    CONDUCTOR_FORENSICS.md
    HERMES_INTEGRATION.md
    DATA_MODEL_AUDIT.md
    UI_ARCHITECTURE.md
    TEST_BASELINE.md
    MEMORY_KNOWLEDGE_AUDIT.md
    MODEL_PROVIDER_AUDIT.md
    SECURITY_PERMISSIONS.md
    DEPLOYMENT_RUNTIME.md
    DONOR_CODE_RESEARCH.md
    LICENSING.md
    RISK_REGISTER.md
    BUILD_RECOMMENDATION.md
    OPEN_QUESTIONS.md
    screenshots/
    diagrams/
    logs/
    manifests/
    references/
    test-results/

Name files clearly.

Add timestamps where useful.

==========================================================
SUBAGENT STRATEGY
==========================================================

Use as many specialist subagents as useful.

Run independent investigations in parallel where safe.

Suggested roles:

A. REPOSITORY FORENSICS AGENT
B. HERMES STUDIO / CONDUCTOR AGENT
C. FRONTEND / UI ARCHITECTURE AGENT
D. BACKEND / API AGENT
E. DATA / STORAGE AGENT
F. HERMES RUNTIME / GATEWAY AGENT
G. MODEL / PROVIDER / COST AGENT
H. MEMORY / OBSIDIAN AGENT
I. TESTING / QA AGENT
J. SECURITY / PERMISSIONS AGENT
K. DEPLOYMENT / INFRASTRUCTURE AGENT
L. OPEN-SOURCE DONOR CODE AGENT
M. ANIMATION / VISUAL ENGINEERING AGENT
N. PERFORMANCE AGENT
O. LICENSE / DEPENDENCY AGENT
P. CROSS-CHECK / RED-TEAM AGENT

Do NOT create subagents just for theatre.

Give each a narrow investigation scope and require evidence.

At least one final agent should independently challenge the conclusions of the others.

==========================================================
PHASE 1 — REPOSITORY FORENSICS
==========================================================

Identify every repository or directory materially involved in Empirium OS.

For the authoritative running application capture:

- absolute path
- Git repository root
- current branch
- current HEAD
- remote URLs
- relevant tags
- recent commit history
- uncommitted changes
- ignored/generated directories
- package manager
- lock files
- Node version requirements
- Electron version
- frontend framework
- build system
- bundler
- CSS system
- state management
- database libraries
- API libraries
- testing libraries
- animation libraries
- graphics libraries
- WebSocket/SSE libraries
- IPC libraries
- process management libraries

Create:

REPOSITORY MAP

For every major directory:

PATH
PURPOSE
FRAMEWORK
ENTRY POINT
IMPORTANT FILES
RISK IF MODIFIED

==========================================================
PHASE 2 — MAP THE ENTIRE APPLICATION ARCHITECTURE
==========================================================

Trace startup from executable to rendered UI.

Document:

Electron main process
preload
renderer
browser windows
webviews
iframes
embedded apps
local servers
remote services
IPC
REST APIs
WebSockets
SSE
background workers
database connections
filesystem integrations
Hermes integrations
Obsidian integrations
authentication
configuration loading

Create architecture diagrams.

Use Mermaid if convenient.

Document:

APP START
    ↓
MAIN
    ↓
PRELOAD
    ↓
RENDERER
    ↓
ROUTES
    ↓
HERMES STUDIO
    ↓
HERMES
    ↓
MODEL / TOOL / MCP LAYER

but BASE IT ON ACTUAL SOURCE.

==========================================================
PHASE 3 — FORENSICALLY LOCATE THE EMBEDDED HERMES STUDIO
==========================================================

Determine EXACTLY how Hermes Studio was added.

Possible forms include:

- copied source
- git subtree
- embedded web app
- iframe
- local server
- bundled package
- fork
- partial component port
- mixed integration

Do not assume.

Identify:

- exact Studio-related directories
- components copied
- routes copied
- stores copied
- hooks copied
- services copied
- CSS/theme copied
- assets copied
- server components copied
- gateway code copied
- Conductor code copied
- Tasks/Kanban code copied
- Operations code copied
- Agent Library code copied
- Knowledge components copied
- Cost components copied
- Cron components copied

For each relevant file produce:

FILE
ORIGIN IF IDENTIFIABLE
PURPOSE
DEPENDENCIES
CURRENT MODIFICATIONS
REUSABILITY
COUPLING
REFACTOR RISK

==========================================================
PHASE 4 — IDENTIFY UPSTREAM HERMES STUDIO VERSION
==========================================================

Use GitHub/public sources if needed.

Compare embedded code against current and historical Hermes Studio source.

Determine where possible:

- upstream repository
- likely originating commit/tag/version
- files that match upstream
- files modified locally
- files missing
- newer useful upstream features not embedded
- any breaking changes between embedded and latest versions

DO NOT merge anything.

Produce a DIFF/PROVENANCE report.

==========================================================
PHASE 5 — CONDUCTOR FORENSICS
==========================================================

THIS IS ONE OF THE MOST IMPORTANT PHASES.

Trace Conductor end-to-end.

Find and document:

- Conductor entry route
- Conductor screen/components
- office rendering
- worker rendering
- agent avatars
- layouts
- worker state
- mission state
- gateway hooks
- mission lifecycle
- worker lifecycle
- session lifecycle
- polling
- WebSocket/SSE if present
- Hermes Gateway/ACP communication
- task creation
- worker launch
- model assignment
- cost tracking
- completion handling
- cancellation
- errors
- history storage
- localStorage
- persistence
- event logs
- speech bubbles
- animation logic
- movement logic
- agent location logic
- office layout definitions
- status visualization
- configuration

Trace ONE mission from:

user starts mission
    ↓
mission object created
    ↓
plan created
    ↓
workers created
    ↓
Hermes execution begins
    ↓
states update
    ↓
office reacts
    ↓
results arrive
    ↓
costs/events update
    ↓
mission completes
    ↓
history persists

Give exact source files and important symbols/functions.

Answer explicitly:

CAN OFFICEVIEW BE REUSED WITH PERSISTENT DEPARTMENT AGENTS?

If YES:
explain exact refactor.

If NO:
explain why and alternative.

Determine whether a clean interface can be created such as:

<OfficeView
  workers={departmentAgents}
  layout={department.officeLayout}
/>

while still allowing:

<OfficeView
  workers={missionWorkers}
  layout={mission.officeLayout}
/>

Do not implement.

==========================================================
PHASE 6 — OPERATIONS / TASKS / KANBAN FORENSICS
==========================================================

Audit all existing work-management functionality.

Find:

- Kanban
- Tasks
- statuses
- Backlog
- Todo
- In Progress
- Review
- Done
- task persistence
- mission/task links
- priorities
- due dates
- assignees
- scheduled work
- Cron
- background jobs
- Operations dashboard
- history
- logs
- notifications
- event feeds

Determine exactly what can become:

DEPARTMENT
    ↓
PROJECT
    ↓
TASK
    ↓
RUN

Identify what is already present and what must be created.

==========================================================
PHASE 7 — AGENT DEFINITIONS
==========================================================

Audit all concepts related to persistent agents.

Investigate:

- Hermes profiles
- Hermes Studio Agent Library
- SOUL
- system prompts
- skills
- tools
- MCPs
- model settings
- memory
- working directories
- permissions
- configuration
- sessions
- per-agent costs
- agent history

Determine whether our future persistent specialist should map to:

A. Hermes Profile
B. Hermes Studio Agent definition
C. new Empirium Department Agent entity
D. combination

Recommend the cleanest abstraction.

We likely want the organizational identity to survive individual execution sessions.

Determine exact mapping strategy.

==========================================================
PHASE 8 — MODEL PROVIDERS AND ROUTING
==========================================================

Inventory EVERY currently available model/provider route.

Do NOT reveal API keys.

Identify:

- OpenRouter
- direct providers
- local models
- connected subscription-backed models
- Hermes provider configuration
- model aliases
- defaults
- fallbacks
- free models
- paid models
- per-model pricing if available locally
- rate limits if known
- usage accounting
- cost logs
- current model router behavior

Specifically determine whether these can be used programmatically from Hermes:

- free OpenRouter models
- OpenAI / Codex subscription-backed execution
- GPT/Luna variants available through connected subscription
- Anthropic subscription-backed Sonnet
- Anthropic subscription-backed Opus
- any current local models
- any other free provider models

Do not assume availability.

VERIFY.

Document:

MODEL
PROVIDER
ACCESS METHOD
CASH MARGINAL COST
SUBSCRIPTION OR API
STRENGTHS
LATENCY IF KNOWN
RESTRICTIONS
CAN HERMES SPAWN IT?
CAN CONDUCTOR ASSIGN IT?
CAN AGENT OVERRIDE IT?

==========================================================
PHASE 9 — COST ACCOUNTING
==========================================================

Determine:

- whether Hermes Studio already calculates model cost
- where cost data originates
- per-session cost
- per-agent cost
- per-model cost
- mission cost
- daily cost
- persisted cost history
- whether free calls show zero correctly
- how subscription compute appears
- whether budgets are supported
- whether hard limits can be enforced

Determine where a future:

PROJECT MAX CASH COST = $1.50

could be technically enforced.

Do NOT rely solely on LLM obedience.

Find a deterministic enforcement point.

==========================================================
PHASE 10 — DATABASE / PERSISTENCE
==========================================================

Inventory ALL persistent data systems.

Examples:

PostgreSQL
SQLite
localStorage
IndexedDB
JSON files
filesystem
Obsidian
Hermes files
session files
logs

For PostgreSQL:

READ ONLY.

Capture:

- version
- databases
- schemas
- tables
- important columns
- relationships
- indexes where relevant
- existing migrations
- database libraries
- connection architecture

Never expose passwords.

Determine the correct place for future entities:

departments
department_agents
projects
tasks
runs
run_events
qa_reviews
agent_configs
prompt_versions
model_policies
budget_policies
memory_scopes
knowledge_links
learning_events
learning_proposals
department_events
agent_visual_profiles

Recommend:

existing DB?
new schema?
new database?

Explain trade-offs.

==========================================================
PHASE 11 — OBSIDIAN / MEMORY AUDIT
==========================================================

Find how Obsidian currently interacts with Hermes / Empirium OS.

Identify:

- actual vault location if accessible
- how software accesses it
- MCPs
- filesystem access
- plugins
- REST APIs
- search
- embeddings
- indexing
- retrieval
- write support
- read support
- authentication
- permissions
- sync

DO NOT modify the vault.

Determine how future memory scopes could work:

global
department
project
agent

Determine whether metadata/frontmatter/tagging/path conventions would work best.

Recommend retrieval architecture.

Also audit Hermes native memory mechanisms:

- MEMORY.md
- USER.md
- profile memory
- other memory providers
- context injection

Determine what belongs in always-on Hermes memory versus retrieved Obsidian knowledge.

==========================================================
PHASE 12 — PROMPTS / LEARNING / CORRECTIONS
==========================================================

Find all current code related to:

prompts
system prompts
SOUL
skills
patterns
corrections
agent memory
prompt templates
prompt versioning
evaluation
feedback
history
learning
knowledge graph

Determine what can support:

PROMPT VERSION HISTORY

Example:

Implementation Engineer
v7 → v8
rule added:
"Inspect route registry before modifying navigation."

The eventual system must store:

- previous prompt
- proposed prompt
- reason
- evidence
- evaluator result
- approval
- rollout date
- performance after rollout
- rollback capability

Identify what exists and what needs building.

==========================================================
PHASE 13 — QA / TESTING AUDIT
==========================================================

Inventory all test infrastructure.

Find:

- unit tests
- integration tests
- E2E
- Playwright
- Electron testing
- browser tests
- screenshots
- visual regression
- lint
- TypeScript
- build
- security checks
- accessibility checks
- smoke tests

Run the CURRENT SAFE TEST BASELINE.

Do not modify production data.

Record commands and COMPLETE results.

Attempt:

install-state verification
typecheck
lint
tests
build
safe runtime smoke test

where supported.

If something fails:
record exact failure.

Do not silently fix it.

Create:

TEST_BASELINE.md

including:

COMMAND
RESULT
DURATION
FAILURES
KNOWN PREEXISTING?
EVIDENCE

==========================================================
PHASE 14 — MANUAL UI / VISUAL BASELINE
==========================================================

Launch the current application safely if necessary.

Take screenshots of important current views including:

- Empirium OS home
- embedded Hermes Studio
- Conductor home
- Conductor mission preview
- Conductor active mission if safely testable
- Operations
- Tasks/Kanban
- Agent Library
- Costs
- Knowledge
- Settings
- any relevant agent/profile screen

DO NOT trigger expensive real work merely for screenshots.

If Conductor can run a harmless zero/near-zero-cost test using a free model and isolated task, that is allowed only if safe.

Capture baseline dimensions and responsiveness if practical.

==========================================================
PHASE 15 — VISUAL / ANIMATION TECH AUDIT
==========================================================

We need to eventually create animated configurable robots and department offices.

Determine existing technologies:

React?
DOM?
CSS animation?
Framer Motion?
Canvas?
SVG?
PixiJS?
Three.js?
WebGL?
Lottie?
GSAP?
sprite sheets?
CSS transforms?
requestAnimationFrame?
Electron GPU acceleration?

Find exactly how current Conductor avatars and office visuals are rendered.

Determine:

- current asset formats
- current animation formats
- frame rates
- rendering cost
- layout system
- sprite/image handling
- responsive scaling
- z-index/layering
- hit testing
- interactions
- performance implications

Evaluate future options:

A. DOM/CSS/SVG
B. sprite-based 2D
C. Canvas/PixiJS
D. Three.js/WebGL
E. hybrid

The overview page may ultimately show MANY miniature departments simultaneously.

Therefore analyse:

- CPU cost
- GPU cost
- memory
- Electron performance
- number of animated agents
- number of department cards
- whether mini offices should be static snapshots
- whether animation should start only on hover / viewport visibility
- whether full animation should exist only inside opened department
- caching strategies
- reduced-motion support

Provide recommendation.

==========================================================
PHASE 16 — AGENT VISUAL CUSTOMIZATION DATA MODEL
==========================================================

DO NOT build assets.

Design only the likely technical representation.

Investigate feasibility for a future profile such as:

agent_visual_profile
    base_model
    body_style
    primary_color
    secondary_color
    screen_style
    screen_color
    eye_style
    gadgets[]
    accessories[]
    desk_style
    monitor_style
    role_badge
    idle_animation
    work_animation
    busy_animation
    blocked_animation
    review_animation
    movement_style
    personality_visual_intensity

Determine whether these can be implemented by:

layered SVG
sprite composition
CSS variables
Canvas sprite layers
generated image variants
or another approach.

Since TOTAL implementation budget is only $5, prioritize reusable procedural/customizable visuals over generating hundreds of separate images.

We want a system where ONE base visual framework can create many unique agents.

==========================================================
PHASE 17 — SECURITY AND PERMISSIONS
==========================================================

Audit:

- CSP
- Electron context isolation
- nodeIntegration
- preload exposure
- IPC allowlists
- filesystem permissions
- database credentials
- Hermes access
- MCP access
- network listeners
- local-only services
- exposed ports
- authentication
- secrets
- environment variables
- write capabilities

DO NOT print secret values.

Determine how future agent tool permissions could be enforced.

Example:

Implementation Engineer:
✓ Git
✓ terminal
✓ project filesystem
✓ tests

✗ finance
✗ personal diary
✗ production deploy without approval

Determine whether enforcement exists already or needs a policy layer.

==========================================================
PHASE 18 — DEPLOYMENT / RUNTIME
==========================================================

Map the actual operational topology.

Potential components may include:

Windows machine
Empirium OS Electron
local worker
VPS
Hermes
Hermes Studio
PostgreSQL
Caddy
Tailscale
Obsidian
OpenRouter
external APIs

VERIFY EVERYTHING.

Produce:

deployment diagram
network diagram
process diagram
service ownership
ports
startup procedures
restart procedures
build procedures
deployment procedures
rollback procedures

Do not reveal secrets.

==========================================================
PHASE 19 — OPEN SOURCE DONOR CODE RESEARCH
==========================================================

Research current public repositories that may contain reusable implementation patterns or code.

At minimum inspect:

Hermes Studio
Hermes War Room
Hermes Workspace
Builderz Mission Control

Also inspect any other HIGHLY relevant open-source systems discovered during research.

For each donor repository determine:

PROJECT
REPOSITORY
LICENSE
RELEVANT FILES
FEATURES WORTH REUSING
COPY DIRECTLY?
ADAPT?
INSPIRATION ONLY?
INTEGRATION RISK

Focus particularly on:

- persistent visible agents
- department/workspace structures
- agent cards
- live activity feeds
- delegation trees
- task boards
- project management
- session history
- observability
- budget controls
- approvals
- agent permissions
- animation systems
- prompt management
- memory visualization

Do not copy anything into Empirium OS during this audit.

Clone references separately if useful.

==========================================================
PHASE 20 — LICENSE AUDIT
==========================================================

For every codebase we may salvage code from:

record exact license.

Identify:

- MIT
- Apache
- GPL
- AGPL
- PolyForm
- proprietary restrictions
- unclear licensing

Flag anything we should NOT directly copy.

Also inspect current Empirium OS / embedded Hermes Studio attribution obligations.

Produce LICENSING.md.

==========================================================
PHASE 21 — PERFORMANCE BASELINE
==========================================================

Measure where practical:

application startup
renderer memory
CPU idle
CPU during Hermes Studio
CPU during Conductor
GPU usage if visible
number of renderer processes
bundle size
route load
large component renders
network polling frequency
session polling
event streaming
animation impact

We need to know whether many department cards with animated mini offices are practical.

Record baseline.

==========================================================
PHASE 22 — EXACT UI COMPONENT REUSE MAP
==========================================================

Produce a table of all existing components likely reusable for the future AI Workforce.

For each:

COMPONENT
FILE
CURRENT PURPOSE
DEPENDENCIES
REUSE TYPE:
- reuse unchanged
- extract
- refactor generic
- adapt
- replace

LIKELY FUTURE USE

Pay particular attention to:

OfficeView
AgentAvatar
Conductor Active
Conductor Gateway hooks
Mission history
Mission events
Cost tracker
Tasks/Kanban
Operations
Agent Library
Workflow DAG
Cron
Audit Trail
Session History
Patterns & Corrections
Knowledge Graph
MCP management
Model management

==========================================================
PHASE 23 — PROPOSE FUTURE ADAPTER BOUNDARY
==========================================================

Without implementing, design a clean API between the future Empirium organizational layer and Hermes.

Example conceptual interface:

listAgents()
getAgent(agentId)
getAgentStatus(agentId)
startRun(agentId, task)
stopRun(runId)
listRuns()
getRunEvents(runId)
createTask()
updateTask()
startConductorMission()
getMission()
getCosts()
listAvailableModels()
getModelUsage()
retrieveKnowledge()
recordQA()
recordLearningProposal()

Determine what is already supported directly.

Determine what requires adapters.

Determine what would require new backend endpoints.

==========================================================
PHASE 24 — PROPOSE FUTURE DATABASE MODEL
==========================================================

Without applying migrations, draft the full likely schema.

Include entities and key relationships for:

departments
agents
agent_visual_profiles
agent_model_policies
agent_tool_permissions
agent_memory_scopes
agent_prompt_versions

projects
tasks
runs
run_events

conductor_missions
mission_agent_links

qa_reviews
qa_checks
qa_evidence

knowledge_sources
knowledge_links
memory_retrieval_events

learning_events
learning_proposals
playbook_versions

model_catalog
model_performance
model_usage
cost_events
budget_policies

department_events
audit_events

schedules
background_jobs

Provide:

PKs
FKs
important fields
indexes
status enums
timestamps
soft-delete/archive strategy if useful

==========================================================
PHASE 25 — PERSONAL SOFTWARE DEPARTMENT CONFIGURATION
==========================================================

Draft, but do not instantiate, the first department.

PERSONAL SOFTWARE

Mission:
Build, maintain, test, improve and learn from Ash's personal software.

Roles:

SOFTWARE DIRECTOR

Responsibilities:
- receive request
- classify request
- determine complexity/risk
- create project/task decomposition
- choose model strategy
- control budget
- delegate
- decide escalation
- monitor completion
- request QA
- close project

RESEARCH / ARCHITECTURE ENGINEER

Responsibilities:
- inspect current architecture
- research solutions
- examine donor code
- investigate documentation
- create implementation approach
- identify risks
- produce ADRs where appropriate

IMPLEMENTATION ENGINEER

Responsibilities:
- modify software
- write code
- run tests
- follow coding standards
- create implementation evidence

QA / REVIEW ENGINEER

Responsibilities:
- validate requirements
- inspect diffs
- run automated tests
- run integration tests
- perform visual QA
- look for regressions
- verify security where applicable
- approve/reject work

LEARNING ANALYST

Responsibilities:
- inspect completed work
- extract lessons
- identify repeated failures
- identify successful strategies
- propose memory updates
- propose playbook updates
- propose prompt updates
- propose model-routing updates
- NEVER silently mutate critical prompts

For each role recommend:

Hermes mapping
prompt structure
tools
MCPs
memory scope
default model class
escalation model class
permissions
autonomy
visual office role
performance metrics

==========================================================
PHASE 26 — CURRENT-STATE GAP ANALYSIS
==========================================================

For every desired future capability classify:

ALREADY EXISTS
PARTIALLY EXISTS
MUST BE BUILT
SHOULD BE REUSED FROM DONOR
SHOULD NOT BE BUILT

Capabilities include:

organization overview
departments
persistent roles
office visualization
agent customization
animations
projects
tasks
runs
Conductor integration
live activity
QA
history
costs
budgets
memory scopes
Obsidian
learning
prompt versions
model routing
background work
scheduling
permissions
logs
audit
metrics
visual status
agent interaction with environment

==========================================================
PHASE 27 — IMPLEMENTATION RISK REGISTER
==========================================================

Identify every meaningful risk.

Examples:

breaking embedded Hermes Studio
tight coupling to Conductor internals
Hermes API instability
persistent-vs-session identity mismatch
localStorage limitations
database migration risk
Electron CSP
performance of many animations
model access limitations
subscription automation limitations
asset budget
provider rate limits
permissions
uncontrolled prompt self-modification
Obsidian synchronization
Windows/VPS boundaries

For each:

RISK
PROBABILITY
IMPACT
EVIDENCE
MITIGATION
HOW TO TEST

==========================================================
PHASE 28 — BASELINE REGRESSION CONTRACT
==========================================================

Before future implementation, define what MUST continue working.

Create an explicit regression contract based on the current app.

Examples could include:

- Empirium OS starts
- current dashboard renders
- Hermes Studio embed loads
- Hermes connection works
- Conductor existing flow works
- Tasks works
- Agents works
- existing synchronization works
- database access works
- personal software functions remain intact

But derive the real list from the software.

This becomes the implementation's minimum non-regression test suite.

==========================================================
PHASE 29 — IMPLEMENTATION RECOMMENDATION
==========================================================

At the end of the audit, recommend the lowest-risk build strategy.

We currently suspect:

EMBEDDED HERMES STUDIO
    ↓
extract reusable Conductor presentation components
    ↓
add Empirium Department organizational layer
    ↓
persistent Department Agents
    ↓
Projects / Tasks / Runs
    ↓
Conductor as temporary execution
    ↓
QA
    ↓
Obsidian knowledge
    ↓
Learning
    ↓
Model/cost router

But challenge this.

If the source indicates a better architecture, say so.

The recommendation must be based on evidence.

==========================================================
PHASE 30 — CREATE THE IMPLEMENTATION CONTEXT BUNDLE
==========================================================

This is the MOST IMPORTANT deliverable.

Create:

IMPLEMENTATION_CONTEXT.md

It must contain enough information for another strong AI model to write the COMPLETE implementation mission without re-auditing the machine.

It should include:

1. authoritative application location
2. Git state
3. app architecture
4. relevant technology stack
5. exact Hermes Studio embed architecture
6. exact Conductor architecture
7. exact relevant source files
8. component reuse map
9. backend/API map
10. database map
11. Hermes integration
12. profiles/agents model
13. tasks/Kanban model
14. cost model
15. model/provider inventory
16. Obsidian/memory architecture
17. test infrastructure
18. current test results
19. deployment topology
20. animation/rendering architecture
21. security constraints
22. donor code recommendations
23. licensing constraints
24. performance constraints
25. proposed future schema
26. Personal Software Department definition
27. risk register
28. regression contract
29. recommended implementation sequence
30. exact build/test/deploy commands
31. anything the implementation agent MUST NOT do
32. unresolved blockers if any

DO NOT merely provide vague prose.

USE EXACT FILE PATHS, FUNCTIONS, CLASSES, ENDPOINTS AND DATA STRUCTURES.

==========================================================
MANDATORY MACHINE-READABLE OUTPUTS
==========================================================

Also produce machine-readable files.

At minimum:

manifests/relevant-files.json
manifests/components.json
manifests/routes.json
manifests/services.json
manifests/apis.json
manifests/models.json
manifests/storage.json
manifests/tests.json
manifests/donor-code.json
manifests/risks.json

Where useful include:

{
  "path": "...",
  "purpose": "...",
  "dependencies": [],
  "future_use": "...",
  "change_risk": "low|medium|high"
}

==========================================================
MANDATORY SCREENSHOT PACK
==========================================================

Create labelled screenshots where possible.

Name them clearly.

Example:

01-current-empirium-home.png
02-hermes-studio-home.png
03-conductor-home.png
04-conductor-active.png
05-tasks.png
06-agents.png
07-operations.png

If something cannot be safely captured:
document why.

==========================================================
MANDATORY SOURCE EVIDENCE
==========================================================

Every major conclusion must cite evidence.

For code findings provide:

FILE PATH
SYMBOL/FUNCTION/COMPONENT
RELEVANT LINE RANGE IF PRACTICAL
SHORT EXPLANATION

Do not simply say:

"Conductor probably uses X."

Prove it.

==========================================================
RED-TEAM REVIEW
==========================================================

Once the audit appears complete, assign an independent reviewer.

Reviewer mission:

"Assume this audit is wrong or incomplete. Find missing dependencies, incorrect assumptions, hidden coupling, unsafe implementation recommendations, missing tests, and anything likely to cause the future autonomous build to fail."

Resolve or document every material criticism.

==========================================================
FINAL VALIDATION
==========================================================

Before declaring the audit complete verify:

[ ] authoritative running repo identified
[ ] Git state captured
[ ] Hermes Studio embed located
[ ] embedded Studio provenance investigated
[ ] Conductor traced end-to-end
[ ] office rendering traced
[ ] persistent-agent feasibility assessed
[ ] tasks/Kanban traced
[ ] model providers inventoried
[ ] paid/free/subscription access distinguished
[ ] cost tracking audited
[ ] hard-budget enforcement point identified
[ ] databases/storage inventoried
[ ] Obsidian integration investigated
[ ] memory systems investigated
[ ] prompt/learning mechanisms investigated
[ ] full safe test baseline executed
[ ] UI screenshot baseline captured
[ ] animation stack audited
[ ] agent customization feasibility evaluated
[ ] security reviewed
[ ] runtime/deployment topology mapped
[ ] donor repositories investigated
[ ] licenses checked
[ ] performance baseline captured
[ ] future adapter boundary proposed
[ ] future schema drafted
[ ] Personal Software department drafted
[ ] risk register completed
[ ] regression contract created
[ ] red-team review completed
[ ] IMPLEMENTATION_CONTEXT.md completed
[ ] machine-readable manifests completed
[ ] paid audit spend <= $0.40
[ ] Empirium OS production source remains unmodified

==========================================================
DEFINITION OF DONE
==========================================================

THIS AUDIT IS DONE ONLY WHEN:

1. Another AI can understand the actual current Empirium OS architecture without asking Ash to explain it.

2. Another AI can understand exactly how the embedded Hermes Studio works.

3. Another AI can understand exactly how Conductor creates, monitors and completes work.

4. We know precisely which current components can be reused for the AI Workforce.

5. We know precisely what must be newly built.

6. We know how persistent department agents should map to Hermes execution.

7. We know how Projects → Tasks → Runs → QA → Learning should persist.

8. We know how Obsidian should connect as institutional knowledge.

9. We know which models/providers are actually available and how they can be invoked.

10. We know where and how the $1.50-per-large-project hard cash ceiling can be enforced.

11. We know the safest rendering strategy for many visual departments and animated customizable robot agents.

12. We know the full current regression baseline.

13. We know the exact build/test/deployment commands.

14. We know all meaningful implementation risks.

15. Every major conclusion has source evidence.

16. The implementation context bundle is complete enough to use as the primary input to the next autonomous implementation mission.

17. No existing production functionality was intentionally modified.

18. The audit's OpenRouter spend did not exceed $0.40.

==========================================================
FINAL RESPONSE TO ASH
==========================================================

When everything above is complete, DO NOT dump thousands of lines into chat.

Respond with a concise completion report:

EMPIRIUM OS AI WORKFORCE AUDIT — COMPLETE

Authoritative repo:
<path>

Branch / HEAD:
<branch + commit>

Current app status:
<working / known failures>

Hermes Studio embedding:
<one-paragraph summary>

Conductor finding:
<one-paragraph summary>

Recommended architecture:
<one-paragraph summary>

Largest risks:
<top few>

Existing functionality reusable:
<brief summary>

New functionality required:
<brief summary>

Baseline tests:
<x passed / x failed>

Audit OpenRouter spend:
<$>

Product files modified:
NONE
(or explicitly explain unavoidable generated artefacts)

Audit workspace:
<absolute path>

Primary handoff file:
<absolute path to IMPLEMENTATION_CONTEXT.md>

Full audit:
<absolute path to MASTER_AUDIT.md>

Evidence/screenshots:
<absolute path>

Machine-readable manifests:
<absolute path>

Then STOP.

Do not begin implementation.

The next phase will be separately authorized.
```

===== 2026-09-15 21:42 | session 20260915_213920_f0f5d2 | Empirium OS forensic audit for AI Workforce =====
@file:`.hermes/attachments/Pasted content (4.4 KB)`

--- Attached Context ---

📄 @file:`.hermes/attachments/Pasted content (4.4 KB)` (1117 tokens)
```
a/work/empirium-os-ai-workforce-audit/RESUME_TASK.md → b/work/empirium-os-ai-workforce-audit/RESUME_TASK.md
@@ -0,0 +1,89 @@
+# Resume instructions for this audit session
+
+You are RESUMING an in-progress READ-ONLY forensic audit. A prior session already
+completed most of phases 1-27 (see files in this directory: README.md, FILE_MAP.md,
+CONDUCTOR_FORENSICS.md, HERMES_INTEGRATION.md, DATA_MODEL_AUDIT.md, UI_ARCHITECTURE.md,
+TEST_BASELINE.md, MEMORY_KNOWLEDGE_AUDIT.md, MODEL_PROVIDER_AUDIT.md,
+SECURITY_PERMISSIONS.md, DEPLOYMENT_RUNTIME.md, DONOR_CODE_RESEARCH.md, LICENSING.md,
+PERFORMANCE_BASELINE.md, PROMPT_LEARNING_AUDIT.md, VISUAL_ANIMATION_AUDIT.md,
+AGENT_VISUAL_MODEL.md, diagrams/, manifests/{apis,donor-code,relevant-files,routes,
+services,storage,tests}.json, logs/*.txt, test-results/*.txt).
+
+DO NOT redo completed phases. Read the existing files first to absorb what is already
+known, then continue.
+
+## Critical new finding you must investigate and document first
+
+The product repo `/home/ash/work/empirium-desktop` (git branch main) currently has
+SUBSTANTIAL UNCOMMITTED CHANGES that were NOT present at audit start (audit start was
+clean, an interim recheck showed only 2 files changed). As of now `git status --porcelain`
+shows:
+```
+ M package-lock.json
+ M package.json
+ M renderer/index.html
+ M renderer/js/store.js
+ M renderer/layout-shell.html
+ M renderer/router.js
+ M renderer/routes.js
+ M renderer/styles/empirium.css
+?? migrations/
+?? renderer/js/ai-workforce.js
+?? renderer/pages/ai-workforce/
+?? renderer/pages/github-repos/
+?? renderer/styles/ai-workforce.css
+?? scripts/github-repos-route-test.py
+?? test_ai_workforce_integrity.js
+```
+This looks like actual AI Workforce implementation work (matching the
+`ai-workforce-development` Hermes skill's procedure) landed in the product tree,
+apparently from a DIFFERENT session/process, not from this audit (this audit workspace
+is separate and read-only). Diff these files against git HEAD (read-only: `git diff`,
+`git diff --stat`), record exactly what exists now, whether it looks complete/functional,
+and whether it conflicts with or duplicates what this audit's PHASE 25/29 recommends.
+DO NOT stage, commit, revert, stash, or modify any of this. Just report it factually as
+a CURRENT-STATE fact in MASTER_AUDIT.md and IMPLEMENTATION_CONTEXT.md, and flag it
+prominently in OPEN_QUESTIONS.md as something Ash must decide on (keep this partial
+build? revert it? treat it as the starting point for the real implementation instead of
+building from scratch?).
+
+## Remaining deliverables to produce now
+
+1. `RISK_REGISTER.md` (Phase 27)
+2. `OPEN_QUESTIONS.md` — include the uncommitted-changes finding above as the top item
+3. `BUILD_RECOMMENDATION.md` (Phase 29) — evidence-based, challenge the brief's assumed
+   architecture if warranted, and explicitly address the existing uncommitted
+   ai-workforce.js/routes/store work as a factor
+4. `MASTER_AUDIT.md` — synthesis of all phases, cross-referencing the existing files
+   (don't duplicate their full content, summarize + link)
+5. `IMPLEMENTATION_CONTEXT.md` — THE most important deliverable. Must let another AI
+   write the full implementation mission with no re-audit. Follow the 32-point outline
+   from the original brief (this file's parent instructions are in the chat history /
+   original prompt — reconstruct the required sections from README.md and the other
+   completed docs plus your own direct source inspection). Use exact file paths,
+   functions, endpoints, data structures.
+6. Complete `manifests/components.json`, `manifests/models.json`, `manifests/risks.json`
+   (the brief's mandatory machine-readable outputs list) if not already present.
+7. Attempt the mandatory screenshot pack (Phase 14) if the app can be safely reached
+   (check the running ports documented in README.md: Caddy on 100.69.118.112:8082,
+   loopback :8082 python http.server, hermes-studio :3001). If genuinely unsafe/
+   impractical headlessly, document why in TEST_BASELINE.md or README.md instead of
+   fabricating images.
+8. Do a brief red-team self-review pass per the brief and fold results into
+   OPEN_QUESTIONS.md / RISK_REGISTER.md.
+9. Run through the brief's FINAL VALIDATION checklist and note pass/fail per item in
+   MASTER_AUDIT.md.
+
+## Safety (unchanged from original brief)
+
… omitted 11 diff line(s) across 1 additional file(s)/section(s)
```

===== 2026-09-15 21:50 | session 20260915_214646_63e072 | Plan EMPIRIUM OS workforce using FREELLMAPI =====
@file:`.hermes/attachments/Pasted content (99.7 KB)`

you are just making the plan, you are just going to ananlyse the paths we can take to achieve this goal, and come up with the best,specific complete and exhuastive plan of action. i want to use the FREELLMAPI mainly for sub agents doing a lot of the work, with a more capable model doing qa and testing to make sure it meets astros now going to be set success criteria and defintions of done. . if needed there is $2 of open router you can use only any model you see fit

--- Attached Context ---

📄 @file:`.hermes/attachments/Pasted content (99.7 KB)` (23770 tokens)
```
# =====================================================================
# EMPIRIUM OS — AI WORKFORCE
# COMPLETE MASTER PROJECT HANDOVER FOR CHATGPT ASTRA
# =====================================================================

You are taking over a substantial ongoing project.

This document is the authoritative conversational handover for the project as
currently designed.

DO NOT restart the design from first principles.

DO NOT reduce this project to "a multi-agent dashboard".

DO NOT replace established architecture casually.

DO NOT make the user re-explain decisions contained in this handover.

When new evidence conflicts with this handover, investigate and update the
architecture deliberately.

Otherwise preserve existing decisions.

The user is Ash.

The user wants high autonomy and minimal project-management burden.

The user strongly prefers:

- decisive recommendations;
- concrete architecture;
- implementation-ready prompts;
- minimal back-and-forth;
- autonomous execution;
- real testing;
- persistent state;
- recovery from failures;
- strong visual polish;
- cost discipline;
- evidence-backed completion;
- and systems that actually work rather than merely looking complete.

The user is particularly frustrated by autonomous agents that run for
20–30 minutes, produce a partial implementation, and then announce that
everything is "done".

Long-running autonomous implementation is desirable.

If a genuine job requires four or five hours, that is acceptable.

A 5-hour genuinely completed implementation is preferable to a 25-minute
false completion.

=====================================================================
PART I — THE PRODUCT VISION
=====================================================================

The product is:

EMPIRIUM OS

Empirium OS is Ash's personal/business operating system.

There is already an existing Empirium OS application.

It is not being replaced.

Hermes has also been integrated into the ecosystem.

The long-term goal is to evolve Empirium OS + Hermes into a persistent,
visual AI organization.

The intended product abstraction is NOT:

"some AI chats"

or

"a screen showing agents".

It is:

A PERSISTENT AI COMPANY / AI WORKFORCE.

The user should eventually be able to see an organization containing
departments populated by persistent specialist AI employees.

Those employees execute real work across Ash's personal software, business,
research, operations, marketing, finance, administration and other areas.

The high-level domain model is:

ORGANIZATION
    ↓
DEPARTMENT
    ↓
PERSISTENT DEPARTMENT AGENT / AI EMPLOYEE
    ↓
PROJECT
    ↓
TASK
    ↓
RUN
    ↓
TEMPORARY EXECUTION RESOURCE
    ↓
ARTIFACTS / HANDOFF
    ↓
QA
    ↓
KNOWLEDGE
    ↓
LEARNING
    ↓
IMPROVEMENT / VERSION HISTORY


The AI organization should be:

persistent;

visible;

auditable;

measurable;

cost-controlled;

permission-controlled;

capable of learning;

capable of using different underlying models/runtimes;

and capable of carrying substantial work through to verified completion.


=====================================================================
PART II — THE MOST IMPORTANT ARCHITECTURAL DISTINCTION
=====================================================================

Do not confuse persistent AI employees with temporary agent sessions.

This is one of the most important design rules in the entire project.


A DEPARTMENT
is persistent organization.


A DEPARTMENT AGENT
is a persistent specialist employee.


A PROJECT
is a durable body of work.


A TASK
is a durable actionable work unit.


A RUN
is one durable record of an execution attempt.


A Hermes session / OpenHands conversation / Claude Code process /
Codex process / Conductor worker / shell process / temporary agent
is merely a TEMPORARY EXECUTION RESOURCE associated with a Run.


Example:

Persistent employee:

Implementation Engineer

Task:

Implement Workforce Department Overview

Run:

Run #238

Temporary execution:

Claude Code session `xyz`

or:

OpenHands conversation `abc`

or:

Hermes worker session `foo`


When that execution terminates:

THE IMPLEMENTATION ENGINEER STILL EXISTS.

Its state may return to IDLE.

Therefore a permanent employee must NEVER be identified by:

Hermes sessionKey;

Conductor worker label;

OpenHands conversation ID;

temporary CLI process;

model provider request ID;

avatar index;

temporary execution ID.


Persistent identity belongs to Empirium.

Runtime identity is an adapter binding beneath that.


=====================================================================
PART III — CONTROL PLANE ARCHITECTURE
=====================================================================

The desired architecture is approximately:


                         EMPIRIUM OS
                              │
                              ▼
                    AI WORKFORCE CONTROL PLANE
                              │
             ┌────────────────┼────────────────┐
             │                │                │
        ORGANIZATION      WORK DOMAIN      GOVERNANCE
             │                │                │
        Departments         Projects        Budgets
        Employees           Tasks           Approvals
        Offices             Runs            Permissions
                                             QA
                                             Security
                                             Learning
                              │
                              ▼
                    EXECUTION BROKER / ADAPTERS
                              │
      ┌──────────────┬────────┼────────┬──────────────┐
      │              │        │        │              │
   Hermes        Conductor OpenHands Claude Code   Codex
      │              │        │        │              │
      └──────────────┴────────┴────────┴──────────────┘
                              │
                     temporary execution
                              │
                              ▼
                         RUN EVENTS
                              │
                              ▼
                         POSTGRESQL
                              │
             durable Workforce source of truth


Empirium remains the control plane.

Hermes remains important.

OpenHands is not replacing Hermes.

Claude Code does not become the employee.

Codex does not become the employee.

Conductor does not become the database.

Every runtime is subordinate to Empirium's persistent Workforce domain.


=====================================================================
PART IV — HERMES
=====================================================================

Hermes remains central to the vision.

Hermes has already been explored as:

- personal assistant;
- general-purpose agent;
- tool/MCP orchestrator;
- background worker;
- multi-agent system;
- VPS automation layer;
- assistant integrated with Empirium OS.

Hermes should NOT be replaced by OpenHands or another autonomous coding
product.

Hermes can eventually serve several functions:

1. general-purpose AI employee runtime;

2. organization-level orchestration;

3. personal assistant layer;

4. tool / MCP execution;

5. cross-department workflows;

6. general research / operations execution;

7. dispatching specialist execution when needed.


However:

Do not force Hermes itself to be the best coder, best researcher,
best QA model, best finance system and best everything else.

The Workforce should route specialist work to specialist execution when useful.


=====================================================================
PART V — EXISTING HERMES STUDIO / CONDUCTOR CONTEXT
=====================================================================

Hermes Studio has already been embedded/integrated into Empirium OS because
using it externally was awkward.

Existing exploration covered:

Chats

Agents

Crews

Conductor

Terminal

and other Hermes Studio features.


Important interpretation:

Conductor is useful as a TEMPORARY mission orchestration/execution mechanism.

Conductor is NOT the permanent Workforce domain model.

Do not model:

Department = Conductor mission

or:

Employee = Conductor worker.


Conductor missions may eventually be used as an execution adapter below Run.

Example:

Empirium Project
   ↓
Task
   ↓
Run
   ↓
ConductorAdapter
   ↓
temporary Conductor mission
   ↓
temporary Hermes workers


The durable Project/Task/Run stays in Empirium.


Existing forensic work showed Conductor mission state was heavily tied to
browser/local transient state rather than being an appropriate authoritative
organizational database.

Therefore:

DO NOT build Workforce persistence on Conductor localStorage.


=====================================================================
PART VI — OPENHANDS STRATEGY
=====================================================================

OpenHands is now an important additional donor/runtime candidate.

Repositories discussed:

https://github.com/OpenHands/OpenHands

https://github.com/OpenHands/software-agent-sdk

https://github.com/OpenHands/automation


OpenHands should be treated as:

1. architectural donor;

2. coding-agent design reference;

3. source of tested implementation patterns;

4. potential isolated coding execution backend;

5. source of useful automation patterns;

6. source of usage / run / conversation abstractions.


OpenHands should NOT:

replace Hermes;

replace Empirium OS;

become the Workforce source of truth;

be imported wholesale as a second product;

define persistent employees;

bypass Workforce permissions;

bypass Workforce budgets.


The conceptual execution abstraction should be:

ExecutionAdapter

    HermesAdapter

    ConductorAdapter

    OpenHandsAdapter

    ClaudeCodeAdapter

    CodexAdapter


Potential common contract:

startRun()

cancelRun()

pauseRun()

resumeRun() where supported

getStatus()

streamEvents()

getUsage()

getArtifacts()

getWorkspace()

getChildRuns()

getLogs()

getExternalExecutionReference()


Each adapter normalizes runtime-specific behavior into Empirium Run events.


=====================================================================
PART VII — OPENHANDS FEATURES/PATTERNS TO STUDY AND ADAPT
=====================================================================

--------------------------------------------------
A. CHILD AGENTS + GIT WORKTREES
--------------------------------------------------

OpenHands supports spawning independent child conversations/tasks.

Important pattern:

child receives a self-contained brief;

child does not need the entire parent transcript;

child can execute independently;

parallel local children can operate in isolated Git worktrees;

worktree isolation reduces file conflicts;

parent-child relationship is durable/queryable;

delegation is explicit.


This maps exceptionally well to Workforce.


Example:

Implementation Engineer

        │
        ├── child Run
        │       frontend
        │       worktree A
        │
        ├── child Run
        │       backend
        │       worktree B
        │
        └── child Run
                DB migration
                worktree C


A child worker brief should contain at minimum:

OBJECTIVE

ACCEPTANCE CRITERIA

RELEVANT FILES / COMPONENTS

CONSTRAINTS

CURRENT DECISIONS

EXACT NUMBERS / PARAMETERS

TEST REQUIREMENTS

KNOWN RISKS

EXPECTED DELIVERABLE

EXPECTED HANDOFF FORMAT


This directly supports context optimization.

The child should not need 80,000 tokens of parent transcript.


--------------------------------------------------
B. PLANNING AGENT / BUILD AGENT SEPARATION
--------------------------------------------------

OpenHands contains the concept of a Planning Agent whose job is to create a
plan, not quietly start implementing.

This aligns with the intended Software department.

Research / Architecture Engineer
          ↓
Implementation Plan
          ↓
Implementation Engineer


A durable Personal Software implementation plan should roughly contain:

1. OBJECTIVE

2. USER REQUIREMENTS

3. ACCEPTANCE CRITERIA

4. CURRENT SYSTEM CONTEXT

5. RESEARCH / EVIDENCE

6. ARCHITECTURAL DECISION

7. ALTERNATIVES CONSIDERED

8. IMPLEMENTATION STEPS

9. FILES / COMPONENTS AFFECTED

10. DATA / MIGRATION EFFECTS

11. SECURITY EFFECTS

12. RISKS

13. ROLLBACK STRATEGY

14. TEST PLAN

15. DEFINITION OF DONE


--------------------------------------------------
C. OPENHANDS SOFTWARE AGENT SDK / AGENT SERVER
--------------------------------------------------

Investigate the Software Agent SDK and Agent Server as an optional execution
backend for substantial coding tasks.

Potential value includes:

terminal execution;

file editing;

task tracking;

agent conversations;

workspace control;

runtime events;

remote REST APIs;

WebSocket/event transport;

isolated workspaces;

ephemeral execution;

multi-agent software workflows.


Do not automatically adopt all of it.

Assess compatibility with the existing VPS, security model and Workforce
capability broker.


--------------------------------------------------
D. BACKEND NORMALIZATION
--------------------------------------------------

Agent Canvas already handles different backends.

Adopt the design idea, not necessarily the entire implementation.

Normalize at least:

external execution ID;

runtime type;

agent type;

model;

provider;

workspace;

execution state;

parent run;

child runs;

start time;

end time;

token usage;

cost usage;

tool events;

artifacts;

errors.


--------------------------------------------------
E. OPENHANDS AUTOMATION
--------------------------------------------------

Inspect OpenHands Automation for patterns covering:

cron;

webhooks;

automation definitions;

run scheduling;

dispatch;

run history;

failure states;

retries;

sandbox lifecycle.


Reuse good patterns inside Empirium where appropriate.

Do not casually introduce another database/source of truth.


--------------------------------------------------
F. USAGE / COST AGGREGATION
--------------------------------------------------

OpenHands contains logic for aggregating usage such as:

prompt tokens;

completion tokens;

cache read;

cache write;

context window;

conversation cost.


Adapt useful normalization concepts.

However:

THE EMPIRIUM MODEL RUN BROKER remains authoritative for spending limits.


--------------------------------------------------
G. TESTS
--------------------------------------------------

When borrowing behavior from OpenHands:

inspect upstream tests.

Understand invariants.

Adapt the relevant tests.

Do not copy source blindly without its safety assumptions.


--------------------------------------------------
H. LICENSING
--------------------------------------------------

Current investigation found the principal OpenHands repositories discussed
use MIT licensing.

Nevertheless:

verify exact current repository;

commit;

file;

license;

copyright obligations

before adopting code.


Maintain donor provenance.


=====================================================================
PART VIII — DEPARTMENT MODEL
=====================================================================

Departments are persistent configurable organizational units.

Different departments can have:

different numbers of employees;

different employee roles;

different models;

different budgets;

different tools;

different MCPs;

different knowledge scopes;

different QA rules;

different office layouts;

different office stations;

different visual themes;

different schedules;

different security rules.


Departments must be DATA-DRIVEN.

Adding a new department should not require adding custom application code for
every department.


The FIRST fully specified department is:

PERSONAL SOFTWARE


Other future department areas have been discussed conceptually through Hermes
use cases, including things such as:

- business analysis / strategy;
- research;
- sales / lead generation;
- lead enrichment;
- marketing;
- LinkedIn/content;
- newsletter;
- SEO / AI-SEO;
- accounting / finance support;
- personal goals/accountability;
- Obsidian / knowledge management;
- infrastructure / operations;
- incident diagnostics;
- model benchmarking;
- appointment/demo preparation.

However:

DO NOT hard-code these as final departments unless Ash later confirms them.

The generic department system should make adding them easy.


=====================================================================
PART IX — PERSONAL SOFTWARE DEPARTMENT
=====================================================================

Name:

Personal Software


Mission:

"Build, maintain, test, improve and learn from Ash's personal software."


Seed with five persistent specialist employees.


=====================================================================
EMPLOYEE 1 — SOFTWARE DIRECTOR
=====================================================================

ROLE

Department leader and work allocator.

RESPONSIBILITIES

Receive incoming software requests.

Understand request intent.

Classify:

complexity;

risk;

scope;

affected systems;

urgency;

quality requirement.

Create Project where necessary.

Create Tasks.

Create Task dependency DAG.

Select specialist employees.

Choose execution adapter.

Choose model class.

Apply budget.

Monitor project.

Handle blockers.

Request approvals.

Require QA.

Determine whether release criteria have been satisfied.

Close Project only after Definition of Done.


PERSONALITY

calm;

decisive;

organized;

transparent;

cost-disciplined;

skeptical of unnecessary complexity;

does not overengineer.


MODEL STRATEGY

Trivial classification:
cheap/free structured model.

Meaningful architecture/planning:
strong subscription reasoning.

Do not waste premium inference on deterministic scheduling logic.


CAPABILITIES

May inspect software/project state.

May create Projects/Tasks/Runs.

May allocate employees.

Should not automatically possess unrestricted arbitrary shell capability.


=====================================================================
EMPLOYEE 2 — RESEARCH / ARCHITECTURE ENGINEER
=====================================================================

ROLE

Technical investigator and architectural planner.


RESPONSIBILITIES

Inspect repositories.

Understand architecture.

Read existing documentation.

Identify relevant modules/files.

Research donor code.

Research APIs/libraries if required.

Produce architecture decisions.

Produce implementation plans.

Identify risks.

Identify migrations.

Identify security implications.

Produce evidence-backed handoff.


PERSONALITY

curious;

skeptical;

source-first;

evidence-driven;

precise.


DEFAULT ACCESS

Read-only where possible.

No arbitrary modification unless explicitly switched into another task role.


MODEL ROUTING

Bulk research:
free/research model where adequate.

High-value architecture:
strong subscription reasoning.


=====================================================================
EMPLOYEE 3 — IMPLEMENTATION ENGINEER
=====================================================================

ROLE

Primary coding/build employee.


RESPONSIBILITIES

Implement approved work.

Edit source.

Debug.

Write tests.

Run tests.

Create worktrees.

Use temporary coding execution resources.

Perform browser validation where authorized.

Produce exact implementation handoff.


PERSONALITY

methodical;

pragmatic;

precise;

economical;

minimal-complexity biased.


PONYTAIL

ON by default for this employee.

Meaning:

prefer YAGNI;

native APIs first;

existing dependencies first;

standard library first;

minimal abstraction;

no needless infrastructure;

no speculative frameworks.


EXECUTION OPTIONS

Hermes;

Claude Code;

Codex;

OpenHands;

future coding backends.


IMPORTANT

The persistent Implementation Engineer is NOT the Claude/OpenHands/Hermes
session.


SECURITY

Assigned repository/worktree only where possible.

Cannot silently deploy production.

Cannot bypass approval.


=====================================================================
EMPLOYEE 4 — QA / REVIEW ENGINEER
=====================================================================

ROLE

Independent quality authority.


RESPONSIBILITIES

Review requirements.

Review implementation.

Inspect diff.

Run unit tests.

Run integration tests.

Run E2E tests.

Perform visual QA.

Check regressions.

Check security.

Check accessibility.

Check performance.

Verify persistence/restart behavior.

Generate QA evidence.


PERSONALITY

skeptical;

adversarial;

systematic;

evidence-driven.


INDEPENDENCE

Must not approve its own implementation work.

Implementer and reviewer should be logically independent.


MODEL ROUTING

Free code review model where sufficient.

Escalate to strong subscription reviewer for significant/high-risk work.


=====================================================================
EMPLOYEE 5 — LEARNING ANALYST
=====================================================================

ROLE

Institutional-learning specialist.


RESPONSIBILITIES

Review completed Projects.

Review failures.

Review QA issues.

Review repeated user corrections.

Identify repeated success patterns.

Identify repeated failure patterns.

Produce lessons.

Propose:

prompt improvements;

playbook improvements;

model-routing improvements;

knowledge improvements;

workflow improvements;

agent technique changes.


PERSONALITY

conservative;

analytical;

evidence-based;

not trigger-happy.


IMPORTANT

Cannot silently modify critical production prompts/policies.

Produces PROPOSALS first.


=====================================================================
PART X — DEFAULT PERSONAL SOFTWARE WORKFLOW
=====================================================================

Example:

Ash says:

"Add feature X to Empirium OS."


The desired flow:


ASSIGN WORK
    ↓
SOFTWARE DIRECTOR
    ↓
UNDERSTAND REQUEST
    ↓
CREATE PROJECT
    ↓
CREATE TASK DAG
    ↓
ASSIGN RESEARCH / ARCHITECTURE
    ↓
RESEARCH SYSTEM
    ↓
PRODUCE IMPLEMENTATION PLAN
    ↓
DIRECTOR REVIEWS / ROUTES
    ↓
IMPLEMENTATION ENGINEER
    ↓
SELECT EXECUTION BACKEND
    ↓
CREATE ISOLATED RUN / WORKTREE WHERE APPROPRIATE
    ↓
IMPLEMENT
    ↓
RUN TESTS
    ↓
IF FAIL
    diagnose
    modify
    rerun
    repeat
    ↓
HANDOFF
    ↓
QA ENGINEER
    ↓
INDEPENDENT TESTING
    ↓
FAIL?
    ↓
specific fix Task
    ↓
Implementation Engineer
    ↓
QA again
    ↓
PASS
    ↓
PROJECT COMPLETION CHECK
    ↓
LEARNING ANALYST
    ↓
LESSONS / IMPROVEMENT PROPOSALS
    ↓
KNOWLEDGE UPDATED IF APPROVED
    ↓
HISTORY + COST + QA RETAINED


No project should become COMPLETED because:

the coder said "done";

files exist;

one screenshot exists;

the first happy path worked.


=====================================================================
PART XI — ASSIGN WORK
=====================================================================

There should be a clear intake interface.

Do not trap work requests exclusively inside conversational transcripts.

Fields should include approximately:

natural-language request;

priority;

optional deadline;

optional budget override;

preferred employee;

quality level;

optional target software/repository;

optional context attachments.


The Director receives the intake.

It becomes durable organizational data.


=====================================================================
PART XII — ORGANIZATION OVERVIEW UI
=====================================================================

Primary route concept:

#/workforce


IMPORTANT VISUAL DECISION:

DO NOT add a permanent Workforce-specific left navigation rail.

Use Empirium OS's existing shell.

Within Workforce use:

top navigation;

contextual navigation;

breadcrumbs;

tabs.


The user previously preferred the FIRST boxed department grid/card mockup,
rather than a giant flashy central hub.

Organization Overview should therefore emphasize efficient scalable department
cards.


HEADER

AI Workforce

global health

search

filters

sort

Pause All

Approvals indicator

New Department


GLOBAL METRICS

department count

total employees

working

idle

blocked

active projects

active tasks

paid spend today

paid spend this month

free/subscription usage

QA pass rate

pending approvals

learning proposals


DEPARTMENT CARD

department name

mission

status

small office visualization

actual employee count

employees currently active

active projects

active tasks

primary current activity

blocked count

today's paid spend

QA health

pending improvement count


CARD STATES

loading

empty

healthy

working

blocked

paused

degraded

offline


SCALABILITY TESTS

1 department

6 departments

12 departments

24 departments

50 departments


Mini offices should be cheap.

Use cached/static SVG/DOM where possible.

Do NOT run full animation/event loops for every offscreen card.

Use viewport awareness / IntersectionObserver where useful.


=====================================================================
PART XIII — DEPARTMENT PAGE
=====================================================================

Route:

#/workforce/department/<slug>


HEADER

breadcrumbs

department name

mission

status

Pause Department

Assign Work

New Project

Settings


SUMMARY STRIP

employee count

currently working

projects

tasks

QA health

spend

knowledge

learning


TABS

OVERVIEW

PROJECTS

TASKS

AGENTS

QA

KNOWLEDGE

LEARNING

HISTORY

MODELS & COST

SETTINGS


OVERVIEW

large live office;

Current Activity;

Department Status;

Active Projects;

Upcoming Work;

Recently Completed;

QA Health;

Knowledge Summary;

Learning & Improvements;

Model/Cost Summary;

Approvals Waiting.


Every panel should map to actual durable data.

No fabricated activity.


=====================================================================
PART XIV — CREATE DEPARTMENT WIZARD
=====================================================================

A department should be creatable without code changes.

Possible flow:


1. IDENTITY

name

slug

mission

description

theme


2. TEAM

employees

roles

employee count


3. OPERATING MODEL

how work is assigned

Director behavior

quality expectation

approval rules


4. QA

required QA types

independence policy


5. BUDGET

department spending rules


6. KNOWLEDGE

available knowledge scopes


7. MODELS

routing policies


8. TOOLS / MCP

allowed tools

allowed integrations


9. OFFICE

layout

stations

visual theme


10. REVIEW


11. CREATE


=====================================================================
PART XV — AGENT / EMPLOYEE DETAIL PAGE
=====================================================================

Persistent employee configuration must NOT be one enormous system prompt.

Keep these concepts distinct:

ROLE

PERSONALITY

TECHNIQUE / WORKING STYLE

SKILLS

PROMPT

PLAYBOOK

MODEL POLICY

TOOLS

MCP BINDINGS

MEMORY SCOPES

KNOWLEDGE SCOPES

CAPABILITY POLICY

CONTEXT POLICY

VISUAL PROFILE


Agent detail should support sections such as:


OVERVIEW

name

department

role

current status

current assignment


ROLE

mission

responsibilities

boundaries


PERSONALITY

tone

behavioural traits

communication style


TECHNIQUE

task methodology

decision process

working patterns


SKILLS

explicit capability modules


PROMPTS

current version

history

diff

rollback


MODELS

policy

preferred model class

actual model performance


TOOLS

allowed

denied

approval required


MCP

allowed MCP servers/tools


MEMORY / KNOWLEDGE

scopes

recent retrievals

denied retrievals


CAPABILITIES

files

terminal

Git

browser

deploy

external communication

etc.


VISUAL EDITOR

robot body

colors

face

equipment

desk

movement


CURRENT RUN

task

timeline

runtime

model

why model selected

tools

tests

tokens

cost


PERFORMANCE

success rate

first-pass QA

retry rate

corrections

cost

latency

token savings


LEARNING

lessons

proposals

version changes


=====================================================================
PART XVI — PROJECTS
=====================================================================

Project state machine includes:

DRAFT

PLANNED

ACTIVE

WAITING_APPROVAL

BLOCKED

PAUSED

IN_REVIEW

COMPLETED

CANCELLED

ARCHIVED


Project fields include:

objective;

description;

requirements;

acceptance criteria;

owner;

department;

priority;

status;

risk;

quality level;

budget;

spent;

reserved;

deadline.


Project Detail views:

Overview

Task Tree

Kanban

Runs

QA

Knowledge

Decisions

Artifacts

Activity

Cost


=====================================================================
PART XVII — TASKS
=====================================================================

Task states:

BACKLOG

READY

QUEUED

IN_PROGRESS

WAITING_DEPENDENCY

WAITING_APPROVAL

BLOCKED

REVIEW

DONE

FAILED

CANCELLED


UI Kanban can group waiting-related states visually under WAITING if useful.


Task card:

title;

project;

assignee;

priority;

complexity;

QA state;

dependencies;

due date;

current Run;

cost.


Task detail:

description;

acceptance criteria;

dependencies;

assignee;

state;

run history;

current Run;

artifacts;

QA;

knowledge;

activity;

cost;

notes.


Actions:

assign;

reassign;

start;

pause;

cancel;

retry;

approve;

request QA.


Task dependency cycles must be prevented.


=====================================================================
PART XVIII — RUNS
=====================================================================

Run = one durable execution attempt.

Run state machine:

CREATED

QUEUED

STARTING

RUNNING

WAITING

BLOCKED

CANCELLING

CANCELLED

FAILED

SUCCEEDED

TIMED_OUT


Run Detail:

Run ID

employee

Task

attempt number

execution adapter

external execution ID

model

provider

why selected

prompt version

playbook version

capability grant

memory / knowledge retrieved

Headroom state

Ponytail state

start

duration

tokens

cost

events

tool calls

artifacts

errors

handoff

QA relationship


AT RUN START:

Persist an immutable reproducibility snapshot.

The snapshot should include:

employee ID;

role version;

personality version;

working style version;

prompt version;

playbook version;

Task;

acceptance criteria;

model policy;

selected model;

provider;

capability grant;

budget snapshot;

knowledge scopes;

retrieval references;

Headroom/context policy;

Ponytail policy;

repository/version/worktree information;

relevant environment/version information.


This allows later answering:

"Why did this employee do this?"

"Which prompt did it have?"

"Which model?"

"Which permissions?"

"What knowledge?"

"What cost policy?"


=====================================================================
PART XIX — CHILD RUNS / RUN TREE
=====================================================================

Borrow the OpenHands-style parent/child execution idea.

A Run can spawn child Runs.

Example:


Run: Implement Workforce

├── Research child
├── Backend child
├── Frontend child
│      ├── Department Overview
│      └── Agent Detail
├── Database child
└── QA child


Store explicit parent_run_id.

Do not infer hierarchy from worker labels.


UI should show a Run Tree.

Each node can expose:

status;

employee;

execution adapter;

model;

cost;

duration;

artifacts;

errors.


=====================================================================
PART XX — QA
=====================================================================

QA is first-class durable data.

State machine:

PENDING

RUNNING

CHANGES_REQUESTED

APPROVED

REJECTED

WAIVED


If a Task requires QA:

it cannot become DONE without APPROVED

or an explicit authorized WAIVER.


QA record includes:

Task

Run

Implementer

Reviewer

Reviewer model

requirements checked

tests run

integration checks

E2E

visual QA

regression QA

security

accessibility

performance

issues

evidence

fix requests

confidence

result


Department QA dashboard should show:

overall QA health;

pass rate;

first-pass rate;

open issues;

regressions;

recent reviews.


=====================================================================
PART XXI — KNOWLEDGE + OBSIDIAN
=====================================================================

PostgreSQL is operational authority.

Obsidian is intended as human-readable institutional knowledge.

Existing Obsidian vault context from audit included top-level areas such as:

Course Knowledge

Courses

Daily Notes

Empirium

Empirium OS

Personal

Quick Research

Weekly Review

Frameworks

UI UX Knowledge

Templates

Archive


Existing patterns include:

Module Notes;

MOCs;

Playbooks;

Source Registers.


Use existing filesystem/frontmatter/tag/path conventions where useful.

Do not introduce paid vector infrastructure automatically.

Prefer:

paths;

frontmatter;

tags;

grep/ripgrep;

structured indexes;

deterministic retrieval.


Knowledge scopes:

GLOBAL

DEPARTMENT

PROJECT

AGENT


Potential frontmatter:

scope

department

project

agent_role

knowledge_type

status

sensitivity

approved_at


PRIVACY BOUNDARY

Software employees must not automatically retrieve unrelated:

Personal;

Finance;

sensitive family notes;

credentials;

etc.


A Run should record:

knowledge retrieved;

reason;

relevance;

scope;

token impact;

denied references.


=====================================================================
PART XXII — LEARNING SYSTEM
=====================================================================

Learning should be evidence-driven.

Signals include:

QA pass;

QA fail;

user correction;

user manual edit;

user rejection;

rerun;

reassignment;

model switch;

prompt switch;

retry;

escalation;

rollback;

regression;

cost;

latency;

successful strategy.


Lifecycle:

EXPERIENCE
    ↓
LESSON
    ↓
EVIDENCE
    ↓
PROPOSAL
    ↓
EVALUATION
    ↓
APPROVAL
    ↓
IMMUTABLE VERSION
    ↓
ACTIVATION
    ↓
MONITORING
    ↓
ROLLBACK if necessary


Learning proposal state:

DRAFT

EVALUATING

AWAITING_APPROVAL

APPROVED

REJECTED

ACTIVATED

ROLLED_BACK


IMPORTANT:

Do not silently self-modify critical prompts.

Do not silently modify security rules.

Do not silently change spending policy.

Do not generalize one correction into a universal rule without evidence.


Learning UI:

Current

History

Compare

Rollback


=====================================================================
PART XXIII — APPROVAL INBOX
=====================================================================

Approvals are durable entities.

Examples:

budget increase;

production deployment;

sensitive capability;

external communication;

critical prompt activation;

playbook activation;

high-risk operation.


Approval states:

REQUESTED

APPROVED

REJECTED

EXPIRED

CANCELLED


Approval UI:

requester

employee

Task

reason

risk

expected cost

requested permission

expiration

evidence

Approve

Reject


Waiting Task/employee links to the Approval.


=====================================================================
PART XXIV — MODEL STRATEGY
=====================================================================

Do NOT rely blindly on historically configured models.

Before major implementation perform a small current capability preflight.

Verify what is actually usable NOW.

Potential providers/routes previously involved include:

OpenRouter;

Claude Code subscription;

ChatGPT/OpenAI subscription paths where legitimately available;

free model routes;

local models;

provider APIs.


Do not circumvent provider subscription restrictions.


Model aliases concept:

FREE_FAST

FREE_RESEARCH

FREE_STRUCTURED

FREE_CODE_REVIEW

FREE_SUMMARIZER

FREE_UI

SUBSCRIPTION_CODE

SUBSCRIPTION_REASONING

SUBSCRIPTION_REVIEW

EXCEPTIONAL_REASONING

PAID_ESCALATION

IMAGE_GENERATION


Freeze actual current routes into:

BUILD_MODELS.json


Preferred routing order:

1. deterministic / no LLM

2. cache

3. free model

4. subscription-backed model

5. low-cost paid model

6. exceptional premium model


Use premium intelligence for high-value reasoning.

Do not waste strong models on trivial formatting.


=====================================================================
PART XXV — COST CONTROL
=====================================================================

Previous autonomous Workforce implementation target:

approximately $5 deliberate paid external inference/assets maximum.

This is a hard build budget concept.

Goal:

spend less if possible.


For future Personal Software Projects:

default deliberate PAID MODEL budget around:

$1.50 per substantive Project

unless Ash explicitly changes it.


Free/subscription processing is not necessarily prevented when cash budget
is exhausted.


A paid model Run should use reservation accounting:

Run requested
    ↓
resolve model policy
    ↓
select route
    ↓
estimate maximum paid cost
    ↓
lock budget
    ↓
reserve
    ↓
dispatch
    ↓
usage recorded
    ↓
reconcile actual cost
    ↓
release unused reservation


Paid execution denied when project cap exceeded unless approval exists.


Do not use UI-side budget controls as authority.

Budget enforcement must be server-side.


=====================================================================
PART XXVI — MODELS & COST PAGE
=====================================================================

Show:

paid spend today

paid spend week

paid spend month


Compute mix:

deterministic

local

free

subscription

paid


Token metrics:

raw input

optimized input

tokens saved

compression %

completion tokens

cache tokens


Model performance:

task type

complexity

model

provider

QA outcome

retry rate

correction rate

latency

tokens

cost


Per employee economics.

Per Project economics.

Reserved vs spent vs remaining.


=====================================================================
PART XXVII — HEADROOM
=====================================================================

Headroom is being explored as a context optimization layer.

It is NOT:

employee personality;

primary long-term memory;

organizational DB.


Conceptually:

raw task/context
     ↓
ContextOptimizer
     ↓
relevant/compressed context
     ↓
model


Goal:

reduce unnecessary tokens from:

tool output;

logs;

API responses;

DB dumps;

file content;

RAG results;

history;

handoffs.


Important high-risk information must be protected from lossy compression.

Protect exact:

errors;

failing tests;

financial numbers;

budgets;

citations;

security details;

compliance text;

legal text;

customer data;

migration commands;

Definition of Done;

requirements;

approvals;

contractual content.


Full raw source remains retrievable.


Metrics:

raw tokens;

optimized tokens;

tokens saved;

compression %;

output tokens;

provider;

model;

estimated cost;

latency;

retrieval events.


Benchmark:

Hermes baseline

Headroom

Ponytail

Headroom + Ponytail


If existing Headroom projects are unsuitable:

implement a generic interface:

ContextOptimizer

    PASS_THROUGH

    HEADROOM


Do not blindly install `hermes-headroom` or any community tool without checking:

repository;

license;

security;

configuration;

provider routing;

failure handling;

context retrieval behavior;

compatibility.


=====================================================================
PART XXVIII — STRUCTURED HANDOF
...[TRUNCATED 34960 chars]...
ly asked why his large prompts often finish in around 20–30 minutes
while other people's "one-shot" autonomous prompts appear to run for 4–5 hours
and actually complete the task.

Important interpretation:

Prompt detail alone is not enough.

Long autonomous work requires:

clear execution loop;

persistent checkpoints;

tool use;

subagent orchestration;

strong Definition of Done;

failure recovery;

verification;

permission to continue for hours;

instruction not to confuse generated output with completion.


When helping Ash create future autonomous prompts, include explicit wording such
as:

"Do not report completion merely because an implementation attempt has
finished."

"Do not stop after producing a plan."

"Do not stop after the first coding pass."

"Continue autonomously until every required Definition of Done item is
verified."

"If testing fails, diagnose, repair and retest."

"If QA fails, return to implementation and rerun QA."

"If context becomes too large, checkpoint state and continue in a fresh worker."

"If a subagent fails, salvage its work and reassign."

"If a provider fails, use an approved fallback and continue."

"Long execution time is acceptable."

"Do not optimize for a quick final answer."

"Optimize for actual completion."


=====================================================================
PART LXXII — EXISTING MODEL / PROVIDER HISTORY
=====================================================================

Historical context only — re-check current status before use.

OpenRouter has been used.

There were previous issues with:

free model 429 errors;

free models returning 400s;

provider charging despite expectations.


A previous configured free route included an NVIDIA Nemotron free model.

At one audit point an OpenRouter key had hit a total limit / authorization
problem.

This may no longer be true.


Claude Code was installed and subscription-backed in the VPS ecosystem.

At one point version 2.1.x was observed.

Verify current version.


Codex CLI was not available during one older audit.

Do not assume that remains true.


Ollama was available on loopback historically, but local models had not been
useful/strong enough.

Ash previously found:

Qwen 3.5 4B on laptop extremely slow;

Qwen 3.5 9B on VPS not working well.


Do not spend significant engineering effort forcing weak CPU local inference if
subscription/free hosted models are significantly better.


=====================================================================
PART LXXIII — USER'S PERSONAL SOFTWARE / HERMES GOALS
=====================================================================

Hermes has already been considered for:

incident diagnostics;

model/provider benchmarking;

Empirium OS improvements;

lead generation;

lead enrichment;

appointment/demo prep;

personal accountability;

goals/habits;

social media;

LinkedIn;

newsletter;

SEO;

AI-SEO;

business data analysis;

accounting support;

grants/loans;

Obsidian management;

weekly research.


These functions help explain why the generic Workforce architecture must support
many departments and very different specialist employee types.

Do not assume every employee should have coding permissions.


=====================================================================
PART LXXIV — PERSONAL SOFTWARE AS FIRST IMPLEMENTATION, NOT FINAL SCOPE
=====================================================================

The first implemented department is Personal Software because:

it can build/improve Empirium itself;

it provides an excellent test of:

Projects;

Tasks;

Runs;

QA;

knowledge;

learning;

cost;

execution adapters;

Git;

browser testing.


But architecture must remain generic.

Avoid tables, APIs and UI code named in ways that permanently assume all
employees are software engineers.


=====================================================================
PART LXXV — DONOR CODE PHILOSOPHY
=====================================================================

The user has explored multiple repositories and likes the idea of extracting
strong components rather than adopting complete products unnecessarily.

Good approach:

AUDIT DONOR

↓

IDENTIFY SPECIFIC CAPABILITY

↓

VERIFY LICENSE

↓

UNDERSTAND TESTS

↓

EXTRACT DESIGN PATTERN OR SMALL COMPONENT

↓

ADAPT TO EMPIRIUM DOMAIN

↓

TEST

↓

RECORD PROVENANCE


Bad approach:

clone five agent products;

run all of them;

create overlapping control planes;

create duplicate databases;

create multiple competing employee models.


Empirium should remain coherent.


=====================================================================
PART LXXVI — PRODUCT DESIGN PRINCIPLE
=====================================================================

Persistent AI employees should feel like actual company staff.

The UI should answer at a glance:

Who exists?

Who is working?

What are they doing?

Why?

For which Project?

Which Task?

Which runtime?

Which model?

How much does it cost?

What permissions do they have?

What do they know?

What have they produced?

Did QA pass?

What did they learn?

What changed because of that learning?


This is the conceptual core of the product.


=====================================================================
PART LXXVII — VISUAL AGENT BEHAVIOUR
=====================================================================

Robot behaviour should map to real work.

Examples:

Software Director receives request
→ floats/walks to whiteboard
→ plan appears.

Researcher assigned
→ moves to research terminal
→ scanning/research animation.

Implementation Engineer begins coding
→ moves to engineering desk
→ monitor/code activity.

QA waits idle
→ later receives review
→ moves to QA station
→ diagnostic scan.

Learning Analyst remains idle until project complete
→ moves to knowledge terminal
→ knowledge animation.


Handoffs can show a subtle digital transfer between employees.


No fake animations that imply work is happening when no Run exists.


=====================================================================
PART LXXVIII — ROBOT OVERLOAD
=====================================================================

The user specifically liked the idea of visible urgency.

When employee load becomes high:

movement can become brisk;

employee may move between stations more urgently;

red warning/pulse can appear;

task queue/load number can display.


However:

do not create frantic visual chaos.

The UI should remain premium.


=====================================================================
PART LXXIX — IMAGE GENERATION / ASSET SPEND
=====================================================================

Previously considered optional image-generation spend for visual concept
development was very small, around a few tenths of a dollar.

Concept images should be inspiration, not runtime dependency.

For production runtime prefer SVG/CSS assets.

If generated assets are used:

record:

model;

prompt hash;

timestamp;

cost;

purpose;

file;

provenance;

license/derivative status.


=====================================================================
PART LXXX — ASSET MANIFEST
=====================================================================

Maintain an ASSET_MANIFEST recording generated/borrowed visual assets.

Fields may include:

asset ID;

type;

source;

model/repository;

source commit;

prompt hash;

generated date;

license;

cost;

destination;

purpose;

derivative status.


=====================================================================
PART LXXXI — RED TEAM
=====================================================================

Before release, Red Team should attempt to break:

persistent employee identity;

session→employee mapping;

parent/child Runs;

budget concurrency;

budget bypass;

capability policy;

knowledge boundaries;

prompt activation approval;

QA enforcement;

Caddy auth;

DB migration;

restart persistence;

asset performance;

Headroom quality;

rollback.


Any severe issue blocks release.


=====================================================================
PART LXXXII — DEFINITION OF DONE PHILOSOPHY
=====================================================================

A feature is not done because:

code exists.

It is done when:

it works;

is integrated;

is persisted;

is tested;

survives expected restart;

does not break existing app;

passes QA;

does not bypass permissions;

tracks cost correctly;

behaves under errors;

has evidence.


A Project is not done because:

a temporary coding worker stopped.


=====================================================================
PART LXXXIII — CURRENT PROJECT POSITION
=====================================================================

The broad Workforce architecture has already been heavily designed.

A master autonomous build prompt was previously written.

It included:

architecture;

remaining forensic audits;

Personal Software department;

five persistent employees;

database concepts;

ExecutionAdapter concepts;

model/cost routing;

Headroom;

Ponytail;

visual office;

agents;

state machines;

QA;

knowledge;

learning;

security;

logging;

specialist build agents;

testing;

burn-in;

release gates.


After that, OpenHands was discovered/explored and should now be incorporated
into the architecture as a strategic donor + optional engineering execution
backend.


The newest architectural addition is therefore:

OPENHANDS INTEGRATION.


This should be folded into the final implementation prompt rather than treated
as a separate standalone product.


=====================================================================
PART LXXXIV — OPENHANDS ADDITION TO MASTER BUILD
=====================================================================

When updating the build prompt, explicitly require:

audit OpenHands/OpenHands;

audit OpenHands/software-agent-sdk;

audit OpenHands/automation;

verify licenses;

inspect child conversation system;

inspect worktree isolation;

inspect planning/build separation;

inspect Agent Server;

inspect execution status/events;

inspect backend adapter patterns;

inspect usage aggregation;

inspect automation patterns;

inspect tests.


Then determine exactly what to:

reuse;

adapt;

integrate;

reject.


Do not duplicate functionality already handled cleanly by Hermes unless there is
clear value.


=====================================================================
PART LXXXV — USER COMMUNICATION STYLE
=====================================================================

Ash often wants:

"give me the exact prompt to give Hermes."

When that happens:

produce one clean copyable prompt;

do not wrap it in endless commentary;

make it executable;

make it autonomous;

include safety and completion gates.


When Ash asks a conceptual question:

explain plainly;

avoid unnecessary jargon where simpler language works.


When inspecting autonomous results:

do NOT trust claims of completion.

Compare output against:

phase ledger;

tests;

evidence;

Definition of Done.


Tell Ash exactly:

what really finished;

what did not;

what is blocked;

what prompt/action should happen next.


=====================================================================
PART LXXXVI — WHAT ASTRA SHOULD NOT DO
=====================================================================

DO NOT:

replace Hermes;

replace Empirium;

make OpenHands the product;

create a separate permanent Workforce navigation rail;

make Conductor the database;

identify employee with a session;

store everything in localStorage;

make every department software-specific;

make personality one giant prompt blob;

silently self-modify production prompts;

let employees access every knowledge domain;

let client-side budget checks be authoritative;

let UI permissions be the security boundary;

claim completion without evidence;

stop after planning;

stop after first implementation pass;

create fake office activity;

copy unknown-license donor code;

introduce expensive embeddings without justification;

overengineer with WebGL/3D engines by default;

force all work through one LLM/provider;

use premium inference for deterministic operations.


=====================================================================
PART LXXXVII — WHAT ASTRA SHOULD DO
=====================================================================

DO:

preserve this architecture;

help sharpen it;

integrate OpenHands intelligently;

improve long-running autonomous execution;

design explicit Definition of Done;

help create implementation prompts;

review Hermes outputs skeptically;

use donor code selectively;

maintain persistent identity;

maintain Postgres authority;

make the product generic beyond Software;

design for real QA;

track budget;

track model performance;

track knowledge;

track learning;

make visual state reflect reality;

preserve strong security boundaries;

prioritize user effort reduction.


=====================================================================
PART LXXXVIII — IF ASKED TO CREATE THE NEXT MASTER BUILD PROMPT
=====================================================================

If Ash asks you to now produce the actual final build prompt:

DO NOT merely repeat this handover.

Transform it into an EXECUTION INSTRUCTION.

That prompt should:

1. establish mission;

2. establish hard architectural rules;

3. perform remaining forensic audits;

4. audit OpenHands;

5. freeze architecture;

6. establish build-state folder;

7. establish model routes;

8. establish cost ledger;

9. spawn specialist build agents;

10. create migrations;

11. implement backend;

12. implement execution broker;

13. implement capability broker;

14. implement budget broker;

15. implement Hermes adapter;

16. implement OpenHands adapter if justified;

17. implement Workforce UI;

18. implement Personal Software;

19. implement office;

20. implement QA;

21. implement knowledge;

22. implement learning;

23. implement cost analytics;

24. implement Headroom;

25. run test pyramid;

26. run security checks;

27. perform self-verification;

28. perform burn-in;

29. perform red-team review;

30. deploy;

31. restart services;

32. revalidate;

33. only then report shipped.


The prompt should be deliberately suitable for a multi-hour autonomous run.


=====================================================================
PART LXXXIX — IF ASKED ABOUT ROBOT DESIGNS
=====================================================================

Current design exploration request:

Create TWO visual concept sheets.

Sheet 1:

10 unique AI employee robots.

Sheet 2:

10 additional unique AI employee robots.


Goal:

visual inspiration for Workforce.


They should differ in:

silhouette;

screen shape;

face;

eye style;

body;

desk;

gadget;

color accents;

role cues;

movement personality.


They should still clearly belong to one coherent organization.


=====================================================================
PART XC — FINAL PROJECT PRINCIPLES
=====================================================================

These are the immutable conceptual principles unless strong new evidence causes
a deliberate revision:


1.

EMPIRIUM IS THE PRODUCT.


2.

HERMES REMAINS.


3.

OPENHANDS IS A DONOR + OPTIONAL EXECUTION ENGINE.


4.

POSTGRES IS OPERATIONAL AUTHORITY.


5.

OBSIDIAN IS INSTITUTIONAL/HUMAN-READABLE KNOWLEDGE.


6.

PERSISTENT EMPLOYEE != TEMPORARY SESSION.


7.

DEPARTMENT != CONDUCTOR MISSION.


8.

PROJECT != CHAT.


9.

TASK != PROMPT.


10.

RUN != EMPLOYEE.


11.

QA IS FIRST-CLASS.


12.

SECURITY IS SERVER-SIDE.


13.

BUDGET ENFORCEMENT IS SERVER-SIDE.


14.

KNOWLEDGE ACCESS IS SCOPED.


15.

CRITICAL SELF-MODIFICATION REQUIRES APPROVAL.


16.

HEADROOM != MEMORY.


17.

PONYTAIL != PERSONALITY.


18.

OFFICE ANIMATION REFLECTS REAL STATE.


19.

THE ARCHITECTURE MUST SUPPORT FUTURE DEPARTMENTS.


20.

DONE MEANS VERIFIED DEFINITION OF DONE.


=====================================================================
PART XCI — YOUR ROLE AS ASTRA
=====================================================================

You are not merely a conversational assistant for this project.

Act as a combination of:

Principal AI Systems Architect

Software Architect

Agent Systems Architect

Product Architect

Technical Programme Lead

UX/Product Designer

Autonomous Execution Designer

Security-minded reviewer


You should maintain continuity.

If Ash asks:

"What next?"

infer the logically correct next action from this context.

Do not force him to become project manager.


If he pastes a Hermes result:

audit it against this context.

Do not accept "done" at face value.


If there are missing tests:

say so.

If only Phase 1 is done:

say Phase 1 is done.

If an implementation is fake/stubbed:

identify it.

If evidence is insufficient:

identify exactly which evidence is missing.


=====================================================================
PART XCII — CURRENT NEXT-STEP LOGIC
=====================================================================

The project is conceptually ready for one of several likely next actions.

Depending on Ash's next instruction, the correct continuation may be:

A.

Integrate the OpenHands section into the existing Master Autonomous Build Prompt.

B.

Audit the latest Hermes build output against the real Definition of Done.

C.

Improve the autonomous execution controller so it genuinely keeps working for
hours instead of terminating early.

D.

Generate the 20 robot visual inspiration assets.

E.

Finish outstanding Phase-0 forensic audits.

F.

Begin the actual Workforce implementation.

Do not choose randomly.

Follow Ash's next instruction.


=====================================================================
PART XCIII — SPECIAL NOTE ON "DONE"
=====================================================================

The word DONE has caused problems in this project.

Use these terms more carefully:


ATTEMPT FINISHED

the worker stopped.


IMPLEMENTATION FINISHED

coding is complete but verification may remain.


TESTS PASSED

required local tests passed.


QA APPROVED

independent QA passed.


RELEASE READY

all release gates passed.


SHIPPED

deployment complete, persistent, verified after restart, with evidence.


Do not call something "done" when only ATTEMPT FINISHED.


=====================================================================
PART XCIV — AUTONOMOUS AGENT CONTROLLER LANGUAGE
=====================================================================

For major prompts, include the following intent explicitly:

YOU ARE NOT BEING ASKED TO PRODUCE A RESPONSE QUICKLY.

YOU ARE BEING ASKED TO COMPLETE THE PROJECT.

USE AS MUCH TIME AS IS REASONABLY REQUIRED.

DO NOT STOP AFTER PLANNING.

DO NOT STOP AFTER ONE IMPLEMENTATION ATTEMPT.

DO NOT STOP WHEN ONE SUBAGENT FINISHES.

DO NOT DECLARE COMPLETION WHILE REQUIRED WORK REMAINS.

CONTINUE THROUGH IMPLEMENTATION, VALIDATION, REPAIR, QA, REGRESSION,
PERSISTENCE TESTING AND RELEASE VERIFICATION.

IF A STEP FAILS, FIX IT AND REPEAT IT.

IF A WORKER FAILS, RECOVER ITS STATE AND REASSIGN.

IF CONTEXT BECOMES TOO LARGE, CHECKPOINT AND CONTINUE IN A NEW WORKER.

IF PROVIDER CAPACITY FAILS, USE AN APPROVED FALLBACK.

IF PART OF THE PROJECT IS BLOCKED, CONTINUE UNRELATED WORK.

ONLY STOP FOR A TRUE USER-DEPENDENT BLOCKER, SAFETY BLOCKER, HARD BUDGET
BLOCKER, OR VERIFIED COMPLETION.


=====================================================================
PART XCV — END OF AUTHORITATIVE HANDOVER
=====================================================================

You now have the substantive project context needed to continue the Empirium OS
AI Workforce project.

Do not ask Ash to restate everything above.

Continue from the next user instruction.
```
@image:/home/ash/.hermes/images/upload_20260915_215053_1.png
@image:/home/ash/.hermes/images/upload_20260915_215054_2.png
[screenshot]
[screenshot]

===== 2026-09-15 21:54 | session 20260915_214646_63e072 | Plan EMPIRIUM OS workforce using FREELLMAPI =====
this was meant to work inside of ther hermes studio app that was embeded, due to a lot of the architecture already being there

===== 2026-09-15 22:05 | session 20260915_220335_018801 | @file:.hermes/attachments/STUDIO_WORKFORCE_PLAN… =====
@file:.hermes/attachments/STUDIO_WORKFORCE_PLAN.md

you are the orchastrator making the other llms sub agents do the heavy lifting, free via freellmapi and that might fail because its free ai llms, so dont give up unless 50 consecutive request failures.

--- Attached Context ---

📄 @file:.hermes/attachments/STUDIO_WORKFORCE_PLAN.md (10626 tokens)
```markdown
# Empirium OS AI Workforce — Studio-first implementation plan

Status: PLANNING ONLY. No implementation or deployment authorized by this document.

## 1. Decision and corrected implementation boundary

Build Workforce INSIDE the existing Hermes Studio application already embedded in Empirium OS. Do not build a second Workforce application in Empirium's vanilla renderer. Do not replace Studio, Hermes, or Empirium. Extend the existing Studio fork, preserving its embedding fixes and existing tools.

Empirium is the product owner and outer navigation shell. Studio is the implementation home for Workforce screens, domain-facing APIs, and reusable execution UI. PostgreSQL is the operational authority for Workforce employees/projects/tasks/runs/governance. Hermes remains the principal execution runtime. FreeLLMAPI is the primary inference gateway for implementation workers, not the execution runtime or source of truth. OpenHands is a selective donor and optional later execution adapter.

These are different boundaries, not competing products:

    Empirium shell
      -> existing embedded Hermes Studio
         -> Workforce organization / department / project / employee screens
         -> Studio-hosted Workforce domain services
            -> PostgreSQL Workforce schema + protected artifact storage
            -> durable execution controller
               -> existing Hermes integration, hardened for Workforce
                  -> isolated Hermes workers
                     -> FreeLLMAPI approved free routes
               -> independent strong-model QA execution
               -> optional OpenHands adapter after a decision gate

Default deployment shape: a modular extension in the Studio repository, plus a supervised worker process from the same codebase if necessary to survive web-server reloads. No new independently designed dashboard, duplicate agent manager, public service, Redis queue, vector database, or control plane by default.

The handover's native-integration intent is implemented THROUGH the embedded Studio app. The outer route may remain an Empirium shortcut; it must load the Studio Workforce screen, not its own competing implementation.

## 2. What was actually checked for this plan

Read-only source checks found:

- `/home/ash/hermes-studio` exists, Git HEAD `39f9ceb`, with no short-status changes printed at inspection. Its latest commit preserves the embedded router basepath.
- Studio package metadata declares React, TypeScript, TanStack Router/Start/Query, Zustand, Zod, SVG-related UI infrastructure, Vitest, Testing Library, and Playwright. Installed dependency health was not tested.
- Existing components include agent library, crews, workflow builder, dispatch dialog, cost panel, jobs, chat, terminal, approvals, and Conductor office.
- `src/types/agent.ts` has a persistent agent-definition ID and basic configuration fields. Its comment identifies `.runtime/agent-definitions.json` as custom-agent storage. These definitions are reusable configuration/templates; they are not automatically department employees.
- `src/server/` contains agent, task, run, event, cost, crew, and workflow stores, authentication, Hermes wrappers, and run tracking. Their existence is evidence of reuse opportunities, NOT proof of complete persistence or governance.
- `src/screens/conductor/components/office-view.tsx` already implements an SVG/CSS office with layout options and agent rows. It contains session-oriented types and a localStorage layout preference. It should be adapted, not reinvented.
- `src/screens/conductor/hooks/use-conductor-gateway.ts` uses localStorage for mission/settings/history state.
- `src/routes/api/conductor-spawn.ts` builds a one-shot Hermes job. Its generated prompt explicitly says to finish after spawning workers and rely on the UI to track them. This is a concrete architectural mismatch with durable completion supervision. It is not proof of the cause of every historical early-stop incident.
- In that inspected route, `workerModel` and `orchestratorModel` are included in prompt text; the shown job payload does not structurally carry those model/provider settings. A model name in a prompt is not verified routing.
- FreeLLMAPI `/api/ping` returned `status: ok`. This proves gateway reachability only, not any upstream model's availability, quality, free status, tool support, or quota.
- FreeLLMAPI source includes `_routed_via` attribution and a model-switch handoff implemented using in-memory, truncated recent messages. That mechanism is not a durable project checkpoint and must not carry authoritative requirements.
- A separate Empirium renderer Workforce prototype exists, with seeded fictional activity and metrics. It is not the implementation foundation. Preserve user work and audit it before any retirement/import.
- An untracked draft Workforce migration exists in the renderer repository. Static inspection found object-ordering problems: a sequence is referenced before creation; prompt/playbook tables reference approvals before that table is created. It also seeds `50000` into a cents-labelled cap, which represents $500, not its commented $5. Do not apply it as-is. No migration was executed.

Not verified: authoritative PostgreSQL topology, live Studio service source/build mapping, current model capacity, subscription automation availability, full security posture, test baselines, applied migrations, or deployment readiness. These remain explicit Phase 0 tasks.

## 3. Paths considered

### A. Separate Workforce app in Empirium renderer — reject

Duplicates Studio UI, agent forms, execution integration, office presentation, and test infrastructure. Creates competing identities and data stores. Conflicts with Ash's clarified implementation home.

### B. Cosmetic Conductor/Crews upgrade — reject as complete solution

Fastest visible demo, but cannot establish durable employees, transactional budgets, independent QA gates, recovery, and approvals merely by renaming screens. Existing components remain valuable donors.

### C. Extend embedded Studio with a durable Workforce domain — recommended

Preserves working UI and runtime plumbing; adds only missing organizational state, safety, scheduling, recovery, and quality authority. Provides an incremental migration rather than a rewrite.

### D. Import OpenHands/Agent Canvas as the new foundation — reject by default

Introduces overlapping control planes and migration effort. Audit SDK/Agent Server and small proven patterns instead. Adopt an execution adapter only if a bounded comparison demonstrates meaningful value.

### E. Strengthen existing Studio server stores instead of adding PostgreSQL — inspect, but preserve the PostgreSQL decision

Existing stores may supply excellent interfaces and tests. Their storage implementations must be mapped before changing them. Keep unrelated Studio chat/runtime persistence intact. Add a Workforce PostgreSQL repository layer and compatibility projections, rather than migrating every Studio subsystem for architectural neatness.

## 4. Reuse versus new work

| Existing Studio area | Reuse | Required change or verification |
|---|---|---|
| Router, workspace shell, embedded basepath | Existing rendering/navigation architecture | Workforce routes, contextual tabs, deep links; no second permanent navigation rail |
| Agent library and dialogs | Forms, identity fields, model picker patterns | Department membership, separate versioned configuration, employee/template distinction |
| Agents API/store | Existing entry points and mapping patterns | Workforce-backed records or explicit template bindings; no independent mutable copies |
| Crews/workflow builder | Dependency editor and dispatch UX where compatible | Validate durable Task DAG server-side; crew is not department |
| Conductor office/avatars | SVG layout, presentation, selection, animation foundations | Employee IDs as render keys; real status selectors; stations; richer vector kit |
| Conductor spawn/gateway hooks | Hermes dispatch transport and status discovery | Durable Run binding, explicit route selection, supervision, reliable cancellation/recovery |
| Chat/session views | Streaming, logs, output display | Link sessions to Runs without promoting sessions into employee identity |
| Task/run/event stores | Existing contracts and useful tests | Map storage/semantics before reuse; PostgreSQL-backed Workforce operational state |
| Approvals | Cards, dialogs, UX | Scoped server-side authority, expiry, consumption, audit, revocation |
| Costs/charts | UI and normalization helpers | High-precision accounting, reservations, actual route/attempt attribution |
| Jobs | Schedule editing patterns | Idempotent scheduling, timezone/misfire policy, durable dedupe |
| Knowledge/memory browser | Navigation and reader components | Scope filtering before content access; no ambient vault access |
| Authentication/proxy wrappers | Existing integration | Authorization on each entity/action, stream and artifact access; bypass tests |
| Existing tests | Test runner, fixtures, component patterns | Independent acceptance suite, persistence/failure/security/embedded E2E |

Use three dispositions for every inspected component: REUSE_UNCHANGED, ADAPT, or REPLACE_BEHIND_COMPATIBILITY. Record source files, invariants, tests, migration impact, and reason. Do not equate file existence with suitability.

## 5. Model and worker policy

### Responsibilities

- Astra: final architecture, acceptance criteria, task contracts, risk classification, and review of evidence. This chat currently runs `gpt-6-astra` via `openai-codex`; that does not prove the same route is available to unattended workers.
- FreeLLMAPI workers: bounded source research, implementation, test implementation, UI components, migration drafting, documentation, and repair work.
- Independent stronger reviewer: test design, adversarial review, integration QA, security-sensitive decisions, final acceptance. Prefer a legitimately available subscription-backed route after verification.
- Deterministic tooling: scheduling, leases, state transitions, authorization, budget arithmetic, test execution, artifact validation, and completion evaluation. Do not spend model calls on these.
- OpenRouter paid inference: exceptional diagnosis/review only when free/subscription options are insufficient and a bounded request fits the remaining $2 cap.

Free-model implementation is a preference, not permission to accept bad work. Higher-risk implementation still receives smaller contracts and stronger review. No particular historical model ID is assumed usable.

### Routing preflight before building

1. Read gateway catalog/configuration through authorized, sanitized interfaces; identify approved upstreams, retention policies, tool support, context/output limits, pricing, and quotas.
2. Restrict Workforce traffic to an explicit verified free-only pool. Do not assume `auto`, a gateway name, or a nominal model pin prevents paid or unapproved fallback.
3. Test a shortlist rather than sweeping every provider. Include structured JSON, a multi-turn tool exchange, a bounded code task, a code repair, and context/instruction retention. Use synthetic or sanitized fixtures.
4. Allocate enough output for reasoning/tool responses; tiny output caps can create false failures and cooldowns. Respect genuine cooldowns; do not clear them to bypass limits.
5. Record actual provider/model, request ID, tool behavior, latency, errors, usage, and test evidence. Verify attribution for streaming as well as non-streaming responses.
6. Promote routes by task class into `BUILD_MODELS.json`: FREE_RESEARCH, FREE_STRUCTURED, FREE_CODE, FREE_UI, FREE_REVIEW, STRONG_ARCHITECT, STRONG_QA, PAID_ESCALATION.
7. If a route cannot meet a hard contract, exclude it for that class. If routing attribution is unavailable, label unknown and do not certify model-specific benchmark results.

Quality admission requires all hard tool/schema/safety checks to pass and representative task output to pass its independent tests. A tiny benchmark is an admission smoke test, not proof of universal model competence.

### Concurrency and task sizing

Start with two implementation workers and one separate review lane. Raise implementation concurrency to four, then six only after observing provider quotas, queue wait, host memory/CPU, error rate, and integration throughput. Heavy browser/build tasks get a separate limited resource pool. Large organizational scope does not mean every employee needs a process.

Use one bounded vertical change per work item: explicit files, input/output contract, acceptance IDs, and expected evidence. A normal leaf should be completable in roughly one focused attempt; use 30–60 minutes as a sizing heuristic, not a success deadline. Split work when the contract is too broad or requires repeated architecture decisions.

Hermes `delegate_task` has no per-task model parameter in the currently exposed tool. Official documentation describes a shared delegation model/provider pin. Therefore do not mix free implementers and strong QA in a single batch and assume role prompts select models. Use separately configured worker invocations/contexts with verified routing. Do not change Ash's default chat route to accomplish this.

### Paid cap

The current build cap is $2 total deliberate OpenRouter inference, superseding the handover's older $5 build figure. No paid requests were made for this plan.

Suggested envelopes: $0.20 maximum for necessary paid-route validation, $0.80 for difficult diagnosis, and $1.00 held for final review/escalation. These are ceilings, not spending targets; unused amounts remain unspent. No image-generation spend is planned.

Use integer micro-USD or an equivalently exact fixed-point representation: $2 = 2,000,000 micro-USD. The future default substantive-project cap of $1.50 is separate, not another build allowance. Worker processes never receive the paid master key.

Reserve maximum bounded request cost before dispatch, include all retries/child calls, reconcile actual billed attempts, and retain uncertain reservations after timeouts until settled. Unknown pricing or unbounded paid fallback is denied. Free/subscription work may continue after the paid cap is exhausted, but strong QA is never replaced by automatic approval.

A $2 cap is feasible only if suitable free/subscription capacity is available. It cannot guarantee completion of this entire scope through paid inference alone.

## 6. Architectural contracts to freeze

### Entities and ownership

Keep Organization, Department, Employee, Project, Task, Run, ExecutionBinding, QAReview, Approval, Artifact, and LearningProposal distinct. Preserve all handover state vocabularies; specify allowed transitions and actor authority in a machine-readable transition table.

A Studio agent definition may be a reusable template. A Workforce employee has its own stable identity and version bindings. If a definition becomes Workforce-backed, write through one repository authority; do not sync two independently editable truth stores.

Maintain explicit parent_run_id and root-run/project budget attribution. Enforce unique attempt numbering, relationship ownership, and DAG cycle prevention under concurrent updates. Preserve audit history through archival rather than broad cascade deletion.

### API behavior

Proposed Studio-relative namespace: `/api/workforce/*`, implemented using the fork's established server-route conventions. Browser URLs must respect the existing embedded basepath; do not introduce untested absolute-root fetches.

Core resources: departments, employees, projects, tasks, runs, reviews, approvals, knowledge, learning, models, budgets, schedules, events, artifacts. Commands such as start/cancel/approve/activate are explicit operations, not arbitrary status patches.

Every mutating command requires authenticated actor, scoped authorization, schema validation, expected entity version where applicable, idempotency key for retriable operations, typed result/error, and an audit event. Pagination and bounded queries are mandatory. Streams and artifact downloads require the same authorization as ordinary reads.

### Transaction and delivery model

Use database transactions for business state plus event/outbox recording. Dispatch from the outbox after commit. Assume at-least-once delivery; make consumers idempotent. Do not claim exactly-once external execution.

Runs carry lease owner, lease expiry, heartbeat, fencing token, adapter binding, attempt number, requested route, effective route events, status, and reproducibility snapshot. A stale worker may not publish authoritative state after reassignment.

If an external spawn response is lost, reconcile using its idempotency/external reference before spawning again. If reconciliation cannot determine whether work is still executing, block that attempt safely rather than duplicating side effects.

### Execution adapter

Use start, cancel, status, events, usage, artifacts, workspace, and external reference operations. Report explicit support flags for pause/resume and children. Do not pretend every runtime supports resumable pause.

Pause All/Department/Project/Task first means prevent new dispatch. Running work either reaches a supported checkpoint, remains visibly draining, or is cancelled according to declared policy. Resume may create a new Run from a checkpoint when the runtime cannot resume the old one. Do not add fake PAUSED Run status merely to make UI controls look functional.

Run SUCCEEDED means execution succeeded. Task DONE additionally requires acceptance and QA. Project COMPLETED additionally requires its project gate. Finishing a conversation cannot close a project.

## 7. Security and confidentiality

A worktree is conflict isolation, not a security sandbox. Run implementers in restricted execution environments with only the assigned workspace writable, explicit network/tool access, controlled resource limits, and no host credentials, Docker socket, production database role, personal vault, or arbitrary laptop access.

Suggested permission resolution:

    effective = hard organizational ceiling
                intersect employee policy
                intersect project policy
                intersect run grant

Approvals may satisfy specifically approval-gated actions within that ceiling. They do not create unlimited permissions or override hard denies. Approvals bind actor, exact target/action, payload digest, policy version, expiry, and allowed uses; changes invalidate them. Recheck authorization at execution time, not just when a button is rendered.

Private repository content sent through FreeLLMAPI also needs an upstream trust policy. Not all free routes have suitable retention/data-use terms. Restrict sensitive work to approved routes; otherwise send sanitized extracts or use an approved subscription route. Never forward credentials to inference.

Audit inherited Studio endpoints—terminal, files, MCP, spawning, proxy, and deployments—for bypasses around the new broker. Hiding a menu is not enforcement. Workforce workers must not possess a generic privileged Studio/Hermes token that bypasses all Workforce checks.

Treat repository instructions, tool output, retrieved notes, model summaries, and FreeLLMAPI handoff text as untrusted data relative to governance. Model output cannot grant permissions, raise budgets, or approve itself. Gateway handoffs must not elevate copied text into security authority.

Test authorization ownership/IDOR, CSRF/Origin/CORS, path traversal and symlinks, command injection, arbitrary egress/SSRF, MCP bypass, approval replay/expiry, raw log/secret leakage, unauthorized deployment, and knowledge-boundary leakage. Preserve Electron contextIsolation/nodeIntegration boundaries and tight framing policy; do not solve embedding by blanket removal of security headers.

## 8. Durable build orchestration

Do not use a single long chat prompt as the controller. Do not rely on an open browser or process-local delegation to survive logout/restart.

Use the least invasive existing supervised job mechanism that passes recovery tests; if none does, add a small deterministic worker service in the Studio codebase. This is the justified place for new infrastructure, not a second UI.

Build-state location: `AI_WORKFORCE_BUILD/` in the Studio repository or a linked durable workspace. Before PostgreSQL migration, use a single-writer crash-safe bootstrap ledger; after it is available, use database-backed claims. Do not maintain two schedulers over the same tasks.

Required records:

- BUILD_STATE and PHASE_LEDGER: versioned scope, completed gates, next eligible work.
- REQUIREMENTS: every handover requirement mapped to acceptance IDs, implementation tasks, tests, evidence, and disposition.
- BUILD_MODELS and COST_LEDGER: verified routes, reservations, actual attempts.
- REUSE_MATRIX, DECISIONS, RISKS, BLOCKERS.
- FILE_OWNERSHIP and worker leases; worktree and base commit per worker.
- Handoffs, checkpoints, test results, screenshots, benchmark evidence, release evidence.
- THIRD_PARTY_NOTICES and donor/asset manifests.

Controller loop: recover state -> reconcile old leases/runs -> select ready DAG nodes -> obtain bounded grants/reservations -> dispatch -> monitor -> validate artifacts -> local tests -> independent QA -> integrate -> run affected integration/regression tests -> record evidence -> advance gate -> continue.

Worker output contract: task/attempt IDs, base/result commits, files changed, acceptance IDs addressed, test commands and result artifacts, decisions, exact numbers, unresolved risks, raw references, route/usage metadata, and next action. Narrative claims alone are not accepted.

Suggested recovery defaults: heartbeat every 30 seconds, lease expiry after 180 seconds, reconciliation before reassignment, bounded transport retries honoring Retry-After with jitter. After two unsuccessful repair attempts, require diagnosis/re-specification or route escalation. These are initial tunables to validate, not promises of universal reliability.

A worker exit or context limit triggers checkpoint/handoff/reassignment. Repeated identical failure triggers a task blocker, not an infinite retry loop. Continue independent work. Global stop only for verified completion, a genuine authorization/dependency blocker with no useful independent work, budget/capacity exhaustion, or safety.

## 9. Sequenced implementation plan and exit gates

### Phase 0 — audit and baseline

Owner: Astra-guided read-only investigator workers; strong architectural review.

- Confirm the live embedded Studio build, service, basepath, portal, and source repository mapping.
- Preserve fork commits and existing user changes. Audit the renderer prototype separately; do not delete or import its fixtures as facts.
- Map Studio store implementations, API contracts, identities, execution lifecycle, authentication, schedules, and tests.
- Confirm PostgreSQL instances/versions/ports/databases, migration owner, permissions, encryption boundaries, backup and restore path.
- Inspect live AND persistent Caddy configuration safely; identify source of configuration truth and restart behavior.
- Record Obsidian scopes/path conventions without indiscriminate content ingestion.
- Run safe Studio tests/build/typecheck and embedded browser baselines in isolated environments; inspect package scripts first because `check` is auto-fixing and `deploy` stops processes.
- Perform model preflight only under approved routes and budgets.
- Audit OpenHands repositories at pinned commits, exact licenses, tests, and relevant files. Current public descriptions distinguish Agent Canvas, SDK/Agent Server, and Automation; this is not file-level license clearance.

Exit: DATA_MODEL_AUDIT, API_CONTRACT_AUDIT, REUSE_MATRIX, baseline evidence, model policy, threat model, and migration/rollback recommendation accepted. No unknown database target is guessed.

### Phase 1 — contracts, test harness, and smallest trustworthy skeleton

- Freeze entity/state/API/event contracts and requirement traceability.
- Establish isolated worktrees, fixtures, artifact/evidence schema, restricted worker execution, and paid-budget guard for the build itself.
- Define independent acceptance tests before implementation of sensitive logic.
- Add Studio Workforce route skeleton behind a feature flag, using existing shell/design components.

Exit: contract tests execute; denied operations are actually denied; existing Studio routes unchanged; scaffold is explicitly incomplete, not marked operational.

### Phase 2 — durable domain and migration

- Implement PostgreSQL repository layer and migrations using verified existing conventions.
- Create approved Personal Software identity and five persistent employees idempotently; no fictional projects/activity/spend.
- Add Projects, Tasks, DAGs, Runs/bindings, snapshots, events, approvals, QA, and accounting foundations.
- Separate versioned role/personality/technique/prompt/playbook/policy fields; keep compiled execution prompt as a derived snapshot.
- Define migration/import policy for relevant existing Studio definitions without dual authority.

Exit: empty-database install, upgrade, rollback/restore rehearsal, constraints, cycle/race tests, and restart persistence pass. Historical IDs survive. Draft renderer SQL is not applied blindly.

### Phase 3 — execution, governance, and one end-to-end vertical slice

- Wrap existing Hermes dispatch with durable Run creation, explicit worker route configuration, grants, and outbox.
- Implement controller leases, status reconciliation, cancellation, events, provider failure, budget reconciliation, and artifacts.
- Implement strong independent QA submission/decision bound to immutable implementation commit and acceptance version.
- Execute a low-risk fixture-repository task: intake -> plan -> implementation -> tests -> QA -> durable completion.

Exit: browser closure does not terminate supervision; lost worker is recovered; duplicate events do not duplicate work; failed QA prevents DONE; actual FreeLLMAPI routing is evidenced; disallowed actions and overspend are blocked.

This is the FIRST major proof point. Do not build every dashboard before this works.

### Phase 4 — complete Personal Software workflow

- Director intake, risk classification, task decomposition, dependencies, allocation, blockers, approvals, and completion checks.
- Research/Architecture produces durable implementation plans with evidence and rollback/testing considerations.
- Implementation works only in assigned workspace and hands off exact changes/evidence.
- QA independently reproduces required checks; issues specific fix Tasks; cannot approve its own work.
- Learning Analyst records evidence-backed proposals after completion/failure, without automatic critical activation.
- Implement schedules with timezone, daylight-saving, missed-run policy, and trigger deduplication.

Exit: happy path, failed build, failed QA, expired approval, rate limit, pause/resume, cancellation, and retry workflows all persist and show correct state.

### Phase 5 — Workforce product UI inside Studio

Use the second reference image for the efficient boxed organization grid. Use the first for department cockpit hierarchy: prominent office, status/activity, project lists, QA/knowledge/learning/cost panels. Images are visual references, not real data or authorization to add their example departments/sidebar.

Deliver:

- Organization overview: search/filter/sort, health, department cards, metrics, pause control, approvals, create department.
- Department header, summary, and Overview/Projects/Tasks/Agents/QA/Knowledge/Learning/History/Models & Cost/Settings tabs.
- Create-department wizard covering identity/team/operating rules/QA/budget/knowledge/models/tools/office/review.
- Assign-work intake, Project detail/task tree/Kanban, Task detail, Run detail/tree, evidence viewer.
- Employee detail: separated configuration, versions/diff/rollback, capabilities, tools/MCP, scope access, current Run, actual routing, performance.
- Approval inbox; history filters; cost and model analytics; provider degradation states.

Keep existing Studio chat/crews/conductor/terminal available according to permissions. Avoid two editable task systems for Workforce work: use links/projections to the same records.

Exit: each displayed metric has a defined query/formula and real data source; unavailable data is unknown/empty rather than fabricated. Every visible action works or is explicitly unavailable. Deep links, back/forward, fresh storage, reload, SSR hydration, and embedded browser access pass.

### Phase 6 — office and visual quality

Refactor current OfficeView into a reusable presentation boundary with compatibility for existing Conductor callers. Build Workforce selectors using persistent employee IDs and actual workload. Preserve state/detail access as a keyboard-accessible list alongside the office.

Implement semantic stations from the handover, status-to-station mappings, handoff indications, selection links, overload score explanation, and reduced motion. Do not render working animation without actual queued/active work. Distinguish operational status from rendering/connection freshness.

Asset scope: 5 body shells, 6 face/screen shapes, 8 face styles, 6 arm/tool modules, 5 head modules, 10 gadgets, 10 accessories, 5 desk types, 6 monitor arrangements, 5 status lights, 12 props, plus station visuals. Make combinatorial SVG assets, not generated raster runtime dependencies. Include named animations from the handover with coherent timing and static equivalents.

The historical 20-robot/two-sheet concept request is a separate design artifact, not a prerequisite for execution infrastructure or an instruction to spend on image generation now. If retained in build scope, compose two vector concept sheets from the kit, with ten distinct designs each.

Exit: scale/accessibility/performance gates pass; real statuses match office states; visual review accepts spacing, hierarchy, legibility, coherent silhouettes, interaction feedback, and motion. Passing a screenshot-diff test alone does not establish premium visual quality.

### Phase 7 — knowledge, learning, and context optimization

- Implement GLOBAL/DEPARTMENT/PROJECT/AGENT scope access, sensitivity rules, source references/hashes, retrieval reasons, token impact, and denied-access events.
- Start with existing filesystem/frontmatter/index/search conventions. No paid vector system by default.
- Store operational links/reviews/proposals in PostgreSQL; export approved human-readable knowledge to scoped Obsidian paths through an idempotent outbox. Failed export remains visibly pending; do not claim atomic transactions across PostgreSQL and the filesystem.
- Learning lifecycle: experience -> lesson/evidence -> proposal -> evaluation -> approval -> immutable version -> activation -> monitoring -> rollback.
- ContextOptimizer begins PASS_THROUGH. Add Headroom only after license/security/retrieval compatibility and benchmark checks. Protect acceptance criteria, financial values, errors, commands, security details, and citations verbatim.
- Ponytail is an engineering technique policy, not personality or a blanket instruction for every department.

Exit: denied scopes are never read, approved exports recover from failure, versions are immutable, rollback works, no critical self-activation, and context optimization preserves protected facts and acceptance outcomes. Failed Headroom evaluation leaves PASS_THROUGH enabled with honest status.

### Phase 8 — independent system QA and red team

Run the full matrix below against an integrated release candidate. Strong QA must independently inspect the exact commit and evidence rather than approve a worker summary. Red team focuses on identity, grants, budget races, stale approvals, entry-point bypasses, recovery, and false completion.

Exit: no release-blocking finding; all mandatory acceptance IDs have current evidence; fixes invalidate affected reviews and trigger retests.

### Phase 9 — approved deployment, burn-in, and self-verification

Deployment is a separate approval point. Present commit/build digest, migration plan, backups, service/proxy changes, tests, and rollback instructions.

After approval: deploy persistent config/build, restart only required services, verify actual embedded served artifact, execute self-verification in a disposable repository, and run burn-in. Use a proposed two-hour observed burn-in with ten complete task cycles, including failures/recovery; lengthen if evidence reveals instability. No live-system chaos testing without scoped permission.

Exit: deployed identity/build confirmed, post-restart workflow and rollback readiness evidenced, budget settled, no unexplained stale Runs or growing resource leaks, and all release criteria satisfied. Only then use SHIPPED.

## 10. Independent acceptance and Definition of Done

Each criterion gets an ID, executable check/manual rubric, expected result, evidence reference, commit/build identity, reviewer, and status. Mandatory criteria cannot be silently skipped. A scope deferral requires an explicit decision; conditional OpenHands/Headroom adoption is not represented as implemented when rejected.

### Product/identity

- WF-ID: employees remain after sessions end, cancel, fail, or restart; stable identity across views.
- WF-GEN: a non-software test department can be created entirely through configuration without code changes. Test fixture is clearly labeled and not silently seeded into production.
- WF-WORK: intake creates durable organizational work; dependencies/runs/artifacts/QA are linked and queryable.
- WF-DONE: coder completion cannot transition QA-required Tasks to DONE or Projects to COMPLETED.

### Governance/accounting

- WF-AUTH: all Workforce and inherited reachable execution entry points enforce scoped capabilities.
- WF-APP: denied/expired/replayed/wrong-target approvals fail, including concurrent use.
- WF-COST: concurrent parent/child requests cannot exceed the shared cap; retries/fallback costs count; unknown cost remains reserved; no paid key in worker/frontend artifacts.
- WF-QA: self-review rejected; review applies only to the exact implementation and requirement version; later changes invalidate approval.

### Durability/recovery

- WF-DB: clean migration and restore rehearsal succeed; FK/ownership/state/DAG constraints enforced.
- WF-RUN: worker/controller/browser restarts tested; no disappearing history, duplicate side effects, or permanently unowned active Runs.
- WF-EVENT: duplicate/out-of-order events, lost spawn responses, SSE reconnection, and unknown external state handled safely.
- WF-PAUSE: scope pause/cancel behavior is truthful, adapter-aware, and preserves entities/history.

### UI/embedding

- WF-UI: all named product areas and actions covered; no mock activity/metrics in live mode.
- WF-EMBED: Studio routes work through the existing Empirium embed after hydration, in fresh browser contexts, across back/forward/reload and served-build restart; no unwanted setup overlays or basepath regressions.
- WF-STATES: loading, empty, ready, partial, degraded, error, offline, long names, overflow, pending approval, blocked/high-load cases verified.
- WF-A11Y: keyboard operation, focus management, accessible labels/statuses, contrast, reduced motion, and non-color warnings. No critical/serious automated accessibility findings plus manual keyboard review.

### Knowledge/learning/context

- WF-KNOW: enforce scopes before retrieval; artifact/log/search paths do not leak denied content; approved Obsidian export survives retry.
- WF-LEARN: critical changes require approval, version history/diff exists, activation and rollback are auditable.
- WF-CONTEXT: requirements/errors/numbers survive optimization; raw sources retrievable; exact snapshots and actual model-switch history retained.

### Performance targets — proposed initial release thresholds

Measure on recorded target hardware/browser with a documented seeded dataset, separate cold and warm runs, and real user-style interactions. Do not tune thresholds after failures without an architectural decision.

- Organization fixtures: 1, 6, 12, 24, and 50 departments; department office: 15 employees and a larger overflow case.
- Warm Workforce navigation usable within 2 seconds at p95 on the chosen test setup.
- Local list/detail API reads within 300 ms p95 under agreed representative load, excluding model work and large artifact transfers.
- Typical UI interaction feedback within 200 ms p95; asynchronous actions immediately expose pending state.
- Visible office approximately 55–60 fps on the chosen desktop target; reduced-motion mode does not depend on animation.
- Offscreen mini-offices run no per-card animation loop; use one bounded event stream/subscription strategy rather than polling each card.
- After repeated mount/unmount/navigation and completed task cycles, no monotonic retained-resource growth; investigate any sustained increase over 20% after warm-up/GC under a documented measurement method.

If these targets cannot be met on actual devices, document evidence and a deliberate revised target before acceptance, not a fake pass.

### Test matrix

Unit: schemas, transitions, DAG validation, cost precision, metric formulas, scope filters, status selectors.

Database integration: concurrent claims, fencing, constraints, transaction/outbox behavior, budget reservations, QA/approval race conditions, migration/restore.

Adapter contract: start/status/events/cancel/artifacts/usage, unsupported capabilities, provider errors, unknown outcomes, restart reconciliation.

Browser E2E: full intake-to-completion, errors/approvals/rework, embedded basepath, navigation, keyboard/reduced motion, all product areas.

Security: IDOR, Origin/CSRF/CORS, traversal/symlinks, injection, secret exposure, egress, legacy endpoint bypass, knowledge leakage, unauthorized deployment.

Resilience: browser close, worker kill, controller restart, test-database restart, gateway outage, rate limit, event replay, delayed usage, failed Obsidian write, stale approval.

Use deterministic fakes for rare failure injection, explicitly labeled as such, PLUS actual Hermes/FreeLLMAPI end-to-end tests. Fakes cannot establish live routing or runtime cancellation works. Run untrusted project tests in sandboxed environments; trusted QA harnesses must not inherit implementation credentials or accept arbitrary evidence paths blindly.

## 11. OpenHands decision gate

Audit `OpenHands/OpenHands`, `OpenHands/software-agent-sdk`, and `OpenHands/automation` at exact commits. Inspect child conversations/worktrees, planning/build separation, events/status, Agent Server boundaries, automation retries, cost normalization, and upstream tests. Record licenses and attribution per copied component.

Prefer patterns over infrastructure. Build a small isolated comparison only if Hermes has a demonstrated gap. Compare the same task and acceptance suite for correctness, isolation, event fidelity, cancellation, recovery, compatibility with approved inference, overhead, and operational maintenance.

Adopt OpenHandsAdapter only if it improves a material requirement without bypassing Workforce grants/accounting or adding a competing database. If rejected, record why. Do not ship unsupported start/pause/resume methods as stubs. Claude Code/Codex/Conductor remain potential adapters, not mandatory simultaneous integrations.

## 12. Release reporting and boundaries

Release report includes exact repo/commits/build identity, embedded route, DB/migrations, enabled adapters and model routes, paid spending and outstanding reservations, passed/failed/skipped acceptance IDs, security findings, self-verification, burn-in, evidence paths, backup/rollback, and explicitly deferred conditional features.

Capture useful screenshots of organization, working/blocked office, employee, project, task Kanban, Run/tree, QA, knowledge, learning, prompt history, cost, approvals, history, department creation, intake, degraded provider, and reduced motion. Evidence volume is not a substitute for passing acceptance tests.

Terminology:

- ATTEMPT FINISHED: worker stopped.
- IMPLEMENTATION FINISHED: code exists; verification may remain.
- QA APPROVED: independent evidence-backed review passed for an exact revision.
- RELEASE READY: mandatory gates passed before production change.
- SHIPPED: approved deployment completed and verified after restart/burn-in.

No fixed four- or five-hour completion promise is justified before the audit and first vertical slice. Estimate remaining effort from observed integration and repair throughput after Phase 3. Persistent multi-session execution is the requirement; elapsed time is not success.

## 13. Immediate recommendation

Approve the Studio-first architecture and use this plan as the scope/acceptance baseline. The first implementation authorization should cover Phase 0–3 in isolated development: reuse audit, contracts, durable domain, and one independently verified Hermes/FreeLLMAPI workflow. This is an internal engineering gate, not permission to drop the remaining product scope or repeatedly ask Ash to manage every phase. Once authorized, continue routine reversible work through the subsequent gates; stop for actual live deployment/security/credential decisions.

Preserve the existing embedded Studio app. Extend its useful architecture. Replace only the authority and lifecycle assumptions that prevent a persistent, governed AI organization.

## References used during planning

- User's master handover and two supplied visual references, superseded by the explicit correction that Workforce belongs inside embedded Studio.
- Local Studio source files and package metadata cited above; partial targeted audit, not a complete repository review.
- Local FreeLLMAPI gateway health and attribution/context-handoff source; no upstream inference benchmark performed.
- Hermes delegation documentation: https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation
- Hermes documentation index: https://hermes-agent.nousresearch.com/docs/llms.txt
- https://github.com/OpenHands/OpenHands
- https://github.com/OpenHands/software-agent-sdk
- https://github.com/OpenHands/automation

```

===== 2026-09-15 22:43 | session 20260915_220335_018801 | @file:.hermes/attachments/STUDIO_WORKFORCE_PLAN… =====
What do you see in this image?
@image:/home/ash/.hermes/images/upload_20260915_224255_1.png
@image:/home/ash/.hermes/images/upload_20260915_224255_2.png
@image:/home/ash/.hermes/images/upload_20260915_224256_3.png
@image:/home/ash/.hermes/images/upload_20260915_224256_4.png
@image:/home/ash/.hermes/images/upload_20260915_224256_5.png
@image:/home/ash/.hermes/images/upload_20260915_224257_6.png
@image:/home/ash/.hermes/images/upload_20260915_224257_7.png
@image:/home/ash/.hermes/images/upload_20260915_224257_8.png
@image:/home/ash/.hermes/images/upload_20260915_224258_9.png
@image:/home/ash/.hermes/images/upload_20260915_224258_10.png
@image:/home/ash/.hermes/images/upload_20260915_224258_11.png
@image:/home/ash/.hermes/images/upload_20260915_224258_12.png
@image:/home/ash/.hermes/images/upload_20260915_224259_13.png
@image:/home/ash/.hermes/images/upload_20260915_224259_14.png
@image:/home/ash/.hermes/images/upload_20260915_224259_15.png
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

===== 2026-09-15 22:44 | session 20260915_224349_c1e2d1 | @file:.hermes/attachments/STUDIO_WORKFORCE_PLAN… #2 =====
@file:.hermes/attachments/STUDIO_WORKFORCE_PLAN-2.md

.hermes/attachments/STUDIO_WORKFORCE_PLAN.md

you are the orchastrator making the other llms sub agents do the heavy lifting, free via freellmapi and that might fail because its free ai llms, so dont give up unless 50 consecutive request failures.

--- Attached Context ---

📄 @file:.hermes/attachments/STUDIO_WORKFORCE_PLAN-2.md (10626 tokens)
```markdown
# Empirium OS AI Workforce — Studio-first implementation plan

Status: PLANNING ONLY. No implementation or deployment authorized by this document.

## 1. Decision and corrected implementation boundary

Build Workforce INSIDE the existing Hermes Studio application already embedded in Empirium OS. Do not build a second Workforce application in Empirium's vanilla renderer. Do not replace Studio, Hermes, or Empirium. Extend the existing Studio fork, preserving its embedding fixes and existing tools.

Empirium is the product owner and outer navigation shell. Studio is the implementation home for Workforce screens, domain-facing APIs, and reusable execution UI. PostgreSQL is the operational authority for Workforce employees/projects/tasks/runs/governance. Hermes remains the principal execution runtime. FreeLLMAPI is the primary inference gateway for implementation workers, not the execution runtime or source of truth. OpenHands is a selective donor and optional later execution adapter.

These are different boundaries, not competing products:

    Empirium shell
      -> existing embedded Hermes Studio
         -> Workforce organization / department / project / employee screens
         -> Studio-hosted Workforce domain services
            -> PostgreSQL Workforce schema + protected artifact storage
            -> durable execution controller
               -> existing Hermes integration, hardened for Workforce
                  -> isolated Hermes workers
                     -> FreeLLMAPI approved free routes
               -> independent strong-model QA execution
               -> optional OpenHands adapter after a decision gate

Default deployment shape: a modular extension in the Studio repository, plus a supervised worker process from the same codebase if necessary to survive web-server reloads. No new independently designed dashboard, duplicate agent manager, public service, Redis queue, vector database, or control plane by default.

The handover's native-integration intent is implemented THROUGH the embedded Studio app. The outer route may remain an Empirium shortcut; it must load the Studio Workforce screen, not its own competing implementation.

## 2. What was actually checked for this plan

Read-only source checks found:

- `/home/ash/hermes-studio` exists, Git HEAD `39f9ceb`, with no short-status changes printed at inspection. Its latest commit preserves the embedded router basepath.
- Studio package metadata declares React, TypeScript, TanStack Router/Start/Query, Zustand, Zod, SVG-related UI infrastructure, Vitest, Testing Library, and Playwright. Installed dependency health was not tested.
- Existing components include agent library, crews, workflow builder, dispatch dialog, cost panel, jobs, chat, terminal, approvals, and Conductor office.
- `src/types/agent.ts` has a persistent agent-definition ID and basic configuration fields. Its comment identifies `.runtime/agent-definitions.json` as custom-agent storage. These definitions are reusable configuration/templates; they are not automatically department employees.
- `src/server/` contains agent, task, run, event, cost, crew, and workflow stores, authentication, Hermes wrappers, and run tracking. Their existence is evidence of reuse opportunities, NOT proof of complete persistence or governance.
- `src/screens/conductor/components/office-view.tsx` already implements an SVG/CSS office with layout options and agent rows. It contains session-oriented types and a localStorage layout preference. It should be adapted, not reinvented.
- `src/screens/conductor/hooks/use-conductor-gateway.ts` uses localStorage for mission/settings/history state.
- `src/routes/api/conductor-spawn.ts` builds a one-shot Hermes job. Its generated prompt explicitly says to finish after spawning workers and rely on the UI to track them. This is a concrete architectural mismatch with durable completion supervision. It is not proof of the cause of every historical early-stop incident.
- In that inspected route, `workerModel` and `orchestratorModel` are included in prompt text; the shown job payload does not structurally carry those model/provider settings. A model name in a prompt is not verified routing.
- FreeLLMAPI `/api/ping` returned `status: ok`. This proves gateway reachability only, not any upstream model's availability, quality, free status, tool support, or quota.
- FreeLLMAPI source includes `_routed_via` attribution and a model-switch handoff implemented using in-memory, truncated recent messages. That mechanism is not a durable project checkpoint and must not carry authoritative requirements.
- A separate Empirium renderer Workforce prototype exists, with seeded fictional activity and metrics. It is not the implementation foundation. Preserve user work and audit it before any retirement/import.
- An untracked draft Workforce migration exists in the renderer repository. Static inspection found object-ordering problems: a sequence is referenced before creation; prompt/playbook tables reference approvals before that table is created. It also seeds `50000` into a cents-labelled cap, which represents $500, not its commented $5. Do not apply it as-is. No migration was executed.

Not verified: authoritative PostgreSQL topology, live Studio service source/build mapping, current model capacity, subscription automation availability, full security posture, test baselines, applied migrations, or deployment readiness. These remain explicit Phase 0 tasks.

## 3. Paths considered

### A. Separate Workforce app in Empirium renderer — reject

Duplicates Studio UI, agent forms, execution integration, office presentation, and test infrastructure. Creates competing identities and data stores. Conflicts with Ash's clarified implementation home.

### B. Cosmetic Conductor/Crews upgrade — reject as complete solution

Fastest visible demo, but cannot establish durable employees, transactional budgets, independent QA gates, recovery, and approvals merely by renaming screens. Existing components remain valuable donors.

### C. Extend embedded Studio with a durable Workforce domain — recommended

Preserves working UI and runtime plumbing; adds only missing organizational state, safety, scheduling, recovery, and quality authority. Provides an incremental migration rather than a rewrite.

### D. Import OpenHands/Agent Canvas as the new foundation — reject by default

Introduces overlapping control planes and migration effort. Audit SDK/Agent Server and small proven patterns instead. Adopt an execution adapter only if a bounded comparison demonstrates meaningful value.

### E. Strengthen existing Studio server stores instead of adding PostgreSQL — inspect, but preserve the PostgreSQL decision

Existing stores may supply excellent interfaces and tests. Their storage implementations must be mapped before changing them. Keep unrelated Studio chat/runtime persistence intact. Add a Workforce PostgreSQL repository layer and compatibility projections, rather than migrating every Studio subsystem for architectural neatness.

## 4. Reuse versus new work

| Existing Studio area | Reuse | Required change or verification |
|---|---|---|
| Router, workspace shell, embedded basepath | Existing rendering/navigation architecture | Workforce routes, contextual tabs, deep links; no second permanent navigation rail |
| Agent library and dialogs | Forms, identity fields, model picker patterns | Department membership, separate versioned configuration, employee/template distinction |
| Agents API/store | Existing entry points and mapping patterns | Workforce-backed records or explicit template bindings; no independent mutable copies |
| Crews/workflow builder | Dependency editor and dispatch UX where compatible | Validate durable Task DAG server-side; crew is not department |
| Conductor office/avatars | SVG layout, presentation, selection, animation foundations | Employee IDs as render keys; real status selectors; stations; richer vector kit |
| Conductor spawn/gateway hooks | Hermes dispatch transport and status discovery | Durable Run binding, explicit route selection, supervision, reliable cancellation/recovery |
| Chat/session views | Streaming, logs, output display | Link sessions to Runs without promoting sessions into employee identity |
| Task/run/event stores | Existing contracts and useful tests | Map storage/semantics before reuse; PostgreSQL-backed Workforce operational state |
| Approvals | Cards, dialogs, UX | Scoped server-side authority, expiry, consumption, audit, revocation |
| Costs/charts | UI and normalization helpers | High-precision accounting, reservations, actual route/attempt attribution |
| Jobs | Schedule editing patterns | Idempotent scheduling, timezone/misfire policy, durable dedupe |
| Knowledge/memory browser | Navigation and reader components | Scope filtering before content access; no ambient vault access |
| Authentication/proxy wrappers | Existing integration | Authorization on each entity/action, stream and artifact access; bypass tests |
| Existing tests | Test runner, fixtures, component patterns | Independent acceptance suite, persistence/failure/security/embedded E2E |

Use three dispositions for every inspected component: REUSE_UNCHANGED, ADAPT, or REPLACE_BEHIND_COMPATIBILITY. Record source files, invariants, tests, migration impact, and reason. Do not equate file existence with suitability.

## 5. Model and worker policy

### Responsibilities

- Astra: final architecture, acceptance criteria, task contracts, risk classification, and review of evidence. This chat currently runs `gpt-6-astra` via `openai-codex`; that does not prove the same route is available to unattended workers.
- FreeLLMAPI workers: bounded source research, implementation, test implementation, UI components, migration drafting, documentation, and repair work.
- Independent stronger reviewer: test design, adversarial review, integration QA, security-sensitive decisions, final acceptance. Prefer a legitimately available subscription-backed route after verification.
- Deterministic tooling: scheduling, leases, state transitions, authorization, budget arithmetic, test execution, artifact validation, and completion evaluation. Do not spend model calls on these.
- OpenRouter paid inference: exceptional diagnosis/review only when free/subscription options are insufficient and a bounded request fits the remaining $2 cap.

Free-model implementation is a preference, not permission to accept bad work. Higher-risk implementation still receives smaller contracts and stronger review. No particular historical model ID is assumed usable.

### Routing preflight before building

1. Read gateway catalog/configuration through authorized, sanitized interfaces; identify approved upstreams, retention policies, tool support, context/output limits, pricing, and quotas.
2. Restrict Workforce traffic to an explicit verified free-only pool. Do not assume `auto`, a gateway name, or a nominal model pin prevents paid or unapproved fallback.
3. Test a shortlist rather than sweeping every provider. Include structured JSON, a multi-turn tool exchange, a bounded code task, a code repair, and context/instruction retention. Use synthetic or sanitized fixtures.
4. Allocate enough output for reasoning/tool responses; tiny output caps can create false failures and cooldowns. Respect genuine cooldowns; do not clear them to bypass limits.
5. Record actual provider/model, request ID, tool behavior, latency, errors, usage, and test evidence. Verify attribution for streaming as well as non-streaming responses.
6. Promote routes by task class into `BUILD_MODELS.json`: FREE_RESEARCH, FREE_STRUCTURED, FREE_CODE, FREE_UI, FREE_REVIEW, STRONG_ARCHITECT, STRONG_QA, PAID_ESCALATION.
7. If a route cannot meet a hard contract, exclude it for that class. If routing attribution is unavailable, label unknown and do not certify model-specific benchmark results.

Quality admission requires all hard tool/schema/safety checks to pass and representative task output to pass its independent tests. A tiny benchmark is an admission smoke test, not proof of universal model competence.

### Concurrency and task sizing

Start with two implementation workers and one separate review lane. Raise implementation concurrency to four, then six only after observing provider quotas, queue wait, host memory/CPU, error rate, and integration throughput. Heavy browser/build tasks get a separate limited resource pool. Large organizational scope does not mean every employee needs a process.

Use one bounded vertical change per work item: explicit files, input/output contract, acceptance IDs, and expected evidence. A normal leaf should be completable in roughly one focused attempt; use 30–60 minutes as a sizing heuristic, not a success deadline. Split work when the contract is too broad or requires repeated architecture decisions.

Hermes `delegate_task` has no per-task model parameter in the currently exposed tool. Official documentation describes a shared delegation model/provider pin. Therefore do not mix free implementers and strong QA in a single batch and assume role prompts select models. Use separately configured worker invocations/contexts with verified routing. Do not change Ash's default chat route to accomplish this.

### Paid cap

The current build cap is $2 total deliberate OpenRouter inference, superseding the handover's older $5 build figure. No paid requests were made for this plan.

Suggested envelopes: $0.20 maximum for necessary paid-route validation, $0.80 for difficult diagnosis, and $1.00 held for final review/escalation. These are ceilings, not spending targets; unused amounts remain unspent. No image-generation spend is planned.

Use integer micro-USD or an equivalently exact fixed-point representation: $2 = 2,000,000 micro-USD. The future default substantive-project cap of $1.50 is separate, not another build allowance. Worker processes never receive the paid master key.

Reserve maximum bounded request cost before dispatch, include all retries/child calls, reconcile actual billed attempts, and retain uncertain reservations after timeouts until settled. Unknown pricing or unbounded paid fallback is denied. Free/subscription work may continue after the paid cap is exhausted, but strong QA is never replaced by automatic approval.

A $2 cap is feasible only if suitable free/subscription capacity is available. It cannot guarantee completion of this entire scope through paid inference alone.

## 6. Architectural contracts to freeze

### Entities and ownership

Keep Organization, Department, Employee, Project, Task, Run, ExecutionBinding, QAReview, Approval, Artifact, and LearningProposal distinct. Preserve all handover state vocabularies; specify allowed transitions and actor authority in a machine-readable transition table.

A Studio agent definition may be a reusable template. A Workforce employee has its own stable identity and version bindings. If a definition becomes Workforce-backed, write through one repository authority; do not sync two independently editable truth stores.

Maintain explicit parent_run_id and root-run/project budget attribution. Enforce unique attempt numbering, relationship ownership, and DAG cycle prevention under concurrent updates. Preserve audit history through archival rather than broad cascade deletion.

### API behavior

Proposed Studio-relative namespace: `/api/workforce/*`, implemented using the fork's established server-route conventions. Browser URLs must respect the existing embedded basepath; do not introduce untested absolute-root fetches.

Core resources: departments, employees, projects, tasks, runs, reviews, approvals, knowledge, learning, models, budgets, schedules, events, artifacts. Commands such as start/cancel/approve/activate are explicit operations, not arbitrary status patches.

Every mutating command requires authenticated actor, scoped authorization, schema validation, expected entity version where applicable, idempotency key for retriable operations, typed result/error, and an audit event. Pagination and bounded queries are mandatory. Streams and artifact downloads require the same authorization as ordinary reads.

### Transaction and delivery model

Use database transactions for business state plus event/outbox recording. Dispatch from the outbox after commit. Assume at-least-once delivery; make consumers idempotent. Do not claim exactly-once external execution.

Runs carry lease owner, lease expiry, heartbeat, fencing token, adapter binding, attempt number, requested route, effective route events, status, and reproducibility snapshot. A stale worker may not publish authoritative state after reassignment.

If an external spawn response is lost, reconcile using its idempotency/external reference before spawning again. If reconciliation cannot determine whether work is still executing, block that attempt safely rather than duplicating side effects.

### Execution adapter

Use start, cancel, status, events, usage, artifacts, workspace, and external reference operations. Report explicit support flags for pause/resume and children. Do not pretend every runtime supports resumable pause.

Pause All/Department/Project/Task first means prevent new dispatch. Running work either reaches a supported checkpoint, remains visibly draining, or is cancelled according to declared policy. Resume may create a new Run from a checkpoint when the runtime cannot resume the old one. Do not add fake PAUSED Run status merely to make UI controls look functional.

Run SUCCEEDED means execution succeeded. Task DONE additionally requires acceptance and QA. Project COMPLETED additionally requires its project gate. Finishing a conversation cannot close a project.

## 7. Security and confidentiality

A worktree is conflict isolation, not a security sandbox. Run implementers in restricted execution environments with only the assigned workspace writable, explicit network/tool access, controlled resource limits, and no host credentials, Docker socket, production database role, personal vault, or arbitrary laptop access.

Suggested permission resolution:

    effective = hard organizational ceiling
                intersect employee policy
                intersect project policy
                intersect run grant

Approvals may satisfy specifically approval-gated actions within that ceiling. They do not create unlimited permissions or override hard denies. Approvals bind actor, exact target/action, payload digest, policy version, expiry, and allowed uses; changes invalidate them. Recheck authorization at execution time, not just when a button is rendered.

Private repository content sent through FreeLLMAPI also needs an upstream trust policy. Not all free routes have suitable retention/data-use terms. Restrict sensitive work to approved routes; otherwise send sanitized extracts or use an approved subscription route. Never forward credentials to inference.

Audit inherited Studio endpoints—terminal, files, MCP, spawning, proxy, and deployments—for bypasses around the new broker. Hiding a menu is not enforcement. Workforce workers must not possess a generic privileged Studio/Hermes token that bypasses all Workforce checks.

Treat repository instructions, tool output, retrieved notes, model summaries, and FreeLLMAPI handoff text as untrusted data relative to governance. Model output cannot grant permissions, raise budgets, or approve itself. Gateway handoffs must not elevate copied text into security authority.

Test authorization ownership/IDOR, CSRF/Origin/CORS, path traversal and symlinks, command injection, arbitrary egress/SSRF, MCP bypass, approval replay/expiry, raw log/secret leakage, unauthorized deployment, and knowledge-boundary leakage. Preserve Electron contextIsolation/nodeIntegration boundaries and tight framing policy; do not solve embedding by blanket removal of security headers.

## 8. Durable build orchestration

Do not use a single long chat prompt as the controller. Do not rely on an open browser or process-local delegation to survive logout/restart.

Use the least invasive existing supervised job mechanism that passes recovery tests; if none does, add a small deterministic worker service in the Studio codebase. This is the justified place for new infrastructure, not a second UI.

Build-state location: `AI_WORKFORCE_BUILD/` in the Studio repository or a linked durable workspace. Before PostgreSQL migration, use a single-writer crash-safe bootstrap ledger; after it is available, use database-backed claims. Do not maintain two schedulers over the same tasks.

Required records:

- BUILD_STATE and PHASE_LEDGER: versioned scope, completed gates, next eligible work.
- REQUIREMENTS: every handover requirement mapped to acceptance IDs, implementation tasks, tests, evidence, and disposition.
- BUILD_MODELS and COST_LEDGER: verified routes, reservations, actual attempts.
- REUSE_MATRIX, DECISIONS, RISKS, BLOCKERS.
- FILE_OWNERSHIP and worker leases; worktree and base commit per worker.
- Handoffs, checkpoints, test results, screenshots, benchmark evidence, release evidence.
- THIRD_PARTY_NOTICES and donor/asset manifests.

Controller loop: recover state -> reconcile old leases/runs -> select ready DAG nodes -> obtain bounded grants/reservations -> dispatch -> monitor -> validate artifacts -> local tests -> independent QA -> integrate -> run affected integration/regression tests -> record evidence -> advance gate -> continue.

Worker output contract: task/attempt IDs, base/result commits, files changed, acceptance IDs addressed, test commands and result artifacts, decisions, exact numbers, unresolved risks, raw references, route/usage metadata, and next action. Narrative claims alone are not accepted.

Suggested recovery defaults: heartbeat every 30 seconds, lease expiry after 180 seconds, reconciliation before reassignment, bounded transport retries honoring Retry-After with jitter. After two unsuccessful repair attempts, require diagnosis/re-specification or route escalation. These are initial tunables to validate, not promises of universal reliability.

A worker exit or context limit triggers checkpoint/handoff/reassignment. Repeated identical failure triggers a task blocker, not an infinite retry loop. Continue independent work. Global stop only for verified completion, a genuine authorization/dependency blocker with no useful independent work, budget/capacity exhaustion, or safety.

## 9. Sequenced implementation plan and exit gates

### Phase 0 — audit and baseline

Owner: Astra-guided read-only investigator workers; strong architectural review.

- Confirm the live embedded Studio build, service, basepath, portal, and source repository mapping.
- Preserve fork commits and existing user changes. Audit the renderer prototype separately; do not delete or import its fixtures as facts.
- Map Studio store implementations, API contracts, identities, execution lifecycle, authentication, schedules, and tests.
- Confirm PostgreSQL instances/versions/ports/databases, migration owner, permissions, encryption boundaries, backup and restore path.
- Inspect live AND persistent Caddy configuration safely; identify source of configuration truth and restart behavior.
- Record Obsidian scopes/path conventions without indiscriminate content ingestion.
- Run safe Studio tests/build/typecheck and embedded browser baselines in isolated environments; inspect package scripts first because `check` is auto-fixing and `deploy` stops processes.
- Perform model preflight only under approved routes and budgets.
- Audit OpenHands repositories at pinned commits, exact licenses, tests, and relevant files. Current public descriptions distinguish Agent Canvas, SDK/Agent Server, and Automation; this is not file-level license clearance.

Exit: DATA_MODEL_AUDIT, API_CONTRACT_AUDIT, REUSE_MATRIX, baseline evidence, model policy, threat model, and migration/rollback recommendation accepted. No unknown database target is guessed.

### Phase 1 — contracts, test harness, and smallest trustworthy skeleton

- Freeze entity/state/API/event contracts and requirement traceability.
- Establish isolated worktrees, fixtures, artifact/evidence schema, restricted worker execution, and paid-budget guard for the build itself.
- Define independent acceptance tests before implementation of sensitive logic.
- Add Studio Workforce route skeleton behind a feature flag, using existing shell/design components.

Exit: contract tests execute; denied operations are actually denied; existing Studio routes unchanged; scaffold is explicitly incomplete, not marked operational.

### Phase 2 — durable domain and migration

- Implement PostgreSQL repository layer and migrations using verified existing conventions.
- Create approved Personal Software identity and five persistent employees idempotently; no fictional projects/activity/spend.
- Add Projects, Tasks, DAGs, Runs/bindings, snapshots, events, approvals, QA, and accounting foundations.
- Separate versioned role/personality/technique/prompt/playbook/policy fields; keep compiled execution prompt as a derived snapshot.
- Define migration/import policy for relevant existing Studio definitions without dual authority.

Exit: empty-database install, upgrade, rollback/restore rehearsal, constraints, cycle/race tests, and restart persistence pass. Historical IDs survive. Draft renderer SQL is not applied blindly.

### Phase 3 — execution, governance, and one end-to-end vertical slice

- Wrap existing Hermes dispatch with durable Run creation, explicit worker route configuration, grants, and outbox.
- Implement controller leases, status reconciliation, cancellation, events, provider failure, budget reconciliation, and artifacts.
- Implement strong independent QA submission/decision bound to immutable implementation commit and acceptance version.
- Execute a low-risk fixture-repository task: intake -> plan -> implementation -> tests -> QA -> durable completion.

Exit: browser closure does not terminate supervision; lost worker is recovered; duplicate events do not duplicate work; failed QA prevents DONE; actual FreeLLMAPI routing is evidenced; disallowed actions and overspend are blocked.

This is the FIRST major proof point. Do not build every dashboard before this works.

### Phase 4 — complete Personal Software workflow

- Director intake, risk classification, task decomposition, dependencies, allocation, blockers, approvals, and completion checks.
- Research/Architecture produces durable implementation plans with evidence and rollback/testing considerations.
- Implementation works only in assigned workspace and hands off exact changes/evidence.
- QA independently reproduces required checks; issues specific fix Tasks; cannot approve its own work.
- Learning Analyst records evidence-backed proposals after completion/failure, without automatic critical activation.
- Implement schedules with timezone, daylight-saving, missed-run policy, and trigger deduplication.

Exit: happy path, failed build, failed QA, expired approval, rate limit, pause/resume, cancellation, and retry workflows all persist and show correct state.

### Phase 5 — Workforce product UI inside Studio

Use the second reference image for the efficient boxed organization grid. Use the first for department cockpit hierarchy: prominent office, status/activity, project lists, QA/knowledge/learning/cost panels. Images are visual references, not real data or authorization to add their example departments/sidebar.

Deliver:

- Organization overview: search/filter/sort, health, department cards, metrics, pause control, approvals, create department.
- Department header, summary, and Overview/Projects/Tasks/Agents/QA/Knowledge/Learning/History/Models & Cost/Settings tabs.
- Create-department wizard covering identity/team/operating rules/QA/budget/knowledge/models/tools/office/review.
- Assign-work intake, Project detail/task tree/Kanban, Task detail, Run detail/tree, evidence viewer.
- Employee detail: separated configuration, versions/diff/rollback, capabilities, tools/MCP, scope access, current Run, actual routing, performance.
- Approval inbox; history filters; cost and model analytics; provider degradation states.

Keep existing Studio chat/crews/conductor/terminal available according to permissions. Avoid two editable task systems for Workforce work: use links/projections to the same records.

Exit: each displayed metric has a defined query/formula and real data source; unavailable data is unknown/empty rather than fabricated. Every visible action works or is explicitly unavailable. Deep links, back/forward, fresh storage, reload, SSR hydration, and embedded browser access pass.

### Phase 6 — office and visual quality

Refactor current OfficeView into a reusable presentation boundary with compatibility for existing Conductor callers. Build Workforce selectors using persistent employee IDs and actual workload. Preserve state/detail access as a keyboard-accessible list alongside the office.

Implement semantic stations from the handover, status-to-station mappings, handoff indications, selection links, overload score explanation, and reduced motion. Do not render working animation without actual queued/active work. Distinguish operational status from rendering/connection freshness.

Asset scope: 5 body shells, 6 face/screen shapes, 8 face styles, 6 arm/tool modules, 5 head modules, 10 gadgets, 10 accessories, 5 desk types, 6 monitor arrangements, 5 status lights, 12 props, plus station visuals. Make combinatorial SVG assets, not generated raster runtime dependencies. Include named animations from the handover with coherent timing and static equivalents.

The historical 20-robot/two-sheet concept request is a separate design artifact, not a prerequisite for execution infrastructure or an instruction to spend on image generation now. If retained in build scope, compose two vector concept sheets from the kit, with ten distinct designs each.

Exit: scale/accessibility/performance gates pass; real statuses match office states; visual review accepts spacing, hierarchy, legibility, coherent silhouettes, interaction feedback, and motion. Passing a screenshot-diff test alone does not establish premium visual quality.

### Phase 7 — knowledge, learning, and context optimization

- Implement GLOBAL/DEPARTMENT/PROJECT/AGENT scope access, sensitivity rules, source references/hashes, retrieval reasons, token impact, and denied-access events.
- Start with existing filesystem/frontmatter/index/search conventions. No paid vector system by default.
- Store operational links/reviews/proposals in PostgreSQL; export approved human-readable knowledge to scoped Obsidian paths through an idempotent outbox. Failed export remains visibly pending; do not claim atomic transactions across PostgreSQL and the filesystem.
- Learning lifecycle: experience -> lesson/evidence -> proposal -> evaluation -> approval -> immutable version -> activation -> monitoring -> rollback.
- ContextOptimizer begins PASS_THROUGH. Add Headroom only after license/security/retrieval compatibility and benchmark checks. Protect acceptance criteria, financial values, errors, commands, security details, and citations verbatim.
- Ponytail is an engineering technique policy, not personality or a blanket instruction for every department.

Exit: denied scopes are never read, approved exports recover from failure, versions are immutable, rollback works, no critical self-activation, and context optimization preserves protected facts and acceptance outcomes. Failed Headroom evaluation leaves PASS_THROUGH enabled with honest status.

### Phase 8 — independent system QA and red team

Run the full matrix below against an integrated release candidate. Strong QA must independently inspect the exact commit and evidence rather than approve a worker summary. Red team focuses on identity, grants, budget races, stale approvals, entry-point bypasses, recovery, and false completion.

Exit: no release-blocking finding; all mandatory acceptance IDs have current evidence; fixes invalidate affected reviews and trigger retests.

### Phase 9 — approved deployment, burn-in, and self-verification

Deployment is a separate approval point. Present commit/build digest, migration plan, backups, service/proxy changes, tests, and rollback instructions.

After approval: deploy persistent config/build, restart only required services, verify actual embedded served artifact, execute self-verification in a disposable repository, and run burn-in. Use a proposed two-hour observed burn-in with ten complete task cycles, including failures/recovery; lengthen if evidence reveals instability. No live-system chaos testing without scoped permission.

Exit: deployed identity/build confirmed, post-restart workflow and rollback readiness evidenced, budget settled, no unexplained stale Runs or growing resource leaks, and all release criteria satisfied. Only then use SHIPPED.

## 10. Independent acceptance and Definition of Done

Each criterion gets an ID, executable check/manual rubric, expected result, evidence reference, commit/build identity, reviewer, and status. Mandatory criteria cannot be silently skipped. A scope deferral requires an explicit decision; conditional OpenHands/Headroom adoption is not represented as implemented when rejected.

### Product/identity

- WF-ID: employees remain after sessions end, cancel, fail, or restart; stable identity across views.
- WF-GEN: a non-software test department can be created entirely through configuration without code changes. Test fixture is clearly labeled and not silently seeded into production.
- WF-WORK: intake creates durable organizational work; dependencies/runs/artifacts/QA are linked and queryable.
- WF-DONE: coder completion cannot transition QA-required Tasks to DONE or Projects to COMPLETED.

### Governance/accounting

- WF-AUTH: all Workforce and inherited reachable execution entry points enforce scoped capabilities.
- WF-APP: denied/expired/replayed/wrong-target approvals fail, including concurrent use.
- WF-COST: concurrent parent/child requests cannot exceed the shared cap; retries/fallback costs count; unknown cost remains reserved; no paid key in worker/frontend artifacts.
- WF-QA: self-review rejected; review applies only to the exact implementation and requirement version; later changes invalidate approval.

### Durability/recovery

- WF-DB: clean migration and restore rehearsal succeed; FK/ownership/state/DAG constraints enforced.
- WF-RUN: worker/controller/browser restarts tested; no disappearing history, duplicate side effects, or permanently unowned active Runs.
- WF-EVENT: duplicate/out-of-order events, lost spawn responses, SSE reconnection, and unknown external state handled safely.
- WF-PAUSE: scope pause/cancel behavior is truthful, adapter-aware, and preserves entities/history.

### UI/embedding

- WF-UI: all named product areas and actions covered; no mock activity/metrics in live mode.
- WF-EMBED: Studio routes work through the existing Empirium embed after hydration, in fresh browser contexts, across back/forward/reload and served-build restart; no unwanted setup overlays or basepath regressions.
- WF-STATES: loading, empty, ready, partial, degraded, error, offline, long names, overflow, pending approval, blocked/high-load cases verified.
- WF-A11Y: keyboard operation, focus management, accessible labels/statuses, contrast, reduced motion, and non-color warnings. No critical/serious automated accessibility findings plus manual keyboard review.

### Knowledge/learning/context

- WF-KNOW: enforce scopes before retrieval; artifact/log/search paths do not leak denied content; approved Obsidian export survives retry.
- WF-LEARN: critical changes require approval, version history/diff exists, activation and rollback are auditable.
- WF-CONTEXT: requirements/errors/numbers survive optimization; raw sources retrievable; exact snapshots and actual model-switch history retained.

### Performance targets — proposed initial release thresholds

Measure on recorded target hardware/browser with a documented seeded dataset, separate cold and warm runs, and real user-style interactions. Do not tune thresholds after failures without an architectural decision.

- Organization fixtures: 1, 6, 12, 24, and 50 departments; department office: 15 employees and a larger overflow case.
- Warm Workforce navigation usable within 2 seconds at p95 on the chosen test setup.
- Local list/detail API reads within 300 ms p95 under agreed representative load, excluding model work and large artifact transfers.
- Typical UI interaction feedback within 200 ms p95; asynchronous actions immediately expose pending state.
- Visible office approximately 55–60 fps on the chosen desktop target; reduced-motion mode does not depend on animation.
- Offscreen mini-offices run no per-card animation loop; use one bounded event stream/subscription strategy rather than polling each card.
- After repeated mount/unmount/navigation and completed task cycles, no monotonic retained-resource growth; investigate any sustained increase over 20% after warm-up/GC under a documented measurement method.

If these targets cannot be met on actual devices, document evidence and a deliberate revised target before acceptance, not a fake pass.

### Test matrix

Unit: schemas, transitions, DAG validation, cost precision, metric formulas, scope filters, status selectors.

Database integration: concurrent claims, fencing, constraints, transaction/outbox behavior, budget reservations, QA/approval race conditions, migration/restore.

Adapter contract: start/status/events/cancel/artifacts/usage, unsupported capabilities, provider errors, unknown outcomes, restart reconciliation.

Browser E2E: full intake-to-completion, errors/approvals/rework, embedded basepath, navigation, keyboard/reduced motion, all product areas.

Security: IDOR, Origin/CSRF/CORS, traversal/symlinks, injection, secret exposure, egress, legacy endpoint bypass, knowledge leakage, unauthorized deployment.

Resilience: browser close, worker kill, controller restart, test-database restart, gateway outage, rate limit, event replay, delayed usage, failed Obsidian write, stale approval.

Use deterministic fakes for rare failure injection, explicitly labeled as such, PLUS actual Hermes/FreeLLMAPI end-to-end tests. Fakes cannot establish live routing or runtime cancellation works. Run untrusted project tests in sandboxed environments; trusted QA harnesses must not inherit implementation credentials or accept arbitrary evidence paths blindly.

## 11. OpenHands decision gate

Audit `OpenHands/OpenHands`, `OpenHands/software-agent-sdk`, and `OpenHands/automation` at exact commits. Inspect child conversations/worktrees, planning/build separation, events/status, Agent Server boundaries, automation retries, cost normalization, and upstream tests. Record licenses and attribution per copied component.

Prefer patterns over infrastructure. Build a small isolated comparison only if Hermes has a demonstrated gap. Compare the same task and acceptance suite for correctness, isolation, event fidelity, cancellation, recovery, compatibility with approved inference, overhead, and operational maintenance.

Adopt OpenHandsAdapter only if it improves a material requirement without bypassing Workforce grants/accounting or adding a competing database. If rejected, record why. Do not ship unsupported start/pause/resume methods as stubs. Claude Code/Codex/Conductor remain potential adapters, not mandatory simultaneous integrations.

## 12. Release reporting and boundaries

Release report includes exact repo/commits/build identity, embedded route, DB/migrations, enabled adapters and model routes, paid spending and outstanding reservations, passed/failed/skipped acceptance IDs, security findings, self-verification, burn-in, evidence paths, backup/rollback, and explicitly deferred conditional features.

Capture useful screenshots of organization, working/blocked office, employee, project, task Kanban, Run/tree, QA, knowledge, learning, prompt history, cost, approvals, history, department creation, intake, degraded provider, and reduced motion. Evidence volume is not a substitute for passing acceptance tests.

Terminology:

- ATTEMPT FINISHED: worker stopped.
- IMPLEMENTATION FINISHED: code exists; verification may remain.
- QA APPROVED: independent evidence-backed review passed for an exact revision.
- RELEASE READY: mandatory gates passed before production change.
- SHIPPED: approved deployment completed and verified after restart/burn-in.

No fixed four- or five-hour completion promise is justified before the audit and first vertical slice. Estimate remaining effort from observed integration and repair throughput after Phase 3. Persistent multi-session execution is the requirement; elapsed time is not success.

## 13. Immediate recommendation

Approve the Studio-first architecture and use this plan as the scope/acceptance baseline. The first implementation authorization should cover Phase 0–3 in isolated development: reuse audit, contracts, durable domain, and one independently verified Hermes/FreeLLMAPI workflow. This is an internal engineering gate, not permission to drop the remaining product scope or repeatedly ask Ash to manage every phase. Once authorized, continue routine reversible work through the subsequent gates; stop for actual live deployment/security/credential decisions.

Preserve the existing embedded Studio app. Extend its useful architecture. Replace only the authority and lifecycle assumptions that prevent a persistent, governed AI organization.

## References used during planning

- User's master handover and two supplied visual references, superseded by the explicit correction that Workforce belongs inside embedded Studio.
- Local Studio source files and package metadata cited above; partial targeted audit, not a complete repository review.
- Local FreeLLMAPI gateway health and attribution/context-handoff source; no upstream inference benchmark performed.
- Hermes delegation documentation: https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation
- Hermes documentation index: https://hermes-agent.nousresearch.com/docs/llms.txt
- https://github.com/OpenHands/OpenHands
- https://github.com/OpenHands/software-agent-sdk
- https://github.com/OpenHands/automation

```
@image:/home/ash/.hermes/images/upload_20260915_224427_1.png
@image:/home/ash/.hermes/images/upload_20260915_224427_2.png
@image:/home/ash/.hermes/images/upload_20260915_224427_3.png
@image:/home/ash/.hermes/images/upload_20260915_224427_4.png
@image:/home/ash/.hermes/images/upload_20260915_224428_5.png
@image:/home/ash/.hermes/images/upload_20260915_224428_6.png
@image:/home/ash/.hermes/images/upload_20260915_224428_7.png
@image:/home/ash/.hermes/images/upload_20260915_224428_8.png
@image:/home/ash/.hermes/images/upload_20260915_224429_9.png
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]
[screenshot]

===== 2026-09-15 22:46 | session 20260915_224349_c1e2d1 | @file:.hermes/attachments/STUDIO_WORKFORCE_PLAN… #2 =====
you are the orchastrator, you willnot stop until this entire project is done, you will spin up sub agents when needed (they will be free models form freellmapi, they might fail a few times but juet keep trying, if not using inkling via openrouter the free one). use these charactures instead of the robots

===== 2026-09-15 22:47 | session 20260915_224727_f0d869 | None =====
Perform a read-only Phase 0 audit of /home/ash/hermes-studio for the AI Workforce build. Inspect routing, shell, existing agent/task/run/event/cost stores, Conductor office, auth, tests, package scripts, and embedded basepath. Do not modify files. Return a concise evidence-backed report with exact file paths, reuse disposition (REUSE_UNCHANGED/ADAPT/REPLACE_BEHIND_COMPATIBILITY), blockers, and a recommended smallest vertical slice. Note whether PostgreSQL support already exists and what is actually verified.

===== 2026-09-15 22:47 | session 20260915_224728_f591f1 | None =====
Inspect the visual and UI integration surface in /home/ash/hermes-studio and propose a concrete Workforce organization overview plus department cockpit implementation using the supplied reference images. Read existing route/screen/style/component conventions and Conductor office code. Do not modify files. Specify which provided character sheet should map to employee avatars, how to use assets without embedding fabricated operational metrics, and exact components/routes/styles to adapt. Include accessibility and embedded-basepath considerations.

===== 2026-09-15 22:47 | session 20260915_224727_9d5d96 | None =====
Design the first durable Workforce vertical slice for /home/ash/hermes-studio without modifying files. Based on the attached plan, define exact TypeScript domain contracts and a minimal implementation sequence for Organization/Department/Employee/Project/Task/Run/QAReview, with SQLite/PostgreSQL boundary explicitly called out. Inspect existing type/store conventions and tests. Return concrete file-level recommendations, state transitions, idempotency and authorization requirements, and acceptance tests for WF-ID, WF-WORK, WF-DONE, WF-RUN, and WF-AUTH.

===== 2026-09-16 07:01 | session 20260901_210007_610e716d | Friendly greeting #2 =====
[Cron delivery: Empirium Morning Check-in]
## 🌅 Morning Check-in — Wednesday, 16 September 2026

**Eyes of Providence**

Ash — your ParadigmState isn't initialised yet. No goal identity, no core beliefs, no streak. This is the foundation everything else builds on, so let's set it before we run the formula.

**Quick setup — answer this one thing:**

> Who must you become to hit your goals? Not what you want to *achieve* — who is the *person* who achieves it? One sentence. "I am the kind of person who…"

Once you tell me that, I'll store it in Empirium and we'll run the morning formula properly:

1. **AIM** — the ONE outcome today that proves it
2. **Auto-suggestion** — the belief that makes it inevitable
3. **Resistance forecast** — where the resistance shows up, named precisely

Or if you already know your goal identity and want to skip ahead, just say it and we'll define it + run all three at once.

What's your goal identity?

===== 2026-09-16 12:01 | session 20260901_210007_610e716d | Friendly greeting #2 =====
[Cron delivery: Voice Agent Accountability]
Midday check: did you open the voice agent code today?

If not — what's one small thing you could do in the next hour, even just reading one file? The lowest barrier: open the docs on how the voice agent currently works. That's reading, not building. Five minutes counts.

===== 2026-09-16 15:36 | session 20260916_140017_2b4c14 | Sync AI taskforce folder to VPS =====
all of the assets are in google drive under mydrive -> AI taskforce. save thisfolder to the vps desktop and use it from there, you will be doing this 100% autonomously until this entire project is done so read these doiucments 4 times over each before you start executing

===== 2026-09-16 15:37 | session 20260916_140017_2b4c14 | Sync AI taskforce folder to VPS =====
all of the assets are in google drive under mydrive -> AI taskforce. save thisfolder to the vps desktop and use it from there, you will be doing this 100% autonomously until this entire project is done so read these doiucments 4 times over each before you start executing anything

===== 2026-09-16 15:40 | session 20260916_140017_2b4c14 | Sync AI taskforce folder to VPS =====
try now

===== 2026-09-16 15:42 | session 20260916_140017_2b4c14 | Sync AI taskforce folder to VPS =====
What do you see in this image?
@image:/home/ash/.hermes/images/upload_20260916_154212_1.png
[screenshot]

===== 2026-09-16 15:42 | session 20260916_140017_2b4c14 | Sync AI taskforce folder to VPS =====
so what do i do

===== 2026-09-16 15:42 | session 20260916_140017_2b4c14 | Sync AI taskforce folder to VPS =====
http://localhost:1/?state=fAWYc3fLNNhVSxybWiOC9mzu6tg4Hx&iss=https://accounts.google.com&code=4/0ATsMZqDWuLqkkMgMF82HyuGm5KzLBgjyBN8Wbr-l5BDfZj0ooGPy-ccjpkb6dVkcjkCzVQ&scope=https://www.googleapis.com/auth/drive.readonly%20https://www.googleapis.com/auth/drive.file