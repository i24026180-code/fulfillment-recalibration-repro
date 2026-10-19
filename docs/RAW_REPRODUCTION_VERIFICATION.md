# Verified raw-data reproduction of the primary frozen results

On the user-provided original nine-table Olist source, the clean public `scripts/reproduce_olist_primary.py` was executed for **all four fitting origins O1–O4**. Each origin independently fits an S1 cyclical-month logistic regression and runs daily intercept recalibration under Expanding, Rolling-60 and Approval-60 policies.

Numerical comparison to the frozen aggregate archive:

| Quantity | Maximum absolute discrepancy |
|---|---:|
| 16 paired method Brier losses (including Raw) | 2.47e-10 |
| LogLoss | 7.03e-10 |
| Average precision | 1.88e-8 |
| Mean predicted risk | 1.46e-9 |
| 8 predefined historical-window Brier contrasts | 8.83e-11 |
| 95% bootstrap endpoints | 9.43e-11 |

The full reconstruction additionally reports a one-time Frozen intercept reference. Its Brier was compared against the historical source when available, but Frozen is not in the public E16-S1 summary table and therefore excluded from the `compare_raw_to_frozen.py` checker.

The original research reported Python 3.12.10 and pinned NumPy/pandas/scipy/scikit-learn versions. Local verification used Python 3.13 and the same main numerical package versions; exact binary equality is not promised. Full run output and intermediate order-level data were **not** committed, because records are excluded from this public release.

This is a test of the public Olist **primary pipeline** only. It is not an independent re-execution of every E0–E16 research-stage comparison or the auxiliary DataCo/LaDe-P model-fitting workflows.
