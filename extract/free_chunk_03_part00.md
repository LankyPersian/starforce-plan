<!-- model=deepseek-v4-flashfree effective=deepseek-v4-flash:free -->
5, so moderate length. Need include all important requirements. Need organize.

Need "Autonomy/orchestration + complaints about past failures": The specs are about autonomous orchestration. Need include complaints about past failures? User says "jesus fucking christ, look at what we are building, i have told you no open router credits" - this is frustration/complaint, likely past failure of using OpenRouter credits. Also spec mentions "previous installation a sudo-related configuration issue was encountered" - that's a complaint about past failure? Also "You previously installed and extensively tested" etc. "New evidence now establishes..." not complaint. "Do NOT repeat already-proven work unnecessarily." Need include under Autonomy/orchestration + complaints about past failures any explicit mentions of past failures: "During previous installation a sudo-related configuration issue was encountered." "Do not reduce all failures to 'director exited.'" "A multi-day autonomous build can fill a disk." "The current append-only directive JSONL mechanism correctly produces recovery instructions." "Do not use unsafe patterns such as pkill codex, killall node." "No fork bomb occurred." "No lost updates." "Don't endlessly improve." "Do not start Empirium Studio build until after certification." "Stop after supervisor certification." "Next task: register real Empirium meta-orchestrator project and begin AI workforce build." These are orchestration requirements.

Need "Corrections/reversals (with dates)": 
- 2026-09-17: "I have told you no open router credits, use sonnet 5 via subscription for claude pro and codex subscription" - correction to model routing.
- "Do NOT rebuild/replace/repeat previously proven work" - correction to avoid redoing.
- "Do NOT perform a dangerous global rename" - correction to model-agnostic renaming.
- "DO NOT pretend this is a scoped change" - correction about AppArmor global sysctl.
- "Do not use pkill/killall" - correction/rejected approach.
- "DO NOT blindly invent AppArmor rules" - correction.
- "DO NOT start the Empirium Studio build" / "Stop after supervisor certification" - reversal? It says "The next task after successful certification is REGISTER THE REAL EMPIRIUM..." but "Do not start the Empirium Studio build." That's a boundary.
- "FREEZE SUPERVISOR V2. Do not perform a V3 hardening pass unless real production evidence later reveals a defect." - reversal of endless improvement.
- "Do not silently invent defaults" - correction.
- "Do not silently discard fields" - correction.
- "Do not put tokens or credentials in artifact" - correction.
- "Do not keep in-memory-only timer" - correction.
- "Do not require user to manually tell project continue" - correction.

Need "Rejected approaches": 
- Rebuild/replace/repeat proven work.
- pkill codex, killall node, process-name matching.
- Large container orchestration stack for process isolation.
- Distributed consensus, Redis, Kafka, Kubernetes, external workflow engines, separate databases solely for supervisor, microservices, web dashboards, AI reasoning inside supervisor.
- OpenRouter credits.
- Paid API fallback.
- Marking subscription-unavailable as project failure/completion.
- Editing/removing lines from historical JSONL.
- chmod 777.
- Blindly inventing AppArmor rules.
- Pretending sysctl is scoped.
- Silently inventing defaults/blank state over corrupt data.
- Large plugin framework.

Need "Open questions": The user asks "is this fully done now" - open question. Also spec has "Investigate whether there is a supported narrower mechanism..." - open question. "Evaluate, in order of simplicity/safety: dedicated process group/session; existing systemd user transient scope" - open question to be decided. "Implement project generation/epoch feature unless source inspection proves an equivalent mechanism already exists." - open question. "Whichever design is selected must survive..." - open choice between ACK approaches. "Possible areas to investigate: narrowly scoped AppArmor profile; supported bubblewrap/AppArmor accommodation; Codex-supported sandbox mechanism" - open. "If no safe supported narrower approach can be proven: KEEP current..." - open. "Audit remaining long-running control files" (truncated) - open. Need list.

Need perhaps include "Visual/design: none" but also "No great narrative" final response format? That's not visual.

Need structure carefully.

