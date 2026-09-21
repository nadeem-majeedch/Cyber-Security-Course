---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L10 · Module 3 · Week 5'
---

<!-- _class: lead -->
# Lecture 10 — Malware Analysis II
## Dynamic Analysis, Sandboxes & IOCs
**Module 3 · Week 5 · 120 min · CLO-3 (primary)**

<!--
TIMING: 1 min. Hook: "now we let it run — on OUR terms." Recap isolation contract in one line.
-->

---

# Learning Objectives

1. Configure a **fake-net** detonation environment
2. Observe process/file/network behavior safely
3. Extract IOCs and map to **ATT&CK**
4. Produce a reproducible behavior report

<!--
Fake-net is the centerpiece skill. 3 min.
-->

---

# The detonation chamber

```
[Victim VM] ──host-only──► [FakeNet: fake DNS/HTTP]
     │ snapshot BEFORE            ▲
     │                            │ records C2 attempts
     ▼                            └── never reaches internet
[revert AFTER]
```

*Describe: victim VM connected only to a fake-network appliance; snapshot taken before, reverted after; C2 attempts are recorded, never routed out.*

<!--
WHY fake-net: contain + record + reproduce. Checkpoint C item 6. 5 min.
-->

---

# What to watch — three telescopes

| Layer | Tool class | Example artifact |
|---|---|---|
| Process | API monitor | `CreateRemoteThread` |
| Filesystem | drop watcher | `.vbs` in %TEMP% |
| Network | fake-net logs | beacon to `cdn-stat[.]top` |

*Describe: three-row observation table; each layer catches what the others miss.*

<!--
Defanged indicators ONLY in reports/notes — the dot-bracket rule. 5 min.
-->

---

# Behavior → ATT&CK mapping

```
beacon 60 s ─► T1071.001 (Web Protocols)
scheduled task ─► T1053 (Scheduled Task)
%TEMP% svchost ─► T1036 (Masquerading)
```

*Describe: three observed behaviors mapped to technique IDs.*

<!--
EVIDENCE RULE: every technique ID needs the artifact that earns it — checkpoint C item 5 drills this. 4 min.
-->

---

# CS example — dropper chain

- Stage 1 static → stage 2 dynamic (payload fetch) → IOC: staged URL
- Report discipline: reproducible detonation steps

<!--
2 min.
-->

---

# DS example — telemetry contamination

- Detonations generate the logs your models train on — label provenance or poison M6
- Fix: tag sandbox telemetry, separate training stores

<!--
2 min. This is CS-092's seed — say so.
-->

---

# Lab demo — Lab 09 (dynamic analysis)

- Instructor detonates course sample: fake-net capture → process tree screenshot → IOC table → revert
- **MVO:** behavior report with ≥ 5 IOCs + 3 ATT&CK IDs
- Full isolation contract; revert verified on screen

<!--
DEMO 8 min — the longest demo of the term; budget it. Pivot: pre-captured log pack if VM misbehaves.
-->

---

# Case session

**CS-016 "Failures nobody watched"** (Level 1 · Security monitoring)

→ which telescope was missing at this org?

<!--
10 min. Model bridges M3→M4: unmonitored logs = unseen attacks.
-->

---

# Wrap-up & exit ticket

- Contain, observe, map, revert; defang IOCs; evidence or it didn't happen
- **Exit:** one behavior + its technique ID + the artifact name

<!--
Close 110. Preview L11: ransomware.
-->

---

# References

- Sikorski & Honig ch. 3; MITRE ATT&CK; course sample pack v1
- Lecture plan lecture-10; Lab 09
