---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L05 · Module 2 · Week 3'
---

<!-- _class: lead -->
# Lecture 05 — Web Security I
## HTTP Anatomy, Sessions & Auth Flows
**Module 2 · Week 3 · 120 min · CLO-2 (primary)**

<!--
TIMING: 1 min. Hook: open DevTools network tab live on a login — "this is the whole lecture, visible."
-->

---

# Learning Objectives

1. Read an HTTP request/response end to end
2. Explain **cookies** & session state
3. Trace where session logic fails
4. Apply secure cookie attributes

<!--
Objectives = lab-04 prep. DevTools demo is the spine. 3 min.
-->

---

# Request anatomy

```
POST /login HTTP/1.1
Host: portal.example
Content-Type: application/x-www-form-urlencoded
Cookie: sid=abc123

user=anna&pass=••••••
```

*Describe: annotated raw HTTP POST — method, path, headers (Host, Cookie), and body with credentials.*

<!--
READ each line's job. Misconception: "HTTPS hides this from the server" — it hides it from the NETWORK, not the app. 5 min.
-->

---

# Sessions — how state rides on stateless HTTP

```
[Browser] --creds--> [Server] --Set-Cookie: sid--> [Browser]
[Browser] --Cookie: sid (every request)--> [Server]
```

*Describe: two-step sequence — login issues a session cookie, then every subsequent request presents it automatically.*

<!--
THE AMBIENT CREDENTIAL: the browser sends it whether YOU want it or not — seeds CSRF (L07). 5 min.
-->

---

# Cookie attributes that matter

| Attribute | Effect |
|---|---|
| `Secure` | HTTPS-only transmission |
| `HttpOnly` | hidden from JavaScript |
| `SameSite` | cross-site request control |
| `Expires/Max-Age` | lifetime |

*Describe: four-row attribute-effect table.*

<!--
Drill: which attribute stops XSS theft? (HttpOnly.) Network theft? (Secure.) CSRF? (SameSite.) 4 min.
-->

---

# CS example — token in localStorage

- JWT in `localStorage` = XSS-readable
- Fix: `HttpOnly` cookie + CSRF token

<!--
2 min. DS contrast next.
-->

---

# DS example — dashboards & auth

- Analytics dashboard shares session cookie with the API
- Failure: long-lived token, no expiry on shared laptops
- Fix: short TTL + re-auth for exports

<!--
2 min. CS-017 laptop-on-bus echo.
-->

---

# Lab demo — Lab 04 (web foundations)

- Instructor captures login flow in the sandbox proxy: request → Set-Cookie → authenticated GET
- **MVO:** students identify the session cookie and one missing attribute
- Sandbox app only (`localhost` course target)

<!--
DEMO 5 min. Pivot: saved PCAP if proxy misbehaves.
-->

---

# Case session

**CS-034 "Login form trusts the browser"** (Level 2 · Secure web applications)

→ which check lives on the wrong side?

<!--
10 min. Model: client-side trust is the recurring M2 theme.
-->

---

# Wrap-up & exit ticket

- HTTP is readable; sessions ride on cookies; attributes are controls
- **Exit:** write the three cookie headers you'd set for a banking app

<!--
Close 110. Preview L06: injection.
-->

---

# References

- MDN HTTP docs; OWASP Session Management Cheat Sheet
- Lecture plan lecture-05; Lab 04
