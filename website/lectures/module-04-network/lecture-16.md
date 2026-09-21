# Lecture 16 — Wireless, VPN & Midterm Consolidation
**Module 4 · Week 8, Session 2 · 2 hours · CLO-4 (primary), CLO-2 (supporting)**

## Learning Objectives
1. Assess wireless security postures (open, WPA2-PSK, WPA2/3-Enterprise) and the attacks each invites.
2. Compare VPN architectures (IPsec vs. TLS-VPN; full vs. split tunnel) and their exposure trade-offs.
3. Consolidate Modules 1–4 (midterm examination).

## Key Concepts and Definitions

**802.11 security postures:**

| Posture | What it assumes | Invited attacks |
|---|---|---|
| Open | Users self-select; no link encryption | Passive capture, captive-portal credential theft |
| WPA2-PSK | Shared pre-shared key | Offline dictionary attack on the 4-way handshake (if the PSK is weak) |
| WPA3-SAE | Per-try handshake | Resists offline guessing ( Dragonslayer-class issues exist; still the better default) |
| WPA2/3-Enterprise (802.1X/EAP) | Per-user credentials via RADIUS | Evil-twin AP + credential harvesting if clients don't validate the server cert |

**Evil twin / rogue AP:** an attacker's AP clones your SSID; clients associate; credentials or traffic get harvested. Client-side tells: certificate warnings, captive-portal domain mismatch. Network-side detection: new BSSID in 802.11 frames, AP inventory drift.

**VPN architectures:** **IPsec** (network-layer tunnels, site-to-site workhorse) vs. **TLS-VPN** (client convenience). **Full tunnel** routes everything through the corporate edge (inspectable, costly); **split tunnel** routes only "corporate" destinations (efficient; the rest leaves unmanaged — and the endpoint is still on both worlds).

**ZTNA vs. VPN (from L14):** per-application brokered access shrinks the blast radius a stolen VPN credential grants — the network is never "reachable," only the app.

**Midterm scope:** CLO-1..4 integration — threat models (L02–L03), controls layering (L04), web flaw classes and fixes (L05–L07), SDLC (L08), malware analysis flow (L09–L11), social engineering (L12), packet analysis (L13), segmentation (L14), detection and triage (L15). Scenario questions, not recall.

## Conceptual Diagram

```text
evil twin:  victim ──associates──► rogue AP (same SSID) ──► harvest portal
detection:  AP inventory drift (new BSSID) + portal-domain mismatch
split VPN:  endpoint ──► corporate dests via tunnel ──► everything else direct
            (inspection blind spot = egress discipline matters)
```

## Realistic Examples

- **CS track:** the campus SSID cloned outside the library: four client-side tells (cert warning, portal domain, SSID behavior differences, latency) and two network-side detections (BSSID inventory, portal-domain mismatch).
- **DS track:** VPN concentration analytics: connection metadata per user/device; anomaly flags for credential sharing — concurrent, geographically impossible sessions (a rule-based detection today; the ML upgrade arrives in M6).

## Common Misconceptions

| Misconception | Correction |
|---|---|
| "WPA2 means the network is secure" | WPA2 protects the *link* against outsiders; a weak PSK, evil twins, and insiders remain. |
| "HTTPS makes the evil twin harmless" |TLS protects content, but the portal/certificate tells and user behavior still leak credentials. |
| "Split tunnel is just performance tuning" | It is an inspection/exposure decision with egress consequences. |
| "Zero-trust replaces the VPN *today*" | It replaces the *trust model*; migration is incremental per application. |

## Classroom Activities

1. **Review game (10 min):** eight rapid concept questions spanning M1–M4, teams answer on mini-whiteboards.
2. **Posture matching (5 min):** given four scenarios, choose the right 802.11 posture and name its invited attack.
3. **Warm-up scenario (10 min, ungraded):** the "wrong password only on campus" evil-twin case.
4. **Midterm (55 min).**

## Discussion Questions

1. Why does WPA3-SAE resist offline dictionary attacks that WPA2-PSK invites?
2. Split tunnel is convenient — what exactly does it expose, and to whom?
3. If the university moved fully to ZTNA, what happens to the VPN concentrator and its CVE risk?

## Problem-Solving Exercise (pre-exam warm-up, ungraded)

> Users report "password wrong" only on campus. An AP with the correct SSID but an unknown BSSID appears in scans.
> **Deliverable:** the attack hypothesis; four client-side tells; two network-side detections.

## Summary

Wireless and remote access extend the perimeter to wherever clients are — identity and posture become the perimeter. The midterm closes the first half; the second half builds trust machinery (crypto), intelligence (ML), platforms (cloud), and synthesis (capstone).

## Exit Ticket

Midterm itself, plus a one-minute retrospective: "one topic I still fear" (drives the post-midterm office-hours plan).

## References

- NIST SP 800-48 Rev. 1, *Guide to Securing Legacy IEEE 802.11 Wireless Networks*. https://csrc.nist.gov
- Wi-Fi Alliance, *WPA3* overview. https://www.wi-fi.org
- NIST SP 800-207, *Zero Trust Architecture* (recap from L14). https://csrc.nist.gov
- Stallings & Brown, *Computer Security* (wireless and remote-access chapters).
