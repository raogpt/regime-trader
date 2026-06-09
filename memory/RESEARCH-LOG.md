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

## 2026-06-09 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|--------------|-----------|
| Bravos Research | A Once in a Lifetime Economic Reset is Coming. | HIGH_VOL / BEARISH | ★★★ |
| Bravos Research | History is About to Be Made. | HIGH_VOL / BEARISH | ★★★ |
| Investing Simplified (Prof G) | 🚨BREAKING: Markets Are Starting to Crack | HIGH_VOL / BEARISH | ★★★ |
| Investing Simplified (Prof G) | The AI & Quantum Boom Is Just Starting | LOW_VOL / RISK-ON (QQQ bias) | ★★ |
| Real Vision Presents | Retail Is Going to Get REKT by These IPOs! | HIGH_VOL / BEARISH | ★★★ |
| Real Vision Presents | The Real Opportunity Isn't What You Think! | CONTRARIAN / AMBIGUOUS | ★★ |
| Real Vision Presents | A New Frontier in Gold Exploration | DEFENSIVE / FLIGHT-TO-SAFETY | ★★ |
| IG France (Baradez) | Opportunité ou piège pour les investisseurs? | CAUTIOUS / MID_VOL | ★★★ |
| IG France (Baradez) | MarketLive ×4 sessions (06/03–06/09) | TECHNICAL — no vol signal | ★★ |
| Oseille TV | Quitter la France : ne laissez rien au fisc | WEALTH MGMT PRIORITY — tax | ★★★ |
| Oseille TV | Aux USA 90% n'ont RIEN, 10% contrôlent TOUT | Macro inequality context | ★★ |
| Oseille TV | La Chine se venge de 150 ans d'humiliation | GEOPOLITICAL RISK / macro | ★★ |
| Finary | Comment éviter l'impôt sur le revenu à vie | WEALTH MGMT PRIORITY — tax | ★★★ |
| Finary | La vie folle de la famille la plus riche d'Asie | Background | ★ |

**Cross-channel consensus (3/5 macro channels):** HIGH_VOL / BEARISH tilt — treat as forward caution signal for HMM validation.
**Note:** Transcripts unavailable (YouTube API restricted in cloud env). Analysis based on titles only. Confidence: MEDIUM.
