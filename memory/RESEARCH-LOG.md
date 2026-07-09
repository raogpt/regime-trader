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

## 2026-07-09 — YouTube Intel

NOTE: youtube-transcript-api blocked by YouTube (cloud-provider IP ban) — all 17 new videos returned title/metadata only, no transcript text. Signals below are title-only, LOW confidence. See reports/2026-07-09-youtube-intel.md for full detail.

| Channel | Video | Regime Signal | Relevance |
|---------|-------|----------------|-----------|
| George Gammon | This Multi Trillion Dollar Bubble May Have Just Broken The Economy | Risk-off / crisis framing → HIGH_VOL bias (title-only) | High |
| George Gammon | Are We On The Brink Of Another Financial Crisis? | Risk-off framing, echoes above | Medium |
| Bravos Research | Something Just Broke in the Financial System... | Risk-off / crisis framing → HIGH_VOL bias, corroborates Gammon | High |
| IG France (Baradez) | Le Japon sous haute surveillance (yen, BoJ, inflation) | Macro catalyst watch: JPY/BoJ — could spill into global vol regime | Medium |
| IG France (Baradez) | Fibonacci & Retracements : Zones d'Entrée | Technical-analysis, no regime signal | Low |
| IG France (Baradez) | MarketLive x2, Ce qui fait la différence en trading | Routine market commentary, no regime signal | Low |
| Finary | Le plan pour construire sa richesse sur plusieurs générations | Wealth-mgmt, generational allocation | Wealth mgmt |
| Finary | À 37 ans, il a parié tout son PEA sur une seule action | Cautionary tale re: concentration risk | Wealth mgmt |
| Investing Simplified (Prof G) | How to Make $4,100/Month in Dividends | Wealth-mgmt, income strategy | Wealth mgmt |
| Investing Simplified (Prof G) | $2 Million Invested - Can I retire soon? | Wealth-mgmt, retirement | Wealth mgmt |
| Investing Simplified (Prof G) | The Real Reason Your Portfolio Isn't Growing Faster | Wealth-mgmt, generic | Wealth mgmt |
| Oseille TV | Assurance vie: Luxembourg vs France | Wealth-mgmt, tax/expat | Wealth mgmt |
| Oseille TV | 6 mois de prison pour un journaliste | Not market-relevant | None |
| Oseille TV | Ceux qui méprisent l'argent | Money mindset, not market-relevant | Low |
| Oseille TV | L'impôt te transforme en prisonnier | Tax/expat commentary | Wealth mgmt |
| Real Vision Presents | (no new videos) | — | — |

Cross-channel consensus: George Gammon + Bravos Research both titled around a systemic "break"/crisis theme this week (title-only, unverified) — soft risk-off signal, not actionable without transcript confirmation or price/vol confirmation from HMM.
