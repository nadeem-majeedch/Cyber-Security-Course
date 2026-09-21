# Lecture 13 — Network Defense I: Packet Analysis with Wireshark
**Module M4 · Week 7, Session 1 · 120 min · CLO-4 (primary)**

## Learning Objectives
1. Read TCP/IP and TLS flows at packet level: handshakes, resets, retransmissions, DNS, HTTP metadata.
2. Capture and filter traffic in Wireshark (capture vs. display filters) to isolate a conversation of interest.
3. Recognize suspicious patterns in a capture: scanning, beaconing, cleartext credentials, DNS anomalies.
4. Produce a packet-evidence summary with timestamps, endpoints, and frame citations.

## Key Concepts
- TCP handshake/teardown, RST semantics, retransmission storms; UDP patterns
- DNS as a telemetry goldmine (lookalike domains, high-entropy labels, tunneling awareness)
- TLS metadata without decryption: SNI, certificate chain, JA3/JA4 fingerprinting (concept)
- Wireshark skills: display filters (`ip.addr`, `tcp.stream`, `http`, `dns`), Follow Stream, Statistics → Conversations, I/O graphs
- Beacon detection: inter-arrival timing regularity (jitter analysis)

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–08 | Module 4 hook: play a 60-second capture; class guesses what happened | Hook |
| 08–30 | TCP refresher on the wire: handshake, stream following, RST storms — annotate on the projector | Live demo |
| 30–48 | Filter workshop: 10 progressive filters from "all traffic" to "one conversation"; students predict result counts before each | Guided practice |
| 48–60 | Break | — |
| 60–105 | **Lab block (Lab 12):** analyze provided capture A (normal) vs. B (seeded anomalies: one scan, one beacon, one cleartext POST); students produce an evidence summary | Hands-on |
| 105–115 | Beacon math: compute inter-arrival stats for the beaconing flow; discuss false positives (NTP, keepalives) | Mini-lecture + calc |
| 115–120 | Exit ticket; preview L14 (firewalls/segmentation) | Q&A |

## Examples
- **CS track:** RST-after-SYN pattern across 254 hosts — port-scan signature; students write the display filter that isolates it.
- **DS track:** the inter-arrival distribution as data: mean/σ, coefficient of variation; discuss threshold choice and its FPR (feeds Module 6).

## Discussion Questions
1. Why is TLS metadata still valuable when payloads are encrypted? What does it leak?
2. Display filters vs. capture filters — when do you need each?
3. Your beacon detector fires on a backup agent. Fix the detector or the deployment?

## Student Activity
Progressive-filter practice; paired capture analysis with an evidence template; class discussion of detection thresholds.

## Problem-Solving Scenario
> Capture B contains an internal host that: resolved a DDNS domain, opened a TLS session with an unusual JA3, and sent uniform 45-second small uploads for an hour. Produce: the endpoint+flow evidence table (with frame numbers), the pattern description, one hypothesis, and the filter chain you used.

## Summary
Packets don't lie, but they don't testify either — analysis turns capture into evidence. Filtering skill + timing analysis + metadata awareness = the SOC analyst's microscope. L14 adds the controls that shape what the wire carries at all.

## Formative Assessment
1. Which filter shows only one TCP conversation?
2. Name two things TLS metadata leaks without decryption.
3. What statistic distinguishes a beacon from normal traffic?

## Required Resources
- `labs/lab-12-packet-analysis/` capture files A/B (synthetic, sanitized)
- Wireshark (course VM); display-filter cheat sheet
- Bejtlich, *Practice of Network Security Monitoring* ch. 1–2 (excerpt)
- CLO mapping: **CLO-4** (objectives 1–4).
