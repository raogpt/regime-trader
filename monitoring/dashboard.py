"""
Terminal dashboard using the `rich` library.

Layout (refreshes every 5 seconds):
  ┌─ REGIME ──────────────────────────────────────────────────┐
  │ BULL (72%) | Stability: 14 bars | Flicker: 1/20           │
  ├─ PORTFOLIO ───────────────────────────────────────────────┤
  │ Equity: $105,230 | Daily: +$340 (+0.32%)                  │
  │ Allocation: 95% | Leverage: 1.25x                         │
  ├─ POSITIONS ───────────────────────────────────────────────┤
  │ SPY | LONG | $520.30 | +1.2% | Stop: $508 | 3h            │
  ├─ RECENT SIGNALS ──────────────────────────────────────────┤
  │ 14:30 | SPY | Rebalance 60%→95% | Low vol                 │
  ├─ RISK STATUS ─────────────────────────────────────────────┤
  │ Daily DD: 0.3%/3% ✅ | From Peak: 1.2%/10% ✅            │
  ├─ SYSTEM ──────────────────────────────────────────────────┤
  │ Data: ✅ | API: ✅ 23ms | HMM: 2d ago | PAPER             │
  └───────────────────────────────────────────────────────────┘
"""

from __future__ import annotations

import threading
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional


# ---------------------------------------------------------------------------
# State container (updated from main loop)
# ---------------------------------------------------------------------------

@dataclass
class DashboardState:
    # Regime
    regime_label:      str   = "—"
    regime_prob:       float = 0.0
    stability_bars:    int   = 0
    flicker_count:     int   = 0
    flicker_window:    int   = 20

    # Portfolio
    equity:            float = 0.0
    equity_start:      float = 0.0   # start of day equity
    allocation_pct:    float = 0.0
    leverage:          float = 1.0

    # Risk
    daily_dd_pct:      float = 0.0
    peak_dd_pct:       float = 0.0
    cb_daily_half:     bool  = False
    cb_daily_halt:     bool  = False
    cb_weekly_half:    bool  = False
    cb_weekly_halt:    bool  = False
    cb_peak_locked:    bool  = False

    # Positions: {ticker: {"side","price","pnl_pct","stop","age_h"}}
    positions:         dict  = field(default_factory=dict)

    # Recent signals (last 5)
    recent_signals:    list  = field(default_factory=list)

    # System
    data_ok:           bool  = False
    api_ok:            bool  = False
    api_latency_ms:    int   = 0
    hmm_trained_ago:   str   = "—"
    paper_mode:        bool  = True
    last_update:       Optional[datetime] = None

    def add_signal(self, time_str: str, ticker: str, description: str,
                    strategy: str) -> None:
        self.recent_signals.insert(0, (time_str, ticker, description, strategy))
        self.recent_signals = self.recent_signals[:5]


# ---------------------------------------------------------------------------
# Dashboard renderer
# ---------------------------------------------------------------------------

