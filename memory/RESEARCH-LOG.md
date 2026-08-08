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

## 2026-08-08 — Market Intel (regime_trader)
| Source | Type | Item | Regime Signal | Vol Bias | Relevance |
|--------|------|------|----------------|----------|-----------|
| WSJ Markets + Investing.com + Yahoo Finance + Motley Fool (cross-source, 8+ headlines) | blog | July NFP shock: economy lost 23k jobs (vs. gain expected); S&P/Dow to fresh record highs; rate-hike odds collapse; dollar to 7-wk low | Dovish Fed repricing, "bad news is good news" risk-on breakout | LOW near-term, but crowded/one-sided | High — direct SPY/QQQ driver |
| Investing.com — Market Overview | blog (title-only) | "Forget Goldilocks: It's the Old-Fashioned 'Bad News Is Good News' Trade"; "Is the Stock Market Rally Running Out of Steam?"; "The Recovery Trap No One Sees Coming" | Consensus rally + contrarian caution flags | LOW near-term / caution | High |
| WSJ Markets | blog | Comex Gold +7.2% wk to $4340.70, silver +3.1%; Investing.com: "Gold Strength Tests Final Barrier Before a Larger Advance" | Safe-haven bid alongside equity rally — cross-asset divergence | Watch — precedes vol pickup historically | Med-High |
| WSJ Markets | blog | Oil: WTI $78.18 (-7.7% wk), Brent $83.55 (-5% wk); nat gas 7th straight weekly loss; UN FAO cites "near-total closure of Strait of Hormuz" lifting food prices | Energy vol elevated, Hormuz disruption still live | HIGH (energy) | Med-High |
| Seeking Alpha — Market Currents | blog (title-only) | "Oil futures end down week...as Strait of Hormuz deal turns more uncertain" | Geopolitical oil-supply risk unresolved | HIGH | Med |
| WSJ Markets (2 articles) + IG France (video, title-only) | blog+youtube | US-Japan joint yen intervention (first in a generation, yen at 40-yr low); "Only BoJ Can Arrest Yen's Decline"; "Bessent's Yen Trade Has Unintended Consequences" | FX intervention = tail-risk catalyst; Fed easing pressure via yen carry unwind | HIGH | Med-High |
| IG France (Alexandre Baradez) | youtube (title-only) | "L'indice VIX au contact d'un niveau technique important" (8/7) | Technician flags VIX at key level, no detail | Possible vol regime shift signal | Med (low confidence) |
| IG France (Alexandre Baradez) | youtube (title-only) | "Effet de levier excessif : l'avertissement du PDG de JPMorgan" (8/7) | Systemic leverage warning from JPM CEO | Risk-off undertone | Med (low confidence) |
| WSJ Markets | blog | "'Perps' Are the Risky New Derivatives That Could Amplify Stock Blowups"; Situational Awareness ($45B AI hedge fund) implodes on leverage, redemption queue forming | Leverage/derivatives fragility building in AI trade | Vol risk building | High |
| The Big Picture (Ritholtz) | blog | AM-reads detail Situational Awareness collapse further; separately flags Warsh Fed-chair "Sticking With It... Until January" commentary | Corroborates AI-leverage blowup theme (3rd source); Fed policy stance flagged | Vol risk / Neutral-hawkish-lean | Med-High |
| Yahoo Finance + Motley Fool (duplicate headline, 2 sources) | blog | "The AI Trade Rotation: Money Is Moving Out of Chips"; WSJ: memory-chip stocks drop on soft guidance | Sector rotation away from semis/AI leaders | QQQ-specific risk | High — QQQ overweight risk |
| George Gammon | youtube (title-only, 3 items) | "AI Bubble Just Popped" (7/16); "$10 Trillion Derivatives Timebomb" (7/23); "Economic Sign That Can't Be Ignored" (7/18) | Recurring bearish AI-bubble/leverage warnings | Bias: vol-up | Low confidence (title-only), but pattern corroborates other sources |
| Bravos Research | youtube (title-only, 2 items) | "A Once in a Lifetime Economic Reset Is Arriving" (8/4); "An Opportunity Like This Won't Come Again" (7/23) | Vague macro-reset/contrarian framing, no content | Unclear direction | Low confidence (title-only) |
| Investing Simplified (Prof G) | youtube (title-only, 13 items, Jul–Aug) | Recurring vol/crash/buy-the-dip titles: "Extreme Fear: Complete Market Failure," "BREAKING...CHAOS," "Best Buying Opportunity of 2026" | Persistent retail fear + dip-buy narrative across a month | Sentiment proxy — elevated perceived vol | Low confidence (title-only) but notable recurring pattern |
| Yahoo Finance | blog | Buffett/Berkshire sitting on $397.4B cash; net seller of stocks 3+ years | Top allocator signaling valuation caution despite record highs | Bias: caution | Med |
| Federal Reserve (official) | blog | FOMC statement issued 7/29; discount-rate meeting minutes (6/8, 6/17) released 7/14 | Routine policy comms, no hike signaled | Neutral-to-dovish given jobs miss | Med |
| Liberty Street Economics (NY Fed) | blog | "A Window into Bond Investors' Uncertainty About R-Star" | Rate-path uncertainty research | Context for Fed-path forecasting | Med |
| Liberty Street Economics (NY Fed) | blog | "Stablecoins and (Non)Crypto Shocks: A 2026 Update" | Stablecoin growth & shock-transmission channel | Low-Med — crypto/vol linkage context | Low-Med |
| WSJ Markets | blog | "New Intelligence Warns Russia May Provoke NATO Amid Dwindling U.S. Munitions" | Geopolitical tail-risk | Vol risk (low-prob, high-impact) | Med |
| WSJ Markets (3 opinion pieces) | blog | Crypto "Clarity Act" Senate debate (pro/con) ongoing | Regulatory overhang, indirect equity linkage | Low-Med | Low |
| Investing.com — Stock Market News | blog (title-only) | Typhoon Dolphin hits Okinawa, China shuts ports ahead of landfall | Regional supply-chain/weather catalyst | Low-Med | Low-Med |
| Federal Reserve Press Releases (7 remaining items) | blog | Bank-specific approvals/enforcement actions (Coastal Bend, FS Bancorp, Santander, Iuka Bancshares, etc.) | — | — | Low — bank-supervisory noise, skipped |
| Liberty Street Economics (5 remaining items) | blog | Renter mobility, AI-labor market post, 3-part nonbank-subsidiary/Basel III series | — | — | Low-Med — structural/academic, skipped detail |
| FRED Blog (7 items) | blog | Bank balance-sheet mix, construction-employment seasonality, oldest FRED series, 1996 productivity debate, oil-airfare link, unemployment-by-marriage, state GDP/mfg | — | — | Low — data trivia, skipped |
| WSJ Markets (~50 remaining items) | blog | Single-company/M&A/opinion pieces (AstraZeneca, SpaceX, HSBC, Wells Fargo tokenized deposits, Monte dei Paschi/Intesa, JPMorgan whistleblower, sector "Market Talk" roundups) | — | — | Low — broad earnings season underway; outside ETF-only mandate, skipped |
| Yahoo Finance (~12 remaining items) | blog | Single-stock earnings/price moves (PagSeguro, StoneCo, Li Auto, Cisco, Accenture, American Eagle, DraftKings, SpaceX) | — | — | Low — earnings-season noise, skipped |
| Motley Fool (5 remaining items) | blog | Retirement/SS personal-finance pieces + single-name deep dives (SpaceX/Musk, Alphabet, Airbnb, JPMorgan shipbuilding initiative) | — | — | Low — see Wealth Mgmt TLDR |
| Investing.com — Stock Market News (7 remaining items) | blog (title-only) | Single-company/political headlines (AG confirmation, Klesch/BP, Verisk/AccuLynx, BHP strike, minerals investment, Nvidia-Lancium, SEC case) | — | — | Low — title-only, skipped |
| Seeking Alpha — Market Currents (6 remaining items) | blog (title-only) | Single-company headlines (AIXC, Vaxart, Nutex, Gladstone Investment, Bimini, I3 Verticals) | — | — | Low — title-only, skipped |
| Oseille TV (8 items) | youtube (title-only) | Offshore tax/residency, EU surveillance/privacy, passport-sales content | — | — | Low — not market-relevant, skipped |
| Finary (9 items) | youtube (title-only) | General FR wealth-mgmt content (market-timing skepticism, over-saving cost, FIRE, crypto-transfer guide, currency comparison) | — | — | Low-Med — see Wealth Mgmt TLDR |
| IG France MarketLive daily livestreams (7 items) | youtube (title-only) | Generic daily technical-analysis stream titles, no specific content | — | — | Low — title-only, no signal, skipped |
