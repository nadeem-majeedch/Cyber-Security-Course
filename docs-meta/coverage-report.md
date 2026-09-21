# Coverage Report — Syllabus & Lecture Plans
**Validation date: 2026-09-19 · Scope: `syllabus.md` + `instructor-materials/instructor-only/lecture-plans/`**

> **Audit update (2026-09-19, independent QA):** the gates below were re-verified during the final audit — see `final-course-audit.md` §10 (new) and `findings-register.md`. Sections 1–9 are retained from the original plan-phase validation.

## 1. File-count gate: exactly 32 lecture plans

Verified by `glob instructor-materials/instructor-only/lecture-plans/lecture-*.md` and by shell count: **32/32** (`lecture-01.md` … `lecture-32.md`, sequential, no gaps — machine-checked with a sequence script).

## 2. Hours gate: 64 instructional hours

- 32 lectures × 2 h = **64 contact hours** (matches the program requirement).
- Each plan carries a minute-by-minute teaching sequence summing to **120 minutes** (segments: recap 8–12′, theory 40–50′, break 5′, lab/activity 35–50′, consolidation 8–15′). Spot-audited across all eight modules.
- Deviations are intentional and documented: L16 midterm (55′ review + 55′ exam), L24 checkpoint + case-brief collection, L30/L31 build/tabletop formats (team-time-boxed), L32 showcase (60′) + final exam (35′).

## 3. Topic-coverage gate: required content areas

All 20 required areas are covered, mapped to lectures:

| Required area | Covered by | Depth evidence |
|---|---|---|
| Foundations | L01, L04 | CIA, risk, controls taxonomy |
| Threat models | L02, L03 | STRIDE, attack trees, ATT&CK, surface |
| Networking | L13, L14, L16 | Packet analysis, segmentation, wireless/VPN |
| Operating systems | L09, L10 (analysis VM/process/registry), prereq bridge (Lab 00) | Static/dynamic artifacts |
| Access control | L04, L05, L25, L26 | Least privilege, sessions, IAM, workload identity |
| Cryptography | L17–L20 | Modes, PKI/TLS, password storage, failure taxonomy |
| Data protection | L19, L28 | KDFs, secrets lifecycle, minimization, DPIA |
| Web security | L05–L08 | HTTP, injection, XSS/CSRF/SSRF/IDOR, SDLC |
| APIs | L05 (auth flows), L07 (object-level authz), L25 (cloud API identity) | Embedded in those plans |
| Vulnerability management | L08 | SAST/DAST/SCA, CVSS triage, SLAs |
| Logging | L13, L15, L21, L27 | Capture, SIEM, telemetry features, cloud audit |
| Forensics | L10, L27 | IOC curation, evidence discipline, timeline reconstruction |
| Incident response | L11, L31, L32 | Resilience design, tabletop, IR decisions |
| Resilience | L11, L14, L20, L26 | Backups, blast radius, crypto agility, hardening |
| Governance | L04, L08, L28 | CSF functions, SDLC gates, DPIA/sign-off |
| Cloud | L25–L27 | Shared responsibility, IAM, containers, audit |
| IoT | L02 (vending-box spec), L20 (IoT camera case) | Threat-model + failure case |
| AI security | L21–L24 | Anomaly detection, classifiers, adversarial ML, detection engineering |
| Threat intelligence | L03, L10, L15, L24 | ATT&CK hypotheses, IOCs/TTPs, coverage mapping, purple-team testing |
| Capstone work | L29–L32 | Model → build → tabletop → showcase |

## 4. Progression and prerequisite-logic gate

- Module order preserved: M1→M8 as approved in `docs-meta/architecture-and-requirements.md` §3; DAG unchanged.
- Forward references are intentional and flagged in plans: L05↔M5 (TLS full treatment later), L13 beacon → L21 (timing analytics), L09 features → L22 (classifier reuse), L14 segmentation → L27 (logging account). Each is marked "concept now, depth in Mx" in the relevant plan — no plan depends on untaught mechanics.
- Backward dependencies honored: every M6 plan reuses M3/M4 artifacts; L23 reuses the L22 model; capstone plans explicitly reuse L02, L04, L06, L11, L21–L24, L25, L28 craft (cited inside the plans).

