

===== 2026-09-22 02:17 | session 20260922_021616_abfb3d | Nailify to Nailed It MVP polish =====
@file:.hermes/attachments/NAILED_IT_MASTER_PROMPT_V5_GOAL.md
@file:`.hermes/attachments/Pasted content (3.6 KB)`

/goal  Take the existing Expo/React Native app at `/home/ash/Desktop/nailify` from its verified current state (HEAD `f5f33f249e6ad9d38aeaa7fb0f25c52f0ffb8ca6`, branch `main`, clean) to a polished, genuinely usable consumer MVP whose core experiences are:
1. an excellent **individual nail + full ten-nail set designer**,
2. a convincing **live AR try-on** on the user's real hand,
3. a beautiful, coherent, production-quality mobile app shell around those two core features. 

The MVP should feel like something a real consumer could download and enjoy — **not a developer demo, wireframe, debug tool, or UI kit showcase**. The one-sentence mission (V3 §0, verbatim): *"Transform the existing Nailify prototype into Nailed It: a premium, user-friendly mobile nail-design app whose core experiences are: 1. an excellent individual nail + full set designer, 2. a convincing live AR try-on on the user's real hand, 3. a beautiful, coherent, production-quality mobile app shell around those two core features."*
**Start condition.** This session receives the complete document, reads it fully (all appendices), verifies the §2 state facts on disk, and begins Phase A (§4.1).
**Stop condition.** The goal is complete when the Definition of Done in §4.8 is met — i.e., when the deterministic release gate sets `SHIPPED`. Alternative stop: a tripwire (§4.9) fires with no autonomous path forward, in which case the system checkpoints state and notifies the owner (genuine blockers only). Or: explicit user cancellation (`.hermes/STOP` / `CANCELLED_BY_USER`).
**CLEAR CRITERIA OF SUCCESS (all must be true, each independently checkable — the goal may not be declared finished otherwise):**

--- Attached Context ---

