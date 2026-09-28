# EMPIRIUM STUDIO / AI STAFF FORCE — COMPLETE CONTEXT DOSSIER
## Compiled 2026-09-16 for independent Astra review

This dossier is the authoritative reconstruction of the user's stated ambitions, corrections, constraints, rejected approaches, visual goals, autonomy requirements, model strategy, and product philosophy for the AI staff-force project. It is intended to be supplied together with the current Hermes master prompt to an independent high-capability reviewer.

---

# 1. THE CORE AMBITION

The user wants a **visible, persistent, departmental AI workforce**, not merely a chat UI, not merely a collection of ephemeral subagents, and not merely a dashboard that claims agents exist.

The intended experience is a **living digital company**:

- permanent departments;
- permanent named AI employees;
- project-specific temporary crews;
- temporary subagents where useful;
- visible current work and background work;
- real tasks, runs, errors, reviews, approvals, costs, models and histories;
- a high-quality 2D animated office showing what the agents are actually doing;
- the ability to click an agent and understand or interact with it;
- long-running autonomous project execution that continues on the VPS without an open browser;
- strong planning/architecture/QA, with the bulk of coding and repetitive work delegated to free models;
- continuous review/rework until explicit Definition of Done gates are met.

The goal is not a demo. The goal is a **working personal AI company / AI workforce operating environment**.

---

# 2. CURRENT PRODUCT BOUNDARY — IMPORTANT CORRECTION

The user has now **separated Empirium OS from the AI workforce product**.

Empirium OS remains the user's personal operating system / personal software.

The AI workforce should now live in a **standalone heavily customized Hermes Studio fork**.

The user explicitly decided to keep these products separate rather than embedding Hermes Studio inside Empirium OS.

Therefore:

- DO NOT modify Empirium OS for this project.
- DO NOT embed the new workforce back into Empirium OS as its implementation home.
- DO NOT create a third unrelated workforce application.
- The target product should be a personal fork/evolution of Hermes Studio.

The user likes the idea of **two Hermes Studio clones/repositories**:

1. **Stable Control Studio** — known-good Hermes Studio used to run and observe the build.
2. **Target Empirium Studio** — separate clone/fork modified aggressively into the new product.

The stable control copy should not be modified by coding workers during the build.

---

# 3. WHY HERMES STUDIO IS THE FOUNDATION

The user has concluded that Hermes Studio already provides much of the execution machinery they want and should be treated as the engine/foundation rather than replaced.

Relevant concepts already present in or around Hermes Studio/Hermes include:

- Agent Library;
- custom system prompts;
- role labels;
- per-agent model overrides;
- tags;
- profile-scoped workspaces;
- Crews;
- Conductor;
- workflows/DAGs;
- tasks/Kanban-like views;
- jobs/cron;
- chat/session inspection;
- terminal;
- tools and MCP management;
- approvals;
- live activity;
- cost/usage displays;
- logs/audit/history;
- memory/knowledge;
- gateway integration.

The user does **not** want these reinvented without reason. The project should inspect the installed versions, reuse sound functionality, adapt what is coupled to old assumptions, and replace only what cannot support the new product.

---

# 4. DEFINITIONS THE PRODUCT MUST KEEP DISTINCT

These concepts must not be collapsed into one another.

## Organization
The whole visible AI company.

## Department
A permanent organizational container with purpose, staff, memory, rules, tools, model policies, projects, history, cost and QA information.

## Employee
A persistent named AI worker with identity that survives sessions and individual tasks. The employee has versioned configuration and can accumulate history, performance and learning data.

## Studio Agent Definition / Hermes Profile
Reusable execution configuration that may back an employee, but is not automatically equivalent to the employee's organizational identity.

## Crew
A temporary or reusable **execution team** assembled for a shared project/SOP. A department is not a crew. The same persistent employees may participate in different crews.

## Conductor Mission
Temporary mission orchestration / ephemeral worker coordination. Conductor is useful for missions and visualization but should not define the permanent organizational structure.

## Temporary Subagent
A short-lived worker spawned for bounded work. If represented in the office, it should look visibly temporary/contractor-like and may disappear after completion.

## Project
Durable user intent with tasks, dependencies, runs, reviews, artifacts, costs and completion gates.

## Task
Bounded work item assigned to a worker/profile.

## Run
One concrete execution attempt, with exact model/provider, status, logs, artifacts and usage.

## Review / QA
Independent acceptance of the exact revision/artifact against explicit criteria. The implementer cannot self-approve.

## Learning Proposal
Evidence-backed suggested improvement to prompts, models, skills, memory or operating process. Critical changes do not self-activate.

