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

## 2026-07-04 — YouTube Intel

18 new videos across 6 channels (first check, 7-day lookback). Full report: reports/2026-07-04-youtube-intel.md

| Channel | Video | Regime Signal | Relevance |
|---------|-------|----------------|-----------|
| Bravos Research | The Bubble is Bursting... (Emergency Update) | AI-led mega-cap tech correction (-3% index, PE compressing 15%), but broad breadth healthy; frames as buying opportunity | High |
| George Gammon | Are We On The Brink Of Another Financial Crisis? | CPI/oil/rates trajectory mirrors early-2008 GFC lead-up; weak NFP (57k vs 115k exp, -74k revisions) risks passive equity outflows | High |
| George Gammon | Powerful Stock Indicator Just Gave An Extreme Crash Warning | Dow/NASDAQ 5.5% divergence (rare since 1971) → 67% historical odds of bear market within 3mo; ties to AI-bubble/circular-financing unwind, cites BIS warning | High |
| IG France (Baradez) | MarketLive 2026-07-02 | VIX 16-17 at multi-year support, catalyst-dependent break either way; US/EU 10yr yields ticking up, Fed (Hassett) reaffirming 2% target, no near-term cuts | Medium |
| IG France (Baradez) | Ce qui fait la différence en trading | Trading-plan/psychology webinar, no regime signal | Low |
| Investing Simplified | The ETF that CRUSHED the S&P500 (VGT) | Promotes tech-concentrated ETF (Mag7+semis) — in tension with AI-bubble warnings above | Low-Medium |
| Investing Simplified | My ENTIRE Investing Portfolio (2026 Big Changes) | Personal allocation walkthrough, no SPY/QQQ/IWM signal | Low |
| Investing Simplified | 14 Money Truths from the Bible | General investing philosophy, no market signal | Low |
| Oseille TV | 8 videos (tax/expat/CBDC/AI/broker topics) | No SPY/QQQ/IWM regime signal; Turkey 0% foreign-income tax package noted for wealth-mgmt | Low |
| Finary | 2 videos (financial psychology, case study) | No regime signal | Low |
| Real Vision Presents | — | No new videos | — |

**Cross-channel consensus:** 3 channels (Bravos Research, George Gammon x2, IG France) independently flag elevated volatility/correction risk this week, all rooted in AI capex/circular-financing unwind — agreement on *risk elevated*, disagreement on *direction* (dip-buy vs. bear-market-started). Worth monitoring against HMM regime confidence over the next 1-3 months, especially given QQQ's AI/tech concentration.
