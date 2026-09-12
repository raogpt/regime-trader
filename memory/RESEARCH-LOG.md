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

## 2026-09-12 — Market Intel (regime_trader)
Full report: `reports/2026-09-12-market-intel.md`. Covers a ~2-month gap since last check (2026-07-13); 291 new items, 96 YouTube (all title-only, transcripts blocked from cloud IP, 81 newly queued).

| Source | Type | Item | Regime Signal | Vol Bias | Relevance |
|--------|------|------|----------------|----------|-----------|
| Investing.com — Market Overview (6 of 7 headlines) | blog (title-only) | "Hot CPI Report Puts a Fed Rate Hike Squarely Back on the Table," "Sure Fed Hike Ahead," "FOMC Preview: Fed Set To Hike 0.25%," "Fed Rate Hike Looks Locked In" | Hawkish Fed hike now near-consensus (vs. contested in July) | HIGH | High — direct HMM/rates input |
| Yahoo Finance | blog | Hot August CPI: +0.4% m/m, 3.4% y/y | Triggers the hike-consensus wave above | HIGH | High |
| WSJ Markets | blog | "The Fed Is Poised to Raise Interest Rates for the First Time in Years"; "Wall Street Cheers Clarity on Fed Outlook—Even if It Means Higher Rates" | Hawkish shift, but stocks rose on reduced uncertainty | HIGH (rate-level) / lower (policy-uncertainty) | High |
| WSJ Markets (×2) | blog | "Government Bond Yields Finish Near Multiyear Highs"; "10-Year Yield on the Cusp of 5%" | 10y up from 4.56% (July) toward 5% | HIGH | High |
| WSJ Markets | blog | Saudi shuts vital Hormuz-bypass pipeline; Houthis take oil chokepoint; oil to $102-107/bbl | Second live war-driven oil/yield spike | HIGH | High — direct SPY/QQQ/IWM driver |
| Seeking Alpha — Market Currents | blog (title-only) | "Saudi shuts pipeline that was vital Hormuz bypass as new front opens in Middle East war" | Corroborates oil/war cluster | HIGH | Med — title-only |
| IG France (Baradez) | youtube (title-only) | "Fed : un seul chiffre vendredi peut tout changer" (pre-CPI); "Pourquoi le pétrole à 94$ fait exploser les taux souverains" | Anticipated CPI catalyst; corroborates oil→yields link | HIGH | Med — title-only but validated by blog cluster |
| Motley Fool | blog | Shiller CAPE ratio at 41.7 — second-highest ever after dot-com peak | Valuation-stretch warning | Correction risk | High |
| Yahoo Finance | blog | Morgan Stanley's Mike Wilson warns of possible stock market correction | Named major-bank correction call | Correction risk | High |
| Investing.com — Market Overview | blog (title-only) | "Market at a Critical Point: Nasdaq, Russell and VIX Signals" | Direct QQQ/IWM/vol framing | Unknown detail | Med — title-only, most on-mandate hit this cycle |
| WSJ Markets | blog | Bank of Japan tightening bets spark yen recovery; WSJ Dollar Index whipsaws | Fed/BoJ policy divergence, cross-asset watch item | Mixed | Med-High |
| The Big Picture (Ritholtz) | blog | "Corporate vs Treasury Debt Duration" — corporate America locked in low fixed rates 2008-2022, US govt did not | Sovereign debt more exposed to rate rise than corporate credit | Context | Med-High |
| Liberty Street Economics (NY Fed) | blog | "Are Central Banks Moving Out of Dollar Assets?" — aggregate dollar reserve-share decline traced to a few large holders, not systemic exit | Nuance against dollar-crisis narrative | Context | Med |
| George Gammon + Bravos Research (22 items) | youtube (title-only) | Recurring crisis-framed titles: "House of Cards About To Fall," "Global Monetary Reset," "$10T Derivatives Timebomb," "Dollar Will Lose Reserve Status" | Directionally consistent w/ debt/dollar-stress theme, not independent evidence | Low confidence | Low-Med |
| Investing Simplified (Prof G) (YouTube) | youtube (title-only) | "Worried About a 'Lost Decade'?"; "Major OverPriced Market"; "next big market crash" | Consistent w/ CAPE/correction theme | Low confidence | Low-Med |
| Finary, Oseille TV (28 items) | youtube (title-only) | Evergreen FR personal-finance/psychology content; one African-passport/residency title (not allocation-relevant) | — | — | Low — no UEMOA/Africa wealth-mgmt hit this cycle |
| Federal Reserve (official, 20 items) | blog | Mostly routine bank enforcement/charter actions; July FOMC statement/minutes now superseded by Sept CPI repricing | — | — | Low (subset High: FOMC minutes) |
| Motley Fool (46 remaining), Investing.com — Stock Market News (10), Seeking Alpha (6 remaining) | blog | Single-stock/insider-sale/M&A content (Qualcomm, Lululemon, GameStop, Etsy, etc.) | — | — | Low — outside ETF-only mandate |
