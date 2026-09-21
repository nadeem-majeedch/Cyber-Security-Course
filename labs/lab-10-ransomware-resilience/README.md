# Lab 10 — Ransomware Resilience Scenario
**Enrichment · Module 3 (L11) · CLO-3 (primary), CLO-4 (supporting) · Duration: 2 hours · Check-in lab**

> **Safety note:** this lab uses a paper scenario + instructor-provided artifact images (screenshots/log excerpts). No ransomware is executed anywhere; no encryption events occur. The skill practiced is *response design*, not attack.

## Learning Objectives
1. Reconstruct a ransomware kill chain from provided artifacts with ATT&CK mappings.
2. Make and log the three time-critical containment decisions.
3. Design the backup/restore architecture per 3-2-1-1 and compute a restore order.
4. Draft the detection rule for the recovery-destruction indicator (T1490).

## Prerequisites
Lecture 11. Lab 01's risk-ranking habits.

## Hardware/Software Requirements
Course VM or paper: the scenario pack (`scenario-ransomware-v1.pdf` + artifact images: event-log excerpt, GPO editor screenshot, egress graph, leak-site screenshot — all synthetic); worksheet.

## Installation and Setup
None; teams of 4; roles from the course convention.

## Ethical Authorization and Safety Notes
The scenario is fictional; artifact "screenshots" are mockups generated for teaching. No victim organization is named or implied. Payment debate stays analytical; the course position is *design so the decision is not coerced*.

## Step-by-Step Student Tasks
1. Read the scenario pack; list the artifacts you have (and — deliberately — the ones you don't).
2. Kill-chain reconstruction: stage-by-stage with ATT&CK IDs, each stage tied to an artifact.
3. The three decisions for the next 60 minutes: contain spread / preserve evidence / communicate — one logged decision each with options considered.
4. Backup-architecture redesign: the provided design has four flaws (same-site NAS, single admin, no offline copy, no restore tests); fix all four; sketch.
5. Restore order: prioritized list with dependency justification (infrastructure → verify → tier-1 data → shares → endpoints).
6. Detection rule for the shadow-copy deletion command line (T1490 indicator) in the course rule format.
7. Residual-risk statement: what your redesigned architecture still does not stop (double extortion).

## Expected Observations
- Artifacts show: GPO login-script modification (2 days prior), new admin account, 40 GB egress to a file-share site, shadow-copy deletion, `.locked` extensions, leak-site countdown.
- The exfiltration *precedes* encryption in the artifact timeline — the double-extortion lesson made visible.

## Questions for Analysis
1. Your restore order puts identity infrastructure first. What breaks if you are wrong about that — and how would you *verify* the order before an incident?
2. Which single control in your redesign would have changed this incident most, and where in the kill chain does it act?

## Troubleshooting
Stage mapping stuck → re-read the artifacts against the kill-chain table in the notes; every artifact belongs to some stage. Restore order contested → use the dependency argument (what does the *next* item need?).

## Cleanup Instructions
Return scenario packs; nothing was executed; no system state changed.

## Submission Requirements
Kill-chain table with ATT&CK IDs + artifact citations, three logged decisions, redesigned backup sketch, restore order, T1490 rule, residual-risk statement.

## Expected Outputs / Evidence
Every stage claim cites an artifact page; the rule must be specific (command-line pattern, not "monitor for ransomware").

---
### Instructor Answer Key (summary)
- Kill chain (model): access via GPO script + new admin (T1136/T1484-class) → recon/share discovery (artifact: egress graph start) → staging → exfil 40 GB (T1567-class) → T1490 shadow-copy deletion → T1486 encryption → leak-site countdown.
- Three decisions (bars): contain = disable the GPO + isolate file server; evidence = preserve the modified GPO object before reverting; communicate = who tells the campus, with what facts.
- Restore order: backup/identity infra → verify integrity → tier-1 (finance/regulatory) → shares → endpoints.
- T1490 rule (model): process creation with `vssadmin delete shadows /all` or `wmic shadowcopy delete` → high-severity alert.
- Residual risk: exfiltrated data disclosure — backups cannot cap it; only earlier-stage detection (egress anomaly) and data minimization reduce it.

### Assessment Rubric (10 pts — check-in)
| Criterion | Points |
|---|---|
| Kill-chain reconstruction with artifact citations | 3 |
| Three logged decisions (options + evidence) | 2 |
| Backup redesign + restore order | 3 |
| T1490 rule specificity + residual-risk honesty | 2 |
