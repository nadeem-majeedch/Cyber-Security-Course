---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L26 · Module 7 · Week 13'
---

<!-- _class: lead -->
# Lecture 26 — Cloud Security II
## Containers, Serverless & Secrets
**Module 7 · Week 13 · 120 min · CLO-7 (primary)**

<!--
TIMING: 1 min. Hook: "a container is a process with opinions about walls" — the walls are thinner than VMs.
-->

---

# Learning Objectives

1. Harden images (base, user, capabilities)
2. Explain escape vectors (privileged, socket mounts)
3. Manage secrets WITHOUT environment-as-vault
4. Apply least privilege to functions

<!--
Lab 24: the escape surface audit. 3 min.
-->

---

# Image hardening ladder

```
1. minimal base (distroless)      2. non-root USER
3. read-only rootfs               4. drop capabilities
5. pinned digests, scanned layers
```

*Describe: five-step hardening ladder ordered from base image to layer scanning; each step removes a class of escape fuel.*

<!--
SF-5's answer shape. Every step = smaller blast radius. 5 min.
-->

---

# Escape surfaces

```
--privileged            → host is the container's playground
docker.sock mounted     → talk to the host daemon = own the host
kernel exploits         → namespace/capability escape
```

*Describe: three escape surfaces; the socket mount and privileged flag convert a container bug into host compromise.*

<!--
MCQ-7.7. Kernel patches: whose responsibility? (customer's — IaaS). 4 min.
-->

---

# Secrets — where NOT to put them

| Location | Verdict |
|---|---|
| image layers | ❌ history is forever |
| env vars | ⚠️ visible in process/inspect |
| secret manager + runtime injection | ✅ audited, rotated |

*Describe: three-row verdict table for secret locations.*

<!--
MCQ-7.4's elimination principle applied to runtime. 4 min.
-->

---

# CS example — CI builds the image

- Distroless + non-root in the Dockerfile; scanner gate blocks critical CVE layers at build (L08 pattern)
- Admission policy blocks privileged at deploy — policy-as-code preview

<!--
2 min.
-->

---

# DS example — training jobs as functions

- Serverless training/eval jobs: scoped role per function, secrets via manager, no long-lived tokens in notebooks
- GPU node pools: same hardening ladder, higher blast radius

<!--
2 min.
-->

---

# Lab demo — Lab 24 (containers)

- Instructor audits the seeded container: privileged? socket? root? — fixes each, shows blocked deploy
- **MVO:** hardened image + admission-policy denial screenshot
- Course container sandbox only

<!--
DEMO 6 min.
-->

---

# Case session

**CS-064 "Serverless hours"** (Level 3 · Cloud security)

→ function-level IAM: where did the over-scope creep in?

<!--
10 min. Model: per-function roles vs shared execution role.
-->

---

# Wrap-up & exit ticket

- Images, surfaces, secrets — each shrinks blast radius
- **Exit:** two Dockerfile lines that reduce escape risk

<!--
Close 110. Preview L27: cloud detection.
-->

---

# References

- CIS Docker/Kubernetes Benchmarks; lecture plan lecture-26; Lab 24
