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

## 2026-09-19 — Market Intel (regime_trader)
Gap since last check: 2026-07-13 → 2026-09-19 (~9 weeks; watchlist untouched over the summer). 297 new items across 17 sources (ETF Trends, CNBC Economy, CNBC Finance had none). Headline event of the period: **Fed hiked rates Sept 16–17, first hike since 2023**, against sustained oil >$100 (Iran war / Saudi pipeline attacks) and a BoJ hike the same week.

| Source | Type | Item | Regime Signal | Vol Bias | Relevance |
|--------|------|------|----------------|----------|-----------|
| Federal Reserve — Press Releases | blog | FOMC statement + economic projections released (Sept 15-16 meeting) | First rate hike since 2023, confirmed hawkish pivot | HIGH | High |
| WSJ Markets | blog | "Gold, Silver Post Weekly Gains Despite Fed Rate Increase" | Confirms Fed hike; safe-havens still bid | HIGH | High |
| WSJ Markets | blog | "2-Year Yield Hits Highest Level Since 2024" (4.741%) | Front-end yields pricing more hikes | HIGH | High |
| Seeking Alpha — Market Currents | blog (title-only) | "S&P 500 ends volatile week as Fed hikes rates, yields jump, oil surges" | Single-headline cross-confirmation of hike+oil+yields | HIGH | High |
| The Big Picture (Ritholtz) | blog | Claudia Sahm (via reads): FOMC "highly likely to hike a quarter point Wednesday" — called ahead of the event | Hike was well-telegraphed by week's start | HIGH | High |
| IG France (Alexandre Baradez) | youtube (title-only) | "Fed demain: de 40% à 91% de probabilité de hausse en quelques semaines" | Hawkish repricing shock in weeks before decision | HIGH | High |
| WSJ Markets | blog | "Stocks Rally, Shaking Off Fed's Rate Hike"; "S&P 500 and Nasdaq Post Biggest Gains in Six Weeks" (AI-led, 9/17) | Relief rally post-hike, tech/QQQ led | HIGH (whipsaw) | High — rotation signal |
| WSJ Markets / Yahoo Finance | blog | "Wall Street Ends Volatile Week with Quiet Finish", Dow fell 3rd straight week; Yahoo: "Dow Drops To Record Worst Week In Six Months Amid Elevated Yields, Oil" | Broad-market/value (IWM-adjacent) underperforming vs. AI/tech bounce | HIGH | High — SPY/QQQ vs Dow divergence |
| WSJ Markets | blog | "Saudi Arabia Has Another Option to Get Its Oil Out"; "Oil Futures End Week Little Changed" after "four-month highs on disruptions to Saudi Arabia's East-West pipeline" | Iran war/oil-supply shock persists into Sept | HIGH | High |
| IG France (Alexandre Baradez) | youtube (title-only) | "Pourquoi le pétrole à 94$ fait exploser les taux souverains partout dans le monde"; "Pétrole à 100$... pourquoi les taux ne peuvent pas baisser" | Oil shock → global sovereign yields, independent FR-language confirmation | HIGH | High |
| Motley Fool | blog | "2 Stocks to Buy if You Think $100 Oil Will Last" (Brent/WTI >$100, Iran war) | Corroborates oil-shock thesis (single-stock framing, ETF-mandate excludes picks) | HIGH | Med |
| The Big Picture (Ritholtz) | blog | "10 Friday AM Reads" — Ben Carlson: mortgages 6%→7%, 10y 4%→5%, inflation 2.4%→3.4%, oil <$60→>$100 this year | Independent recap of the full macro deterioration arc | HIGH | High |
| WSJ Markets | blog | "Dollar Rally Eases..."; "Fed Policy Outlook Weighs on Yen Ahead of BoJ Decision"; Buffett item notes "Bank of Japan's rate hike sends yen sinking" | BoJ hike same week as Fed hike; USD/JPY volatile, no clean directional read yet | HIGH | Med-High |
| Liberty Street Economics (NY Fed) | blog | "Are Central Banks Moving Out of Dollar Assets?" — USD share of global FX reserves 64% (2015) → 56% (2025) | Structural de-dollarization trend (long-horizon, not a trade trigger) | Context | Med — regime background |
| WSJ Markets | blog | "Daily Briefing: Higher Rates Deepen Private Equity's Zombie-Fund Problem"; "Rising Rates Will Make Private Equity's Bad Year a Lot Worse" | Credit-market stress emerging from the hike | MID-HIGH | Med |
| Bravos Research (5+ videos) | youtube (title-only) | "The Bubble's Final Phase Has Begun", "A Once in a Lifetime Financial/Economic Reset", "China Just Triggered A New World Order/Global Monetary Reset" (x2), "First Domino of the Global Debt Crisis" | Sensationalist-channel bear cluster; directionally consistent w/ hawkish-Fed regime but low individual confidence | HIGH (sentiment) | Med — title-only, known clickbait bias |
| George Gammon (5+ videos) | youtube (title-only) | "Money Supply Is EXPLODING...hyperinflation?", "The Entire House of Cards Is About To Fall (US Treasury Is Terrified)", "Nvidia Might Not Survive This", "This Is When The Dollar Will Lose Reserve Currency Status" | Bearish macro/AI-bubble cluster, echoes dollar/debt themes above | HIGH (sentiment) | Med — title-only |
| WSJ Markets / Motley Fool | blog | "Meta's AI Agent Has a Trust Problem"; "Sam Altman Admits the AI Industry Has Done 'a Terrible Job'... Amid Growing Backlash"; "U.S. AI-Related Stocks Extend Rally Premarket" same week | AI-narrative cracks alongside continued rallies — QQQ-specific whipsaw source | HIGH (QQQ) | High |
| Liberty Street Economics (NY Fed) | blog | "How Distressed Are Consumers? Reconciling Diverging Credit Card Delinquency Measures" — total debt balances dipped $13B in Q2 2026 | Consumer credit stress mixed, not yet acute | Context | Med |
| FRED Blog (St. Louis Fed) | blog | "Using options prices to measure financial risk: The KC Fed Policy Rate Skew" | Official options-implied rate-risk gauge — useful methodology, not a live reading here | Context | Med — HMM-adjacent tooling |
| Federal Reserve — Press Releases (~18 remaining) | blog | Bank enforcement actions, charter/M&A approvals (SNB Bancshares, Regions Bank employee actions, Santander, etc.) | Routine supervisory items, no regime signal | — | Low |
| FRED Blog (6 remaining) | blog | M2 explainer, consumer sentiment, rent-vs-own, AI/labor pieces, Texas ratio explainer | Background/methodology, no fresh regime signal | — | Low-Med |
| Liberty Street Economics (10 remaining) | blog | Jackson Hole recap, AI/labor research (2 posts), equity term structure, STRIPs trading, renter mobility, bank-holding-co structure series (3 parts), stablecoin update | Research-depth macro background, no immediate trigger | — | Low-Med |
| The Big Picture (9 remaining) | blog | Daily AM-reads roundups, RIA/advisor content, podcast transcripts | Wealth-mgmt/aggregator content, folded into TLDR below | — | Low — see Wealth Mgmt |
| Investing Simplified (Prof G) (15 items) | youtube (title-only) | Mix of single-stock buy calls (MU, "10 Growth Stocks"), retirement/tax-bucket content, "24-Month Stock Market Prediction" | Stock picks excluded (ETF-only mandate); tax/retirement pieces folded into Wealth Mgmt | — | Low-Med |
| Finary (14 items, FR) | youtube (title-only) | Savings-rate, tax, FIRE, OpenAI-spending-losses content | Evergreen wealth-mgmt/FR retail-investor education | — | Low — see Wealth Mgmt |
| Oseille TV (14 items, FR) | youtube (title-only) | Expat tax-residency content (Italy, Panama/Paraguay, African passport programs), EU privacy-law commentary | Expat/tax-optimization, not UEMOA-specific investment signal this cycle | — | Low — see Wealth Mgmt |
| IG France MarketLive (9 recurring episodes) | youtube (title-only) | Near-daily technical/market-wrap show, no extractable thesis beyond titles | — | — | Low — title-only, folded above |
| Motley Fool (~46 remaining) | blog | Single-stock/crypto picks (NVDA, TSLA, SPCX, XRP/ETH/BTC, dividend lists) | — | — | Low — outside ETF-only mandate |
| Yahoo Finance — Market News (~15 remaining) | blog | Single-stock mover recaps (PAGS, IIPR, ZTS, NLY, DBX, etc.) | — | — | Low — outside ETF-only mandate |
| WSJ Markets (~30 remaining) | blog | Opinion columns, M&A/deals, company-specific stories, market-talk roundups | — | — | Low |
| Investing.com — Market Overview + Stock Market News (20 items) | blog (title-only) | Headline-only, per known feed limitation | — | — | Low — title-only |
| Real Vision Presents (1 item) | youtube (title-only) | "Phase One Drilling Results Explained \| Midnight Sun Mining" | Single-name mining, off-mandate | — | Low |
