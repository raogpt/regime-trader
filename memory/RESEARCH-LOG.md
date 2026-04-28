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

## 2026-04-28 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Bravos Research | The Damage is done… (2026-04-27) | HIGH_VOL — bearish post-damage; drawdown confirmed | HIGH |
| Bravos Research | The UNTHINKABLE is About to Happen to Stocks — Emergency Update (2026-04-23) | HIGH_VOL — extreme bearish, emergency tone | HIGH |
| Investing Simplified (Prof G) | Next Week is the Most Important Week for the Stock Market in 2026 (2026-04-25) | HIGH catalyst risk — FOMC/earnings vol event imminent | HIGH |
| Investing Simplified (Prof G) | Big Money is BUYING HEAVY Here (2026-04-23) | Contrarian dip-buy signal — institutional accumulation | MEDIUM |
| Investing Simplified (Prof G) | How I Saved $30,000 in Taxes — DAF Strategy (2026-04-27) | Neutral — tax/wealth mgmt | LOW |
| IG France (Alexandre Baradez) | MarketLive ×3 (2026-04-21/23/24) | Technical analysis cadence — elevated market watch | MEDIUM |
| IG France (Alexandre Baradez) | Comment utiliser TradingView sur IG (2026-04-23) | Educational — no signal | LOW |
| Oseille TV | IRAN, USA, CBDC, IA, Agenda 2030 (2026-04-21) | Risk-off — geopolitical + CBDC uncertainty | MEDIUM |
| Finary | ×4 personal finance videos (2026-04-21–26) | Wealth mgmt — generational wealth/inflation narrative | MEDIUM (wealth) |
| Real Vision | A Peek Into Binance with Catherine Chen (2026-04-21) | Crypto rotation — risk appetite gauge | LOW |
| George Gammon ★★★ | (no new videos this week) | Notable silence from top-rated macro source | MEDIUM |

**Cross-channel consensus:** 2/2 EN macro channels (Bravos Research) signal HIGH_VOL with emergency language. Prof G confirms major catalyst week ahead. George Gammon (★★★) silence may indicate uncertainty rather than conviction. **Regime implication → HIGH_VOL. Reduce allocation 60%, widen stops, gate new entries.**
