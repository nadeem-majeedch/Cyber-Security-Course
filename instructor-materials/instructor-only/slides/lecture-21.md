---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L21 · Module 6 · Week 11'
---

<!-- _class: lead -->
# Lecture 21 — DS for Security I
## Log Anomaly Detection
**Module 6 · Week 11 · 120 min · CLO-6 (primary)**

<!--
TIMING: 1 min. Hook: "M4 taught you to SEE anomalies; now we teach the machine — and learn what that costs."
-->

---

# Learning Objectives

1. Engineer features from raw auth logs
2. Fit & tune an **isolation forest**
3. Choose thresholds by SOC capacity (precision/recall)
4. Validate with **time-based** splits

<!--
L15's honest rule returns as code. 3 min.
-->

---

# From logs to features

```
raw:  2026-09-19T02:14 anna ssh 203.0.113.9 FAIL
features: failures/10min · new-country? · hour-z-score
```

*Describe: one raw log line and three derived features; windows and normalization choices accompany each.*

<!--
FEATURES ARE THE MODEL (checkpoint E item 3). Aggregation window = design decision. 6 min.
-->

---

# Isolation forest intuition

```
normal:  deep in random partitions (long path)
anomaly: isolated FAST (short path)
contamination param = expected anomaly share
```

*Describe: two-line intuition plus the key hyperparameter; anomalies separate in few splits.*

<!--
MCQ-6.2. Unsupervised = triage aid, not verdict. 5 min.
-->

---

# Thresholds belong to operations

```
threshold too low  → alert flood → SOC mistrust
threshold too high → silent misses → incidents
choose: max recall subject to precision floor
```

*Describe: three-line tradeoff; the operating point is a human-capacity decision, not a model property.*

<!--
PR curve over ROC under imbalance (MCQ-6.1/SM-4). 5 min.
-->

---

# Validation that doesn't lie

```
random split:   duplicates straddle train/test → inflated F1
time split:     train on past, test on future → honest
```

*Describe: two-line contrast; temporal leakage is the failure mode, time-ordered splits the cure.*

<!--
MCQ-6.4 — the DS students' most transferable lesson. 4 min.
-->

---

# CS example — SSH brute force

- Features: per-source failure velocity, distinct-username count
- Detector output → L15 triage queue, severity-tagged

<!--
2 min.
-->

---

# DS example — drift reality

- SSO migration broke feature distributions (SF-10's scenario)
- Monitoring: PSI/KS on feature drift weekly

<!--
2 min. Drift monitoring is a deliverable in Lab 20.
-->

---

# Lab demo — Lab 20 (log anomaly detection)

- Instructor fits the forest on the course auth dataset, moves the threshold live, shows precision/recall swing
- **MVO:** ROC + PR curves side by side with the chosen operating point justified
- Synthetic dataset v2 (labeled windows documented)

<!--
DEMO 6 min. The PR-vs-ROC gap at 1% prevalence is the visual to remember.
-->

---

# Case session

**CS-055 "3 a.m. tuning call"** (Level 3 · Security monitoring)

→ which knob was wrong: features, threshold, or trust?

<!--
10 min. Model: threshold set without SOC capacity math.
-->

---

# Wrap-up & exit ticket

- Features > models; thresholds are human; time-splits or bust
- **Exit:** one feature for VPN-login anomalies + its window

<!--
Close 110. Preview L22: phishing classification.
-->

---

# References

- scikit-learn isolation forest docs; Chio & Freeman ch. 4
- Lecture plan lecture-21; Lab 20
