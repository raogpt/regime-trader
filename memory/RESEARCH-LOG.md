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

## 2026-06-04 — YouTube Intel

> Note: All 19 transcripts blocked (YouTube cloud IP ban). Signals derived from titles + channel context.

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Bravos Research | History is About to Be Made. (2026-06-02) | AMBIGUOUS — major milestone framing, possible breakout or top | HIGH |
| Bravos Research | The UNTHINKABLE is About to Happen to Stocks — Emergency Update (2026-05-29) | HIGH_VOL WARNING — emergency tone suggests elevated tail risk | HIGH |
| Investing Simplified | The AI & Quantum Boom Is Just Starting (2026-06-03) | RISK-ON — AI/tech momentum → QQQ tailwind, LOW/MID vol supportive | MEDIUM |
| Investing Simplified | CAUTION: Quiet Tax the New Fed is About to Charge Every Investor (2026-05-30) | RISK-OFF — Fed inflation/yield warning → macro volatility catalyst | HIGH |
| IG France (Baradez) ★★★ | MarketLive x4 episodes (2026-05-28 to 2026-06-04) | DAILY TECHNICAL — active market, 4 consecutive reviews indicate high market activity | HIGH |
| Real Vision ★★★ | The Biggest Crypto Narrative Hasn't Started Yet! (2026-06-03) | RISK-ON — crypto appetite elevated, risk appetite intact | LOW |
| Real Vision ★★★ | A New Frontier in Gold Exploration (2026-06-03) | MILD RISK-OFF HEDGE — gold coverage signals macro uncertainty | MEDIUM |
| Real Vision ★★★ | Stablecoins, ETFs, and the New Crypto Market Structure (2026-06-02) | ETF CONVERGENCE — crypto ETF inflows = risk-on environment | LOW |
| Real Vision ★★★ | It Said 2-Months... It Did It In Minutes! (2026-05-28) | HIGH_VOL TRIGGER — rapid unexpected move narrative | MEDIUM |
| Finary | Le Japon perd 1 habitant toutes les 35 secondes (2026-05-28) | MACRO — Japan demographic/debt collapse risk; global contagion angle | MEDIUM |
| Finary | Ce que révèle cette émission TV sur la finance (2026-06-02) | WEALTH MGMT — financial literacy/culture | LOW |
| Finary | La première note parfaite de l'histoire de la chaîne (2026-05-31) | WEALTH MGMT — product review (ETF/broker) | LOW |
| Finary | A quoi ressemble la vie dans la famille la plus riche d'Asie (2026-06-03) | WEALTH MGMT — aspirational/informational | LOW |
| Oseille TV | Amazon FBA en 2026 : C'est fini ? (2026-06-03) | ENTREPRENEURSHIP — not market signal | LOW |
| George Gammon ★★★ | (no new videos this week) | NO SIGNAL | — |

**Cross-channel consensus (2+ channels agreeing):**
- RISK-ON: Real Vision + Investing Simplified → AI/tech/QQQ momentum
- MACRO CAUTION: Bravos (emergency) + Investing Simplified (Fed tax) → elevated tail risk, keep stops tight
- Net HMM bias: MID_VOL or LOW/MID transition, but downside risk asymmetry elevated
