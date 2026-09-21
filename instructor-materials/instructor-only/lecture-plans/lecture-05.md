# Lecture 05 — Web Foundations: HTTP, Sessions, and Authentication
**Module M2 · Week 3, Session 1 · 120 min · CLO-2 (primary)**

## Learning Objectives
1. Trace an HTTP request/response cycle including headers, cookies, and status codes.
2. Explain session mechanisms (cookies, tokens, server-side state) and their security properties.
3. Compare authentication models (session cookie, JWT, OAuth 2.0 flows, SSO) and where each fails.
4. Identify insecure patterns: session fixation, missing `Secure`/`HttpOnly`/`SameSite`, long-lived tokens.

## Key Concepts
- HTTP methods/status codes; headers relevant to security (Cookie, Set-Cookie, Authorization, Location, Referer)
- Cookies: attributes `Secure`, `HttpOnly`, `SameSite`, `Domain`, `Path`, expiry
- Sessions: server-side session IDs vs. stateless JWTs; rotation and expiry
- Authentication vs. authorization vs. identity federation; OAuth 2.0 grant types (authorization code + PKCE; why implicit is deprecated)
- TLS as the transport precondition (full treatment in M5)

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–10 | Module 2 hook: live demo — log into the course demo app, show the cookie in dev tools | Live demo |
| 10–35 | HTTP anatomy: methods, status codes, headers; students decode 6 captured requests on the board | Interactive |
| 35–55 | Sessions & cookies deep dive: attributes table; rotation; what an attacker sees in a stolen cookie | Slides + dev tools |
| 55–60 | Break | — |
| 60–100 | **Lab block (Lab 04):** inspect the demo app's auth flow; find 4 cookie/session weaknesses from a checklist; document with screenshots | Hands-on |
| 100–112 | Auth model comparison: session vs JWT vs OAuth code+PKCE — decision table exercise | Discussion |
| 112–120 | Exit ticket; preview: injection (L06) | Q&A |

## Examples
- **CS track:** decode a real (sanitized) login capture: `Set-Cookie: session=…; HttpOnly` present but `Secure` missing — what attack does that enable on captive networks?
- **DS track:** a data-science dashboard serving plots with a JWT in `localStorage` — XSS consequences vs. `HttpOnly` cookies; API-token expiry for scheduled notebooks.

## Discussion Questions
1. JWTs remove server-side state. What do you lose, and how do you revoke a compromised token?
2. Why did OAuth deprecate the implicit flow? Explain in terms of this lecture's concepts.
3. `SameSite=Lax` vs `Strict` vs `None` — pick for a banking site, a public blog, an embedded widget, and defend each.

## Student Activity
Dev-tools scavenger hunt in the demo app: each pair records one weak cookie/session property, its CWE, and the one-line fix; pairs report findings to build a class checklist.

## Problem-Solving Scenario
> The demo app's "remember me" sets a cookie valid for 1 year, `HttpOnly` absent, `SameSite` absent, and the session ID is the username+static secret hashed with MD5. Enumerate the exploitable properties, rank them, and write the corrected `Set-Cookie` header plus session-ID generation rule.

## Summary
Web security starts with the protocol's state machinery: cookies carry identity, so their attributes are security controls. Sessions must rotate, expire, and resist theft. With this foundation, L06 attacks the other great web weak spot — unvalidated input.

## Formative Assessment
1. Name the cookie attribute that blocks JavaScript read access.
2. Which OAuth grant should a mobile app use, and why?
3. What does a 302 to an external domain in a login flow suggest?

## Required Resources
- Course demo web app (`labs/lab-04-web-foundations/` + `starter/`)
- Browser dev tools; sanitized HTTP capture set
- OWASP Authentication Cheat Sheet; MDN Set-Cookie reference
- CLO mapping: **CLO-2** (objectives 1–4).
