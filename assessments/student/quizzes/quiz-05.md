# Quiz 5 — Specimen (Week 5) · Network Defense
**Ungraded self-check · 12 marks · ~12 minutes · CLO-4 · Answer key discussed in class; not posted.**

## Part A — Multiple choice (1 mark each)

**1.** The TCP three-way handshake sequence is:
- A. ACK → SYN → FIN
- B. SYN → SYN/ACK → ACK
- C. SYN → ACK → PSH
- D. SYN → FIN → RST

**2.** A TCP connect scan returns SYN/ACK for 22, 80, 443 and RST for everything else. Interpretation:
- A. Those three ports are open and accepting connections
- B. A firewall is silently dropping SYNs
- C. The host is offline
- D. All ports are filtered

**3.** A flat campus network hosts labs, servers, and BYOD on one subnet. The change that most reduces lateral-movement risk:
- A. Doubling the DHCP pool
- B. Separating server VLANs from client/BYOD zones with an intervening firewall
- C. Enabling spanning tree
- D. Increasing Wi-Fi transmit power

**4.** Rules process top-down: rule 1 allows 8080 from any → web01; rule 2 denies 8080 from untrusted-net → web01. Outcome:
- A. Rule 2 blocks untrusted-net
- B. Rule 1 matches first, so untrusted-net reaches 8080
- C. All traffic is denied
- D. The firewall logs a conflict and halts

**5.** An open captive-portal Wi-Fi is risky mainly because:
- A. It is slower
- B. Unauthenticated traffic is readable and spoofable by anyone in radio range without transport encryption
- C. It uses WPA3
- D. It throttles bandwidth

**6.** WPA3-SAE improves on WPA2-PSK chiefly by:
- A. Longer SSIDs
- B. Resisting offline dictionary attacks on the handshake
- C. Disabling guest networks
- D. Using a new frequency band

## Part B — Short answer (6 marks)

**7.** Design a minimal segmentation scheme for a school with (a) student laptops, (b) administration servers, (c) guest Wi-Fi. State the zones (1), the inter-zone default policy (2), one explicit exception you would allow (1), and the single most valuable logging point (2).

---
*Specimen items are contaminated for grading use once shown. Review answers against the in-class key.*
