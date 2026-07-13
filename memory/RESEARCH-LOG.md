# Research Log — regime_trader

Daily regime detection entries appended here.
Format:

## YYYY-MM-DD — Regime Detection

### Account
- Equity: $X
- Cash: $X
- Open positions: N

### Regime Signal
- Detected regime: LOW_VOL / MID_VOL / HIGH_VOL
- Confidence: X%
- Consecutive bars: N
- Flickering: yes/no

### ETF Snapshot (from Alpaca REST)
- SPY: $X (Xd chg: X%)
- QQQ: $X (Xd chg: X%)
- IWM: $X (Xd chg: X%)

### Cross-Enrichment Signal (from trading-bot)
- Sector momentum: X
- Active earnings/catalyst risk: yes/no (detail)
- Regime gate: OPEN / BLOCKED

### Signals Generated
| ETF | Side | Shares | Entry | Stop | Conf | Reason |
|-----|------|--------|-------|------|------|--------|

### Decision
TRADE or HOLD

## 2026-07-13 — YouTube Intel

**Transcripts blocked** — YouTube rejects cloud-provider IPs (IP ban), all 19 videos returned NO_TRANSCRIPT. Signals below are title-only inference, low confidence, background context only — not actionable.

| Channel | Video | Regime Signal | Relevance |
|---------|-------|----------------|-----------|
| George Gammon | The Next Subprime Crisis Was Just Triggered...Bigger Than 2008 | Risk-off framing (title only) | Low — no transcript |
| George Gammon | This Multi Trillion Dollar Bubble May Have Just Broken The Economy | Risk-off framing (title only) | Low — no transcript |
| Bravos Research | Something Just Broke in the Financial System... | Risk-off framing (title only) | Low — no transcript |
| IG France | VIX (volatilité) : un rebond marqué...puis une détente | Title implies vol spike then fade — consistent w/ MID→LOW vol mean-reversion | Low — no transcript, title-only |
| IG France | Le Japon sous haute surveillance (chute du yen, BoJ, inflation) | JPY/BoJ catalyst flagged | Low — no transcript |
| IG France | MarketLive x3, Fibonacci retracements | Routine technical content, no vol signal in title | None |
| Prof G | 🚨BREAKING: 2026 Market Outlook (Expect Major Change in July) | Vague "major change" framing | Low — no transcript |
| Finary, Oseille TV | wealth-mgmt/lifestyle content | n/a | Wealth-mgmt only |

No transcript content → cannot confirm cross-channel vol consensus or feed HMM. See reports/2026-07-13-youtube-intel.md for full writeup.
