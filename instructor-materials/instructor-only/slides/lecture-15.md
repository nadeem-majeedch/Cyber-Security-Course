---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L15 · Module 4 · Week 8'
---

<!-- _class: lead -->
# Lecture 15 — Network Security III
## IDS/IPS & SIEM Triage
**Module 4 · Week 8 · 120 min · CLO-4 (primary)**

<!--
TIMING: 1 min. Hook: "the network speaks; IDS is grammar, SIEM is the librarian."
-->

---

# Learning Objectives

1. Contrast signature vs anomaly IDS tradeoffs
2. Place sensors for east-west visibility
3. Triage a SIEM queue (enrich, correlate, decide)
4. Write one detection rule with honest metrics

<!--
Metrics here seed L24's detection engineering. 3 min.
-->

---

# Signature vs anomaly

```
Signature:  known patterns ──► low FP, blind to novelty
Anomaly:    baseline deviation ──► catches new, FP-heavy
```

*Describe: two-line contrast; the tradeoff pairs detection breadth with alert noise.*

<!--
MCQ-4.5 / SM-10 territory. Neither wins — placement does. 4 min.
-->

---

# Placement — where sensors earn their keep

```
edge: sees internet ── but never sees lateral movement
inter-zone choke points: sees east-west ── the real battles
```

*Describe: two placement options; only inter-zone sensors observe lateral movement.*

<!--
SM-7. Tie to L14's choke points — sensors live where policies log. 4 min.
-->

---

# The SIEM triage loop

```
alert ─► enrich (asset value, intel) ─► correlate (related events)
      ─► decide (escalate / close / tune) ─► feedback to rules
```

*Describe: five-step loop; the feedback arrow back to rules is what reduces future noise.*

<!--
MT-SA (400 alerts/night) is the drill. FP-rate + MTT-triage as tracked metrics. 6 min.
-->

---

# Writing one honest rule

```
WHEN >5 failed SSH logins / 5 min from one source
AND  ≥3 distinct usernames
THEN alert, severity medium
MEASURED: TPR 0.85, FPR 0.04 (course dataset, week 6)
```

*Describe: a complete detection rule with condition, action, and measured performance figures.*

<!--
MEASURED is the word that separates engineering from wishful thinking — L24 requires it. 5 min.
-->

---

# CS example — IPS tradeoff

- Inline IPS blocks a scan wave — and breaks a legitimate scanner
- Rule: alert-mode first, block after measured FP weeks

<!--
2 min.
-->

---

# DS example — the SIEM as data product

- Alert queue = model output feeding humans; enrichment = features
- Alert-fatigue metric ≈ precision — same math as M6

<!--
2 min. M6's threshold-setting previews here.
-->

---

# Lab demo — Lab 14 (SIEM triage)

- Instructor triages the course alert queue live: enrich one, correlate two, tune one rule
- **MVO:** queue shrinks with justification for each action
- Course dataset only

<!--
DEMO 6 min. Keep the tuning evidence — it feeds L24.
-->

---

# Case session

**CS-039 "Alert nobody owned"** (Level 2 · Security monitoring)

→ where in the triage loop did this alert die?

<!--
10 min. Model: ownership + feedback arrows missing.
-->

---

# Wrap-up & exit ticket

- Tradeoffs by placement; loops close; rules carry numbers
- **Exit:** one sentence — why is edge-only IDS blind to lateral movement?

<!--
Close 110. Preview L16: wireless/VPN + MIDTERM.
-->

---

# References

- Bejtlich ch. 2–3; lecture plan lecture-15; Lab 14
