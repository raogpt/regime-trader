# YouTube Intel — 2026-07-12

## ⚠️ Data Quality Warning
`youtube-transcript-api` was blocked by YouTube on this cloud IP for all 18/18 videos
(`IpBlocked` / `RequestBlocked` error — cloud-provider IPs are commonly blocked by YouTube's
transcript endpoint). No transcript text was retrievable. Everything below is inferred from
**video titles only** — treat as low-confidence directional color, not a substitute for the
full transcript-based analysis this workflow is meant to produce. To fix: route
`youtube_monitor.py` transcript fetches through a proxy (see youtube-transcript-api README,
"Working around IP bans").

## Executive Summary (vol regime implications)
Title-only signal skews risk-off / crisis-framing this week:
- **George Gammon** (2 videos) and **Bravos Research** (1 video) are independently using
  "broke/subprime/bigger than 2008"-style language — consistent risk-off framing from
  2 distinct macro channels.
- **IG France** (Alexandre Baradez) flags a VIX rebound "then a cooldown" — read as a
  vol spike that's already fading, i.e. possibly HIGH_VOL → MID_VOL transition rather than
  a sustained regime break.
- **Investing Simplified (Prof G)** flags "expect major change in July" — vague but timed
  to the current month.
- No SPY/QQQ/IWM-specific rotation signal surfaced in titles; nothing here should move
  HMM confidence on its own given the transcript gap.

## Per-Video Notes

| Channel | Title | Thesis (title-inferred) | Regime Signal | Confidence |
|---|---|---|---|---|
| George Gammon | The Next Subprime Crisis Was Just Triggered...And It's Bigger Than 2008 | Credit-cycle/crisis framing | Risk-off | Low (title-only) |
| George Gammon | This Multi Trillion Dollar Bubble May Have Just Broken The Economy | Bubble-burst framing | Risk-off | Low (title-only) |
| Bravos Research | Something Just Broke in the Financial System... | Systemic stress framing | Risk-off | Low (title-only) |
| IG France | VIX (volatilité): un rebond marqué...puis une détente | Vol spike, now cooling | HIGH_VOL fading → MID_VOL | Low (title-only) |
| IG France | Le Japon sous haute surveillance des marchés ! (chute du yen, Banque du Japon, inflation...) | BoJ/yen stress as macro catalyst | Watch for cross-asset spillover | Low (title-only) |
| IG France | MarketLive x2 (2026-07-07, 2026-07-10) | Routine daily TA stream | Neutral | — |
| IG France | Fibonacci & Retracements: Identifier les Zones d'Entrée | Educational TA content | Neutral | — |
| Investing Simplified (Prof G) | 🚨BREAKING: 2026 Market Outlook (Expect Major Change in July) | Regime-shift call, timing = this month | Watch | Low (title-only) |
| Investing Simplified (Prof G) | How to Make $4,100 per Month in Dividends (SIMPLE) | Income strategy content | None | — |
| Investing Simplified (Prof G) | $2 Million Invested - Can I retire soon?! | Retirement planning content | None | — |
| Finary | 🚨 Vous devez migrer vos cryptos ? | Crypto-specific risk mgmt | Not SPY/QQQ/IWM relevant | — |
| Finary | Le plan pour devenir (très) riche | General wealth-building | Wealth mgmt | — |
| Finary | À 25 ans, il a déjà son plan pour être millionnaire à 65 ans | Long-horizon allocation profile | Wealth mgmt | — |
| Oseille TV | Assurance vie : pourquoi le Luxembourg écrase la France ? | Life-insurance wrapper tax comparison (FR/LUX) | Wealth mgmt / tax | — |
| Oseille TV | L'illusion qui vous empêche de quitter la France | Expat/tax framing | Wealth mgmt | — |
| Oseille TV | Pourquoi la plupart des gens ne veulent pas être libres | Lifestyle/mindset, non-financial | None | — |
| Oseille TV | 6 mois de prison pour un journaliste qui a enquêté | Non-financial | None | — |
| Real Vision Presents | (no new videos this window) | — | — | — |

## Cross-Channel Consensus (2+ channels agree)
- **Risk-off / "something broke" framing**: George Gammon (2 videos) + Bravos Research (1 video)
  independently use crisis/subprime/bubble-burst language this week. Title-only — cannot
  confirm whether this is about credit markets broadly or equity vol specifically. Flag for
  next transcript-capable run rather than acting on it now.
- No consensus found on ETF rotation (SPY vs QQQ vs IWM) — no channel titles addressed this
  directly.

## Wealth Management TLDR
1. Oseille TV covered Luxembourg vs. France life-insurance (assurance-vie) wrappers —
   revisit with full transcript if UEMOA/Africa tax angle comes up in future episodes
   (none did this week).
2. Finary and Prof G both published generic long-horizon wealth-building content — no
   actionable allocation change signal from titles alone.
3. No UEMOA/Africa-specific content surfaced this window.

## Recommendation for Next Run
Fix transcript access (proxy) before treating any of the above as more than a title scan —
the risk-off consensus from George Gammon + Bravos Research is the one item worth re-checking
with real transcript text once that's fixed.
