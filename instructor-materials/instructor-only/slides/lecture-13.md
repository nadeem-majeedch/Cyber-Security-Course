---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L13 · Module 4 · Week 7'
---

<!-- _class: lead -->
# Lecture 13 — Network Security I
## Packet Analysis with Wireshark
**Module 4 · Week 7 · 120 min · CLO-4 (primary)**

<!--
TIMING: 1 min. Hook: open the course PCAP — "the incident is in this file; by hour's end you can find it."
-->

---

# Learning Objectives

1. Read a TCP conversation from SYN to FIN
2. Follow streams; read TLS handshake metadata
3. Spot scan/beacon/exfil patterns in captures
4. Filter with intent (display vs capture filters)

<!--
The PCAP is the lecture's spine. 3 min.
-->

---

# The TCP lifecycle on the wire

```
A ──SYN──► B        A ──data──► B        A ──FIN──► B
A ◄─SYN/ACK─ B      A ◄─data─── B        A ◄─ACK──── B
A ──ACK──► B
```

*Describe: three moments of a TCP conversation — handshake, data exchange, teardown — each as arrows between endpoints.*

<!--
MISCONCEPTION: "retransmits = attack." Noise vs signal — baseline first. 5 min.
-->

---

# Reading TLS without breaking it

| Observable | What it reveals |
|---|---|
| SNI field | server name being visited |
| certificate chain | issuer, validity, self-signed? |
| handshake size | client/server capabilities |

*Describe: three-row metadata table — TLS hides content, not metadata.*

<!--
Content stays encrypted; metadata still detects. 5 min.
-->

---

# Three patterns worth knowing

```
SCAN:    many SYNs, few completions, many destinations
BEACON:  regular intervals, similar sizes, one destination
EXFIL:   sustained upload, one pair, large volume
```

*Describe: three one-line signatures — scanning, beacons, and bulk transfer — each with its statistical fingerprint.*

<!--
These three signatures ARE Lab 12 and MT-G. Have students tag each in the course PCAP. 6 min.
-->

---

# CS example — log4j-style callback

- Outbound LDAP/RMI string in a capture = exploitation attempt signal
- Filter: `dns or ldap` + alert on internal workstations

<!--
2 min. Directional example; no CVE arithmetic.
-->

---

# DS example — flow features for models

- Flows → features: duration, bytes up/down ratio, interval variance
- Beacon regularity = low jitter — a feature, not just an eyeball

<!--
2 min. This table feeds L21's dataset directly.
-->

---

# Lab demo — Lab 12 (packet analysis)

- Instructor drives Wireshark on the course PCAP: stream-follow a session, isolate the beacon, export the IOC
- **MVO:** annotated PCAP with one flagged conversation + justification
- Prepared capture only — no live network collection

<!--
DEMO 6 min. Display filters cheat-sheet is in the lab sheet.
-->

---

# Case session

**CS-056 "Two logs, one story"** (Level 3 · Security monitoring)

→ correlate capture + host log; what's the timeline?

<!--
10 min. Correlation is the M4→M6 bridge.
-->

---

# Wrap-up & exit ticket

- Conversations, metadata, three signatures
- **Exit:** which pattern: "200 SYNs, 3 completions, 180 hosts"?

<!--
Close 110. Preview L14: segmentation design.
-->

---

# References

- Wireshark official docs; Bejtlich, *Practice of NSM*
- Lecture plan lecture-13; Lab 12; course PCAP v1
