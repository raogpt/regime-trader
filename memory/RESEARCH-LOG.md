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

## 2026-07-13 — Market Intel (regime_trader)
| Source | Type | Item | Regime Signal | Vol Bias | Relevance |
|--------|------|------|----------------|----------|-----------|
| Yahoo Finance | blog | Strait of Hormuz tensions squeeze Wall St pre-bell; US airstrikes on Iran, Iran retaliates; futures/oil react | Fresh war escalation, risk-off open | HIGH | High — direct SPY/QQQ/IWM driver |
| WSJ Markets | blog | Oil rises, gold slides on fresh U.S.-Iran strikes ("reviving concerns about inflation and prospects of tighter monetary policy") | Inflation-driven risk-off; gold down not up (hike fear dominates) | HIGH | High |
| WSJ Markets | blog | "Oil Prices Could Stay Elevated as Mideast Tensions Rise"; Treasury yields edge higher | Sustained energy/rate pressure | HIGH | High |
| CNBC — Finance | blog | Kalshi traders: Strait of Hormuz traffic won't normalize until 2027 (only 43% odds by Dec 1) | Prediction markets pricing prolonged disruption | HIGH | Med-High |
| CNBC — Finance | blog | Kalshi traders: odds gas >$3.50 through election day jump to 75% | Sustained energy/inflation pressure | HIGH | Med |
| Investing.com — Market Overview (3 headlines) | blog (title-only) | "US Markets Open to a War", "Gulf Tensions Igniting Risk-Off Monday", "Middle East Tensions Fuel Fed Hike Bets" | Risk-off + hawkish repricing | HIGH | High — but headline-only, low confidence detail |
| Seeking Alpha — Market Currents | blog (title-only) | Crude oil climbs >3% as US/Iran fight for Hormuz control | Oil-driven vol confirmation | HIGH | Med — title only |
| Liberty Street Economics (NY Fed) | blog | Tariff pass-through survey: ~47% service / 44% mfg firms still plan further price hikes from tariffs | Sticky, still-building inflation input | Supports HIGH | High — Fed/HMM relevant |
| Liberty Street Economics (NY Fed) | blog | Small Business Credit Survey: majority of goods/retail firms report tariff cost challenges in 2025 | Inflation persistence, corroborates above | Supports MID-HIGH | Med |
| Motley Fool | blog | Fed minutes show rate HIKE (not cut) "fully on the table" 2026; CME FedWatch shows 81.9% odds fed funds ends year above current range | Hawkish Fed regime shift | HIGH | High |
| CNBC — Economy | blog | Fed June minutes show officials split on rate direction ("family fight" could drag on) | Policy uncertainty at the Fed | MID-HIGH | High |
| Federal Reserve (official) | blog | June 16-17 FOMC minutes released; Warsh names task force leadership | Institutional/Fed governance context | Neutral | Med |
| Yahoo Finance | blog | Stocktwits retail sentiment: bullish on SPY, neutral on QQQ during Iran-driven selloff | Rotation: SPY favored over QQQ in sentiment | Rotation signal | High — direct SPY/QQQ split |
| Motley Fool | blog | "3 Dividend Stocks Leading 2026's Rotation Into Value" — tech worst H2 sector so far; capital flowing to energy/financials/healthcare/staples after soft jobs report | Broadening away from AI/tech mega-caps | Rotation (QQQ risk, IWM/value tailwind) | High |
| ETF Trends (VettaFi) | blog | "'Mega-Rotation' Could Lift This Income ETF" — breadth widening beyond AI trade, brief July 7 pullback | Confirms broadening/rotation | Med-High | High |
| ETF Trends (VettaFi) | blog | "Broadening Trade Returns as Conflict Eases. Can It Outlast a Hawkish Fed and Fading Liquidity?" — H1 2026 recap | Rotation thesis now tested by hawkish Fed + fading liquidity | Cautionary | High |
| The Big Picture (Ritholtz) | blog | Monday reads cite WSJ survey: "War Leaves Economy With More Stubborn Inflation," economists raising 2027 inflation forecasts | Confirms sticky-inflation narrative independently | HIGH | Med-High |
| Motley Fool | blog | Michael Burry places AI short bets, calls it "the beginning of the end" (single-name framed but macro AI-bubble theme) | AI-bubble sentiment risk flag | Vol risk | Med |
| WSJ Markets | blog | "The Quarter-Trillion-Dollar Onslaught of AI Bonds Is Testing Investors' Limits" | Credit-market stress from AI capex debt issuance | Vol risk | Med-High |
| WSJ Markets | blog | "AI Jitters Weigh on Nasdaq Futures"; "Tech Stock Jitters Just Went Off the Charts" | Tech-specific volatility elevated | HIGH (QQQ-specific) | High |
| ETF Trends (VettaFi) | blog | Bitcoin ETFs in longest outflow streak on record (~$8B over 8 weeks); early signs of a bounce | Risk-appetite cooling in crypto, tentative stabilization | Med | Low-Med (sentiment proxy, not ETF universe) |
| ETF Trends (VettaFi) | blog | "So Far, So Good" — soft June jobs report (+57k, participation 61.5%) reduced odds of immediate July hike; front-end yield curve rallied | Partial dovish counter-signal to the hawkish narrative | Mixed | High |
| ETF Trends (VettaFi) | blog | Treasury Yields Snapshot 7/10: 10y 4.56%, 2y 4.21% | Rate-level/curve data point (normal curve) | Context | Med |
| Motley Fool + Yahoo Finance (2 sources) | blog | Bank earnings season opens Tue 7/14: JPM, WFC, C, GS, BAC report | Cross-source macro read via bank earnings | Catalyst event (2 days out) | High — earnings/catalyst filter relevant |
| WSJ Markets | blog | "How to Invest When the Global Crises Never Stop" — argues bond yields need higher risk premium in a multi-crisis world | Wealth-mgmt regime framing | Context | Med |
| CNBC — Economy | blog | India inflation accelerates to 4.38% in June (Iran war + food/energy); China CPI soft but PPI near 4-yr high | Global inflation spillover from war, independent of US sources | HIGH | Med |
| ETF Trends (VettaFi) | blog | "Focus on Intent" — post-tax-season reminder to revisit estate planning docs | Wealth-mgmt (generic) | Low direct | Low |
| WSJ Markets | blog | "10 of the Best Financial Advisor Companies" — fiduciary RIA rankings | Wealth-mgmt reference | Low | Low |
| Motley Fool (3 items) | blog | Retirement/Social Security personal-finance pieces ("$500k enough to retire?", SS claim-at-70 math, spousal benefits) | Wealth-mgmt, evergreen | n/a | Low |
| FRED Blog (St. Louis Fed) | blog | Primary vs. total deficit history; foreign-held US assets ~59% equities / ~24% Treasuries | Fiscal/macro background context | Low-Med | Low |
| IG France (Alexandre Baradez) | youtube (title-only) | "MarketLive: derniers tendances graphiques des marchés" | Unknown content — title-only | Low confidence | Low |
| Motley Fool (46 remaining items) | blog | Single-stock/AI-name deep dives (Nvidia, SpaceX, Micron, Nike, Salesforce, UnitedHealth, etc.) and generic index-fund/retirement explainers | — | — | Low — outside ETF-only mandate |
| ETF Trends (VettaFi) (~35 remaining items) | blog | Niche ETF launches and sector pieces (nuclear, drones, dividends, CLOs, healthcare, REITs) | — | — | Low-Med — product-level, not macro |
| WSJ Markets (~35 remaining items) | blog | M&A/deals, opinion columns, company-specific stories (UniCredit/Commerzbank, Circle bank charter, etc.) | — | — | Low |
| Investing.com — Stock Market News (10 items) | blog (title-only) | Single-company headlines (Q32 Bio, Ford/Unifor, Meta data center, Fraport, etc.) | — | — | Low — title-only |
| Seeking Alpha — Market Currents (6 remaining items) | blog (title-only) | Single-company news headlines (CoreCivic, Ocugen, Gamehaus, Cathie Wood trades, etc.) | — | — | Low — title-only |

