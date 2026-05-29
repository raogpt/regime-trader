# Trade Log — regime_trader

## Day 0 — Baseline (pre-launch)
**Portfolio:** $100,000.00 | **Cash:** $100,000.00 (100%) | **Day P&L:** $0 | **Phase P&L:** $0
**Regime:** UNKNOWN (HMM not yet run in episodic mode)

No positions. Bot launches Monday Apr 27.

## 2026-05-29 — Market Open
**Regime:** BULL | **Confidence:** 100.0% | **Portfolio:** $115,624.56

_No trades executed — HOLD (insufficient buying power: $7,003.38 available vs ~$16k+ required per ticker; existing positions consuming margin)._

**Diagnostic:** Signals generated for SPY/QQQ/IWM (BULL regime), but Alpaca rejected all orders with `code:40310000 insufficient buying power`. Account equity $115,624.56 but buying power only $7,003.38 — existing open positions likely holding most capital. No circuit breaker triggered. Bot fixes applied this session: IEX data feed, FeatureEngineer method name, n_bars 60→300, RiskManager API corrections, StrategyOrchestrator construction.