---

# 5. FIRST PERMANENT DEPARTMENT — PERSONAL SOFTWARE

The first explicit department is **Personal Software**.

Its purpose is to build, maintain and improve the user's personal software systems.

The default permanent employee set previously agreed for this department is:

## Director
- department orchestrator;
- accepts work;
- clarifies goal/risk;
- plans/decomposes;
- allocates work;
- monitors progress/blockers;
- checks that review gates exist;
- communicates status;
- does not casually become the main coder.

## Research Architect
- investigates the repo and relevant technologies;
- turns requirements into implementation plans;
- makes architecture decisions;
- identifies risks/dependencies;
- creates rollback/testing strategy;
- supplies evidence to implementers.

## Developer / Implementation Engineer
- performs bounded implementation;
- works in isolated workspace/worktree;
- runs local tests;
- returns exact evidence;
- does not self-approve.

## QA Engineer
- independently reproduces acceptance requirements;
- runs automated and browser tests;
- searches for regressions;
- requests precise changes;
- gates acceptance of implementation.

## Learning Analyst
- examines completed/failed work;
- extracts lessons;
- monitors agent/model performance;
- proposes prompt, skill, routing, memory and workflow improvements;
- writes institutional knowledge;
- does not silently activate critical changes without review/approval.

Future departments should be configurable rather than hard-coded.

---

# 6. EMPLOYEE CONFIGURATION / PERSONALITY AMBITION

The user wants employees to feel individual and inspectable.

Each persistent employee should eventually have separately editable/versioned fields such as:

- name;
- department;
- role title;
- role responsibilities;
- routing description;
- personality;
- communication style;
- system prompt / SOUL;
- techniques/playbooks;
- skills;
- tools;
- MCP servers/tool filters;
- model policy / primary model / fallbacks;
- reasoning effort where supported;
- memory scope;
- knowledge scope;
- permission policy;
- approval requirements;
- project/task history;
- current run;
- performance/evaluation history;
- model/cost history;
- learning proposals;
- visual skin/outfit;
- preferred workstation / department visual role.

Prompt/personality changes should be versioned, diffable and rollbackable.

The employee identity must not disappear simply because a chat/session ends.

---

# 7. ORGANIZATION OVERVIEW — USER EXPERIENCE

The user supplied a mockup showing the desired high-level experience.

The exact pixels are not sacred, but the **function, density, clarity and premium quality bar are**.

The overview should make the organization immediately legible, with things such as:

- organization title and health/status;
- number of active agents;
- departments online;
- current spend;
- active projects;
- pending improvements;
- department cards;
- miniature visual department offices;
- per-department agent count;
- per-department project count;
- per-department spend where truthful;
- QA/health signal where meaningfully defined;
- organization activity feed;
- model/API spend by department;
- recent improvements;
- create-department path;
- search/filter/sort if useful.

The user wants to be able to **step back and see the whole company**, then click into a department/room.

---

# 8. DEPARTMENT COCKPIT — USER EXPERIENCE

The department mockup establishes the desired hierarchy:

- global/application navigation;
- department header;
- purpose/status;
- department tabs;
- large central office visualization;
- named visible employees;
- right-side status/activity rail;
- active projects;
- upcoming work;
- completed work;
- QA information;
- knowledge;
- learning/improvements;
- model/cost information.

The user explicitly rejected sparse, low-information dashboards made of a few generic cards and large dead areas.

The result should feel polished, intentional and dense — closer to a premium command center than a CRUD admin page.

---

# 9. THE LIVING 2D OFFICE — CENTRAL AMBITION

The user explicitly chose **2D rather than 3D** to reduce complexity and system load.

The office must be a real, interactive 2D visualization driven by real agent state — not a decorative static generated image.

The user wants little AI characters/robots who:

- are visibly alive;
- are never unnaturally frozen;
- wander, shift, gesture or perform ambient movement when idle;
- move to workstations/tools when working;
- look busy while doing real work;
- look frustrated when encountering errors;
- look frightened/scared/confused when a worker crashes or times out;
- become more urgent/attention-seeking when they need the user;
- can visibly hand work to another agent;
- may converse with one another when delegation/handoff occurs;
- celebrate briefly when finishing;
- visually distinguish rate-limit waiting from genuine error;
- return to calmer ambient behavior after work ends.

If an agent needs approval/attention, the user should be able to notice it visually and click the character.

Characters should **always have some motion**, including subtle idle loops, breathing/bobbing, eye changes, looking around, device checking or small roaming.

The motion must remain bounded and readable rather than chaotic.

---

# 10. CHARACTER BANK / VISUAL IDENTITY

