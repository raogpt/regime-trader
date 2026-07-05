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

## 2026-07-05 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---|---|---|---|
| George Gammon | Powerful Stock Indicator Just Gave An Extreme Crash Warning | Dow/NASDAQ 5.5% divergence (7-10d) → historically 67% odds of -20% bear market within 3mo; BIS flags AI circular-financing bubble risk | High — HIGH_VOL warning, QQQ-concentrated |
| George Gammon | Are We On The Brink Of Another Financial Crisis? | NFP badly missed (57k vs 115k exp), prior 2 months revised down 74k combined; CPI/oil/rate path echoes early-2008 GFC setup | High — risk-off, labor deterioration |
| Bravos Research | The Bubble is Bursting... (Emergency Update) | Mega-cap AI capex ~100% of cash flow (dotcom-era levels); S&P PE compressed 15% while price flat; ex-tech breadth (Dow, banks, energy) still strong | High — tech/QQQ vol risk, but broad market fundamentals intact |
| IG France (Baradez) | MarketLive 7/2 | VIX ~16-17, sitting at technical support (10-15 floor), not yet breaking down; US10Y ~4.5%; Fed's Warsh reiterates hawkish 2% mandate; NFP release same-day catalyst | Medium — current realized vol still contained despite forward-looking warnings |
| IG France (Baradez) | Ce qui fait la différence en trading | Trading-plan discipline / pre-defined risk before entry (process, not a market signal) | Low |
| Investing Simplified (Prof G) | The ETF that CRUSHED the S&P500 | Promotes VGT off a 10yr 25%/yr extrapolation — recency-bias / concentration risk | Low — contrarian flag vs. Gammon's tech-crash call |
| Investing Simplified (Prof G) | 14 Money Truths from the Bible | Diversification, DCA, emergency fund, avoid debt — general principles | Low (wealth mgmt) |
| Investing Simplified (Prof G) | The Real Reason Your Portfolio Isn't Growing Faster | No transcript available | — |
| Finary | Facteur, 37 ans, 177 000 € | Case study: 60% net worth in one stock, ~€60 liquid, no emergency fund | Low (wealth mgmt, cautionary) |
| Finary | L'erreur que tout le monde fait avec l'argent | Financial-goal psychology; emergency fund framed as goal #1 | Low (wealth mgmt) |
| Oseille TV | 7 videos (tax/CBDC/expat/AI/broker) | No regime signal; expat/tax/broker themes (Panama safety, IBKR recs, CBDC/tax concerns) | Low — no UEMOA/Africa content this cycle |

**Consensus (2+ channels):** George Gammon + Bravos Research both flag AI-capex/circular-financing as the proximate volatility trigger, both note the risk is concentrated in mega-cap tech (NASDAQ/QQQ) while broader-market breadth (Dow-type, ex-tech sectors) holds up. IG's realized-vol read (VIX 16-17, at support) has **not yet confirmed** a regime shift — forward-looking narrative risk is elevated but the HMM's volatility state hasn't flipped. Treat as an early-warning watch item, not an actionable signal (confidence/stability gates not met).

Full report: reports/2026-07-05-youtube-intel.md
