"""
Unit tests for RiskManager — Phase 5.

Covers:
  Circuit breakers : daily -2%/-3%, weekly -5%/-7%, peak -10% + lock file
  Position sizing  : 1% risk formula, regime/portfolio/gap caps, scale factor
  Order validation : stop-loss mandatory, daily limit, concurrent positions,
                     exposure limits, single-position cap
  Leverage clamp   : max 1.25×, halved when scale_factor=0.5
  Lock file        : written on peak DD, detected by is_locked()
"""

from __future__ import annotations

import os
import pytest

from risk.risk_manager import RiskManager, RiskConfig, LOCK_FILE


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _rm(equity: float = 100_000.0, **cfg_kwargs) -> RiskManager:
    cfg = RiskConfig(**cfg_kwargs) if cfg_kwargs else RiskConfig()
    rm  = RiskManager(portfolio_value=equity, config=cfg)
    # Initialise daily/weekly anchors by calling update once
    rm.update_portfolio_value(equity)
    return rm


# ---------------------------------------------------------------------------
# 1. Circuit breakers
# ---------------------------------------------------------------------------

class TestCircuitBreakers:

    def test_daily_half_at_2pct(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        rm = _rm(100_000)
        rm.update_portfolio_value(97_900)   # -2.1% daily
        assert rm.cb.daily_half_active
        assert rm.cb.scale_factor == pytest.approx(0.5)

    def test_daily_close_at_3pct(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        rm = _rm(100_000)
        rm.update_portfolio_value(96_900)   # -3.1% daily
        assert rm.cb.daily_halt_active
        assert not rm.cb.trading_allowed

    def test_weekly_half_at_5pct(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        rm = _rm(100_000)
        rm._week_start = 100_000
        rm._day_start  = 95_900  # keep daily DD ~1% so daily CBs don't interfere
        rm.update_portfolio_value(94_900)   # -5.1% weekly, -~1.05% daily
        assert rm.cb.weekly_half_active
        assert rm.cb.scale_factor == pytest.approx(0.5)

    def test_weekly_close_at_7pct(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        rm = _rm(100_000)
        rm._week_start = 100_000
        rm.update_portfolio_value(92_900)   # -7.1% weekly
        assert rm.cb.weekly_halt_active
        assert not rm.cb.trading_allowed

    def test_peak_lock_at_10pct(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        rm = _rm(100_000)
        rm._peak = 100_000
        rm.update_portfolio_value(89_900)   # -10.1% from peak
        assert rm.cb.peak_locked
        assert rm.is_locked()
        assert os.path.exists(LOCK_FILE)

    def test_lock_file_written_on_peak_lock(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        rm = _rm(100_000)
        rm._peak = 100_000
        rm.update_portfolio_value(89_000)
        assert os.path.exists(LOCK_FILE)
        content = open(LOCK_FILE).read()
        assert "Trading halted" in content
        assert "Drawdown" in content

    def test_scale_factor_resets_to_1_after_daily_reset(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        from datetime import date, timedelta
        rm = _rm(100_000)
        rm.update_portfolio_value(97_900)   # trigger daily half
        assert rm.cb.scale_factor == pytest.approx(0.5)
        # Simulate new day
        rm._last_date = date.today() - timedelta(days=1)
        rm.update_portfolio_value(97_900)   # same equity, but new day
        assert rm.cb.scale_factor == pytest.approx(1.0)


# ---------------------------------------------------------------------------
# 2. Position sizing
# ---------------------------------------------------------------------------

class TestPositionSizing:

    def test_basic_1pct_risk_formula(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        # Disable portfolio and gap caps so only the 1% formula determines sizing
        rm     = _rm(100_000, max_single_position=0.50, gap_risk_budget=1.0)
        result = rm.calculate_position_size("SPY", entry=400.0, stop=390.0,
                                             regime_max_pct=0.50)
        # Risk = $1000 (1% of 100k) / $10 (entry-stop) = 100 shares
        assert result.shares == 100
        assert result.risk_amount == pytest.approx(1000.0, rel=0.01)

    def test_portfolio_max_cap_15pct(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        rm     = _rm(100_000)
        # Very tight stop → huge uncapped size
        result = rm.calculate_position_size("SPY", entry=400.0, stop=399.9,
                                             regime_max_pct=0.50)
        assert result.notional <= 100_000 * 0.15 + 1.0
        assert result.portfolio_capped

    def test_regime_max_cap(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        rm     = _rm(100_000)
        result = rm.calculate_position_size("SPY", entry=400.0, stop=399.0,
                                             regime_max_pct=0.05)
        assert result.notional <= 100_000 * 0.05 + 1.0
        assert result.regime_capped

    def test_gap_risk_cap(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        rm     = _rm(100_000)
        # entry=10, stop=9 → risk_per_share=1.0, shares_raw=1000, notional=$10k (<15% cap)
        # gap cap: 3×$1 = $3/share; budget 2%×100k = $2000 → max_gap_shares=666
        result = rm.calculate_position_size("SPY", entry=10.0, stop=9.0,
                                             regime_max_pct=0.50)
        assert result.shares <= 667
        assert result.overnight_capped

    def test_scale_factor_halves_shares(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        rm = _rm(100_000, max_single_position=0.50, gap_risk_budget=1.0)
        rm.update_portfolio_value(97_900)  # trigger daily half (scale_factor=0.5)
        rm._portfolio = 100_000           # restore for clean arithmetic
        result = rm.calculate_position_size("SPY", entry=400.0, stop=390.0,
                                             regime_max_pct=0.50)
        assert result.shares == 50   # 100 halved to 50

    def test_minimum_notional_returns_zero_shares(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        rm = _rm(500)   # tiny portfolio
        result = rm.calculate_position_size("SPY", entry=400.0, stop=399.0)
        assert result.shares == 0   # 1% of $500 = $5 → 0.0125 shares → $0 notional < $100

    def test_stop_above_entry_raises(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        rm = _rm(100_000)
        with pytest.raises(ValueError):
            rm.calculate_position_size("SPY", entry=390.0, stop=400.0)


# ---------------------------------------------------------------------------
# 3. Order validation
# ---------------------------------------------------------------------------

class TestOrderValidation:

    def test_approved_when_healthy(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        rm  = _rm(100_000)
        dec = rm.approve_order("SPY", notional=5_000, side="BUY",
                                stop_loss=390.0, entry_price=400.0)
        assert dec.approved

    def test_rejected_when_locked(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        rm = _rm(100_000)
        rm._peak = 100_000
        rm.update_portfolio_value(89_000)   # triggers lock
        dec = rm.approve_order("SPY", notional=5_000, side="BUY",
                                stop_loss=390.0, entry_price=400.0)
        assert not dec.approved
        assert "locked" in dec.reason.lower() or "halted" in dec.reason.lower()

    def test_rejected_without_stop_loss(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        rm  = _rm(100_000)
        dec = rm.approve_order("SPY", notional=5_000, side="BUY",
                                stop_loss=None, entry_price=400.0)
        assert not dec.approved
        assert "stop_loss" in dec.reason.lower()

    def test_rejected_when_daily_trade_limit_reached(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        rm = _rm(100_000, max_daily_trades=2)
        rm._daily_trades = 2
        dec = rm.approve_order("SPY", notional=1_000, side="BUY",
                                stop_loss=390.0, entry_price=400.0)
        assert not dec.approved
        assert "limit" in dec.reason.lower()

    def test_rejected_when_max_concurrent_reached(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        rm = _rm(100_000, max_concurrent=2)
        rm._open_positions = {"SPY": 5000, "QQQ": 5000}
        dec = rm.approve_order("IWM", notional=1_000, side="BUY",
                                stop_loss=190.0, entry_price=200.0)
        assert not dec.approved
        assert "concurrent" in dec.reason.lower()

    def test_rejected_when_total_exposure_exceeded(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        rm = _rm(100_000)
        rm._open_positions = {"SPY": 79_000}   # already at 79% of 100k
        dec = rm.approve_order("QQQ", notional=2_000, side="BUY",
                                stop_loss=390.0, entry_price=400.0)
        assert not dec.approved
        assert "exposure" in dec.reason.lower()

    def test_rejected_when_single_position_too_large(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        rm  = _rm(100_000)
        dec = rm.approve_order("SPY", notional=16_000, side="BUY",
                                stop_loss=390.0, entry_price=400.0)
        assert not dec.approved
        assert "limit" in dec.reason.lower() or "exceed" in dec.reason.lower()

    def test_sell_always_allowed_when_trading_on(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        rm = _rm(100_000)
        rm._open_positions = {"SPY": 5000}
        dec = rm.approve_order("SPY", notional=5_000, side="SELL",
                                stop_loss=None, entry_price=400.0)
        assert dec.approved


# ---------------------------------------------------------------------------
# 4. Leverage validation
# ---------------------------------------------------------------------------

class TestLeverageValidation:

    def test_leverage_clamped_to_max(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        rm = _rm(100_000)
        assert rm.validate_leverage(2.0) == pytest.approx(1.25)

    def test_leverage_halved_when_cb_half(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        rm = _rm(100_000)
        rm.update_portfolio_value(97_900)  # trigger daily half
        assert rm.validate_leverage(1.25) == pytest.approx(0.625)
