# Lab 11 — Awareness Campaign Design
**Enrichment · Module 3 (L12) · CLO-3 · Duration: 2 hours · Check-in lab**

## Learning Objectives
1. Dissect three synthetic phishing samples with SPF/DKIM/DMARC verdicts.
2. Analyze a BEC storyboard and identify pretext markers.
3. Design an awareness campaign with consented simulations and defensible metrics.
4. Map compensating controls (incl. phishing-resistant MFA) to each lure type.

## Prerequisites
Lecture 12. No tooling; this is an analysis + design lab.

## Hardware/Software Requirements
Course VM or paper: three inert sample emails (links rewritten to a sandbox explainer page; attachments neutered), the BEC storyboard, worksheet.

## Installation and Setup
None. Pairs for dissection; teams of 4 for campaign design.

## Ethical Authorization and Safety Notes
- Sample mails are synthetic and inert by construction (verified in the build); never re-arm or forward them.
- Campaign designs must include the consent paragraph — unconsented shock simulations are off-rubric by course policy (L12's evidence on shaming and reporting culture).
- No real vendor, bank, or university brand is impersonated in the samples; do not add one.

## Step-by-Step Student Tasks
1. Per sample: header walk (SPF/DKIM/DMARC columns) → verdict → the *tell* (spoof vs lookalike vs compromised-mailbox).
2. BEC storyboard: annotate pretext markers (authority/urgency/social proof); note the absence of payload.
3. Campaign design: audience segments, one consented-simulation policy (with your consent paragraph), ≥ 3 metrics with target values (≥ 2 beyond click rate), escalation path for reported mails (who reads them, how fast).
4. Compensating-control matrix: lure type → control (incl. phishing-resistant MFA and payment-verification process).
5. Class vote: which campaign would actually change behavior, and why.

## Expected Observations
Sample 1: SPF pass/DKIM fail with From/envelope mismatch (spoof tell). Sample 2: all pass but homoglyph domain (infrastructure tell). Sample 3: all pass — real compromised mailbox (content/process tell → BEC class). The escalation path is the most commonly missing design element.

## Questions for Analysis
1. Sample 3 passes every technical check — name the process control that catches it and the human control that reports it.
2. Your metrics: why does time-to-report beat click rate for *program* health? What behavior does each metric actually measure?

## Troubleshooting
Header verdicts feel opaque → the three-column card in the notes (what each mechanism proves/fails when) is the decoder. Campaign lists only "training" → the matrix needs technical + process + human rows.

## Cleanup Instructions
Return samples to the instructor (they are re-issued); no system state changed.

## Submission Requirements
Three header verdicts, annotated storyboard, campaign design (with consent paragraph + metrics table + escalation path), compensating-control matrix, vote note.

## Expected Outputs / Evidence
The consent paragraph and escalation path are the two most-forgotten deliverables — presence of both is the design-maturity marker.

---
### Instructor Answer Key (summary)
- Verdicts (model): S1 spoof (alignment failure) — receiver action: quarantine, DMARC `p=reject` would have handled it; S2 homoglyph lookalike — infrastructure tell, brand-monitoring + client warnings; S3 compromised real mailbox — all technical checks pass; controls: out-of-band payment verification, dual approval, reporting culture.
- Metrics (model): report rate (target +50% y/y), time-to-report (target < 10 min median), simulation-report quality (fewer false escalations).
- Common design failure: shaming leaderboards → penalized by rubric; the consent paragraph must promise no individual attribution.

### Assessment Rubric (10 pts — check-in)
| Criterion | Points |
|---|---|
| Three header verdicts with tells | 3 |
| Campaign design incl. consent paragraph + escalation path | 4 |
| Metrics (≥ 3, ≥ 2 beyond click rate, with targets) | 2 |
| Compensating-control matrix | 1 |