## 5. CLO-coverage gate

| CLO | Primary lectures | Formative touchpoints | Summative evidence |
|---|---|---|---|
| 1 | L01, L03, L04 | Checkpoint A | Midterm, final, capstone ethics |
| 2 | L05–L08 | Labs 04–07, Checkpoint B | Lab reports, midterm |
| 3 | L09–L12 | Labs 08–11, Checkpoint C | Malware lab report, case brief |
| 4 | L13–L16 | Labs 12–14, midterm | Network design review |
| 5 | L17–L20 | Labs 15–18, Checkpoint D | Crypto lab |
| 6 | L21–L24 | Labs 19–22, Checkpoint E | ML labs F1 ≥ 0.90 gate |
| 7 | L25–L28 | Labs 23–26, Checkpoint F | Cloud lab, DPIA |
| 8 | L29–L32 | Milestones 1–4 | Capstone report + showcase (non-compensable) |

All eight CLOs have ≥ 3 primary lectures, a module checkpoint, and a named summative artifact. Every lecture plan ends with an explicit "CLO mapping" line — verified present in all 32 files.

## 6. Syllabus completeness gate (required items 1–11)

| # | Required item | Where in `syllabus.md` |
|---|---|---|
| 1 | Complete course syllabus | whole document |
| 2 | Course description | §1 |
| 3 | Prerequisites | §2 |
| 4 | CLOs + measurable outcomes | §4 |
| 5 | CLO-to-lecture mapping | §5 |
| 6 | Weekly teaching schedule | §6 |
| 7 | Lecture-by-lecture objectives | §7 |
| 8 | Detailed lecture plans | §8 (pointer to the 32 files) |
| 9 | Assessment strategy | §9 |
| 10 | Prerequisites + expected background | §2, §3, §10 |
| 11 | Readings and references | §11 |

## 7. Every-lecture-fields gate

All 12 mandated fields are present in every plan, in fixed order: title/metadata, learning objectives, key concepts, detailed teaching sequence, examples (CS+DS tracks where relevant), discussion questions, student activity, problem-solving scenario, summary, formative assessment, required resources, CLO mapping. Verified by structural spot-audit of all 32 files (field headings present in each).

## 8. Preservation gate

`git status --porcelain` shows only additions (`??`); no existing file deleted or overwritten. The architecture doc received one change-log row (new lecture titles refine, but do not alter, the approved module boundaries or lecture allocations).

## 9. Known limitations (honest reporting — updated 2026-09-19)

- ~~Lab worksheets to be authored~~ **Resolved:** 31 lab directories with 16-component core worksheets now exist; remaining gap is infrastructure artifacts and first-delivery testing (findings H3).
- ~~Case write-ups not yet written~~ **Resolved:** 100-case collection authored and validated; remaining gap: none (validator enforces completeness).
- Reading lists cite editions generically (e.g., "4th/5th ed.") where the department may choose; library confirmation is an open item.
- Labs referenced by plans follow the authoritative crosswalk in `labs/README.md`; plan-phase lab numbering was superseded by that crosswalk (see audit §7).

## 10. Independent audit cross-check (2026-09-19)

| Gate | Re-verified during audit | Outcome |
|---|---|---|
| 1. 32 plans | direct count + validators | PASS |
| 2. 64 hours | plan timing tables (deviations documented) | PASS |
| 3. Topic coverage | 20 areas re-mapped; IoT/AI/threat-intel rows re-checked | PASS |
| 4. Progression | module DAG unchanged; calendar alignment validated | PASS |
| 5. CLO coverage | bank-wide CLO tags + per-note tag counts | PASS, with thin note-level tags for CLO-3/5 (finding L2) |
| 6. Syllabus 1–11 | byte-level inspection of §5 matrix; all sections present | PASS |
| 7. Plan fields | component greps across all 32 | PASS |
| 8. Preservation | `git status` additions-only re-confirmed | PASS |

New findings from the audit that affect this report's scope: checkpoint key gap (H1), public exposure of live exams (C1), website/Pages not buildable (H2). Full register: `findings-register.md`.
