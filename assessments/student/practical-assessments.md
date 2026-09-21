# Practical Lab Assessments — Student Guide

## How lab marks work

- Labs are worth **30%** of the course; your **best 6 of 8** graded lab reports count.
- Every graded lab is announced one week ahead in the lecture; the worksheet lives in `labs/lab-NN-…/README.md`.
- Work happens **inside the isolated course environment** only. Evidence must be produced by you, in your own VM — the academic-integrity policy treats shared screenshots as collusion.
- **Due:** 23:59 on the day of the lab session +7 days. Late policy: −10% per 24 h, up to 3 days, then 0.

## Report template (every graded lab)

Submit a single PDF (or the platform's format) with these sections:

| # | Section | What it must contain | Marks |
|---|---|---|---|
| 1 | Objective | The lab's CLO and what you set out to demonstrate | 5 |
| 2 | Method | Steps you actually performed (commands, settings) — reproducible | 20 |
| 3 | Evidence | Your own screenshots/outputs, each with a one-line caption and timestamp | 30 |
| 4 | Analysis | Answers to the worksheet's "questions for analysis," in your own words | 25 |
| 5 | Remediation | The defensive fix/verification the worksheet asks for | 15 |
| 6 | Reflection | One paragraph: what was hard, what you would do differently | 5 |

Rubric anchors: **correctness 40%** (method + analysis), **evidence quality 30%**, **remediation quality 30%**. A report with evidence that cannot have been produced by your VM scores zero on evidence and is referred under the integrity policy.

## Minimum pass expectation

Each lab names its **minimum viable outcome** in the worksheet (e.g., "at least 8 of 10 seeded flaws identified with CWE + fix"). Meeting the MVO anchors you at the 70% band; the bands above it reward analysis depth and remediation verification.

## Which labs are graded

The 8 core labs are graded (see `labs/README.md` for the current crosswalk: hardening baseline, packet analysis, crypto/integrity, web testing, vulnerability assessment, log correlation, forensics, IR simulation). Enrichment labs feed your capstone and checkpoints but are ungraded.
