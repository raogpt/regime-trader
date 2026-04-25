"""
Unit tests for OrderExecutor — Phase 6.

All broker calls are mocked so no real Alpaca connection is needed.
Covers:
  Rebalancing   : buy when below target, sell when above, skip within threshold
  Stop management: stop triggers close, stop update persisted
  Close-all      : all positions are closed
  Risk gate      : rejected orders don't reach the broker
"""

from __future__ import annotations

import pytest
from unittest.mock import MagicMock, patch
from datetime import datetime, timezone

from execution.order_executor import OrderExecutor, OpenPosition
from risk.risk_manager import RiskManager, PositionSizeResult
from models.regime_strategies import Signal


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

def _filled_order(ticker: str = "SPY", qty: int = 10,
                  price: float = 400.0, order_id: str = "ord-1") -> dict:
    return {
        "id": order_id, "status": "filled",
        "filled_avg_price": price, "filled_qty": qty,
    }


def _signal(symbol: str = "SPY", size_pct: float = 0.50,
             entry: float = 400.0, stop: float = 390.0,
             leverage: float = 1.0) -> Signal:
    return Signal(
        symbol             = symbol,
        direction          = "LONG",
        confidence         = 0.80,
        entry_price        = entry,
        stop_loss          = stop,
        take_profit        = None,
        position_size_pct  = size_pct,
        leverage           = leverage,
        regime_id          = 3,
        regime_name        = "bull",
        regime_probability = 0.80,
        timestamp          = datetime.now(timezone.utc),
        reasoning          = "test",
        strategy_name      = "LowVolBull",
        metadata           = {},
    )


@pytest.fixture
def mock_broker():
    broker = MagicMock()
    broker.submit_market_order.return_value = _filled_order()
    broker.get_open_positions.return_value  = []
    return broker


@pytest.fixture
def executor(mock_broker, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    risk = RiskManager(portfolio_value=100_000.0)
    risk.update_portfolio_value(100_000.0)
    return OrderExecutor(broker=mock_broker, risk_manager=risk)


def _add_position(executor: OrderExecutor, ticker: str = "SPY",
                   qty: int = 10, entry: float = 400.0,
                   stop: float = 390.0) -> None:
    """Inject a pre-existing position into executor's local state."""
    executor._open_positions[ticker] = OpenPosition(
        ticker          = ticker,
        qty             = qty,
        entry_price     = entry,
        current_price   = entry,
        stop_price      = stop,
        pnl             = 0.0,
        pnl_pct         = 0.0,
        regime_at_entry = "bull",
        opened_at       = datetime.now(timezone.utc),
    )
    executor._risk._open_positions[ticker] = qty * entry


# ---------------------------------------------------------------------------
# 1. Rebalancing
# ---------------------------------------------------------------------------

class TestRebalance:

    def test_buy_when_below_target(self, executor, mock_broker):
        # No open position → 0 notional, target = 100k × 0.50 × 1.0 = 50k
        # delta = 50k → buy
        mock_broker.submit_market_order.return_value = _filled_order(qty=10, price=400.0)
        sig     = _signal(size_pct=0.50, entry=400.0, stop=390.0)
        results = executor.rebalance(sig, account_value=100_000.0)
        assert len(results) == 1
        assert results[0].side == "buy"
        mock_broker.submit_market_order.assert_called_once()

    def test_sell_when_above_target(self, executor, mock_broker):
        # Inject large existing position → target is smaller → sell delta
        _add_position(executor, qty=1000, entry=400.0)   # 400k notional
        mock_broker.submit_market_order.return_value = _filled_order(qty=875, price=400.0)
        sig     = _signal(size_pct=0.05, entry=400.0, stop=390.0)  # target=5k
        results = executor.rebalance(sig, account_value=100_000.0)
        assert len(results) == 1
        assert results[0].side == "sell"

    def test_no_order_when_within_threshold(self, executor, mock_broker):
        # Current position ≈ target (within 5% of account_value = $5k threshold)
        _add_position(executor, qty=125, entry=400.0)  # 50k notional
        # Target = 100k × 0.52 = 52k → delta = 2k < 5k threshold
        sig     = _signal(size_pct=0.52, entry=400.0, stop=390.0)
        results = executor.rebalance(sig, account_value=100_000.0)
        assert results == []
        mock_broker.submit_market_order.assert_not_called()


# ---------------------------------------------------------------------------
# 2. Stop management
# ---------------------------------------------------------------------------

class TestStopManagement:

    def test_stop_triggers_close(self, executor, mock_broker):
        _add_position(executor, qty=10, entry=400.0, stop=390.0)
        mock_broker.submit_market_order.return_value = _filled_order(qty=10, price=385.0)
        closed = executor.check_stops({"SPY": 385.0})  # price below stop
        assert len(closed) == 1
        assert closed[0].ticker == "SPY"
        assert "SPY" not in executor._open_positions

    def test_stop_not_triggered_above_stop(self, executor, mock_broker):
        _add_position(executor, qty=10, entry=400.0, stop=390.0)
        closed = executor.check_stops({"SPY": 395.0})  # price above stop
        assert closed == []
        assert "SPY" in executor._open_positions

    def test_stop_update_persisted(self, executor):
        _add_position(executor, stop=390.0)
        assert executor.update_stop("SPY", 395.0) is True
        assert executor._open_positions["SPY"].stop_price == 395.0

    def test_stop_update_unknown_ticker(self, executor):
        assert executor.update_stop("UNKNOWN", 100.0) is False


# ---------------------------------------------------------------------------
# 3. Close all positions
# ---------------------------------------------------------------------------

class TestCloseAll:

    def test_close_all_positions(self, executor, mock_broker):
        _add_position(executor, "SPY", qty=10)
        _add_position(executor, "QQQ", qty=5, entry=350.0)
        mock_broker.submit_market_order.side_effect = [
            _filled_order("SPY", qty=10, price=400.0, order_id="o1"),
            _filled_order("QQQ", qty=5,  price=350.0, order_id="o2"),
        ]
        results = executor.close_all_positions(reason="test")
        assert len(results) == 2
        assert executor._open_positions == {}

    def test_close_all_no_positions(self, executor, mock_broker):
        results = executor.close_all_positions()
        assert results == []
        mock_broker.submit_market_order.assert_not_called()


# ---------------------------------------------------------------------------
# 4. Risk gate integration
# ---------------------------------------------------------------------------

class TestRiskGate:

    def test_rejected_buy_does_not_reach_broker(self, executor, mock_broker, tmp_path):
        # Trigger peak lock so all trading is halted
        executor._risk._peak = 100_000
        executor._risk.update_portfolio_value(89_000)   # -11% → lock
        size = PositionSizeResult(
            ticker="SPY", shares=10, notional=4_000, entry_price=400.0,
            stop_price=390.0, risk_amount=100.0,
        )
        result = executor.buy("SPY", size, "bull")
        assert result is not None
        assert result.status == "rejected"
        mock_broker.submit_market_order.assert_not_called()
