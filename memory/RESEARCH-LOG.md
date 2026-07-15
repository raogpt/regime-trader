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

## 2026-07-15 — Market Intel (regime_trader)
Source: 20-feed RSS monitor (7 YouTube, 13 blog/news; lookback since 2026-07-13 last check). 195 new items. 5 sources had no new content (Finary, Investing Simplified/Prof G, George Gammon, Real Vision Presents, Liberty Street Economics). 5 YouTube videos posted (Oseille TV, Bravos Research, IG France x3) — all title-only, queued for off-cloud transcript fetch.

| Source | Type | Item | Regime Signal | Vol Bias | Relevance |
|--------|------|------|----------------|----------|-----------|
| CNBC — Economy | blog | June CPI +3.5% y/y, below 3.8% expected | Cooling inflation, disinflationary surprise | LOW (per se) | High |
| Yahoo Finance | blog | "Wall Street ends higher on cool inflation data, solid bank earnings" | Risk-on reaction to CPI + earnings | LOW | High |
| Investing.com — Market Overview (title-only x3) | blog | "Softer US CPI Supports Risk Appetite Despite Geopolitical Tensions" / "A Softer June CPI Report Reignites Rate-Cut Hopes" / "Soft US Inflation Cools Fed Hike Bets, but Middle East Tensions Keep Oil Bid" | Dovish CPI repricing, explicitly contrasted against Mideast risk | MIXED | High (title-only) |
| CNBC — Finance | blog | "A July rate hike from the Fed? The odds are rising" — driven by oil spike, not CPI | Hawkish repricing via energy shock, contradicts CPI-driven dovish read | HIGH | High |
| WSJ Markets | blog | "Oil Surges Most Since 2020, Reflecting Bet Strait Won't Go Back to Normal"; "U.S. Reimposed Naval Blockade on Iran"; "Oil Jumps as Trump Vows to Renew Iran Blockade" | Fresh Hormuz/Iran escalation reigniting oil-driven inflation risk | HIGH | High |
| ETF Trends (VettaFi) | blog | "Revival of Oil Turbulence Puts These Energy ETFs in Focus" — notes "relative calm" in oil may be over post last week's Mideast events | Independent confirmation of oil-vol catalyst | HIGH | Med-High |
| CNBC — Finance | blog | Fed Chair Kevin Warsh testifies to House Financial Services Cmte; pledges Fed policy "regime change" to fight inflation "tax" | Hawkish Fed leadership messaging despite soft CPI | MED-HIGH | High |
| CNBC — Finance | blog | Waller: Fed "shouldn't fight the last war" on inflation, hikes still possible | Hawkish governor commentary | MED-HIGH | High |
| CNBC — Finance | blog | "Big banks poised to report booming revenue propelled by SpaceX IPO, Iran war volatility" | Banks monetizing elevated vol — confirms vol regime is live, not theoretical | Context | Med |
| CNBC — Finance | blog | "The AI boom just found two new winners: Goldman Sachs and JPMorgan Chase" (record trading/IB revenue) | Confirms bank-earnings strength | LOW | Med |
| CNBC — Economy | blog | China Q2 growth slowest since 2022, fanning stimulus calls | Global growth risk-off counterweight | MED | Med-High |
| CNBC — Economy | blog | India inflation accelerates to 4.38% in June (Iran war + rainfall) | Independent, non-US inflation spillover from conflict | MED | Med |
| ETF Trends (VettaFi) | blog | "Small-Caps Extending Bullish Ways? Play It Safe With OUSM" — best first-half since 1991 | Direct IWM rotation/strength signal | context | High (IWM-specific) |
| ETF Trends (VettaFi) | blog | "Small-Caps Offer Rare Value as Sector Gaps Narrow" — Morningstar favors equal-weighting (same-channel, corroborates above) | Confirms small-cap thesis | context | High (IWM-specific) |
| ETF Trends (VettaFi) | blog | "Strong Markets, Growing Complexity" — Q2 2026 recap: S&P best April since Nov 2020, fresh record highs, "volatility re-emerged in June" | Direct regime narrative, SPY/QQQ | context | High |
| ETF Trends (VettaFi) | blog | "Time to Upgrade Financials? The Bull Case for Banks" — Iran war weakened growth expectations via inflation + oil vol | Sector-rotation signal tied to same Iran/oil theme | MED | Med-High |
| ETF Trends (VettaFi) | blog | "Q2 Earnings Preview: Tech & Energy Drive Growth Amid Healthcare Headwinds" — 23.3% S&P EPS growth expected | Earnings-season catalyst kicking off | context | High (catalyst filter) |
| Investing.com — Market Overview (title-only) | blog | "Gold Long Sentiment Falls out of Extreme Buy as Traders Note the Bear Channel" | Gold sentiment cooling despite war/oil — atypical, same pattern as 7/13 report | context | Med |
| Federal Reserve (official) | blog | Minutes of Board's discount rate meetings, June 8 & 17, 2026 | Official record, title-only | Low | Med |
| FRED Blog (St. Louis Fed) | blog | Real GDP by state, Q1 2026: 47/50 states grew, national avg 2.1% annualized | Background growth context | Low | Low-Med |
| The Big Picture (Ritholtz) | blog | Monday/Tuesday AM Reads + McKeel Hagerty (Hagerty Insurance) transcript | Link-aggregation, no distinct new macro thesis this batch | Low | Low |
| IG France (Alexandre Baradez) | youtube (title-only x3) | "MarketLive" general; "Tensions USA-Iran: impact Pétrole/Taux/Actions"; "BCE et Fed: les marchés anticipent le pire" (Short) | Titles align with oil/Iran/Fed themes above but content unverified | Low confidence | High — queued for transcript |
| Bravos Research | youtube (title-only) | "Nobody is Prepared for What's About to Happen…" | Urgent title, macro/trade-ideas channel, content unknown | Low confidence | Med — queued for transcript |
| Oseille TV | youtube (title-only) | "Ces pays d'Afrique vendent leur passeport (et c'est 100% légal)" | Africa/wealth-mgmt-adjacent (passports, not UEMOA specifically), content unknown | Low confidence | High (wealth-mgmt priority) — queued for transcript |
| Motley Fool (50 items) | blog | Single-stock deep-dives (Nvidia, SpaceX, IBM, Tesla, etc.) + retirement/SS explainers | — | — | Low — outside ETF-only mandate |
| ETF Trends (VettaFi) (~19 remaining) | blog | Niche fund launches/product pieces (CLOs, nuclear, space, MLPs, REITs) | — | — | Low-Med — product-level |
| WSJ Markets (~38 remaining) | blog | Deals/opinion columns/company-specific (IBM warning, PayPal/Stripe bid, media deals) | — | — | Low |
| Investing.com — Stock Market News (10 items, title-only) | blog | Single-company headlines (SK Hynix, BMW, PayPal/Stripe, Oracle) | — | — | Low — title-only |
| Seeking Alpha — Market Currents (7 items, title-only) | blog | Single-company/movers headlines (PYPL, Nokia, DeepSeek, Pentair) | — | — | Low — title-only |
| Yahoo Finance (~19 remaining) | blog | Single-stock/personal-finance pieces (Coca-Cola, Rocket Lab, dividend picks) | — | — | Low |
