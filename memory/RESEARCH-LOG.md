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

## 2026-08-22 — Market Intel (regime_trader)
| Source | Type | Item | Regime Signal | Vol Bias | Relevance |
|--------|------|------|----------------|----------|-----------|
| WSJ Markets | blog | Bessent leans into "bond trader in chief" role; Treasury signals willingness to intervene after yields hit nearly two-decade highs | Fed/Treasury bond-market intervention; rates regime shift | HIGH | High |
| WSJ Markets | blog | "The Wild Week When Scott Bessent Was Schooled by the Bond Market" — Treasury bond-buyback announcement stemmed selloff only briefly | Buyback intervention losing effectiveness | HIGH | High |
| WSJ Markets | blog | "Bond Yields Rise Despite Treasury Efforts to Curb Borrowing Costs"; "Markets Brush Off Treasury's Buyback Plans" | Bond-market stress persists despite policy response | HIGH | High |
| WSJ Markets | blog | "The Treasury Market's Coveted Status as a Safe Haven Is Fading" — two new studies find investors less willing to accept low yields for Treasury safety | Structural rates-regime shift, not just a one-week move | HIGH | High — rates/vol input |
| WSJ Markets (opinion) | blog | "High Anxiety in the Bond Market" — frames move as "return to pre-2008 interest rates," not panic-worthy | Rates elevated but framed as normalization, not crisis | Med-High | Med |
| WSJ Markets (opinion) | blog | "The Bond 'Chaos' Is a Sign Kevin Warsh's Plan Is Working" — new Fed Chair Warsh described as less willing to "subsidize spendthrift lawmakers" | Confirms Fed leadership change (Warsh) + hawkish-on-fiscal framing | HIGH | High — Fed/HMM relevant |
| Ritholtz (Claudia Sahm via Big Picture) | blog | "Read the Minutes, Fade the Presser" — July FOMC minutes (Warsh's 2nd meeting as Chair) revealed a different reaction function than his press conference explanation of the hold | Fed communication/credibility gap under new Chair | HIGH | High |
| Ritholtz (Stay-At-Home Macro via Big Picture) | blog | Kevin Warsh's first Jackson Hole speech (imminent) framed as "a test of the Chair, and of the Fed's credibility" | Major pending Fed catalyst, outcome unresolved | Uncertain — HIGH pending | High |
| Federal Reserve (official) | blog | FOMC statement issued 7/29/2026; FOMC minutes for July 28-29 meeting released 8/19/2026 | Primary Fed policy record for the period | Context | High |
| Investing.com — Market Overview | blog | "US Dollar Weakness Exposes Rising Doubts Over Fed Credibility"; "THINK Ahead: Bessent Versus the Bond Market" | Dollar/Fed-credibility signal, independent source | HIGH | High |
| Yahoo Finance | blog | US 30-year Treasury yield climbed for a second straight week; stocks end week lower on pressure from elevated long-duration yields | Direct rates-driven equity pressure, named data point | HIGH | High — direct SPY/QQQ/IWM driver |
| Ritholtz (Krugman via Big Picture) | blog | "What Are Bond Markets Telling Us?" — long-term government yields in many countries back at levels not seen since mid-2000s; deficits only part of the story | Independent economist read corroborating global rate surge | HIGH | Med-High |
| NPR (via Ritholtz) | blog | "The bond market is signaling trouble ahead" — selloff attributed to rising-inflation fears plus persistent fiscal deficits | Third independent framing of same bond-stress narrative | HIGH | Med-High |
| WSJ Markets | blog | "Gold Above $4,600 on Weaker Dollar, Debt Fears" — Treasury's buyback expansion read by investors as a stress signal, triggering fresh dollar selling | Debasement-trade / inflation-hedge flow | HIGH | High |
| Investing.com — Market Overview | blog | "Brent Nears $100, Gold Breaks Above $4,500 as Investors Await PCE Inflation Data" | Independent gold/oil corroboration ahead of PCE print | HIGH | Med-High |
| WSJ Markets | blog | "Bitcoin Surges as Institutional Demand, Short Covering, Clarity Act Progress Converge" — jumped >9% to $79,455, near $80k, highest since late May | Risk-appetite/debasement-trade proxy outside ETF universe | Med (context) | Low-Med |
| WSJ Markets | blog | "U.S. Stocks Rise as Bitcoin Nears $80,000"; "Dollar Looks Best Defensive Currency During Bond and Equity Selloffs" (BNY) | Cross-asset risk-appetite context | Mixed | Med |
| WSJ Markets | blog | "Stock Market News, Aug. 21, 2026": S&P 500 ends Friday with a weekly loss; Dow facing its largest weekly decline since March | Direct SPY-relevant weekly drawdown data point | HIGH | High |
| Investing.com — Market Overview | blog | "Stock Market Outlook: Major Indexes Flash New Sell Signals"; "Nasdaq 100 Is About to Make Wall Street Sleepy" | Technical sell-signal read, mixed with a complacency counter-read on QQQ | Mixed | Med — QQQ-relevant |
| Yahoo Finance | blog | "Dow Jones Futures: Market Rally Repairs Some Damage; Nvidia Earnings Loom" — bitcoin/gold "shined" while broad market took damage last week | Bounce attempt into next week's Nvidia earnings + Jackson Hole | Mixed | High — near-term catalyst calendar |
| WSJ Markets | blog | "Trump Threatens Iran With 'Economic D-Day'"; "Oil Posts Weekly Gains on Simmering Middle East Tension" — no resolution, US shifting to economic squeeze rather than renewed strikes | Iran conflict de-escalated from active strikes (per 7/13 report) to sanctions-phase, but unresolved | Med (down from HIGH in July) | Med — earnings/catalyst filter |
| Ritholtz (WSJ item via Big Picture) | blog | "Iran's Secret Plan to Escalate the War" — intercepted communications suggest hardline leaders may raise costs for US/allies | Re-escalation risk still live despite the economic-pressure framing | Uncertain (tail risk) | Med |
| WSJ Markets | blog | "See How China Weathered the Iran Oil Shock" — China cut crude imports, tamping down global prices | Global spillover context, mitigating factor on oil-driven vol | Mitigating | Low-Med |
| WSJ Markets | blog | "How Wall Street Sussed Out That Situational Awareness Was on the Ropes" — options/prime-broker signals detected trouble before an AI-conviction hedge fund's blow-up tied to an Anthropic stake sale | AI-bubble/concentration-risk event, single-fund but macro-relevant as a stress indicator | Vol risk | Med-High |
| Ritholtz (Damodaran via Big Picture) | blog | "The Situational Awareness Fund Blow-up" post-mortem — conviction investing/concentration-risk lessons from the Aschenbrenner fund implosion | Independent corroboration of the AI-conviction blow-up | Vol risk | Med |
| Ritholtz (Sascha Steffen via Big Picture) | blog | "Inside Nvidia's $500 Billion AI Debt Machine" — credit-risk breakdown of vendor financing/circular deals; risk if the AI capex cycle turns | AI-credit-stress thesis, corroborates 7/13 report's AI-bond concern | Vol risk | Med-High |
| IG France (Alexandre Baradez) | youtube (title-only) | "Nvidia, Meta, Alphabet...le prix des 'assurances' (CDS) contre un risque de défaut augmente" (8/13) | Independent, French-source corroboration of rising AI-mega-cap default-protection costs | Vol risk | Med — title-only |
| IG France (Alexandre Baradez) | youtube (title-only) | "Guerre en Iran: Les Etats-Unis empruntent plus cher" (8/12); "La forte hausse de l'effet de levier aux Etats-Unis" (8/14); "L'indice VIX au contact d'un niveau technique important" (8/7); "Effet de levier excessif: l'avertissement du PDG de JPMorgan" (8/7) | Independent French-source thread tracking rates/leverage/VIX over the period, consistent with the English-source narrative | Supports HIGH | Med — title-only |
| Motley Fool | blog | "Every S&P 500 Index Fund Owner Holds More Nvidia Than Apple" — Nvidia 7.50% of VOO vs Apple 6.58% as of 6/30/2026 | Index-concentration risk data point, direct ETF relevance | Context | High — SPY/VOO composition |
| Ritholtz (via Big Picture) | blog | Weak July retail sales (-0.6% vs +0.1% expected); BNPL lenders now pitching loans for electricity/rent (NYT) | Consumer-stress signals corroborating a softening backdrop | Supports MID-HIGH | Med-High |
| WSJ Markets | blog | Walmart earnings miss cited as weighing on markets ("Stocks Slump as Bond Yields Rise With Crude Prices," "Markets Brush Off Treasury's Buyback Plans") | Consumer-spending read via a bellwether retailer | Med | Med |
| Liberty Street Economics (NY Fed) | blog | Credit card stock delinquency rose 7.6%→12.8% (2022:Q3–2026:Q1) but driven by aging charged-off debt; flow delinquency has been stable since 2024 | Mitigating factor — consumer credit stress is not accelerating on a flow basis | Mitigating | Med — Fed/HMM relevant |
| Liberty Street Economics (NY Fed) | blog | "A Window into Bond Investors' Uncertainty About R-Star" — investor r-star estimates carry ~±170bp 95% confidence bands | Primary research on rate-market uncertainty, background context | Context | Med |
| FRED Blog | blog | "Is AI reducing employment for software coders?" — coder employment decelerated sharply after Nov-2022 genAI launch per Fed Board research (Crane & Soto) | AI-labor-displacement data point, corroborates AI-disruption theme | Context | Med |
| FRED Blog | blog | Crude oil/jet fuel/airfare tracker notes WTI spiked when the US-Iran conflict began 2/28/2026 — airfare pass-through much more muted than fuel-cost spike | Confirms Iran conflict predates this batch by ~6 months; useful base-rate context | Context | Low-Med |
| WSJ Markets (opinion) | blog | "AI Bubble May Deflate, Not Burst" — economy transformation "proceeding, but at a slower pace than we were led to expect" | Measured counter-read to AI-bubble-crash narratives | Mitigating | Med |
| Ritholtz (Advisor Perspectives via Big Picture) | blog | "Long TIPS Yield 3%. Time to Buy?" — real yields at levels last seen briefly in 2008 | Actionable wealth-mgmt real-yield signal tied to the rates move | Context | Med — wealth-mgmt |
| WSJ Markets | blog | "How Index Funds Went From Being Mocked to Feared in 50 Years" — Vanguard's S&P 500 fund (launched 1976) turns 50 on 8/31/2026, now $1.67T across share classes | Evergreen wealth-mgmt/index-investing milestone | Low direct | Low |
| George Gammon | youtube (title-only) | "WARNING: This Is When The Dollar Will Lose Reserve Currency Status" (8/21); "BREAKING NEWS: They Just Admitted The Conspiracy Theories Are True" (8/22); "WARNING: They Just Created A $10 Trillion Derivatives Timebomb" (7/23) | Thematically aligned with dollar-weakness/debt-fear narrative but sensationalized, single-source, title-only | Low confidence | Low — title-only, editorializing |
| Bravos Research | youtube (title-only) | "Japan and the US Just Pulled the Trigger (Brace for Impact)" (8/18); "History is About to Be Made... (Emergency Update)" (8/21); "A Once in a Lifetime Economic Reset Is Arriving" (8/4) | Directionally consistent with elevated-macro-uncertainty theme; title-only, cannot verify content | Low confidence | Low — title-only |
| Investing Simplified (Prof G) | youtube (title-only, 15 items) | Recurring "market crash," "volatile stock market," "overpriced market" framing across July-Aug uploads | Retail-facing volatility/crash framing, consistent cadence | Low confidence | Low — title-only |
| **No UEMOA/West Africa wealth-management content identified** — Oseille TV's "Ces pays d'Afrique vendent leur passeport" (7/14) is citizenship-by-investment/expat content, not UEMOA financial/wealth content; flagged per bot priority, nothing to log | — | — | — | — | — |
| Motley Fool (48 remaining items) | blog | Single-stock/AI-name deep dives (Nike, Berkshire, Blink Charging, etc.) and generic retirement/index-fund explainers | — | — | Low — outside ETF-only mandate |
| WSJ Markets (~35 remaining items) | blog | Roundups (Financial Services, Health Care, TMT, Energy, Basic Materials "Market Talk"), M&A/deals, opinion columns, single-company/culture pieces | — | — | Low |
| Investing.com — Stock Market News (10 items, title-only) | blog (title-only) | Single-company/regional headlines (Boeing union vote, China auto recall, Mexico/Colombia stock closes, OpenAI pricing) | — | — | Low — title-only |
| Seeking Alpha — Market Currents (7 items, title-only) | blog (title-only) | Single-company/commodity headlines (Iran oil to China, Hims & Hers, Silver Storm placement, gold/dollar note) | — | — | Low — title-only, one item (gold/dollar) already captured above |
| Finary (14 items) | youtube (title-only, FR) | Generic French personal-finance content (savings, investing basics, wealth psychology); one ambiguous title "Toute une génération ruinée en moins d'un mois" (8/9) — cannot assess without transcript | — | — | Low — title-only |
| Oseille TV (10 items) | youtube (title-only, FR) | Expat/citizenship-by-investment and tax-residency content (Panama, Italy, Africa passports, EU privacy law), not core markets content | — | — | Low — title-only, off-mandate |
