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

## 2026-08-01 — Market Intel (regime_trader)
Full report: reports/2026-08-01-market-intel.md · 19-day catch-up run (last checked 2026-07-13) · 268 new items across 17 sources (3 sources had no new items) · 34/34 YouTube items title-only, queued for off-cloud transcript fetch.

| Source | Type | Item | Regime Signal | Vol Bias | Relevance |
|--------|------|------|----------------|----------|-----------|
| ETF Trends (VettaFi) | blog | FOMC holds 3.50-3.75% on 9-3 split vote; Warsh removes forward guidance ("not a communications change, it's a policy tool") | New Fed chair adds policy uncertainty, not resolution | HIGH | High |
| WSJ Markets | blog | "Kevin Warsh's Honeymoon With the Bond Market Is Already Over" — investors want inflation-fight commitment after Wednesday's selloff | Credibility/communication shock, hawkish repricing | HIGH | High |
| Motley Fool | blog | Warsh presser called "confusing," "contradictory"; 30-year yields up to 5.2% | Fed communication risk as independent vol input | HIGH | High |
| The Big Picture (Ritholtz) | blog | Borrowing costs hit 19-year high, biggest one-day jump since "liberation day" tariffs (citing FT) | Confirms Fed-driven bond stress independently | HIGH | High |
| ETF Trends (VettaFi) | blog | Treasury Yields Snapshot 7/31: 10y 4.75%, 2y 4.28% (up from 10y 4.56%/2y 4.21% on 7/10) | Rate-level confirmation of yield spike | HIGH | High |
| ETF Trends (VettaFi) | blog | Two Measures of Inflation: core PCE 3.3%, still above 2% target | Inflation not cooling | HIGH | High |
| WSJ Markets | blog | U.S. "hit back at Iran" for attack on bases in Jordan; oil gives back some gains after retaliation | Two-sided escalation, active conflict not one-off | HIGH | High — direct SPY/QQQ/IWM driver |
| WSJ Markets | blog | "Oil Posts Big Monthly Gains on Resumption of Conflict" — renewed Iranian attacks on Hormuz shipping | Sustained oil/energy pressure | HIGH | High |
| WSJ Markets | blog | Yen jumps to 2-month high on suspected BOJ intervention; Treasury warns banks it might intervene in dollar-yen (×4 related items) | New FX volatility channel opening | HIGH | High |
| WSJ Markets | blog | "Iran War Pushes Companies to Raise Prices on Beer, Paint, Fries and More" (Sherwin-Williams, Samuel Adams brewer) | War-driven inflation visible in consumer staples | HIGH | High |
| Yahoo Finance — Market News (S&P 500) | blog | El Niño compounding Iran-war Panama Canal disruption; capacity-reduction odds raised to 81% from 25% | Second, independent supply-chain/inflation vector | Supports HIGH | Med-High |
| The Big Picture (Ritholtz) | blog | New Section 301 tariffs (10-12.5%) on multiple trading partners take effect as Section 122 10% tariff expires | Second, tariff-driven inflation input alongside war | HIGH | Med-High |
| Motley Fool | blog | Nasdaq within 0.3pp of correction, down 9.7% from early-June highs; Fed held rates but future hikes could "add fuel to the fire" | Tech-specific volatility elevated | HIGH (QQQ-specific) | High |
| Yahoo Finance — Market News (S&P 500) | blog | Amazon +15%+ on Q2 blowout, Microsoft strong — eased AI jitters; Apple fell >7% on AI-driven component shortages | Narrow, mega-cap-concentrated relief rally, not broad | Mixed | High — direct rotation/breadth signal |
| The Big Picture (Ritholtz) | blog | "Nearly half of small-cap and midcap stocks are losing money" (citing MarketWatch) | IWM-specific fragility beneath index-level calm | Vol risk | High — direct IWM signal |
| The Big Picture (Ritholtz) | blog | "Stocks Finally Have Some Competition" — return of real yields changes asset-allocation math (citing TrendLabs) | Rate-regime shift with equity-risk-premium implications | Context | High |
| Motley Fool | blog | "If a Recession Is Coming, Here's How I'm Preparing My Portfolio" — unemployment/GDP/earnings still good, but inflation 3.5%, oil pressure, likely Fed hike flagged as headwinds | Recession "not imminent" but not dismissible | Mixed | Med-High |
| ETF Trends (VettaFi) | blog | "A Broad Approach in a Narrow Market" — Q2 rallied repeatedly on on-again/off-again Iran ceasefire headlines | Confirms conflict as the swing factor for market direction | HIGH | High |
| ETF Trends (VettaFi) | blog | QQQJ (mid-cap "next-gen" growth) and SPMO (momentum factor) pitched as investors look past mega-cap concentration | Rotation-adjacent positioning signal | Rotation signal | Med — product pitch, not flow data |
| George Gammon | youtube (title-only) | "It's Official, The AI Bubble Just Popped"; "$10 Trillion Derivatives Timebomb"; economic-warning sign | Bearish tail-risk signal, unverified | Vol risk | Med — title-only, consistent w/ correction/bond-stress items |
| Investing.com — Market Overview (5 titles) | blog (title-only) | "5 Signs Chairman Warsh's Honeymoon at the Fed Is Over"; "Long Bonds Are Weary of Warsh's Inflation Resolve"; "How Much Did AI Spending Contribute to Q2 GDP?" | Directly echoes Fed/inflation/GDP themes above | HIGH | Med-High — headline-only but strong corroboration |
| WSJ Markets | blog | "Buyer Beware: Private Funds Come With Big Tax Bills" | Wealth-mgmt, tax risk | Context | High — wealth-mgmt relevant |
| WSJ Markets | blog | "5 of the Top Financial Advisor Companies for Retirees" — fiduciary RIA rankings | Wealth-mgmt reference | Low | Med |
| Motley Fool | blog | Social Security COLA under-tracks inflation — retiree purchasing power down ~13.7% since 2010 | Wealth-mgmt, structural | Low | Med |
| Investing Simplified (Prof G) (3 titles) | youtube (title-only) | "SCHD vs. JEPI" dividend-income comparison; "Sequence of Returns Risk" retirement withdrawal piece | Wealth-mgmt, retirement-income theme | n/a | Low-Med — title-only |
| Oseille TV | youtube (title-only) | "Ces pays d'Afrique vendent leur passeport (et c'est 100% légal)" — African countries selling passports/residency | **UEMOA/Africa-adjacent — PRIORITY**, title-only | n/a | Med — flagged for transcript follow-up |
| Finary (2 titles) | youtube (title-only) | Currency/monetary-system explainer; crypto-transfer help guide | Wealth-mgmt adjacent | n/a | Low — title-only |
| Motley Fool (~40 remaining items) | blog | Single-stock deep dives (Micron, Meta, Alphabet, Marvell, PayPal, Apple, Reddit, Roblox, Nvidia, Caterpillar, etc.) | — | — | Low — outside ETF-only mandate |
| ETF Trends (VettaFi) (~35 remaining items) | blog | Niche ETF launches, Bitcoin ETF products, CLO/muni-bond explainers | — | — | Low-Med — product-level, not macro |
| WSJ Markets (~45 remaining items) | blog | M&A/deals, opinion columns, single-company stories | — | — | Low |
| Investing.com — Stock Market News (10) / Seeking Alpha — Market Currents (7) | blog (title-only) | Single-company headlines and dividend declarations | — | — | Low — title-only |
| Federal Reserve — Press Releases (6 remaining) / Liberty Street Economics (4) / FRED Blog (5 remaining) | blog | Administrative releases; stablecoin/bank-holding-company research; historical/methodological data explainers | — | — | Low — not directly regime-relevant this batch |
