# Teaching Guide — Lecture 10 (Dynamic Analysis, Sandboxes, IOCs)
**Instructor-only.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–08 | Reveal: what the samples did | Instructor pre-ran them; reveal closes L09's hypotheses. |
| 08–30 | Instrumentation tour | Four sensor layers; fake-net logs examined live. |
| 30–52 | Guided dynamic run | Class calls behaviors; ATT&CK table fills together. |
| 52–60 | Break | — |
| 60–105 | Lab 09 (samples 2–3) | Driver/observer pairs; IOC tables; mappings with citations. |
| 105–115 | IOC curation workshop | Quality criteria applied; STIX-lite table. |
| 115–120 | Exit ticket + preview | Tease L11: "the most disruptive behavior class." |

## Board/Projector Activities

- **Projector:** the sensor stack (process/file/registry/network) with the fake-net's DNS log beside it.
- **Board:** the behavior-chain diagram built live for sample 1; the ATT&CK mapping table beside it.

## Speaker Notes (key beats)

1. Evidence rule from minute one: every behavior claim gets a citation (procmon line, frame number). No citation, no claim.
2. Beacon math: compute inter-arrival mean/σ from timestamps; jitter explains why the mean alone isn't the story.
3. IOC quality = specific + observable + attributable; cull the table ruthlessly.
4. Evasion awareness: sleep bombs and VM checks mean "sandbox silent" ≠ "benign" — notes must carry that caveat.

## Expected Student Difficulties

- Pairs where the driver hoards the keyboard. Fix: driver/observer roles swap at the break — non-negotiable.
- Students list every registry access as an IOC. Fix: apply the three quality criteria; ambient noise dies.
- ATT&CK ambiguity (two candidate techniques). Fix: record the better-evidenced one and note the alternative — that *is* professional practice.

## Teaching Tips

- Pre-run both samples; know the expected behavior chains cold (keys below).
- The reveal at the start is the hook: "your hypotheses from last week — here is what actually happened."
- Seed one *silent* behavior into sample 3 (a delayed write) so the "absence of evidence" caveat lands from experience.

## Answer Keys **[KEY]**

- Sample 2 behavior chain: dropper URL fetch → writes EXE to temp → Run key → DNS to C2 → HTTP beacon 60 s ± jitter. Mappings: T1105 (ingress tool transfer, accept T1071), T1547.001 (Run key), T1071 (app-layer protocol).
- Sample 3 behavior chain: writes `%APPDATA%\svchost32.exe` → scheduled task → DDNS resolution → 45 s POST beacon. Mappings: T1547-class (accept T1053.005), T1568-class (DDNS C2), T1071.
- Exit ticket: 1 Run key, scheduled task (accept service); 2 specific observable vs. behavior class; 3 containment + evidence integrity (nothing reaches real C2).

## Lab Delivery (Lab 09)

- Minimum viable outcome: one behavior chain + ATT&CK mapping with citations + curated IOC table (≥ 3).
- Expected failure points: snapshot restore forgotten between samples (cross-contamination of evidence) — restore is a checklist line; fake-net certificate warnings are expected noise, explain once.

## Discussion Facilitation

Q2 (IP vs. domain IOC) rewards operational thinking — IP is specific but infra-rotates; a DDNS domain is stable but broad. Q3 (two candidate techniques) previews detection engineering: the choice changes what rule you write (L24 callback).

## Accessibility

- Dynamic-analysis screens move fast: the sensor-layer narration script is available in advance; students may record their own runs and review at their own pace.
- IOC table: provide as a structured CSV/spreadsheet template, not just markdown.
