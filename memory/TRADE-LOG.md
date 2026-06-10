# Trade Log — regime_trader

## Day 0 — Baseline (pre-launch)
**Portfolio:** $100,000.00 | **Cash:** $100,000.00 (100%) | **Day P&L:** $0 | **Phase P&L:** $0
**Regime:** UNKNOWN (HMM not yet run in episodic mode)

No positions. Bot launches Monday Apr 27.

## 2026-06-10 — Market Open
**Regime:** CRASH | **Confidence:** 100.0% | **Portfolio:** $108,717.64
**⚠️ NOTE:** Regime confirmed=False (1/3 bars). Stability guard was missing — patched post-execution. Orders below should be treated as erroneous; stability check now enforced.

| ETF | Side | Shares | Entry | Stop | Conf | Regime |
|---|---|---|---|---|---|---|
| SPY | BUY | 22 | 734.82 | 716.75 | 1.00 | crash |
| QQQ | BUY | 23 | 705.05 | 672.27 | 1.00 | crash |
| IWM | BUY | 53 | 286.89 | 272.49 | 1.00 | crash |

_Fills are async (paper trading). Qty/price updated from Alpaca post-fill._
_Existing positions carried: SPY 166, QQQ 142, IWM 444 (from prior sessions)._
