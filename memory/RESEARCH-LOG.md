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

## 2026-07-10 — YouTube Intel
| Channel | Video | Regime Signal | Relevance |
|---------|-------|----------------|-----------|
| Bravos Research | Something Just Broke in the Financial System... | Title-only (transcript blocked): possible risk-off/stress signal | Med |
| George Gammon | This Multi Trillion Dollar Bubble May Have Just Broken The Economy | Title-only: bearish/crisis narrative, potential HIGH_VOL setup | Med |
| George Gammon | Are We On The Brink Of Another Financial Crisis? | Title-only: bearish/crisis narrative, reinforces above | Med |
| IG France (Baradez) | Le Japon sous haute surveillance des marchés (yen, BoJ, inflation) | Title-only: BoJ/yen catalyst — potential vol regime driver | Med |
| IG France (Baradez) | MarketLive: tendances graphiques des marchés | Title-only: routine market-daily technical update | Low |
| IG France (Baradez) | Fibonacci & Retracements | Title-only: pure TA education, no macro signal | Low |
| IG France (Baradez) | Ce qui fait la différence en trading | Title-only: trading psychology/education, no macro signal | Low |
| Oseille TV | Assurance vie: Luxembourg vs France | Wealth-mgmt (tax/insurance), no regime signal | Low |
| Oseille TV | 6 mois de prison pour un journaliste | Not finance-relevant | None |
| Oseille TV | Ceux qui méprisent l'argent... | Motivational, no regime signal | Low |
| Finary | Vous devez migrer vos cryptos ? | Wealth-mgmt (crypto), no regime signal | Low |
| Finary | Le plan pour construire sa richesse en famille | Wealth-mgmt (family finance), no regime signal | Low |
| Finary | À 37 ans, il a parié tout son PEA sur une action | Wealth-mgmt (risk/diversification cautionary tale) | Low |
| Investing Simplified (Prof G) | How to Make $4,100/Month in Dividends | Wealth-mgmt (income investing), no regime signal | Low |
| Investing Simplified (Prof G) | $2 Million Invested - Can I retire soon? | Wealth-mgmt (retirement), no regime signal | Low |
| Investing Simplified (Prof G) | The Real Reason Your Portfolio Isn't Growing Faster | Wealth-mgmt (general), no regime signal | Low |

Note: youtube-transcript-api blocked by YouTube (cloud-provider IP ban) for all 16 videos today. Analysis is title/metadata-only — confidence capped at Medium. Real Vision Presents: no new videos.
