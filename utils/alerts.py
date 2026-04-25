"""
Alert dispatcher for critical trading events.

Delivery: console (always) + rotating log file + email (optional) + webhook (optional).
Rate limit: 1 alert per event type per 15 minutes to prevent spam.
"""

from __future__ import annotations

import json
import logging
import logging.handlers
import os
import time
import urllib.request
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Optional

from config import settings

logger = logging.getLogger(__name__)

_RATE_LIMIT_SECONDS = 900   # 15 minutes
_last_sent: dict[str, float] = {}   # event_type → last send timestamp

# Dedicated alerts log (separate from main.log)
_alert_log: Optional[logging.Logger] = None


def _get_alert_logger() -> logging.Logger:
    global _alert_log
    if _alert_log is None:
        Path("logs").mkdir(exist_ok=True)
        _alert_log = logging.getLogger("alerts")
        _alert_log.propagate = False
        h = logging.handlers.RotatingFileHandler(
            "logs/alerts.log", maxBytes=10 * 1024 * 1024, backupCount=30)
        h.setFormatter(logging.Formatter("%(asctime)s | %(message)s"))
        _alert_log.addHandler(h)
        _alert_log.setLevel(logging.INFO)
    return _alert_log


class AlertLevel(Enum):
    INFO     = "INFO"
    WARNING  = "WARNING"
    CRITICAL = "CRITICAL"


class AlertDispatcher:
    """Routes alerts to configured channels with per-type rate limiting."""

    def send(self, level: AlertLevel, subject: str, body: str,
             event_type: str = "") -> None:
        key = event_type or subject
        now = time.monotonic()
        if now - _last_sent.get(key, 0.0) < _RATE_LIMIT_SECONDS:
            logger.debug("Alert rate-limited | %s", key)
            return
        _last_sent[key] = now

        msg = f"[{level.value}] {subject} — {body}"
        logger.log(
            logging.CRITICAL if level == AlertLevel.CRITICAL else
            logging.WARNING  if level == AlertLevel.WARNING  else
            logging.INFO,
            "ALERT: %s", msg,
        )
        _get_alert_logger().info("%s | %s | %s", level.value, subject, body)

        if settings.ALERT_EMAIL_ENABLED:
            self._send_email(subject, body)
        if settings.ALERT_WEBHOOK_ENABLED:
            self._send_webhook(subject, body)

    def _send_email(self, subject: str, body: str) -> None:
        import smtplib
        from email.mime.text import MIMEText
        try:
            host  = os.environ.get("SMTP_HOST", "")
            port  = int(os.environ.get("SMTP_PORT", "587"))
            user  = os.environ.get("SMTP_USER", "")
            pwd   = os.environ.get("SMTP_PASSWORD", "")
            to    = os.environ.get("ALERT_EMAIL_TO", user)
            msg   = MIMEText(body)
            msg["Subject"] = f"[regime_trader] {subject}"
            msg["From"]    = user
            msg["To"]      = to
            with smtplib.SMTP(host, port) as s:
                s.starttls()
                s.login(user, pwd)
                s.send_message(msg)
        except Exception as exc:
            logger.warning("Email alert failed: %s", exc)

    def _send_webhook(self, subject: str, body: str) -> None:
        url = os.environ.get("ALERT_WEBHOOK_URL", "")
        if not url:
            return
        try:
            payload = json.dumps({"text": f"*{subject}*\n{body}"}).encode()
            req = urllib.request.Request(url, data=payload,
                                          headers={"Content-Type": "application/json"})
            urllib.request.urlopen(req, timeout=5)
        except Exception as exc:
            logger.warning("Webhook alert failed: %s", exc)


# ---------------------------------------------------------------------------
# Module-level convenience functions
# ---------------------------------------------------------------------------

_dispatcher = AlertDispatcher()


def alert_circuit_breaker(level: str, pnl_pct: float) -> None:
    _dispatcher.send(
        AlertLevel.CRITICAL,
        subject    = f"Circuit breaker fired: {level}",
        body       = f"P&L drawdown: {pnl_pct:+.2f}%",
        event_type = f"cb_{level}",
    )


def alert_regime_change(previous: str, current: str, confidence: float) -> None:
    _dispatcher.send(
        AlertLevel.INFO,
        subject    = f"Regime change: {previous} → {current}",
        body       = f"Confidence: {confidence:.0%}",
        event_type = "regime_change",
    )


def alert_order_filled(ticker: str, side: str, qty: int, price: float) -> None:
    _dispatcher.send(
        AlertLevel.INFO,
        subject    = f"Order filled: {side.upper()} {qty} {ticker} @ ${price:.2f}",
        body       = "",
        event_type = f"fill_{ticker}",
    )


def alert_lock_file_created(reason: str) -> None:
    _dispatcher.send(
        AlertLevel.CRITICAL,
        subject    = "Bot HALTED — trading_halted.lock created",
        body       = reason,
        event_type = "peak_lock",
    )


def alert_data_feed_down(ticker: str) -> None:
    _dispatcher.send(
        AlertLevel.WARNING,
        subject    = f"Data feed down: {ticker}",
        body       = "Signals paused; stops remain active.",
        event_type = f"feed_down_{ticker}",
    )


def alert_hmm_retrained(n_states: int, bic: float) -> None:
    _dispatcher.send(
        AlertLevel.INFO,
        subject    = f"HMM retrained: {n_states} states (BIC={bic:.0f})",
        body       = f"Timestamp: {datetime.now(timezone.utc).isoformat()}",
        event_type = "hmm_retrain",
    )
