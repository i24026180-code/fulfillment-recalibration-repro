> Historical protocol/background. Current R2 capability boundaries and command coverage are defined in PROTOCOL_R2.md and REPRODUCTION_COVERAGE.csv; this document is not a new execution log.

# Paper-to-code evidence map

| Paper claim | Experiment | Public aggregate | Public reconstruction command |
|---|---|---|---|
| Four-origin calibration directions | E15 + S1 | `results/olist/four_origin_s1.csv` | `scripts/reproduce_olist_primary.py` |
| Encoding sensitivity | S0–S3 | `results/olist/calendar_encoding_all_origins.csv` | aggregate checks only; private frozen fits |
| Admission-time vs approval-time rolling | E16-S1 | `results/olist/window_s1.csv`, `window_s1_contrasts.csv` | `scripts/reproduce_olist_primary.py` |
| Negative/positive Brier contributions | S1 | `results/olist/brier_loss_decomposition_s1.csv` | recomputed from four-origin raw outputs |
| DataCo supply-chain auxiliary | E8–E9 | `results/auxiliary/dataco_deadline_closed_test_stress.csv` | additional legacy pipeline, not included |
| LaDe-P Jilin rare-event auxiliary | E12–E13 | `results/auxiliary/lade_jilin_e13_aggregate.csv` | additional legacy pipeline, not included |

All figures and tables derive from frozen aggregate evidence. The prior expansive E0–E14 model search is **development-stage**, not an independently replicated final test. Do not claim causal source-of-shift identification or actual avoided delivery costs.
