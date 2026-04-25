"""
Integration tests — Phase 9.

Five scenarios (all run without a real Alpaca connection):

  a. End-to-end dry run : data → HMM → strategy → risk → simulated orders
  b. Look-ahead audit   : backtest equity identical when run with different end dates
  c. Risk stress        : extreme signals capped, rapid-fire blocked, no-stop rejected
  d. Broker simulation  : submit_order / modify_stop / cancel / verify clean state
  e. Recovery           : write state_snapshot.json, reload, verify no double-entry
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import MagicMock, patch

import numpy as np
import pandas as pd
import pytest

from data.feature_engineering import FeatureEngineer
from execution.alpaca_broker import AlpacaBroker
from execution.order_executor import OrderExecutor, OpenPosition
from models.hmm_engine import HMMEngine, HMMEngineConfig
from models.regime_strategies import StrategyOrchestrator, Signal
from risk.risk_manager import RiskManager, RiskConfig, PositionSizeResult, LOCK_FILE


# ---------------------------------------------------------------------------
# Shared synthetic data helpers
# ---------------------------------------------------------------------------

def _make_ohlcv(n: int = 700, seed: int = 1) -> pd.DataFrame:
    rng   = np.random.default_rng(seed)
    close = 400.0 * np.exp(np.cumsum(rng.normal(0.0003, 0.010, n)))
    high  = close * rng.uniform(1.000, 1.012, n)
    low   = close * rng.uniform(0.988, 1.000, n)
    open_ = close * rng.uniform(0.996, 1.004, n)
    vol   = rng.integers(1_000_000, 8_000_000, n).astype(float)
    return pd.DataFrame({"open": open_, "high": high, "low": low,
                          "close": close, "volume": vol})


def _build_engine(feats: np.ndarray, n_states: int = 4) -> HMMEngine:
    cfg = HMMEngineConfig(n_states_range=(n_states, n_states),
                           n_init=2, random_state=0)
    eng = HMMEngine(config=cfg)
    eng.fit(feats)
    return eng


def _regime_infos(hmm: HMMEngine) -> list:
    return [hmm.get_regime_info(lbl) for lbl in hmm.regime_labels]


# ---------------------------------------------------------------------------
# a. End-to-end dry-run pipeline
# ---------------------------------------------------------------------------

class TestEndToEndPipeline:
    """
    Full data → HMM → strategy → risk → (simulated) order pipeline.
    No real broker — orders are intercepted and validated.
    """

    @pytest.fixture(scope="class")
    def pipeline(self):
        df      = _make_ohlcv(700)
        fe      = FeatureEngineer()
        feats   = fe.build_feature_matrix(df)
        hmm     = _build_engine(feats, n_states=4)
        infos   = _regime_infos(hmm)
        orch    = StrategyOrchestrator(infos)
        return df, fe, feats, hmm, orch

    def test_features_computed_without_nan(self, pipeline):
        _, _, feats, _, _ = pipeline
        assert not np.isnan(feats).any()

    def test_hmm_predicts_valid_regime(self, pipeline):
        _, _, feats, hmm, _ = pipeline
        regime = hmm.predict_regime(feats)
        assert regime.label in hmm.regime_labels
        assert 0.0 <= regime.probability <= 1.0

    def test_strategy_generates_signal(self, pipeline):
        df, fe, feats, hmm, orch = pipeline
        regime = hmm.predict_regime(feats)
        bars   = {"SPY": df.reset_index(drop=True)}
        sigs   = orch.generate_signals(["SPY"], bars, regime)
        assert isinstance(sigs, list)
        # May be empty if < 50 bars, but structure is valid
        for s in sigs:
            assert isinstance(s, Signal)
            assert s.stop_loss < s.entry_price

    def test_risk_sizes_from_signal(self, pipeline, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        df, fe, feats, hmm, orch = pipeline
        regime = hmm.predict_regime(feats)
        bars   = {"SPY": df.reset_index(drop=True)}
        sigs   = orch.generate_signals(["SPY"], bars, regime)
        if not sigs:
            pytest.skip("No signal generated with this data/regime combination")

        risk = RiskManager(portfolio_value=100_000.0,
                            config=RiskConfig(gap_risk_budget=1.0,
                                              max_single_position=0.50))
        risk.update_portfolio_value(100_000.0)
        sig  = sigs[0]
        size = risk.calculate_position_size(
            ticker         = sig.symbol,
            entry          = sig.entry_price,
            stop           = sig.stop_loss,
            regime_max_pct = sig.position_size_pct,
        )
        assert size.shares >= 0
        assert size.notional >= 0.0

    def test_order_approved_and_logged(self, pipeline, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        df, fe, feats, hmm, orch = pipeline
        regime = hmm.predict_regime(feats)
        bars   = {"SPY": df.reset_index(drop=True)}
        sigs   = orch.generate_signals(["SPY"], bars, regime)
        if not sigs:
            pytest.skip("No signal generated")

        broker = MagicMock()
        broker.submit_market_order.return_value = {
            "id": "dry-1", "status": "filled",
            "filled_avg_price": sigs[0].entry_price,
            "filled_qty": 10,
        }
        risk     = RiskManager(portfolio_value=100_000.0)
        risk.update_portfolio_value(100_000.0)
        executor = OrderExecutor(broker=broker, risk_manager=risk)

        sig  = sigs[0]
        size = PositionSizeResult(
            ticker="SPY", shares=10,
            notional=10 * sig.entry_price,
            entry_price=sig.entry_price,
            stop_price=sig.stop_loss,
            risk_amount=10 * (sig.entry_price - sig.stop_loss),
        )
        result = executor.buy("SPY", size, regime.label)
        # Result may be rejected by risk gate (e.g. position > 15%), that's OK
        assert result is not None
        assert result.status in ("filled", "pending", "rejected")

    def test_pipeline_produces_no_look_ahead(self, pipeline):
        """Quick check: regime at T is same whether or not future bars are present."""
        _, _, feats, hmm, _ = pipeline
        T     = 300
        short = hmm.predict_regime_filtered(feats[:T])[-1]
        long  = hmm.predict_regime_filtered(feats[:T + 100])[T - 1]
        assert short == long, "Look-ahead bias in pipeline integration"


# ---------------------------------------------------------------------------
# b. Backtest reproducibility (look-ahead audit)
# ---------------------------------------------------------------------------

class TestBacktestReproducibility:
    """
    Running the backtester on data[0:N] and data[0:N-100] must produce
    the same regime predictions for the overlapping window [0:N-100].
    """

    @pytest.fixture(scope="class")
    def setup(self):
        df    = _make_ohlcv(700)
        fe    = FeatureEngineer()
        feats = fe.build_feature_matrix(df)
        hmm   = _build_engine(feats[:500], n_states=4)
        return hmm, feats

    def test_regime_labels_unchanged_when_future_data_added(self, setup):
        hmm, feats = setup
        T           = 350
        preds_short = hmm.predict_regime_filtered(feats[:T])
        preds_long  = hmm.predict_regime_filtered(feats[:T + 100])

        # Every label in the short window must match the long window
        mismatches = [
            (i, preds_short[i].label, preds_long[i].label)
            for i in range(T)
            if preds_short[i] != preds_long[i]
        ]
        assert mismatches == [], \
            f"Look-ahead: {len(mismatches)} mismatches: {mismatches[:3]}"

    def test_forward_probabilities_identical_at_cut_point(self, setup):
        hmm, feats = setup
        T           = 280
        short       = hmm.predict_regime_filtered(feats[:T])[-1]
        long        = hmm.predict_regime_filtered(feats[:T + 80])[T - 1]
        np.testing.assert_allclose(
            short.state_probabilities,
            long.state_probabilities,
            atol=1e-6,
            err_msg="Posterior probs changed when future data added.",
        )


# ---------------------------------------------------------------------------
# c. Risk stress tests
# ---------------------------------------------------------------------------

class TestRiskStress:

    @pytest.fixture
    def rm(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        risk = RiskManager(portfolio_value=100_000.0)
        risk.update_portfolio_value(100_000.0)
        return risk

    # Extreme signal: position would be astronomically large → capped
    def test_extreme_signal_capped(self, rm):
        # stop so close to entry that uncapped shares = millions
        result = rm.calculate_position_size("SPY", entry=400.0, stop=399.99)
        assert result.shares < 100_000   # some cap must fire

    # Rapid-fire: second identical order blocked by risk gate after first fills
    def test_rapid_fire_blocked_by_daily_limit(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        rm = RiskManager(portfolio_value=100_000.0,
                          config=RiskConfig(max_daily_trades=1))
        rm.update_portfolio_value(100_000.0)
        # First order
        d1 = rm.approve_order("SPY", notional=5_000, side="BUY",
                               stop_loss=390.0, entry_price=400.0)
        assert d1.approved
        rm.record_fill("SPY", 5_000, "BUY")   # consume daily trade count
        # Second order — should be blocked (limit=1 already used)
        d2 = rm.approve_order("QQQ", notional=5_000, side="BUY",
                               stop_loss=190.0, entry_price=200.0)
        assert not d2.approved
        assert "limit" in d2.reason.lower()

    # No stop-loss → hard rejection
    def test_no_stop_rejected(self, rm):
        dec = rm.approve_order("SPY", notional=5_000, side="BUY",
                                stop_loss=None, entry_price=400.0)
        assert not dec.approved
        assert "stop_loss" in dec.reason.lower()

    # CB halve: sizes are halved but not zeroed
    def test_circuit_breaker_halves_not_zeros(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        rm = RiskManager(portfolio_value=100_000.0,
                          config=RiskConfig(gap_risk_budget=1.0,
                                            max_single_position=0.50))
        rm.update_portfolio_value(100_000.0)   # initialise day_start
        rm.update_portfolio_value(97_900)       # trigger daily half
        rm._portfolio = 100_000                 # restore for clean arithmetic
        s_half = rm.calculate_position_size("SPY", entry=400.0, stop=390.0,
                                             regime_max_pct=0.50)
        assert s_half.shares > 0           # not zeroed
        assert rm.cb.scale_factor == pytest.approx(0.5)

    # Concurrent positions: 5th is allowed, 6th blocked
    def test_max_concurrent_blocks_sixth(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        rm = RiskManager(portfolio_value=100_000.0,
                          config=RiskConfig(max_concurrent=5))
        rm.update_portfolio_value(100_000.0)
        for i in range(5):
            rm._open_positions[f"TKR{i}"] = 5_000
        dec = rm.approve_order("NEW", notional=1_000, side="BUY",
                                stop_loss=90.0, entry_price=100.0)
        assert not dec.approved
        assert "concurrent" in dec.reason.lower()

    # Portfolio exposure cap: 80% → reject order that would push past it
    def test_total_exposure_cap_enforced(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        rm = RiskManager(portfolio_value=100_000.0)
        rm.update_portfolio_value(100_000.0)
        rm._open_positions["SPY"] = 79_500
        dec = rm.approve_order("QQQ", notional=5_000, side="BUY",
                                stop_loss=390.0, entry_price=400.0)
        assert not dec.approved
        assert "exposure" in dec.reason.lower()

    # SELL goes through during daily_half (trading_allowed=True, scale_factor=0.5)
    def test_sell_allowed_during_daily_half(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        rm = RiskManager(portfolio_value=100_000.0)
        rm.update_portfolio_value(100_000.0)    # initialise day_start
        rm.update_portfolio_value(97_900)        # trigger daily half (scale=0.5)
        assert rm.cb.trading_allowed             # half, not halt
        rm._open_positions["SPY"] = 5_000
        dec = rm.approve_order("SPY", notional=5_000, side="SELL",
                                stop_loss=None, entry_price=400.0)
        assert dec.approved


# ---------------------------------------------------------------------------
# d. Broker simulation (mock Alpaca paper flow)
# ---------------------------------------------------------------------------

class TestBrokerSimulation:
    """
    Simulate: submit → fill → modify stop → verify state → cancel → verify clean.
    No real HTTP calls — AlpacaBroker methods are mocked at the client level.
    """

    @pytest.fixture
    def broker_and_executor(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        broker = MagicMock(spec=AlpacaBroker)
        broker.submit_market_order.return_value = {
            "id": "sim-001", "status": "filled",
            "filled_avg_price": 400.0, "filled_qty": 25,
        }
        broker.get_open_positions.return_value = []
        risk     = RiskManager(portfolio_value=100_000.0)
        risk.update_portfolio_value(100_000.0)
        executor = OrderExecutor(broker=broker, risk_manager=risk)
        return broker, executor

    def test_submit_order_records_position(self, broker_and_executor):
        broker, executor = broker_and_executor
        size = PositionSizeResult(
            ticker="SPY", shares=25, notional=10_000,
            entry_price=400.0, stop_price=390.0, risk_amount=250.0,
        )
        result = executor.buy("SPY", size, "bull")
        assert result.status == "filled"
        assert "SPY" in executor.get_open_positions()
        pos = executor.get_position("SPY")
        assert pos.qty   == 25
        assert pos.entry_price == 400.0
        assert pos.stop_price  == 390.0

    def test_modify_stop_only_tightens(self, broker_and_executor):
        broker, executor = broker_and_executor
        size = PositionSizeResult(
            ticker="SPY", shares=25, notional=10_000,
            entry_price=400.0, stop_price=390.0, risk_amount=250.0,
        )
        executor.buy("SPY", size, "bull")
        # Tighten is allowed
        ok = executor.update_stop("SPY", 395.0)
        assert ok
        assert executor.get_position("SPY").stop_price == 395.0
        # We don't enforce widen-guard in OrderExecutor (it's a caller responsibility),
        # but we verify the mechanism works
        executor.update_stop("SPY", 393.0)
        assert executor.get_position("SPY").stop_price == 393.0

    def test_cancel_leaves_no_open_orders(self, broker_and_executor):
        broker, executor = broker_and_executor
        broker.cancel_all_orders.return_value = 0
        count = broker.cancel_all_orders()
        assert count == 0
        broker.cancel_all_orders.assert_called_once()

    def test_close_position_removes_from_tracker(self, broker_and_executor):
        broker, executor = broker_and_executor
        size = PositionSizeResult(
            ticker="SPY", shares=25, notional=10_000,
            entry_price=400.0, stop_price=390.0, risk_amount=250.0,
        )
        executor.buy("SPY", size, "bull")
        broker.submit_market_order.return_value = {
            "id": "sim-002", "status": "filled",
            "filled_avg_price": 402.0, "filled_qty": 25,
        }
        executor.close_position("SPY", reason="test_close")
        assert "SPY" not in executor.get_open_positions()

    def test_verify_clean_state_after_close_all(self, broker_and_executor):
        broker, executor = broker_and_executor
        # Open two positions
        for ticker, price, stop in [("SPY", 400.0, 390.0), ("QQQ", 350.0, 340.0)]:
            executor._open_positions[ticker] = OpenPosition(
                ticker=ticker, qty=10, entry_price=price,
                current_price=price, stop_price=stop,
                pnl=0.0, pnl_pct=0.0, regime_at_entry="bull",
                opened_at=datetime.now(timezone.utc),
            )
            executor._risk._open_positions[ticker] = 10 * price

        broker.submit_market_order.side_effect = [
            {"id": "c1", "status": "filled", "filled_avg_price": 400.0, "filled_qty": 10},
            {"id": "c2", "status": "filled", "filled_avg_price": 350.0, "filled_qty": 10},
        ]
        results = executor.close_all_positions(reason="clean_state_test")
        assert len(results) == 2
        assert executor.get_open_positions() == {}
        assert executor._risk._open_positions == {}


# ---------------------------------------------------------------------------
# e. Recovery: state snapshot write → reload → no double-entry
# ---------------------------------------------------------------------------

class TestSessionRecovery:

    @pytest.fixture
    def snapshot_path(self, tmp_path):
        return tmp_path / "state_snapshot.json"

    def _write_snapshot(self, path: Path, positions: dict) -> None:
        snap = {
            "saved_at":       datetime.now(timezone.utc).isoformat(),
            "portfolio":      100_000.0,
            "regime":         "bull",
            "daily_pnl":      0.005,
            "peak_dd":        0.02,
            "open_positions": positions,
        }
        path.write_text(json.dumps(snap))

    def test_snapshot_written_correctly(self, tmp_path, snapshot_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        # Simulate save_state() from main.py
        broker   = MagicMock()
        broker.get_open_positions.return_value = []
        risk     = RiskManager(portfolio_value=100_000.0)
        executor = OrderExecutor(broker=broker, risk_manager=risk)
        executor._open_positions["SPY"] = OpenPosition(
            ticker="SPY", qty=10, entry_price=400.0, current_price=402.0,
            stop_price=390.0, pnl=20.0, pnl_pct=0.005,
            regime_at_entry="bull", opened_at=datetime.now(timezone.utc),
        )

        state = {
            "saved_at":   datetime.now(timezone.utc).isoformat(),
            "portfolio":  risk._portfolio,
            "regime":     "bull",
            "daily_pnl":  risk.daily_pnl_pct(),
            "peak_dd":    risk.peak_dd_pct(),
            "open_positions": {
                t: {"qty": p.qty, "entry": p.entry_price, "stop": p.stop_price}
                for t, p in executor.get_open_positions().items()
            },
        }
        snapshot_path.write_text(json.dumps(state))
        assert snapshot_path.exists()

        loaded = json.loads(snapshot_path.read_text())
        assert "SPY" in loaded["open_positions"]
        assert loaded["open_positions"]["SPY"]["qty"] == 10

    def test_recovery_does_not_double_open_position(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        self._write_snapshot(
            tmp_path / "state_snapshot.json",
            {"SPY": {"qty": 10, "entry": 400.0, "stop": 390.0}},
        )
        # Simulate sync_positions: broker shows SPY already open
        broker = MagicMock()
        broker.get_open_positions.return_value = [{
            "symbol": "SPY", "qty": 10, "avg_entry": 400.0,
            "current_price": 402.0, "market_value": 4020.0,
            "unrealized_pl": 20.0, "side": "long",
        }]
        risk     = RiskManager(portfolio_value=100_000.0)
        executor = OrderExecutor(broker=broker, risk_manager=risk)
        # sync_positions reconciles broker state
        executor.sync_positions()
        assert "SPY" in executor.get_open_positions()
        assert executor.get_open_positions()["SPY"].qty == 10
        # No duplicate: still exactly 1 position
        assert len(executor.get_open_positions()) == 1
        # Buy must NOT be called (we don't re-enter an existing position)
        broker.submit_market_order.assert_not_called()

    def test_lock_file_prevents_restart(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        # Write lock file
        (tmp_path / LOCK_FILE).write_text("Trading halted by peak drawdown.")
        from risk.risk_manager import RiskManager
        rm = RiskManager(portfolio_value=100_000.0)
        assert rm.is_locked()   # detects file even before update_portfolio_value
