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

## 2026-04-29 — YouTube Intel (REVISED — full transcripts obtained)

> 12 new videos across 5 channels (Apr 22–28). **10/12 transcripts obtained** via yt-dlp + Node.js v22 runtime (bypassed cloud IP block). 2 videos (403 error) analyzed from titles.
> **⚠️ SIGNAL REVISION:** Title-only analysis previously signaled HIGH_VOL. Full transcripts show MID_VOL / constructive near-term.

**MACRO CONTEXT:** Active war with Iran — oil +40% pre-war; S&P at ALL-TIME HIGHS; Fed restarted QE; CPI above 2% for 60 months; dollar at 4-year lows.

| Channel | Video | Regime Signal (REVISED) | Relevance |
|---------|-------|------------------------|-----------|
| Bravos Research | The Damage is done… | MID_VOL 🟡 | ★★★ Yield curve FLATTENING (not steepening); job market strengthening; +10-15% more upside forecast |
| Bravos Research | The UNTHINKABLE is About to Happen to Stocks | MID_VOL 🟡 / HIGH_VOL late-2026 | ★★★ ATH = dollar debasement; near-term constructive; food inflation risk (urea +50%) end of year |
| Investing Simplified (Prof G) | Big Money is BUYING HEAVY Here | MID_VOL 🟡 risk-ON | ★★★ 13F Q1-2026: Harvard in IBIT, Goldman Bitcoin ETF, institutions in AI infra; confirms floor |
| Investing Simplified (Prof G) | 🚨Next Week is the Most Important Week for the Stock Market in 2026 | HOLD — catalyst week | ★★★ GDP (Apr 30) + FOMC (May 1) + earnings + jobs (May 2) — wait for clarity |
| Investing Simplified (Prof G) | The Best Tax Strategy for Investors: How to Use a Donor Advised Fund | NONE | ★★★ Wealth mgmt — DAF: contribute appreciated ETF shares, deduct full value, zero CGT |
| IG France (Baradez) | MarketLive Apr 24 | MID_VOL 🟡 | ★★ IFO Germany 2nd consecutive deterioration → Aug 2023 levels; geopolitically reversible |
| IG France (Baradez) | MarketLive Apr 23 | MID_VOL 🟡 | ★★ German PMI surprise contraction; US PMI mixed; Iran ceasefire move at 2 AM |
| IG France (Baradez) | Comment utiliser TradingView sur IG ? | NONE | ★ Educational/tutorial |
| Oseille TV | Ces 12 pays ne prélèvent AUCUN impôt (pour l'instant) | NEUTRAL | ★★★ Wealth mgmt — Cayman (#1): no CGT/income/corp/inheritance, residency via $2.9M USD property |
| Finary | Pourquoi vous êtes moins riches que vos parents | NEUTRAL | ★★★ Wealth mgmt — 30 glorieuses dead; equity investing mandatory for UEMOA diaspora |
| Finary | À 30 ans, ce salarié en marketing digital a fait le bon départ ! | NEUTRAL | ★★ Wealth mgmt — portfolio at 30 (transcript 403, title analysis) |
| Finary | Qui est le Président français le plus riche ? | NONE | ★ Background — Sarkozy €10M+, VGE estate, Macron €500k |

**REVISED cross-channel consensus: MID_VOL** — Bravos Research bullish (yield curve, jobs, +10-15% S&P upside); institutional buying confirms floor; near-term constructive.
**HMM implication:** HOLD through catalyst week (Apr 28–May 2). Post-FOMC: if 3 consecutive MID/LOW_VOL bars → regime gate OPEN. Prefer QQQ over SPY over IWM.
**Late-2026 watch:** Food inflation (urea +50%), dollar debasement → HIGH_VOL risk building; retrain HMM if regime shifts materially.
**Wealth mgmt priority:** (1) Oseille TV zero-tax + Cayman residency structure; (2) Prof G DAF strategy; (3) Finary equity DCA framework.
→ Full report: reports/2026-04-29-youtube-intel.md
