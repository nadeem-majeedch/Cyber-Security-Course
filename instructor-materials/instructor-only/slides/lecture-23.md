---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L23 · Module 6 · Week 12'
---

<!-- _class: lead -->
# Lecture 23 — DS for Security III
## Adversarial Machine Learning
**Module 6 · Week 12 · 120 min · CLO-6 (primary), CLO-4 (supporting)**

<!--
TIMING: 1 min. Hook: L22's reworded URLs were a warm-up — "now we attack the model ON PURPOSE."
-->

---

# Learning Objectives

1. Execute sandbox **evasion, poisoning, extraction** demos
2. Map attacks to the **Adversarial ML Threat Matrix**
3. Apply mitigations with their costs
4. Document failure modes (CLO-6 evidence ≥ 3)

<!--
Safety framing: sandbox models/datasets only. 3 min.
-->

---

# The attack trio

```
EVASION:    perturb INPUT at inference      → flip prediction
POISONING:  corrupt TRAINING data           → shift boundary
EXTRACTION: query the API                   → clone the model
```

*Describe: three one-line attack definitions paired with the stage they target — inference, training, deployment.*

<!--
MCQ-6.5/6.6/6.7. Stage-targeting is the exam discriminator. 6 min.
-->

---

# Mitigations and their prices

| Attack | Mitigation | Cost |
|---|---|---|
| Evasion | adversarial training | retrain cycles; blind spots remain |
| Poisoning | source validation, weighting | slower data flow |
| Extraction | rate limits, output noise | API usability drops |

*Describe: three-row mitigation table with explicit costs; every defense buys robustness with something.*

<!--
Checkpoint E SA. SA-6.2 rehearses this. 6 min.
-->

---

# Threat-mapping discipline

```
MITRE ATLAS / Adversarial ML Threat Matrix:
technique ─► stage ─► mitigation ─► residual risk
```

*Describe: four-step mapping chain from technique to residual risk, mirroring the L03 defense-hypothesis template.*

<!--
The L03 template RETURNS for ML — continuity is the point. 4 min.
-->

---

# CS example — malware classifier hardening

- Adversarial training set = perturbation families you EXPECT; document the ones you don't
- Detection on input-entropy anomalies as a tripwire

<!--
2 min.
-->

---

# DS example — feedback-loop poisoning

- Model labels become training labels (CS-068 pattern): quarantine the loop
- Human spot-check tier on auto-labeled data

<!--
2 min. Self-labeled loops are the DS-specific poisoning surface.
-->

---

# Lab demo — Lab 21 (adversarial ML)

- Instructor runs the three sandbox demos: evasion flip, poisoned retrain shift, extraction curve; then adversarial-training recovery
- **MVO:** ≥ 3 documented failure modes WITH mitigations (CLO-6 line)
- Course models/datasets only; no external API probing

<!--
DEMO 7 min. CLO-6's "≥ 3 failure modes documented" is satisfied in this lab — say it.
-->

---

# Case session

**CS-067 "Feature that leaks training data"** (Level 3 · AI security)

→ privacy × ML: which feature betrays, and what's the fix?

<!--
10 min. Model: membership-inference-shaped leak; feature audit.
-->

---

# Wrap-up & exit ticket

- Attacks target stages; mitigations have prices; ATLAS maps them
- **Exit:** one attack→mitigation→cost chain, your choice

<!--
Close 110. Preview L24: detection engineering metrics.
-->

---

# References

- MITRE ATLAS; NIST AI RMF 1.0 (overview); lecture plan lecture-23; Lab 21
