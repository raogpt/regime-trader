# YouTube Intel — 2026-05-07

**Bot:** regime_trader  
**Run date:** 2026-05-07  
**Status:** NO DATA — RSS unavailable

---

## Executive Summary

RSS feed fetch failed for all 7 monitored channels. The `feedparser` and `requests` Python packages could not connect to YouTube's RSS endpoints (no outbound network access in cloud session). This is the first run for all channels; a 7-day lookback was applied but yielded zero entries.

**Vol Regime Implication:** No signal extracted. Regime detection must rely on HMM model + Alpaca price data only for today's session.

---

## Per-Channel Results

| # | Channel | Lang | Signal Score | Result |
|---|---------|------|-------------|--------|
| 1 | Oseille TV | FR | — | No transcript (RSS failed) |
| 2 | Bravos Research | EN | — | No transcript (RSS failed) |
| 3 | Finary | FR | — | No transcript (RSS failed) |
| 4 | Investing Simplified (Prof G) | EN | — | No transcript (RSS failed) |
| 5 | George Gammon | EN | ★★★ | No transcript (RSS failed) |
| 6 | IG France (Alexandre Baradez) | FR | ★★★ | No transcript (RSS failed) |
| 7 | Real Vision Presents | EN | ★★★ | No transcript (RSS failed) |

---

## Cross-Channel Consensus

N/A — No data.

---

## Wealth Management TLDR

N/A — No data ingested today. Oseille TV and Finary (FR wealth-mgmt channels) are high-priority for next successful run.

---

## Operational Notes

- All channels are first-run ("never" last_checked) → timestamps NOT updated
- Retry: next session will attempt same 7-day lookback window for all channels
- Fix: ensure `pip install feedparser requests` succeeds in environment with network access
