"""
Structured logging configuration for regime_trader.
"""

from __future__ import annotations

import logging
import logging.handlers
import sys
from pathlib import Path

from config import settings


def setup_logging(log_dir: str = "logs") -> None:
    """
    Configure root logger with:
      - Console handler (INFO+)
      - Rotating file handler  logs/main.log   (10 MB, 30 files)
    Log level read from settings.LOG_LEVEL.
    """
    level  = getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO)
    fmt    = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    datefmt= "%Y-%m-%dT%H:%M:%SZ"

    root = logging.getLogger()
    root.setLevel(level)
    root.handlers.clear()

    # Console
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(level)
    ch.setFormatter(logging.Formatter(fmt, datefmt=datefmt))
    root.addHandler(ch)

    # Rotating file
    Path(log_dir).mkdir(parents=True, exist_ok=True)
    fh = logging.handlers.RotatingFileHandler(
        f"{log_dir}/main.log",
        maxBytes  = 10 * 1024 * 1024,  # 10 MB
        backupCount = 30,
        encoding    = "utf-8",
    )
    fh.setLevel(level)
    fh.setFormatter(logging.Formatter(fmt, datefmt=datefmt))
    root.addHandler(fh)


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
