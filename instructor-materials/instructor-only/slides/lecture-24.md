---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L24 · Module 6 · Week 12'
---

<!-- _class: lead -->
# Lecture 24 — Detection Engineering
## Metrics, Rules & Checkpoint E
**Module 6 · Week 12 · 120 min · CLO-6 (primary), CLO-8 (supporting)**

<!--
TIMING: 1 min. Hook: "a rule without numbers is a rumor." Checkpoint E at min 100.
-->

---

# Learning Objectives

1. Define FPR/TPR/precision/recall for **operations**
2. Take a rule through **shadow → alert → block**
3. Write coverage statements (incl. what's NOT covered)
4. Demonstrate Module 6 mastery (Checkpoint E)

<!--
This lecture turns M6's math into M8's capstone deliverables. 3 min.
-->

---

# The metrics that drive decisions

```
TPR (recall):  of real attacks, how many caught?
FPR:           of benign events, how many alarm?
precision:     of alerts, how many real?   ← SOC's daily life
```

*Describe: three metric definitions with their operational meaning; precision is what analysts feel.*

<!--
SF-4's arithmetic (0.9/0.2 on 10k events) is the drill — do it live. 5 min.
-->

---

# Rollout discipline

```
SHADOW (log only, measure on live traffic)
  → ALERT (humans decide)
    → BLOCK (only after measured FP weeks)
```

*Describe: three-stage rollout staircase; enforcement follows evidence, never precedes it.*

<!--
MCQ-6.8. Each arrow needs a metric threshold — name them. 5 min.
-->

---

# Coverage statements — honest maps

```
WE DETECT:    T1110 brute force (TPR .85, FPR .04)
WE DO NOT:    insider exfil via personal cloud
BECAUSE:      no egress DLP telemetry (roadmap Q3)
```

*Describe: three-line coverage statement pairing detections with explicit non-coverage and its reason.*

<!--
FE-F rewards exactly this shape. "We monitor everything" = automatic deduction. 5 min.
-->

---

# CS example — regression testing detections

- Unit tests for rules: replay labeled dataset → assert TPR/FPR bounds in CI
- Rule change without metrics = rejected PR

<!--
2 min.
-->

---

# DS example — the metrics dashboard

- Weekly: precision by rule, FP top-offenders, drift flags
- Metrics that move nothing (CS-072) = vanity — tie each to an action

<!--
2 min. CS-072 pairs perfectly here.
-->

---

# Lab demo — Lab 22 (detection engineering)

- Instructor takes the L21 rule through shadow mode on the course feed, produces its measured numbers
- **MVO:** one rule with TPR/FPR measured on live-class traffic
- Course dataset only

<!--
DEMO 5 min. This rule's numbers appear in checkpoint E and the capstone rubric.
-->

---

# Checkpoint E — last 20 minutes

- 8 items: imbalance, isolation forest, features, PR vs ROC, leakage, rollout + 2 scenarios
- From `quizzes/quiz-12.md`

<!--
ADMIN at 100. M6 complete. Case-brief deadline is THIS week — remind.
-->

---

# Case session (if time)

**CS-085 "Detection debt"** (Level 4 · Security monitoring)

→ rule backlog as technical debt: triage it.

<!--
Optional 8 min; strong L4 practice for case-brief writers.
-->

---

# Wrap-up

- Numbers or silence; rollouts in stages; coverage includes the gaps
- **Reading:** L25 notes; cloud sandbox check

<!--
Close. M6 complete — log checkpoint E; collect case briefs.
-->

---

# References

- Lecture plan lecture-24; Lab 22; case-brief rubric
