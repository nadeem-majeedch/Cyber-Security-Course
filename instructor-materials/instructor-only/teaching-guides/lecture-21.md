# Teaching Guide — Lecture 21 (Anomaly Detection in Logs)
**Instructor-only.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–10 | Hook: SOC alert flood screenshot | "Your job: make this survivable." |
| 10–32 | Telemetry → features | Auth log parsed live; class proposes ≥ 5 features. |
| 32–52 | Isolation forest intuition + demo | Score distribution; threshold slider live. |
| 52–60 | Break | — |
| 60–105 | Lab 19 (notebook) | Features → model → budget threshold → alert text. |
| 105–115 | Threshold debate | High-recall vs high-precision teams. |
| 115–120 | Exit ticket + preview | Tease L22: "labels change everything." |

## Board/Projector Activities

- **Projector:** the notebook with the score histogram; the threshold slider moving precision/recall in real time.
- **Board:** the feature table (proposed features × who benefits) — a running asset for L22.

## Speaker Notes (key beats)

1. Open with prevalence: 40k benign, 40 attacks — compute the "always benign" confusion matrix live; accuracy dies visibly.
2. Features encode *behavior*, not raw logs: off-hours ratio, failure streak, new-source flag. Feature quality > model choice at this scale.
3. Isolation-forest intuition in one sentence: "anomalies are easy to isolate — few random cuts."
4. Alert budget: 15–20/day is the constraint that picks the threshold; precision/recall is the language of that choice.
5. The alert text deliverable: behavior + evidence + suggested action — L15's discipline with model output.

## Expected Student Difficulties

- CS students' ML anxiety: the lab is deliberately two scikit-learn calls; the *thinking* is the feature design.
- DS students' protocol anxiety: the log format is pre-parsed in the starter; say so.
- Threshold debates collapse into taste. Fix: the budget constraint decides — both teams must show their precision/recall numbers.

## Teaching Tips

- Seed the "CEO travel week" anomaly into the demo so enrichment's necessity is experienced, not asserted.
- Keep the model choice fixed (isolation forest); mention alternatives verbally — the lesson is the frame, not the algorithm zoo.
- Collect the three best feature proposals; they open L22's feature engineering.

## Answer Keys **[KEY]**

- Lab 19 model answers: separating features = new-source-success-after-failures, failure-streak, off-hours flag; threshold for ≤ 20 alerts/day is dataset-dependent — accept any threshold with its precision/recall stated; alert text must name behavior, cite evidence rows, suggest first action.
- Exit ticket: 1 accuracy ignores prevalence (degenerate classifier wins); 2 expected anomaly proportion (prior for scoring shape); 3 any two of failed-streak, new-source, off-hours ratio.

## Lab Delivery (Lab 19)

- Minimum viable outcome: ≥ 8 features + fitted model + threshold with stated precision/recall + one alert text.
- Expected failure points: notebook environment drift (pin requirements); students tune contamination to hit the budget backwards — require the precision/recall *report*, not just the number.

## Discussion Facilitation

Q2 (CEO anomaly) lands the enrichment lesson: the model flags deviation; *context* (travel calendar) makes it a BTP — L15's verdict vocabulary returns. Q3 (ownership) is a governance seed for L27/L28 — who owns the model is an accountability question.

## Accessibility

- Notebooks: provide the executed notebook with outputs as HTML (screen-reader navigable) alongside the .ipynb.
- The threshold slider: describe the precision/recall movement aloud as it moves; the CSV of scores lets students reproduce the trade-off table at their own pace.
