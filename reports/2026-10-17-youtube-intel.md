# YouTube / Market Intel — 2026-10-17

**Data caveat:** `scripts/youtube_monitor.py` is missing from the repo; `scripts/intel_monitor.py` was used instead. 95 YouTube items found, **no transcripts available** (YouTube blocks this egress IP; items queued in `memory/transcript-queue.json`). All YouTube analysis below is **title-only**. Only blog/RSS items had content. No trade actions derived from this report — HMM regime/confidence rules in CLAUDE.md govern.

## Executive Summary (vol regime implications)
- Tilt: **upward volatility pressure**, not yet confirmed by price. Equities calm (S&P ~-0.25% 10/8–10/15) while macro stress rises.
- Drivers (content-backed): Brent $110 / WTI >$100 (10/17, Seeking Alpha); hot inflation with retail sales +0.8% (Investing.com 10/16); "case for another rate hike growing stronger"; USD slid as hike bets faded — mixed rate expectations; FOMC minutes (Sep 15-16) out 10/7.
- Narrative layer (titles only): Gammon/Bravos heavily bearish (Fed mistake, debt crisis, dollar reset); Investing Simplified split (complacency warning vs "dip is a gift").
- Implication for HMM: watch for transition LOW/MID → HIGH vol. Act only on model output (≥55% confidence, 3 stable bars). Treat oil spike + rate-hike risk as a catalyst-filter flag.

## Per-Video (title-only; confidence = low unless noted)
| Channel | Title | Thesis (inferred) | Regime signal | Confidence |
|---|---|---|---|---|
| George Gammon | The Fed Just Made Their Biggest Mistake Since 2008 (10/7) | Fed policy error | Risk-off | Low |
| George Gammon | Systemic Risk Is EXPLODING In Financial Markets (10/1) | Systemic stress | Risk-off / high vol | Low |
| George Gammon | A Secret Global Monetary Reset Has Started (10/17) | Monetary reset narrative | Risk-off (hyperbolic) | Very low |
| Bravos Research | The Entire Financial System Just Changed Forever (10/15) | Macro regime shift | Risk-off | Low |
| Bravos Research | Trump Just Announced The US Dollar's Reset (10/9) | USD policy change | Dollar/macro vol | Low |
| Investing Simplified | The Stock Market Is Ignoring a HUGE Warning Sign (10/10) | Complacency | Late-cycle, vol underpriced | Low |
| Investing Simplified | Everything Says Stocks Should CRASH.. So Why Aren't They? (10/3) | Resilient tape | Low realized vol | Low |
| Investing Simplified | This Market Dip is a GIFT (10/13) | Buy the dip | Mild risk-on | Low |
| IG France | MarketLive 10/13, 10/14, 10/15 | Daily chart read | Unknown | None |
| Finary | J'ai enquêté sur le MSCI World (10/14) | Global index ETF education | n/a | n/a |
| Oseille TV | Le paradis fiscal où vous n'êtes même pas obligé de vivre (10/14) | Offshore/tax residency | n/a (wealth) | n/a |
| Real Vision | Red Sea: The Last Unread Map / Gold Frontier (10/8, 10/14) | Geopolitics/commodities | Context | Very low |

## Cross-Channel Consensus
- **Risk-off / elevated systemic-risk narrative**: Gammon + Bravos (2 channels) — title-only, sensationalist; weak evidence.
- **Markets resilient despite warnings**: Investing Simplified titles + Ritholtz ("Top? Beware Your Confirmation Bias") + S&P price action — vol still subdued.
- **Content-backed corroboration** (non-YouTube): oil spike + inflation + Fed-hike risk (Investing.com, Seeking Alpha).
- ETF preference (SPY/QQQ/IWM): no usable signal.

## Wealth Management TLDR
1. Global diversification: Finary's MSCI World deep-dive — verify what the index holds (US/tech concentration) before treating it as diversified.
2. UEMOA/Africa PRIORITY: Oseille TV's "passeport africain" (8/12) and tax-residency videos — need transcripts before any recommendation; consult a cross-border tax adviser (France/UEMOA treaty, CRS reporting — "116 pays balancent vos comptes", 8/5).
3. Retirement tax buckets (Investing Simplified 9/16): hold taxable / tax-deferred / tax-free mix — generic, check UEMOA/home-country equivalents.
4. Inflation + oil >$100: keep real-asset/inflation-protected exposure under review; avoid concentrated bets on narrative-driven "reset" thesis videos.
5. Fetch transcripts (residential-IP workflow) so next run can issue real, confidence-rated recommendations.
