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

## 2026-07-22 — Market Intel (regime_trader)
| Source | Type | Item | Regime Signal | Vol Bias | Relevance |
|--------|------|------|----------------|----------|-----------|
| WSJ Markets | blog | "Stock Market Today: Oil Approaches $95 as War Squeezes Supply"; "Brent Climbs Past $94 a Barrel"; "Oil Futures Extend Rally on Continued U.S., Iran Strikes" (3rd straight up session) | Iran/Hormuz war reignited and escalating, not de-escalating since 7/13 | HIGH | High — direct SPY/QQQ/IWM driver |
| WSJ Markets | blog | "Gold Past $4,100 on Fresh Buying Interest..."; "Gold Prices Have Tanked. Buying the Dip Makes Sense."; "Precious Metals Mount Rally" | Gold now rallying as classic safe-haven — a reversal of the 7/13 pattern (gold had fallen then on hike fear) | HIGH | High |
| WSJ Markets | blog | "Iran War to Cost About $37.5 Billion, Hegseth Says"; Jordan named new flashpoint, troop deaths rising, naval blockade reimposed (per Motley Fool item citing oilprice.com) | Escalation confirmed multi-source; war is deepening, not resolving | HIGH | High |
| CNBC — Economy | blog | "Renewed Hormuz hostilities drive ECB rates rethink amid 'extremely volatile' outlook" | Policy-uncertainty spillover to ECB, not just the Fed | HIGH | High |
| CNBC — Economy | blog | CPI +3.5% YoY June, "less than expected" (vs 3.8% forecast); wholesale prices -0.3% on falling gasoline | Cooler-than-feared inflation prints — partial dovish counter-signal | Mixed (dovish tilt) | High |
| Yahoo Finance | blog | Cleveland Fed's Hammack: inflation "has become a broad-based problem" (FOMC voter) | Hawkish voting-member commentary | HIGH | High |
| CNBC — Finance (4 items) | blog | Dallas Fed's Logan calls for "modestly higher" rates; Waller warns hikes "still possible"; Warsh pledges Fed policy "regime change" on inflation; "A July rate hike from the Fed? The odds are rising" | Multiple Fed voices leaning hawkish | HIGH | High |
| CNBC — Finance | blog | NY Fed's Williams: "inflation has peaked, rates well positioned" | Dovish counter-voice — Fed direction remains contested, as in 7/13 | Mixed | High |
| Yahoo Finance | blog | "US Stock Market Today... Earnings And Inflation Crosscurrents" — cites ~50-60% odds of a September Fed hike, 10y near 4.6% | Quantified, if secondary, hike-odds data point | Contested/Mixed | High |
| WSJ Markets + ETF Trends + Yahoo Finance (multi-source) | blog | Semiconductor "bloodbath" (SOXX crossed into bear market per veteran strategist) then "best day in a month" rebound; "Chip Stocks Rebound, Lifting Indexes"; Supermicro margins surge; MU/SNDK/WDC rally | Sharp two-way whipsaw in QQQ-heavy names = elevated realized vol, not directional break | HIGH (QQQ-specific) | High |
| ETF Trends (VettaFi) | blog | "Cyber ETFs Surge While Semis Stumble" | Rotation within tech itself, not fully away from tech | Rotation | High |
| ETF Trends (VettaFi) | blog | "The Changing Mosaic of Risk Factors" — explicit regime-shift language: from hawkish-Fed + "bulletproof" AI cycle + ignoring Iran, to Fed-tightening respite + doubts on AI ROI | Directly regime-framing thesis, most HMM-relevant single piece in batch | Regime shift flagged | High |
| Yahoo Finance | blog | Stocktwits retail sentiment "extremely bearish" on SPY, "neutral" on QQQ (7/22) | SPY/QQQ sentiment divergence — opposite polarity vs 7/13 (SPY was bullish then) | Rotation/sentiment reversal | High — direct SPY/QQQ split |
| ETF Trends (VettaFi) | blog | "S&P 500 Snapshot": index dropped below 50-day MA, -1.6% week, 2.0% off record close, still +8.9% YTD (as of 7/17) | Technical damage confirms rising realized vol | HIGH | High |
| WSJ Markets (2 items, same story) | blog | "Everyday Investors Sour on the Mag Seven and Flock to Newer AI Trades" | Rotation within AI/tech (mega-cap to newer AI names), not away from QQQ per se | Rotation (intra-QQQ) | Med-High |
| ETF Trends (VettaFi) | blog | "Notes from the Desk: Priced for Perfection" — big-4 hyperscalers to spend $700B+ on AI capex in 2026, ~80% above 2025, debt-financed | AI-credit stress continuing, echoes 7/13's AI-bond concern | Vol risk | High |
| CNBC — Finance | blog | Jamie Dimon: "markets underestimate risks," wouldn't buy stocks or Treasurys at current prices | High-profile risk-off dissent against an otherwise risk-on tape | Cautionary | High |
| CNBC — Finance + WSJ (multi) | blog | Morgan Stanley record equities trading (+69%); Goldman/JPM "AI winners"; "Wall Street Traders Are Having Their Best Year Ever" | Trading-desk windfalls confirm elevated realized vol/volume, not just headline fear | HIGH | High |
| ETF Trends (VettaFi) | blog | "Weekly Economic Snapshot: Inflation Cools, But Energy Headwinds Loom" | Cooling core inflation vs. rising energy costs — mixed picture | Mixed | Med-High |
| CNBC — Economy | blog | China Q2 GDP slowest since 2022 (stimulus calls); import prices from China at highest since 2008 | Global growth slowdown + continuing tariff pass-through | Supports contested-Fed/sticky-inflation thesis | Med-High |
| CNBC — Finance | blog | "'WarshGPT': How Wall Street is adapting to the Fed's new era of communication" (less public Fed commentary) | Reduced Fed forward guidance = noisier policy signal for rate-based HMM features | Vol-of-uncertainty | Med-High |
| WSJ Markets | blog | "Tech Stocks Return to Rally Mode Ahead of Earnings" — Alphabet, Tesla, IBM report Wed 7/22 | Scheduled mega-cap earnings catalyst, 0-1 day out | Catalyst event (earnings/catalyst filter relevant) | High |
| WSJ Markets | blog | WSJ Dollar Index up 4 consecutive sessions to 97.34 | Mild dollar strength consistent with hawkish-Fed-odds repricing | Context | Med |
| ETF Trends (VettaFi) | blog | Treasury Yields Snapshot 7/17: 10y 4.55%, 2y 4.18% | Curve little-changed vs. 7/13 (still normal, moderately elevated) | Context | Med |
| Investing.com — Market Overview (3 of 10 items) | blog (title-only) | "Chips Lead Amid Middle East Tensions"; "Risk-On Rally Builds as Strong Earnings Drive a Sharp Tech Rebound"; "Markets Await Technology Earnings" | Directionally consistent with content-available sources above | HIGH (directional) | Med — headline-only |
| Seeking Alpha — Market Currents (2 of 7 items) | blog (title-only) | "Nasdaq futures come under pressure ahead of Tesla, Alphabet results"; "Tesla enters earnings with shorts piling in, technicals weakening" | Consistent with QQQ-specific vol theme above | HIGH (directional) | Med — title-only |
| The Big Picture (Ritholtz) (10 items) | blog | Daily AM/weekend link round-ups; references "Wall Street Traders... Best Year Ever" (risk-on) among curated links | Secondary aggregation; limited standalone signal beyond items captured above | — | Low-Med |
| Liberty Street Economics (NY Fed) (3 items) | blog | 3-part series on nonbank subsidiaries / Basel III capital arbitrage inside bank holding companies | Financial-stability/structural research; not directly tariff/inflation-relevant this cycle | Low-direct | Low-Med |
| Federal Reserve (official, 3 items) | blog | Bank-exam sensitive-info joint statement; enforcement action; discount-rate meeting minutes | Institutional/regulatory, terse | Neutral | Low-Med |
| FRED Blog (St. Louis Fed) (3 items) | blog | Unemployment by marriage status; manufacturing employment by state; Q1 2026 GDP by state | Background macro, not near-term actionable | Low | Low |
| WSJ Markets (~35 remaining items) | blog | Deals/M&A, opinion columns, single-company earnings (Santander, Fifth Third, Super Micro, SpaceX short interest) and personal-finance/tax pieces | — | — | Low — outside ETF-only mandate |
| ETF Trends (VettaFi) (~35 remaining items) | blog | Niche ETF launches/product pieces (nuclear, REITs, muni bonds, crypto research, single-country funds, leveraged/inverse rankings) | — | — | Low-Med — product-level, not macro |
| Motley Fool (50 items) | blog | Almost entirely retirement/Social Security/COLA/RMD/Roth personal-finance explainers (one Iran-war-linked COLA piece) | — | — | Low — outside ETF-only mandate |
| CNBC — Finance (~14 remaining items) | blog | Single-company/deal news (SpaceX short interest, Capital One/Discover, Coinbase, China car sales, India IPO, Anthropic IPO, Buffett/Gates commentary) | — | — | Low — single-name/noise |
| Yahoo Finance — Market News (~5 remaining items) | blog | Single-stock notes (Analog Devices, Waste Management, Phillips 66, Sigma Lithium, Zoetis) | — | — | Low — single-stock |
| Investing.com — Stock Market News (10 items) | blog (title-only) | Single-company headlines (SK Hynix, Sodexo, Tata Communications, Nike/Topsports, Supermicro, Indonesia stocks, Henry Boot, etc.) | — | — | Low — title-only |
| Seeking Alpha — Market Currents (5 remaining items) | blog (title-only) | Single-company/regional deal headlines (Saudi nuclear deal, Pepkor/Flash deal, government funding bill, Asian equities) | — | — | Low — title-only |
| IG France (Alexandre Baradez) (7 items) | youtube (title-only) | French technical-analysis "MarketLive" titles incl. explicit Iran/oil/rates framing ("Tensions USA-Iran: impact Pétrole/Taux/Actions", "BCE et Fed: les marchés anticipent le pire", "Inflation US: pourquoi les marchés ne réagissent pas") | Titles alone echo the Iran/Fed-hawkish narrative above | Low confidence (title-only) but directionally consistent | Med — title-only |
| Oseille TV (3 items, FR) | youtube (title-only) | "Ces pays d'Afrique vendent leur passeport (et c'est 100% légal)"; "L'Europe coule comme le Titanic..."; "Le jeu est truqué..." | WEALTH MGMT / Africa-adjacent flag per project priority — title-only, content unknown | Low confidence | Low-Med — flagged (Africa-adjacent, title-only) |
| Finary + Investing Simplified (Prof G) + George Gammon (13 items, FR+EN) | youtube (title-only) | Generic retirement/dividend/crypto titles (SCHD vs. JEPI, "AI Bubble Just Popped", "Votre bitcoin ne vaut rien", retirement-prep videos) | Title-only; one AI-bubble-themed title directionally consistent with AI-ROI-doubt theme above | Low confidence | Low |
