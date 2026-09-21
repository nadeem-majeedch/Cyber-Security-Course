# Lab 19 — Log Analysis & Anomaly Detection
**Core Lab 6 · Module 6 (L21; extends Lab 14's triage) · CLO-6 · Duration: 2 hours · Graded lab**

## 1. Learning Objectives
1. Engineer features from raw authentication logs that encode attacker-relevant behavior.
2. Fit and tune an unsupervised anomaly detector (isolation forest) on those features.
3. Choose an operating threshold under a realistic alert budget; state precision/recall consequences.
4. Correlate the flagged account's events across sources into a short incident narrative (event correlation).

## 2. Prerequisites
Lecture 21 (telemetry as data, isolation forest, alert budgets). Spreadsheet comfort. Lab 14 vocabulary (TP/FP/BTP) recommended.

## 3. Hardware/Software Requirements
- Course VM: Python 3.10+, `pandas`, `scikit-learn` (course image has them; `python -m pip install pandas scikit-learn` otherwise).
- Instructor-provided dataset: `auth-day.csv` (synthetic day of SSH/auth events; ~40k benign rows, seeded anomalies; documented schema in the file header).

## 4. Installation and Setup
1. Verify the environment:
   ```bash
   python -c "import pandas, sklearn; print('ok')"
   ```
2. Copy `auth-day.csv` to your working directory; open the header and read the schema note.
3. Open the starter notebook `starter/log_anomaly.ipynb`; run cell 1 to confirm the dataset loads.
   *(Dataset schema and notebook cell order are instructor-verified; column names must not be renamed.)*

## 5. Ethical Authorization and Safety Notes
- The dataset is synthetic; no real persons, hosts, or credentials appear. Do not import real logs from any live system into the course environment.
- Findings in this lab describe *behavior in a dataset*; acting on "findings" against real people is never in scope.

## 6. Step-by-Step Student Tasks
| # | Task | Hint |
|---|---|---|
| 1 | Load the CSV; report row count and time range | `pandas` describe |
| 2 | Engineer ≥ 8 features per account-hour: failed-count, success-after-failures flag, new-source flag, off-hours ratio, distinct sources, geo-dispersion proxy, inter-arrival CV, avg bytes-out proxy | Notebook cells 2–3 |
| 3 | Fit `IsolationForest` (contamination 0.01); add the anomaly score column | Cell 4 |
| 4 | Plot/inspect the score distribution; choose a threshold for ≤ 20 alerts/day | Cells 5–6 |
| 5 | Report precision/recall of your threshold against the dataset's seeded-attack labels (in the instructor key; use the lab's `labels.csv` when provided) | Cell 7 |
| 6 | **Correlation task:** for the top-flagged account, pull its rows from the raw CSV and write a 5-line narrative (source → behavior → outcome) | Spreadsheet or pandas |
| 7 | Write one analyst-readable alert for the top anomaly: behavior + evidence + suggested first action | L21 alert format |
| 8 | Retune: raise the threshold to halve alerts; report the recall cost | Cell 6 rerun |

## 7. Expected Observations
- Benign mass scores low; a handful of accounts (the seeded brute-force account, the new-country success account, and the off-hours file-reader) separate cleanly.
- Threshold at ~20 alerts/day captures the seeded chains with a small FP tail (misconfigured service account appears — expected and instructive).
- Correlation: the top account shows failure-streak → success from a new source → mass reads: the L21 pattern.

## 8. Questions for Analysis
1. Why did "failed-count" alone nearly miss the new-country account, while "success-after-failures" caught it? What does that say about feature design?
2. Your threshold's FP tail includes a service account. In L15 vocabulary, what is the correct verdict, and what are the two remedies (rule-side vs asset-side)?
3. If the log format changed next month (extra field, renamed column), which part of your pipeline breaks first, and who should own the fix?

## 9. Troubleshooting
- `KeyError` on a column → the schema note in the CSV header is authoritative; do not rename.
- Notebook hangs on fit → sample to 10k rows for iteration; fit the full set once for the submission.
- Scores all near-zero → check that you fitted on features only (not the label column).

## 10. Cleanup Instructions
- Remove the CSV and notebook outputs from the VM home after submission.
- No system changes were made; nothing to restore.

## 11. Submission Requirements
- Completed notebook (executed) or `results.md` with: feature table, threshold + precision/recall, correlation narrative, alert text, retune comparison.
- Answers to the three analysis questions.

## 12. Expected Outputs / Evidence
Executed notebook or equivalent report + `alerts.md`; figures may be screenshots of your own run.

---
### Instructor Answer Key (summary — full version in `assessments/instructor-only/`)
- Seeded chains (labels in the instructor-only `labels.csv`): (1) brute-force from 203.0.113.50 → account `svc-backup` (failure streak, no success — pure FP-prone pattern without enrichment); (2) new-country success → `alice` (5 failures then success from 198.51.100.23, then mass reads); (3) off-hours reader → `svc-report` at 03:10–03:40.
- Expected best features: success-after-failures, new-source flag, off-hours ratio; failed-count alone flags (1) but misses (2).
- Threshold @ ≤ 20 alerts/day: precision ≈ 0.7–0.9 depending on tuning; recall ≥ 0.9 on chains (2) and (3); chain (1) is the deliberate FP-tail lesson (benign-true-positive: the real backup service).
- Retune: halving alerts typically drops recall on (3) first — the honest trade-off statement is the graded skill.

### Assessment Rubric (20 pts)
| Criterion | Points |
|---|---|
| Feature engineering (≥ 8, defensible) | 4 |
| Detector + threshold with stated precision/recall | 5 |
| Correlation narrative grounded in raw rows | 4 |
| Alert text (behavior + evidence + action) | 3 |
| Analysis answers | 3 |
| Evidence completeness | 1 |