The user has created many robot character concept sheets.

The final product should support a **bank/roster of character appearances** that can be assigned to employees.

Requirements:

- many appearances can reuse the same behavior/animation rig;
- unique behavior per costume is not required;
- different outfits/skins are valuable;
- the user should be able to assign/swap skins;
- visual role identity should be clear;
- the character system should be extensible with new skins later;
- appearance should be separated from behavior;
- expressions should be separately controllable where practical;
- runtime should not require expensive generated images every frame.

The user likes the small, expressive, charming robot style demonstrated in their concept sheets.

---

# 11. THE MISADVENTURES OF TRON BONNE / SERVBOT INSPIRATION

The user owns the physical disc and has supplied a ROM/disc archive for private personal experimentation.

They are particularly interested in the way Servbots:

- move around;
- idle;
- turn;
- talk/interact;
- become frustrated;
- look frightened or alarmed;
- express urgency;
- feel like a little workforce/society.

The preferred engineering approach is clean-room behavioral/asset-format study rather than relying on leaked source code.

The final runtime remains 2D.

Possible R&D paths include:

- study the supplied disc filesystem;
- extract standard PS1 media where possible;
- inspect model/texture/animation containers;
- observe behavior in an emulator;
- document motion timing/state transitions;
- if useful, pre-render extracted 3D animation into 2D sprites;
- alternatively recreate the behavior on original Empirium robot art;
- isolate any proprietary extracted assets so they can be removed/replaced without changing application code.

The user values the behavior/interaction language more than literal dependence on Capcom assets.

---

# 12. AUTONOMOUS LONG-RUNNING EXECUTION

This is one of the most important requirements.

The user does **not care if the build takes days** on the VPS.

The build should run primarily in the background without repeated manual babysitting.

The failure mode the user wants to eliminate is:

- one long prompt runs;
- an agent writes a partial implementation;
- the session ends;
- it claims success too early;
- visual quality is poor;
- no one independently tests it;
- the user must manually tell it to continue.

Instead the build needs durable project state and a real multi-agent lifecycle:

- plan;
- decompose;
- assign;
- implement;
- test;
- request review;
- independent review;
- request changes if needed;
- rework;
- integrate;
- regression test;
- visual review;
- release gate;
- continue until Definition of Done.

Browser closure must not stop the system.

A worker/model/context ending must not mean the project ends.

A VPS/gateway restart should recover work safely.

No task should silently disappear after a failure.

---

# 13. HERMES EXECUTION PHILOSOPHY

The user previously tried `/go`, long prompts and repeated "continue until done" wording. That was not sufficient.

The current desired approach is to use Hermes' durable primitives rather than treating one conversation as the controller.

Desired conceptual use:

- **Profiles** = persistent specialist worker identities;
- **Native Hermes Kanban** = authoritative durable build task lifecycle;
- **Crews** = visible named teams / reusable groupings;
- **Conductor** = temporary mission orchestration / visual mission layer;
- **Goal-mode Kanban cards** = bounded tasks that should iterate until explicit card acceptance criteria are met;
- **delegate_task** = bounded child reasoning/research inside a worker, not the project database;
- **Gateway dispatcher** = continuous background worker dispatch;
- **Cron** = watchdogs/scheduled checks, not the main software-project lifecycle.

Important: the implementation must verify whether the current Hermes Studio "Tasks/Kanban" UI is actually backed by the same native Hermes Kanban database. It must not assume two similarly named boards are the same thing.

---

# 14. FREE-MODEL / STRONG-MODEL STRATEGY

The user wants **free inference to do most of the heavy token-consuming implementation**.

Strong/expensive/subscription-backed models should be concentrated on high-value reasoning:

- overall architecture;
- initial project decomposition;
- difficult diagnosis;
- high-risk decisions;
- visual QA where a stronger vision model materially helps;
- security-sensitive review;
- final acceptance.

Routine coding, tests, repairs, source archaeology and repetitive work should preferentially run on verified free models.

The user explicitly wants QA/rework loops rather than lowering quality because the workers are free models.

Free models may be slower; elapsed time is not the success criterion.

Do not silently spend money because a free provider fails.

A previous user constraint put an **absolute maximum of about $1.50 for a very large feature** and the user has repeatedly emphasized economical OpenRouter use. Therefore any deliberate paid strong-model call should be explicitly bounded and rare. A one-time Astra review should be treated as a high-value exception, not a general worker model.

---

# 15. STRONG MODEL / SUBSCRIPTION INTENT

The user has access to ChatGPT and Claude subscriptions and wants to use stronger models for planning and QA where legitimate unattended access exists.

