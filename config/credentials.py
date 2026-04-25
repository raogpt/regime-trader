"""
Loads broker credentials from environment variables (via .env).
Never hard-code keys here — always use the .env file.
"""

import os
from dotenv import load_dotenv

load_dotenv()


def get_alpaca_credentials() -> dict:
    """Return Alpaca API credentials loaded from environment."""
    return {
        "api_key":    os.environ.get("ALPACA_API_KEY", ""),
        "secret_key": os.environ.get("ALPACA_SECRET_KEY", ""),
        "base_url":   os.environ.get("ALPACA_BASE_URL", "https://paper-api.alpaca.markets"),
    }
