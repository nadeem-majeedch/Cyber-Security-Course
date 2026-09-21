# Question Bank — Module 4 (L13–L16) · CLO-4 · ⚠️ INSTRUCTOR-ONLY

Used by weekly quizzes Q5 (W5), Q7 (W7), and makeup packs. Duplicate-avoidance rule: see `README.md`.

## MCQ-4.1

**Topic:** TCP handshake · **CLO-4** · **Bloom:** Understand · **Difficulty:** Easy · **Week:** 5
**Used in:** Q5

The TCP three-way handshake sequence is:

- A. ACK → SYN → FIN
- B. SYN → SYN/ACK → ACK ✔
- C. SYN → ACK → PSH
- D. SYN → FIN → RST

**Explanation:** Standard connection setup; FIN/RST belong to teardown. Key: B.

## MCQ-4.2

**Topic:** Port scanning · **CLO-4** · **Bloom:** Apply · **Difficulty:** Medium · **Week:** 5
**Used in:** Q5

A TCP connect scan returns SYN/ACK for 22, 80, 443 and RST for others. Correct interpretation:

- A. Those three ports are open and accepting connections ✔
- B. A firewall is dropping SYN packets
- C. The host is offline
- D. All ports are filtered

**Explanation:** SYN/ACK = open (completing the handshake would confirm); RST = closed. Silent drops would show as timeouts (filtered). Key: A.

## MCQ-4.3

**Topic:** Segmentation rationale · **CLO-4** · **Bloom:** Analyze · **Difficulty:** Medium · **Week:** 5
**Used in:** Q5

A flat campus network puts labs, servers, and BYOD on one subnet. The segmentation change that most reduces lateral-movement risk:

- A. Double the DHCP pool
- B. Separate server VLANs from client/BYOD zones with an intervening firewall ✔
- C. Enable STP
- D. Increase Wi-Fi transmit power

**Explanation:** Lateral movement needs network paths; segmenting zones and filtering inter-zone traffic removes them. Key: B.

## MCQ-4.4

**Topic:** Firewall rule order · **CLO-4** · **Bloom:** Apply · **Difficulty:** Hard · **Week:** 5
**Used in:** Q5

Rules process top-down. `1: allow 8080 from any → web01` precedes `2: deny 8080 from untrusted-net → web01`. Outcome:

- A. The deny applies to untrusted-net
- B. The allow fires first, untrusted-net reaches 8080 ✔
- C. All traffic is denied
- D. Both rules log a conflict

**Explanation:** First-match wins; the broad allow shadows the deny. Order specific→general. Key: B.

## MCQ-4.5

**Topic:** IDS comparison · **CLO-4** · **Bloom:** Analyze · **Difficulty:** Medium · **Week:** 7
**Used in:** Q7

Compared with signature NIDS, anomaly NIDS can catch novel attacks but tends to:

- A. Use less CPU
- B. Generate more false positives ✔
- C. Need no baselines
- D. Miss all known attacks

**Explanation:** Deviation-from-baseline detection generalizes to new behavior at the cost of FP volume — the precision/recall tradeoff students meet again in M6. Key: B.

## MCQ-4.6

**Topic:** Wireless security · **CLO-4** · **Bloom:** Understand · **Difficulty:** Easy · **Week:** 7
**Used in:** Q7

An open captive-portal network is risky mainly because:

- A. It is slower
- B. Unauthenticated traffic is readable and spoofable by anyone in radio range (without transport encryption) ✔
- C. It uses WPA3
- D. It limits bandwidth

**Explanation:** No link-layer auth/encryption means any peer can observe or impersonate; TLS-protected traffic mitigates, everything else is exposed. Key: B.

## MCQ-4.7

**Topic:** WPA3 rationale · **CLO-4** · **Bloom:** Understand · **Difficulty:** Medium · **Week:** 7
**Used in:** Q7

WPA3-SAE improves on WPA2-PSK chiefly by:

- A. Longer SSIDs
- B. Resisting offline dictionary attacks on the handshake ✔
- C. Disabling guest networks
- D. 10 GHz operation

**Explanation:** SAE's dragonfly handshake limits offline guessing of the PSK — the WPA2 weakness. Key: B.

## MCQ-4.8

**Topic:** VPN security · **CLO-4** · **Bloom:** Evaluate · **Difficulty:** Hard · **Week:** 7
**Used in:** Q7

A "VPN equals secure" mindset fails most because:

- A. VPNs are illegal in some countries
- B. A connected device sits inside the trusted network — lateral-movement rules and endpoint posture still matter ✔
- C. VPNs block all ports
- D. VPN logs are always corrupted

**Explanation:** The VPN grants network presence, not safety; zero-trust posture (device health, least privilege, segmentation) still applies. Key: B.

## SA-4.1 (short answer, 6 marks)

**Topic:** Segment design · **CLO-4** · **Bloom:** Create · **Difficulty:** Medium · **Week:** 5
**Used in:** Q5

Design a minimal segmentation scheme for a school with (a) student laptops, (b) administration servers, (c) guest Wi-Fi. State zones, inter-zone policy defaults, and one logging point.

**Key:** Three zones (students, admin/servers, guests); default-deny between zones with explicit needs (e.g., students→admin app on 443 only; guests→internet only); log at the inter-zone firewall, alert on admin-zone access attempts from student/guest zones.

## SA-4.2 (short answer, 6 marks)

**Topic:** Alert triage · **CLO-4** · **Bloom:** Evaluate · **Difficulty:** Hard · **Week:** 7
**Used in:** makeup MT-5 only

A SIEM fires 400 alerts/night, 95% false positives. Propose a triage improvement plan with three concrete changes and the metric you would track.

**Key:** Tune noisy rules with allow-lists for known-good patterns; enrich alerts with asset criticality + threat intel for prioritization; group/correlate into incidents; track FP rate and mean-time-to-triage (accept ESCALATION rate, MTTD).
