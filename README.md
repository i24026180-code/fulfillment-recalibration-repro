# Fulfillment-risk recalibration: reproducibility materials

**Author-review candidate v0.3.0 — 10 October 2026**

Companion to *Temporal Sensitivity of Historical Intercept Recalibration for Fulfillment-Risk Prediction*.
This release aligns the evidence for **Frozen−Raw**, **Expanding−Frozen** and **Expanding−Raw**.
It adds direct paired backbone differences of these effects, Frozen trajectories, fixed-prediction
unknown-outcome bounds, and visible 3/7/14-day block sensitivity. No model is retrained in these
post-analyses. The archive does not assert journal acceptance or an already published GitHub release.

## Quick start: public aggregate reproduction

Use Python 3.13 for the recorded review environment (see `docs/ENVIRONMENT_R2.json`).
From this repository directory run:

```bash
python -m pip install -r requirements-review-lock.txt
python scripts/validate_revision.py
python scripts/rebuild_core_tables.py --out build/core
python scripts/make_revision_tables.py
python scripts/make_revision_figures.py
```

Use a new/empty `--out` directory. The single `rebuild_core_tables.py` entry creates
`Table_core_comparisons.csv`, complete three-pair intervals, absolute scores, cross-backbone
intervals and the aggregate bound checks. This entry **re-estimates paired intervals from
public daily sufficient statistics**, but does not verify upstream feature construction or
retrain models. The baseline `validate_revision.py` only checks archived arithmetic and hashes.

`requirements.txt` preserves the original experiment's package specification; the review lock
records the environment actually used for this release's CPU post-analysis. GPU models are not
required for the public checks. The figure entry creates one chart per output file; the manuscript
may combine those files in a single figure. Figure 1 is never rewritten.

## Private-record analyses (not included in the public package)

```bash
python scripts/align_core_comparisons.py --e17-dir /path/to/extracted/E17 --out outputs/r2
python scripts/replay_e17_calibration.py --archive /path/to/private_E17_archive.zip --origin O2 --out outputs/replay_O2
```

The first command requires the extracted E17 directory containing `predictions/`,
`Core_O1_pools.csv` through `Core_O4_pools.csv`, `metrics.csv`, `paired_intervals.csv` and
`unknown_outcome_bounds.csv`. It aligns the stored records across backbones, reconstructs Frozen
from archived warm-up offsets, and repeats the R2 statistics. Input hashes appear in
`evidence/r2/analysis_manifest.json`. It fits no predictor or calibrator. Keep these inputs local.

The second command refits supported calibration policies from saved out-of-training base scores;
it does not rebuild features or train the base model. The new R2 smoke validation covers O2 only,
with 12,209 evaluation records and 420 policy/day entries. Earlier four-origin validation records
are dated separately. This private ZIP is not provided here; public users can run the aggregate
layer without it.

## Raw-data entry and honest coverage

```bash
python scripts/reproduce_olist_primary.py --olist-zip /path/to/original_Olist.zip --out outputs/core --threads 2
```

This retained entry covers the earlier raw-Olist Core/S1 LR and window pipeline only. It was not
rerun during R2, and does not claim to regenerate every E17 CatBoost, PeriodicLR or auxiliary
experiment. See `docs/REPRODUCTION_COVERAGE.csv` before interpreting any validation result.

## Information timing and interpretation

No outcome unavailable at an update enters that update. Earlier evaluation-period outcomes
**may enter later updates** after their observation and admission conditions are met; issued
predictions are never overwritten. Main deadline/closed admission equals the promised-day end
under the stated status-observation assumption. Frozen LR (Figure 1) means a fixed backbone;
Frozen calibration means a single post-warm-up intercept. PeriodicLR instead refits on expanding
eligible history at evaluation start and day 30, with each training feature vector evaluated at
its original approval time.

For a fixed evaluation cohort, total correction = initial correction + update increment as a
score-difference identity; interval endpoints are not additive. Cross-backbone effects use the
same order/date/label alignment and common date-block weights. No significant-vs-nonsignificant
comparison substitutes for that direct contrast.

Unknown-label bounds retain all predictors, histories and calibration parameters. Nominal
follow-up is `(2018-10-17 17:30:18 − approval).total_seconds()/86400`, not time since the deadline.
The horizon is a proxy, not certified complete follow-up. Equal threshold-selected sets are
identified and are not independent robustness observations. Bounds are not confidence intervals.

All Olist comparisons are retrospective and use a completed-delivery analytical cohort. The
calendar specification and later analyses followed earlier access to these historical windows.
Block intervals condition on saved predictions and do not cover full model/research selection.
Different DataCo/LaDe outcomes are auxiliary tasks, not same-target confirmation. Value coverage
is transaction exposure, not profit or prevented loss.

## Contents and public release

- `evidence/e17/`: archived scores, diagnostics, original paired intervals and protocols.
- `evidence/r2/`: new aligned sufficient statistics, bounds, effects and validation records.
- `evidence/protocols/`, `evidence/auxiliary/`, `evidence/derived/`: prior sanitized evidence.
- `tables/`, `figures/`: regenerable manuscript assets; current files use lowercase names.
- `docs/`: coverage, measured validation, environment and source/license notes.

No raw transactions, individual prediction caches, trained models or font files are included.
Dataset and derivative redistribution rights, code ownership/license and author citation metadata
must be approved before public release. Run `python scripts/audit_public_files.py` and manually
inspect the Git index. Automated scanning is not legal or privacy certification. The provided
workflow has not been run on remote GitHub during this work. Suggested repository name:
`fulfillment-recalibration-repro`.
