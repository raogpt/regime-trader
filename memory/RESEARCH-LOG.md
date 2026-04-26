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

## 2026-04-26 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Oseille TV | IRAN, USA, CBDC, IA, Agenda 2030 : Ce qu'on ne vous dit pas… | HIGH_VOL / risk-off (geopolitical escalation framing) | MEDIUM — macro tail-risk; UEMOA/expat wealth context |
| Bravos Research | The UNTHINKABLE is About to Happen to Stocks (Emergency Update) | HIGH_VOL / bearish warning | HIGH — market-signal channel, urgent tone mid-week |
| Bravos Research | Yep… It's Happening AGAIN. | HIGH_VOL / bearish continuation pattern | HIGH — second consecutive bearish title this week |
| Finary | Qui est le Président français le plus riche ? | NEUTRAL | LOW — lifestyle/entertainment |
| Finary | Pourquoi les jeunes générations sont-elles plus pauvres ? | NEUTRAL / macro-structural | LOW-MEDIUM — generational wealth context |
| Finary | Découvrez la voiture de... Bernard Arnault | NEUTRAL | VERY LOW — lifestyle |
| Finary | À quoi ressemblent 30 ans de bonnes décisions (59 ans, 3000 €/mois) | NEUTRAL / long-term bullish | LOW — wealth-mgmt anecdote |
| Investing Simplified (Prof G) | 🚨 Next Week is the Most Important Week for the Stock Market in 2026 | HIGH_VOL / CATALYST ALERT wk Apr 28–May 2 | VERY HIGH — timely, triggers earnings/catalyst filter |
| Investing Simplified (Prof G) | Big Money is BUYING HEAVY Here (Actual Portfolios of the 1% in 2026) | RISK-ON / institutional accumulation signal | HIGH — smart-money dip-buying → potential LOW_VOL setup |
| Investing Simplified (Prof G) | 🚨 BIG Portfolio Changes: My Biggest Buys & Sells Early 2026 | MIXED / regime-transition | MEDIUM — portfolio rebalancing in elevated vol |

**Cross-channel consensus:** Bravos (2 bearish) + Prof G "most important week" = elevated volatility expected wk of Apr 28. Prof G simultaneously signals institutional buying → directional uncertainty, HIGH vol probable. Earnings/catalyst filter: **ACTIVATE — hold new entries until post-catalysts.**
**Transcript note:** All transcripts blocked (cloud IP ban by YouTube). Analysis derived from titles + channel context + publication timing.