Do not assume a consumer subscription automatically equals API automation access.

The build should inspect what Hermes can actually use through authorized OAuth/subscription/provider routes.

Where strong unattended access is not available, the system should not secretly substitute paid API inference.

---

# 16. QA LOOP — NON-NEGOTIABLE

The user is dissatisfied with systems that technically function but fail their quality expectations.

Therefore:

- implementers do not self-approve;
- every meaningful change is independently reviewed;
- QA reproduces behavior from the exact revision;
- test output and screenshots are evidence;
- failed review routes the same work back with precise defects;
- repeated failure changes strategy/model/spec instead of endlessly retrying the same prompt;
- integrated changes rerun affected regression tests;
- visual work receives visual QA, not only unit tests;
- final release requires full-system E2E proof.

"Code exists" is not completion.

"Tests pass" is not necessarily visual acceptance.

"Screenshot looks similar" is not necessarily functional acceptance.

---

# 17. VISUAL QUALITY BAR

The user has repeatedly described prior AI-generated software as far below their standards.

The desired experience is:

- premium;
- polished;
- smooth;
- coherent;
- high information density;
- strong visual hierarchy;
- excellent transitions/animation;
- no obviously unfinished placeholders;
- no large accidental dead spaces;
- no generic ugly admin-dashboard appearance;
- no fake metrics;
- no static "office image" pretending to be live.

The references are directional quality bars, not permission to copy their fake sample data.

The user cares more about the functions and experience than exact pixel identity, but would be happy if the implementation reaches or exceeds the visual references.

---

# 18. OBSERVABILITY

The user wants to be able to see and optimize what individual agents are doing, including background/repetitive work.

Clicking an employee should expose as much real operational context as supported, such as:

- identity;
- department;
- role;
- personality/config version;
- current task;
- project;
- run/session;
- model/provider actually serving the run;
- token usage;
- cost;
- current tool/activity;
- latest error;
- review status;
- skills;
- tools/MCPs;
- memory/knowledge scope;
- permissions;
- historical work;
- evaluation/performance;
- prompt history;
- links to chat, task, run, logs and evidence.

The UI should explain **why** a bot appears busy, blocked, frustrated or scared.

---

# 19. KNOWLEDGE, MEMORY AND LEARNING

The user has emphasized this as extremely important.

Desired system concepts include:

- institutional memory;
- scoped Obsidian knowledge;
- durable project knowledge;
- lessons learned from completed/failed work;
- prompt/model/skill improvement proposals;
- evidence-backed learning;
- explicit scope boundaries (global / department / project / agent);
- critical changes require review/approval;
- version/diff/rollback for important agent configuration;
- no uncontrolled self-modification.

Obsidian remains important as human-readable knowledge / institutional memory.

Operational state should not be confused with Obsidian notes.

---

# 20. HEADROOM / PONYTAIL CONTEXT-OPTIMIZATION IDEA

The user previously accepted the idea of applying Headroom/Ponytail-style techniques to the workforce.

The intended concept was:

- **Headroom**: global context/tool-result compression and retrieval optimization to reduce excessive token use, with reversibility and preserved evidence;
- **Ponytail-style guidance**: especially for technical agents, reduce overengineering and keep implementation focused;
- compact structured handoffs instead of blindly forwarding full transcripts;
- preserve exact acceptance criteria, errors, commands, numbers, evidence references and security details;
- context compression is NOT the authoritative employee memory system.

This should be evaluated behind a benchmark gate rather than blindly inserted into every context path.

---

# 21. MODEL/COST TRANSPARENCY

The user wants to know which models actually run work and how much they cost.

Requirements should include:

- requested model;
- effective provider/model;
- free/paid classification;
- rate-limit events;
- fallback events;
- input/output tokens;
- cost where available;
- task/project/department attribution;
- model performance history;
- ability to compare models by task class.

Do not claim "free" solely because the configured model name sounds free; verify the effective route/provider.

---

# 22. DATA/TRUTHFULNESS

The user explicitly disliked the previous seeded/mock implementation.

Production/live mode must never fabricate:

- activity;
- tasks;
- spend;
- QA results;
- project progress;
- agent status;
- health.

If data is unavailable, display unknown/empty/unavailable honestly.

Health metrics must have a documented formula or be replaced with more truthful status summaries.

---

# 23. SECURITY / PERMISSIONS

Long-running workers should not all receive unlimited VPS authority.

Desired principles:

