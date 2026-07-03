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

## 2026-07-03 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|----------------|-----------|
| Bravos Research | The Bubble is Bursting... (Emergency Update) | S&P -3% off ATH but mega-cap tech -12-18%; $2.5T wiped since June; hyperscaler AI capex ~100% of cash flow (dotcom-level); PE compressing while earnings mask it; base case = buying opportunity, risk flagged | HIGH |
| George Gammon | Powerful Stock Indicator Just Gave An Extreme Crash Warning | Dow/NASDAQ 7-10 day divergence (5.5%) — historically (since 1971) 67-70% odds of -20% bear market within 3mo; cites BIS warning on AI bubble + circular AI financing; NASDAQ (QQQ) most exposed vs Dow/broader market | HIGH |
| IG France (A. Baradez) | MarketLive 2 juillet | VIX 16-17, retesting support zone (10-15 floor) ahead of US jobs report; Fed's Kevin Warsh reiterates hawkish 2% inflation target, no near-term cuts (core CPI >3%); EU rates ticking back up | MID |
| Investing Simplified (Prof G) | 3 videos (Bible truths / VGT ETF / portfolio update) | Generic long-term ETF/DCA advocacy (QQQ, VGT); no regime-timing signal | LOW |
| Finary | 2 videos (money mindset / patrimoine review) | Personal finance mindset content, no market signal | LOW |
| Oseille TV | 8 videos (tax/expat/CBDC/AI) | Expat tax optimization (Turkey, Panama), CBDC/surveillance commentary; no UEMOA/Africa content this cycle | LOW |

**Cross-channel consensus (2+ channels):** Bravos Research + George Gammon independently flag AI-capex/circular-financing unwind as the top catalyst for a volatility regime shift, with NASDAQ/QQQ most exposed vs. Dow/broader-market breadth (SPY/IWM proxy). Watch for HMM regime transition toward HIGH_VOL if this correction broadens beyond mega-cap tech.

Full report: reports/2026-07-03-youtube-intel.md
