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

## 2026-07-01 — YouTube Intel

First run (7-day lookback, 19 new videos / 7 channels). Full report: reports/2026-07-01-youtube-intel.md

| Channel | Video | Regime Signal | Relevance |
|---|---|---|---|
| Bravos Research | The Bubble is Bursting... (Emergency Update) | AI capex at dot-com-era intensity; S&P -3% from ATH; PE compressing but earnings melt-up offsetting; non-tech breadth strong | Medium |
| George Gammon | A $100 Trillion Currency Crisis Just Started | Dollar reset thesis: DXY 99→101+, JPY/KRW/INR weakening; Fed pricing shifted toward hikes post Iran-conflict oil spike | Medium |
| IG France | MarketLive Jun 25 | VIX holding above support ~20s, retreated <20 post-Micron beat; open Q on NASDAQ trend resumption | Medium |
| IG France | MarketLive Jun 24 | VIX ~19.2 after spiking >20; KOSPI -9% correction after +300%/15mo rally; PCE + Fed Warsh flagged as this week's catalysts | Medium |
| IG France | Inflation américaine, vers une réaction de la Fed ? | PCE due Thu (4.1% headline/3.4% core, 3yr high); Fed chair Warsh hawkish surprise; market prices 89% odds of a hike | High |
| IG France | 5 valeurs, vos avis en live | Live poll 54% bearish on gold; framed as correction not reversal | Low |
| Investing Simplified (Prof G) | 7 Best ETFs to invest in ROTH IRA Forever | Buffett Indicator ~230% (highest ever); S&P 35% concentrated in top-7 (above dot-com peak) | Medium |
| Investing Simplified (Prof G) | 2 other videos | ETF/portfolio content, minor de-dollarization mention | Low |
| Real Vision Presents | What Finance Looks Like in 5 Years?! | TradFi/DeFi convergence thesis, long-horizon thematic | Low |
| Finary | Bienvenue dans le siècle chinois | China-rise/US-decline geopolitical background | Low |
| Finary | Bon salaire, mauvaises décisions | Personal finance case study, no regime signal | — |
| Oseille TV | 7 videos | Expat tax/broker wealth-mgmt content, no regime signal | — |

**Consensus (2+ channels):** (1) Hawkish Fed surprise raising rate-hike odds — Gammon + IG France. (2) AI/tech valuation stretch as vol driver — Bravos Research + IG France + Prof G. (3) Current pullback framed as not-yet-confirmed regime break — Bravos Research + IG France.

**HMM read:** watch-list only — precursor conditions present (hawkish Fed, stretched AI valuations, dollar/FX stress) but no 3-bar stable regime shift confirmed by commentary. No UEMOA/Africa wealth content this cycle.
