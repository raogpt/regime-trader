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

## 2026-06-05 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Bravos Research | History is About to Be Made. | HIGH_VOL watch — imminent major catalyst implied | ★★★ macro |
| Bravos Research | The UNTHINKABLE is About to Happen to Stocks (Emergency Update) | HIGH_VOL / RISK-OFF — emergency framing, bearish lean | ★★★ macro |
| Investing Simplified (Prof G) | The AI & Quantum Boom Is Just Starting | LOW-MID_VOL / RISK-ON — bullish tech (QQQ) narrative | ★★ ETF |
| Investing Simplified (Prof G) | CAUTION: Quiet Tax the New Fed is About to Charge Every Investor | MID-HIGH_VOL — Fed/monetary headwind, inflation risk | ★★★ macro |
| IG France (Baradez) | MarketLive × 4 sessions (May–Jun) | MID-HIGH_VOL — 4 daily analyses in one week = active/volatile tape | ★★★ technical |
| IG France (Baradez) | Comment creer un robot de trading avec l'IA | No regime signal — AI tools meta-content | ★ info |
| Real Vision | A New Frontier in Gold Exploration | HIGH_VOL / RISK-OFF — gold bullish, flight-to-safety narrative | ★★★ macro |
| Real Vision | Stablecoins, ETFs, and the New Crypto Market Structure | MID_VOL — institutional crypto flows, capital diversification | ★★ macro |
| Real Vision | Why Financial Privacy Is a Human Right! | No direct regime signal — Bitcoin/privacy narrative | ★ info |
| Real Vision | Why This Founder Left Ethereum for Sui / How Current Makes DeFi Yield Simple | No regime signal — crypto ecosystem | ★ info |
| Finary | La première note parfaite de l'histoire de la chaîne | Wealth mgmt portfolio review — no regime signal | ★★ wealth |
| Finary | Ce que révèle cette émission TV sur la finance... | General finance education — no regime signal | ★ info |
| Finary | A quoi ressemble la vie dans la famille la plus riche d'Asie ? | Lifestyle/wealth content — no regime signal | ★ wealth |
| Oseille TV | Amazon FBA en 2026 : C'est fini ? | Business/e-commerce — no regime signal | ★ wealth |

**Cross-channel consensus (2026-06-05):** RISK-OFF / MID→HIGH_VOL — 3 of 4 macro-rated channels (Bravos ×2, Prof G, Real Vision gold) signal caution or elevated vol. One bullish counter (Prof G AI). Active Baradez tape confirms intraday volatility elevated. HMM gate: verify ≥55% confidence before acting; prefer SPY/QQQ over IWM in risk-off.

**Transcript status:** All 20 transcripts UNAVAILABLE (cloud IP blocked by YouTube). Analysis based on title + channel metadata only.