📄 @file:.hermes/attachments/NAILED_IT_MASTER_PROMPT_V5_GOAL.md (108008 tokens)
```markdown
# NAILED IT — MASTER PROMPT V5 (AUTONOMOUS /GOAL BUILD)

**Version:** V5 — 2026-09-22 (Europe/London, BST)
**Prepared by:** the "prep for nailify" session (Hermes chat `20260921_234936_670e4e`), at the owner's explicit instruction: *"do not start this yourself. Please produce the complete prompt, exhaustive detail, attention to granular detail, prompt to have another chat start and finish this /goal project. Make sure the prompt is a slash-goal starting prompt with clear criteria of success."*
**Supersedes:** `NAILED-IT-FINAL-BUILD-GOAL.md` (the earlier goal doc, retained as reference only), all `HERMES_NAILED_IT_MASTER_PROMPT_V3_AUTONOMOUS*.md` copies (embedded verbatim in Appendix E), and every earlier planning artifact.
**Form:** this entire document is the `/goal` starting prompt. Paste the whole file (including every appendix) as the goal for a fresh Hermes chat. That chat starts and finishes the build.

---

## §0. GOAL STATEMENT (the /goal)

**Goal.** Take the existing Expo/React Native app at `/home/ash/Desktop/nailify` from its verified current state (HEAD `f5f33f249e6ad9d38aeaa7fb0f25c52f0ffb8ca6`, branch `main`, clean) to a polished, genuinely usable consumer MVP whose core experiences are:

1. an excellent **individual nail + full ten-nail set designer**,
2. a convincing **live AR try-on** on the user's real hand,
3. a beautiful, coherent, production-quality mobile app shell around those two core features.

The MVP should feel like something a real consumer could download and enjoy — **not a developer demo, wireframe, debug tool, or UI kit showcase**. The one-sentence mission (V3 §0, verbatim): *"Transform the existing Nailify prototype into Nailed It: a premium, user-friendly mobile nail-design app whose core experiences are: 1. an excellent individual nail + full set designer, 2. a convincing live AR try-on on the user's real hand, 3. a beautiful, coherent, production-quality mobile app shell around those two core features."*

**Start condition.** This session receives the complete document, reads it fully (all appendices), verifies the §2 state facts on disk, and begins Phase A (§4.1).

**Stop condition.** The goal is complete when the Definition of Done in §4.8 is met — i.e., when the deterministic release gate sets `SHIPPED`. Alternative stop: a tripwire (§4.9) fires with no autonomous path forward, in which case the system checkpoints state and notifies the owner (genuine blockers only). Or: explicit user cancellation (`.hermes/STOP` / `CANCELLED_BY_USER`).

**CLEAR CRITERIA OF SUCCESS (all must be true, each independently checkable — the goal may not be declared finished otherwise):**

| # | Criterion | How it is checked |
|---|---|---|
| S1 | `verify.sh` exists at `app/verify.sh`, is the **sole acceptance authority**, passes at the release SHA, and its protected files are hash-verified unchanged | `cd app && bash verify.sh` exit 0; `sha256sum` vs `.hermes/state/harness-sha.json` |
| S2 | Every one of the 36 mandatory P0 requirements (Appendix B §6 ledger) has a **FROZEN acceptance contract** and is either (a) PASS with current-SHA evidence, or (b) explicitly `hardware-limited` with the strongest legitimate substitute evidence and a recorded release limitation | `.hermes/state/acceptance-contracts/` + `verify.sh` output at release SHA |
| S3 | The mandatory **27-step 10-minute user story** (V3 §67, Appendix E) runs end-to-end without failure, with session log + screenshots tied to the release SHA | QA evidence in `.hermes/evidence/` |
| S4 | **Zero visible fake flows** in normal P0 navigation (no "simulated", "preview build", "coming soon", fake sign-in/purchase/AI/QR) | `grep -RniE 'TODO\|FIXME\|stub\|simulated\|mock\|coming soon\|placeholder\|preview build' app/src app/app.json` → 0 matches in P0 flows |
| S5 | **Independent review** of the full P0 release diff completed by a fresh session that did not implement it (schema/migration, persistence/deletion, state/undo, AR/native, security/privacy, navigation/state, control plane, release candidate, large builder changes — all reviewed) | `REVIEW_QUEUE.md` R-states = PASS with reviewer identity |
| S6 | `SHIPPED` set **only** by the release gate, atomically, with the release record in `.hermes/state/release.json` (SHA + checklist results + reviewer identity) | `.hermes/state/release.json` |

**The anti-goal:** do not optimize continuity (uptime, sessions, commits, task counts). The single metric is **independently accepted product changes per day, verified against the requirement ledger at the current SHA**. If that line is flat while workers are "alive", the architecture is irrelevant (retrospective §36/Q9, Appendix C).

---

## §1. AUTHORITY, PRECEDENCE, FROZEN OWNER DECISIONS

### 1.1 Document layout and precedence

This document contains **every piece of data the owner provided in the prep session**, verbatim, in appendices:

| Appendix | Content | Source (verbatim) |
|---|---|---|
| A | Session record: the owner's requests and the assistant's V4 plan, Stage 0 verdict, live-repo verification, and the owner's plan tweaks | prep-session messages |
| B | HUMAN ANSWERS — NAILED IT STAGE 0/1/2/3 (14 Stage-0 answers; full Stage 1 audit; 28 locked Stage 2 items; Stage 3 answers A–I + the seven owner decisions) | owner dataset, 63 KB |
| C | FORENSIC RETROSPECTIVE (429-line report: 40 sections, evidence-anchored timeline, 43 quantitative findings, one-page doctrine, Q1–Q10, "What I should remember" ×21, five mandated final statements) | owner-attached report, 69.6 KB, committed `71bd829` |
| D | PRE-RUN LOCK — "answers to all the questions" (fallback benchmark, AR spike decision tree, re-run budget, dependency graph, worker packet template, harness lifecycle, acceptance contracts, environment rules, commissioning gates) | owner dataset, 22.5 KB |
| E | THE V3 MASTER PROMPT in full (3,629 lines / 105,798 bytes, all four on-disk copies byte-identical, md5 `606c7461d5b46f66b24a07911c048b87`) | owner-attached charter |
| F | THE RETROSPECTIVE MANDATE — the 86-section forensic-audit brief the owner authored, which produced Appendix C | owner dataset, 65 KB |

**Precedence order (when wording conflicts, the lower number wins):**

1. **§1.2 Frozen owner decisions** (latest, 2026-09-22) — the owner's final words from the prep session.
2. **§2 Verified current state** — facts measured on disk at `f5f33f2`, 2026-09-22.
3. **§4 Execution plan (this V5 body)** — the operative plan.
4. **Appendix D** (pre-run lock, 2026-09-22).
5. **Appendix B** (human answers Stage 0/1/2/3).
6. **Appendix C** (forensic retrospective — doctrine and lessons).
7. **Appendix E** (V3 charter). The V3 *product intent* (its §0–§5, §8–§67) remains the product spec and governs all product decisions not explicitly overridden here. The V3 *baseline description* (its §3 "known starting state") and its *Phase A bootstrap ordering* (§58 "Phase A — Autonomy bootstrap" as a 22-test pre-requisite) are **superseded**: the repo has advanced past that baseline (Phases 1–2 are done, §2.2) and the owner chose Path A (acceptance harness first, §1.2 D3/D4) instead of the V3 full-controller bootstrap.

**Source-of-truth order for product questions** (V3 §2, amended): this prompt → the actual source code at the current SHA → the user-owned visual inspiration files → existing README/old prompt packs as historical context only.

### 1.2 Frozen owner decisions (2026-09-22, prep session — do not renegotiate)

**D1 — Authoritative workspace.** `/home/ash/Desktop/nailify` is the real project. The V3 charter's `~/Desktop/nailfy` spelling is a typo to reconcile, not a reason to rename or duplicate. App root: `/home/ash/Desktop/nailify/app`. (Stage 0 answer Q1; verified on disk.)

**D2 — Phases 1–2 are complete. Skip them.** Do not redo foundation, schema-v2/project-library work, or native-AR bootstrap merely because earlier planning documents assumed they were unfinished. The verified current repository state supersedes those stale baseline assumptions. Preserve existing passing behaviour and test coverage. (Owner decision, verbatim: "Yes — treat Phases 1–2 as complete and skip them.")

**D3 — Path A: build the acceptance harness first.** Freeze acceptance against the **current HEAD `f5f33f2`**, not against the old baseline assumptions. Record current truth honestly: existing capabilities may already pass; incomplete ones fail; hardware/environment-limited items remain explicitly unverified. (Owner: "The more valuable next measurement is whether the remaining gaps can be expressed as bounded WorkItems with frozen predicates.")

**D4 — Permission granted: build the acceptance harness now.** Create `verify.sh` and the associated fixed predicates/evidence machinery as the **sole acceptance authority before further product implementation proceeds**. The harness may add acceptance/testing infrastructure, but it **must not weaken existing tests or modify product behaviour merely to make checks pass**. (Owner: "Yes — you have permission to build the acceptance harness now.")

**D5 — The French 20-run benchmark is retired as the Stage 2 measurement task.** French is already substantially implemented (first-class control, 5 styles, depth, tip colour, apply-to-focused — §2.2). Do **not** spend the 20-worker benchmark budget on it. Once the acceptance layer is operational, choose a **genuinely outstanding, bounded requirement from the remaining gaps** and **pre-register its predicate before using worker-hours to measure first-attempt acceptance**. French remains an acceptance case, but it is no longer the worker-reliability benchmark. (Owner, verbatim: "retire the French 20-run benchmark as the Stage 2 measurement task…")

**D6 — Model split, with the owner's Claude Code allowance.** The full heavy lifting of coding is done by **FreeLLMAPI**. The owner has Claude Code subscription usage to use up: *"i want to use it as much as possible. i mean the full 5 hour window usage at 2:50, 7:50, and 12:50."* Use Claude **as much as needed for important reviews and planning** in those windows. (Encoded in §4.4.)

**D7 — No execution from the prep chat.** *"now do not start this your self."* This document is the deliverable; the next `/goal` chat starts and finishes the project.

**D8 — Provider policy (locked in Appendix B/C/D and re-confirmed).** No OpenRouter credits, no Luna, no ChatGPT route in the routing table. FreeLLMAPI = Tier A (all heavy coding). Authorized Claude subscription = Tier B (reviews, planning, architecture). **£0 / $0 / ¥0 new metered spend.** Freeze provider/model at start; change only on classified provider failure, one variable at a time, with written rationale.

**D9 — The existing orchestration is adequate; earn every addition.** `controller.py` (16.3 KB), `project.db` (151 KB), `watchdog.py`, systemd units, and worktrees already exist and shipped Phases 1–2. Do **not** re-bootstrap the V3 Phase-A 22-test commissioning factory. No new orchestration machinery (leases rework, merge queues, reconcilers, director layers, persistent managers) is added unless a tripwire (§4.9) fires with evidence. (Retrospective §34/§38 + owner decision; the one exception: the acceptance harness, which is a predicate layer, not a supervisor.)

**D10 — Deliverable form.** A slash-goal starting prompt with clear criteria of success (§0), containing every piece of owner data, from which one chat can start and finish the /goal project.

### 1.3 What is deliberately NOT in scope (exclusions, frozen)

- Cloud services/backend/server-side logic (Firebase/RevenueCat/AI remain stubbed or removed from the user path — Stage 0 Q6–Q9).
- Accounts/authentication (local-first guest use; a fresh user must install, open, create, save, reopen without registration — Stage 0 Q9).
- Subscriptions/paywall (MVP is fully unlocked unless a fully real, tested RevenueCat setup is discovered — Stage 0 Q7).
- Production AI generation (AI Studio is not an MVP pillar — Stage 0 Q8).
- App Store/Play Store publication, signing ownership, legal-owner actions (a polished validated release candidate is the objective — Stage 0 Q11).
- Social/community/monetization/booking/commerce/3D sculpting/salon CRM (P2, Appendix E §4).
- Re-implementation of the existing SVG/nail/layer engine (it is preserved and extended — V3 §59, Appendix E).
- Foundation work (Phases 1–2 already complete and verified — D2).

---

## §2. VERIFIED CURRENT STATE (operational baseline, measured 2026-09-22)

**Do not redo verified work. This section is the baseline.** If your first action is to redo something listed in §2.2, you are wrong — re-read this section. Every row below was measured on disk on 2026-09-22, not inherited from a document. Re-verify cheaply at session start (§4.1 step 1); if reality differs, **record the discrepancy and trust the filesystem**, never the narrative.

### 2.1 Environment and provenance

| Fact | Value | How verified |
|---|---|---|
| Project root | `/home/ash/Desktop/nailify` | `ls`, git |
| App root | `/home/ash/Desktop/nailify/app` (Expo + RN) | `package.json`, `app.json`, `src/` present |
| Git HEAD | `f5f33f249e6ad9d38aeaa7fb0f25c52f0ffb8ca6` (`f5f33f2`, *"chore: record native build and branding validation"*) | `git rev-parse HEAD` |
| Branch / tree | `main`, clean (only untracked `.hermes/goals/`) | `git status --short` |
| Remote | `origin https://github.com/LankyPersian/nailify.git` | `git remote -v` |
| Prior commits | `1056e3d` (ignore local work-queue artifacts), `873dd61` (feat(branding): Nailed It icon and splash) | `git log --oneline` |
| Stack | Expo ~51, React Native 0.74.5, React 18, React Navigation v6, Zustand + AsyncStorage, react-native-svg, gesture-handler, expo-camera, expo-haptics, react-native-view-shot | `app/package.json` |
| npm scripts present | `start`, `android`, `ios`, `web`, `test` | `package.json` — **no `lint` script** |
| Controller assets | `.hermes/autonomy/controller.py` (16,306 B), `.hermes/autonomy/watchdog.py` (2,733 B), `.hermes/state/project.db` (151,552 B) | `ls -la` |
| systemd units | `nailed-it-controller-watchdog.service`, `…​.timer`, and `nailed-it-controller.service.contained-20260918` (the main unit is **contained/disabled**) | `ls ~/.config/systemd/user/` |
| Controller status | **Stopped.** Last heartbeat `STOP` 2026-09-19 12:53 UTC; no active leases; `project.db` project state `WAITING_RETRY` | heartbeat JSON + DB |
| Existing `.hermes` docs | `CHANGELOG.md`, `CHECKPOINT.md`, `DECISIONS.md`, `KNOWN_ISSUES.md`, `MASTER_PLAN.md`, `QA_MATRIX.md`, `REQUIREMENTS.md`, `REVIEW_QUEUE.md` | `ls` |
| Host | CPU-only VPS, ~16 GB RAM, no GPU, headless, no iOS simulator, no Android emulator, no attached phone | owner statement + environment |

