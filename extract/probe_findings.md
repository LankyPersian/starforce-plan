# FreeLLMAPI probe — 2026-09-28 ~14:50 BST (5 pings + 1 tool-call test per model)

| model | success | avg s | tool calls | failure |
|---|---|---|---|---|
| auto | 5/5 | 2.19 | yes | — |
| mistral-code | 5/5 | 0.33 | yes | — |
| codestral-2508 | 5/5 | 0.85 | yes | — |
| gpt-oss-120b | 5/5 | 1.08 | yes | — |
| mimo-v2.6-flashfree | 5/5 | 1.14 | yes | — |
| deepseek-v4-flashfree | 5/5 | 1.28 | yes | — |
| nemotron-3-super-120b | 5/5 | 1.37 | yes | — |
| glm-5.3 | 0/5 | — | — | 503 no usable provider key |
| glm-5.3-fast, kimi-k3-fast, qwen3.6-27b, qwen3.7-flash | 0/5 | — | — | 429: every key `out_of_credits`, cooldown ~10m |
| gemma-4-26b-a4b | 0/5 | — | — | 429; routed via **openrouter** `:free` |

Implications for the build design:
1. Failures are per-model and bursty (a whole model goes dark for 10+ min); pinning a task to one model = stall. Use a fallback ladder + per-model circuit breaker, with `auto` as last resort.
2. Error bodies are machine-readable (`rate_limit_error`, `out_of_credits`, "Soonest reset ~Nm") — parse the reset hint and open the breaker for that long.
3. Some pool routes go via OpenRouter free tier. User bans OpenRouter spending; `:free` routes cost $0 but the orchestrator must enforce a denylist on any non-free OpenRouter route and log effective route.
4. Only ping-level test; coding quality still needs a bounded benchmark task before model ranking.
