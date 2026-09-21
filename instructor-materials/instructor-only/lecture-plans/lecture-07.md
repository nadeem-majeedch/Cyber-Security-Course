# Lecture 07 — XSS, CSRF, SSRF, and IDOR
**Module M2 · Week 4, Session 1 · 120 min · CLO-2 (primary)**

## Learning Objectives
1. Distinguish reflected, stored, and DOM-based XSS and select the matching remediation (context-aware output encoding, CSP, sanitization).
2. Explain CSRF's preconditions and apply token-based and `SameSite` defenses.
3. Explain SSRF's server-side reach and apply egress filtering, allow-lists, and metadata-service hardening.
4. Detect IDOR (broken object-level authorization) and apply server-side object ownership checks (CWE-79, CWE-352, CWE-918, CWE-639).

## Key Concepts
- XSS contexts (HTML body, attribute, JS, URL) and why one encoder is not enough; DOM sinks (`innerHTML`, `eval`); Trusted Types (concept)
- CSRF: ambient authority (cookies), cross-site request forgery preconditions; synchronizer token, `SameSite`, origin checks
- SSRF: URL as attack vector; cloud metadata endpoints (169.254.169.254), internal services; redirect chains and DNS rebinding (awareness)
- IDOR/BOLA: authorization at the object level vs. authentication; predictable IDs; mass assignment
- Content Security Policy: `default-src`, nonces/hashes; report-only rollout

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–08 | Recap L06 fixes: one pair shows their parameterized diff | Showcase |
| 08–30 | XSS family: live demo of reflected XSS in the sandboxed demo app comment field; then the three-context encoding table | Live demo |
| 30–48 | CSRF: the forged-transfer storyboard; why GET "state changes" are fatal; token + SameSite combo | Storyboard slides |
| 48–60 | SSRF + IDOR: URL-fetch feature demo; object-ID enumeration in the demo app's invoice API | Demo |
| 60–62 | Break | — |
| 62–105 | **Lab block (Lab 06):** four stations (XSS/CSRF/SSRF/IDOR) on the sandboxed app; each station: reproduce (locally), identify CWE, write the fix, verify the fix blocks the original payload | Station rotation |
| 105–115 | CSP workshop: write a CSP for the demo app; observe report-only violations | Hands-on |
| 115–120 | Exit ticket; preview L08 (secure SDLC) | Q&A |

## Examples
- **CS track:** stored XSS in a support-ticket title — admin views the queue, payload runs in admin session; remediation chain: encoding → CSP → Trusted Types.
- **DS track:** SSRF in a "fetch dataset by URL" feature of an ML platform — attacker points the server at the metadata service; egress allow-list fix. Also: IDOR on a `/predictions/{id}` endpoint leaking other users' inference results.

## Discussion Questions
1. Why does `innerHTML` remain dangerous even with escaped server output? What is a DOM sink?
2. If cookies were always `SameSite=Strict`, would CSRF disappear? What breaks instead? (embedded flows, SSO handoffs)
3. Who is responsible for IDOR — the framework, the developer, or the reviewer? How do you make object-authz testable?

## Student Activity
Station rotation with a shared findings board; each student must personally write one fix and verify a peer's fix (verification exchange).

## Problem-Solving Scenario
> The demo app adds "import avatar from URL" (SSRF candidate), a `/invoices/{n}` endpoint with sequential IDs (IDOR candidate), and a comment box rendered with `innerHTML` (XSS candidate). For each: the exploit path in one diagram, the CWE, the fix, and a regression test that would catch its return.

## Summary
Four flaws, one theme: the server trusted something it shouldn't — markup, a cross-site request, a URL, or an ID. Trust boundaries must be enforced at every layer the data crosses. L08 zooms out: catching this class of flaw systematically in the SDLC.

## Formative Assessment
1. Which XSS type lives only in client-side JS?
2. Name two independent CSRF defenses.
3. Why do sequential invoice IDs make IDOR easier?

## Required Resources
- `labs/lab-06-xss-csrf-ssrf-idor/` (4-station sandboxed app + starter)
- OWASP Cheat Sheet Series: XSS Prevention, CSRF Prevention, SSRF Prevention; CSP reference; MDN
- CLO mapping: **CLO-2** (objectives 1–4).
