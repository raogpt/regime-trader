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

## 2026-07-19 — Market Intel (regime_trader)
| Source | Type | Item | Regime Signal | Vol Bias | Relevance |
|--------|------|------|----------------|----------|-----------|
| Yahoo Finance | blog | Iran attack kills two U.S. troops; Google/Tesla/Intel/GE Vernova earnings ahead | Casualty-level escalation of Iran conflict | HIGH | High — direct SPY/QQQ/IWM driver |
| Seeking Alpha — Market Currents | blog (title-only) | Iran suspends ceasefire commitments with U.S. after escalating strikes | Corroborates ceasefire collapse, 1 day ahead of casualty report | HIGH | Med-High — title only |
| WSJ Markets | blog | Oil futures rise on Middle East escalation; U.S. widened strikes, Iran hit Gulf neighbors, double-digit weekly gain | Sustained energy/geopolitical pressure | HIGH | High |
| WSJ Markets | blog | U.S. Emergency Oil Reserve hits lowest level since 1983 (Iran War context) | Reduced strategic buffer, higher ceiling on future oil shocks | HIGH | High |
| CNBC — Economy | blog | Renewed Hormuz hostilities drive ECB rate rethink amid "extremely volatile" outlook | Non-US central bank policy hostage to conflict | HIGH | High |
| CNBC — Economy | blog | Wholesale prices fell 0.3% partly due to a "brief pause" in US-Iran tensions — pause now over per items above | Confirms pause-then-escalation pattern | HIGH | High |
| ETF Trends (VettaFi) | blog | Multiple pieces: "ongoing conflict over the Strait of Hormuz" still pressuring global markets | Sustained geopolitical drag | HIGH | High |
| IG France (Alexandre Baradez) | youtube (title-only) | "Tensions USA-Iran: impact Pétrole/Taux/Actions"; "BCE et Fed: les marchés anticipent le pire" | Directionally consistent w/ escalation | HIGH | Med — title only |
| CNBC — Finance | blog | Kevin Warsh confirmed Fed chair; pledges "regime change" to fight inflation; declines to submit dot plot | Hawkish new-chair rhetoric | HIGH | High |
| CNBC — Finance | blog | "WarshGPT" — Wall Street using AI to fill gap from reduced Fed communication | Reduced forward guidance = interpretive uncertainty | Vol risk | High |
| CNBC — Finance | blog | Dallas Fed's Logan calls for "modestly higher" rates | Hawkish regional voice | HIGH | Med-High |
| CNBC — Finance | blog | NY Fed's Williams: inflation "has peaked," rates "well positioned" | Dovish counter-voice | Mixed | High |
| CNBC — Finance | blog | Waller: don't "fight the last war" on inflation, but hikes still possible | Mixed/contested | Mixed | Med |
| CNBC — Economy | blog | June CPI +3.5% YoY, below 3.8% expected; core ~2.9% | Actual inflation cooling vs hawkish Fed tone | Dovish counter-signal | High |
| CNBC — Economy | blog | PPI unexpectedly fell 0.3% in June on gasoline drop | Confirms cooling wholesale inflation | Dovish counter-signal | High |
| ETF Trends (VettaFi) | blog | American Century's Greenblath: new Fed chair a "major change to bond landscape," curtailing forward projections | Confirms Warsh regime shift | HIGH | High |
| ETF Trends (VettaFi) | blog | S&P 500 Snapshot: 1.6% weekly loss, closed below 50-day MA, 2.0% off June 2 record, still +8.9% YTD | First technical break of the batch on SPY benchmark | HIGH | High — direct SPY signal |
| WSJ Markets | blog | Multi-day Nasdaq/chip selloff: "Nasdaq Drops Again," "Chip Stocks Extend Slide; Netflix Tumbles," "Moonshot AI Adds Fuel," "TSMC Record Overshadowed" | Sustained QQQ weakness across full trading week | HIGH (QQQ-specific) | High |
| ETF Trends (VettaFi) | blog | Small-cap rally: Russell 2000/S&P SmallCap 600 up ~20.8% YTD, outpacing S&P 500 (2 pieces) | Continued IWM-favorable rotation | Rotation signal | High — direct IWM signal |
| ETF Trends (VettaFi) | blog | Healthcare sector strength: State Street upgrades healthcare to positive; healthcare ETFs top performers | Rotation into defensive/healthcare | Rotation signal | High |
| WSJ Markets | blog | "Here's What Is Happening Behind the Market's Swings, in Charts" — chips falling, transports rising, indexes near records | Internal breadth rotation signal | Rotation | High |
| The Big Picture (Ritholtz) | blog | "Overvalued, Bubble, or Revolution?" — Q3 client-call charts on AI valuation | AI-bubble sentiment risk flag | Vol risk | Med-High |
| ETF Trends (VettaFi) | blog | "Priced for Perfection" — big 4 hyperscalers to spend $700B+ in 2026, ~80% higher than 2025 | Quantified AI-capex/credit-stress datapoint | Vol risk | High |
| George Gammon | youtube (title-only) | "It's Official, The AI Bubble Just Popped" | Directionally consistent, unverified | Vol risk | Low — title only |
| ETF Trends (VettaFi) | blog | GSEW equal-weight piece: "Were AI to actually pop like a bubble, portfolios would suffer" | AI-bubble risk framing | Vol risk | Med-High |
| Yahoo Finance + Motley Fool (syndicated) | blog | TSMC/ASML earnings show soaring demand, yet AI stocks fell anyway | Fundamentals-vs-price divergence | Vol risk | Med |
| CNBC — Finance (2 items) | blog | Morgan Stanley record revenue (equities trading +69%); Goldman/JPMorgan "AI boom's two new winners" | Institutional risk appetite strong despite tech-sentiment sourness | Mixed | High |
| WSJ Markets (2 items) | blog | U.S. Bancorp record Q2 revenue; Fifth Third profit boosted by Comerica acquisition | Confirms bank-earnings strength | Mixed | Med-High |
| ETF Trends (VettaFi) | blog | Tesla reports Wed 7/22 after close | Forward catalyst 3 days out | Catalyst event | High — earnings/catalyst filter relevant |
| Yahoo Finance | blog | Google, Tesla, Intel, GE Vernova all report this week | Cross-source confirmation of dense earnings week | Catalyst event | High |
| WSJ Markets | blog | Netflix growth warning (7/16) triggered contagion into broader chip/tech selloff | Realized catalyst event, not just scheduled | HIGH (QQQ-specific) | High |
| ETF Trends (VettaFi) | blog | Treasury Yields Snapshot 7/17: 10y 4.55%, 2y 4.18% — flat vs. 7/13 reading | Rate-level/curve data point (normal curve) | Context | Med |
| WSJ Markets | blog | Comex Gold ends week 2.23% lower at $4012.70 despite live Iran escalation | Confirms gold trading as rate-hike-fear proxy, not safe haven | Context | Med |
| WSJ Markets | blog | "How Sky-High Deficits Threaten the Bond Market" — record Treasury issuance | Fiscal/duration risk context | Context | Med-High |
| The Big Picture (Ritholtz) | blog | "At The Money: When Should DIY Investors Fire Themselves?" | Wealth-mgmt strategic-allocation framing | Context | Med-High |
| The Big Picture (Ritholtz) | blog | MiB interview: Jason Wenk (Altruist CEO) on RIA custodial tech/AI | Industry-structure context | n/a | Med |
| Oseille TV | youtube (title-only) | "Ces pays d'Afrique vendent leur passeport (et c'est 100% légal)" | **PRIORITY-flagged, Africa-adjacent** (passport/citizenship programs, not UEMOA-specific) | n/a | Low confidence — title only, flagged for visibility |
| WSJ Markets (2 items) | blog | "10 of the Best Financial Advisor Companies"; "5 Top Financial Advisor Companies for Retirees" | Wealth-mgmt reference, evergreen | Low | Low |
| Motley Fool (50 items) | blog | Single-stock/AI-name deep dives (Nvidia, AMD, Coca-Cola, Netflix, SpaceX, Intel, Ethereum, Buffett/Berkshire moves, insider-sale trackers) plus retirement/Social Security explainers | — | — | Low — outside ETF-only mandate |
| ETF Trends (VettaFi) (~35 remaining items) | blog | Niche single-fund/product coverage (crypto ETPs, leveraged single-country funds, dividends, REITs, nuclear, commodities) | — | — | Low-Med — product-level, not macro |
| WSJ Markets (~45 remaining items) | blog | Deals/M&A, opinion columns, sector "Market Talk" roundups, single-company stories (IBM 25% plunge, SpaceX below IPO price) | — | — | Low |
| CNBC — Finance (~15 remaining items) | blog | Company-specific items (SpaceX short interest, Robinhood/PayPal insider sales, Anthropic IPO chatter, Buffett/Gates Foundation) | — | — | Low — outside ETF-only mandate |
| Yahoo Finance (~15 remaining items) | blog | Single-stock listicles (Coca-Cola, Conagra, Chubb, Nvidia, "Magnificent Seven" comparisons) | — | — | Low — outside ETF-only mandate |
| Investing.com — Market Overview (10 items) | blog (title-only) | Headlines echo AI-selloff/Iran-escalation themes but no body text | — | — | Med (directional) — title-only |
| Investing.com — Stock Market News (10 items) | blog (title-only) | Single-company/sector headlines (Samsung layoffs, BofA luxury rankings, Meta outages) | — | — | Low — title-only |
| Seeking Alpha — Market Currents (6 remaining items) | blog (title-only) | Single-company/sector wire items (refiner margins, Walmart recall, IBM hold rating) | — | — | Low — title-only |
| Federal Reserve (official, 3 items) | blog | Bank-examination guidance, enforcement action, discount-rate-meeting minutes | — | — | Low-Med — terse official releases |
| Liberty Street Economics (NY Fed, 3 items) | blog | Three-part series on Basel III / nonbank-subsidiary capital reallocation within BHCs | — | — | Low-Med — regulatory structure, not near-term rate signal |
| FRED Blog (2 items) | blog | State-level manufacturing employment; Q1 2026 real GDP by state | — | — | Low-Med — background only |
| Finary / Investing Simplified (Prof G) (6 items) | youtube (title-only) | Wealth-mgmt/crypto and "market opportunity" titles | — | — | Low — title-only, unverified |
