"""
Structured JSON logging for regime_trader.

Four rotating files (10 MB / 30 days each):
  logs/main.log    — all events
  logs/trades.log  — fills and order outcomes
  logs/alerts.log  — circuit breakers and warnings
  logs/regime.log  — every regime prediction + flicker status

Every entry includes: timestamp, regime, probability, equity, positions, daily_pnl.
"""

from __future__ import annotations

import json
import logging
import logging.handlers
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional


# ---------------------------------------------------------------------------
# JSON formatter
# ---------------------------------------------------------------------------

class _JSONFormatter(logging.Formatter):
    """Emit each log record as a single-line JSON object."""

    def __init__(self, extra_fields: Optional[dict] = None) -> None:
        super().__init__()
        self._extra = extra_fields or {}

    def format(self, record: logging.LogRecord) -> str:
        doc: dict[str, Any] = {
            "ts":      datetime.now(timezone.utc).isoformat(),
            "level":   record.levelname,
            "logger":  record.name,
            "message": record.getMessage(),
        }
        doc.update(self._extra)
        if record.exc_info:
            doc["exc"] = self.formatException(record.exc_info)
        # Merge any extra fields attached to the record
        for key, val in record.__dict__.items():
            if key.startswith("_rt_"):   # convention: _rt_<field>
                doc[key[4:]] = val
        return json.dumps(doc, default=str)


# ---------------------------------------------------------------------------
# Public logger factory
# ---------------------------------------------------------------------------

_loggers: dict[str, logging.Logger] = {}


def _make_logger(name: str, filename: str, log_dir: str = "logs") -> logging.Logger:
    if name in _loggers:
        return _loggers[name]

    Path(log_dir).mkdir(parents=True, exist_ok=True)
    lg = logging.getLogger(f"rt.{name}")
    lg.propagate = False
    lg.setLevel(logging.DEBUG)

    handler = logging.handlers.RotatingFileHandler(
        f"{log_dir}/{filename}",
        maxBytes    = 10 * 1024 * 1024,
        backupCount = 30,
        encoding    = "utf-8",
    )
    handler.setFormatter(_JSONFormatter())
    lg.addHandler(handler)
    _loggers[name] = lg
    return lg


def get_main_logger   (log_dir: str = "logs") -> logging.Logger:
    return _make_logger("main",   "main.log",   log_dir)

def get_trades_logger (log_dir: str = "logs") -> logging.Logger:
    return _make_logger("trades", "trades.log", log_dir)

def get_alerts_logger (log_dir: str = "logs") -> logging.Logger:
    return _make_logger("alerts", "alerts.log", log_dir)

def get_regime_logger (log_dir: str = "logs") -> logging.Logger:
    return _make_logger("regime", "regime.log", log_dir)


# ---------------------------------------------------------------------------
# Structured event helpers
# ---------------------------------------------------------------------------

def log_regime_event(regime: str, probability: float,
                      equity: float, positions: dict,
                      daily_pnl: float, flicker_rate: float,
                      is_confirmed: bool) -> None:
    lg = get_regime_logger()
    rec = logging.makeLogRecord({
        "level": logging.INFO, "name": "rt.regime",
        "msg": f"regime={regime} prob={probability:.2%}",
        "_rt_regime":      regime,
        "_rt_probability": round(probability, 4),
        "_rt_equity":      round(equity, 2),
        "_rt_positions":   positions,
        "_rt_daily_pnl":   round(daily_pnl, 4),
        "_rt_flicker_rate":round(flicker_rate, 4),
        "_rt_confirmed":   is_confirmed,
    })
    lg.handle(rec)


def log_trade_event(order_id: str, ticker: str, side: str,
                     qty: int, price: float, status: str,
                     regime: str, pnl: float = 0.0) -> None:
    lg = get_trades_logger()
    rec = logging.makeLogRecord({
        "level": logging.INFO, "name": "rt.trades",
        "msg": f"{side.upper()} {qty} {ticker} @ {price:.2f} [{status}]",
        "_rt_order_id": order_id,
        "_rt_ticker":   ticker,
        "_rt_side":     side,
        "_rt_qty":      qty,
        "_rt_price":    round(price, 4),
        "_rt_status":   status,
        "_rt_regime":   regime,
        "_rt_pnl":      round(pnl, 2),
    })
    lg.handle(rec)


def log_alert_event(level: str, subject: str, body: str) -> None:
    lg = get_alerts_logger()
    rec = logging.makeLogRecord({
        "level": getattr(logging, level, logging.WARNING),
        "name": "rt.alerts",
        "msg": f"{subject}: {body}",
        "_rt_subject": subject,
        "_rt_body":    body,
    })
    lg.handle(rec)
