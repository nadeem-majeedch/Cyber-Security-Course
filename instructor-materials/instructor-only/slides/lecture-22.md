---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L22 · Module 6 · Week 11'
---

<!-- _class: lead -->
# Lecture 22 — DS for Security II
## Phishing Classification Pipeline
**Module 6 · Week 11 · 120 min · CLO-6 (primary)**

<!--
TIMING: 1 min. Hook: "a classifier is a policy" — every false positive is a blocked invoice.
-->

---

# Learning Objectives

1. Build features that survive attacker rewording
2. Train/evaluate a phishing URL classifier honestly
3. Manage **feature drift** and label quality
4. Deploy behind human review with measured FPR

<!--
Lab 20-2 is this pipeline. Robustness is the theme. 3 min.
-->

---

# Features that generalize

```
weak:   contains "login"          (attacker: delete word)
strong: domain age, TLS age, path depth, ASN reputation
```

*Describe: weak-vs-strong feature contrast; lexical tokens die to rewording, structural/registration features survive.*

<!--
MCQ-6.3. Adversary-in-the-training-loop thinking starts here. 5 min.
-->

---

# Label hygiene

```
labels from: user reports + verified feeds
noise:  reported ≠ malicious (newsletters!)
fix:    triage layer before labeling; document the error rate
```

*Describe: three-line label pipeline; report-derived labels carry newsletter noise that must be triaged and quantified.*

<!--
Garbage labels beat garbage features for damage. 4 min.
-->

---

# Honest evaluation

```
time split (labels age!) · stratify by campaign, not by URL
report: PR-AUC, FPR at chosen threshold, latency budget
```

*Describe: evaluation-protocol line plus the reporting triple; campaign-stratification avoids near-duplicate leakage.*

<!--
Random splits on campaigns = leakage (MCQ-6.4 again, new costume). 5 min.
-->

---

# CS example — API gateway integration

- Classifier scores at the mail gateway; ≥ 0.9 F1 target from CLO-6
- Human review queue for the gray band — automation assists, decides never

<!--
2 min.
-->

---

# DS example — drift playbook

- Weekly: feature-distribution shift check; monthly: retrain on fresh labels
- Rollback model = versioned artifacts + shadow evaluation (L24 rollout)

<!--
2 min.
-->

---

# Lab demo — Lab 20 part B (phishing classifier)

- Instructor trains the sandbox URL classifier, attacks it with reworded held-out URLs, shows F1 drop, then hardens features
- **MVO:** before/after robustness numbers on the adversarial slice
- Synthetic URL corpus; no live phishing traffic

<!--
DEMO 6 min. The reworded-URL drop motivates L23's whole module.
-->

---

# Case session

**CS-068 "Poisoned by the crowd"** (Level 3 · AI security)

→ which pipeline stage did the attacker target?

<!--
10 min. Model: public label submission = untrusted training channel.
-->

---

# Wrap-up & exit ticket

- Generalizing features, clean labels, time-split, human in the loop
- **Exit:** name one weak feature and its adversarial fix

<!--
Close 110. Preview L23: adversarial ML.
-->

---

# References

- Chio & Freeman ch. 6; lecture plan lecture-22; Lab 20
