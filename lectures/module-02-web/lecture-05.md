# Lecture 05 — Web Foundations: HTTP, Sessions, and Authentication
**Module 2 · Week 3, Session 1 · 2 hours · CLO-2**

## Learning Objectives
1. Trace an HTTP request/response cycle including headers, cookies, and status codes.
2. Explain session mechanisms (server-side IDs vs. stateless tokens) and their security properties.
3. Compare authentication models (session cookie, JWT, OAuth 2.0 authorization-code + PKCE) and where each fails.
4. Identify insecure cookie/session patterns and state the fix for each.

## Key Concepts and Definitions

**HTTP** is stateless: each request is independent, so *state* (who is logged in?) must be layered on. The mechanisms that carry state are the security-critical parts.

**Cookie attributes** (the ones that matter for security):

| Attribute | What it does | Attack it mitigates |
|---|---|---|
| `Secure` | Cookie sent only over HTTPS | Interception on mixed content |
| `HttpOnly` | JavaScript cannot read the cookie | XSS session theft |
| `SameSite=Lax/Strict/None` | Controls cross-site sending | CSRF (with other layers) |
| `Domain`/`Path` | Scoping | Over-broad exposure |

**Sessions:** two families. *Server-side:* the cookie holds an opaque random ID; the server stores the state — revocation is easy. *Stateless tokens (JWT):* the token itself carries signed claims — revocation is hard (the token is valid until expiry). Session IDs must be high-entropy, rotated at login, and expired server-side.

**Authentication vs. authorization:** authentication proves *who you are*; authorization decides *what you may do*. Mixing them up causes the IDOR class later (L07).

**OAuth 2.0** delegates authorization. The web/mobile-appropriate grant is **authorization code + PKCE**; the implicit grant is deprecated (tokens exposed in URL fragments).

## Conceptual Diagram

```text
Browser                          Server
   │  POST /login (user+pass)      │
   │──────────────────────────────►│ verify credentials
   │  Set-Cookie: sid=R4nd0m;      │ create session(sid→user),
   │    Secure; HttpOnly; SameSite │ rotate ID at login
   │◄──────────────────────────────│
   │  GET /account (Cookie: sid=…)  │ lookup session → authorize
   │──────────────────────────────►│
```
*What you would see:* the login flow in the browser dev tools — the `Set-Cookie` response header and the `Cookie` request header on the next page.

## Realistic Examples

- **CS track:** a login capture where `Set-Cookie: session=…; HttpOnly` appears but `Secure` is missing. On a captive network, that cookie can be observed in transit — the fix is one word plus HSTS.
- **DS track:** a dashboard storing a JWT in `localStorage`: any XSS now reads it (no `HttpOnly` protection exists for localStorage). Also: scheduled notebooks calling APIs with long-lived personal tokens — fix with short-lived tokens scoped to the job.

## Common Misconceptions

| Misconception | Correction |
|---|---|
| "JWTs are encrypted" | JWTs are *signed*, not encrypted — anyone can read the claims. |
| "HttpOnly makes a cookie safe" | It blocks JS reading; interception and CSRF remain possible — attributes combine. |
| "Logout deletes the token" | Only if server-side state exists; stateless tokens live until expiry unless you add a denylist. |
| "HTTPS fixes everything" | TLS protects transport; cookie flags, rotation, and validation remain your job. |

## Classroom Activities

1. **Dev-tools tour (10 min):** log into the course demo app; find the session cookie; read its attributes.
2. **Header decode drill (10 min):** six sanitized request/response pairs — students call out the security-relevant header in each.
3. **Lab 04 (40 min):** inspect the demo app's auth flow; find four cookie/session weaknesses from a checklist; document with screenshots.

## Discussion Questions

1. JWTs remove server-side session state. What do you lose — and how would you revoke a compromised token?
2. Why was OAuth's implicit flow deprecated? Explain it using this lecture's concepts.
3. Choose `SameSite` for: a banking site, a public blog, an embedded payment widget. Defend each choice.

## Problem-Solving Exercise

> The demo app's "remember me" sets a cookie valid for 1 year, `HttpOnly` absent, `SameSite` absent, and the session ID is `md5(username + static_secret)`.
> **Deliverable:** enumerate the exploitable properties; rank them; write the corrected `Set-Cookie` header and the session-ID generation rule (entropy, rotation, expiry).

## Summary

Cookies carry identity, so cookie attributes *are* security controls. Sessions must be high-entropy, rotated, expirable — and revocable if you need revocation. With the state machinery understood, the next lecture attacks what flows through it: unvalidated input.

## Exit Ticket

1. Which cookie attribute blocks JavaScript read access?
2. Which OAuth grant should a mobile app use, and why?
3. What does a 302 to an external domain in a login flow suggest?

## References

- MDN, *Set-Cookie* and *HTTP cookies*. https://developer.mozilla.org
- OWASP Cheat Sheet Series, *Session Management* and *Authentication*. https://cheatsheetseries.owasp.org
- IETF RFC 6749 (OAuth 2.0) and RFC 7636 (PKCE). https://datatracker.ietf.org
- Fielding, R. et al., RFC 9110 (HTTP semantics; status codes). https://datatracker.ietf.org
