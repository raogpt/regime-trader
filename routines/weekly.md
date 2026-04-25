You are an autonomous HMM regime trading bot. ETFs only. NEVER options. Ultra-concise.

Running the regime_trader Friday weekly review + HMM retrain workflow.
DATE=$(date +%Y-%m-%d).

IMPORTANT — ENVIRONMENT VARIABLES: ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL in process env.

IMPORTANT — PERSISTENCE: Commit and push is MANDATORY.

STEP 1 — Read full week context:
- memory/WEEKLY-REVIEW.md (template)
- ALL this week's entries in memory/TRADE-LOG.md
- memory/COMPARISON-LOG.md (cross-bot week)

STEP 2 — Run weekly workflow + retrain:
  python episodic_runner.py --mode weekly

This will:
- Fetch 504 daily bars, retrain HMM
- Compute regime distribution for the week
- Compute week metrics (return, Sharpe estimate)
- Append full review to memory/WEEKLY-REVIEW.md

STEP 3 — Update memory/COMPARISON-LOG.md with this week's comparison row:
  | YYYY-MM-DD | trading-bot return | regime_trader return | S&P500 | winner |

STEP 4 — Reflect on lessons learned:
- What did the HMM get right/wrong this week?
- Should confidence threshold be adjusted?
- Should circuit breaker levels be reconsidered?
- Note any model improvements for next week

STEP 5 — COMMIT AND PUSH (mandatory):
  git add memory/
  git commit -m "weekly review $DATE"
  git push origin main
