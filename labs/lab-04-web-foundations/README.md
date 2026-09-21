# Lab 04 — Web Auth Flow Review (Demo App)
**Enrichment · Module 2 (L05) · CLO-2 · Duration: 2 hours · Check-in lab**

## Learning Objectives
1. Trace the demo app's login flow at the HTTP level (headers, cookies, redirects).
2. Audit cookie/session configuration against a checklist; identify ≥ 4 weaknesses.
3. Compare session-cookie vs JWT handling in the app's two client types.
4. Write the corrected `Set-Cookie` header and session-ID rule.

## Prerequisites
Lecture 05 (HTTP, cookies, sessions, OAuth code+PKCE awareness). Browser dev tools.

## Hardware/Software Requirements
Course VM with the `webdemo` container (loopback-only, like all course targets): `http://127.0.0.1:8080`. Browser; `curl`; dev tools.

## Installation and Setup
```bash
sudo docker start webdemo && sudo docker port webdemo
# expect: 8080/tcp -> 127.0.0.1:8080
```
Log in with the provided lab account (in the worksheet handout).

## Ethical Authorization and Safety Notes
The demo app is course-owned, loopback-only, and seeded with *weaknesses to find* (not to exploit elsewhere). The lab accounts are fake; nothing here touches a real identity provider. No scanning beyond the target port.

## Step-by-Step Student Tasks
1. Log in with dev tools open; capture the `Set-Cookie` response header verbatim.
2. Checklist audit: for each cookie attribute (Secure/HttpOnly/SameSite/Domain/Expiry), record present/absent + the attack it enables when absent.
3. Session-ID inspection: is it high-entropy? Try the "remember me" flow; compare the two cookies.
4. Second client: open the dashboard's token view (the app intentionally shows its JWT); decode the payload; note signature vs encryption.
5. Redirect check: submit a bad login; examine the 302 target; note where it points.
6. Write the corrected `Set-Cookie` header + the session-ID generation rule (entropy, rotation, expiry).

## Expected Observations
`HttpOnly` present but `Secure` absent; `SameSite` absent; remember-me cookie valid 1 year; session ID = md5(username+static); the dashboard JWT is decodable (signed, not encrypted); the bad-login 302 points to an external placeholder (open-redirect seed).

## Questions for Analysis
1. Which single attribute change would most reduce real-world risk for this app as deployed (loopback in lab, internet in the fiction)? Justify.
2. The JWT is signed, not encrypted — what exactly does an attacker gain from reading it, and what do they *not* gain?

## Troubleshooting
Cookie not visible → the Network tab must be open *before* login (preserve log setting). 302 not shown → enable "Preserve log" and re-submit. Container 502 → `docker restart webdemo`.

## Cleanup Instructions
`sudo docker stop webdemo`; clear browser cookies for the lab origin; nothing else persists.

## Submission Requirements
Header capture (verbatim), completed checklist, JWT decode notes, corrected header + session rule, answers.

## Expected Outputs / Evidence
Findings table with verbatim header evidence; the corrected header must be syntactically valid.

---
### Instructor Answer Key (summary)
- Seeded weaknesses: missing `Secure`; missing `SameSite`; 1-year remember-me; md5-derived session ID; open-redirect on login failure; JWT in localStorage for the dashboard view.
- Corrected header (model): `Set-Cookie: sid=<128-bit random>; Secure; HttpOnly; SameSite=Lax; Max-Age=3600; Path=/` + rotate at login + server-side revocation list.
- JWT decode: payload readable (base64) — attacker gains the claims' content, not forgery (signature still holds without the key).

### Assessment Rubric (10 pts — check-in)
| Criterion | Points |
|---|---|
| Verbatim header capture + ≥ 4 weaknesses with attack mapping | 4 |
| JWT decode notes (signed ≠ encrypted) | 2 |
| Corrected header + session rule (valid syntax, entropy/rotation) | 3 |
| Analysis answers | 1 |
