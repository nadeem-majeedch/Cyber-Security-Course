# Lecture 08 — Secure SDLC, Dependency Hygiene & Security Headers + Checkpoint B
**Module M2 · Week 4, Session 2 · 120 min · CLO-2 (primary)**

## Learning Objectives
1. Integrate SAST, DAST, and SCA (dependency scanning) into a CI pipeline and interpret their findings.
2. Configure security headers (CSP, HSTS, X-Content-Type-Options, frame options) and verify with an online checker.
3. Manage vulnerability triage: severity (CVSS basics), exploitability, and patch SLAs.
4. Apply Checkpoint B consolidation of Module 2.

## Key Concepts
- Secure SDLC gates: design review, code review, automated scanning, release check
- SAST vs. DAST vs. SCA — what each sees; false-positive triage discipline
- Software supply chain: SBOM (concept), dependency pinning, provenance; a dependency-confusion story
- Headers: CSP (from L07), HSTS, `X-Content-Type-Options: nosniff`, `X-Frame-Options`/`frame-ancestors`, referrer policy
- CVSS v3.1 base metrics in one table; triage workflow (exploitable? exposed? compensating controls?)

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–08 | Recap L07: class votes on the best CSP written in the lab | Vote |
| 08–30 | Secure SDLC map: where each control lives in a real pipeline (design → PR → CI → staging → release) | Pipeline diagram |
| 30–50 | Hands-on pipeline: add SCA + SAST jobs to the demo repo's CI config; run; triage 5 seeded findings live | Live demo |
| 50–60 | Break | — |
| 60–72 | **Checkpoint B** (Module 2 quiz, CLO-2 items) | Assessment |
| 72–100 | **Lab block (Lab 07):** headers lab — set the full header set on the demo app, verify with securityheaders-style check; fix one CSP violation | Hands-on |
| 100–112 | Dependency-confusion case walk-through: how a public package name shadowed an internal one; the pinning/provenance mitigations | Case |
| 112–120 | Module 2 wrap; M3 preview (malware) | Q&A |

## Examples
- **CS track:** PR introduces `left-pad`-style unpinned dependency + a `eval()` in a util — the pipeline flags both; students write the triage comments.
- **DS track:** a `requirements.txt` with `pandas` unpinned and a typosquatted package in the lockfile — SCA output walkthrough; SBOM generation for audit.

## Discussion Questions
1. SAST reports 400 findings, 380 are false positives. What happens to the tool's credibility, and how do you fix the program rather than the tool?
2. Which headers are worthless without HTTPS? Why does HSTS need a preload discussion?
3. Should a critical CVE in a transitive dependency block release? Build the decision rule.

## Student Activity
Pipeline build-out in pairs (config diff review); triage role-play: one student is the security engineer, one the product owner negotiating a patch SLA.

## Problem-Solving Scenario
> Release is Friday. The scanner shows: one critical RCE in a web framework (public exploit exists), one medium header gap, one license conflict. Produce: the triage table (severity, exploitability, exposure), the go/no-go recommendation, and the two-line CI policy that prevents recurrence.

## Summary
Individual flaws (L05–L07) become systemic when the pipeline catches them before release. Scanners, headers, and dependency hygiene make security a property of the process, not of individual heroics. Module 3 shifts to the endpoint: what malicious code does once inside.

## Formative Assessment
1. Which scanner type finds a vulnerable library version? Which finds a reflected XSS at runtime?
2. What does `nosniff` prevent?
3. Give one CVSS base metric and what it captures.

## Required Resources
- `labs/lab-07-headers-sdlc/` + demo repo with seeded CI findings
- OWASP Secure Headers project; CVSS v3.1 spec (base group only); SBOM overview (CISA)
- CLO mapping: **CLO-2** (objectives 1–4).