Need use markdown headings exactly: Names/aliases; Product requirements; Visual/design; Architecture/tech; Model/LLM routing; Autonomy/orchestration + complaints about past failures; Corrections/reversals (with dates); Rejected approaches; Open questions.

Need prefix each bullet [2026-09-17]. For all.

Need maybe include "verbatim quotes where decisive" - use quotes from user. Need not overquote? Use short quotes.

Need ensure no invention. If we include "Sonnet 5" as model, quote.

Need perhaps mention "claude pro" subscription. User says "use sonnet 5 via subscription for claude pro and codex subscription". So Model/LLM routing: "No OpenRouter credits. Use Sonnet 5 via subscription for Claude Pro, and Codex subscription." Also from spec: "current verified backend adapter: codex-subscription, effective model: gpt-6-astra" "authentication mode is ChatGPT subscription; stored API key=false; stored ChatGPT tokens=true; actual available model observed locally is gpt-6-astra" "direct API billing credentials not required." Need include.

Need maybe "Claude subscription launcher should implement its own equivalent attestation" - future. "Another project could later use adapter: claude-subscription model: <verified model> or adapter: freellmapi model: <verified free model>".

Need "No paid inference: PAID INFERENCE: $0 authorized, $0 observed" from final response format. Also zero-paid enforcement: strip API keys, reject paidEmergency.enabled=true, reject maxUsdPerProject > 0. Need include in Model/LLM routing and Architecture.

Need "director process identity via PID + /proc start-time fingerprint; PID reuse not accepted." Good.

Need "systemd user service; linger enabled; Ubuntu 24.04.4; Node v26.8.1; systemd 255; ash has linger=yes." Could include in Architecture/tech.

Need "systemd unit with ProtectHome=read-only + ReadWritePaths=/home/ash/.codex" specific.

Need "supervisor.selftest only registered; Empirium Studio project NOT registered; service active/enabled/healthy."

Need "real Codex subscription sentinel passed; nonce read; heartbeat; receipt matched; checkpoint; relaunch; resume; completion SHIPPED; sentinel removed."

Need "cross-process state mutex; stale lock recovery; state reread inside lock; 40-way mutation stress; 45 concurrent CLI ops."

Need "director log retention capped at 30."

Need "state schema versioning etc."

Need perhaps "SUPERVISOR_INSTALLATION_CERTIFICATE.json" etc.

Need maybe "backup under /home/ash/.local/state/empirium-supervisor/install-evidence/pre-v2-backup/"

Need "final rule freeze V2."

Need perhaps "The supervisor must never say 'checkpoint saved' when write failed."

Need "wall-clock backwards no immortal lease; forward no kill all without sanity checks."

Need "project Generation authoritative: stale generation mutations rejected."

Need "child lease generations: actorId = ui-project-manager, leaseId = ui-project-manager-0007" - maybe not necessary but can include.

Need "Bounded control-plane storage: director logs 30-file cap; audit remaining control files" - spec truncated. Need mention.

Need "Open questions" include "What exactly is in the truncated section 10 'Bound control-plane storage' audit?" Not necessary? It's an open question because spec cut off. But user pasted truncated content. Could include "Remaining control-file audit content from section 10 was truncated in pasted spec." That is fact.

Need perhaps "is this fully done now" as open question.

Need "No visual/design" maybe.

Let's draft.

Need be careful with "Names/aliases" include "Empirium deterministic heartbeat supervisor" and "Empirium Supervisor", "Empirium Studio" etc. Also "meta-director", "empirium-ai-director", "luna-master", "empirium-luna-director", "codex-subscription", "supervisor-selftest". Also "AI workforce build" alias? User's product. Need include.

Need perhaps "Empirium workforce supervisor service: empirium-workforce-supervisor.service" from paths. Include.

Need "Product requirements" perhaps combine with "Architecture/tech"? But headings separate. Product requirements should be high-level user-facing. Architecture/tech more implementation. Need avoid duplication. But many specs are technical. We can cross-reference.

