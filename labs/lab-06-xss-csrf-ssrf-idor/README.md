# Lab 06 — Web Flaw Stations (Sandboxed)
**Enrichment · Module 2 (L07) · CLO-2 · Duration: 2 hours · Check-in lab**

> **Scope rule:** the course container `webdemo` on `127.0.0.1:8080` is the only target; its SSRF station has real egress disabled (fake-net) — requests to "external" hosts are answered by the sandbox. No scanning beyond the target; payloads are visible markers, never destructive.

## Learning Objectives
1. Reproduce (locally), classify, and remediate one flaw per station: XSS, CSRF, SSRF, IDOR.
2. Verify each remediation blocks the original payload (regression discipline).
3. Write a CSP for the demo app and read report-only violations.
4. Name the CWE for each flaw class.

## Prerequisites
Lecture 07. Lab 04/05 pair discipline.

## Hardware/Software Requirements
Course VM; `webdemo` container (4 seeded stations); browser + dev tools; `starter/csp-lab.md`.

## Installation and Setup
```bash
sudo docker start webdemo && sudo docker port webdemo   # 127.0.0.1:8080
```
Stations reset automatically every rotation (documented); find the reset button at `/admin/reset` (lab account).

## Ethical Authorization and Safety Notes
All payloads are classroom markers (e.g., a visible `<b>` tag, a benign fetch to the fake-net sink); nothing destructive, no credential capture, no real egress. The IDOR station's "other users" are fictional accounts with fictional data.

## Step-by-Step Student Tasks
1. **Station XSS:** the comment field renders via `innerHTML`; place a *visible marker* (`<b>lab-marker</b>`); observe rendering; fix with context-aware encoding (patch provided); verify the marker renders as text.
2. **Station CSRF:** the profile-update form has no token; demonstrate a forged cross-origin POST from the sandbox's `evil.html`; apply token patch; verify 403 without token.
3. **Station SSRF:** the "import avatar from URL" feature; point it at the fake-net metadata address; observe the sandbox's simulated response; apply the egress allow-list patch; verify rejection.
4. **Station IDOR:** `/invoices/1042` (your account) vs `/invoices/1041` (another); observe the missing ownership check; apply the object-authz patch; verify 403/404.
5. **CSP lab:** write a CSP for the app (nonce for its inline script); deploy report-only; read the violation report; tighten one directive.

## Expected Observations
Each station: flaw visible → patch → original payload blocked. The CSP report shows the analytics-script violation (seeded).

## Questions for Analysis
1. The four flaws differ in *who runs the request* (victim/victim/server/attacker). Place each fix at the boundary where trust is decided — why does fixing "later" fail?
2. Why is report-only the correct CSP rollout posture for a live app, and what would justify flipping to enforce?

## Troubleshooting
Station appears already patched → wrong rotation order; reset the station. Forged POST returns 200 → the token patch is not applied; check `docker ps` tag. CSP blocks everything → report-only mode first (per the lab doc).

## Cleanup Instructions
`sudo docker stop webdemo`; reset stations; clear the lab origin's storage.

## Submission Requirements
Per-station: reproduce note (one line), CWE, patch applied, verification line. Plus the CSP you wrote and one violation you explained.

## Expected Outputs / Evidence
4 × (reproduce/fix/verify) + CSP deliverable; visible-marker discipline is rubric-relevant.

---
### Instructor Answer Key (summary)
- Station seeds: comment `innerHTML` (CWE-79); profile form no token (CWE-352); avatar URL fetch with fake-net (CWE-918); invoices sequential without ownership check (CWE-639).
- Patches: encoding function at the render boundary; synchronizer token + `SameSite`; egress allow-list (two hosts) + link-local block; ownership check in the object-fetch path.
- CSP violation seeded: the analytics script on the dashboard — expected fix: nonce or self-host.
- Verify lines: marker renders as text; no-token POST → 403; metadata fetch → blocked; other-user invoice → 403/404.

### Assessment Rubric (10 pts — check-in)
| Criterion | Points |
|---|---|
| Four reproduce/fix/verify cycles complete | 5 |
| Correct CWEs + boundary reasoning | 2 |
| CSP deliverable (valid, one violation explained) | 2 |
| Marker/probe discipline | 1 |
