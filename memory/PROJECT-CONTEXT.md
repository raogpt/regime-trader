# Project Context — regime_trader

## Overview
- What: Autonomous HMM-based regime trading bot
- Account: Alpaca paper #2 (separate from trading-bot)
- Universe: SPY, QQQ, IWM (ETF only — no individual stocks)
- Strategy: Volatility-regime detection via Gaussian HMM, 3-7 states
- Bar size: 5-minute (episodic mode via REST) and daily (HMM training)

## Architecture
- models/hmm_engine.py — HMM with BIC-based state selection (3-7 states)
- models/regime_strategies.py — 3 strategies: LowVol/MidVol/HighVol
- data/feature_engineering.py — 14 rolling features, forward-safe
- execution/order_executor.py — Alpaca REST orders
- risk/risk_manager.py — circuit breakers, position sizing
- episodic_runner.py — stateless cloud-compatible runner (no WebSocket)

## Regime Labels (volatility-ranked)
- LOW_VOL → 95% allocation, 1.25x leverage
- MID_VOL → 60-95% allocation, 1.0x leverage
- HIGH_VOL → 60% allocation, 1.0x leverage, wide stops

## Cross-Enrichment (from trading-bot)
- Earnings/catalyst filter: avoid entry 2 days before FOMC, CPI, major ETF earnings
- Sector momentum bias: if trading-bot is in Materials/Energy → prefer IWM

## Key Files
- memory/PROJECT-CONTEXT.md (this file)
- memory/TRADE-LOG.md
- memory/RESEARCH-LOG.md
- memory/WEEKLY-REVIEW.md
- memory/COMPARISON-LOG.md (shared with trading-bot)

## Rules
- NEVER share API keys externally
- Every trade logged BEFORE execution
- HMM retrained weekly (or if model > 7 days old)
- Circuit breakers are HARD stops — never override
