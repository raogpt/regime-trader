# Trade Log — regime_trader

## Day 0 — Baseline (pre-launch)
**Portfolio:** $100,000.00 | **Cash:** $100,000.00 (100%) | **Day P&L:** $0 | **Phase P&L:** $0
**Regime:** UNKNOWN (HMM not yet run in episodic mode)

No positions. Bot launches Monday Apr 27.

## 2026-06-09 — Market Open
**Regime:** CRASH | **Confidence:** 100.0% | **Portfolio:** $112,642.53
**Existing positions:** SPY 144sh, QQQ 119sh, IWM 391sh (carried from prior sessions)
**Cash:** -$193,391 (account on margin from prior buys)

| ETF | Side | Shares | Entry | Stop | Conf | Regime |
|---|---|---|---|---|---|---|
| SPY | BUY | 22 | 744.52 | 717.69 | 1.00 | crash |
| QQQ | BUY | 15 | 722.68 | 674.13 | 1.00 | crash |
| IWM | BUY | 46 | 288.57 | 272.30 | 1.00 | crash |

> Note: fills initially logged as 0/0.00 (paper async fill). Actual fills confirmed via Alpaca API.
> Note: CRASH regime + LONG signals = HighVolDefensiveStrategy (small size). Catalyst gate OPEN (no trading-bot in cloud).
