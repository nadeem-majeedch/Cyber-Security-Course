# Lab 29 — Vulnerability Assessment of an Authorized Lab Target
**Core Lab 4+5 (secure web testing + vuln assessment) · Modules 2/4 (L06–L08, L15) · CLO-2 (primary), CLO-4 · Duration: 2 hours · Graded lab**

## 1. Learning Objectives
1. Execute a structured vulnerability assessment against the **course-owned vulnerable web target**: scoping → identification → verification → remediation → re-verification.
2. Verify and fix the seeded web flaw classes (injection, session weakness, missing headers) from Modules 2.
3. Grade findings with severity *and* exploitability *and* exposure — the triage discipline from L08.
4. Produce a client-ready assessment report with a remediation plan and re-test evidence.

## 2. Prerequisites
Lectures 06–08 (injection, web flaws, secure SDLC) and Lab 00's verification discipline. The course VM with the `vuln-app` target image running locally.

## 3. Hardware/Software Requirements
- Course VM running the **local** target container `vuln-app` (deliberately vulnerable training app, course-built; bound to `127.0.0.1:8081` only).
- Browser + dev tools; `curl`; Python 3.10+.
- The assessment report template (`starter/report-template.md`).

## 4. Installation and Setup
1. Start the target and confirm it is loopback-only:
   ```bash
   sudo docker start vuln-app && sudo docker port vuln-app
   # expect: 8081/tcp -> 127.0.0.1:8081
   ```
2. Confirm scope boundary (this is the lab's authorization document):
   ```bash
   curl -s http://127.0.0.1:8081/robots.txt | grep -i scope
   ```
3. Baseline the target: fetch the homepage, note the tech stack header, save a pre-assessment copy.
   *(Target image build, port binding, and robots scope line verified on the instructor workstation; the app's seeded flaws are documented in the key.)*

## 5. Ethical Authorization and Safety Notes
- **Scope is 127.0.0.1:8081 and nothing else.** The target is course-owned and deliberately vulnerable; that is your entire authorized universe for two hours.
- No scanning of the host machine, the campus network, Docker's other services, or anything beyond the target port. If a probe returns data from outside scope, stop and report it — that is the correct professional response.
- No credential theft, no destructive payloads, no persistence: findings are demonstrated with a minimal proof (e.g., the boolean-blind *behavior*, not an extraction pipeline) and then **fixed**.
- Every finding must ship with a remediation; assessment without remediation is half the deliverable.

## 6. Step-by-Step Student Tasks
| # | Task | Notes |
|---|---|---|
| 1 | Scope statement in your report: target, port, authorization basis (this lab), exclusions | §1 of template |
| 2 | Enumeration: fetch the sitemap of the target (5 routes provided in robots.txt); note input fields per route | manual + curl |
| 3 | **Flaw class 1 — injection:** the search route builds a query by concatenation; demonstrate with the boolean-blind *behavior difference* (`x' OR '1'='1` returns all rows vs. a normal query) | minimal proof only |
| 4 | Fix 1: apply the parameterized-query patch from `starter/patches/`; rebuild; re-run your probe; record before/after | evidence pair |
| 5 | **Flaw class 2 — session:** inspect the session cookie (missing flags, guessable ID from Lab 05 knowledge); document | dev tools |
| 6 | Fix 2: apply the session-hardening patch (flags + entropy); re-check the cookie | evidence pair |
| 7 | **Flaw class 3 — headers:** enumerate missing security headers (CSP, HSTS, nosniff, frame-options) | `curl -I` |
| 8 | Fix 3: apply the headers patch; re-run `curl -I`; diff | evidence pair |
| 9 | Grade all three findings: severity (CVSS-style reasoning), exploitability, exposure (loopback-only = low exposure — *say so*) | triage table |
| 10 | Re-verification section: all three fixes hold; regression probes documented | before/after table |
| 11 | Remediation plan: priority order + effort estimate + residual risk | final section |

## 7. Expected Observations
- The search route returns the full table for the probe string (concatenated query); after the patch, the probe string returns zero rows as literal text.
- Session cookie pre-patch: no `Secure`/`HttpOnly`/`SameSite`, ID derivable from the username; post-patch: 128-bit random, all flags set.
- `curl -I` pre-patch: no CSP/HSTS; post-patch: all four headers present.
- Exposure honesty: because the target is loopback-only, real-world exposure is *lab-only* — the report must say this (severity in context, not inflated).

## 8. Questions for Analysis
1. Your probe demonstrated the flaw without extracting any data. Why is a behavior-difference proof sufficient for a finding — and what would convince you it is *not*?
2. The headers finding is trivially exploitable in production but harmless in the loopback lab. How do you grade it so a client takes it seriously without alarmism?
3. Which of your three fixes is a *deployment* fix, which is *code*, and which is *configuration* — and why does that distinction matter for the remediation plan's priority order?

## 9. Troubleshooting
- `docker: permission denied` → use `sudo` per the course image convention.
- Target responds 502 → restart the container (`docker restart vuln-app`); if it persists, `docker logs vuln-app | tail -20` and attach to your report.
- Probe returns an error page instead of the boolean difference → you likely hit the *patched* build; confirm with `docker ps` which image tag is running (`vuln-app:weak` vs `vuln-app:fixed`).

## 10. Cleanup Instructions
- Stop the target: `sudo docker stop vuln-app`.
- Keep the report and evidence; delete the target's database volume only if instructed (`docker volume rm vulnapp-db` — instructor call per section).

## 11. Submission Requirements
- `assessment-report.md` per the template: scope, methodology, findings (3 × before/after evidence), triage table, re-verification, remediation plan, residual risk.
- Terminal transcripts for each probe pair.

## 12. Expected Outputs / Evidence
The report + transcripts. The three before/after pairs are the core evidence; a finding without a fix, or a fix without a re-test, is an incomplete finding per the rubric.

---
### Instructor Answer Key (summary — full version in `assessments/instructor-only/`)
- Seeded flaws in `vuln-app:weak`: (1) search route — concatenated LIKE query (CWE-89; probe `x' OR '1'='1` → all 12 rows); (2) session — `sid=<md5(username+static)>`, no flags (CWE-614/330 class); (3) headers — all four missing (CWE-693 class). Patches in `starter/patches/` flip the image to `vuln-app:fixed`.
- Triage (model): (1) high severity / high exploitability / *lab-only* exposure → "high-if-deployed" framing; (2) medium (requires network position or XSS chain); (3) medium (defense-in-depth, trivial fix).
- Header check expectation post-patch: `content-security-policy`, `strict-transport-security`, `x-content-type-options`, `x-frame-options` all present.
- Common failure: students probe the host's other ports (out of scope) — the report must note scope discipline; the rubric rewards the *stated* scope boundary.

### Assessment Rubric (20 pts)
| Criterion | Points |
|---|---|
| Scope statement + methodological discipline | 3 |
| Three findings with minimal-proof evidence | 6 |
| Three before/after fix pairs (fix + re-verify) | 6 |
| Triage table (severity × exploitability × exposure) | 3 |
| Remediation plan + residual-risk honesty | 2 |
