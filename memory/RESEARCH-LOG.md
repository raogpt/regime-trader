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

## 2026-05-17 — YouTube Intel

> Note: Transcripts IP-blocked from cloud environment. Analysis based on title + channel context.

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Oseille TV | S'expatrier en Andorre en 2026 | NEUTRAL | WealthMgmt/Tax — Andorra expat tax optimization |
| Bravos Research | Your Last Chance at Generational Wealth. | RISK-ON | Bullish cycle framing; buy-the-dip narrative |
| Bravos Research | This Time Is NOT Different. | RISK-ON | Historical pattern dismissal; stay-invested bias |
| Bravos Research | The Next 6 Months Will Make History. | HIGH-VOL WARNING | Forward-looking high-conviction call; implies major move |
| Finary | Comment devenir riche en étant professeur | NEUTRAL | WealthMgmt — patrimoine building, French middle class |
| Finary | Comment le Real Madrid gagne-t-il autant? | NEUTRAL | Sports biz; low regime relevance |
| Finary | Oubliez ce qu'on vous a appris sur l'économie | MID-VOL | Heterodox macro challenge; potential regime shift framing |
| Finary | Pokémon : la valeur est en carton ? | NEUTRAL | Alt assets; low regime relevance |
| Investing Simplified (Prof G) | BREAKING: Expect the Great Market Flip (VERY SOON) | HIGH-VOL / ROTATION | KEY SIGNAL — imminent regime change / sector rotation call |
| Investing Simplified (Prof G) | Add this ONE Sector to 3 Fund Portfolio | RISK-ON / ROTATION | Growth-sector rotation, QQQ-adjacent bullish |
| Investing Simplified (Prof G) | MAJOR BUY: Best Quantum Computing ETF | RISK-ON | Tech/growth bull; QQQ sentiment positive |
| IG France (Baradez) | MarketLive 2026-05-13 | MID-VOL | Professional TA — market trend analysis (3 sessions) |
| IG France (Baradez) | MarketLive 2026-05-12 | MID-VOL | Professional TA — market trend analysis |
| IG France (Baradez) | MarketLive 2026-05-11 | MID-VOL | Professional TA — consecutive sessions = stable view |
| Real Vision Presents | Can Sui Become Internet's Money Layer? | RISK-ON (crypto) | Crypto optimism → risk appetite leading indicator |

**Cross-channel consensus:** 3/6 channels (Bravos, Prof G, Real Vision) signal RISK-ON. Prof G "Great Market Flip" is dominant regime signal — watch for MID→HIGH vol or sector rotation from growth to value. Bravos Research cluster (3 videos) reinforces bullish-with-caveat framing.
**Wealth Mgmt priority:** Oseille TV (Andorra tax optimization), Finary (patrimoine analysis for salaried investors).
