# Lecture 20 — Cryptographic Failures in the Wild + Checkpoint D
**Module M5 · Week 10, Session 2 · 120 min · CLO-5 (primary) · CLO-6 (supporting)**

## Learning Objectives
1. Dissect named real-world crypto failures and classify each root cause (mode misuse, randomness, protocol logic, implementation).
2. Extract design rules from failure patterns ("never roll your own," "randomness is a feature," "protocol + implementation both fail").
3. Evaluate a vendor's crypto claims from a spec sheet (the "military-grade encryption" trap).
4. Apply Checkpoint D consolidation of Module 5.

## Key Concepts
- Failure taxonomy: weak randomness (seeded PRNGs), nonce reuse, fallback downgrade paths, padding oracles (concept), hard-coded keys, home-made ciphers
- Case set (each with public write-up, cited in `case-studies/`): a RNG-predictable-keys incident, a downgrade-attack protocol story, a hardcoded-key app harvest, a mode-misuse data exposure
- Crypto agility: what made these systems unpatchable or patchable
- Reading CVE crypto entries: what the vectors mean (CWE-327, CWE-330, CWE-798 families)

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–08 | Recap L19: benchmark results table | Q&A |
| 08–30 | Case 1 walk-through: predictable RNG → predictable keys; students trace the failure chain and propose the design rule | Case analysis |
| 30–48 | Cases 2–3 rapid dissection in pairs: each pair classifies root cause + writes the one-line design rule; pairs present | Pair dissection |
| 48–60 | Break | — |
| 60–72 | **Checkpoint D** (Module 5 quiz) | Assessment |
| 72–95 | **Lab block (Lab 18):** vendor-claim review — three fictional product crypto pages (red flags: proprietary cipher, no mode named, "military-grade," no KMS); students write the challenge questions | Exercise |
| 95–110 | Failure-pattern wall: class aggregates all M5 failures into a pattern board (mode/randomness/logic/implementation) | Synthesis |
| 110–120 | Module 5 wrap; M6 preview (DS for security) | Q&A |

## Examples
- **CS track:** a firmware update signing story: hardcoded verification key → harvest campaign; students map to CWE-798 and the HSM/vault fix.
- **DS track:** a telemetry archive encrypted with per-record ECB + a static key derived from a timestamp — pattern leakage across records; students design the re-encryption plan (ties to L17's migration thinking).

## Discussion Questions
1. "Don't roll your own crypto" — but someone must. Who should, with what process, and how do the rest of us verify?
2. Which failure class is hardest to patch retroactively, and why (data at rest vs. code)?
3. What three questions unmask marketing crypto claims fastest?

## Student Activity
Case dissection in rotating pairs; vendor-claim challenge questions; pattern-wall synthesis.

## Problem-Solving Scenario
> An IoT camera line: "AES-256" in the spec, no mode named, firmware contains the same key string across devices, and a debug RNG seeds from uptime. Produce: the four defects with classification, the exploit narrative a researcher would follow (responsible-disclosure framing), and the remediation spec (mode, KMS, RNG source) with the recall/OTA patch strategy.

## Summary
Crypto fails at the seams: randomness, modes, protocol logic, and key custody — rarely at the primitive itself. Design rules beat heroics: standard libraries, AEAD defaults, real randomness, keys out of code. Module 6 now weaponizes data science for defense — and examines attacks on the models themselves.

## Formative Assessment
1. CWE-330 covers what failure class?
2. Why is data-at-rest crypto failure worse to remediate than code failure?
3. Name the red flag in "proprietary military-grade algorithm."

## Required Resources
- `labs/lab-18-crypto-failures/` vendor-page handouts + case write-ups (cited)
- CWE-327/330/798 pages; case bibliography in `case-studies/`
- CLO mapping: **CLO-5** (objectives 1–4); **CLO-6** seed (failure analytics mindset).