### 2.2 What IS complete and verified — DO NOT REDO (frozen by D2)

| Area | State | Evidence |
|---|---|---|
| Foundation / shell | App root `app/` with `src/`, navigation, brand tokens, fake-flow removal done | Phases 1–2 accepted; `expo-doctor` 17/17 recorded |
| Test infrastructure | Jest configured; suites present: `ar-placement.test.js`, `builder-depth.test.js`, `design-store-migration.test.js`, `shapes.test.js`, plus `src/components/studio/categoryUtils.test.js` — **64 tests, 0 failures** as last recorded | `jest.config.js`, `__tests__/`, prior run record |
| Design model | **Schema v2** + migration from legacy; project library (create/load/rename/duplicate/delete/autosave) | 10 migration tests pass; `design-store-migration.test.js` |
| Persistence | Zustand persist middleware + AsyncStorage; undo history excluded from persistence via `partialize` | `useDesignStore.js` `schemaVersion`, `partialize` |
| Builder base | 10-nail set (`hands.L[5]`/`R[5]`), shape/length, base colour, gradient, single-nail hero | `builder-depth.test.js` |
| **French control** | **First-class, already implemented** — `applyFrench(style='classic', tipColor='#ffffff', depth=0.18)` at `useDesignStore.js:424`; dedicated French UI with 5 styles + apply-to-focused | verified: `grep -n applyFrench` → line 424; `StudioPanels.js` French block |
| Draw tool | Freehand stroke layer with colour, width, opacity (`makeStrokeLayer`, `addStrokeLayer`) | `useDesignStore.js` |
| Text tool | Text layer with editable text, colour, font, size (`addTextLayer`, `useDesignStore.js:469`) + inspector editing | `InspectorPanel` |
| Undo/redo | 50-entry history (past/future arrays, `HISTORY_LIMIT`), `undo:` ~`:677`, `redo:` ~`:696` | `useDesignStore.js` |
| Layers | Art/text/stroke layers; select, move, recolour, duplicate, delete, visibility, lock | `InspectorPanel.js`, `StudioPanels.js` |
| **AR native pipeline** | **Real, not a stub** — `src/ar/HandTracker.js` (3,984 B) using `react-native-vision-camera` + `expo-vision-camera-v4-mediapipe` + Worklets + `landmarksToTransforms` | verified file listing 2026-09-19 13:41 |
| AR web pipeline | `src/ar/HandTracker.web.js` (8,389 B) — MediaPipe HandLandmarker via CDN, live video → landmarks → transforms | verified |
| AR placement math | `src/ar/placement.js` (6,618 B) — box, mirror, `designByHand`, `handFilter`, adjust, smoothing | verified; covered by `ar-placement.test.js` |
| AR fit calibration | Global + per-nail (size/along/across/rot), persisted, smoothing control, `resolveAdjust()` pure helper | `src/state/useArStore.js` |
| AR try-on screen | HandTracker integrated; capture/share wired; honest fallback notes | `ARTryOnScreen.js` |
| Export/share | `captureDesign` (view-shot, JPEG, 2× DPR), `saveToCameraRoll`, `shareImage` | `src/services/export.js` |
| Shell screens | Home (tabs incl. AR); Explore (SearchBar + style/occasion/artist filtering, `ExploreScreen.js:84-142`); MyNails (rename/duplicate/delete, `:57-132`); Settings (haptics toggle, clear local data, `:53-114`); Onboarding (3 slides, Android back, `completeOnboarding`) | verified files |
| Branding | Nailed It icon (10.8 KB) + splash (24.9 KB), `app.json` configured | commit `873dd61` |
| Android | Native build successful; scoped media permissions; AR min SDK configured | commits `1e024c1`, `428968c`, `1854a5b`, `5503825` |
| Web export | `npx expo export --platform web` → 1.38 MB bundle, `dist/` exists | prior run |
| Orchestration | `controller.py`, `watchdog.py`, `project.db`, systemd units, worktrees | verified (§2.1) |

