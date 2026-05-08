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

## 2026-05-08 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Bravos Research | Brace Yourself. (2026-05-07) | HIGH VOL / Risk-off warning | ★★★ |
| Bravos Research | History is About to Be Made. (2026-05-01) | Major macro inflection incoming | ★★★ |
| Finary | Les États-Unis... en faillite technique ? (2026-05-05) | US fiscal stress, dollar risk | ★★★ |
| Finary | Un système au bord du gouffre ? (2026-05-07) | Systemic risk signal, vol spike risk | ★★★ |
| Investing Simplified (Prof G) | EXTREME Market Update: S&P 500 All Time High! (2026-05-02) | Bull confirmed, ATH caution | ★★ |
| Investing Simplified (Prof G) | $300k dividends FOREVER (2026-05-05) | Dividend/income positioning | ★ |
| IG France (Alexandre Baradez) | MarketLive 2026-05-07 | Daily TA — market trends | ★★★ |
| IG France (Alexandre Baradez) | MarketLive 2026-05-06 | Daily TA — market trends | ★★★ |
| IG France (Alexandre Baradez) | MarketLive 2026-05-04 | Daily TA — market trends | ★★ |
| IG France (Alexandre Baradez) | CFD guide 2026 (2026-05-07) | Educational — no signal | — |
| Real Vision Presents | Top Picks in the Gold Miners (2026-05-04) | Defensive rotation, risk-off | ★★ |
| Real Vision Presents | Sui Live Miami 2026 (2026-05-08) | Crypto risk-on, low signal | — |
| Finary | Il est temps de réinventer l'assurance-vie (2026-05-06) | Wealth mgmt — insurance reform | ★ (wealth) |
| Finary | Je quitte la chaîne Finary...? (2026-05-06) | Channel update — no signal | — |
| Finary | Signes que vos objectifs financiers sont irréalistes (2026-05-03) | Behavioral finance | — |
| Oseille TV | Passeport GRATUIT pour vos enfants (2026-05-06) | Expat/citizenship strategy — UEMOA | ★★ (wealth) |

**Cross-channel consensus:** Bravos Research + Finary (2 channels) signal elevated vol/fiscal risk → HMM should monitor for LOW_VOL→MID_VOL transition. Contradicted by Prof G ATH confirmation (bull regime). Net: CAUTIOUS BULL with rising tail risk.
**Note:** Transcripts unavailable — YouTube IP-blocks cloud transcript API. Title-based analysis only.
