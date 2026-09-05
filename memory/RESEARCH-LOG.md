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

## 2026-09-05 — Market Intel (regime_trader)
| Source | Type | Item | Regime Signal | Vol Bias | Relevance |
|--------|------|------|----------------|----------|-----------|
| WSJ Markets | blog | Dovish Fed comments (Gov. Waller signals could support holding rates steady) 9/3 — Dow +600pts, stocks/bonds rally, yields fall | Dovish repricing | Eases HIGH | High |
| WSJ Markets | blog | Blowout August jobs report 9/4 reverses 9/3 dovish move — stocks fall, short-term Treasury yields climb, rate-hike bets resurge | Hawkish whipsaw within 48h | HIGH | High — most actionable item in batch |
| WSJ Markets | blog | Gold, silver futures slip on blowout jobs report as short-term yields climb, Sept-hike odds rise | Confirms hawkish repricing (gold down not up) | HIGH | High |
| WSJ Markets | blog | WSJ Dollar Index falls 0.68% on the week to 95.24 (down most of the week) despite hawkish jobs data — cross-asset divergence | USD weak even as rate-hike bets rise | Med-High | High |
| WSJ Markets | blog | Japanese yen strengthens to 1-month high on BOJ/MOF intervention chatter; Japan "vows to keep eye on yen" as weak-yen inflation risk builds | FX-intervention risk, JPY carry-unwind watch | Med-High | Med-High |
| WSJ Markets | blog | Oil futures post weekly gain on Middle East escalation (resumed US strikes on Iran, Iranian shipping attacks); diesel hits record $5.85/gal | Sustained energy/inflation pressure | HIGH | High |
| WSJ Markets | blog | "There Are Four Forces Pressuring Bonds: War Is No. 1" — war, fiscal deficits, new Fed chair uncertainty, AI-bond issuance flood all cited as yield drivers | Multi-factor bond-stress thesis | HIGH | High |
| WSJ Markets | blog | "Oil Prices Push Global Bond Market Closer to the Edge" — energy costs framed as the inflationary trigger behind rising yields | Corroborates bond-stress thesis independently | HIGH | High |
| WSJ Markets | blog | 5 sector "Market Talk" roundups (Energy, Auto, Materials, Tech/Media, Health Care), all dated 9/4, reference jobs-report-day moves (gold down, diesel record, choppy tape) | Corroborating detail, not new signal | HIGH (context) | Med |
| WSJ Markets | blog | "Why We'll Have to Get Used to 'Meh' Job Reports"; European indexes edge higher in early trade despite US jobs shock | US/Europe reaction diverges | Mixed | Med |
| Investing.com — Market Overview | blog (title-only) | 10/10 headlines all on hot jobs report/Fed-hike risk ("Gold and Bitcoin Hit by Hot US Payrolls and Fed Hike Risk," "A New US Economic Equation: Strong Jobs, Higher Oil and a Tougher Fed Decision," "Trump Threatens to Halt Trade Unless the Fed Cuts Rates") | Strong 2nd-source corroboration of jobs/Fed story | HIGH | High — title-only, weight down |
| Yahoo Finance — Market News | blog | "S&P 500, Dow End Lower As Blowout Jobs Report Fans Rate Hike Fears" + "Review & Preview: A Strong Jobs Report Has Investors Bracing for a Rate Hike" | 3rd independent source corroboration | HIGH | High |
| IG France (Alexandre Baradez) | youtube (title-only) | Non-"MarketLive" titles: US household/market leverage rising sharply, Nvidia/Meta/Alphabet CDS spreads widening, US borrowing costs up on Iran war, Fed watching yen-vs-dollar | Credit/leverage stress theme, title-only | Med (low confidence) | Med |
| George Gammon + Bravos Research (19 combined) | youtube (title-only) | Recurring alarmist dollar/debt/derivatives narrative ("$10 Trillion Derivatives Timebomb," "Global Debt Crisis," "Dollar Will Lose Reserve Currency Status," "Global Monetary Reset," "Japan and the US Just Pulled the Trigger") | Low-confidence recurring sentiment signal only, no transcript to verify | Low-confidence directional | Low-Med (sentiment gauge) |
| Liberty Street Economics (NY Fed) | blog | "Are Central Banks Moving Out of Dollar Assets?" — dollar share of global FX reserves fell 64%→56%, 2015-2025 | Structural dollar-reserve erosion; supports weak-USD backdrop seen this week | Med | Med-High |
| Liberty Street Economics (NY Fed) | blog | "A Window into Bond Investors' Uncertainty About R-Star" — term-structure-implied uncertainty about neutral rate | Rates-regime research, directly relevant to HMM rate inputs | Med | Med-High |
| Liberty Street Economics (NY Fed) | blog | "Does the Equity Term Structure Respond to Monetary Policy Shocks?" | Equity-vol / monetary-policy linkage research | Med | Med |
| Liberty Street Economics (NY Fed) | blog | "Stablecoins and (Non)Crypto Shocks: A 2026 Update" | Stablecoin/crypto-adjacent financial-stability research | Low-Med | Low-Med |
| Liberty Street Economics (NY Fed) | blog | "How Distressed Are Consumers? Reconciling Diverging Credit Card Delinquency Measures" — total household debt balances -$13B in Q2 2026 | Consumer-credit health check, mildly reassuring | Low-Med | Med |
| Liberty Street Economics (NY Fed, 6 remaining) | blog | Nonbank/Basel-III regulatory-arbitrage trilogy, AI-and-labor pieces, renter-mobility, Jackson Hole recap, STRIPs trading activity — structural/academic, no near-term trading signal | — | — | Low |
| Federal Reserve (official) | blog | FOMC statement, 7/29/2026 | Primary Fed policy event (rate decision) | — | High (event marker) |
| Federal Reserve (official) | blog | FOMC minutes for the July 28-29 meeting, released 8/19 | Primary Fed policy event | — | High |
| Federal Reserve (official) | blog | Discount-rate meeting minutes: 7/20 & 7/29 (released 8/25), 6/8 & 6/17 (released 7/14) | Regional-Fed policy input, corroborates FOMC timeline | — | Med-High |
| Federal Reserve (official, 15 remaining) | blog | Routine enforcement actions (8, mostly "former employee of [Bank]") + bank-application approvals (4: NatWest, Coastal Bend, FS Bancorp, Santander) + regulatory-proposal comment requests (3) | No regime signal | — | Low |
| The Big Picture (Ritholtz) | blog | "Nobody Knows Anything, Rate Expectations Edition" — SF Fed / Torsten Slok (Apollo) chart on dispersion in rate expectations | Direct rate-uncertainty regime signal, independent framing of the Fed-whipsaw story | Med-High | High |
| The Big Picture (Ritholtz, 9 remaining) | blog | AM Reads link-roundups + long-form culture pieces (Niederhoffer profile, Dolly Parton, David Booth/Dimensional transcript, $150T global-economy-by-2030 infographic) | — | — | Low-Med (aggregator, some links reference AI-capex-bubble debate) |
| FRED Blog (St. Louis Fed, 10 items) | blog | Educational/background pieces (consumer sentiment vs. financial well-being, rent-vs-own math, AI/coder employment, state minimum wages, Texas ratio, FDIC securities holdings) | — | — | Low |
| Motley Fool (50 items) | blog | Near-entirely Social Security 2027-COLA / RMD-age-73 / 401(k) / spousal-survivor-benefit personal-finance pieces (evergreen, recurring "2027 COLA" theme ahead of 9/11 SSA update) | — | — | Low (wealth-mgmt only — see TLDR) |
| Yahoo Finance — Market News (remaining ~18 items) | blog | Single-stock pieces (Bloom Energy S&P 500 inclusion ×6 duplicate items, Micron closes >$1,000, Sirius XM, V.F. Corp, Steel Dynamics, Atlassian +92%) | — | — | Low — single-name, outside ETF mandate |
| Seeking Alpha — Market Currents (7 items) | blog (title-only) | Dividend-declaration notices (4×) + misc headlines (Saudi $5.75B arms sale, record VLCC shipping rate) | — | — | Low — title-only |
| Investing.com — Stock Market News (10 items) | blog (title-only) | Single-company headlines (Foxconn, Starbucks/NLRB, Anthropic IPO timing shift, OpenAI agent breach, Boring Co. $20B valuation) | — | — | Low — title-only |
| IG France — "MarketLive" (9 items) | youtube (title-only) | Near-daily French technical-analysis livestream, generic recurring title, no transcript cached | Unknown content | Low confidence | Low |
| Finary (15 items) | youtube (title-only, FR) | French personal-finance/FIRE content, evergreen | — | — | Low |
| Investing Simplified / Prof G (15 items) | youtube (title-only) | Generic market-timing clickbait ("MAJOR Market Update," "the next big market crash," "stocks should SOAR") | Low-confidence sentiment only, no transcript | Low | Low |
| Oseille TV (12 items) | youtube (title-only, FR) | Expat/tax-residency/privacy content, not market-relevant | — | — | Low |
