---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L09 · Module 3 · Week 5'
---

<!-- _class: lead -->
# Lecture 09 — Malware Analysis I
## Static Triage in an Isolated VM
**Module 3 · Week 5 · 120 min · CLO-3 (primary)**

<!--
TIMING: 1 min. Hook: pass around (pictures of) a real-looking sample hash report — "we never ran it, and we know a lot."
-->

---

# Learning Objectives

1. Perform static triage: hashes → strings → imports → headers
2. Justify **sandbox isolation** controls
3. Extract IOCs without execution
4. Start an ATT&CK behavior map

<!--
Safety contract first (next slide), then skills. 3 min.
-->

---

# Safety contract (read verbatim)

> **Samples run only in the course VM: host-only network, snapshot taken, shared folders off, no production data on the host.**

- Violations = lab suspension for the module — no exceptions
- This contract appears in Lab 08/09 worksheets and the instructor manual

<!--
Read it slowly, get acknowledgment. This is a non-negotiable slide. 3 min.
-->

---

# Static triage pipeline

```
[file] ─► hash + TI lookup ─► filetype/headers ─► strings
      ─► imports (what APIs?) ─► embedded resources ─► IOC list
```

*Describe: six-stage left-to-right pipeline; every stage is static — no execution at any point.*

<!--
MISCONCEPTION: "strings is outdated" — packed binaries limit it, but stage ORDER is what matters. 6 min.
-->

---

# Reading PE/ELF headers

| Field | What it tells you |
|---|---|
| compile timestamp | provenance clue (spoofable) |
| sections | packed? (entropy, odd names) |
| imports | capabilities: network, crypto, process |

*Describe: three-row header-field table; imports reveal capability, entropy hints packing.*

<!--
Demo `file`, `objdump -x` on the course sample — benign one FIRST. 5 min.
-->

---

# CS example — supply-chain implant

- Imports list `WinHTTP` + crypto APIs in a "screensaver"
- Static IOC: unique mutex string → ATT&CK T1027 discussion

<!--
2 min.
-->

---

# DS example — dataset/drop triage

- Same discipline for suspicious "datasets": filetype, provenance, embedded scripts in CSVs
- Never open unverified files on the host OS

<!--
2 min. DS students receive files constantly — generalize the discipline.
-->

---

# Lab demo — Lab 08 (static analysis)

- Instructor triages the course sample: hash → strings → imports → IOC table
- **MVO:** 5 IOCs + 2 ATT&CK hypotheses, zero execution
- Isolation contract active throughout

<!--
DEMO 6 min. Capture the IOC table as the lab's exemplar artifact.
-->

---

# Case session

**CS-042 "Image that wasn't"** (Level 2 · Digital forensics)

→ what static artifact betrayed the masquerade?

<!--
10 min. Model: extension/mime mismatch + header truth.
-->

---

# Wrap-up & exit ticket

- Static-first, isolation always, IOCs before detonation
- **Exit:** 3 static stages in order + why never host-machine

<!--
Close 110. Preview L10: dynamic analysis.
-->

---

# References

- Sikorski & Honig, *Practical Malware Analysis*, ch. 1–2
- Lecture plan lecture-09; Lab 08; safety contract (instructor manual §)
