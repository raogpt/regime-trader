"""
Monitoring alerts — thin re-export of utils.alerts with structured logging.

Triggers:
  regime_change, circuit_breaker, large_pnl, data_feed_down,
  api_lost, hmm_retrained, flicker_exceeded

Rate limit: 1 per event type per 15 minutes.
Delivery  : console, logs/alerts.log, email (opt), webhook (opt).
"""

from __future__ import annotations

from monitoring.logger import log_alert_event
from utils.alerts import (
    AlertLevel,
    AlertDispatcher,
    alert_circuit_breaker,
    alert_regime_change,
    alert_order_filled,
    alert_lock_file_created,
    alert_data_feed_down,
    alert_hmm_retrained,
    _dispatcher,
)

__all__ = [
    "AlertLevel",
    "AlertDispatcher",
    "alert_circuit_breaker",
    "alert_regime_change",
    "alert_order_filled",
    "alert_lock_file_created",
    "alert_data_feed_down",
    "alert_hmm_retrained",
    "alert_large_pnl",
    "alert_api_lost",
    "alert_flicker_exceeded",
]


def alert_large_pnl(ticker: str, pnl_pct: float, threshold: float = 0.05) -> None:
    """Fire when a single position P&L exceeds ±threshold."""
    if abs(pnl_pct) < threshold:
        return
    sign = "+" if pnl_pct >= 0 else ""
    _dispatcher.send(
        AlertLevel.WARNING,
        subject    = f"Large P&L: {ticker} {sign}{pnl_pct:.1%}",
        body       = f"Position moved {sign}{pnl_pct:.1%} from entry.",
        event_type = f"large_pnl_{ticker}",
    )
    log_alert_event("WARNING", f"Large P&L: {ticker}", f"{sign}{pnl_pct:.1%}")


def alert_api_lost(error: str) -> None:
    _dispatcher.send(
        AlertLevel.CRITICAL,
        subject    = "Alpaca API connection lost",
        body       = error,
        event_type = "api_lost",
    )
    log_alert_event("CRITICAL", "API lost", error)


def alert_flicker_exceeded(rate: int, window: int) -> None:
    _dispatcher.send(
        AlertLevel.WARNING,
        subject    = f"Regime flicker: {rate}/{window} transitions",
        body       = "Uncertainty mode activated — position sizes halved.",
        event_type = "flicker_exceeded",
    )
    log_alert_event("WARNING", "Flicker exceeded", f"{rate}/{window}")
