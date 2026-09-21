# Lecture 23 — Adversarial Machine Learning: Evasion, Poisoning, Extraction
**Module 6 · Week 12, Session 1 · 2 hours · CLO-6 (primary), CLO-4 (supporting)**

## Learning Objectives
1. Execute (in the lab) the three canonical ML attack classes: evasion, poisoning, extraction.
2. Map ML attacks to the MITRE ATLAS taxonomy and to the systems hosting models.
3. Apply mitigations and state honestly what each does and does not buy.
4. Write a model threat model using STRIDE adapted to ML pipelines.

## Key Concepts and Definitions

**Evasion (at inference):** craft inputs that flip decisions. Feature-space perturbations must obey **problem-space constraints** — a "modified" phish must still be a *usable* phish. *Fact:* many reported adversarial examples fail this usability test; feature-space wins overstate real-world risk.

**Poisoning (at training):** corrupt the training data. Classes: **label flips**, **backdoor triggers** (a specific pattern in input → attacker-chosen output), and **collection poisoning** (attacker controls some of what you ingest — security telemetry is a magnet for this). The concentration question: how few poisoned samples suffice? For backdoors, surprisingly few — which is why *data provenance* is the control.

**Extraction (via API):** reconstruct the model by querying it (steal the model or its decision boundary). Controls: rate limiting, query-pattern monitoring, output abstention, watermarking (research maturity varies — state it honestly).

**MITRE ATLAS:** the ATT&CK-style knowledge base for ML-system attacks (recon, poisoning, evasion, exfiltration classes) — the vocabulary for the threat model.

**Mitigation honesty table (the lecture's spine):**

| Attack | Mitigation | What it does NOT stop |
|---|---|---|
| Evasion | Adversarial training, input validation/sanitization, ensembles | Novel attacks outside the training distribution |
| Poisoning | Data provenance, label QA, outlier screening of training data | Well-mixed, low-volume poisoning |
| Extraction | Rate limits, anomaly-monitored APIs, watermarking | Determined, patient, low-and-slow extraction |

**Robustness–accuracy tension:** hardening against perturbations typically costs clean accuracy; certification exists only for narrow regimes. Claims should be scoped, not absolute.

## Conceptual Diagram

```text
TRAINING:   data sources ─► label QA ─► training ─► model      ◄── poisoning lives here
INFERENCE:  input ─► model ─► score ─► decision ─► API         ◄── evasion (input) ·
                                                                 extraction (API)
STRIDE-for-ML: S=spoofed sources/labels  T=tampered training data  I=model theft
               R=who trained/deployed?   D=score flooding      E=shell via pipeline
```

## Realistic Examples

- **CS track:** evasion in feature space vs. problem space: the perturbed "phishy" URL is *unusable* by a real actor — students articulate why problem-space constraints matter more than L∞ norms.
- **DS track:** poisoning via the *feedback queue*: users "report" benign mails as phish to get competitors' domains jailed — the trust model of labels is the vulnerability; mitigation is label QA and reporting-rate anomaly checks.

## Common Misconceptions

| Misconception | Correction |
|---|---|
| "Adversarial examples = glasses fooling face recognition, therefore ML is useless" | Those demos often ignore real-world constraints; lab perturbations ≠ feasible attacks. |
| "We cleaned the dataset, so we're safe" | Post-hoc cleaning cannot prove the absence of well-mixed triggers; prevention (provenance) beats cure. |
| "Rate limiting stops extraction" | It slows it; low-and-slow extraction is an economics game, not a wall. |
| "Adversarial training = robust" | It raises cost against *known* attack classes; novel classes remain open. |

## Classroom Activities

1. **Evasion demo (15 min):** perturb the L21 features to hide a "file-read spike" while keeping the behavior real; decision-boundary visual.
2. **Lab 21 (45 min):** three stations — evasion on L22's model (with constraints), poisoning 2% and measuring backdoor success, extraction-lite via queries; each ends with a mitigation checklist.
3. **Honesty table (10 min):** fill attack → mitigation → what-it-doesn't-stop.

## Discussion Questions

1. If evasion requires knowing the features, does the API boundary help? What leaks feature structure?
2. Why can't we fully clean a poisoned dataset after the fact? What does that imply for provenance investment?
3. Is model extraction theft, a vulnerability, or neither — and what does current law actually say?

## Problem-Solving Exercise

> Your L22 model is in production. An insider can submit labels; an external scraper queries 10k/day.
> **Deliverable:** the ML threat model (assets, adversaries, entry points — ATLAS vocabulary); the two highest-impact mitigations under a zero-budget constraint; the monitoring signals that would reveal each attack class first.

## Summary

Models inherit every weakness of their data pipeline plus new ones: evadable at the boundary, poisonable at the source, stealable through the API. Defense is layered — provenance, label QA, rate limits, monitoring — and claims stay scoped. Next: turning model output into engineered detection.

## Exit Ticket

1. Name the three attack classes and the pipeline stage each targets.
2. Why does feature-space evasion overstate real-world risk?
3. Which mitigation slows extraction most, at what cost?

## References

- MITRE ATLAS. https://atlas.mitre.org
- Biggio, B. & Roli, F., "Wild Patterns: Ten Years After the Rise of Adversarial ML," *Pattern Recognition*, 2018.
- NIST AI 100-2, *Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations*. https://csrc.nist.gov
- NIST AI RMF 1.0. https://www.nist.gov/itl/ai-risk-management-framework
