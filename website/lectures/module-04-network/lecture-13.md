# Lecture 13 — Network Defense I: Packet Analysis with Wireshark
**Module 4 · Week 7, Session 1 · 2 hours · CLO-4**

## Learning Objectives
1. Read TCP/IP and TLS flows at packet level: handshakes, resets, retransmissions, DNS, HTTP metadata.
2. Use Wireshark capture vs. display filters to isolate a conversation of interest.
3. Recognize suspicious patterns in a capture: scans, beacons, cleartext credentials, DNS anomalies.
4. Produce a packet-evidence summary with timestamps, endpoints, and frame citations.

## Key Concepts and Definitions

**TCP handshake:** `SYN` → `SYN/ACK` → `ACK` (connection), `FIN`/`RST` teardown. **RST storms** across many hosts = scanning class. **Retransmission bursts** = congestion or interference, not (by itself) attack.

**DNS as telemetry:** every lookup names a destination before any payload flows. Look for: lookalike domains (typosquatting), high-entropy labels (algorithmically generated domains — *indicator, not proof*), and tunneling *concepts* (data encoded in queries — awareness level).

**TLS metadata without decryption:** SNI (server name), certificate chain and issuer, handshake fingerprint (**JA3/JA4** — a hash of the handshake parameters). Fact: encryption protects payload, not metadata; metadata analysis is a legitimate, privacy-conscious detection source.

**Wireshark skills:**

| Task | Filter (display) |
|---|---|
| One conversation | `tcp.stream eq N` |
| All HTTP to one host | `http.request and ip.addr eq A` |
| DNS to suspicious domain | `dns.qry.name contains "example"` |
| SYN scan shape | `tcp.flags.syn eq 1 and tcp.flags.ack eq 0` |

**Beacon detection as measurement:** inter-arrival times of periodic flows → mean and coefficient of variation (σ/mean). Low CV ≈ regular (beacon-like); high CV ≈ human/chaotic. *Assumption to verify:* legitimate services also poll regularly (NTP, keepalives) — context enrichment decides.

## Conceptual Diagram

```text
host A ──SYN──► host B:80   (scan: many hosts, few ports, RST answers)
host A ──SYN/SYNACK/ACK──► host B:443 ──TLS ClientHello (SNI=…)──► beacons
        every 45 s ± jitter  ◄── inter-arrival table = your evidence
```

## Realistic Examples

- **CS track:** capture B shows SYN-without-ACK across 254 hosts: the scan signature; students write the display filter that isolates it and cite frames.
- **DS track:** the inter-arrival distribution *is* a dataset: compute mean, σ, CV for the beacon flow; discuss the threshold choice and its false-positive cost on the backup agent (the same trade-off returns in L21 with a model instead of a threshold).

## Common Misconceptions

| Misconception | Correction |
|---|---|
| "Encrypted = invisible" | Payload is protected; SNI, timing, sizes, and endpoints leak structure. |
| "Wireshark captures everything on the network" | You capture what your vantage point sees; switch ports and TLS scope change the picture. |
| "A high-entropy DNS label proves malware" | It is an indicator — CDN/token subdomains also look random; enrich before judging. |
| "RST packets mean attack" | RSTs are normal refusals; *pattern and scale* make the signature. |

## Classroom Activities

1. **Filter progressive drill (20 min):** ten filters from "all traffic" to "one conversation"; students predict result counts before each reveal.
2. **Lab 12 (45 min):** capture A (normal) vs. B (seeded: one scan, one beacon, one cleartext POST) — evidence summary with frame citations.
3. **Beacon math (10 min):** compute mean/σ/CV for the beacon flow; argue a threshold.

## Discussion Questions

1. Why is TLS metadata still valuable when payloads are encrypted — and what does it leak?
2. Capture filters vs. display filters: when do you *need* each?
3. Your beacon detector fires on a backup agent. Fix the detector, the deployment, or both?

## Problem-Solving Exercise

> Capture B: an internal host resolves a DDNS domain, opens TLS with an unusual fingerprint, and sends uniform 45-second small uploads for an hour.
> **Deliverable:** endpoint + flow evidence table (with frame numbers); pattern description; one hypothesis; the filter chain you used.

## Summary

Packets don't lie, but they don't testify either — analysis turns capture into evidence: filtering skill, timing math, metadata awareness. Next lecture adds the controls that shape what the wire carries at all.

## Exit Ticket

1. Which display filter isolates one TCP conversation?
2. Name two things TLS metadata leaks without decryption.
3. What statistic distinguishes a beacon from normal periodic traffic?

## References

- Wireshark official documentation & display filter reference. https://www.wireshark.org/docs/
- Bejtlich, R., *The Practice of Network Security Monitoring*, ch. 1–2, No Starch Press.
- Postel, J., RFC 793 (TCP). https://datatracker.ietf.org
- Salesforce, *JA3* project page; *JA4* specification. https://github.com/salesforce/ja3
