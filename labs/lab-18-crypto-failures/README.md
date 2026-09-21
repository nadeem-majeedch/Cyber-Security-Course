# Lab 18 — Crypto Failure Review
**Enrichment · Module 5 (L20) · CLO-5 (primary), CLO-6 (supporting) · Duration: 2 hours · Check-in lab**

## Learning Objectives
1. Classify named failures into the four-class taxonomy (mode misuse, randomness, protocol logic, implementation).
2. Write one-line design rules per case.
3. Interrogate three fictional vendor crypto pages with challenge questions.
4. Aggregate all Module 5 failures into the pattern wall.

## Prerequisites
Lecture 20 and the case set's public write-ups (linked from `case-studies/`).

## Hardware/Software Requirements
Course VM or paper: the three fictional vendor pages (handouts), the case links (instructor-verified each term), taxonomy worksheet.

## Installation and Setup
None. Pairs for dissection; solo for the vendor pages.

## Ethical Authorization and Safety Notes
- Vendor pages are synthetic teaching artifacts; they do not describe any real product. Never name a real company in your challenge questions.
- Case analysis uses only public, citable write-ups; no speculation beyond the published facts, no invented statistics.
- The exploit narratives you write for cases stay at *researcher-and-disclosure* altitude: what the weakness is, how it was found class-wise, the fix — not operational attack steps.

## Step-by-Step Student Tasks
1. Case 1 (predictable RNG → keys): trace the failure chain; classify; write the design rule.
2. Cases 2–3 (downgrade; hard-coded key): pair-dissect; classify each; one-line rules.
3. Vendor pages A–C: write four challenge questions each — algorithm/mode, randomness, key lifecycle, agility/migration.
4. Read one real CVE description (from the case set's citations); identify its CWE family (327/330/798 class).
5. Pattern wall: place every Module 5 failure (yours and the cases') on the taxonomy grid; photograph.

## Expected Observations
- All three case roots are *usage* failures, not primitive breaks — the module's thesis.
- Vendor page A's red flag: proprietary algorithm + no third-party analysis. B: "AES-256" with no mode or KMS story. C: "military-grade" + no randomness story.
- The CVE you read maps cleanly to one family — the families cover most of what you will meet.

## Questions for Analysis
1. Which failure class is hardest to remediate after deployment, and what does that imply for *when* the design rule must be applied?
2. Your vendor-page questions: which one would the vendor most likely fail, and what does that predict about the product's real security posture?

## Troubleshooting
Cases read as "the algorithm was broken" → re-check: the taxonomy puts nearly everything in usage/key custody; find the actual misused seam. Vendor questions too vague ("is it secure?") → the four slots force specificity.

## Cleanup Instructions
Paper exercise; return handouts; keep the pattern-wall photo for the capstone reference.

## Submission Requirements
Case classifications + design rules (3), vendor challenge questions (3 × 4), CVE family identification, pattern-wall photo.

## Expected Outputs / Evidence
Design rules must be actionable ("use AES-GCM with per-message random nonces from the OS CSPRNG"), not aspirational ("be careful with crypto").

---
### Instructor Answer Key (summary)
- Classifications (model): RNG case → randomness (CWE-330/338) — rule: vetted CSPRNG + entropy health checks; downgrade case → protocol logic — rule: fail closed, no silent downgrades; hard-coded key → implementation (CWE-798) — rule: per-device keys, keys out of code.
- Vendor page expected fails: A fails the algorithm/analysis question; B fails mode+KMS; C fails randomness+lifecycle.
- CVE mapping: accept any from the term's cited set; the family, not the number, is graded.

### Assessment Rubric (10 pts — check-in)
| Criterion | Points |
|---|---|
| Three classifications + actionable design rules | 4 |
| Vendor challenge questions (specific, four-slot) | 3 |
| CVE family identification | 1 |
| Pattern-wall synthesis | 2 |
