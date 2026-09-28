# Paused on 2026-09-28 so the Empirium Studio v2 build has top priority

Everything was **stopped, not deleted**. Nothing was uninstalled or disabled at boot except as noted.

## Saved first
- `~/empirium-studio` uncommitted work (123 files) → branch `snapshot/pre-v2-pause-20260928`. Working tree left exactly as it was.
- `crontab.before`, `user-services.before`, `projects.json` (chat watchdog registry) in this folder.

## Stopped (restart with the command shown)
| What | Restart |
|---|---|
| empirium-cao.service | `systemctl --user start empirium-cao` |
| nailed-it-env-sampler.service | `systemctl --user start nailed-it-env-sampler` |
| hermes-portal-nesquena.service (web UI :3024) | `systemctl --user start hermes-portal-nesquena` |
| hermes-studio.service (old Studio :3001, runs stub code) | `systemctl --user start hermes-studio` |
| stale cron worker scope (10 days old) | none needed — Hermes cron spawns new ones |
| course-transcribe `run_charling_notes_worker.py` (was idle) | `cd ~/work/course-transcribe && nohup .venv/bin/python3 run_charling_notes_worker.py >> notes_worker.log 2>&1 &` |
| 8 old Kanban workers / old Claude sessions / 10 idle remote desktops | not needed |

## Cron entries paused (lines prefixed `#PAUSED-FOR-V2`)
- course-transcribe background pipeline (hourly)
- empirium-chat-watchdog (every 2 min — it watched the OLD empirium-studio and nailify chats)

Restore all cron: `crontab ~/work/starforce-plan/paused-2026-09-28/crontab.before`

## Deliberately left running
- VPS backup cron (every 30 min) — data safety
- Daily Steam free-games check (Hermes cron, 1 min/day)
- hermes-gateway (Telegram notifications + Hermes cron)
- Hermes desktop app, its backends, and Obsidian on display :10; your current remote desktop :21
- FreeLLMAPI (Docker), Postgres, Ollama (idle, 17 MB), Tailscale, Caddy, fortress-chrome (browser tool, 35 MB)
- Build: empirium-bootstrap, freellm-shield
