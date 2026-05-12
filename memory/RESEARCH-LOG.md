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

## 2026-05-12 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Oseille TV | Passeport GRATUIT pour vos enfants (et pour vous ensuite) | NEUTRAL — expat/citizenship, no vol signal | Wealth-mgmt / expat |
| Bravos Research | The Next 6 Months Will Make History. | HIGH_VOL caution — historic inflection framing | ★★ macro |
| Bravos Research | Brace Yourself. | HIGH_VOL — explicit warning, risk-off tilt | ★★★ regime |
| Finary | Retraite à 45 ans... projet impossible ? Analyse de patrimoine | NEUTRAL — early retirement wealth analysis | Wealth-mgmt |
| Finary | Un système au bord du gouffre ? | HIGH_VOL — systemic risk framing | ★★ macro |
| Finary | Finary Life est disponible en gestion libre | NEUTRAL — product launch | Informational |
| Finary | Je quitte la chaîne Finary... ? | NEUTRAL — channel drama | Informational |
| Finary | Les États-Unis... en faillite technique ? | HIGH_VOL — US debt/fiscal risk-off signal | ★★★ macro |
| Investing Simplified (Prof G) | MAJOR BUY: Best Quantum Computing ETF on the Planet | LOW_VOL / risk-on — bullish ETF call | ★ retail sentiment |
| Investing Simplified (Prof G) | The 7 Money Rules 95% of Americans Break | NEUTRAL — financial literacy | Wealth-mgmt |
| Investing Simplified (Prof G) | $300,000 is ALL YOU NEED to live off dividends FOREVER | NEUTRAL — income/dividend strategy | Wealth-mgmt |
| IG France (Baradez) | MarketLive — tendances graphiques (2026-05-12) | LIVE — technical analysis, no transcript | ★★★ monitor |
| IG France (Baradez) | MarketLive — tendances graphiques (2026-05-11) | MID/HIGH — daily technical scan | ★★★ monitor |
| IG France (Baradez) | MarketLive — tendances graphiques (2026-05-07) | MID/HIGH — daily technical scan | ★★★ monitor |
| IG France (Baradez) | CFD chez IG : guide complet 2026 | NEUTRAL — product tutorial | Informational |
| IG France (Baradez) | MarketLive — tendances graphiques (2026-05-06) | MID/HIGH — daily technical scan | ★★★ monitor |
| Real Vision Presents | Sui Live Miami 2026 (Raoul Pal + guests) | RISK-ON — crypto/macro bull thesis | ★★ macro |

**Cross-channel consensus**: Bravos Research + Finary agree on elevated macro risk (HIGH_VOL bias). Conflicts with Prof G bullish retail ETF call and Real Vision crypto risk-on. Net: MID→HIGH vol transition, cautious positioning warranted.
