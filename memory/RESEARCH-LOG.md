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

## 2026-05-15 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Oseille TV | S'expatrier en Andorre en 2026 | None (wealth-mgmt) | ★★★ WEALTH MGMT |
| Bravos Research | This Time Is NOT Different. | HIGH_VOL warning (late-cycle) | ★★★ MACRO |
| Bravos Research | The Next 6 Months Will Make History. | HIGH_VOL / major catalyst H2 2026 | ★★★ MACRO |
| Finary | Comment le Real Madrid gagne-t-il autant d'argent ? | None | Background |
| Finary | Oubliez ce qu'on vous a appris sur l'économie | Macro framing (weak signal) | Moderate |
| Finary | Pokémon : la valeur est en carton ? | Speculative bubble / late-cycle | Low |
| Finary | Retraite à 45 ans... Analyse de patrimoine | None (wealth-mgmt) | ★★★ WEALTH MGMT |
| Investing Simplified | (For Faster Growth) Add this ONE Sector | Risk-ON / LOW_VOL perception | Moderate |
| Investing Simplified | MAJOR BUY: Best Quantum Computing ETF | Risk-ON speculative | Low |
| Investing Simplified | The 7 Money Rules 95% of Americans Break | None (personal finance) | ★★ WEALTH MGMT |
| IG France (Baradez) ★★★ | MarketLive 2026-05-13 | Active market / MID_VOL | ★★★ DIRECT |
| IG France (Baradez) ★★★ | MarketLive 2026-05-12 | Active market / MID_VOL | ★★★ DIRECT |
| IG France (Baradez) ★★★ | MarketLive 2026-05-11 | Active market / MID_VOL | ★★★ DIRECT |

**Channels with no new videos:** George Gammon, Real Vision Presents
**Transcripts:** 0/13 available (YouTube bot-blocking in cloud environment — title-only analysis)
**Cross-channel consensus:** None — macro-bearish (Bravos) vs. risk-on (Investing Simplified) divergence
**Regime gate:** BLOCKED — estimated confidence <55%, below action threshold
**Full report:** reports/2026-05-15-youtube-intel.md
