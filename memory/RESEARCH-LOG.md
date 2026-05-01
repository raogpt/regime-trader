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

## 2026-05-01 — YouTube Intel

> Note: Transcripts unavailable (YouTube blocks cloud IPs). Analysis based on titles + channel context.

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Bravos Research | The Damage is done… (2026-04-27) | HIGH_VOL confirmed / post-shock framing | HIGH — macro signal, risk-off |
| Investing Simplified (Prof G) | 🚨Next Week is the Most Important Week for the Stock Market in 2026 (2026-04-25) | CATALYST ALERT — we are in that week | HIGH — circuit breaker awareness |
| IG France (Alexandre Baradez) | MarketLive: Analysons les dernières tendances graphiques (2026-04-24) | Technical trend monitoring, EU macro | MEDIUM — ★★★ channel, no data |
| IG France (Alexandre Baradez) | Le cockpit d'un expert — Marc Dagher ouvre son ProRealTime (2026-04-30) | Educational/tools focus | LOW — no regime signal |
| Finary | Les gérants de fonds peuvent-ils encore faire la différence ? (2026-04-30) | Active vs passive debate | LOW regime / MEDIUM wealth-mgmt |
| Finary | Le secret le mieux gardé de la finance (2026-04-29) | Likely fee/index/alpha focus | LOW regime / MEDIUM wealth-mgmt |
| Finary | À 30 ans, ce salarié en marketing digital a fait le bon départ ! (2026-04-26) | Personal finance case study | LOW |
| Investing Simplified (Prof G) | You Do NOT Need $1.46 Million to Retire (2026-04-30) | Retirement sufficiency | LOW regime / HIGH wealth-mgmt |
| Investing Simplified (Prof G) | The Best Tax Strategy: Donor Advised Fund (2026-04-27) | Tax optimization | LOW regime / HIGH wealth-mgmt |
| Oseille TV | Ces 12 pays ne prélèvent AUCUN impôt (pour l'instant) (2026-04-28) | Tax-free jurisdictions for expats | LOW regime / VERY HIGH wealth-mgmt (UEMOA priority) |

**Cross-channel consensus (2+ channels):** Bravos + Prof G both flag HIGH_VOL / major catalyst week → HMM catalyst filter ACTIVE. Recommendation: HOLD sizing until regime stabilizes post-catalyst.

**George Gammon, Real Vision:** No new videos this week.
