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

## 2026-05-09 — Weekly Review

### HMM Retrain Summary
- Training bars: 343
- n_states selected: 7
- Current regime: WEAK_BULL (confidence 100.0%)
- Week dominant regime: WEAK_BULL

### Regime Distribution (full window)
- crash: 14 bars (4.1%)
- euphoria: 8 bars (2.3%)
- neutral: 112 bars (32.7%)
- strong_bear: 29 bars (8.5%)
- strong_bull: 30 bars (8.7%)
- weak_bear: 115 bars (33.5%)
- weak_bull: 35 bars (10.2%)

### Portfolio
- Equity: $108,100.81
- Cash: -$102,287.48 (leveraged, 3-ETF basket open)
- Est. week-start equity (May 4 close): ~$101,384
- **Week return (May 5–8): ~+6.62%**
- **Since inception (Apr 28–May 8): +8.10%**

### Stats
| Metric | regime_trader | S&P 500 (SPY) |
|--------|--------------|---------------|
| Starting equity | $100,000 | — |
| Ending equity | $108,100.81 | — |
| Week return | ~+6.62% | +2.71% |
| Since inception | +8.10% | +3.62% |
| Alpha vs SPY (inception) | +4.48% | — |
| Trades (closed) | 0 | — |
| Win rate | N/A | — |
| Sharpe (est.) | N/A (no closed trades) | — |
| Dominant regime | WEAK_BULL | — |

### Open Positions (no closed trades this week)
| ETF | Qty | Entry | Current | Unreal. P&L | Unreal. % |
|-----|-----|-------|---------|------------|-----------|
| IWM | 228 | $275.90 | $284.17 | +$1,886.07 | +3.00% |
| QQQ | 73 | $664.05 | $711.23 | +$3,443.99 | +7.11% |
| SPY | 127 | $715.80 | $737.62 | +$2,770.75 | +3.05% |
| **Total** | | | | **+$8,100.81** | **+8.10%** |

### ETF Week Returns (May 5–8, benchmark context)
| ETF | Week | Since Inception |
|-----|------|----------------|
| SPY | +2.71% | +3.62% |
| QQQ | +5.70% | +8.17% |
| IWM | +2.26% | +2.98% |

### What Worked
- HMM identified WEAK_BULL regime correctly — all 3 ETFs rallied into week-end
- 7-state BIC selection captured fine-grained market structure (crash/bear/neutral/bull spectrum)
- Leveraged basket (IWM + QQQ + SPY) captured cross-asset momentum — QQQ +7.11% unrealized is the star
- Portfolio significantly outperformed SPY (+8.10% vs +3.62% since inception)

### What Didn't Work
- **Critical logging bug**: TRADE-LOG.md shows no entries after Day 0 — bot executed trades but never wrote to the log; no audit trail of entry signals, stop levels, or regime at entry
- Cash is -$102,287 (2x+ leverage on $100k) — position sizing may be oversized relative to risk manager settings
- No closed trades yet → Sharpe and win-rate are unmeasurable; need first full trade cycle

### Model Adjustments for Next Week
- **Fix TRADE-LOG append bug (P0)** — identify why `append_to_log(TRADE_LOG, ...)` isn't firing in market-open/eod modes and patch immediately
- Verify position sizing against risk_manager.py: at current leverage (~2x), a -5% correlated drawdown would wipe ~$10k; confirm circuit breaker levels match the overleveraged state
- HMM: 7 states converged with BIC selection — model is healthy. Some convergence warnings on n_states=6,7 but final BIC-selected model converged (9 iterations). No adjustment needed yet.
- Confidence threshold (55%) held fine — WEAK_BULL at 100% confidence is a strong signal; did not flicker
- Consider adding a max-leverage circuit breaker: if total_positions_value > 1.5× equity → reduce automatically

### Overall Grade: B+
- **Alpha generation: A** — +8.10% vs SPY +3.62% is excellent
- **Execution/logging: D** — no trade log is a serious operational failure
- **Risk management: C** — 2x leverage in WEAK_BULL is defensible but undocumented; stop levels unknown
