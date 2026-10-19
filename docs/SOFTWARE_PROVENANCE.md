# Provenance

`src/fulfillment_recalibration/olist_helpers.py` is a preserved implementation of the original order aggregation, historical seller feature construction, and LR preprocessing from the frozen exploratory experiments. `scripts/reproduce_olist_primary.py` is a clean, configurable public reconstruction of the final E15/S1/E16-S1 protocol. `results/` copies only aggregated, non-record-level tables from the user-supplied frozen experiment archive, with no recomputation or tuning to change signs.

The archived research environment reports Python 3.12.10, NumPy 2.3.5, pandas 2.2.3, SciPy 1.17.0, scikit-learn 1.8.0, joblib 1.6.0, threadpoolctl 3.6.0. Source repositories and processing scripts should be cited alongside data publishers; copying from historical files does not itself establish a software license. Any public release remains subject to author review.
