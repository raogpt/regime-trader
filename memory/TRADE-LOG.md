# Trade Log — regime_trader

## Day 0 — Baseline (pre-launch)
**Portfolio:** $100,000.00 | **Cash:** $100,000.00 (100%) | **Day P&L:** $0 | **Phase P&L:** $0
**Regime:** UNKNOWN (HMM not yet run in episodic mode)

No positions. Bot launches Monday Apr 27.

## 2026-05-11 — Market Open
**Regime:** CRASH | **Confidence:** 100.0% | **Portfolio:** $108,356.09
**Positions:** SPY 127sh | QQQ 81sh (+8 today) | IWM 228sh | **Cash:** -$107,981 (2x leveraged)

| ETF | Side | Shares | Entry | Stop | Conf | Regime |
|---|---|---|---|---|---|---|
| QQQ | BUY | 8 | 711.64 | 629.04 | 1.00 | crash |
| SPY | SKIP | — | — | — | — | insufficient BP ($6,071 < cost) |
| IWM | SKIP | — | — | — | — | insufficient BP ($379 < cost) |

**Note:** Paper fill-tracking showed 0 shares; Alpaca order history confirms 8 QQQ filled @ $711.64.
