"""
Alpaca broker API wrapper.

Handles authentication, account info, and raw REST calls via alpaca-py.
Credentials are loaded exclusively from environment variables — never
hardcoded here or passed through Claude Code.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Optional

from config.credentials import get_alpaca_credentials

logger = logging.getLogger(__name__)


@dataclass
class AccountInfo:
    account_id:      str
    equity:          float
    cash:            float
    buying_power:    float
    portfolio_value: float
    is_paper:        bool
    status:          str


class AlpacaBroker:
    """
    Thin wrapper around the Alpaca Trading REST API (alpaca-py SDK).
    Used by OrderExecutor for all order and account operations.
    """

    def __init__(self) -> None:
        creds             = get_alpaca_credentials()
        self._api_key     = creds["api_key"]
        self._secret_key  = creds["secret_key"]
        self._base_url    = creds["base_url"]
        self._client      = None   # alpaca.trading.client.TradingClient

    # ------------------------------------------------------------------
    # Connection
    # ------------------------------------------------------------------

    def connect(self) -> None:
        """Initialise the Alpaca REST client and verify credentials."""
        from alpaca.trading.client import TradingClient
        paper = "paper" in self._base_url.lower()
        self._client = TradingClient(
            api_key    = self._api_key,
            secret_key = self._secret_key,
            paper      = paper,
            # alpaca-py constructs its own URLs; base_url is informational only
        )
        # Lightweight connectivity check
        acct = self._client.get_account()
        logger.info("Alpaca connected | account=%s status=%s paper=%s",
                    acct.id, acct.status, paper)

    def is_connected(self) -> bool:
        return self._client is not None

    def ping(self) -> bool:
        """Make a lightweight API call to verify connectivity."""
        try:
            self._client.get_account()
            return True
        except Exception as exc:
            logger.warning("Alpaca ping failed: %s", exc)
            return False

    # ------------------------------------------------------------------
    # Account
    # ------------------------------------------------------------------

    def get_account(self) -> AccountInfo:
        acct = self._client.get_account()
        return AccountInfo(
            account_id      = str(acct.id),
            equity          = float(acct.equity),
            cash            = float(acct.cash),
            buying_power    = float(acct.buying_power),
            portfolio_value = float(acct.portfolio_value),
            is_paper        = "paper" in self._base_url.lower(),
            status          = str(acct.status),
        )

    def get_buying_power(self) -> float:
        return float(self._client.get_account().buying_power)

    def get_portfolio_value(self) -> float:
        return float(self._client.get_account().portfolio_value)

    # ------------------------------------------------------------------
    # Positions
    # ------------------------------------------------------------------

    def get_open_positions(self) -> list[dict]:
        positions = self._client.get_all_positions()
        return [self._position_to_dict(p) for p in positions]

    def get_position(self, ticker: str) -> Optional[dict]:
        try:
            p = self._client.get_open_position(ticker)
            return self._position_to_dict(p)
        except Exception:
            return None

    @staticmethod
    def _position_to_dict(p) -> dict:
        return {
            "symbol":        str(p.symbol),
            "qty":           int(p.qty),
            "avg_entry":     float(p.avg_entry_price),
            "current_price": float(p.current_price),
            "market_value":  float(p.market_value),
            "unrealized_pl": float(p.unrealized_pl),
            "side":          str(p.side),
        }

    # ------------------------------------------------------------------
    # Orders
    # ------------------------------------------------------------------

    def submit_market_order(self, ticker: str, qty: int, side: str) -> dict:
        """
        Submit a market order.  side = 'buy' | 'sell'.
        Returns the Alpaca order object as a plain dict.
        """
        from alpaca.trading.requests import MarketOrderRequest
        from alpaca.trading.enums   import OrderSide, TimeInForce

        req = MarketOrderRequest(
            symbol       = ticker,
            qty          = qty,
            side         = OrderSide.BUY if side.lower() == "buy" else OrderSide.SELL,
            time_in_force= TimeInForce.DAY,
        )
        order = self._client.submit_order(req)
        logger.info("Market order submitted | %s %s %d | id=%s",
                    side.upper(), ticker, qty, order.id)
        return self._order_to_dict(order)

    def submit_limit_order(self, ticker: str, qty: int, side: str,
                            limit_price: float) -> dict:
        from alpaca.trading.requests import LimitOrderRequest
        from alpaca.trading.enums   import OrderSide, TimeInForce

        req = LimitOrderRequest(
            symbol        = ticker,
            qty           = qty,
            side          = OrderSide.BUY if side.lower() == "buy" else OrderSide.SELL,
            time_in_force = TimeInForce.DAY,
            limit_price   = round(limit_price, 2),
        )
        order = self._client.submit_order(req)
        logger.info("Limit order submitted | %s %s %d @ %.2f | id=%s",
                    side.upper(), ticker, qty, limit_price, order.id)
        return self._order_to_dict(order)

    def cancel_order(self, order_id: str) -> bool:
        try:
            self._client.cancel_order_by_id(order_id)
            logger.info("Order cancelled | id=%s", order_id)
            return True
        except Exception as exc:
            logger.warning("Failed to cancel order %s: %s", order_id, exc)
            return False

    def cancel_all_orders(self) -> int:
        cancelled = self._client.cancel_orders()
        count = len(cancelled) if cancelled else 0
        logger.info("All orders cancelled | count=%d", count)
        return count

    def close_position(self, ticker: str) -> dict:
        order = self._client.close_position(ticker)
        logger.info("Position closed | ticker=%s order_id=%s", ticker, order.id)
        return self._order_to_dict(order)

    def close_all_positions(self) -> int:
        responses = self._client.close_all_positions(cancel_orders=True)
        count = len(responses) if responses else 0
        logger.info("All positions closed | count=%d", count)
        return count

    # ------------------------------------------------------------------
    # Clock
    # ------------------------------------------------------------------

    def get_clock(self) -> dict:
        clock = self._client.get_clock()
        return {
            "is_open":    clock.is_open,
            "next_open":  clock.next_open.isoformat(),
            "next_close": clock.next_close.isoformat(),
            "timestamp":  clock.timestamp.isoformat(),
        }

    def is_market_open(self) -> bool:
        return self._client.get_clock().is_open

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    @staticmethod
    def _order_to_dict(order) -> dict:
        return {
            "id":               str(order.id),
            "symbol":           str(order.symbol),
            "qty":              int(order.qty or 0),
            "side":             str(order.side),
            "type":             str(order.type),
            "status":           str(order.status),
            "filled_qty":       int(order.filled_qty or 0),
            "filled_avg_price": float(order.filled_avg_price or 0.0),
            "submitted_at":     order.submitted_at.isoformat() if order.submitted_at else "",
        }
