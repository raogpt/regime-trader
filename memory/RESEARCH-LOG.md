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

## 2026-07-14 — Market Intel (regime_trader)
| Source | Type | Item | Regime Signal | Vol Bias | Relevance |
|--------|------|------|----------------|----------|-----------|
| WSJ Markets | blog | "Oil Surges Most Since 2020" — Trump reimposes Strait of Hormuz blockade, 3rd straight night of US strikes on Iran; Brent >$85 | War escalation deepening, not resolving | HIGH | High — direct energy/inflation driver |
| Investing.com — Market Overview | blog (title-only) | "Oil Jumps, Bonds Break and the AI Trade Starts Losing Its Shine"; "War, Yields, Yen and AI Collide Across the Global Fault Lines" | Multi-asset stress compounding (oil+bonds+AI) | HIGH | High — directly ties oil/rates shock to QQQ-relevant AI trade |
| Seeking Alpha — Market Currents | blog (title-only) | "AI boom: Data-center operators reportedly race to sell majority stakes" | Corroborates WSJ AI-financing-stress item independently | HIGH (QQQ) | Med-High |
| WSJ Markets | blog | "Data-Center Builders Are Racing to Offload Stakes Worth Billions" — investors seeking to own AI physical infra directly | AI-capex financing stress continuing from 7/13 | HIGH (QQQ) | High |
| CNBC — Finance | blog | Waller: Fed "shouldn't fight the last war" on inflation but hikes still possible | Hawkish-Fed thesis persists into CPI day | HIGH | High |
| Investing.com — Market Overview | blog (title-only) | "Waller Warns Fed May Need to Hike Rates If June's CPI Runs Hot"; "US CPI Preview: Will the Fed Actually Hike Rates on a Hot Inflation Report?" | Today's CPI print (8:30am ET) framed as the swing catalyst for hike odds | HIGH | High — direct earnings/catalyst-filter trigger, same-day |
| Motley Fool | blog | "Prediction: Today's Inflation Report Will Contain a Much-Needed Silver Lining, but Also Highlight Something Sinister" — June CPI due 8:30am ET | Headline decline expected but underlying detail flagged as problematic | HIGH | High — CPI is today, not 2 days out |
| CNBC — Finance | blog | "A July rate hike from the Fed? The odds are rising" — tied to oil spike from Hormuz | Rate-hike odds rising in tandem with oil shock | HIGH | High |
| CNBC — Finance | blog | "Big banks poised to report booming revenue" — SpaceX IPO + Iran war volatility cited as tailwinds for Q2 bank results | Volatility itself becoming a Wall St revenue driver | Confirms HIGH | High — bank earnings same day (7/14) |
| WSJ Markets | blog | "Dollar Could Rise if U.S. Core Inflation Data Exceed Forecasts" vs. "Dollar Faces Pullback as Fed Might Not Lift Rates" (7/13) | Contested/two-sided Fed-direction pricing, same pattern as prior day | Mixed | High — rates/FX regime input |
| WSJ Markets (×2) | blog | "Gold Falls Below $4,000" (7/13) then "Gold Rises on Inflation Concerns" (7/14) | Gold whipsawing both directions in 24h — inflation-vs-rate-hike tug of war | HIGH (elevated vol, no clean direction) | High |
| Investing.com — Market Overview | blog (title-only) | "Gold Caught in the East-West Divide: Is the Bullish Wave About to Begin?" (×2 headline variants) | Independent confirmation gold direction is contested/unsettled | Mixed | Med |
| Yahoo Finance (Stocktwits) | blog | Retail sentiment flipped: QQQ improved to "bullish", SPY declined to "neutral" — reverse of 7/13 read (SPY bullish/QQQ neutral) | Rotation signal reversing day-over-day | Rotation flip | High — direct SPY/QQQ divergence, opposite sign from yesterday |
| Investing.com — Market Overview | blog (title-only) | "Traders Tilt to Heavy Buy in the Nasdaq 100 Following Latest Pullback" | Dip-buying flow into QQQ-adjacent index | Consistent with QQQ sentiment flip above | Med-High |
| WSJ Markets | blog | "U.S. Stocks Fall as AI Selloff, Oil Jump Rattle Markets" (7/13, carried into 7/14 futures) | Confirms chip/AI-led selloff alongside oil shock | HIGH (QQQ-specific) | High |
| ETF Trends (VettaFi) | blog | "Revenue Weighting Has Relevance" — S&P 500 top-5 concentration risk flagged as indexes sit near all-time highs | Concentration-risk framing relevant to SPY regime interpretation | Context | Med-High |
| ETF Trends (VettaFi) | blog | "Revival of Oil Turbulence Puts These Energy ETFs in Focus" — explicitly ties Iran conflict to renewed oil-linked ETF volatility | Confirms energy-linked vol regime shift | HIGH | Med-High |
| CNBC — Economy | blog | India inflation 4.38% in June, 8th straight monthly rise (Iran war + weak rainfall) | Independent non-US confirmation of war-driven inflation spillover | HIGH | Med |
| CNBC — Finance | blog | Kalshi launches "Pro" product for perpetual futures / multi-market traders | Market-structure note, not a direct signal | Low | Low |
| Bravos Research | youtube (title-only) | "Nobody is Prepared for What's About to Happen…" | Unknown content — title-only, queued for transcript | Low confidence | Low |
| IG France (Alexandre Baradez) | youtube (title-only) | "MarketLive: dernières tendances graphiques des marchés"; Short: "BCE et Fed : les marchés anticipent le pire (et ça se voit)" | Short's title alone signals markets pricing a hawkish ECB/Fed outcome | Low confidence (title-only) | Med (title directly macro-relevant) — queued for transcript |
| FRED Blog (St. Louis Fed) | blog | Real GDP growth by state Q1 2026 — 47/50 states grew, national avg 2.1% annualized | Background growth data, no near-term vol signal | Low | Low |
| The Big Picture (Ritholtz) | blog | "10 Monday AM Reads" — cites WSJ survey: economists raising 2027+ inflation forecasts on Iran conflict cost embedding | Corroborates sticky-inflation thesis independently | HIGH | Med-High |
| WSJ Markets | blog | "10 of the Best Financial Advisor Companies" — fiduciary RIA rankings | Wealth-mgmt reference | Low | Low |
| Motley Fool (48 remaining items) | blog | Single-stock deep dives (Micron, Walmart, Buffett/Berkshire, American Express, Chipotle, etc.) and generic retirement/dividend explainers | — | — | Low — outside ETF-only mandate |
| ETF Trends (VettaFi) (~18 remaining items) | blog | Niche/product-level ETF pieces (ETF of the Week, fixed-income launches, nuclear, single-nation World Cup ETFs, active-ETF AUM growth) | — | — | Low-Med — product-level, not macro |
| WSJ Markets (~15 remaining items) | blog | Market-Talk roundups (energy, health care, TMT, basic materials), opinion (Chicago pensions), Goldman GC story | — | — | Low |
| Investing.com — Stock Market News (10 items) | blog (title-only) | Single-company headlines (Maersk, Debenhams, Ericsson, Indra, Genus, Rank, BMW recall, etc.) | — | — | Low — title-only |
| Seeking Alpha — Market Currents (6 remaining items) | blog (title-only) | Single-company news headlines (Watches of Switzerland, Google/Android probe, Samsung ADR, AstraZeneca license) | — | — | Low — title-only |
| Yahoo Finance — Market News (S&P 500) (~15 remaining items) | blog | Single-stock movers (SanDisk, AppLovin, Astera Labs, SolarEdge, Clearway Energy, etc.) | — | — | Low — outside ETF-only mandate |
