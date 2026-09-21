# Lecture 07 — XSS, CSRF, SSRF, and IDOR
**Module 2 · Week 4, Session 1 · 2 hours · CLO-2**

## Learning Objectives
1. Distinguish reflected, stored, and DOM-based XSS and select the matching remediation.
2. Explain CSRF's preconditions and apply token + `SameSite` defenses.
3. Explain SSRF's server-side reach and apply egress allow-lists.
4. Detect IDOR and apply server-side object-level authorization checks.

## Key Concepts and Definitions

**XSS (CWE-79):** attacker-controlled script runs in a *victim's* browser under your origin. Three types: **reflected** (payload arrives in the request and is echoed), **stored** (payload persists — comment fields), **DOM-based** (client-side JS writes untrusted data into a *sink* like `innerHTML`). Fix hierarchy: **context-aware output encoding** (HTML body ≠ attribute ≠ JS context), then **CSP** as a net, then framework auto-escaping (know where it does *not* apply).

**CSRF (CWE-352):** the browser silently attaches ambient credentials (cookies) to cross-site requests, so a forged form on evil.com can spend the victim's session. Preconditions: state-changing action + cookie auth + no CSRF defenses. Fixes (layer two): **synchronizer token** (random per-session token in forms), **`SameSite`** cookies, origin checks.

**SSRF (CWE-918):** the *server* fetches a URL the attacker chooses — the request comes from inside the network. Classic targets: internal services and cloud metadata endpoints (e.g., `169.254.169.254`). Fixes: **egress allow-list** (protocol + hosts), no raw user URLs, block/link-local ranges, and metadata-service hardening on the platform.

**IDOR / BOLA (CWE-639):** the app authenticates the user but never checks *object ownership*: `/invoices/1042` for someone else's invoice. Fix: server-side check "does this object belong to the calling principal?" on every access — plus non-sequential IDs as a slowing measure, not a fix.

**CSP:** browser policy (`default-src 'self'`, per-context allowances, nonces for inline scripts). Roll out `Content-Security-Policy-Report-Only` first to observe violations.

## Conceptual Diagram

```text
XSS:    attacker ─► your site stores/echoes payload ─► victim's browser runs it (your origin!)
CSRF:   victim logged in ─► visits evil.com ─► forged request + ambient cookie ─► your server acts
SSRF:   attacker ─► your server's "fetch URL" feature ─► internal/metadata service (server's vantage)
IDOR:   attacker ─► GET /invoices/1042 ─► server authenticates user but never checks ownership
```
The four differ in *who runs the request* (victim's browser, victim's browser, your server, attacker) — that distinction drives the fix.

## Realistic Examples

- **CS track:** stored XSS in a support-ticket title: the admin's queue view executes the payload in an admin session. Remediation chain: encoding → CSP → (modern) Trusted Types.
- **DS track:** SSRF in an ML platform's "fetch dataset by URL": the server is pointed at the metadata service; the fix is an egress allow-list to known data hosts. Also IDOR on `/predictions/{id}` leaking other users' inference results.

## Common Misconceptions

| Misconception | Correction |
|---|---|
| "Escaping server output makes XSS impossible" | DOM sinks run client-side after your (safe) server output; `innerHTML` re-creates the flaw. |
| "SameSite=Strict alone solves CSRF" | It breaks legitimate embedded flows and doesn't cover all vectors; pair with tokens. |
| "SSRF is a server-side port scan" | The essence is the *server's vantage point* — internal trust is what gets abused. |
| "Unpredictable IDs prevent IDOR" | They slow enumeration; the missing authorization check is the flaw. |

## Classroom Activities

1. **Live demo (12 min):** reflected XSS in the sandboxed demo app's comment field; then the three-context encoding table.
2. **Four stations (40 min, Lab 06):** XSS / CSRF / SSRF / IDOR — reproduce locally, identify CWE, fix, verify the fix blocks the original payload.
3. **CSP workshop (10 min):** write a CSP for the demo app; inspect report-only violations.

## Discussion Questions

1. Why does `innerHTML` remain dangerous even when the server escaped everything?
2. If every cookie were `SameSite=Strict`, would CSRF disappear? What legitimate functionality breaks?
3. Who "owns" IDOR — framework, developer, or reviewer? How would you make object-authz testable in CI?

## Problem-Solving Exercise

> The demo app adds: "import avatar from URL" (SSRF candidate), `/invoices/{n}` sequential IDs (IDOR candidate), and a comment box rendered via `innerHTML` (XSS candidate).
> **Deliverable:** for each — the exploit path as a one-line flow, the CWE, the fix, and a regression test that would catch its return.

## Summary

Four flaws, one theme: trusting something that crossed a boundary — markup, a cross-site request, a URL, an object reference. Fix at the boundary where trust is decided, then layer. Next lecture: making the *pipeline* catch this class before release.

## Exit Ticket

1. Which XSS type exists only in client-side JavaScript?
2. Name two independent CSRF defenses.
3. Why do sequential invoice IDs make IDOR easier?

## References

- OWASP Cheat Sheet Series: *XSS Prevention*, *CSRF Prevention*, *SSRF Prevention*. https://cheatsheetseries.owasp.org
- MDN, *Content Security Policy (CSP)*. https://developer.mozilla.org
- MITRE CWE-79, CWE-352, CWE-918, CWE-639. https://cwe.mitre.org
- OWASP, *OWASP Top 10* (current ed.): A01 Broken Access Control, A03 Injection.
