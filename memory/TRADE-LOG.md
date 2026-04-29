# Trade Log — regime_trader

## Day 0 — Baseline (pre-launch)
**Portfolio:** $100,000.00 | **Cash:** $100,000.00 (100%) | **Day P&L:** $0 | **Phase P&L:** $0
**Regime:** UNKNOWN (HMM not yet run in episodic mode)

No positions. Bot launches Monday Apr 27.

## 2026-04-29 — Market Open
**Regime:** CRASH | **Confidence:** 100.0% | **Portfolio:** $99,528.98 | **Cash:** $5,213.88
**Strategy:** HighVolDefensiveStrategy (60% invested, 1.0x leverage)

| ETF | Side | Shares | Avg Entry | Stop | Conf | Regime |
|---|---|---|---|---|---|---|
| SPY | BUY | 55 (total) | 711.98 | 678.46 | 1.00 | crash |
| QQQ | BUY | 38 (total) | 659.61 | 610.82 | 1.00 | crash |
| IWM | BUY | 111 (total) | 275.34 | 258.21 | 1.00 | crash |

_Unrealized P&L: SPY -$114.77 | QQQ -$80.81 | IWM -$275.45 | Total: -$471.03_
_Note: fill qty=0 display bug fixed — orders confirmed filled via Alpaca positions API._
