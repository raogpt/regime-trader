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

## 2026-06-13 — Weekly Review

### HMM Retrain Summary
- Training bars: 343
- n_states selected: 6
- Current regime: CRASH (confidence 100.0%)
- Week dominant regime: CRASH

### Regime Distribution (full window)
- crash: 49 bars (14.3%)
- euphoria: 12 bars (3.5%)
- strong_bear: 19 bars (5.5%)
- strong_bull: 40 bars (11.7%)
- weak_bear: 114 bars (33.2%)
- weak_bull: 109 bars (31.8%)

### Portfolio
- Equity (Sat Jun 13): $108,016.70
- Cash: -$28,569.68 (leveraged — margin used)
- Open positions: IWM ×149, QQQ ×62, SPY ×65
- Unrealized P&L: +$1,402.27

### Week Performance Stats
| Metric | regime_trader | S&P 500 (SPY) |
|--------|--------------|---------------|
| Start equity (Jun 5 Fri) | $108,011.71 | $737.55 |
| End equity (Jun 12 Fri) | $107,188.94 | $741.75 |
| Week return | **-0.76%** | **+0.57%** |
| Alpha vs S&P | **-1.33%** | — |
| Intra-week max drawdown | -4.51% (Jun 11) | -1.65% (Jun 10) |
| Cumulative since inception | +8.02% | — |
| Dominant regime (week) | CRASH | — |
| HMM confidence | 100% (CRASH) | — |

### Regime Distribution This Week (Jun 8–12)
CRASH dominated: severe volatility on Wed Jun 11 (-4.74% portfolio in one session).
Mid-week recovery Thu-Fri recovered most losses but still closed negative for the week.

### Closed Trades
None closed this week. All three positions (IWM, QQQ, SPY) remain open.

### What Worked
- HMM CRASH signal was accurate: Wed Jun 11 saw the worst single-day drop (-4.74%)
- Portfolio recovered Thu-Fri, suggesting the underlying positions retained value
- 6-state BIC-optimal model chose the right complexity for current market structure
- Cumulative return +8.02% since inception remains well above baseline

### What Didn't Work
- **Positions held through a CRASH regime** — hard rule violation in spirit: CRASH at 100% confidence should have triggered risk reduction or exit
- Leveraged positions (-$28k cash) are dangerous under CRASH regime; amplifies drawdowns
- No stop-loss triggered on Jun 11 despite -4.51% drawdown from week start (stop loss rule is 7% — nearly hit)
- Mid-week drawdown to $103,282 (-3.45% from $106,897 inception adj.) was uncomfortable
- -1.33% alpha miss vs. SPY this week is a meaningful underperformance

### Model Adjustments
- **Confidence threshold**: 55% is too permissive for entering/holding through CRASH regime; consider raising to 65% for position initiation
- **CRASH regime circuit breaker**: add explicit CRASH-regime position cap (e.g., max 50% allocation when regime=CRASH at >80% confidence)
- **Negative cash / leverage**: enforce no-margin rule — positions should never push cash negative; this is a hard budget constraint
- **Retrain cadence**: 6-state model is BIC-optimal; keep n_states_range=[3,7] but consider weekly forced retrain (already implemented)
- **Stop-loss tightening in CRASH**: reduce ATR multiplier from 2.0× to 1.5× when CRASH regime detected

### Lessons Learned
1. A 100% CRASH confidence reading means the model is certain — yet positions stayed open. The execution layer must respect the regime signal more aggressively.
2. Leverage (negative cash) in a CRASH regime is the highest-risk combination possible. Must be unwound first.
3. The intra-week recovery (Jun 11 → Jun 12: +$3,905) shows the model's underlying ETF selection is sound but timing needs improvement.
4. SPY outperformed this week — in a CRASH regime, the market can still recover; a "crash" state means elevated volatility, not necessarily directional down.

### Overall Grade: D+
- Lost -1.33% vs. SPY benchmark
- Held leveraged positions through verified CRASH regime (risk management gap)
- HMM signal quality: HIGH (correctly called crash conditions)
- Execution discipline: LOW (positions not reduced despite signal)
