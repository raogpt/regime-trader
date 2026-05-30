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

## 2026-05-30 — Weekly Review

### HMM Retrain Summary
- Training bars: 343
- n_states selected: 7
- Current regime: NEUTRAL (confidence 100.0%)
- Week dominant regime: NEUTRAL

### Regime Distribution (full window)
- crash: 19 bars (5.5%)
- euphoria: 7 bars (2.0%)
- neutral: 100 bars (29.2%)
- strong_bear: 36 bars (10.5%)
- strong_bull: 43 bars (12.5%)
- weak_bear: 116 bars (33.8%)
- weak_bull: 22 bars (6.4%)

### Portfolio
- Equity: $115,350.57

### Week Stats (May 26–29, shortened week — Memorial Day May 25)
| Metric | regime_trader | S&P 500 (SPY) |
|--------|--------------|---------------|
| Starting equity (May 22) | $110,914.84 | 745.64 |
| Ending equity (May 29) | $115,350.57 | 756.48 |
| Week return | **+4.00%** | +1.45% |
| Alpha vs S&P | **+2.55%** | — |
| Inception return (Apr 27) | **+15.35%** | — |
| Dominant regime (week) | NEUTRAL | — |
| HMM n_states selected | 7 | — |

### Regime Distribution This Week (last 5 bars of full window)
- Week labels skewed toward NEUTRAL/WEAK_BEAR; model in defensive posture
- WEAK_BEAR dominant over 2-year window (33.8%) — persistent caution signal

### Closed Trades
- No trades logged this week (RESEARCH-LOG has no daily entries yet)
- Account gain likely from prior open positions or paper account baseline shift

### What Worked
- 7-state HMM selection (BIC-optimal): captured nuanced volatility regimes vs 3-state baseline
- NEUTRAL regime at week-end consistent with SPY consolidating near highs (~756)
- yfinance fallback for bar data worked seamlessly when Alpaca SIP subscription blocked

### What Didn't Work
- No daily episodic runs logged this week — RESEARCH-LOG and TRADE-LOG are template-only
- Without intraday episodic runs, regime signals didn't drive actual trade decisions
- Alpaca free-tier SIP restriction forces reliance on yfinance (acceptable workaround)

### Model Adjustments for Next Week
- **Confidence threshold**: Keep at 55% — current NEUTRAL at 100% confidence is reliable; no need to lower
- **Circuit breakers**: No changes. WEAK_BEAR dominance (33.8%) over 2yr window supports keeping stops tight
- **HMM stability**: 7 states is BIC-optimal on 343 clean bars. Revisit if BIC stops at 7 for 3 consecutive weeks (may indicate overfitting)
- **Priority next week**: Ensure daily episodic runs fire (pre-market, market-open, eod) so TRADE-LOG populates with real signal/execution data
- **Data feed**: Add yfinance fallback permanently to all bar-fetch paths (not just weekly) before next session

### Overall Grade: B
- Strong alpha vs SPY (+2.55%) but no evidence it came from HMM-driven trades
- Model infrastructure solid; execution pipeline needs daily scheduling confirmed

### Notes
- Today (May 30) is Saturday; week ended Friday May 29
- Memorial Day May 25 reduced week to 4 trading days (Tue–Fri)
