# Weekly Review — regime_trader

Friday reviews appended here.

## Week ending YYYY-MM-DD

### Stats
| Metric | regime_trader | trading-bot |
|--------|--------------|-------------|
| Starting portfolio | $X | $X |
| Ending portfolio | $X | $X |
| Week return | +-X% | +-X% |
| S&P 500 week | +-X% | +-X% |
| Alpha vs S&P | +-X% | +-X% |
| Trades | N | N |
| Win rate | X% | X% |
| Sharpe (est.) | X.XX | X.XX |
| Dominant regime | X | — |

### Regime Distribution This Week
| Regime | Bars | % of time |
|--------|------|-----------|

### Closed Trades
| ETF | Entry | Exit | P&L | Regime |

### What Worked
- ...

### What Didn't Work
- ...

### Model Adjustments
- ...

### Overall Grade: X

## 2026-05-02 — Weekly Review

### Stats
| Metric | regime_trader | trading-bot |
|--------|--------------|-------------|
| Starting portfolio | $100,000 | — |
| Ending portfolio | $102,173.43 | — |
| Week return | +2.17% | TBD |
| S&P 500 week (SPY) | +0.91% | +0.91% |
| Alpha vs S&P | +1.26% | TBD |
| Trades | 3 (SPY/QQQ/IWM, all open) | — |
| Win rate | 3/3 open, 100% unrealized | — |
| Sharpe (est.) | ~1.2 (5 days, insufficient) | — |
| Dominant regime | EUPHORIA | — |

### HMM Retrain Summary
- Training bars: 343
- n_states selected: 6 (BIC-optimal)
- Current regime: EUPHORIA (confidence 100.0%)
- Week dominant regime: EUPHORIA

### Regime Distribution (full window)
| Regime | Bars | % of time |
|--------|------|-----------|
| weak_bear | 159 | 46.4% |
| strong_bull | 94 | 27.4% |
| euphoria | 36 | 10.5% |
| weak_bull | 25 | 7.3% |
| crash | 17 | 5.0% |
| strong_bear | 12 | 3.5% |

### Open Positions (end of week)
| ETF | Shares | Entry | Current | Unrealized P&L | P&L% |
|-----|--------|-------|---------|----------------|------|
| IWM | 194 | $275.20 | $279.28 | +$790.87 | +1.48% |
| QQQ | 62 | $662.13 | $674.15 | +$745.18 | +1.82% |
| SPY | 91 | $713.65 | $720.65 | +$637.38 | +0.98% |

### Closed Trades
_None — all positions still open._

### What Worked
- HMM correctly identified EUPHORIA regime → long all 3 ETFs at open
- All 3 positions profitable; +2.17% vs +0.91% S&P 500 (+1.26% alpha)
- 6-state BIC-selected model provides better regime granularity than 3-state baseline
- EUPHORIA label triggered high-allocation entries, capturing the week's upside

### What Didn't Work
- **Leverage overshoot**: cash = -$59,383 → actual leverage ~1.58x vs hard max 1.25x — risk_manager sizing not enforced correctly
- **Trade logging gap**: positions opened during the week but NOT recorded in TRADE-LOG.md (cloud session isolation — each session runs stateless without prior log context)
- TRADE-LOG shows "no positions" from Day 0 yet 3 positions are live → log is stale

### Model Adjustments
- Fix leverage enforcement: investigate why risk_manager allowed ~1.58x when MAX_LEVERAGE=1.25 — likely regime_info.max_position_size_pct not being respected in market-open rebalance
- Fix trade logging: ensure each cloud session reads existing TRADE-LOG before appending
- Confidence threshold 55% — appropriate, no change needed this week
- Circuit breakers intact — not triggered this week
- 6-state model stable — keep for next week; monitor if EUPHORIA → weak_bear flip occurs

### Portfolio
- Equity: $102,173.43 | Cash: -$59,383.34 | Open positions: 3

### Overall Grade: B+
_(Returns strong, alpha positive — but leverage overshoot and logging gap are process failures that must be fixed before next week)_
