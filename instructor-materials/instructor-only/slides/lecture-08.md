---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L08 · Module 2 · Week 4'
---

<!-- _class: lead -->
# Lecture 08 — Web Security IV
## Secure SDLC, Headers & Checkpoint B
**Module 2 · Week 4 · 120 min · CLO-2 (primary)**

<!--
TIMING: 1 min. Hook: cost-of-late-fix sketch — 1× design, 10× code, 100× production (directional, not a statistic).
-->

---

# Learning Objectives

1. Place SAST/DAST/SCA in the pipeline
2. Configure **CSP** & **HSTS** with their limits
3. Describe a secure SDLC gate model
4. Demonstrate Module 2 mastery (Checkpoint B)

<!--
Checkpoint B at min 100. 3 min.
-->

---

# Shifting security left

```
Design ──► Code ──► Build ──► Test ──► Release ──► Operate
  ▲           ▲        ▲         ▲
 threat     SAST     SCA/      DAST
 modeling   secrets  deps      + pentest
```

*Describe: pipeline with four check-ins — threat modeling at design, static analysis at code, dependency scanning at build, dynamic testing before release.*

<!--
MCQ-2.8's answer: scanning at merge, not at freeze. 5 min.
-->

---

# Security headers that matter

| Header | Mitigates | Limit |
|---|---|---|
| CSP | XSS impact | `unsafe-inline` ruins it |
| HSTS | SSL-strip, downgrade | first visit unprotected |
| X-Content-Type-Options | MIME sniffing | narrow scope |

*Describe: three-row header table with mitigation and honest limitation columns.*

<!--
Headers are REDUCTION not cure — limits column is the exam discriminator (SA-2.2). 5 min.
-->

---

# Dependency & secret hygiene

- SCA: licenses + CVEs in the lockfile
- Secret scanning: keys never reach git history
- Misconception: "we'll rotate if leaked" — bots beat you to it

<!--
Recall CS-014 and MCQ-7.4's elimination principle. 3 min.
-->

---

# CS example — PR gate

- Merge blocked if: new critical SCA hit, secret pattern, SAST regression
- Tradeoff: gate fatigue → allowlist process, not disabling

<!--
2 min.
-->

---

# DS example — model release pipeline

- Same gates for notebooks: dependency lock, dataset provenance check, no secrets in cells
- DAST equivalent: probe the scoring API's error paths

<!--
2 min.
-->

---

# Lab demo — Lab 07 (headers & SDLC)

- Instructor adds CSP/HSTS to the sandbox app, shows one inline script break, fixes with nonce
- **MVO:** headers verified via curl; one CSP violation caught live
- Sandbox app only

<!--
DEMO 5 min. The "CSP breaks something" moment is the lesson — plan for it.
-->

---

# Checkpoint B — last 20 minutes

- 8 items: CWEs, shell semantics, session, IDOR, one scenario pair
- From `quizzes/quiz-04.md`; keys in checkpoint-keys.md

<!--
ADMIN at min 100. Module 2 complete after. Preview M3 malware.
-->

---

# Case session (if time)

**CS-049 "Ten routes, one sanitizer"** (Level 3 · Secure web applications)

→ centralize vs distribute validation?

<!--
Optional; assign otherwise. SDLC framing: one chokepoint or per-route?
-->

---

# Wrap-up

- Pipeline gates beat release heroics; headers reduce, don't cure
- **Reading:** L09 notes; VM check for M3

<!--
Close. VM check reminder is critical for L09.
-->

---

# References

- OWASP ASVS (verification levels); MDN CSP docs
- Lecture plan lecture-08; Lab 07; checkpoint keys (instructor)
