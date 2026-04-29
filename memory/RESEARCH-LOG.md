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

## 2026-04-29 — YouTube Intel

> 12 new videos across 5 channels (Apr 22–28). Transcripts IP-blocked (cloud env); analysis from titles + channel context.

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Oseille TV | Ces 12 pays ne prélèvent AUCUN impôt (pour l'instant) | NEUTRAL | ★★★ Wealth mgmt — zero-tax jurisdictions, UEMOA/expat |
| Bravos Research | The Damage is done… | HIGH_VOL 🔴 | ★★★ Macro — post-correction bearish assessment |
| Bravos Research | The UNTHINKABLE is About to Happen to Stocks (Emergency Update) | HIGH_VOL 🔴 | ★★★ Macro — extreme tail-risk alert |
| Finary | À 30 ans, ce salarié en marketing digital a fait le bon départ ! | NEUTRAL | ★★ Wealth mgmt — portfolio at 30, ETF DCA |
| Finary | Qui est le Président français le plus riche ? | NONE | ★ Background |
| Finary | Pourquoi vous êtes moins riches que vos parents | NEUTRAL | ★★ Macro — generational wealth gap |
| Investing Simplified (Prof G) | The Best Tax Strategy for Investors: How to Use a Donor Advised Fund | NONE | ★★ Wealth mgmt — DAF tax strategy |
| Investing Simplified (Prof G) | 🚨Next Week is the Most Important Week for the Stock Market in 2026 | HIGH_VOL 🔴 | ★★★ Catalyst cluster Apr 28–May 2 (GDP, FOMC, earnings) |
| Investing Simplified (Prof G) | Big Money is BUYING HEAVY Here (Actual Portfolios of the 1% in 2026) | MID_VOL 🟡 contrarian | ★★ Institutional accumulation signal |
| IG France (Baradez) | MarketLive : Analysons les dernières tendances graphiques (Apr 24) | UNKNOWN | ★★ Technical analysis, S&P levels |
| IG France (Baradez) | MarketLive : Analysons les dernières tendances graphiques (Apr 23) | UNKNOWN | ★★ Technical analysis |
| IG France (Baradez) | Comment utiliser TradingView sur IG ? | NONE | ★ Educational/tutorial |

**Cross-channel consensus: HIGH_VOL** — 3/3 EN macro channels bearish/defensive for Apr 28–May 2 window.
**HMM implication:** Avoid new entries until GDP (Apr 30) + FOMC (May 1) + jobs (May 2) catalysts clear. Require 3 consecutive MID/LOW_VOL bars before re-entry.
**Wealth mgmt priority:** Oseille TV zero-tax jurisdictions (UEMOA-relevant), Prof G DAF strategy.
→ Full report: reports/2026-04-29-youtube-intel.md
