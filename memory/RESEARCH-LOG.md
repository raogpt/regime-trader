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

## 2026-07-02 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Bravos Research | The Bubble is Bursting... (Emergency Update) | S&P -3% off ATH, mega-cap tech down 12-18% from highs; AI capex ~100% of hyperscaler cash flow (dotcom-era levels); PE compression offset by earnings; non-AI 80% of market still strong | HIGH — QQQ concentration risk |
| George Gammon | Powerful Stock Indicator Just Gave An Extreme Crash Warning | NASDAQ/Dow 5.5% divergence (Jun 15-25) — historically 67-70% odds of 20%+ bear market within 3mo; BIS warns AI bubble/circular financing unwind could rival 2008 GFC | HIGH — vol regime early warning |
| IG France (Baradez) | MarketLive Jun 25 | VIX holding above trendline support (~20), NASDAQ rebounding post-Micron earnings; undecided whether new highs (VIX→12-16) or downtrend resumes | MID — confirms elevated-but-unresolved vol |
| IG France (Baradez) | 5 valeurs live Q&A | Retail sentiment poll: gold 54% bearish/14% bullish; no new regime data | LOW |
| Investing Simplified (Prof G) | The ETF that CRUSHED the S&P500 / My Entire Portfolio | Promotes VGT (tech-heavy ETF), 10yr CAGR 25% — same AI/mega-cap exposure flagged as high-risk above | LOW (bias risk, not regime signal) |
| Oseille TV / Finary (5 videos) | Tax/expat/budgeting content | No regime signal | Wealth-mgmt only |

**Cross-channel consensus:** Bravos Research + George Gammon (2 independent EN macro channels) both flag elevated bear-market probability tied to AI-bubble/mega-cap concentration and circular-financing unwind risk — concentrated in QQQ exposure, not broad market. IG France confirms VIX still elevated above support, direction unresolved. Early warning only — HMM has not confirmed a regime shift (need conf >=55%, 3 stable bars per hard rules). No trade action taken.

Full report: reports/2026-07-02-youtube-intel.md
