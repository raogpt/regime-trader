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

## 2026-05-16 — YouTube Intel

> Transcripts: BLOCKED (cloud IP). Analysis title-based; confidence LOW across all signals.

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Oseille TV | S'expatrier en Andorre en 2026 | N/A — expat tax planning | ★ PRIORITY wealth-mgmt |
| Bravos Research | Your Last Chance at Generational Wealth. | Inflection point / buying window → LOW-MID vol transition | HIGH |
| Bravos Research | This Time Is NOT Different. | Historical analog warning → MID→HIGH vol risk | HIGH |
| Bravos Research | The Next 6 Months Will Make History. | Major macro events ahead → HIGH vol anticipation 6m | HIGH |
| Finary | Oubliez ce qu'on vous a appris sur l'économie | Contrarian macro view, paradigm shift risk | MEDIUM |
| Finary | Retraite à 45 ans — Analyse de patrimoine | FIRE/wealth-mgmt | ★ PRIORITY wealth-mgmt |
| Finary | Comment le Real Madrid gagne-t-il autant? | Sports finance | LOW |
| Finary | Pokémon : la valeur est en carton? | Alt-assets collectibles | LOW |
| Investing Simplified (Prof G) | Add this ONE Sector to 3 Fund Portfolio | RISK-ON, sector rotation, LOW-MID vol | MEDIUM |
| Investing Simplified (Prof G) | MAJOR BUY: Best Quantum Computing ETF | RISK-ON, tech/QQQ-adjacent bullish | MEDIUM |
| Investing Simplified (Prof G) | 7 Money Rules 95% of Americans Break | Behavioral finance | LOW |
| IG France (Baradez) | MarketLive TA x3 (May 11-13) | Active market monitoring, MID vol | HIGH |
| Real Vision Presents | Can Sui Become the Internet's Money Layer? | Crypto — regime irrelevant | LOW |
| George Gammon | (no new videos) | ★★★ channel silent — no macro alert | NOTE |

**Cross-channel vol consensus**: NONE (Bravos cautious/HIGH vol ←→ Prof G risk-on/LOW vol)
**HMM bot action**: No external override. Let HMM-detected regime dominate. Monitor Bravos 6m thesis.
**George Gammon silence**: Notable — ★★★ channel issued no new macro alert this week.
