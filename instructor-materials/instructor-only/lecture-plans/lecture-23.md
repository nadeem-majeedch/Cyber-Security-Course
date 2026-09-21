# Lecture 23 — Adversarial Machine Learning: Evasion, Poisoning, Extraction
**Module M6 · Week 12, Session 1 · 120 min · CLO-6 (primary) · CLO-4 (supporting)**

## Learning Objectives
1. Execute (in the lab) the three canonical attacks on ML: evasion at inference, poisoning at training, model extraction via queries.
2. Map ML attacks to the MITRE ATLAS adversary-view and to the systems that host models (CLO-4 systems thinking).
3. Apply mitigations and state honestly what each does and does not buy: adversarial training, input sanitization, rate limiting, output abstention.
4. Write a model threat model using the STRIDE-from-L02 lens adapted to ML pipelines.

## Key Concepts
- Evasion: perturbations that flip decisions; feature-space vs. problem-space constraints (a "malicious" feature vector must remain a real attack)
- Poisoning: label flips, backdoor triggers, data-collection poisoning; why security telemetry is a poisoning magnet (attacker controls some inputs)
- Extraction: query-based model theft; watermarking awareness; the API rate-limit as a control
- ATLAS taxonomy; the ML supply chain (pretrained models, datasets) as attack surface
- Robustness-accuracy tension; certification limits (conceptual)

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–08 | Recap L22: model card of the class's phishing classifier | Showcase |
| 08–30 | Evasion demo: perturb the L21 anomaly features to hide a "file-read spike" while keeping the behavior real; decision boundary visual | Live demo |
| 30–50 | Poisoning: the trigger-backdoor storyboard on a synthetic text classifier; how many poisoned samples suffice (concentration math, simplified) | Storyboard |
| 50–60 | Break | — |
| 60–105 | **Lab block (Lab 21):** three stations — (a) evasion against L22's phishing model via feature tweaks + constraints, (b) poisoning 2% of a training set and measuring backdoor success, (c) extraction-lite: reconstruct a decision boundary from API queries; each station ends with the mitigation checklist | Station lab |
| 105–115 | Mitigation honesty table: students fill (attack → mitigation → what it doesn't stop) | Exercise |
| 115–120 | Exit ticket; preview L24 (detection engineering) | Q&A |

## Examples
- **CS track:** evasion in feature space fails in problem space: the tweaked "phishy" URL is unusable by a real actor — students articulate why problem-space constraints matter more than L∞ norms.
- **DS track:** poisoning via the feedback queue (users "report" benign mails as phish to jail competitors' domains) — the trust model of labels is the vulnerability.

## Discussion Questions
1. If an evasion requires the attacker to know the features, does the API boundary help? What leaks feature structure?
2. Why can't we fully clean a poisoned dataset after the fact? What does that imply for data provenance?
3. Is model extraction theft, a vulnerability, or neither — and does the law currently agree?

## Student Activity
Three-station rotation with mitigation write-ups; ML threat-model draft (STRIDE-for-ML on the phishing pipeline).

## Problem-Solving Scenario
> Your L22 model is in production. An insider can submit labels; an external scraper is querying 10k/day. Produce: the ML threat model (assets, adversaries, entry points), the two highest-impact mitigations given a zero-budget constraint, and the monitoring signals that would reveal each attack class first.

## Summary
Models inherit every weakness of their data pipeline plus new ones of their own: evadable at the boundary, poisonable at the source, stealable through the API. Defense is layered like everything else in this course — provenance, monitoring, rate limits, and humility about robustness claims. L24 turns model output into engineered detection.

## Formative Assessment
1. Name the three attack classes and their pipeline stage.
2. Why does feature-space evasion overstate real-world risk?
3. Which mitigation slows extraction most, at what cost?

## Required Resources
- `labs/lab-21-adversarial-ml/` notebooks (3 stations) + the L22 saved model
- MITRE ATLAS site tour; adversarial-examples primer (selected)
- CLO mapping: **CLO-6** (objectives 1–4); **CLO-4** (systems framing).
