# Lab 07 — Security Headers & Dependency Hygiene
**Enrichment · Module 2 (L08) · CLO-2 · Duration: 2 hours · Check-in lab**

## Learning Objectives
1. Set and verify the core security-header set on the demo app.
2. Add SCA + SAST jobs to a CI config; triage seeded findings honestly.
3. Generate an SBOM and explain what audit question it answers.
4. Write a triage decision (go/no-go) with a patch-SLA rule.

## Prerequisites
Lecture 08; Lab 04's target (`webdemo`) and its repo.

## Hardware/Software Requirements
Course VM; `webdemo` + its git repo; CI runner config in the image (local runner); `pip-audit`-class SCA tool and a SAST demo rule set (provided).

## Installation and Setup
```bash
sudo docker start webdemo
cd ~/webdemo-repo && git checkout headers-lab
```
CI runs locally (`runner.sh` in the repo) — no external CI service is used.

## Ethical Authorization and Safety Notes
Your own repo and your own loopback app; CI is local. The seeded dependencies are real packages pinned to known-vulnerable *old* versions — the audit finds them; nothing is exploited.

## Step-by-Step Student Tasks
1. Baseline `curl -I 127.0.0.1:8080` — list which of the four headers are missing.
2. Add the header set in the app config (`starter/headers.conf`); restart; re-run `curl -I`; diff.
3. Fix the seeded CSP violation (the analytics script): nonce or self-host; verify report-only shows clean.
4. Add the SCA job to `runner.sh`; run; record the two seeded vulnerable pins.
5. Add the SAST job; run; record the seeded `eval()` finding.
6. Generate the SBOM (tool in the image); save it; answer: what audit question does this file answer?
7. Triage table: severity × exploitability × exposure for all three findings; go/no-go recommendation + a two-line patch-SLA policy.

## Expected Observations
Baseline: all four headers missing; post-fix all present. SCA finds the pinned-old `flask`-class and `lodash`-class entries; SAST finds `eval()` in `utils.py`.

## Questions for Analysis
1. Which finding blocks release, and what does the *public exploit* line change in your triage?
2. Your SBOM lists 214 transitive packages you never chose. Who is accountable for them, and what mechanism makes accountability workable?

## Troubleshooting
CI job fails on tool version → the image pins versions; do not upgrade, read the pinned-versions note. Header not appearing → app not restarted (`docker restart webdemo`).

## Cleanup Instructions
`git checkout main` in the repo; stop the container; nothing persists.

## Submission Requirements
Header before/after diff, CI findings list, SBOM file, triage table + go/no-go + SLA policy, answers.

## Expected Outputs / Evidence
Command outputs pasted; the triage table must reference the finding IDs from your own CI run.

---
### Instructor Answer Key (summary)
- Seeded CI findings: `flask==0.12.2` (known RCE-class advisory), `lodash-class==4.17.4` (prototype-pollution advisory), `eval()` in `utils.py` (SAST).
- Triage (model): flask pin — high severity, public exploit, internet-exposed *in the fiction* → blocks release; lodash-class — medium; eval — medium (context-dependent).
- SBOM answer: "what exactly were we running on date X" — the regulator/insurance/IR question.

### Assessment Rubric (10 pts — check-in)
| Criterion | Points |
|---|---|
| Header before/after + CSP fix | 3 |
| CI findings identified + triage table | 4 |
| SBOM + audit-question answer | 2 |
| Go/no-go + SLA policy | 1 |