**Five stale-baseline conflicts (resolved — the documents are wrong, the disk is right):** (1) "Native AR is a stub at `HandTracker.js:1-14`" — **false**, it is a real implementation; (2) "French is only a `frenchTip` art asset/smart-set shortcut" — **false**, `applyFrench` is first-class; (3) "Phases 1–2 not done" — **done**; (4) QA matrix SHA `9fb9391` — **stale**, current HEAD is `f5f33f2`; (5) the 36-requirement ledger's Baseline column is stale for roughly 8 entries (AR-002, BUILDER-006, DATA-003/004/005, SHELL-001/003, possibly others). **Re-baseline the ledger honestly against current code as part of Phase A (§4.1).** A ledger whose baseline column lies is worse than no ledger, because it silently re-prioritises work.

### 2.3 What is NOT complete — the actual work targets

| Area | Specific gap | Evidence |
|---|---|---|
| **Acceptance harness** | `app/verify.sh` does **not** exist; `app/checks/` does **not** exist; no acceptance contracts for any requirement | verified: `ls app/verify.sh app/checks` → both missing |
| Lint | No `lint` script in `app/package.json`; no ESLint config | verified `grep '"lint"'` → empty |
| Builder — finishes | Finishes/effects/patterns/gems/chrome/glitter quality not audited against visual requirements (V3 §18, §25–§27) | `KNOWN_ISSUES.md` |
| Builder — draw/erase | Eraser + smoothing behaviour not verified; 60 fps drawing unproven | `KNOWN_ISSUES.md` |
| Builder — layer UX | Visibility/locking and selected-layer behaviour need a complete interaction pass | `KNOWN_ISSUES.md` |
| Builder — set helpers | UI for smart-set helpers, templates, presets beyond seed data incomplete; **bidirectional mirroring** still partial (code copies L→R only) | `KNOWN_ISSUES.md`, Stage 1 audit |
| Builder — calm UX | Progressive-disclosure density target (V3 §14) not achieved | charter gap |
| AR — device validation | **No physical Android/iOS development build has been run in this environment.** Tracker, placement, permissions, fit, capture/share all untested on device | `KNOWN_ISSUES.md` |
| AR — permissions | Camera + media-library permission flows untested on device | `KNOWN_ISSUES.md` |
| Shell — MyNails | Lacks complete export and finished/draft management UI | `KNOWN_ISSUES.md` |
| Shell — Settings | Lacks About, reduced-motion preference, permission links, onboarding re-entry | `KNOWN_ISSUES.md` |
| Shell — Explore detail | Design detail view with full info + apply-to-designer action | gap |
| Accessibility / responsive | Accessibility, reduced motion, keyboard behaviour, Android back, loading/error states need evidence; 320/430 px screenshots not captured | `KNOWN_ISSUES.md` |
| Product integration | The mandatory 27-step 10-minute user story has **not** been executed end-to-end | `KNOWN_ISSUES.md` |
| Crash recovery | Autosave implemented but **not** crash/relaunch tested | `KNOWN_ISSUES.md` |
| Independent review | Final P0 diff has **not** received independent review (R-04) | `REVIEW_QUEUE.md` |
| Measurement infra | `.hermes/experiments/worker-baseline/` (packet template, harness, manifest) does not exist; browser-automation probe not run; environment sampling not wired; provider/model discovery + freeze not done; commissioning gate 0/15 | verified |

