---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L04 · Module 1 · Week 2'
---

<!-- _class: lead -->
# Lecture 04 — Defense in Depth, Least Privilege
## + Checkpoint A
**Module 1 · Week 2 · 120 min · CLO-1 (primary), CLO-8 (supporting)**

<!--
TIMING: 1 min. Hook: castle metaphor in 30 s, then immediately the modern version — "your layers are code, config, identity, detection."
-->

---

# Learning Objectives

1. Layer **preventive / detective / corrective** controls
2. Apply **least privilege** & secure defaults
3. Classify controls across admin/technical/physical
4. Demonstrate Module 1 mastery (Checkpoint A)

<!--
Announce checkpoint timing NOW: last 20 min, closed book. 3 min.
-->

---

# Defense in depth — layered failure

```
[Attacker]
   │  WAF (preventive)        ── bypassed
   ▼
[input validation]            ── bypassed
   ▼
[parameterized query]         ── holds ✓
   ▼
[least-priv DB account]       ── limits damage ✓
   ▼
[backups] (corrective)        ── recovery ✓
```

*Describe: vertical funnel of five layers; the attack penetrates two, is stopped by two, and the last bounds the damage.*

<!--
POINT: no single layer is load-bearing — that's the principle. 5 min.
-->

---

# Least privilege & secure defaults

| Principle | Bad default | Good default |
|---|---|---|
| Accounts | shared admin | per-person, scoped |
| Services | all enabled | off until needed |
| Storage | world-readable | owner-only + grants |

*Describe: three-row table contrasting permissive defaults with hardened ones.*

<!--
Secure defaults = the unsafe state doesn't exist (MCQ-1.8). 4 min.
-->

---

# Control taxonomy drill

```
            Preventive   Detective   Corrective
Technical   firewall     SIEM alert  restore backup
Admin       policy       audit       IR runbook
Physical    lock         camera      replacement
```

*Describe: 3×3 grid classifying controls by type and function with one example per cell.*

<!--
60-second drill: class fills empty cells. Then classify the L03 hypothesis's control (3 min).
-->

---

# CS example — containerized API

- Layers: schema validation → non-root user → read-only FS → egress allow-list
- Which layer fails silently? **Egress** — nobody watches it

<!--
2 min; egress returns in L07 SSRF.
-->

---

# DS example — training pipeline

- Layers: signed datasets → least-priv service accounts → drift alerts → backups
- Weakest human layer: shared service-account tokens

<!--
2 min; CS-073 preview.
-->

---

# Lab demo — Lab 03 (controls layering)

- Instructor hardens one service live: disable root SSH → dedicated user → log watch
- **MVO:** before/after `sshd -T` diff on screen
- Sandbox VM only

<!--
DEMO 4 min. Pivot: show config file diff if terminal sharing fails.
-->

---

# Checkpoint A — last 20 minutes

- 7 items: CIA, STRIDE, trees, surface (from `quizzes/quiz-02.md`)
- Closed book; recorded /10; lowest checkpoint dropped at term end

<!--
ADMIN: papers out at 100 min. After: 1-min preview of M2. Keys: assessments/instructor-only/checkpoint-keys.md — never project.
-->

---

# Case session (if time)

**CS-006 "Logged-in lab machine"** (Level 1 · Endpoint hardening)

→ apply least privilege: what would you change first?

<!--
Optional 8 min if checkpoint runs short — otherwise assign as reading.
-->

---

# Wrap-up

- Layers catch what single controls miss; defaults remove unsafe states
- **Reading:** L05 notes before Week 3

<!--
Close. M1 complete — log checkpoint scores today.
-->

---

# References

- NIST SP 800-53 (control families overview)
- Lecture plan lecture-04; Lab 03; checkpoint keys (instructor)
