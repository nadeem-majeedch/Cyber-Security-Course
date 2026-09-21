# Lab 08 — Malware Static Triage (Synthetic Samples)
**Enrichment · Module 3 (L09) · CLO-3 · Duration: 2 hours · Check-in lab**

## Learning Objectives
1. Apply the safe-analysis procedure (VM, snapshot, no shared folders) before touching any sample.
2. Perform static triage: hashes, strings, imports, section entropy.
3. Write an analyst note: identifiers → capabilities (evidence-cited) → verdict → confidence.
4. List exactly what dynamic analysis must confirm.

## Prerequisites
Lecture 09 and its safety contract (read aloud in class; restated here).

## Hardware/Software Requirements
Course **analysis VM** (isolated image; fake-net configured); the instructor-provided **synthetic** samples `sample-2.bin`, `sample-3.bin` (built for teaching; harmless by construction — no real malicious payload, no persistence, no network escape); `strings`, `sha256sum`, entropy tool, PE/ELF header viewer.

## Installation and Setup
1. Boot the analysis VM; **snapshot `lab08-clean` before anything else**.
2. Verify isolation: shared folders off, network = internal fake-net only.
3. Copy samples into `~/samples/`; hash them first:
   ```bash
   sha256sum sample-*.bin | tee hashes.txt
   ```

## Ethical Authorization and Safety Notes
- The samples are synthetic teaching artifacts: they contain the *indicators* (imports, strings, entropy) without the *capability* — no harmful code can execute because there is none to execute.
- The isolation procedure is still mandatory: it is the professional habit this course certifies you in.
- Real malicious binaries are out of scope everywhere in this course; if you obtain one elsewhere, do not bring it into the lab.

## Step-by-Step Student Tasks
1. Hash both samples; record in `hashes.txt`.
2. Strings pass (both ASCII and UTF-16): list network indicators, mutex-like strings, file paths.
3. Imports pass: group imports into capability stories (network / process / persistence); cite the import names.
4. Entropy pass: compute per-section entropy; interpret (packed vs. not).
5. Write one analyst note per sample in the template (identifiers → capabilities → verdict → confidence → what-dynamic-must-confirm).
6. Peer cross-check: swap notes; find one missed capability hint in your partner's note.

## Expected Observations
- Sample 2: URL string + `WSAStartup`/`connect` imports → network-capable dropper hypothesis (medium confidence).
- Sample 3: Run-key strings + scheduled-task imports + DDNS-looking domain → persistence + C2 hypothesis (medium-high confidence).
- Entropy: one sample has a packed section (> 7.0) explaining its thin strings output.

## Questions for Analysis
1. Which claim in your note has the *weakest* evidence, and what dynamic observation would settle it?
2. High entropy had three candidate explanations in lecture. Which applies to your sample, and what made you decide?

## Troubleshooting
Strings output empty → try the UTF-16 flag (`strings -el`). Hash mismatch vs. a classmate → re-download; the instructor's hash sheet is authoritative. Tool missing → the VM image ships everything; do not install random binaries into the *analysis* VM.

## Cleanup Instructions
Delete samples and outputs from the VM; restore the `lab08-clean` snapshot; log out.

## Submission Requirements
`hashes.txt`, two analyst notes (template), entropy table, cross-check finding.

## Expected Outputs / Evidence
Notes must cite artifact lines (string output, import names) for every capability claim.

---
### Instructor Answer Key (summary)
- Sample 2 seeded: URL `http://telemetry.example-security-lab.invalid/d`, imports WSAStartup/connect/InternetOpenA → dropper; thin entropy (not packed).
- Sample 3 seeded: `Run` key string + `RegSetValueEx` import + `DDNS-domain.example-security-lab.invalid` + packed section (entropy 7.4) → persistence + C2, medium-high.
- Dynamic-must-confirm lists: (2) does it beacon? to where? payload? (3) Run-key value written? beacon interval? DDNS resolution?
- Verdict language: hypotheses with confidence, never certainty — the rubric penalizes overclaiming.

### Assessment Rubric (10 pts — check-in)
| Criterion | Points |
|---|---|
| Safe-procedure compliance (snapshot, isolation, hashes-first) | 2 |
| Notes: identifiers + evidence-cited capabilities | 4 |
| Entropy interpretation | 2 |
| Confidence calibration + dynamic-confirm list | 2 |
