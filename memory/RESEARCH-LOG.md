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

## 2026-05-05 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Oseille TV | Ces 12 pays ne prélèvent AUCUN impôt (pour l'instant) | None — wealth/tax content | HIGH (UEMOA/expat) |
| Bravos Research | History is About to Be Made. | HIGH_VOL / macro inflection | ★★★ catalyst watch |
| Finary | Comment déceler les objectifs financiers irréalistes ? | None | LOW regime / MEDIUM wealth |
| Finary | Les gérants de fonds peuvent-ils encore faire la différence ? | Mild HIGH_VOL (active mgmt debate) | MEDIUM — supports ETF-only |
| Finary | Ce marché est en train de tout faire basculer | HIGH_VOL / risk-off | ★★ regime signal |
| Investing Simplified (Prof G) | 🚨 EXTREME Market Update: How to invest now May 2026? (S&P 500 ATH) | MID→HIGH vol boundary; ATH confirmed | ★★★ key context |
| Investing Simplified (Prof G) | You Do NOT Need $1.46 Million to Retire. | None | MEDIUM wealth mgmt |
| IG France (Alexandre Baradez) | MarketLive : Analysons les dernières tendances graphiques | Technical — direction unclear | ★★★ freshest signal (2026-05-04) |
| IG France (Alexandre Baradez) | Le cockpit d'un expert — Marc Dagher ProRealTime | Technical S/R levels | ★★ chart context |
| Real Vision Presents | Top Picks in the Gold Miners | HIGH_VOL / risk-off (gold rally) | ★★★ cross-asset confirm |

**Cross-channel consensus:** MID_VOL base / HIGH_VOL tail risk. 3 channels signal elevated stress. Gold miners + "overturning market" = risk-off. S&P ATH (Prof G) is conflicting bullish signal. Recommended stance: 60-75% allocation, SPY > IWM, hold IWM sizing at 50% until 3-bar regime confirms.

Full report: reports/2026-05-05-youtube-intel.md
