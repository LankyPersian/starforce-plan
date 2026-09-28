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
