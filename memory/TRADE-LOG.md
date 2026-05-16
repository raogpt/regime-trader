# Trade Log — regime_trader

## Day 0 — Baseline (pre-launch)
**Portfolio:** $100,000.00 | **Cash:** $100,000.00 (100%) | **Day P&L:** $0 | **Phase P&L:** $0
**Regime:** UNKNOWN (HMM not yet run in episodic mode)

No positions. Bot launches Monday Apr 27.

---

## Week ending 2026-05-16 — Audit Flag
**Portfolio:** $106,635.15 | **Return since inception:** +6.64%
**Current Regime:** BEAR (99.9% confidence) — single bar, stability unconfirmed
**⚠ AUDIT NEEDED:** Trade log shows no recorded trades but equity shows +$6,635.15 gain.
Must reconcile on Monday pre-market run. Possible causes:
- Positions opened by daily modes (pre-market/market-open/eod) without trade-log writes
- Paper account seeded differently than $100k
Action: run `--mode pre-market` Monday to get live position snapshot.
