# YouTube Intel — 2026-07-11

First run of the YouTube monitor: all 7 watchlist channels had `last_checked = never`,
so each was scanned back 7 days. 17 new videos found across 6 channels (Real Vision:
none). Transcript fetch was blocked by YouTube (cloud-IP rate limit) for 16/17 videos —
only titles are available for those. One transcript (George Gammon) came through in
full and is analyzed below.

## Executive Summary — Vol Regime Implications
- **Primary signal (transcript-confirmed):** George Gammon flags a sharp deterioration
  in the Atlanta Fed GDPNow tracker (~4.5% in Apr/May → 1.2% now, likely heading toward
  0%/negative), driven by a trade-deficit spike tied to AI-capex imports, plus a very
  weak NFP print (57K vs ~115K expected, prior two months revised down a combined
  -74K) and news of Blackstone canceling its largest-ever proposed data center project.
  Net framing: recession-risk / growth-scare narrative building — a HIGH_VOL,
  risk-off lean if it gains traction.
- **Title-only signals (low confidence, no transcript):** IG France posted a video
  titled directly on VIX ("VIX (volatilité) : un rebond marqué...puis une détente" —
  "a marked rebound... then a cooldown") on 2026-07-10, consistent with a vol spike
  that is already fading — this is in some tension with Gammon's more alarmist framing.
  Bravos Research's "Something Just Broke in the Financial System..." (2026-07-07)
  points the same recession-risk/high-vol direction as Gammon but can't be confirmed
  without transcript text.
- Net read: weak-but-not-yet-confirmed cluster of risk-off signals (GDP downgrade,
  soft labor print, VIX pop) around early July. Not enough independently-verified
  signal today to move regime confidence on its own — treat as a watch item, cross-check
  against the HMM's own regime output before acting. **No IWM/QQQ/SPY rotation calls**
  were identifiable from any source today (title-only channels didn't address ETF
  preference; Gammon's video is macro/GDP-focused, not ETF-specific).

## Per-Video Detail

### George Gammon — "This Multi Trillion Dollar Bubble May Have Just Broken The Economy" (2026-07-09)
- **Transcript:** available (analyzed in full, ~8000 chars)
- **Thesis:** Atlanta Fed GDPNow collapsed from ~4.5% (Apr/May) to 1.2%, mainly due to
  a trade-deficit blowout from AI-capex-driven imports (servers, semiconductors,
  computer accessories) — not a straightforward "demand is weak" story on its face,
  but compounded by a very soft July 2 NFP report (57K actual vs ~115-117K expected,
  with -74K in prior revisions, and a household-survey employment drop of >500K).
  Blackstone canceled its largest-ever proposed AI data center project (2,100 acres),
  cited as corroborating evidence the AI-capex boom is cracking.
- **Regime signal:** Growth/recession risk rising → supports a HIGH_VOL regime lean if
  confirmed by price action. Fed/rates relevance: weak labor data increases odds of a
  more dovish Fed reaction function (rate-cut narrative), which historically also can
  spike near-term vol before compressing it.
- **Confidence:** Medium — single-channel, no independent transcript corroboration yet.
  Macro data cited (GDPNow, NFP) is checkable against Alpaca/FRED-independent sources
  if desired.

### IG France (Alexandre Baradez) — 5 new videos (2026-07-06 to 2026-07-10)
- **Transcripts:** all blocked (NO_TRANSCRIPT, YouTube IP rate-limit)
- Titles: MarketLive market-trends round-ups (x2), a VIX rebound-then-cooldown piece,
  a Fibonacci/technical-entry piece, and a Japan/BoJ/yen piece.
- **Regime signal (title-only, low confidence):** "VIX (volatilité): un rebond
  marqué...puis une détente" suggests a vol spike that already faded by publish date
  (2026-07-10) — tentatively RISK-OFF-then-STABILIZING. The Japan/BoJ/yen title
  suggests carry-trade/yen-volatility commentary, a known cross-asset vol catalyst,
  but content is unconfirmed.

### Bravos Research — "Something Just Broke in the Financial System..." (2026-07-07)
- **Transcript:** blocked (NO_TRANSCRIPT)
- **Regime signal (title-only, low confidence):** Alarmist framing consistent with
  Gammon's recession-risk narrative; can't independently verify claim without content.

### Finary — 3 new videos (2026-07-05 to 2026-07-10)
- **Transcripts:** all blocked
- Titles: crypto migration prompt, "plan to get (very) rich," a concentrated-PEA
  (single-stock) risk story. Wealth-mgmt content, no regime signal.

### Investing Simplified (Prof G) — 3 new videos (2026-07-04 to 2026-07-08)
- **Transcripts:** all blocked
- Titles: dividend income ($4,100/mo), $2M portfolio retirement readiness, "why your
  portfolio isn't growing faster." Wealth-mgmt/retirement content, no regime signal.

### Oseille TV — 3 new videos (2026-07-06 to 2026-07-10)
- **Transcripts:** all blocked
- Titles: France-exit/expat commentary, Luxembourg vs France assurance-vie comparison,
  a press-freedom story. UEMOA/Africa-adjacent expat/tax angle but no direct Africa
  content this cycle; no regime signal.

### Real Vision Presents
- No new videos since last (first) check.

## Cross-Channel Consensus
- **2+ channels pointing risk-off/high-vol:** George Gammon (confirmed via transcript)
  + Bravos Research (title-only) both flag "something broke" / recession-risk framing
  in the same window (2026-07-07 to 2026-07-09). IG France's VIX title is directionally
  consistent (a vol event occurred) but reads as already cooling by 2026-07-10.
  **This is a 2-channel consensus on elevated-but-fading volatility / rising
  recession-risk narrative** — worth flagging to the HMM regime check, but Bravos and
  IG France signals are title-only and unverified; treat as soft confirmation, not a
  standalone trigger.
- No consensus found on SPY/QQQ/IWM rotation preference.

## Wealth Management TLDR
1. No UEMOA/Africa-specific content surfaced this cycle (Oseille TV covered French
   expat/tax topics, not Africa) — nothing actionable on that front today.
2. Finary's "concentrated PEA into one stock" story and Prof G's "$4,100/mo dividend"
   pitch are both single-name/concentration-risk narratives — flag as investor-education
   content only, not applicable to this bot's ETF-only, no-individual-stock mandate.
3. If the Gammon/Bravos recession-risk narrative persists across the next 2-3 trading
   days with price confirmation (SPY/QQQ drawdown + VIX re-acceleration), consider it
   corroborating context for a HIGH_VOL regime call — but the HMM's own signal should
   lead, not this commentary.

## Data Quality Note
- 16 of 17 new videos returned `NO_TRANSCRIPT` due to YouTube blocking transcript
  requests from this cloud environment's IP (see raw log). This is a structural
  limitation of running `youtube-transcript-api` from a cloud/datacenter IP, not a
  one-off fetch failure. Future runs will likely hit the same wall until this is
  fixed (proxy configuration would be required per the library's own guidance).
  Titles were used as a fallback low-confidence signal where noted above.
