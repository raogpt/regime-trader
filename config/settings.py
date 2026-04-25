"""
Global configuration parameters for regime_trader.
Edit this file to customise tickers, HMM, strategies, risk, backtest, and monitoring.
"""

# ---------------------------------------------------------------------------
# Broker
# ---------------------------------------------------------------------------
BROKER = "alpaca"
PAPER_TRADING = True

# ---------------------------------------------------------------------------
# Universe
# ---------------------------------------------------------------------------
TICKERS = ["SPY", "QQQ", "IWM"]
PRIMARY_TICKER = "SPY"
BAR_TIMEFRAME = "5Min"          # bar size for the main loop
MARKET_OPEN = "09:30"
MARKET_CLOSE = "16:00"
TIMEZONE = "America/New_York"

# ---------------------------------------------------------------------------
# HMM
# ---------------------------------------------------------------------------
HMM_N_STATES_RANGE = (3, 7)     # tested automatically; best selected via BIC
HMM_TRAINING_DAYS = 504         # ~2 years of daily bars for initial fit
HMM_RETRAIN_INTERVAL_DAYS = 21  # re-fit every ~1 month
HMM_STABILITY_BARS = 3          # consecutive bars required before acting
HMM_INSTABILITY_WINDOW = 20     # bars window for flickering detection
HMM_INSTABILITY_THRESHOLD = 4   # max regime flips inside window before warning

# ---------------------------------------------------------------------------
# Regime labels (mapped by sorted mean return: lowest → highest)
# ---------------------------------------------------------------------------
REGIME_LABELS_3 = ["bear", "neutral", "bull"]
REGIME_LABELS_4 = ["crash", "bear", "bull", "euphoria"]
REGIME_LABELS_5 = ["crash", "bear", "neutral", "bull", "euphoria"]

# ---------------------------------------------------------------------------
# Allocation targets per regime  (fraction of portfolio, 0–1)
# ---------------------------------------------------------------------------
ALLOCATION = {
    "crash":    {"target": 0.05, "leverage": 1.0},
    "bear":     {"target": 0.25, "leverage": 1.0},
    "neutral":  {"target": 0.55, "leverage": 1.0},
    "bull":     {"target": 0.90, "leverage": 1.25},
    "euphoria": {"target": 0.45, "leverage": 1.0},
}

# ---------------------------------------------------------------------------
# Risk / circuit breakers
# ---------------------------------------------------------------------------
MAX_POSITION_RISK_PCT = 0.01        # max 1 % of portfolio at risk per trade
MAX_LEVERAGE = 1.25

CIRCUIT_BREAKERS = {
    "daily_loss_half":      -0.02,  # cut position sizes 50 %
    "daily_loss_close_all": -0.03,  # close all positions
    "weekly_loss_resize":   -0.05,  # resize portfolio
    "drawdown_stop":        -0.10,  # stop bot + write .lock file
}

DRAWDOWN_LOCK_FILE = "trading_halted.lock"

# ---------------------------------------------------------------------------
# Walk-forward back-test
# ---------------------------------------------------------------------------
BACKTEST = {
    "in_sample_days":   252,    # ~1 year
    "out_sample_days":  126,    # ~6 months
    "step_days":        21,     # ~1 month slide
    "slippage_bps":     5,      # basis points per side
    "commission_per_share": 0.0, # Alpaca is $0
}

# ---------------------------------------------------------------------------
# Monitoring
# ---------------------------------------------------------------------------
DASHBOARD_REFRESH_SECONDS = 30
LOG_LEVEL = "INFO"
ALERT_EMAIL_ENABLED = False
ALERT_WEBHOOK_ENABLED = False
