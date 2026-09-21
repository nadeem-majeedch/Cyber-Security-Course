# Teaching Guide — Lecture 24 (Detection Engineering + Checkpoint E)
**Instructor-only.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–08 | Recap: mitigation honesty tables | Two read aloud. |
| 08–30 | Detection-as-code tour | Repo, tests, staged rollout; the untested-blocking-rule story. |
| 30–48 | Rule-authoring workshop | Beacon hypothesis → rule → test events. |
| 48–60 | Break | — |
| 60–72 | **Checkpoint E** | 10 min + most-missed recap. |
| 72–100 | Lab 22 (full pipeline run) | Synthetic day; per-rule metrics; dashboard. |
| 100–112 | Dashboard critique | Which number will management misread? |
| 112–120 | M6 wrap + case-brief collection + M7 preview | Brief collected (10% assessment). |

## Board/Projector Activities

- **Projector:** the detection-as-code repo (PR diff, test events passing); the synthetic-day dashboard live.
- **Board:** the shadow→alert→block ladder with entry criteria written beside each rung.

## Speaker Notes (key beats)

1. Detection-as-code = software engineering discipline: version control, tests, review, staged rollout. The story of the untested blocking rule that paged the whole org is the cautionary tale.
2. Rule quality = fidelity (matches intended behavior) + fit (fits the alert budget) — both measured per rule.
3. Coverage ≠ protection: the dashboard annotation exercise trains students to present metrics with caveats.
4. The pipeline assembled: anomaly pre-filter → classifier → rules → humans. Each stage gets a canary; silent degradation is the enemy.
5. Case-study brief collection: check names/format per the rubric; store in the instructor-only tier.

## Expected Student Difficulties

- Students conflate coverage with quality. Fix: per-rule TPR/FPR vs tactic-coverage table side by side.
- Writing test events feels bureaucratic. Fix: it *is* the purple-team loop — synthetic events are how rules earn trust.
- Checkpoint E: the classic miss is PR-vs-ROC reasoning; recap with the subsample demo callback.

## Teaching Tips

- The synthetic-day dataset is the module's capstone artifact — verify the three chains fire before class; adjust seed if needed.
- Keep the dashboard minimal (three panels: per-rule precision, coverage by tactic, MTTD) — minimalism makes the misreading question sharp.
- The case brief is due: announce the collection point twice (start and break).

## Answer Keys **[KEY]**

- Checkpoint E: see `assessments/instructor-only/checkpoint-keys.md` §E.
- Lab 22 model answers: chain 1 (phish→persistence) caught by classifier + persistence rule; chain 2 (brute force) caught by threshold rule — FP risk from service accounts; chain 3 (beacon+exfil) caught only if the egress-volume rule exists — the gap most teams must fill. New rules must ship with one test event each.
- Exit ticket: 1 shadow → alert → block; 2 test events / purple-team validation; 3 visibility ≠ rule quality or tuning.

## Lab Delivery (Lab 22)

- Minimum viable outcome: per-rule metrics table + one gap filled (rule + test event) + dashboard draft.
- Expected failure points: pipeline ordering errors (classifier before enrichment); the answer-key chain locations must stay instructor-only until after the lab.

## Discussion Facilitation

Q1 (100% coverage) rewards precision of language — collect the two best caveats and keep them for the capstone report template. Q3 (canary design) connects to L22's drift checklist; the union of both is the M6 deployable-system picture.

## Accessibility

- Dashboards: provide the underlying metrics CSV; describe each panel verbally as it loads.
- The synthetic day: the benign-event volume is large — analysis happens on pre-aggregated tables for accessibility and time.
