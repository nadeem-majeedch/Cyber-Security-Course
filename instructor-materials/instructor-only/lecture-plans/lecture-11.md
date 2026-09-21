# Lecture 11 — Ransomware & Worms: Anatomy and Resilience
**Module M3 · Week 6, Session 1 · 120 min · CLO-3 (primary) · CLO-4 (supporting)**

## Learning Objectives
1. Describe the modern ransomware kill chain: access → recon → persistence → staging → exfiltration → encryption → extortion.
2. Explain double/triple extortion and why exfiltration changed backup strategy.
3. Design resilient backup/restore per the 3-2-1 rule, with immutability and tested restoration.
4. Analyze the propagation logic of worms and the network controls that contain them (CLO-4 seed).

## Key Concepts
- Ransomware-as-a-Service (RaaS) ecosystem: affiliates, IABs (initial access brokers), leak sites
- Kill-chain stages mapped to ATT&CK: T1566/T1078 (access), T1486 (encryption), T1490 (inhibit recovery — deleting shadow copies), T1567 (exfiltration)
- 3-2-1 backups (+offline/immutable variant), restore-time objectives; tabletop-style recovery planning
- Worm propagation: scanning strategies, credential reuse (e.g., EternalBlue-era worms as history), containment: segmentation, rate limits, takedowns
- Case thread: a public ransomware post-mortem (cited in `case-studies/`)

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–08 | Recap L10: best student IOC table projected | Showcase |
| 08–32 | Kill-chain walk-through on the cited post-mortem: stage-by-stage with the ATT&CK IDs; where each stage was detectable | Case slide walk |
| 32–50 | Extortion economics: why exfiltration forced the 3-2-1-1-0 conversation; RaaS roles | Slides |
| 50–60 | Break | — |
| 60–72 | Backup design mini-lab: students patch a flawed backup design (same-site NAS, single admin, no restore tests) | Exercise |
| 72–105 | **Lab block (Lab 10):** "ransomware resilience" scenario — a synthetic encrypted-file event on a lab share; students (a) trace the simulated kill chain from provided artifacts, (b) design the containment + restore plan, (c) compute restore order | Scenario lab |
| 105–115 | Worm containment debate: given a spreading worm with credential reuse, what contains it first — segmentation, credential hygiene, or takedown? | Debate |
| 115–120 | Exit ticket; preview L12 | Q&A |

## Examples
- **CS track:** shadow-copy deletion command line as a T1490 indicator; students write the EDR-style detection rule for it.
- **DS track:** backup-coverage analytics: file-age vs. backup-success heatmap of a fake environment; identify the unprotected share before "encryption day."

## Discussion Questions
1. Backups are necessary — why are they not sufficient against double extortion?
2. Who should hold the immutability credentials, and why does that question decide whether the plan works?
3. Ransom payment: legal, ethical, strategic — map the arguments and the counter-arguments.

## Student Activity
Flawed-backup-design surgery (pairs), then the scenario lab with a restore-order deliverable; debate roles assigned randomly to force perspective-taking.

## Problem-Solving Scenario
> Sunday 03:00: file server shows `.locked` extensions, shadow copies gone, a leak-site countdown. Artifacts: GPO-deployed login script modified 2 days ago, new admin account, 40 GB egress to a file-share site. Produce: the stage-by-stage reconstruction with ATT&CK IDs, the three decisions for the next 60 minutes, and the redesigned backup architecture with restore-time estimate.

## Summary
Ransomware is a business process — so resilience is an architecture, not a product. Detect earlier stages, make recovery independent of the encrypted systems, and rehearse. L12 turns to the human layer that started this incident: the credential that made access possible.

## Formative Assessment
1. Which ATT&CK technique covers deleting backup artifacts?
2. State the 3-2-1 rule and the modern +1.
3. Why did exfiltration change backup design?

## Required Resources
- `labs/lab-10-ransomware-resilience/` scenario pack (synthetic artifacts)
- Cited public post-mortem (in `case-studies/case-ransomware-postmortem.md`)
- CISA #StopRansomware guide (student-friendly)
- CLO mapping: **CLO-3** (objectives 1–2, 4); **CLO-4** (objectives 3–4).
