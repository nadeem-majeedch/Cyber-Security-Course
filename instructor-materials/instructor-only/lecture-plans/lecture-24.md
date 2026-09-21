# Lecture 24 — Detection Engineering: Metrics, Rules, and the SOC Pipeline + Checkpoint E
**Module M6 · Week 12, Session 2 · 120 min · CLO-6 (primary) · CLO-8 (supporting)**

## Learning Objectives
1. Define detection-engineering metrics: TPR/FPR per rule, coverage vs. ATT&CK, dwell time, MTTR feed-in.
2. Author, test, and version a detection rule end-to-end (hypothesis → rule → test against synthetic event → tune).
3. Evaluate an ML-assisted triage queue against a manual baseline (builds on L21–L23).
4. Apply Checkpoint E consolidation of Module 6; collect the case-study brief (assessment).

## Key Concepts
- Detection-as-code: rules in version control, tests, peer review, rollout stages (shadow → alert → block)
- Rule quality: fidelity (does it match intent?), alert budget fit, ATT&CK coverage mapping
- The triage pipeline assembled: L21 anomaly pre-filter, L22 classifier, L15-style SIEM rules, human queue
- Purple-team testing loop: synthetic events (atomic-red-team-style, safe emulation) validate rules before production
- Metrics that matter: FPR by rule, coverage by tactic, mean time-to-detect in the synthetic exercises

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–08 | Recap L23: mitigation honesty tables | Q&A |
| 08–30 | Detection-as-code tour: repo, PR review, test events, staged rollout; failure story of an untested blocking rule | Slides + story |
| 30–48 | Rule-authoring workshop: from hypothesis (L03-style) to a concrete rule for the L13 beacon; students write test events | Workshop |
| 48–60 | Break | — |
| 60–72 | **Checkpoint E** (Module 6 quiz) | Assessment |
| 72–100 | **Lab block (Lab 22):** capstone-of-module: run the full pipeline on a synthetic day-of-activity dataset (includes 3 embedded attack chains); measure per-rule FPR/TPR, coverage gaps, and produce the metrics dashboard | Hands-on |
| 100–112 | Metrics critique: two team dashboards compared; what metric would mislead management? | Discussion |
| 112–120 | Module 6 wrap; M7 preview (cloud); case-study brief submission collected | Admin |

## Examples
- **CS track:** the beacon rule from L13 gets a test suite: three synthetic variants (jittered, bursty, low-volume) — students tune until all three alert without firing on the backup-agent FP.
- **DS track:** the dashboard: per-rule precision, coverage heat by tactic, MTTD trend; students annotate one metric that management will misread (coverage ≠ protection).

## Discussion Questions
1. What does 100% ATT&CK coverage actually promise? Nothing — discuss what it hides.
2. Shadow-mode rollout delays blocking value — build the risk argument for and against speed.
3. If the ML pre-filter (L21) silently degrades, how long until anyone notices? Design the canary.

## Student Activity
Rule authoring with test events; pipeline run + dashboard production; critique exchange.

## Problem-Solving Scenario
> Synthetic day: 3 attack chains (phish → persistence; brute force; beacon+exfil) among 40k benign events. Produce: which chains your rule set catches end-to-end, the gap per chain, one new rule per gap with a test event, and the updated dashboard with before/after FPR.

## Summary
Detection engineering is software engineering with an adversary: versioned rules, tested against emulated behavior, measured honestly, rolled out in stages. Module 6 gave students the analytics; Module 7 moves the battlefield to the platforms hosting all of it.

## Formative Assessment
1. Name the three rollout stages for a rule.
2. What validates a rule before production?
3. Why is coverage-by-tactic a weak proxy for security?

## Required Resources
- `labs/lab-22-detection-engineering/` pipeline + synthetic day dataset
- Sigma-rule format intro (selected); ATT&CK coverage template
- **Case-study brief collection** (assessment, 10% weight)
- CLO mapping: **CLO-6** (objectives 1–4); **CLO-8** seed (pipeline synthesis).
