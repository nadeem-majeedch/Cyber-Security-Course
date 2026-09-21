---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L27 · Module 7 · Week 14'
---

<!-- _class: lead -->
# Lecture 27 — Cloud Security III
## Audit, Detection & Misconfiguration
**Module 7 · Week 14 · 120 min · CLO-7 (primary)**

<!--
TIMING: 1 min. Hook: "who deleted the bucket?" — control-plane logs or silence forever.
-->

---

# Learning Objectives

1. Distinguish control-plane vs data-plane telemetry
2. Build the minimum cloud detection set
3. Run misconfiguration scanning in CI (policy-as-code)
4. Detect **drift** between declared and deployed state

<!--
Lab 25 wires these together. 3 min.
-->

---

# Two planes, two log types

```
control plane: WHO did WHAT to the infrastructure  (audit logs)
data plane:    WHO accessed WHICH data             (flow/access logs)
```

*Describe: two-line distinction; infrastructure actions vs data access, both needed, neither substitutes.*

|
<!--
MCQ-7.5 (checkpoint F item 4). "Who deleted the bucket" lives ONLY in control-plane audit. 4 min.
-->
|

---

# Minimum detection set (cloud)

```
1. IAM role/policy changes        2. public-exposure changes
3. key creation/use anomalies     4. logging DISABLING
```

*Describe: four-item priority list; disabling logging is the attacker's second move — alert on it first.*

<!--
Priority argues itself: identity + exposure + evidence destruction. 5 min.
-->

---

# Policy-as-code & drift

```
IaC declares ──► CI policy scan ──► deploy ──► drift detect
     (public bucket? blocked HERE, not at 2 a.m.)
```

*Describe: four-stage pipeline; misconfigurations are rejected at build, drift between declared and deployed state is detected continuously.*

<!--
MCQ-7.6 + checkpoint F item 5. Console changes = drift's favorite cause. 5 min.
-->

---

# CS example — multi-account guardrails

- Organization-level SCPs: nobody can disable logging anywhere — including admins
- Guardrails ≠ policies you hope people follow

<!--
2 min. CS-088's landing-zone lesson in miniature.
-->

---

# DS example — dataset bucket watchtower

- Alerts on public ACL changes to feature-store buckets
- Access-pattern anomaly on data-plane logs → L21 detector, cloud edition

<!--
2 min.
-->

---

# Lab demo — Lab 25 (cloud audit)

- Instructor enables audit logging, makes a console change (drift), shows the scanner catching it, then fixes via IaC
- **MVO:** drift event → alert → reconciled state, all demonstrated
- Course sandbox account/LocalStack only

<!--
DEMO 6 min. The drift arc (declare → change → detect → reconcile) is the full lesson.
-->

---

# Case session

**CS-063 "Cross-tenant curiosity"** (Level 3 · Cloud security)

→ which control-plane signal would have caught the probing?

<!--
10 min. Model: anomaly on cross-account role assumptions.
-->

---

# Wrap-up & exit ticket

- Two planes; four detections; policy-as-code; drift is continuous
- **Exit:** which detection fires first when an attacker disables logging?

<!--
Close 110. Preview L28: privacy engineering.
-->

---

# References

- CIS Benchmarks (logging sections); lecture plan lecture-27; Lab 25
