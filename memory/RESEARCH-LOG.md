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

## 2026-07-17 — Market Intel (regime_trader)
| Source | Type | Item | Regime Signal | Vol Bias | Relevance |
|--------|------|------|----------------|----------|-----------|
| WSJ Markets | blog | Oil headed for 10% weekly gain on escalating U.S.-Iran attacks | War shock intensifying, not resolving, a week in | HIGH | High |
| WSJ Markets | blog | Gold below $4,000 as U.S.-Iran conflict fuels rate-hike bets | Gold down on hike-fear, not up on safe-haven flight — same atypical pattern as 07-13 | HIGH | High |
| CNBC — Economy | blog | Renewed Hormuz hostilities drive ECB rates rethink amid "extremely volatile" outlook | War shock now shaping non-US central bank policy | HIGH | Med-High |
| Yahoo Finance | blog | Nasdaq/S&P 500 futures slide as chip stocks tumble, Iran tensions fuel risk-off; Stocktwits bullish QQQ / neutral SPY | Named SPY/QQQ sentiment divergence | HIGH | High — direct SPY/QQQ split |
| Yahoo Finance | blog | US Stock Market Today: S&P 500 futures dip on tariff and energy cost worries (new 25% Brazil tariff) | New tariff catalyst layering onto oil/Iran inflation input | HIGH | Med-High |
| CNBC — Finance | blog | "A July rate hike from the Fed? The odds are rising" — hike odds tied directly to Hormuz oil spike | War shock directly repricing Fed-hike odds | HIGH | High |
| WSJ Markets | blog | "Stock Market Today: Nasdaq Futures Drop as Chip Selloff Deepens" — AI buildout concerns | New dominant driver: AI/chip selloff, QQQ-specific | HIGH (QQQ-specific) | High |
| Yahoo Finance | blog | Asian shares sink, Tokyo down >5%, TSMC -7.3%; S&P futures -0.8%, Dow futures -0.5% | Sharpest single magnitude data point in batch; AI-selloff contagion to Asia | HIGH | High |
| WSJ Markets | blog | "Chip Stocks Fall as AI Trade Loses Steam" — Nasdaq -1.5% on fresh semiconductor selling | Confirms AI-trade unwind is real, not just headline noise | HIGH (QQQ-specific) | High |
| Investing.com — Market Overview | blog (title-only) | "The Macro Storm Is Fading but AI Is Becoming the Market's Main Fault Line"; "Asia Wrap: The AI Trade Is Discovering Gravity" | Names the driver-composition shift explicitly | HIGH | Med — headline-only |
| George Gammon | youtube (title-only) | "It's Official, The AI Bubble Just Popped (Here's Why)" | Thematically aligned with AI-selloff consensus but not independent corroboration | Directional only | Low — title-only |
| Yahoo Finance | blog | "Dow Jones Futures Fall, Netflix Dives, SpaceX Scrubs Launch After Latest AI Sell-Off" — regional banks/transports rose while AI names tumbled | Rotation within the selloff, not broad decline | Mixed | High |
| ETF Trends (VettaFi) | blog | "Priced for Perfection" — Meta/MSFT/Alphabet/Amazon slated to spend ≥$700B 2026 AI capex, ~80% above 2025 | Credit/capex stress context behind chip selloff | Vol risk | Med-High |
| CNBC — Finance | blog | Fed Chair Kevin Warsh pledges policy "regime change" to fight inflation, testifies to House and Senate | New hawkish Fed leadership — genuine regime-relevant change | HIGH | High |
| CNBC — Finance | blog | Dallas Fed's Logan calls for "modestly" higher rates even after cooler CPI | Hawkish committee voice | HIGH | High |
| CNBC — Finance | blog | NY Fed's Williams says inflation "has peaked," rates "well positioned" | Dovish-leaning counter-voice — Fed direction still contested | Mixed | High |
| CNBC — Economy | blog | CPI rose 3.5% annually in June, less than the 3.8% expected | Cooler-than-expected inflation print, immediately contested by Logan | Mitigating (dovish) | High |
| WSJ Markets | blog | "Sharp Drop in Diesel Supplies Threatens to Rev Up Inflation Again" | Independent supply-side inflation-reacceleration risk | HIGH | Med-High |
| ETF Trends (VettaFi) + Investing.com (2 sources) | blog | Retail sales rose for 5th straight month (+0.2%, $768.6B per Census Bureau); "Second-Quarter Consumer Rebound" | Consumer demand holding up despite war/inflation backdrop | Mitigating (lower vol) | High |
| ETF Trends (VettaFi) ×4 + Motley Fool ×1 | blog | Small-caps "easily outpacing" S&P 500 on "strong, fundamental legs" across 4 independent pieces + Motley Fool small-cap-ETF comparison | Durable IWM relative-strength / broadening-out signal | Rotation signal | High — direct IWM relevance |
| Yahoo Finance | blog | El-Erian: Dow +9% YTD, Nasdaq +11%, S&P +10% — gap closing ("fascinating market shift") | Broadening away from mega-cap tech, corroborates small-cap rotation | Rotation signal | High |
| ETF Trends (VettaFi) | blog | "Time to Upgrade Financials?" — explicitly ties "2026 war with Iran" to inflation/oil-vol portfolio drag, pitches financials rotation | Ties geopolitical and rotation threads together | Med-High | Med-High |
| Yahoo Finance / Motley Fool (same wire item) | blog | S&P 500 Shiller CAPE ratio "on the verge of reaching its highest level in history" | Valuation-regime caveat on SPY strength | Vol risk (valuation) | Med-High |
| CNBC — Finance | blog | Buffett: "It's tough to find values when everybody is preferring gambling" | Widely-followed valuation-risk commentary | Vol risk | Medium |
| WSJ Markets | blog | "Blockbuster Stock Sales Are Threatening to Overwhelm the Bull Market" — share-issuance pace echoes "later stages of prior rallies" | Late-cycle equity-supply signal | Vol risk | Med-High |
| Yahoo Finance | blog | UBS doubles down on its S&P 500 target | Bullish counter-voice, sharpens debate | Mitigating | Medium |
| WSJ Markets | blog | Morgan Stanley record quarterly revenue (equities trading +69%); BlackRock AUM past $15T (+20% profit) — but Nasdaq fell same week TSMC posted record results | Strong earnings currently overwhelmed by AI-valuation concerns — earnings/price divergence | Mixed | High — catalyst-filter relevant |
| CNBC — Finance | blog | "Big banks poised to report booming revenue propelled by SpaceX IPO, Iran war volatility" | War-driven vol is a revenue tailwind for bank trading desks, not uniformly bearish | Context | Medium |
| The Big Picture (Ritholtz) | blog | "At The Money: When Should Do-It-Yourself Investors Fire Themselves?" | Legitimate wealth-mgmt / advisory-transition content | n/a | Medium |
| Oseille TV | youtube (title-only) | "Ces pays d'Afrique vendent leur passeport (et c'est 100% légal)" | Africa-adjacent but NOT UEMOA/CFA-franc content — passport-by-investment programs; explicitly ruled out | n/a | Low — title-only, not UEMOA-relevant |
| IG France (Alexandre Baradez) ×7 | youtube (title-only) | MarketLive videos on Iran/oil impact, US inflation reaction, EUR/USD signal, Fed/ECB | Thematically aligned with geopolitical/Fed threads but unverifiable | Directional only | Low — title-only |
| Motley Fool (~44 remaining items) | blog | Single-stock deep-dives (Nvidia, Tesla, IBM, Amazon, Sandisk, TSM/UNH/Wipro earnings transcripts, retirement/SS explainers) | — | — | Low — outside ETF-only mandate |
| ETF Trends (VettaFi) (~35 remaining items) | blog | Niche single-fund/product pieces (nuclear, crypto ETPs, CLOs, MLPs, healthcare/space funds) | — | — | Low-Med — product-level, not macro |
| WSJ Markets (~30 remaining items) | blog | Opinion columns, M&A/single-company stories (Alcoa, Altice, U.S. Bancorp, prenup/housing features) | — | — | Low |
| Investing.com — Stock Market News (10 items) | blog (title-only) | Single-company/regional headlines (Hemnet, Getinge, SMA Solar, Indonesia index) | — | — | Low — title-only |
| Seeking Alpha — Market Currents (7 items) | blog (title-only) | Single-company earnings/M&A wire items (SKF, Husqvarna, Assa Abloy, Getinge) | — | — | Low — title-only |
| Federal Reserve (official) (3 items) | blog | Bank-exam/enforcement notices, discount-rate-meeting minutes | — | — | Low-Med — administrative |
| Liberty Street Economics (NY Fed) (2 items) | blog | Basel III / bank-holding-company capital-structure research series | — | — | Low-Med — background only |
| FRED Blog (St. Louis Fed) (2 items) | blog | State-level manufacturing employment, Q1 2026 state GDP data | — | — | Low — long-run background |
