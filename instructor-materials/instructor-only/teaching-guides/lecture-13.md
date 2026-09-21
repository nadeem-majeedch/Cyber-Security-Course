# Teaching Guide — Lecture 13 (Packet Analysis with Wireshark)
**Instructor-only.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–08 | Hook: 60-second mystery capture | Class guesses; reveal that analysis, not playback, answers. |
| 08–30 | TCP on the wire | Handshake/teardown/RST annotated on the projector. |
| 30–48 | Filter workshop | Ten progressive filters; class predicts counts before each. |
| 48–60 | Break | — |
| 60–105 | Lab 12 (captures A/B) | Pairs; evidence template with frame citations. |
| 105–115 | Beacon math | mean/σ/CV; threshold debate. |
| 115–120 | Exit ticket + preview | Tease L14: "controls that shape the wire." |

## Board/Projector Activities

- **Projector:** Wireshark with capture B; zoom on the SYN-scan and the beacon flow; Statistics → Conversations view.
- **Board:** the inter-arrival table (t₀…tₙ) with mean/σ/CV computed live.

## Speaker Notes (key beats)

1. Open with the vantage-point point: you see what your tap sees — that shapes every conclusion.
2. Filters: capture = what you record (resource-limited), display = what you look at (analysis). Teach both; drill display.
3. TLS metadata: SNI, cert chain, JA3/JA4 — "encryption protects payload, not structure."
4. Beacon math: CV = σ/mean; low CV + known interval = beacon-shaped; enrichment decides (backup agents poll too).

## Expected Student Difficulties

- Filter syntax failures stall pairs. Fix: cheat-sheet card per seat; the ten drills are cumulative so syntax sticks.
- Students mistake any RST for scanning. Fix: pattern-and-scale rule; single RSTs are normal refusals.
- DS students stall at protocol mechanics. Fix: the CV calculation is *their* comfort zone — hand them the timing analysis role.

## Teaching Tips

- Pre-open Wireshark with capture B loaded; the 60-second hook must start instantly.
- Prediction-before-reveal (filter counts) keeps the class computing, not watching.
- Frame citations are graded: enforce "every claim has a frame number" in the evidence template.

## Answer Keys **[KEY]**

- Capture B expected findings: SYN-scan (host X → /24, frames ~40–90); beacon (host Y → DDNS domain, 45 s ± small jitter); cleartext POST with credentials (host Z, mid-capture).
- Threshold answer (model): alert when CV < 0.1 AND interval within ±15% of a stable mean over ≥ 10 intervals — accept defended alternatives.
- Exit ticket: 1 `tcp.stream eq N`; 2 SNI, cert chain/issuer (accept sizes/timing); 3 low coefficient of variation (regular inter-arrivals).

## Lab Delivery (Lab 12)

- Minimum viable outcome: evidence table with ≥ 5 rows, each with frame citations.
- Expected failure points: students filter display when they meant capture (or vice versa); Wireshark column confusion — preset the profile (columns: time, src, dst, info) in the lab image.

## Discussion Facilitation

Q3 (backup-agent FP) previews L15's tuning discussion; collect the two fix philosophies (detector vs deployment) on the board and leave them standing into next lecture.

## Accessibility

- Wireshark is visually dense: provide the annotated screenshot series + text transcript; the filter drills work entirely from text output.
- Beacon math: provide the inter-arrival CSV so calculations can be done in a spreadsheet, not off the screen.
