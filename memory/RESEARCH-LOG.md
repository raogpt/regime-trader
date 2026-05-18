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

## 2026-05-18 — YouTube Intel

> Note: Transcripts blocked (cloud IP — YouTube rate-limits cloud providers). Analysis from titles + channel context only. Confidence reduced accordingly.

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Bravos Research | Your Last Chance at Generational Wealth. | HIGH_VOL / Risk-OFF — "last chance" framing implies market-top concern | ★★★ HIGH |
| Bravos Research | This Time Is NOT Different. | HIGH_VOL — historical crisis-cycle repeat thesis (Reinhart/Rogoff ref) | ★★★ HIGH |
| Bravos Research | The Next 6 Months Will Make History. | HIGH_VOL — major non-linear macro event expected near-term | ★★★ HIGH |
| Investing Simplified (Prof G) | BREAKING: Expect the Great Market Flip (VERY SOON) | Regime transition imminent — directionally ambiguous (could be bullish reversal) | ★★ MED |
| Investing Simplified (Prof G) | Add this ONE Sector to 3 Fund Portfolio | Risk-ON sector rotation — growth tilt | ★ LOW |
| Investing Simplified (Prof G) | MAJOR BUY: Best Quantum Computing ETF | Speculative risk-ON; outside SPY/QQQ/IWM universe | ★ LOW |
| IG France (Baradez) | MarketLive x4 (technical analysis) | Daily TA monitoring — no directional signal from titles alone | ★★ MED |
| Oseille TV | S'expatrier en Andorre en 2026 | No regime signal — wealth mgmt / expat tax strategy (PRIORITY) | WEALTH |
| Finary | Devenir riche en étant professeur | No regime signal — DCA / patrimoine building | WEALTH |
| Finary | Real Madrid finance model | No regime signal — sports business case | LOW |
| Finary | Le cours d'économie | Macro education — no direct HMM signal | LOW |
| Finary | Pokémon: la valeur est en carton? | Alt-asset speculation = risk-ON appetite signal | ★ LOW |
| Real Vision Presents | Can Sui Become the Internet's Money Layer? | Crypto pivot — no SPY/QQQ/IWM signal | LOW |
| George Gammon | (no new videos this week) | — | — |

**Cross-channel consensus (≥2 channels):** Bravos Research 3/3 titles signal elevated uncertainty and potential HIGH_VOL regime. No ★★★ channel explicitly contradicts. Net YouTube signal: **MID→HIGH_VOL caution bias**. Confidence LOW (title-only, no transcripts).