**Honest read (carry this into planning):** the remaining work is roughly **95% product** (builder depth, AR device completion, shell polish, integration, hardening) and ~5% measurement/acceptance infrastructure. The binding constraint is no longer *"does the worker produce accepted output"* — it is *"is the remaining product scope decomposable into bounded packets with frozen predicates."* Adding orchestration now would be the exact anti-pattern the retrospective documents: **architecture-after-failure without measurement, when there is no failure here to respond to.**

---

## §3. OPERATING DOCTRINE (pre-registered; do not renegotiate mid-flight)

These are distilled from Appendix C (the forensic retrospective) and locked by the owner. Each is a rule with a reason; violating one invalidates the run.

**3.1 One worker at a time.** No parallel implementation workers until single-worker first-attempt acceptance is measured (§4.3) and ≥60%. *Why: a fleet inherits the reliability of the thing it multiplies; the history built 102 worktrees around an effective concurrency of 1.*

**3.2 Acceptance is a predicate, never a self-report.** The worker never declares its own work done. `verify.sh` is the sole authority. A worker's `status_claim` is informational only. *Why: every acceptance number in the history was a controller self-declaration with 0 independent reviews.*

**3.3 No runnable work ≠ complete.** Empty queue, no pending tasks, and idle workers are all consistent with nothing being done. Only the §4.8 release gate may set `SHIPPED`. *Why: two isolated reconciles produced `WAITING_RETRY` with 0 work items and 0 events — a permanent logical stall while alive.*

**3.4 Failed predicates create work.** `FAIL`/`REJECT` produces a bounded WorkItem describing exactly what must change and why. **There is no ordinary `FAILED` terminal state** — the only terminal states are `SHIPPED` and `CANCELLED_BY_USER`. Worker crash, controller restart, session limit, context exhaustion, 429, quota exhaustion, provider timeout, malformed response, bad implementation, failing test, QA rejection, visual rejection, merge conflict, dependency conflict, failed build, failed predicate, and "no runnable task right now" are **all non-terminal**. *Why: the reconciler logged `initial_status: FAIL` 2,245 times over 18.7 hours and generated zero diagnoses.*

**3.5 Waiting is allowed; stopping is not.** Legitimate wait states: `WAITING_PROVIDER`, `WAITING_RETRY`, `WAITING_DEPENDENCY`, `WAITING_REVIEW`, `WAITING_INTEGRATION`, `WAITING_EXTERNAL`, `DIAGNOSING`, `RECONCILING`. Record why, back off, retry, continue all independent work. Never write a failure report and stop; never require the user to type "continue".

**3.6 Worker reliability is measured, not assumed.** Before any scaling decision: one bounded task, pre-registered predicate, ≥20 fresh-session runs, measure ACCEPT/REJECT/NO-CHANGE/TIMEOUT/MALFORMED. *Why: this measurement cost ~$0 from day one and was never taken across four architecture generations.*

**3.7 The user is not in the normal loop.** Autonomous: implementation, debugging, provider switching within policy, retries, QA rejection, rework, merging, visual review, release verification, ordinary library/UI/engineering choices. Contact the owner **only** for: scope change (adding/removing a P0 requirement), architecture change (stack change, major dependency, app restructuring), metered spend, irreversible/external/legal/store actions, deletion of irreplaceable data, credentials that cannot be created autonomously, hardware the owner must physically supply, contradictory owner-level product requirements, and the final SHIPPED confirmation.

**3.8 The project survives every death.** State lives in `.hermes/state/project.db` (SQLite, WAL) + append-only `.hermes/state/event-log.jsonl` + git on every accepted integration. A session ending mid-task loses nothing. Any session active > 30 minutes is a candidate for replacement — save state before letting it die. *Why: prompts, managers, and chats all failed exactly at their boundaries.*

**3.9 Prompt = intent; code = transitions.** Anything enforceable in code must not live in prose. Do not encode retry schedules, queue state, or completion definitions in instructions.

**3.10 One variable per experiment.** Provider and architecture never change together. Freeze the model at start; change only on a classified provider failure, with written rationale. *Why: model+provider+prompt+runtime changed together in every historical transition, making attribution impossible.*

**3.11 Recovery is earned, not imagined.** Do not build recovery machinery for a failure class the happy path has not exhibited at least twice. *Why: the commissioning gate passed 13/13 recovery checks while 0/710 requirements were verified.*

**3.12 The single metric.** Independently accepted product changes per day, verified against the ledger at the current SHA. Do **not** optimize: session count, messages, tokens, uptime, worktrees, commits, file counts, requirement counts, test counts, prompt length, or documentation volume.

**3.13 Never fabricate evidence.** Do not claim a command ran, a test passed, a device was used, or a screenshot was taken unless it actually happened. Where hardware/runtime is unavailable, use the strongest legitimate substitute, label it precisely, and record the limitation. **Never claim physical-device AR passed unless it actually ran on a physical device.**

**3.14 Preserve failure artifacts.** Never auto-delete a worktree, log, diff, or attempt record before its evidence is captured and consumed. *Why: force-deleted worktrees destroyed the exact evidence the rework loops needed.*

