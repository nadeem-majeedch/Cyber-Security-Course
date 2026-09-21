# Lecture 16 — Wireless, VPN & Midterm Consolidation
**Module M4 · Week 8, Session 2 · 120 min · CLO-4 (primary) · CLO-2 (supporting)**

## Learning Objectives
1. Assess wireless security postures (open, WPA2-PSK, WPA2/3-Enterprise) and the attacks each invites (evil twin, deauth-adjacent, KREX-era history).
2. Compare VPN architectures (IPsec vs. TLS-VPN, full vs. split tunnel) and their exposure trade-offs.
3. Consolidate Modules 1–4 in the midterm examination.
4. Preview the second half's through-line: trust (M5), intelligence (M6), platforms (M7), synthesis (M8).

## Key Concepts
- 802.11 security: handshake basics, WPA2-PSK shared-secret math, WPA3-SAE improvement, enterprise 802.1X/EAP outline
- Rogue AP / evil twin; captive-portal risks; client-side isolation gaps
- VPN: tunnel modes, split-tunnel exfil paths, VPN as a perimeter choke point vs. ZTNA (from L14)
- Midterm scope: L01–L15 CLO-1..4 items, scenario-heavy

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–10 | Rapid-fire review: 8 concept questions spanning M1–M4 (game format) | Game |
| 10–30 | Wireless security walk: what each posture assumes and breaks; the evil-twin storyboard on campus Wi-Fi | Slides + story |
| 30–45 | VPN architecture comparison table; split-tunnel exfil path sketch; when ZTNA replaces the VPN | Discussion |
| 45–55 | Q&A sweep: students nominate the two topics they most want re-explained | Q&A |
| 55–60 | Break + exam setup | — |
| 60–115 | **Midterm examination** (closed-book; scenario questions; A/B variants) | Assessment |
| 115–120 | Collection, reassurance, M5 teaser (why ECB penguins matter) | Admin |

## Examples
- **CS track:** campus SSID clone with a captive portal harvesting credentials — students list the four tells and the network-side detection (new BSSID in the 802.11 frame headers).
- **DS track:** VPN concentration analytics: connection metadata per user/device; anomaly flags for credential sharing (concurrent geographically impossible sessions).

## Discussion Questions
1. Why does WPA3-SAE resist offline dictionary attacks that WPA2-PSK does not?
2. Split tunnel is convenient — what exactly does it expose, and to whom?
3. If the university moved fully to ZTNA, what happens to the VPN concentrator and its CVE risk?

## Student Activity
Review game in teams (peer teaching under pressure); wireless postures matching exercise; exam.

## Problem-Solving Scenario (pre-exam warm-up, not graded)
> Users report "password wrong" only on campus. An AP with the correct SSID but unknown BSSID appears in scans. Produce: the attack hypothesis, four client-side tells, and the two network-side detections (BSSID inventory drift, portal-domain mismatch).

## Summary
Wireless and remote access extend the perimeter to everywhere clients are — identity and posture become the perimeter. The midterm closes the first half; the second half builds trust machinery (crypto), intelligence (ML), platforms (cloud), and synthesis (capstone).

## Formative Assessment
Midterm itself; plus one-minute retrospective ("one topic I still fear").

## Required Resources
- Midterm A/B papers + keys in `assessments/` (instructor-only versions separated)
- 802.11 security comparison handout
- CLO mapping: **CLO-4** (objectives 1–2); consolidation of CLO-1..4 via the midterm.
