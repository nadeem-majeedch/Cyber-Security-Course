# Lab 03 — Defense-in-Depth Control Plan
**Enrichment · Module 1 (L04) · CLO-1 (primary), CLO-8 (supporting) · Duration: 2 hours · Check-in lab**

## Learning Objectives
1. Classify 20 controls on the 3×3 taxonomy (admin/technical/physical × preventive/detective/corrective).
2. Convert the Lab 01 threat list into a layered control plan (≥ 8 threats covered).
3. Apply least privilege to a provided over-permissive configuration set.
4. Name residual risks with an acceptor role.

## Prerequisites
Lecture 04; Lab 01's threat table (yours or the class master list).

## Hardware/Software Requirements
Course VM or paper: control-card deck, taxonomy wall grid, config-exercise set (`starter/configs/`), worksheet.

## Installation and Setup
None beyond handouts; pairs for the config rewrite.

## Ethical Authorization and Safety Notes
Paper + local config files only; nothing runs as a service; no network changes.

## Step-by-Step Student Tasks
1. Sort the 20 control cards into the 3×3 grid; defend the three most contested placements.
2. For your top-8 threats: fill prevent/detect/correct columns; mark empty cells as named gaps.
3. Least-privilege rewrite: in `starter/configs/`, fix (a) an over-wide DB role, (b) a world-readable secrets file, (c) a service running as root — with the "must still work" list preserved.
4. Verify each config rewrite with the provided check commands.
5. Residual-risk statement: ≥ 2 accepted risks, each with an acceptor *role*.

## Expected Observations
Teams initially over-provide preventive controls and leave detective columns empty; the check commands catch over-revocation (the DB role must still read its own schema).

## Questions for Analysis
1. Which gap (empty column) would you refuse to leave, and what does that refusal cost?
2. Your DB-role rewrite broke nothing on the check — but name a plausible future query it *would* break, and how you'd handle that request without re-widening.

## Troubleshooting
Check fails after rewrite → you over-revoked; widen the *action*, never the resource wildcard. Card sort gridlocked → the axis is *how it acts*, not *what it protects*.

## Cleanup Instructions
Restore `starter/configs/` from git (`git checkout -- configs/`); nothing else persists.

## Submission Requirements
Control matrix (≥ 8 threats), contested-card defenses (3), config diffs + verification outputs, residual-risk statement.

## Expected Outputs / Evidence
Worksheet + config diffs; verification outputs must be pasted, not asserted.

---
### Instructor Answer Key (summary)
- Contested cards: WAF rule = technical/preventive; restore drill = technical/corrective (detective defensible if argued as control-testing); log review = administrative/detective (technical defensible with justification).
- Config checks: DB role must keep SELECT on `analytics.*`; secrets file → `600 svcowner`; service → dedicated `svcuser` with `nohup`-free unit file.
- Common gap: corrective column empty for credential-theft threats (no rotation runbook) — the intended teaching moment.

### Assessment Rubric (10 pts — check-in)
| Criterion | Points |
|---|---|
| Control matrix coverage (≥ 8 threats, ≥ 2 layers on top-3) | 4 |
| Config rewrites with verification outputs | 3 |
| Residual risks with acceptor roles | 2 |
| Contested-card reasoning | 1 |
