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

## 2026-05-10 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Bravos Research | Brace Yourself. | HIGH_VOL — explicit bearish macro warning | HIGH |
| Finary | Un système au bord du gouffre ? | HIGH_VOL — systemic risk framing | HIGH |
| Finary | Les États-Unis... en faillite technique ? | HIGH_VOL — US technical default catalyst | HIGH |
| Real Vision | Top Picks in the Gold Miners | RISK-OFF — institutional rotation to gold | HIGH |
| IG France (Baradez) | MarketLive ×3 (May 4/6/7) | TA-based — European session, likely volatile | HIGH (★★★) |
| Real Vision | Sui Live Miami 2026 (Raoul Pal) | RISK-ON crypto — Africa/UEMOA angle | MEDIUM |
| Finary | Retraite à 45 ans — analyse de patrimoine | Wealth mgmt — FIRE planning | PRIORITY |
| Finary | Il est temps de réinventer l'assurance-vie | Wealth mgmt — allocation vehicles | PRIORITY |
| Oseille TV | Passeport GRATUIT pour vos enfants | Expat/citizenship planning | PRIORITY |
| Prof G | $300K to live off dividends FOREVER | Wealth mgmt — dividend FIRE | MEDIUM |
| Prof G | 7 Money Rules 95% of Americans Break | Retirement education | LOW |
| Finary | Je quitte la chaîne Finary... ? | Channel news — no signal | LOW |
| IG France | CFD guide complet 2026 | Promotional — no regime signal | LOW |

- **Cross-channel consensus**: 3+ channels (Bravos, Finary ×2, Real Vision gold) → HIGH_VOL / RISK-OFF
- **Transcripts**: unavailable (cloud IP block by YouTube)
- **Full report**: reports/2026-05-10-youtube-intel.md
