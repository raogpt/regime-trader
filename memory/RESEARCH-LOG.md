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

## 2026-07-16 — Market Intel (regime_trader)
Catch-up run covering 2026-07-14 through 2026-07-16 (last checked 2026-07-13). 241 new items across 20 sources; 6 new YouTube videos (all title-only, transcripts queued). Full report: `reports/2026-07-16-market-intel.md`.

| Source | Type | Item | Regime Signal | Vol Bias | Relevance |
|--------|------|------|----------------|----------|-----------|
| CNBC — Economy | blog | June CPI +3.5% YoY, below 3.8% expected | Disinflation surprise #1 | Dovish | High |
| CNBC — Economy | blog | June PPI -0.3%, steepest drop in 1yr+ (Yahoo Finance corroborates) | Disinflation surprise #2 | Dovish | High |
| CNBC — Finance | blog | Incoming Fed Chair Warsh pledges "regime change" to end inflation "tax" | Hawkish rhetoric vs. cooling data | Hawkish | High |
| CNBC — Finance | blog | NY Fed's Williams: inflation "has peaked," rates "well positioned" | Directly contradicts Warsh — split Fed messaging | Mixed/uncertainty | High |
| CNBC — Economy | blog | Renewed Hormuz hostilities ("several consecutive days of strikes") drive ECB rates rethink amid "extremely volatile" outlook | Iran conflict escalated, not resolved, since 7/13 report | HIGH | High |
| WSJ Markets | blog | "U.S. Stock Futures Fall on Fresh AI Wobble" — Korea Exchange briefly suspended SK Hynix/Samsung trading | Sharp, distinct AI/chip selloff, QQQ-concentrated | HIGH | High |
| Investing.com — Market Overview (title-only) | blog | "TSMC Beats but the AI Trade Loses More Altitude", "Middle East Tensions and Chip Selloff Set the Tone" | Corroborates WSJ chip-selloff signal | HIGH | Med-High |
| Investing.com — Stock Market News (title-only) | blog | "South Korea leads record Asia equity outflows as tech slump, rate hike hit" | Third independent confirmation of chip-sector outflows | HIGH | Med |
| Yahoo Finance | blog | "Dow Jones Futures: Apple, Google Mask Dell, Sandisk, Micron Sell-Off" | 3rd+ source confirming same-day AI selloff | HIGH | High |
| George Gammon | youtube (title-only) | "It's Official, The AI Bubble Just Popped" — published same day (7/16) as blog-source selloff consensus | Same-day title corroboration | HIGH (unverified) | Med — title-only |
| ETF Trends (VettaFi) | blog | "Small Caps Rally Is Running With Strong, Fundamental Legs" — Russell 2000 outpacing S&P 500 | Rotation signal: IWM relative strength | Rotation | High — direct IWM signal |
| ETF Trends (VettaFi) | blog | "Small-Caps Offer Rare Value as Sector Gaps Narrow" — Morningstar Q3 2026 outlook now favors equal-weighting | Corroborates rotation thesis w/ named source | Rotation | High |
| Yahoo Finance | blog | "Review & Preview: Losing Momentum" — momentum strategy underperforming | Consistent with rotation away from crowded AI/momentum trade | Rotation | Med-High |
| WSJ Markets | blog | "Wall Street Traders Are Having Their Best Year Ever" — "market is clearly extremely risk-on" | Record risk-on positioning same morning as chip selloff — possible inflection point | Contrarian/context | High |
| CNBC — Finance | blog | Morgan Stanley record quarterly revenue, equities trading +69% YoY (Goldman/JPM peers) | Confirms risk-on trading revenue tailwind | Context | High |
| Yahoo Finance | blog | "As AI Gobbles the Market, Make Sure You're Truly Diversified" | Diversification-against-concentration wealth-mgmt angle | Context | Med — wealth mgmt |
| Finary | youtube (title-only) | "Votre argent ne vaut rien" (Your money is worth nothing) — French, currency/purchasing-power theme likely | Unknown — transcript pending | Low confidence | Med — wealth mgmt, pending |
| Oseille TV | youtube (title-only) | "Ces pays d'Afrique vendent leur passeport" — citizenship-by-investment | Unknown — transcript pending | Low confidence | Low-Med — Africa-adjacent, tangential |
| Investing Simplified (Prof G) | youtube (title-only) | "This Market Dip Just Created the BEST Buying Opportunity of 2026" | Contrarian-bullish counterweight, unverified | Low confidence | Med — pending |
| IG France (Alexandre Baradez) (5 items, title-only) | youtube | Titles reference inflation-data non-reaction and USA-Iran impact on oil/rates/equities | Directionally aligned w/ blog consensus, unverified | Low confidence | Med |
| WSJ Markets (~35 remaining) | blog | Deals/M&A, opinion columns, single-company stories | — | — | Low |
| Motley Fool (50 items) | blog | Single-stock deep dives (Nvidia, AMD, Qualcomm, IBM, Lucid, etc.) | — | — | Low — outside ETF-only mandate |
| ETF Trends (VettaFi) (~47 remaining) | blog | Niche ETF product/launch coverage | — | — | Low — product-level |
| Federal Reserve / Liberty Street / FRED Blog (1 each) | blog | Discount-rate minutes, nonbank regulatory-arbitrage research, state GDP data | — | — | Low — background only |
| **No UEMOA/Africa allocation content found** | — | Explicit keyword check across all 241 items: zero direct matches | — | — | — |
