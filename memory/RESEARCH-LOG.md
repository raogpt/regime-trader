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

## 2026-06-03 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Bravos Research | History is About to Be Made. | HIGH_VOL lean — cryptic title implies imminent major market move | HIGH |
| Bravos Research | The UNTHINKABLE is About to Happen to Stocks (Emergency Update) | HIGH_VOL — emergency update on stocks, strong bearish/shock signal | HIGH |
| Finary | Ce que révèle cette émission TV sur la finance... | Neutral — media commentary on finance culture | LOW |
| Finary | La première note parfaite de l'histoire de la chaîne | Neutral — product/savings review, top score | LOW |
| Finary | Le Japon perd 1 habitant toutes les 35 secondes. Son économie va-t-elle s'effondrer ? | MID_VOL overlay — Japan demographic/macro risk, yen carry unwind exposure | MED |
| Finary | Le piège du paiement en 3 fois expliqué | Neutral — personal finance (installment credit) | LOW |
| Investing Simplified (Prof G) | CAUTION: Quiet Tax the New Fed is About to Charge Every Investor | MID→HIGH_VOL — Fed inflation/financial repression warning, rate-vol precursor | HIGH |
| IG France (Baradez) | MarketLive 2026-06-03 | MID_VOL — today's live TA session, key near-term signal (transcript blocked) | HIGH |
| IG France (Baradez) | MarketLive 2026-06-01 | MID_VOL — recent TA trend review | MED |
| IG France (Baradez) | MarketLive 2026-05-28 | MID_VOL — last week TA context | MED |
| IG France (Baradez) | Comment vraiment maîtriser le RSI en trading | Neutral — educational/RSI methodology | LOW |
| IG France (Baradez) | MarketLive 2026-05-27 | MID_VOL — last week TA context | MED |
| Real Vision Presents | How Current Makes DeFi Yield Simple (Sui Miami) | Neutral — DeFi/crypto, not ETF-relevant | LOW |
| Real Vision Presents | Stablecoins, ETFs, and the New Crypto Market Structure | LOW_VOL for crypto overlay — stablecoin/ETF convergence structural theme | LOW |
| Real Vision Presents | It Said 2-Months... It Did It In Minutes! | MID→HIGH_VOL — pace-of-change signal, rapid market structure shift implied | MED |
| Real Vision Presents | The Convergence: AI, DeFi, and the Next Financial System (Sui Miami) | Neutral — structural macro, long-horizon | LOW |
| Real Vision Presents | Sui Overflow 2026: Hackathon Announcement | Neutral — crypto dev event, no regime relevance | LOW |

**Cross-channel vol consensus**: Bravos Research + Prof G (2 EN macro channels) both signal stress/caution → MID→HIGH_VOL bias. No channel signaling LOW_VOL comfort.
**Wealth Mgmt PRIORITY**: Finary Japan macro piece (yen carry watch), IG Baradez MarketLive today (blocked transcript — monitor manually).
