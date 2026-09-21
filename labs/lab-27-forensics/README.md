# Lab 27 — Digital Forensics: Instructor-Provided Artifacts
**Core Lab 7 · Module 3/4 (L10, L27) · CLO-3 (primary), CLO-4 · Duration: 2 hours · Graded lab**

## 1. Learning Objectives
1. Apply evidence-handling discipline: hashes first, work on copies, every claim cited to an artifact.
2. Reconstruct an incident timeline from heterogeneous artifacts (auth log, capture file, file metadata).
3. Produce chain-of-custody notes and an IOC table that meets quality criteria (specific, observable, attributable).
4. Answer the three leadership questions: who, what, contained?

## 2. Prerequisites
Lectures 10 (IOCs vs TTPs, behavior chains) and 27 (timeline reconstruction from logs). Lab 12's frame-citation discipline.

## 3. Hardware/Software Requirements
- Course VM: Python 3.10+, Wireshark, text tools (`grep`, `less`).
- Instructor-provided evidence pack `evidence-pack-v2.zip` (synthetic, generated for teaching): `auth.log`, `net.pcapng`, `fs-metadata.csv`, `README-evidence.txt` (with the pack's SHA-256 for verification).
- A working directory with **enough free space for two copies of the pack**.

## 4. Installation and Setup
1. Create your evidence workspace:
   ```bash
   mkdir -p ~/lab27/{original,working}
   ```
2. Unzip the pack **into `original/` only**; record the pack hash:
   ```bash
   sha256sum evidence-pack-v2.zip | tee original/pack-hash.txt
   ```
3. Copy into `working/`; **all analysis happens on copies in `working/` — never on `original/`**.
4. Verify the pack hash matches the value in `README-evidence.txt`.
   *(Pack generation and hash recording were verified on the instructor workstation; the pack's internal content is documented in the key.)*

## 5. Ethical Authorization and Safety Notes
- The artifacts are synthetic and contain no real persons, credentials, or hosts; any resemblance is coincidental.
- Evidence discipline exists to make findings *admissible*, not just correct: the original copy must never be modified — treat it as a legal exhibit.
- Nothing in this lab touches a live system; do not "follow up" on any endpoint or identity name you see.

## 6. Step-by-Step Student Tasks
| # | Task | Method |
|---|---|---|
| 1 | Verify pack hash; note verification in your custody record | `sha256sum -c` style |
| 2 | Read `auth.log`: identify the account with failure-then-success from a new source; record timestamps | `grep`, sort |
| 3 | In `net.pcapng`: find the flow matching that account's session window; note destination, ports, first/last frames | Wireshark display filters |
| 4 | Quantify egress: total bytes to the external endpoint in the window | Conversations statistics |
| 5 | In `fs-metadata.csv`: find files created/modified inside the window; flag the largest | sort/filter |
| 6 | Build the timeline: merge events from all three sources into one chronological table with source citations (log line / frame / CSV row) | spreadsheet |
| 7 | IOC table: ≥ 5 entries, each meeting the quality criteria; one per source minimum | worksheet format |
| 8 | ATT&CK mapping: ≥ 4 behaviors with technique IDs and evidence citations | ATT&CK website |
| 9 | Chain-of-custody note: who (you), what (hashes), when (your session), how (copies only) | written |
| 10 | Answer the three leadership questions in ≤ 3 sentences each | final section |

## 7. Expected Observations
- The pack tells one coherent story: account compromise (failure-streak → success from a new source), session activity, staged file (large creation event), egress to an external endpoint, then a **failed** attempt to clear traces (log-stop event that did not succeed because the log source is remote — the L27 lesson).
- The three sources corroborate: timestamps overlap within seconds; the file-creation event precedes the egress spike.

## 8. Questions for Analysis
1. Why analyze copies? Name the two things an examiner must be able to prove about `original/` in a hearing.
2. Which single artifact would you preserve first if you could keep only one, and why — does your answer change if the logs are remote/immutable?
3. Your timeline has a gap of 90 minutes between the session and the egress. What are two innocent explanations, and what would you check next (within the pack) before hypothesizing?

## 9. Troubleshooting
- Hash mismatch on the pack → redownload; never "fix" the pack; report it to the instructor (corrupted evidence is a real event with a real procedure).
- `auth.log` timestamps in a different timezone than the capture → normalize using the offset documented in `README-evidence.txt`; state the normalization in your timeline.
- Wireshark chokes on the file size → apply a display filter *before* Follow Stream; the window is narrow by design.

## 10. Cleanup Instructions
- Keep `original/` untouched; delete `working/` after submission (hashes recorded in your report prove what you analyzed).
- Remove the pack from downloads; it is re-issued from the LMS.

## 11. Submission Requirements
- `timeline.csv` (chronological, source-cited).
- `custody.md` (hashes, copies, method).
- `iocs.csv` (≥ 5, quality-criteria column filled).
- `report.md`: behavior chain, ATT&CK mapping (≥ 4 with citations), the three leadership answers, and the gap-analysis answer.

## 12. Expected Outputs / Evidence
All four files, personally produced. The reconstructed chain must match the seeded story in ordering (compromise → staging → egress → failed cleanup) even if exact times differ by timezone normalization.

---
### Instructor Answer Key (summary — full version in `assessments/instructor-only/`)
- Seeded story: account `jsmith` — 5 auth failures from 198.51.100.23 (02:10–02:12), success 02:14; file `Q3-report-final.csv.enc` (412 MB) created 02:31 (`fs-metadata.csv` row 88); egress to 203.0.113.77:4432 totaling 412 MB (02:33–02:51, capture frames 1,140–2,410); log-stop attempt at 03:07 from the same source (`auth.log` line 214: `logger delete` denied — remote source).
- ATT&CK map (expected): T1110.001 (password guessing), T1078 (valid accounts), T1560-class (archive/stage), T1041 (exfiltration over C2 channel), T1070.02-class (clear logs — attempted, failed).
- Leadership answers: who = `jsmith` from 198.51.100.23; what = 412 MB staged file exfiltrated; contained = log source intact (remote), credential disabled, egress identified — "containment partial, evidence complete" is the expected honest verdict.
- Timeline gap: 90 min = attacker dwell (innocent: maintenance window; check: session duration and idle events in the capture).

### Assessment Rubric (20 pts)
| Criterion | Points |
|---|---|
| Custody discipline (hashes, copies, verification) | 4 |
| Timeline completeness and source citations | 5 |
| IOC quality (criteria met, not volume) | 3 |
| ATT&CK mapping with evidence | 4 |
| Leadership answers + gap analysis | 4 |