- least privilege;
- worktree/repo isolation;
- bounded tools;
- no arbitrary secret access;
- approvals for dangerous actions;
- no workers possessing an unrestricted token that bypasses application-level governance;
- test inherited Hermes/Studio execution endpoints for bypasses;
- no public deployment or destructive infrastructure action without explicit authorization;
- model provider data-use/retention matters when sending private code to free endpoints.

---

# 24. PERFORMANCE / RENDERING

The user chose 2D specifically because 3D is unnecessary and more demanding.

Desired performance principles:

- no heavyweight 3D runtime;
- lightweight 2D renderer;
- shared sprite/animation assets;
- offscreen scenes throttled/paused;
- miniature department scenes should not each run full independent 60fps loops;
- no memory leaks after repeated navigation;
- animations should remain smooth on a normal desktop accessing the VPS app;
- reduced-motion mode;
- application remains fully operable without animation.

---

# 25. MOBILE / REMOTE ACCESS CONTEXT

The user has previously liked the idea of accessing the AI command-center remotely from PC/phone.

The desktop office can remain the richest representation, but responsive/mobile use should at least support:

- inspecting organization state;
- checking tasks/agents;
- seeing alerts/approvals;
- opening agent details;
- approving or responding to attention requests.

The mobile UI does not need to run a dense full-resolution office animation if a lighter representation is better.

---

# 26. REJECTED / AVOIDED DIRECTIONS

Avoid reintroducing these unless a new evidence-backed decision explicitly changes them:

- embedding the workforce back into Empirium OS;
- building a totally separate third AI-agent platform from scratch;
- replacing useful Hermes Studio machinery without a reason;
- using Conductor sessions as the sole persistent employee identity;
- treating a Department as merely a renamed Crew;
- one gigantic prompt/session as the durable project controller;
- relying on `/go` or repeated "continue" prompts as persistence;
- making Cron the primary project state machine;
- allowing implementers to self-approve;
- fake dashboard metrics;
- static office art masquerading as live operational state;
- 3D runtime simply because the inspiration came from a PS1 3D game;
- leaked Capcom source code;
- frame-by-frame AI image generation as the default animation pipeline;
- silent paid-model fallback.

---

# 27. DESIGN PHILOSOPHY FOR AGENT DESCRIPTIONS

The user previously investigated best practices for agent routing descriptions and wanted those principles applied whenever agents are created.

Descriptions should be written from the orchestrator's perspective and should:

- start with imperative routing language such as **"Use this profile when..."**;
- describe the user/task intent it should receive;
- be specific enough to avoid overlap;
- include important exclusions so it is not selected for adjacent roles;
- be somewhat "pushy" about the situations where it should be selected;
- avoid implementation trivia that does not help routing;
- match the real capabilities/tools of the profile.

The SOUL/system prompt then contains the detailed operating contract.

---

# 28. FINAL USER EXPERIENCE — WHAT SUCCESS FEELS LIKE

The successful system should let the user do something like this:

1. Open Empirium Studio.
2. See the entire AI organization at a glance.
3. See departments as live little rooms/offices.
4. Open Personal Software.
5. See Director, Research Architect, Developer, QA Engineer and Learning Analyst physically represented as moving bots.
6. Give the department a software task.
7. Watch planning occur and work be assigned.
8. Watch the relevant bot move into a work state.
9. See temporary workers appear where useful.
10. See errors visually and in logs.
11. See QA receive/reject/reapprove work.
12. See an attention-seeking bot if human input/approval is required.
13. Click any bot and inspect exactly what it is doing and why.
14. Close the browser.
15. Return later and find that the project continued.
16. Inspect tasks, runs, evidence, costs, model routing, QA history and learning proposals.
17. Have the project finish only when the real Definition of Done has passed.

That is the product ambition.

---

# 29. META-REQUIREMENT FOR THE BUILD PROMPT

The final Hermes master prompt must provide **far more than a wish list**.

It should specify:

- exact repository topology;
- exact persistent execution mechanism;
- exact build profiles;
- precise routing descriptions;
- detailed SOUL/system instructions;
- role boundaries;
- model class per role;
- tool/toolset policy per role;
- MCP policy per role;
- crew composition;
- board/Kanban behavior;
- task contract format;
- worktree policy;
- review/rework lifecycle;
- free-model preflight;
- rate-limit/cost controls;
- data privacy routing constraints;
- art/asset pipeline;
- ROM extraction research pipeline;
- 2D animation architecture;
- product requirements;
- learning/memory architecture;
- test matrix;
- visual QA process;
- resilience/failure injection;
- performance/accessibility gates;
- deterministic final release gate;
- autonomous demonstration;
- definition of done;
- rules preventing premature success claims.

The build can take a long time. Quality and durable completion are more important than elapsed time.
