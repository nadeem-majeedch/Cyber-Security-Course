# Lab 05 — Injection: Confirm, Fix, Verify (Sandboxed)
**Enrichment · Module 2 (L06) · CLO-2 (primary), CLO-8 (supporting) · Duration: 2 hours · Check-in lab**

> **Scope rule for this lab:** the only authorized target is the course container `vuln-app` on `127.0.0.1:8081`. No scanning of hosts, ports, or services beyond it. Probes demonstrate *behavior differences*; no data extraction, no destructive payloads, no tooling beyond curl/browser.

## Learning Objectives
1. Confirm three seeded injection sinks by behavior difference (boolean-blind pattern).
2. Remediate each with parameterization / safe API shape.
3. Re-verify that the original probe fails against the fixed build (regression pair).
4. Write the taint path (source → sink) for each sink.

## Prerequisites
Lecture 06. Lab 04's dev-tools discipline.

## Hardware/Software Requirements
Course VM; `vuln-app:weak` container (same target as Lab 29 — this lab is its Module-2 subset); `starter/patches/`; curl.

## Installation and Setup
```bash
sudo docker start vuln-app && sudo docker port vuln-app   # expect 127.0.0.1:8081
curl -s http://127.0.0.1:8081/ | head -5                  # confirm the app responds
```

## Ethical Authorization and Safety Notes
- Loopback-only scope; the target is course-built and deliberately vulnerable *for this exercise*.
- Probes are one-request behavior tests; anything resembling extraction, automation at volume, or payload tuning is out of scope and off-rubric.
- Every confirmed sink must be followed by its fix and re-verification — confirmation without remediation is an incomplete task.

## Step-by-Step Student Tasks
1. Draw the taint path for the search route (GET param → string build → SQL execute).
2. **Sink 1 (search):** run the normal query, then the boolean probe (`x' OR '1'='1`); record the behavior difference (row counts) as a two-line evidence pair.
3. Apply `patches/search-parameterized.diff`; rebuild the image tag; re-run both queries; the probe now returns zero rows as literal text.
4. **Sink 2 (login):** confirm the boolean behavior on the login form (invalid-credentials page differs from app page).
5. Apply `patches/login-parameterized.diff`; verify.
6. **Sink 3 (export filename):** the nightly export takes a user-named output file; demonstrate metacharacter acceptance with a *harmless* marker string (e.g., `;touch /tmp/marker` is NOT required — instead use the app's built-in echo-back behavior); apply `patches/export-listargs.diff`; verify the argument list is used, not the shell.
7. Regression table: three rows, before/after for each sink.

## Expected Observations
Pre-patch: probe returns all rows (search) / app page (login); post-patch: zero rows / invalid-credentials. Export pre-patch echoes shell interpretation; post-patch echoes the literal filename in the argument list.

## Questions for Analysis
1. Why does the parameterized fix make the probe *safe but still weird-looking* (the query runs, returns nothing)? What changed in the protocol?
2. Which of your three fixes was a code change, which a library-API change, and which an architecture change?

## Troubleshooting
Probe returns an error page, not a behavior difference → check the image tag (`docker ps`: `weak` vs `fixed`). Patch fails to apply → `git apply --check` first; the diff expects the `weak` tag's file state. DB reset needed → `docker exec vulnapp-db reset.sh` (documented in the starter).

## Cleanup Instructions
`sudo docker stop vuln-app`; keep the regression table; reset the DB volume if instructed.

## Submission Requirements
Taint-path diagrams (3), before/after evidence pairs (3), regression table, answers.

## Expected Outputs / Evidence
Six evidence lines (3×2) + diagrams; minimal-probe discipline is part of the rubric.

---
### Instructor Answer Key (summary)
- Seeded sinks: search (LIKE concat), login (WHERE concat), export (shell string). Patch tags: `vuln-app:fixed`.
- Expected row counts: search normal = 3 rows; probe = 12 rows (all). Post-patch both return 0/1 as literal.
- Minimal-proof rubric line: evidence pairs must be ≤ 4 requests per sink; automation or extraction attempts score zero on ethics compliance.

### Assessment Rubric (10 pts — check-in)
| Criterion | Points |
|---|---|
| Taint paths (3, correct source/sink) | 3 |
| Before/after pairs (3) with minimal probes | 3 |
| Regression table | 2 |
| Analysis answers | 2 |
