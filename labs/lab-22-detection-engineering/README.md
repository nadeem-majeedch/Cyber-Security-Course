# Lab 22 — Detection Engineering Pipeline
**Enrichment · Module 6 (L24) · CLO-6 (primary), CLO-8 (supporting) · Duration: 2 hours · Check-in lab**

## Learning Objectives
1. Run the assembled pipeline (anomaly pre-filter → classifier → SIEM rules → human queue) on a synthetic day of activity.
2. Measure per-rule TPR/FPR and identify coverage gaps against three embedded attack chains.
3. Author one new rule per gap **with a test event** (detection-as-code).
4. Build the metrics dashboard and annotate the number management will misread.

## Prerequisites
Lectures 21–24; Labs 14/19/20 outputs (this lab reuses their artifacts).

## Hardware/Software Requirements
Course VM: Python 3.10+, the synthetic-day dataset `synthetic-day-v2.csv` (~40k benign events, 3 seeded chains — chain locations are instructor-side until after the lab), rule templates, dashboard notebook `starter/dashboard.ipynb`.

## Installation and Setup
```bash
python -c "import pandas, sklearn; print('ok')"
jupyter notebook starter/dashboard.ipynb
```

## Ethical Authorization and Safety Notes
- The dataset is synthetic; chains are seeded patterns (auth anomalies, beacon timing, staged egress), not executable attack content.
- Rules you write are detection logic for course data only; nothing here is deployed or pointed at real telemetry.

## Step-by-Step Student Tasks
1. Run the pipeline end-to-end on the synthetic day; export per-rule alert lists.
2. **Chain hunt:** correlate alerts into chains; state which of the three chains your rule set catches end-to-end, partially, or misses.
3. Per-rule metrics: TPR/FPR table against your rules (the benign mass defines the FPR denominator).
4. Gap analysis: for each partially-caught/missed chain — the missing telemetry or missing rule.
5. Author one new rule per gap **plus its test event** (a synthetic row that must fire it).
6. Staged rollout plan: shadow → alert → block, with entry criteria per stage.
7. Dashboard: per-rule precision, coverage by tactic, MTTD trend; annotate the number management will misread.

## Expected Observations
- Chain 1 (phish→persistence): caught (classifier + persistence rule).
- Chain 2 (brute force): caught, with the service-account FP tail from Lab 19.
- Chain 3 (beacon+exfil): **partially** caught by most rule sets — the egress-volume rule is the usual gap (this is the designed lesson).
- New rules without test events are the most common rubric loss.

## Questions for Analysis
1. Your dashboard shows coverage by tactic near 80%. Write the one-sentence caveat that must accompany that number in a management report.
2. The beacon rule fired on the backup agent in Lab 12's discussion — where does your new egress rule's "backup-agent exception" live: in the rule, in the asset registry, or in the analyst's head? Defend your placement.

## Troubleshooting
Pipeline skips the classifier stage → stage order matters (pre-filter → classifier → rules); check the notebook's stage flags. Test event doesn't fire your rule → field-name mismatch against the dataset schema (header note). Chain 2 floods your metrics → exclude its service-account FP in the *annotated* metric, never silently.

## Cleanup Instructions
Remove the dataset and dashboard outputs; keep your rules + test events (they feed the capstone's detection content).

## Submission Requirements
Chain verdict table (3 chains), per-rule metrics, gap analysis, new rule(s) + test events, rollout plan, dashboard screenshot/figures + the management caveat.

## Expected Outputs / Evidence
Rules ship as rule+test pairs; a rule without a passing test event is not a deliverable — it is a hope.

---
### Instructor Answer Key (summary)
- Seeded chains: (1) phish→persistence (rows 4,100–4,180), (2) brute force `svc-backup` (rows 12,900–12,980), (3) beacon+egress (rows 30,010–30,900 + egress rows 31,200–31,260).
- Expected gap: chain 3's egress-volume leg — new rule (model): `egress_bytes > 5× 7-day median per host → alert` with test event = the seeded egress rows.
- Metrics expectations: chain rules TPR ≥ 0.9; fleet FPR dominated by chain 2's service account; annotated metric = "coverage by tactic" (visibility ≠ protection).
- Rollout entry criteria: shadow (fires on test events, no ops impact) → alert (FPR ≤ budget on 7-day sample) → block (two clean alert-weeks + rollback runbook).

### Assessment Rubric (10 pts — check-in)
| Criterion | Points |
|---|---|
| Chain verdicts with alert-correlation evidence | 3 |
| Per-rule metrics + gap analysis | 2 |
| New rule(s) with passing test events | 3 |
| Dashboard + management caveat | 2 |
