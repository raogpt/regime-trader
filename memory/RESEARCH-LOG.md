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

---

## 2026-05-31 — YouTube Intel

> Note: Transcripts unavailable (YouTube cloud IP block). Analysis from titles + channel context.

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Bravos Research | The UNTHINKABLE is About to Happen to Stocks (Emergency Update) | HIGH_VOL warning, risk-off | ★★★ |
| Investing Simplified | 🚨CAUTION: Quiet Tax the New Fed is About to Charge Every Investor | Fed/inflation headwind, macro risk | ★★ |
| Investing Simplified | The Only Retirement Video You Ever Need to Watch | Retirement allocation, risk-neutral | ★ |
| Investing Simplified | 5 Best Stocks & Hottest Investing Sectors for 2026? | Risk-on outlook, sector rotation | ★ |
| IG France (Baradez) | MarketLive — tendances graphiques (×2, 05-27/05-28) | Daily TA market sessions, active market | ★★ |
| IG France (Baradez) | Comment vraiment maîtriser le RSI en trading | Educational RSI, no direct signal | — |
| Real Vision | It Said 2-Months... It Did It In Minutes! | Shock acceleration event → HIGH_VOL | ★★ |
| Real Vision | The Convergence: AI, DeFi, and the Next Financial System | Crypto macro theme, low ETF relevance | — |
| Real Vision | From Lagos to the World: Future of African Payments (Sui Miami) | Africa/UEMOA fintech — WEALTH MGMT ★ | ★★ |
| Real Vision | Sui Miami conference ×4 | Crypto/DeFi only, negligible regime relevance | — |
| Oseille TV | Votre argent en banque n'est plus à vous! | Banking security alert, wealth protection | ★★ WEALTH |
| Finary | De 0 à 1 million avant 40 ans : son plan est-il réaliste ? | Personal finance, wealth building path | ★ WEALTH |
| Finary | Le Japon perd 1 habitant toutes les 35 secondes — effondrement? | Japan macro risk, indirect global signal | ★ |
| Finary | L'achat que vous ne pouvez (normalement) pas payer | Consumer finance, low regime relevance | — |
| Finary | La richesse réelle de la famille royale britannique | Historical wealth, no signal | — |

**Cross-channel consensus:** Bravos Research + Prof G both flagging caution/risk-off → mild HIGH_VOL / MID_VOL lean. No green light for aggressive risk-on positioning.