class Dashboard:
    """
    Rich-based live terminal dashboard.
    Call `start()` to begin background refresh and `update(state)` from main loop.
    """

    def __init__(self, refresh_seconds: int = 5) -> None:
        self._refresh = refresh_seconds
        self._state   = DashboardState()
        self._running = False
        self._thread: Optional[threading.Thread] = None
        self._live    = None   # rich.live.Live instance

    def update(self, state: DashboardState) -> None:
        self._state = state
        self._state.last_update = datetime.now(timezone.utc)

    def start(self) -> None:
        self._running = True
        self._thread  = threading.Thread(
            target=self._run, daemon=True, name="dashboard")
        self._thread.start()

    def stop(self) -> None:
        self._running = False
        if self._live:
            self._live.stop()

    # ------------------------------------------------------------------
    # Internal render loop
    # ------------------------------------------------------------------

    def _run(self) -> None:
        try:
            from rich.live   import Live
            from rich.layout import Layout
        except ImportError:
            # Fallback: plain text if rich not installed
            self._run_plain()
            return

        with Live(self._render(), refresh_per_second=0.2,
                   screen=False) as live:
            self._live = live
            while self._running:
                time.sleep(self._refresh)
                live.update(self._render())

    def _run_plain(self) -> None:
        while self._running:
            self._print_plain()
            time.sleep(self._refresh)

    def _print_plain(self) -> None:
        s = self._state
        daily_pnl = s.equity - s.equity_start
        daily_pct = daily_pnl / s.equity_start * 100 if s.equity_start else 0.0
        cb_ok     = not (s.cb_daily_half or s.cb_daily_halt or
                         s.cb_weekly_half or s.cb_weekly_halt or s.cb_peak_locked)

        print("\n" + "=" * 62)
        print(f"  REGIME   {s.regime_label.upper()} ({s.regime_prob:.0%}) | "
              f"Stability: {s.stability_bars} bars | "
              f"Flicker: {s.flicker_count}/{s.flicker_window}")
        print(f"  PORTFOLIO  Equity: ${s.equity:,.0f} | "
              f"Daily: {daily_pnl:+,.0f} ({daily_pct:+.2f}%)")
        print(f"             Allocation: {s.allocation_pct:.0%} | "
              f"Leverage: {s.leverage:.2f}x")
        for ticker, pos in s.positions.items():
            print(f"  POSITION   {ticker} | {pos.get('side','LONG')} | "
                  f"${pos.get('price',0):.2f} | "
                  f"{pos.get('pnl_pct',0):+.1%} | "
                  f"Stop: ${pos.get('stop',0):.2f} | "
                  f"{pos.get('age_h',0):.0f}h")
        if s.recent_signals:
            sig = s.recent_signals[0]
            print(f"  SIGNAL     {sig[0]} | {sig[1]} | {sig[2]} | {sig[3]}")
        dd_ok  = "✓" if s.daily_dd_pct  < 2.0 else "!"
        peak_ok= "✓" if s.peak_dd_pct   < 10.0 else "!"
        print(f"  RISK       Daily DD: {s.daily_dd_pct:.1f}%/3% {dd_ok} | "
              f"From Peak: {s.peak_dd_pct:.1f}%/10% {peak_ok}")
        mode  = "PAPER" if s.paper_mode else "LIVE"
        d_ok  = "✓" if s.data_ok else "✗"
        a_ok  = "✓" if s.api_ok  else "✗"
        print(f"  SYSTEM     Data: {d_ok} | API: {a_ok} {s.api_latency_ms}ms | "
              f"HMM: {s.hmm_trained_ago} | {mode}")
        print("=" * 62)

    def _render(self):
        from rich.table  import Table
        from rich.panel  import Panel
        from rich.text   import Text
        from rich.columns import Columns
        from rich        import box

        s         = self._state
        daily_pnl = s.equity - s.equity_start
        daily_pct = daily_pnl / s.equity_start * 100 if s.equity_start else 0.0

        regime_color = {
            "bull": "green", "strong_bull": "bright_green",
            "euphoria": "bright_green",
            "neutral": "yellow", "weak_bull": "yellow",
            "bear": "red", "strong_bear": "bright_red",
            "crash": "bright_red", "weak_bear": "red",
        }.get(s.regime_label.lower(), "white")

        rows = []

        # Regime row
        rows.append(Text.assemble(
            ("  REGIME  ", "bold"),
            (f"{s.regime_label.upper()} ({s.regime_prob:.0%})", regime_color),
            "  |  Stability: ", (str(s.stability_bars), "cyan"), " bars",
            "  |  Flicker: ",
            (f"{s.flicker_count}/{s.flicker_window}",
             "yellow" if s.flicker_count > 4 else "green"),
        ))

        # Portfolio row
        sign  = "+" if daily_pnl >= 0 else ""
        color = "green" if daily_pnl >= 0 else "red"
        rows.append(Text.assemble(
            ("  PORTFOLIO", "bold"),
            f"  Equity: ${s.equity:,.0f}  |  ",
            ("Daily: ", ""),
            (f"{sign}${daily_pnl:,.0f} ({sign}{daily_pct:.2f}%)", color),
            f"\n             Allocation: {s.allocation_pct:.0%}"
            f"  |  Leverage: {s.leverage:.2f}x",
        ))

        # Positions
        if s.positions:
            pos_lines = []
            for ticker, pos in s.positions.items():
                pnl_c = "green" if pos.get("pnl_pct", 0) >= 0 else "red"
                pos_lines.append(Text.assemble(
                    ("  POSITION ", "bold"),
                    ticker, "  |  LONG  |  ",
                    f"${pos.get('price',0):.2f}  |  ",
                    (f"{pos.get('pnl_pct',0):+.1%}", pnl_c),
                    f"  |  Stop: ${pos.get('stop',0):.2f}"
                    f"  |  {pos.get('age_h',0):.0f}h",
                ))
            rows.extend(pos_lines)
        else:
            rows.append(Text("  POSITIONS  —  (none)", style="dim"))

        # Signals
        if s.recent_signals:
            sig = s.recent_signals[0]
            rows.append(Text.assemble(
                ("  SIGNAL   ", "bold"),
                f"{sig[0]}  |  {sig[1]}  |  {sig[2]}  |  {sig[3]}",
            ))

        # Risk status
        dd_color   = "green" if s.daily_dd_pct < 2.0  else "yellow" if s.daily_dd_pct < 3.0  else "red"
        peak_color = "green" if s.peak_dd_pct  < 10.0 else "red"
        rows.append(Text.assemble(
            ("  RISK     ", "bold"),
            f"Daily DD: ",
            (f"{s.daily_dd_pct:.1f}%/3%", dd_color),
            "   |   From Peak: ",
            (f"{s.peak_dd_pct:.1f}%/10%", peak_color),
        ))

        # System
        mode   = "PAPER" if s.paper_mode else ("LIVE", "bold red")
        d_icon = "[green]✔[/]" if s.data_ok else "[red]✘[/]"
        a_icon = "[green]✔[/]" if s.api_ok  else "[red]✘[/]"
        rows.append(Text.assemble(
            ("  SYSTEM   ", "bold"),
            f"Data: {d_icon}  |  API: {a_icon} {s.api_latency_ms}ms"
            f"  |  HMM: {s.hmm_trained_ago}",
            f"  |  {'PAPER' if s.paper_mode else 'LIVE'}",
        ))

        # Build panel
        content = Text("\n").join(str(r) if isinstance(r, str) else r for r in rows)

        ts = s.last_update.strftime("%H:%M:%S UTC") if s.last_update else "—"
        return Panel(
            content,
            title  = "[bold]regime_trader[/]",
            subtitle = f"[dim]refresh every {self._refresh}s | {ts}[/]",
            box    = box.ROUNDED,
        )


# ---------------------------------------------------------------------------
# Module-level singleton
# ---------------------------------------------------------------------------

_dashboard: Optional[Dashboard] = None


def get_dashboard(refresh_seconds: int = 5) -> Dashboard:
    global _dashboard
    if _dashboard is None:
        _dashboard = Dashboard(refresh_seconds=refresh_seconds)
    return _dashboard
