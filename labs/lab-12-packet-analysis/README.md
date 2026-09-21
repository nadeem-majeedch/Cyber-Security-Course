# Lab 12 — Network Traffic Analysis (Prepared Captures)
**Core Lab 2 · Module 4 (L13) · CLO-4 · Duration: 2 hours · Graded lab**

## 1. Learning Objectives
1. Use Wireshark display filters to isolate conversations and behaviors in provided captures.
2. Recognize three seeded anomaly classes in a prepared capture: a TCP SYN scan, a periodic beacon, and a cleartext credential POST.
3. Compute inter-arrival statistics for a flow and interpret them (beacon vs. legitimate polling).
4. Produce an evidence summary in which every claim cites frame numbers.

## 2. Prerequisites
Lecture 13 (TCP/IP on the wire, TLS metadata, filter workshop). Wireshark basics from the in-lecture demo.

## 3. Hardware/Software Requirements
- Course VM with Wireshark (or host install — captures are files; no live network needed).
- Instructor-provided capture files: `capture-A-normal.pcapng`, `capture-B-seeded.pcapng` (synthetic, generated for teaching).
- Calculator or spreadsheet for timing statistics.

## 4. Installation and Setup
1. Copy both capture files to your VM home directory (from the course share or LMS).
2. Open capture A; apply the profile preset in the course image (columns: time, source, destination, info).
3. Verify Wireshark opens both files without errors before starting the clock.
   *(File-open and filter syntax tested in the teaching-image build; the seeded capture content is instructor-generated and documented in the key.)*

## 5. Ethical Authorization and Safety Notes
- The captures are prepared artifacts: no live capture, no scanning, no network interaction with any third party is part of this lab.
- Do **not** attempt to "identify the real host" in the captures — endpoints are synthetic and fictional by design.
- If you capture your own traffic for curiosity, do it only on a network you own and only with the consent of everyone on it; submissions must use the provided files.

## 6. Step-by-Step Student Tasks
| # | Task | Filter / method hint |
|---|---|---|
| 1 | Baseline pass of capture A: how many conversations (Statistics → Conversations)? | — |
| 2 | Capture B: find the host performing SYN probes without completing handshakes | `tcp.flags.syn==1 and tcp.flags.ack==0 and tcp.flags.fin==0` |
| 3 | List the scanned destinations (count + address range) | Sort by destination |
| 4 | Find the repeating flow: one internal host, uniform-sized periodic small uploads | Statistics → Conversations → sort by bytes/packets |
| 5 | Extract that flow's timestamps; compute inter-arrival mean, σ, CV in a spreadsheet | `tshark -r capture-B-seeded.pcapng -Y "ip.addr==<host> && tcp.port==<port>" -T fields -e frame.time_epoch` *(tshark optional; Wireshark export works too)* |
| 6 | Find the cleartext POST carrying credentials | `http.request.method==POST` → Follow Stream |
| 7 | For each finding, record: endpoints, first/last frame numbers, protocol, and one-line pattern description | Evidence table |
| 8 | Hypothesis: which finding is most urgent and why | One paragraph |

## 7. Expected Observations
- Capture A: normal browsing patterns, varied inter-arrivals, no cleartext credentials (TLS everywhere).
- Capture B: (1) SYN-only probes across a /24 from one host; (2) a flow with ~45 s regular inter-arrivals (low CV) to a single external endpoint; (3) an HTTP POST with a username/password form in cleartext.

## 8. Questions for Analysis
1. Why does the SYN-only pattern indicate a scan rather than a connectivity problem? Name the two properties that distinguish them.
2. Your beacon flow's CV is low — but capture A contains an NTP-like flow that is also regular. What enrichment (L15 vocabulary) separates the two?
3. The cleartext POST: what single change to the service removes the exposure entirely, and why is that a *deployment* fix rather than a detection fix?

## 9. Troubleshooting
- Filter yields nothing → check you are in capture B, and that the display-filter bar is green (syntax valid).
- Timestamps look identical → check the time display format (View → Time Display Format → seconds since beginning).
- Wireshark opens but columns are confusing → load the course profile preset (Setup instructions §4.2).

## 10. Cleanup Instructions
- Remove capture files from your VM home after submission (they are re-issued next term).
- No snapshots to change; no services were run.

## 11. Submission Requirements
- Evidence table (≥ 8 rows, each with frame citations).
- Timing analysis: inter-arrival table + mean/σ/CV for the beacon flow.
- Answers to the three analysis questions.
- One paragraph: hypothesis + recommended next action.

## 12. Expected Outputs / Evidence
`evidence.md` (table + answers), `timing.csv` or spreadsheet screenshot, all personally produced from the provided captures.

---
### Instructor Answer Key (summary — full version in `assessments/instructor-only/`)
- Seeded findings in capture B: scan from 10.10.10.66 → 10.10.10.0/24 (frames ≈ 40–90); beacon 10.10.10.42 → 203.0.113.77:443 at ~45 s ± small jitter (frames ≈ 300–520); cleartext POST 10.10.10.51 → 198.51.100.9 with form fields `user`/`pass` (frames ≈ 700–706).
- Scan vs. outage: many distinct destinations + uniform SYN-only shape (an outage retries one destination, with retransmissions not probes).
- Enrichment: the NTP flow's destination is a known infrastructure service with long-lived allocation; the beacon's destination is an unclassified external endpoint — asset context separates them.
- Cleartext fix: enable TLS on the service (transport fix); detection would only ever be a compensating control.

### Assessment Rubric (20 pts)
| Criterion | Points |
|---|---|
| Three findings identified with frame citations | 6 |
| Timing statistics computed and interpreted (CV argument) | 4 |
| Evidence table completeness and accuracy | 4 |
| Analysis answers | 4 |
| Urgency hypothesis with justification | 2 |
