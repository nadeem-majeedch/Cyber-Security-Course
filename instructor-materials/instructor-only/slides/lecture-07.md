---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L07 · Module 2 · Week 4'
---

<!-- _class: lead -->
# Lecture 07 — Web Security III
## XSS · CSRF · SSRF · IDOR
**Module 2 · Week 4 · 120 min · CLO-2 (primary)**

<!--
TIMING: 1 min. Hook: "four ways the browser betrays its user" — 20 s each teaser.
-->

---

# Learning Objectives

1. **Distinguish** the four flaw classes by mechanism
2. Apply output encoding for XSS
3. Block CSRF with tokens + `SameSite`
4. Contain SSRF with egress rules; kill IDOR with object authz

<!--
The distinction table IS the exam question — build it together. 3 min.
-->

---

# The four-way distinction

| Flaw | Who is tricked | Fix |
|---|---|---|
| **XSS** | the *browser* (runs attacker JS) | output encoding + CSP |
| **CSRF** | the *browser* (sends cookie) | token + `SameSite` |
| **SSRF** | the *server* (fetches attacker URL) | egress allow-list |
| **IDOR** | the *server* (skips object check) | object-level authz |

*Describe: four-row table pairing each flaw with the deceived component and its structural fix.*

<!--
6 min drill — students fill a blanked version. This table returns in checkpoint B and the midterm.
-->

---

# XSS — context decides the encoding

```
HTML body:   &lt;script&gt;
Attribute:   &quot; onmouseover=...
JavaScript:  \x3cscript\x3e
URL:         %3Cscript%3E
```

*Describe: four lines showing the same payload encoded differently for HTML, attribute, JS, and URL contexts.*

<!--
MISCONCEPTION: one global encoder. Context-aware or broken. 5 min.
-->

---

# CSRF & SSRF side by side

```
CSRF: browser ──cookie rides along──► server acts
SSRF: server  ──fetches attacker URL──► metadata:169.254.169.254
```

*Describe: two one-line flows — CSRF abuses the browser's credential; SSRF abuses the server's network position.*

<!--
SSRF payoff: cloud metadata credentials (MCQ-2.5). Egress rules = L04 layering. 5 min.
-->

---

# IDOR — the missing check

```
GET /invoice/1041  →  check session? YES
                      check invoice.owner == session.user?  ✗
```

*Describe: two-line request evaluation — session authentication passes, object-ownership authorization is absent.*

<!--
UUID obscurity ≠ fix (MCQ-2.6). 4 min.
-->

---

# CS example — multi-tenant SaaS

- IDOR across tenants = worst case; test with two accounts
- Fix: authorization middleware on every object route

<!--
2 min.
-->

---

# DS example — model-scoring API

- SSRF via URL-scoring feature → internal service map
- Fix: scheme/host allow-list + egress deny by default

<!--
2 min. DS pipelines fetch URLs constantly — this is their SSRF surface.
-->

---

# Lab demo — Lab 06 (XSS/CSRF/SSRF/IDOR)

- Instructor chains sandbox XSS → cookie read → session replay, then fixes via encoding + `HttpOnly`
- **MVO:** exploit works, then fails after each fix
- Sandbox app only

<!--
DEMO 6 min. Chain demos teach layering better than isolated flaws.
-->

---

# Case session

**CS-050 "Client-side price"** (Level 2 · Secure web applications)

→ which of today's four? what does the server wrongly trust?

<!--
10 min. Model: server trusts client-computed price — trust-boundary framing.
-->

---

# Wrap-up & exit ticket

- Four flaws, four deceived components, four structural fixes
- **Exit:** match 4 one-line scenarios to flaw names

<!--
Close 110. Preview L08: SDLC & headers.
-->

---

# References

- OWASP Top 10; XSS Prevention Cheat Sheet; CWE-79/352/918/639
- Lecture plan lecture-07; Lab 06
