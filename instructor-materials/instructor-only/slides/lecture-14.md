---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L14 · Module 4 · Week 7'
---

<!-- _class: lead -->
# Lecture 14 — Network Security II
## Firewalls, Segmentation & Zero Trust
**Module 4 · Week 7 · 120 min · CLO-4 (primary)**

<!--
TIMING: 1 min. Hook: "flat network = one house key opens everything" — then draw zones.
-->

---

# Learning Objectives

1. Design zones with a **default-deny** inter-zone policy
2. Write minimal rulesets (specific → general)
3. Explain zero-trust's shift from location to identity
4. Choose sensor placement for lateral visibility

<!--
The zone diagram is the CLO-4 design artifact. 3 min.
-->

---

# Zones & choke points

```
[INTERNET] ──► [DMZ: web] ──► [APP zone] ──► [DATA zone]
                                   ▲
                             [MGMT: jump host]
        every arrow = a firewall policy point
```

*Describe: four zones chained left to right with a management zone above; each arrow is a policy enforcement and logging point.*

<!--
Every arrow: default-deny + explicit allow + LOG. MT-B's answer shape. 6 min.
-->

---

# Ruleset discipline

```
1. allow 443  internet  → web01        (specific)
2. allow 5432 app-zone  → db01         (specific)
3. deny   any any → any                (explicit default)
```

*Describe: three ordered rules — specific allows first, explicit default-deny last.*

<!--
First-match order: broad-allow-above-deny shadows it (MCQ-4.4). Rule minimalism = attack-surface discipline from L03. 4 min.
-->

---

# Zero trust — identity is the perimeter

| Classic | Zero trust |
|---|---|
| inside = trusted | verify explicitly |
| IP allow-lists | identity + device posture |
| flat east-west | per-flow authorization |

*Describe: three-row contrast table; trust moves from network location to per-request verification.*

<!--
"VPN = secure" dies here (MCQ-4.8). 4 min.
-->

---

# CS example — micro-segmentation

- Kubernetes NetworkPolicies: default-deny namespace, allow specific labels
- Same discipline, smaller boxes

<!--
2 min; L26 preview.
-->

---

# DS example — data-zone isolation

- Feature store and raw data in a separate zone; notebooks reach only the API
- Egress from data zone: none — exfil path removed

<!--
2 min. CS-073/074 echo.
-->

---

# Lab demo — Lab 13 (segmentation)

- Instructor adds a VLAN + inter-zone rules on the lab sandbox, then shows the blocked ping and the logged drop
- **MVO:** policy table + one logged denial as evidence
- Course sandbox switching only

<!--
DEMO 5 min. The LOGGED DROP is the teaching moment — policy without logging is hope.
-->

---

# Case session

**CS-025 "Summer of flat network"** (Level 2 · Segmentation)

→ draw the three-zone fix; what stays flat on purpose?

<!--
10 min. Model includes the tradeoff — some flat ops networks remain, priced in.
-->

---

# Wrap-up & exit ticket

- Zones, default-deny, explicit allows, logged everywhere
- **Exit:** one rule for student→admin traffic, written correctly

<!--
Close 110. Preview L15: IDS/IPS/SIEM.
-->

---

# References

- NIST SP 800-207 (zero trust overview); lecture plan lecture-14; Lab 13