## 2026-07-23 — YouTube/Market Intel (regime_trader)
Note: routine had not run since 2026-07-13 (10-day gap) — 288 new items across 20 sources analyzed in one batch. Full detail in `reports/2026-07-23-market-intel.md`.

| Source | Type | Item | Regime Signal | Vol Bias | Relevance |
|--------|------|------|----------------|----------|-----------|
| WSJ Markets | blog | "Two Wars Put Stranglehold on Global Energy Supplies" — Hormuz, Bab al-Mandeb, Black Sea chokepoints imperil ~25% of world oil supply | Multi-front energy-supply shock, escalated vs. 7/13 | HIGH | High |
| WSJ Markets | blog | Oil tops $98/bbl on Houthi Red Sea tanker attacks + Iran escalation (4th straight up session); bond yields near 2026 highs | Sustained oil/rate pressure | HIGH | High |
| CNBC — Economy | blog | "Renewed Hormuz hostilities drive ECB rates rethink amid 'extremely volatile' outlook" | Vol spillover to ECB policy path | HIGH | High |
| Yahoo Finance | blog | "Fed Chair Kevin Warsh Just Threw Cold Water on Investors Who Thought the Worst of Inflation Was Over" despite June CPI cooling to 3.5% (vs 3.8% forecast) | Hawkish surprise vs. cooling data | HIGH | High — direct Fed/HMM input |
| CNBC — Economy | blog | Kevin Warsh's recurring phrases ("family fight," "first principles," "inflation is a choice") — Fed watchers parsing rhetoric for policy signal | New-chair hawkish framing | Med-High | High |
| CNBC — Finance | blog | Dallas Fed's Logan calls for "modestly" higher rates; separately NY Fed's Williams says inflation "has peaked," rates "well positioned" | FOMC genuinely split, not just rhetoric | Med-High | High |
| CNBC — Finance | blog | "WarshGPT": Wall Street leaning on AI to parse a new, less-communicative Fed era | Regime uncertainty around Fed signal itself | Med | Med |
| Motley Fool | blog | "Prediction: The Fed Hikes Rates Once in 2026" — citing May YoY inflation spike to 4.2%, still above target after June's 3.5% print | Explicit hike call, hawkish tail risk | HIGH | High |
| ETF Trends (VettaFi) | blog | "Rate Cuts Aren't Guaranteed; Consider Preferred Stock ETF VRP" | Confirms contested rate path | Med-High | Med |
| CNBC — Finance | blog | Jamie Dimon: markets "underestimate risks," wouldn't buy stocks or Treasurys at current prices; Buffett separately calls market "increasingly defined by speculative trading" | Two top allocators flag valuation/vol risk | Med-High | High |
| WSJ Markets | blog | "Nasdaq Slips Ahead of Earnings From Tesla, Alphabet"; Alphabet beats (cloud +82%) but stock falls after-hours on capex-hike guidance; Tesla posts negative FCF for first time in 2+ yrs | Mega-cap earnings whipsaw, QQQ-specific | HIGH | High |
| WSJ Markets | blog | "Chip Stocks Recover, Boosting Nasdaq" / "Chip Stocks Shrug Off Chinese AI Worries" — following George Gammon's (YouTube, title-only) "AI Bubble Just Popped" thesis and a semis "bloodbath" | Semis: correction then partial recovery — high realized vol | HIGH (QQQ-specific) | High |
| ETF Trends (VettaFi) | blog | "Cyber ETFs Surge While Semis Stumble" — capital rotating within tech from semis to cybersecurity, not fully out of tech | Intra-sector rotation, not broad de-risking | Med-High | High |
| ETF Trends (VettaFi) | blog | "Concentration Risk Continues: Why Now's the Time to Diversify" — top-5 S&P names ~27% of index (Ritholtz independently notes same ~27% figure, in line with late-1960s/70s peak) | Concentration risk flagged by 2 independent sources | Med-High | High |
| Motley Fool / Investing.com / WSJ (3 sources) | blog | SpaceX (SPCX, IPO'd June) down ~47% from high, closed at all-time low; short interest risen to 32% of float | Single-name but systemically watched — AI/space-hype unwind | Med (concentration/sentiment proxy) | Med |
| CNBC — Economy | blog | China Q2 growth slowest since 2022, missing stimulus-target range, fanning stimulus calls | Global growth deceleration input | Med-High | Med |
| ETF Trends (VettaFi) | blog | "T. Rowe Price's Love Says Small-Cap Earnings Are Turning" — small/mid trading 20-35% below large caps, earnings estimates rising after 10 quarters of declines | Small-cap rotation-in signal | Rotation (IWM tailwind) | High — direct IWM signal |
| ETF Trends (VettaFi) | blog | "A Shift In Stock Market Leadership" / "ETFs for the Next Leg of Earnings Expansion" (equal-weight favored as earnings growth broadens beyond Mag7) | Broadening beyond mega-cap tech continues | Rotation (SPY breadth, QQQ-neutral) | High |
| ETF Trends (VettaFi) | blog | "Risk-Wary Family Offices Double Down on Infrastructure"; "Bonds Are Back" (declining cash yields, attractive real Treasury yields, rebalance-into-bonds thesis) | Institutional derisking/diversification underway despite headline index strength | Cautionary / defensive positioning | High |
| Yahoo Finance | blog | "S&P 500 Q2 Earnings Beats Hit 5-Year Highs as Growth Accelerates" | Offsets bearish vol narrative — fundamentals still strong | Counter-signal (lower vol) | High |
| Investing.com — Stock Market News | blog | "FDIC Issues a Warning About an Increasing Risk in Big Banks" | Bank-sector risk flag | Med | Med |
| Liberty Street Economics (NY Fed) | blog (3-part series) | Basel III capital reallocation to nonbank BHC subsidiaries — regulatory-arbitrage research | Financial-stability background, echoes FDIC warning above | Low-Med | Med |
| WSJ Markets | blog | "The Long Bond Is Making People Nervous"; 2-year Treasury yield "highest in over a year" | Broad curve rate pressure, not just short end | HIGH | High |
| George Gammon, IG France, Real Vision, Oseille TV, Finary, Investing Simplified (22 items) | youtube (title-only) | Titles suggest: AI-bubble/derivatives-risk warnings (Gammon), EUR/USD + BCE/Fed positioning + Hormuz oil impact (IG France), dividend-ETF and SCHD-vs-JEPI income strategy (Prof G), French wealth-mgmt/retirement/currency content (Finary), African-passport/wealth-migration piece (Oseille TV) | Directionally consistent with blog-sourced themes above (AI vol, Fed/Hormuz, rotation) but unconfirmed | Low confidence — all queued to `memory/transcript-queue.json` for off-cloud fetch | Med (Africa item = wealth-mgmt priority per mandate, still title-only) |
| Motley Fool (~45 remaining), ETF Trends (~35 remaining), WSJ (~45 remaining), Investing.com/Seeking Alpha (~24 remaining, title-only) | blog | Single-stock AI-name pieces (Nvidia, Micron, AMD, Alphabet, SpaceX granular coverage), niche ETF launches, M&A/opinion, single-company headlines | — | — | Low — outside ETF-only mandate, see report for rollup |
