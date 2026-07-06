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

## 2026-07-06 — YouTube Intel
Transcript fetch blocked for all 16 new videos (YouTube cloud-IP block on
`youtube_transcript_api`) — analysis below is title-only, LOW confidence.

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Bravos Research | The Bubble is Bursting... (Emergency Update) | risk-off / high-vol warning (title only) | LOW |
| George Gammon | Are We On The Brink Of Another Financial Crisis? | risk-off / high-vol warning (title only) | LOW |
| George Gammon | Powerful Stock Indicator Just Gave An Extreme Crash Warning | risk-off / high-vol warning (title only) | LOW |
| Investing Simplified (Prof G) | The ETF that CRUSHED the S&P500 | possible ETF-rotation angle | LOW |
| Oseille TV | CBDC : bientôt l'État contrôlera chaque euro | monetary-policy adjacent | LOW |

Full report: reports/2026-07-06-youtube-intel.md
