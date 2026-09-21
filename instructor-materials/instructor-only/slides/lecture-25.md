---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L25 · Module 7 · Week 13'
---

<!-- _class: lead -->
# Lecture 25 — Cloud Security I
## Shared Responsibility & IAM
**Module 7 · Week 13 · 120 min · CLO-7 (primary)**

<!--
TIMING: 1 min. Hook: "in the cloud, the perimeter is a LOGIN PAGE." Recall MCQ-7.2.
-->

---

# Learning Objectives

1. Allocate responsibilities across IaaS/PaaS/SaaS
2. Design least-privilege **IAM** (roles, not keys)
3. Explain why identity is the new perimeter
4. Audit an IAM policy against wildcard sprawl

<!--
Lab 23 audits the seeded IAM mess. 3 min.
-->

---

# Shared responsibility — the split

```
        OF the cloud:  provider — hypervisor, physical, host infra
        IN the cloud:  customer — guest OS, config, data, IAM
        PaaS moves runtime patching to "of"
```

*Describe: three-line split; the boundary shifts by service model, data and identity always stay customer-side.*

<!--
Checkpoint F item 1. Ambiguity = where incidents live. 5 min.
-->

---

# Identity as perimeter

```
classic:   trust = network location
cloud:     trust = verified identity + scoped permissions
leaked key = sitting INSIDE, everywhere
```

*Describe: three-line contrast; credential compromise replaces network intrusion as the entry event.*

<!--
MCQ-7.2/7.4; CS-089 "cloud key that saw everything" is the L4 version. 4 min.
-->

---

# IAM hygiene

| Control | Replaces | Why |
|---|---|---|
| roles (short-lived) | static keys | expiry kills leak windows |
| scoped policies | wildcards | `*` on `*` = full compromise |
| permission boundaries | good intentions | blast-radius caps |

*Describe: three-row control table; roles, scoped policies, and boundaries each remove a standing risk.*

<!--
MCQ-7.3. Roles-vs-keys elimination argument (SF-1) — 5 min.
-->

---

# CS example — CI/CD to cloud

- Pipeline assumes role at deploy time — no long-lived keys in env vars
- Secret scanning in CI as the detective layer (recall L08 gates)

<!--
2 min.
-->

---

# DS example — data-science workspace

- Notebooks read feature store via scoped role, never owner keys
- Buckets: block-public-access at the ACCOUNT level, not per-bucket hope

<!--
2 min. Account-level guardrails vs per-resource wishes — CS-088's lesson.
-->

---

# Lab demo — Lab 23 (cloud IAM audit)

- Instructor walks the seeded sandbox project: wildcard policy, static key in a script, public bucket — audits then fixes each
- **MVO:** responsibility matrix + three fixed findings with re-verify
- Course cloud sandbox/LocalStack equivalent only

<!--
DEMO 6 min. Fix-verify pairs again — the course rhythm.
-->

---

# Case session

**CS-062 "IAM archaeology"** (Level 3 · Cloud security)

→ how does permission sprawl ACCUMULATE? design the inventory.

<!--
10 min. Model: drift + no reviews; links to L27's drift detection.
-->

---

# Wrap-up & exit ticket

- Boundary shifts by model; identity is perimeter; roles beat keys
- **Exit:** allocate guest-OS patching + bucket policy: who, and why

<!--
Close 110. Preview L26: containers.
-->

---

# References

- NIST SP 800-145; CIS Benchmarks (IAM sections); lecture plan lecture-25; Lab 23
