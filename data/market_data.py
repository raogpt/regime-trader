"""
Market data provider — alpaca-py SDK.

Historical data : StockHistoricalDataClient
Live streaming  : StockDataStream (WebSocket)
Gaps handled    : weekends, holidays, and halts silently skipped.
"""

from __future__ import annotations

import logging
import threading
import time
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Callable, Optional

import pandas as pd

logger = logging.getLogger(__name__)

_TF_MAP = {
    "1Min":  "1Min",
    "5Min":  "5Min",
    "15Min": "15Min",
    "1Hour": "1Hour",
    "1Day":  "1Day",
}


@dataclass
class Bar:
    ticker:    str
    timestamp: datetime
    open:      float
    high:      float
    low:       float
    close:     float
    volume:    float
    vwap:      float = 0.0


class MarketDataProvider:
    """
    Wraps the Alpaca data API for historical and live bar retrieval.
    All DataFrames are returned with lower-case column names and a UTC index.
    """

    def __init__(self, api_key: str = "", secret_key: str = "",
                  api_client=None) -> None:
        self._api_key    = api_key
        self._secret_key = secret_key
        self._trading_client = api_client   # TradingClient (for clock)
        self._data_client    = None         # StockHistoricalDataClient
        self._stream         = None         # StockDataStream
        self._stream_thread: Optional[threading.Thread] = None
        self._latest_bars:   dict[str, Bar] = {}

    # ------------------------------------------------------------------
    # Connection
    # ------------------------------------------------------------------

    def connect(self) -> None:
        from alpaca.data.historical import StockHistoricalDataClient
        self._data_client = StockHistoricalDataClient(
            api_key    = self._api_key or None,
            secret_key = self._secret_key or None,
        )
        logger.info("MarketDataProvider connected")

    # ------------------------------------------------------------------
    # Historical data
    # ------------------------------------------------------------------

    def get_historical_bars(self, ticker: str, timeframe: str,
                             start: datetime,
                             end: Optional[datetime] = None,
                             limit: Optional[int] = None) -> pd.DataFrame:
        from alpaca.data.requests   import StockBarsRequest
        from alpaca.data.timeframe  import TimeFrame, TimeFrameUnit

        from alpaca.data.enums import DataFeed
        tf_obj = self._parse_timeframe(timeframe)
        req    = StockBarsRequest(
            symbol_or_symbols = ticker,
            timeframe         = tf_obj,
            start             = start,
            end               = end or datetime.now(timezone.utc),
            limit             = limit,
            feed              = DataFeed.IEX,   # free-tier compatible
        )
        bars = self._data_client.get_stock_bars(req)
        df   = bars.df if hasattr(bars, "df") else bars[ticker].df
        df   = df.reset_index()
        df.columns = [c.lower() for c in df.columns]
        df   = df.rename(columns={"timestamp": "datetime"})
        df   = df[["datetime", "open", "high", "low", "close", "volume", "vwap"]]
        df   = df.set_index("datetime")
        if df.index.tz is None:
            df.index = df.index.tz_localize("UTC")
        logger.debug("Historical bars fetched | %s %s rows=%d", ticker, timeframe, len(df))
        return df

    def get_daily_bars(self, ticker: str, n_days: int) -> pd.DataFrame:
        start = datetime.now(timezone.utc) - timedelta(days=n_days + 10)
        df    = self.get_historical_bars(ticker, "1Day", start)
        return df.tail(n_days)

    # ------------------------------------------------------------------
    # Latest snapshot
    # ------------------------------------------------------------------

    def get_latest_bar(self, ticker: str, timeframe: str = "5Min") -> Optional[Bar]:
        if ticker in self._latest_bars:
            return self._latest_bars[ticker]
        # Fallback: fetch last 2 bars and return the last
        try:
            start = datetime.now(timezone.utc) - timedelta(minutes=30)
            df    = self.get_historical_bars(ticker, timeframe, start, limit=2)
            if len(df) == 0:
                return None
            row = df.iloc[-1]
            return Bar(
                ticker    = ticker,
                timestamp = df.index[-1].to_pydatetime(),
                open=float(row["open"]), high=float(row["high"]),
                low=float(row["low"]),  close=float(row["close"]),
                volume=float(row["volume"]),
                vwap  = float(row.get("vwap", 0.0)),
            )
        except Exception as exc:
            logger.warning("get_latest_bar failed for %s: %s", ticker, exc)
            return None

    def get_latest_quote(self, ticker: str) -> Optional[dict]:
        try:
            from alpaca.data.requests import StockLatestQuoteRequest
            req   = StockLatestQuoteRequest(symbol_or_symbols=ticker)
            quote = self._data_client.get_stock_latest_quote(req)
            q     = quote[ticker]
            return {"bid": float(q.bid_price), "ask": float(q.ask_price),
                    "spread": float(q.ask_price - q.bid_price)}
        except Exception as exc:
            logger.warning("get_latest_quote failed for %s: %s", ticker, exc)
            return None

    def get_snapshot(self, ticker: str) -> Optional[dict]:
        try:
            from alpaca.data.requests import StockSnapshotRequest
            req  = StockSnapshotRequest(symbol_or_symbols=ticker)
            snap = self._data_client.get_stock_snapshot(req)
            s    = snap[ticker]
            return {
                "symbol":        ticker,
                "latest_trade":  float(s.latest_trade.price),
                "daily_bar":     {
                    "open":   float(s.daily_bar.open),
                    "high":   float(s.daily_bar.high),
                    "low":    float(s.daily_bar.low),
                    "close":  float(s.daily_bar.close),
                    "volume": float(s.daily_bar.volume),
                },
                "prev_daily_close": float(s.previous_daily_bar.close),
            }
        except Exception as exc:
            logger.warning("get_snapshot failed for %s: %s", ticker, exc)
            return None

    # ------------------------------------------------------------------
    # Live streaming (WebSocket)
    # ------------------------------------------------------------------

    def subscribe_bars(self, tickers: list[str],
                        callback: Callable[[Bar], None],
                        timeframe: str = "5Min") -> None:
        from alpaca.data.live import StockDataStream

        self._stream = StockDataStream(
            api_key    = self._api_key,
            secret_key = self._secret_key,
        )

        async def _on_bar(bar) -> None:
            b = Bar(
                ticker    = bar.symbol,
                timestamp = bar.timestamp,
                open      = float(bar.open),
                high      = float(bar.high),
                low       = float(bar.low),
                close     = float(bar.close),
                volume    = float(bar.volume),
                vwap      = float(getattr(bar, "vwap", 0.0)),
            )
            self._latest_bars[bar.symbol] = b
            try:
                callback(b)
            except Exception as exc:
                logger.error("Bar callback error: %s", exc)

        self._stream.subscribe_bars(_on_bar, *tickers)

        def _run_with_backoff(stream, max_retries: int = 12) -> None:
            """Run the WebSocket stream with exponential backoff on transient errors."""
            delay = 5.0
            for attempt in range(max_retries):
                try:
                    stream.run()
                    break   # clean exit (e.g. unsubscribe_bars called)
                except Exception as exc:
                    msg = str(exc).lower()
                    if "connection limit" in msg:
                        wait = min(delay * (2 ** attempt), 300)
                        logger.warning(
                            "WebSocket: connection limit exceeded — "
                            "waiting %.0fs before retry %d/%d",
                            wait, attempt + 1, max_retries,
                        )
                        time.sleep(wait)
                    elif attempt < max_retries - 1:
                        wait = min(delay * (2 ** attempt), 120)
                        logger.warning(
                            "WebSocket error (%s) — retry %d/%d in %.0fs",
                            exc, attempt + 1, max_retries, wait,
                        )
                        time.sleep(wait)
                    else:
                        logger.error("WebSocket permanently failed after %d retries: %s",
                                     max_retries, exc)

        self._stream_thread = threading.Thread(
            target=_run_with_backoff, args=(self._stream,),
            daemon=True, name="alpaca-stream")
        self._stream_thread.start()
        logger.info("Bar stream started | tickers=%s tf=%s", tickers, timeframe)

    def subscribe_quotes(self, tickers: list[str],
                          callback: Callable[[dict], None]) -> None:
        if self._stream is None:
            logger.warning("subscribe_quotes: no active stream")
            return

        async def _on_quote(quote) -> None:
            try:
                callback({"symbol": quote.symbol,
                           "bid": float(quote.bid_price),
                           "ask": float(quote.ask_price)})
            except Exception as exc:
                logger.error("Quote callback error: %s", exc)

        self._stream.subscribe_quotes(_on_quote, *tickers)

    def unsubscribe_bars(self) -> None:
        if self._stream:
            try:
                self._stream.stop()
                logger.info("Bar stream stopped")
            except Exception as exc:
                logger.warning("Error stopping stream: %s", exc)
        self._stream = None

    # ------------------------------------------------------------------
    # Market hours (uses TradingClient clock if available)
    # ------------------------------------------------------------------

    def is_market_open(self) -> bool:
        try:
            if self._trading_client:
                return self._trading_client.get_clock().is_open
        except Exception:
            pass
        return False

    def next_market_open(self) -> datetime:
        try:
            if self._trading_client:
                return self._trading_client.get_clock().next_open
        except Exception:
            pass
        # Fallback: next 9:30 ET
        from zoneinfo import ZoneInfo
        et  = ZoneInfo("America/New_York")
        now = datetime.now(et)
        nxt = now.replace(hour=9, minute=30, second=0, microsecond=0)
        if nxt <= now:
            nxt += timedelta(days=1)
        return nxt.astimezone(timezone.utc)

    def seconds_until_market_open(self) -> int:
        if self.is_market_open():
            return 0
        nxt   = self.next_market_open()
        delta = (nxt - datetime.now(timezone.utc)).total_seconds()
        return max(0, int(delta))

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _parse_timeframe(tf: str):
        from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
        mapping = {
            "1Min":  TimeFrame(1,  TimeFrameUnit.Minute),
            "5Min":  TimeFrame(5,  TimeFrameUnit.Minute),
            "15Min": TimeFrame(15, TimeFrameUnit.Minute),
            "1Hour": TimeFrame(1,  TimeFrameUnit.Hour),
            "1Day":  TimeFrame(1,  TimeFrameUnit.Day),
        }
        if tf not in mapping:
            raise ValueError(f"Unsupported timeframe: {tf!r}. Use {list(mapping)}")
        return mapping[tf]
