# Lab 09 — Dynamic Analysis & IOCs (Sandboxed)
**Enrichment · Module 3 (L10) · CLO-3 · Duration: 2 hours · Check-in lab**

## Learning Objectives
1. Run the synthetic samples under instrumentation (process/file/registry/network sensors + fake-net).
2. Build a behavior chain with evidence citations (sensor line / frame number).
3. Extract and curate IOCs against quality criteria (specific, observable, attributable).
4. Map ≥ 6 behaviors to ATT&CK techniques and write one detection hypothesis.

## Prerequisites
Lecture 10; Lab 08's analyst notes (your hypotheses become expectations).

## Hardware/Software Requirements
Analysis VM (same image as Lab 08, **restored from the clean snapshot**); sensor tooling in the image (process monitor-class, registry watcher, fake-net with DNS/HTTP logs); the two synthetic samples; Wireshark for the capture side.

## Installation and Setup
1. Restore snapshot `lab08-clean`; re-snapshot as `lab09-clean`.
2. Verify fake-net is answering (`nslookup anything.invalid` → sandbox IP).
3. Start all four sensor captures; confirm each writes a log file.

## Ethical Authorization and Safety Notes
- Samples are the same harmless teaching artifacts as Lab 08; dynamic analysis here means *watching them behave* in a sandbox where every network answer is simulated.
- Nothing leaves the VM: fake-net guarantees it; verify it (setup step 2) — that verification is part of the graded procedure.
- Restore the snapshot between samples; cross-contaminated evidence is a methodology failure, not a curiosity.

## Step-by-Step Student Tasks
1. Execute sample 2; collect the four sensor logs; note every behavior with a citation.
2. Repeat for sample 3 (restore snapshot first).
3. Behavior-chain diagram for each sample (arrows = observed causality, not inference).
4. ATT&CK mapping: ≥ 6 behaviors across both samples, each with technique ID + evidence citation.
5. IOC table: ≥ 5 entries; apply the quality criteria column; cull anything ambient.
6. Detection hypothesis: one rule-shaped statement (if behavior X with telemetry Y → alert) a SOC could deploy.
7. The delayed-write observation: one sample performs a low-and-slow action after 3+ minutes — document it and note what an automated 60-second sandbox would have missed.

## Expected Observations
- Sample 2: DNS query → HTTP beacon (60 s ± jitter) → writes a temp file → no persistence.
- Sample 3: Run-key write → scheduled task → DDNS resolution → 45 s POST beacon → the delayed config fetch (~4 min in).
- Fake-net logs show every "external" request answered locally — zero real egress.

## Questions for Analysis
1. Which of your IOCs will age fastest, and which would still be true next year? What does that imply for report structure (IOCs vs TTPs)?
2. The delayed action: what does it tell you about automated-sandbox coverage, and what is your compensating procedure?

## Troubleshooting
No beacon observed → check fake-net is answering (setup 2); samples are configured to fail silently without simulated DNS. Sensors empty → wrong log path; the image's `~/sensor-logs/` is authoritative. VM behaving oddly → restore snapshot; that is what it is for.

## Cleanup Instructions
Restore `lab09-clean`; export your logs *before* restoring; delete samples.

## Submission Requirements
Behavior-chain diagrams (2), ATT&CK table (≥ 6 with citations), IOC table (≥ 5 with quality columns), detection hypothesis, the delayed-action note.

## Expected Outputs / Evidence
Every behavior claim cites a sensor line or frame; uncited claims are not graded.

---
### Instructor Answer Key (summary)
- Sample 2 behaviors: DNS to `telemetry.example-security-lab.invalid`; HTTP GET beacon 60 s ± 8 s; temp file `%TEMP%\updater.dat`; no persistence. ATT&CK: T1071, T1105-class.
- Sample 3 behaviors: Run-key write (`HKCU\...\Run\svchost32`), scheduled task `SyncTask`, DDNS resolution, POST beacon 45 s ± 2 s, delayed config fetch at ~4 min. ATT&CK: T1547.001, T1053.005, T1568-class, T1071.
- High-quality IOCs: the two `.invalid` domains (specific, observable), the Run-key path, the task name; cull: generic `svchost32.exe` name alone (too common) — keep it only with its path.
- Detection hypothesis (model): "Process writes to `HKCU\...\Run` AND resolves a DDNS-class domain within 60 s → alert."

### Assessment Rubric (10 pts — check-in)
| Criterion | Points |
|---|---|
| Behavior chains with citations (2) | 3 |
| ATT&CK mapping (≥ 6, correct IDs) | 3 |
| IOC table quality (criteria applied, culled) | 2 |
| Detection hypothesis + delayed-action note | 2 |