**3.15 Control-plane self-protection.** Product WorkItems may not modify `.hermes/autonomy/`, `verify.sh`, `app/checks/`, release predicates, provider policy, or control schemas. Such changes require a dedicated controller-maintenance WorkItem with independent review. Any worker modification to a protected harness file is automatically **`MALFORMED — PROTECTED_HARNESS_MUTATION`** and counts as a non-ACCEPT engineering attempt.

**3.16 The doctrine line (from the retrospective's final statement):** *"One agent, one bounded task, one pre-written acceptance predicate — run it twenty times, measure the pass rate, and let that number — and only that number — license every component you add."*

---

## §4. EXECUTION PLAN

Phases run in order. Phase A is **blocking**: nothing in B–F dispatches until A is complete and the harness is frozen.

### 4.1 PHASE A — Acceptance harness (BLOCKING, do first)

**A-00 — Session bootstrap (do this before anything else).**
1. Read this entire document including all appendices.
2. Verify §2 on disk: `git rev-parse HEAD` (expect `f5f33f2…`), `git status --porcelain`, `ls app/verify.sh app/checks` (expect missing), `node -v`, `npm -v`, `npx expo-doctor`, `npm test`. Record actuals. **If HEAD differs from `f5f33f2`, stop and re-baseline §2 before proceeding** — do not assume.
3. Record host resources: CPU count, `MemAvailable`, disk free, significant existing processes. **Do not disturb** the Empirium autobuild service, the laptop gateway, or any other VPS service.
4. Write `.hermes/state/startup-log.json`: session start time, git HEAD, `verify.sh` output (it will fail — the harness does not exist yet), test count, first WorkItem dispatched.
5. Preserve the charter: ensure `.hermes/source/PRODUCT_CHARTER.md` contains **Appendix E verbatim** and record its SHA-256 in `.hermes/source/PRODUCT_CHARTER.sha256`. Also preserve this V5 document at `.hermes/source/MASTER_PROMPT_V5.md` + `.sha256`.

**A-01 — Build the acceptance harness.** (Owner-authorised: D3, D4.)

Deliverables:
- `app/verify.sh` — executable (`chmod +x`), the **sole acceptance authority**. It must run in order and exit non-zero on first failure:

```bash
#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

echo "=== Harness integrity ==="
node ../.hermes/autonomy/check-harness-hashes.js   # aborts if any protected file changed

echo "=== Baseline ==="
npx expo-doctor
npm test
npx expo export --platform web
git diff --check
npm run lint

echo "=== Fixed acceptance checks ==="
node checks/run-checks.js "$@"     # supports --only <REQ-ID>
echo "=== ALL CHECKS PASSED ==="
```

- `app/checks/run-checks.js` — the predicate harness. Each requirement maps to a function returning `{ pass: boolean, evidence: string }`. Supports `--only <REQ-ID>` so a WorkItem can be verified in isolation.
- `app/package.json` gains a real `lint` script (ESLint, version-compatible with Expo 51 / RN 0.74.5). Configure the gate so it reliably checks the files an attempt changed; **do not modify product code merely to satisfy a strict whole-repo lint config** on legacy files.
- `.hermes/state/harness-sha.json` — SHA-256 of every protected file: `app/verify.sh`, `app/checks/**`, `.hermes/packets/packet-template.md`, `.hermes/state/acceptance-contracts/**`, `.hermes/autonomy/check-harness-hashes.js`.
- `.hermes/packets/packet-template.md` — **the frozen worker packet template, exactly as specified in Appendix D item 6.** Save it, normalize line endings, `sha256sum` it, record the hash in `.hermes/state/packet-sha.json`, and instantiate every packet mechanically from it. The **on-disk SHA is authoritative**, never a hash copied from chat.

**Harness rules (locked):**
- `run-checks.js` may only **grow** (new checks for new requirements). It may **never** be modified to weaken an existing check.
- **The harness is reviewed by a fresh independent session before it is hashed and frozen** (Appendix D item 7 — this closes the "who guards the guards" hole). The reviewer must answer, with evidence: does every frozen predicate clause have a corresponding real check? Can a missing implementation incorrectly pass? Can an implementer satisfy a check merely by writing a success marker/file? Does the harness exercise real product state/render logic rather than a duplicate mock? Are failure cases tested? Does it discriminate the current baseline? Does it avoid judging requirements outside its scope? Does it avoid subjective style judgments? Can a worker weaken it from its allowed workspace? Are all artifacts reproducible from a fresh shell?
- After review passes: run the harness against the current baseline, **confirm it discriminates** (some checks pass because the feature genuinely exists; the gaps in §2.3 genuinely fail), hash all protected files, and freeze.
- Recompute hashes **before and after every worker attempt**.

**A-02 — Re-baseline the requirement ledger honestly.** Take the 36-requirement P0 ledger (Appendix B §6) and, for each requirement: (a) re-measure its true state against current code, correcting the ~8 stale entries; (b) attach the dependency edges from Appendix D item 5 verbatim as a `depends_on` field; (c) attach the verification block:

```json
"verification": { "predicate_id": "...", "verification_kind": "...", "command": "...", "evidence_expected": "...", "contract_hash": "..." }
```

Write the result to `.hermes/REQUIREMENTS.json` (machine authority) + `.hermes/REQUIREMENTS.md` (readable projection). Target **30–40 mandatory P0 requirements**; correctness beats hitting exactly 36. Hard traceability conditions: every one of the 27 user-story steps (V3 §67) maps to ≥1 requirement; every applicable V3 §68 P0 DoD item maps to ≥1 requirement/check; every requirement has real evidence or an explicit limitation; **no giant line-by-line ledger returns** (the 1.4 MB / 2,288-item `REQUIREMENTS.json` is retained as a reference record only — no WorkItem is ever dispatched from it alone).

**A-03 — Freeze acceptance contracts.** One record per requirement (Appendix D item 8 schema):

```json
{ "requirement_id": "NAIL-P0-BUILDER-006", "contract_version": 1, "predicate": "observable pass condition",
  "verification_kind": ["deterministic","runtime","visual"], "commands": ["./verify.sh --only NAIL-P0-BUILDER-006"],
  "expected_evidence": ["test-result","exit-code","screenshot"], "baseline_result": "FAIL", "baseline_evidence": "...",
  "hardware_limit": null, "harness_files": [], "harness_sha256": "...", "independent_review": "PASS", "state": "FROZEN" }
```

States: `DRAFT → IMPLEMENTED → REVIEW_PENDING → FROZEN → RETIRED`. **Only `FROZEN` makes a WorkItem runnable.** A requirement that cannot yet be verified gets an explicit contract with `verification_kind: hardware-limited`, `dispatch_allowed` as appropriate, the exact missing capability, the exact strongest substitute evidence, and the exact remaining release limitation.

> **THE HARD DISPATCH RULE (the retrospective's core lesson applied to everything, not just French):** *A product WorkItem is not eligible for dispatch unless every mandatory requirement it claims to implement has a FROZEN acceptance contract and the referenced harness files have verified hashes.* This makes it structurally impossible to recreate the historical failure: **implement first → decide later what "done" was supposed to mean.**

**A-04 — Capability probes (decide before run 1, never after seeing results).**
- **Browser/screenshot probe:** can a repeatable headless journey boot the app and produce a SHA-named screenshot **3 consecutive times**? Record the answer. If **yes**, visual predicates are live. If **no**, every visual requirement falls back to its pre-registered deterministic form (Appendix D item 1's `…-DETERMINISTIC-NONVISUAL-V1` pattern: harness tests + web build/boot + state/geometry assertions, screenshots dropped from the predicate) and `NAIL-P0-VIS-001` becomes `WAITING_EXTERNAL` with an explicit release limitation. **This choice is made before dispatch and cannot change afterwards.**
- **Provider/model freeze:** discover the existing authenticated FreeLLMAPI configuration (Hermes config / env / credential store — **never print or copy secrets** into logs, prompts, commits, or chat). Run **one pre-experiment three-model smoke comparison** across currently-available zero-marginal-cost FreeLLMAPI models; select the strongest sensible **mid-tier coding/tool-use model**; record the exact provider + model ID; **freeze it**. Pre-approved by the owner — no further approval needed. **No model switching after run 1.**
- **Hermes CLI template:** derive the exact supported worker-launch syntax from the installed `hermes --help` + provider config + CLI version; validate with **one throwaway smoke invocation**; freeze and record the command template (fresh-session/non-interactive mode, provider, model, working directory, task packet path, permission/tool mode). **Do not guess flags from an older Hermes version.**
- **Environment sampling:** wire host-resource sampling every **15 s** per attempt (total CPU, experiment-worker CPU, foreign CPU, load average, free/available RAM, swap, disk free).

**A-05 — Remote backup.** If authenticated private GitHub access exists: push the current protected baseline to the private remote and tag/record the frozen SHA. **Never push** `.hermes/experiments/`, `.hermes/logs/`, `.hermes/worktrees/`, `.hermes/evidence/`, provider credentials, environment dumps containing secrets, or temporary attempt branches. If GitHub auth is unavailable, this does **not** block — verify a separate local backup and record `NO_REMOTE_BACKUP` as an operational risk. During execution: **after every accepted canonical integration, push the resulting canonical commit.**

**Phase A commissioning gate — Phase B may not start until all are true:**

```text
[ ] canonical baseline SHA frozen and recorded
[ ] verify.sh exists, executable, and runs end-to-end
[ ] run-checks.js exists and discriminates the current baseline
[ ] lint script exists and passes
[ ] harness independently reviewed by a fresh session → PASS
[ ] harness + packet template hashed; harness-sha.json / packet-sha.json written
[ ] requirement ledger re-baselined honestly against current code
[ ] dependency edges (Appendix D item 5) attached to every requirement
[ ] every P0 requirement has a FROZEN acceptance contract (or explicit hardware-limited contract)
[ ] browser/screenshot capability decided and recorded (visual vs deterministic-nonvisual)
[ ] provider + model frozen and recorded
[ ] Hermes worker-launch command template validated and frozen
[ ] environment sampling enabled
[ ] git isolation strategy verified (worktree/branch per attempt)
[ ] budget counters initialised; provider-abort and environment-abort rules loaded
[ ] AR device-capability question answered (§4.5) and recorded
```


...[TRUNCATED 375693 chars]...
nt that could have validated or falsified the early autonomous-system assumptions.

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

📄 @file:`.hermes/attachments/Pasted content (3.6 KB)` (931 tokens)
```
Goal.** Take the existing Expo/React Native app at `/home/ash/Desktop/nailify` from its verified current state (HEAD `f5f33f249e6ad9d38aeaa7fb0f25c52f0ffb8ca6`, branch `main`, clean) to a polished, genuinely usable consumer MVP whose core experiences are:
1. an excellent **individual nail + full ten-nail set designer**,
2. a convincing **live AR try-on** on the user's real hand,
3. a beautiful, coherent, production-quality mobile app shell around those two core features.
The MVP should feel like something a real consumer could download and enjoy — **not a developer demo, wireframe, debug tool, or UI kit showcase**. The one-sentence mission (V3 §0, verbatim): *"Transform the existing Nailify prototype into Nailed It: a premium, user-friendly mobile nail-design app whose core experiences are: 1. an excellent individual nail + full set designer, 2. a convincing live AR try-on on the user's real hand, 3. a beautiful, coherent, production-quality mobile app shell around those two core features."*
**Start condition.** This session receives the complete document, reads it fully (all appendices), verifies the §2 state facts on disk, and begins Phase A (§4.1).
**Stop condition.** The goal is complete when the Definition of Done in §4.8 is met — i.e., when the deterministic release gate sets `SHIPPED`. Alternative stop: a tripwire (§4.9) fires with no autonomous path forward, in which case the system checkpoints state and notifies the owner (genuine blockers only). Or: explicit user cancellation (`.hermes/STOP` / `CANCELLED_BY_USER`).
**CLEAR CRITERIA OF SUCCESS (all must be true, each independently checkable — the goal may not be declared finished otherwise):**
| # | Criterion | How it is checked |
|---|---|---|
| S1 | `verify.sh` exists at `app/verify.sh`, is the **sole acceptance authority**, passes at the release SHA, and its protected files are hash-verified unchanged | `cd app && bash verify.sh` exit 0; `sha256sum` vs `.hermes/state/harness-sha.json` |
| S2 | Every one of the 36 mandatory P0 requirements (Appendix B §6 ledger) has a **FROZEN acceptance contract** and is either (a) PASS with current-SHA evidence, or (b) explicitly `hardware-limited` with the strongest legitimate substitute evidence and a recorded release limitation | `.hermes/state/acceptance-contracts/` + `verify.sh` output at release SHA |
| S3 | The mandatory **27-step 10-minute user story** (V3 §67, Appendix E) runs end-to-end without failure, with session log + screenshots tied to the release SHA | QA evidence in `.hermes/evidence/` |
| S4 | **Zero visible fake flows** in normal P0 navigation (no "simulated", "preview build", "coming soon", fake sign-in/purchase/AI/QR) | `grep -RniE 'TODO\|FIXME\|stub\|simulated\|mock\|coming soon\|placeholder\|preview build' app/src app/app.json` → 0 matches in P0 flows |
| S5 | **Independent review** of the full P0 release diff completed by a fresh session that did not implement it (schema/migration, persistence/deletion, state/undo, AR/native, security/privacy, navigation/state, control plane, release candidate, large builder changes — all reviewed) | `REVIEW_QUEUE.md` R-states = PASS with reviewer identity |
| S6 | `SHIPPED` set **only** by the release gate, atomically, with the release record in `.hermes/state/release.json` (SHA + checklist results + reviewer identity) | `.hermes/state/release.json` |
**The anti-goal:** do not optimize continuity (uptime, sessions, commits, task counts). The single metric is **independently accepted product changes per day, verified against the requirement ledger at the current SHA**. If that line is flat while workers are "alive", the architecture is irrelevant (retrospective §36/Q9, Appendix C).
```

===== 2026-09-22 04:13 | session 20260922_021616_abfb3d | Nailify to Nailed It MVP polish =====
You are being resumed automatically by a watchdog because this session appeared idle (no active turn, no recent activity). Do NOT restart from scratch and do NOT re-read the entire master prompt document again. First check your own current state on disk (.hermes/CHECKPOINT.md, .hermes/state/project.db, .hermes/WORK_QUEUE.json / work-queue, most recent WorkItem/attempt). Then answer for yourself: WHAT IS STILL LEFT TO DO OF THIS PROJECT? Then immediately continue driving the Nailed It MVP build forward with real actions (not just planning or summarizing) toward the Definition of Done in the goal document. If the deterministic release gate already declared SHIPPED, or you are genuinely blocked with no autonomous path forward (a real tripwire), say so plainly and stop. Otherwise keep working — do not wait for further input.

===== 2026-09-22 10:57 | session 20260922_105531_432d90 | AI staff force set up =====
@file:.hermes/attachments/FORENSIC_RETROSPECTIVE.md

I want you to analyse the find and download forensic ward at Markdown chat. In there, we discuss how to set up an autonomous system to create a software product autonomously using hermes.

--- Attached Context ---

📄 @file:.hermes/attachments/FORENSIC_RETROSPECTIVE.md (19874 tokens)
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

- Deterministic sc
...[TRUNCATED 19276 chars]...
 Directors, Meta-Directors), the worktree fleet, CAO as currently structured, persistent managers, mega-prompt constitutions, the 5-product portfolio, recovery features for unexercised failure modes, and the heartbeat-as-health instrumentation.

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
@image:/home/ash/.hermes/images/upload_20260922_105742_1.png

===== 2026-09-22 11:23 | session 20260922_105531_432d90 | AI staff force set up =====
@file:.hermes/attachments/00_READ_ME_FIRST.md
@file:.hermes/attachments/11_HERMES_EXECUTION_HANDOFF_PROMPT.md
@file:.hermes/attachments/EMPIRIUM_STUDIO_COMPLETE_PRODUCT_BRIEF.md

--- Attached Context ---

📄 @file:.hermes/attachments/00_READ_ME_FIRST.md (1824 tokens)
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

📄 @file:.hermes/attachments/11_HERMES_EXECUTION_HANDOFF_PROMPT.md (2043 tokens)
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

📄 @file:.hermes/attachments/EMPIRIUM_STUDIO_COMPLETE_PRODUCT_BRIEF.md (24978 tokens)
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
-
...[TRUNCATED 55225 chars]...
nt
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

```

===== 2026-09-22 11:24 | session 20260922_105531_432d90 | AI staff force set up =====
@file:.hermes/attachments/EMPIRIUM_STUDIO_COMPLETE_PRODUCT_BRIEF-2.md
@file:.hermes/attachments/00_READ_ME_FIRST-2.md
@file:.hermes/attachments/11_HERMES_EXECUTION_HANDOFF_PROMPT-2.md

--- Attached Context ---

📄 @file:.hermes/attachments/EMPIRIUM_STUDIO_COMPLETE_PRODUCT_BRIEF-2.md (24978 tokens)
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

📄 @file:.hermes/attachments/00_READ_ME_FIRST-2.md (1824 tokens)
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

📄 @file:.hermes/attachments/11_HERMES_EXECUTION_HANDOFF_PROMPT-2.md (2043 tokens)
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