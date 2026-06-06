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

## 2026-06-06 — YouTube Intel

> Transcripts blocked (cloud IP). Signals inferred from titles + channel thesis patterns. 20 new videos across 6 channels.

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Bravos Research ★★★ | A Once in a Lifetime Economic Reset is Coming. | HIGH_VOL / risk-off | HIGH |
| Bravos Research ★★★ | History is About to Be Made. | MID→HIGH_VOL catalyst watch | MEDIUM |
| Real Vision ★★★ | The Real Opportunity Isn't What You Think! | MID_VOL / contrarian rotation | MEDIUM |
| Real Vision ★★★ | A New Frontier in Gold Exploration | Risk-off / inflation hedge signal | MEDIUM |
| Real Vision ★★★ | Stablecoins, ETFs, New Crypto Market Structure | ETF flow awareness | MEDIUM |
| IG France ★★★ | MarketLive x4 sessions (Jun 1–5) | Active/transitional market — elevated realized vol | HIGH |
| IG France ★★★ | Créer un Robot de Trading Automatique avec IA | Algo strategy comparison | LOW |
| Prof G | The AI & Quantum Boom Is Just Starting | LOW_VOL / QQQ-bullish | MEDIUM |
| Prof G | 🚨CAUTION: Quiet Tax the New Fed is About to Charge | HIGH_VOL catalyst — Fed policy risk | HIGH |
| Oseille TV | Une IA révèle des failles cachées depuis 17 ans ! | Uncertain / systemic risk | LOW |
| Oseille TV | Amazon FBA en 2026 : C'est fini ? | Wealth-mgmt / income diversification | WEALTH-MGMT |
| Finary | Il a tout calculé pour ne plus jamais travailler après 40 ans | FIRE / portfolio construction | WEALTH-MGMT PRIORITY |
| Finary | Ce que révèle cette émission TV sur la finance... | Finance media literacy | WEALTH-MGMT |
| Finary | Les dépenses absurdes de la famille la plus riche d'Asie | Wealth display analysis | WEALTH-MGMT |
| George Gammon ★★★ | (no new videos this week) | — | — |

**Cross-channel consensus:** Bravos Research + Real Vision both signal macro stress / risk-off (2+ ★★★ channels). IG France's above-average MarketLive cadence confirms elevated realized vol. **Net: MID_VOL → HIGH_VOL transition watch. Tighten stops if currently in LOW_VOL regime.**

**Wealth-mgmt priority:** Finary FIRE content + Prof G Fed-tax warning → review real-return optimization and UEMOA/Africa currency hedge strategy. Full report: `reports/2026-06-06-youtube-intel.md`
