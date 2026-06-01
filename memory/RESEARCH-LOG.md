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

## 2026-06-01 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Bravos Research | The UNTHINKABLE is About to Happen to Stocks (Emergency Update) | HIGH_VOL / risk-off alert | ★★★ |
| Investing Simplified | 🚨CAUTION: Quiet Tax the New Fed is About to Charge Every Investor | Fed uncertainty → MID→HIGH_VOL | ★★★ |
| Real Vision | It Said 2-Months… It Did It In Minutes! | Sudden vol spike signal | ★★ |
| IG France (Baradez) | MarketLive × 2 (2026-05-27, 2026-05-28) | Technical context, no directional bias | ★★ |
| Finary | Le Japon perd 1 habitant toutes les 35 secondes | Japan macro risk / global contagion → IWM risk | ★★ |
| Oseille TV | Votre argent en banque n'est plus à vous ! | Banking bail-in risk / expat wealth — PRIORITY | PRIORITY |
| Finary | La première note parfaite de l'histoire | Product review (savings/ETF) | ★ |
| Finary | Le piège du paiement en 3 fois | Consumer debt fragility signal | ★ |
| Investing Simplified | 5 Best Stocks & Hottest Sectors for 2026 | Sector rotation (QQQ tilt implied) | ★ |
| Investing Simplified | Retirement: How to Live Off Your Investments FOREVER | Wealth mgmt / passive income | PRIORITY |
| Real Vision | Sui Miami DeFi conference (×5) | Crypto / low ETF relevance | — |
