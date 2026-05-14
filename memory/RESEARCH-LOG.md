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

## 2026-05-14 — YouTube Intel

**16 new videos | 6/7 channels active | George Gammon: no update | Transcripts: BLOCKED (cloud IP)**

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Bravos Research | This Time Is NOT Different. (2026-05-13) | HIGH VOL / Risk-OFF | ★★★ |
| Bravos Research | The Next 6 Months Will Make History. (2026-05-11) | MID→HIGH VOL / elevated uncertainty | ★★★ |
| Bravos Research | Brace Yourself. (2026-05-07) | HIGH VOL / defensive | ★★★ |
| Finary | Un système au bord du gouffre ? (2026-05-07) | HIGH VOL / systemic risk | ★★ |
| IG France (Baradez) | MarketLive x4 (2026-05-07/11/12/13) | TA signals — transcripts needed | ★★★ |
| Real Vision Presents | Sui Live Miami 2026 / Raoul Pal (2026-05-08) | Risk-ON crypto / NEUTRAL equities | ★ |
| Investing Simplified | Quantum Computing ETF MAJOR BUY (2026-05-11) | Risk-ON / MID VOL (growth) | ★ |
| Investing Simplified | 7 Money Rules Americans Break (2026-05-09) | NEUTRAL (wealth mgmt) | — |
| Finary | Retraite à 45 ans analyse patrimoine (2026-05-10) | NEUTRAL — early retirement sizing | PRIORITY |
| Finary | TOUT comprendre à l'économie (2026-05-13) | NEUTRAL — educational | — |
| Finary | Pokémon valeur en carton ? (2026-05-12) | Alt-asset bubble indicator | — |
| Oseille TV | S'expatrier en Andorre 2026 (2026-05-12) | NEUTRAL — expat/tax | PRIORITY |

**Cross-channel consensus:** Bravos Research (3 videos) + Finary = 2 channels → RISK-OFF / MID→HIGH VOL lean.
**Countersignal:** Prof G + Real Vision = Risk-ON, lower conviction.
**Net:** Bearish lean. Watch HMM for MID→HIGH vol confirmation (≥55% conf, 3 bars). ETF pref: SPY > IWM >> QQQ.
**Wealth Mgmt:** Andorra expat guide (tax optim) + Finary early retirement case study — see full report.
**Full report:** reports/2026-05-14-youtube-intel.md
