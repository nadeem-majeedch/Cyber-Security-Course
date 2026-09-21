# Lecture 24 — Detection Engineering: Metrics, Rules, and the SOC Pipeline + Checkpoint E
**Module 6 · Week 12, Session 2 · 2 hours · CLO-6 (primary), CLO-8 (supporting)**

## Learning Objectives
1. Define detection-engineering metrics: per-rule TPR/FPR, ATT&CK coverage, dwell time.
2. Author, test, and version a detection rule end-to-end (hypothesis → rule → test → tune).
3. Evaluate an ML-assisted triage pipeline against a manual baseline.
4. Consolidate Module 6 (Checkpoint E); submit the case-study brief.

## Key Concepts and Definitions

**Detection-as-code:** rules live in version control with tests and review, and roll out in stages — **shadow** (score only) → **alert** (page the queue) → **block** (automated action, only after evidence). Untested blocking rules are how detection engineering breaks production.

**Rule quality = fidelity + fit:** *fidelity* — does the rule match the intended behavior, not just a string? *fit* — does it alert within the team's budget? Both are measured, per rule: **TPR/FPR** on test events and on production samples.

**Coverage vs. protection:** ATT&CK **coverage** maps which tactics you can *see* (telemetry + rules). It is a visibility claim — 100% coverage guarantees nothing about rule quality or tuning. Say it precisely; dashboards will be misread otherwise.

**The assembled pipeline (the module's payoff):** L21 anomaly pre-filter → L22 classifier → L15-style SIEM rules → human queue — with the **purple-team loop**: synthetic events (safe, atomic-style emulations) validate rules *before* production.

**Metrics that matter:** per-rule precision/recall, coverage by tactic, and **MTTD** (mean time to detect) measured on the synthetic exercises — the number leadership can act on, if presented with its caveats.

## Conceptual Diagram

```text
hypothesis (L03 style) ─► rule draft ─► test events ─► PR review ─► SHADOW ─► ALERT ─► BLOCK
        ▲                                                        │                │
        └──────────────── tune (FP sources, thresholds) ◄────────┴──── metrics ◄──┘
pipeline: anomaly pre-filter ─► classifier ─► SIEM rules ─► human queue
```

## Realistic Examples

- **CS track:** the L13 beacon rule gets a test suite: jittered, bursty, and low-volume variants — tune until all three alert while the backup-agent FP stays silent.
- **DS track:** the metrics dashboard: per-rule precision, coverage heat by tactic, MTTD trend — and the annotation exercise: which number will management misread? (Coverage ≠ protection.)

## Common Misconceptions

| Misconception | Correction |
|---|---|
| "We have a SIEM, so we detect" | The pipeline matters only with hypotheses, tested rules, and tuned thresholds (L15's lesson, now engineered). |
| "Blocking is the goal" | Blocking is the *last* stage, earned by shadow/alert evidence. |
| "Coverage dashboards show protection" | They show visibility; quality lives in per-rule metrics. |
| "The ML pre-filter is set-and-forget" | It can silently degrade; canary events must measure it. |

## Classroom Activities

1. **Rule-authoring workshop (20 min):** from hypothesis to rule for the L13 beacon; students write the test events too.
2. **Checkpoint E (12 min).**
3. **Lab 22 (40 min):** run the full pipeline on a synthetic "day of activity" (40k benign events, 3 embedded attack chains); measure per-rule FPR/TPR; find coverage gaps; produce the dashboard.
4. **Dashboard critique (10 min):** two team dashboards compared; the management-misreading question.

## Discussion Questions

1. What does 100% ATT&CK coverage actually promise — and what does it hide?
2. Shadow-mode rollout delays blocking value; build the risk argument for and against speed.
3. If the L21 pre-filter silently degrades, how long until anyone notices? Design the canary.

## Problem-Solving Exercise

> The synthetic day contains three chains: phish→persistence; brute force; beacon+exfil — among 40k benign events.
> **Deliverable:** which chains your rule set catches end-to-end; the gap per chain; one new rule per gap with a test event; the before/after FPR table.

## Summary

Detection engineering is software engineering with an adversary: versioned rules, tested against emulated behavior, measured honestly per rule, rolled out in stages. Module 6 gave you the analytics — Module 7 moves the battlefield to the platforms hosting all of it.

## Exit Ticket

1. Name the three rollout stages for a rule, in order.
2. What validates a rule before production?
3. Why is coverage-by-tactic a weak proxy for security?

## References

- SigmaHQ, *Sigma rule format* documentation. https://github.com/SigmaHQ/sigma
- MITRE ATT&CK + CTID, *Atomic Red Team* (safe emulation concept). https://atomicredteam.io
- NIST SP 800-94 (IDS context). https://csrc.nist.gov
-MITRE ATLAS (ML-system detection context). https://atlas.mitre.org
