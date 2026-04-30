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

## 2026-04-30 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Oseille TV | Ces 12 pays ne prélèvent AUCUN impôt (pour l'instant) | None direct — zero-tax country expat planning | WEALTH MGMT ★★★ |
| Bravos Research | The Damage is done… | HIGH_VOL — post-drawdown damage assessment, bearish reflection | HIGH |
| Bravos Research | The UNTHINKABLE is About to Happen to Stocks (Emergency Update) | HIGH_VOL — emergency alert, extreme language around Apr 23 event | HIGH |
| Finary | Le secret le mieux gardé de la finance : le marché des devises | Weak macro — FX divergence, possible USD stress | MEDIUM |
| Finary | À 30 ans, ce salarié en marketing digital a fait le bon départ! | None | LOW |
| Finary | Qui est le Président français le plus riche ? | None | LOW |
| Investing Simplified (Prof G) | The Best Tax Strategy: How to Use a Donor Advised Fund | None direct — tax optimization | WEALTH MGMT |
| Investing Simplified (Prof G) | 🚨Next Week is the Most Important Week for the Stock Market in 2026 | HIGH_VOL CATALYST — week of Apr 28 flagged as critical (FOMC + mega-cap earnings) | HIGH ⚠️ CATALYST |
| Investing Simplified (Prof G) | Big Money is BUYING HEAVY Here (Actual Portfolios of the 1% in 2026) | MID_VOL transition signal — institutional accumulation on dip | HIGH |
| IG France (Baradez ★★★) | Marc Dagher ouvre son ProRealTime (Apr 30) | TA market brief — near-term technical outlook | MEDIUM |
| IG France (Baradez ★★★) | MarketLive: dernières tendances graphiques (Apr 24) | HIGH_VOL — back-to-back live sessions during stressed week | HIGH |
| IG France (Baradez ★★★) | MarketLive: dernières tendances graphiques (Apr 23) | HIGH_VOL — live market stress analysis at volatility peak | HIGH |