Need maybe "Product requirements" include:
- "Install Empirium deterministic heartbeat supervisor" (user message title).
- "Targeted V2 reliability hardening; incremental changes only."
- "Close distinction between PROCESS ALIVE and PROJECT ACTUALLY ADVANCING."
- "Progress watchdog, directive ACK, safe process-tree containment, model-agnostic, subscription attestation, AppArmor review, hot config, state snapshot, storage bound."
- "Rollback, schema versioning, idempotency, generations, health summary, isolation, quota handling, auth expiry, security, atomic ops, disk/clock robustness, tests, evidence, certification, freeze."
Need perhaps all in Product requirements? But then Architecture/tech duplicates. We can put detailed technical under Architecture. Product requirements as "what to build" in summary.

Need "Visual/design" none.

Need "Architecture/tech" with many bullets.

Need "Model/LLM routing" include no OpenRouter, Sonnet 5/Claude Pro, Codex subscription, gpt-6-astra, adapters, attestation, zero-paid, no API-key billing, exit classification for subscription limits, auth expiry states.

Need "Autonomy/orchestration + complaints about past failures" include "supervisor is infrastructure not product; freeze V2; don't endlessly improve; don't start Empirium Studio until certified; next task register meta-orchestrator; previous sudo config issue; "jesus fucking christ" frustration with OpenRouter credits; "director exited" oversimplification; no fork bomb; no lost updates; "Do not reduce all failures to 'director exited.'" etc.

Need "Corrections/reversals" include from spec.

Need "Rejected approaches" include "OpenRouter credits" and "paid API fallback" and "pkill/killall" etc.

Need "Open questions" include "is this fully done now?" and "narrow AppArmor mechanism?" etc.

Need perhaps include "Date" for short messages: same date. Could include "2026-09-17 (18:54)"? Instructions "with dates" only. We can use [2026-09-17] all.

Need maybe "session" not necessary.

Need maybe mention "v2 updates should not start Empirium Studio build; stop after certification." Good.

Let's write with bullets each prefixed. Need ensure no empty headings. For Visual/design: "None stated." prefixed with date? " [2026-09-17] No visual/design requirements were stated in these messages." Good.

Need maybe "Product requirements" not too long. Let's craft.

Need ensure "verbatim quotes where decisive": we can include e.g. "A HEARTBEAT MUST NOT count as progress." "Do NOT rebuild it. Do NOT replace it." "jesus fucking christ, look at what we are building..." "Do not start the Empirium Studio build." "FREEZE SUPERVISOR V2." etc.

Let's produce.

Need maybe "Names/aliases" bullets:
- [2026-09-17] "Empirium deterministic heartbeat supervisor" / "Empirium Supervisor" (from attachment title).
- [2026-09-17] "Empirium Studio" — the real build project, to be registered only after supervisor V2 certification.
- [2026-09-17] "AI workforce build" / "Empirium meta-orchestrator project" — next task after certification.
- [2026-09-17] Historical names to migrate with backward compatibility: "luna-master" -> "meta-director"; "LUNA_RECOVER_OR_REPLACE_CHILD" -> "DIRECTOR_RECOVER_OR_REPLACE_CHILD"; "empirium-luna-director" -> "empirium-ai-director" (canonical), with compat symlink/wrapper.
- [2026-09-17] "codex-subscription" adapter; future "claude-subscription", "freellmapi".
- [2026-09-17] "supervisor-selftest" disposable project.
- [2026-09-17] "empirium-workforce-supervisor.service" systemd user service.

Need maybe "Empirium Studio" vs "Empirium studio build" - user says "Do not start the Empirium Studio build." Good.

Need "Product requirements" perhaps:
- [2026-09-17] Install the Empirium deterministic heartbeat supervisor with targeted V2 reliability hardening; "Existing installation is accepted. Incremental changes only."
- [2026-09-17] Do not rebuild/replace/repeat already-proven work; regression-test existing features after changes.
- [2026-09-17] Add progress watchdog distinct from heartbeat with durable progress state and CLI `supervisor.mjs progress`.
- [2026-09-17] Add directive acknowledgement with durable ACK, CLI `supervisor.mjs directives` / `directive-ack`, idempotent directives, no JSONL editing.
- [2026-