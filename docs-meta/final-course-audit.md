# Final Course Audit — Area-by-Area Review
**Independent QA · Date: 2026-09-19 · Method: direct file inspection + executed validators + representative tests. Every claim below is verified [V] or explicitly marked not-run [N]. Findings referenced by ID from `findings-register.md`.**

## 1. Course structure — PASS with notes [V]

32 lecture plans, 32 student notes, 32 teaching guides, 32 slide decks, 31 lab directories (14-lab program: 8 core + 6 enrichment per the consolidation decision), 100 cases (20/25/30/25), 15 quiz papers + 2 specimen exams, calendar tooling. Eight module directories; student/instructor tiers separated; numbering gap-free (validators + direct count). Structure matches the approved architecture; the only structural anomaly is the website tree (H2).

## 2. Syllabus — PASS [V]

All 11 mandated sections present (description, prerequisites, background, CLOs with Bloom + measurable outcomes, CLO→lecture matrix, 16-week schedule, per-lecture objectives, assessment weights, readings). §5 matrix inspected at byte level — primary ●/supporting ○ dots intact and consistent with module boundaries. Weights sum to 100% (30+15+15+10+20+10). Prescribed instruments exist in both tiers (audit §9/§19).

## 3. CLO mapping — PASS with notes [V]

Syllabus matrix complete: every CLO has ≥ 3 primary lectures, a checkpoint, and a summative artifact. Question bank covers CLO-1..8 across Understand→Create (validator-checked). Notes tag CLOs thinly for CLO-3/CLO-5 (4 notes each vs 5–7 for others) — L2. Capstone is the sole CLO-8 primary venue in the final third, matching the matrix.

## 4. Lecture plans (32) — PASS [V]

All 32 contain the 12 mandated components in fixed order (title/metadata, objectives, key concepts, 120-minute teaching sequence, worked examples, discussion questions, student activity, problem-solving scenario, summary, formative assessment, resources, CLO mapping) — validated by component greps and spot reads (L03, L13, L23). Timing tables sum to 120 min with documented deviations (L16 midterm, L32 showcase).

## 5. Teaching notes (32) — PASS with notes [V]

All 10 required components present (objectives, concepts, diagram with text description, examples, misconceptions, activities, discussion questions, problem-solving exercise, summary, exit ticket, references); 0 files missing any component; 0 without references or CLO tags. One technical error found: lecture-16 "Dragonslayer-class" should be **Dragonblood** (M4). lecture-32 lacks DS-track content (L1).

## 6. Instructor manual — PASS [V]

`instructor-manual.md` present with package map, standing lab-delivery rules, facilitation patterns, recurring difficulty classes, accessibility provisions, integrity policy, safety rules; the earlier stray non-English typo was fixed at authoring time (verified in current text). Consistent with guides and checkpoint keys.

## 7. Labs — CONDITIONAL PASS [V]

All 8 core worksheets carry the 16 required components (verified 8/8 per component after correcting auditor regex false negatives — recorded honestly in I7). Ethics/authorization notes present in all 31 labs; keys/rubrics instructor-side. **Conditional because** infrastructure artifacts are absent and instructions are untested beyond Lab 15's starter (H3): the lab program is specified, not yet delivered.

## 8. Case studies — PASS [V]

100 cases, validator-enforced completeness (9 student fields + 6 instructor components per case), all labeled simulated, no fictional incident cited as real, difficulty progression 1→4 with open-ended L4 cases, DS-specific cases at every level, INDEX cross-references valid (41 deck→INDEX IDs verified; the single extra CS-062 mention is an intentional cross-reference inside CS-083). Solutions instructor-side.

## 9. Assessments — CONDITIONAL PASS [V]

120-item bank with validated keys, Bloom, CLO, difficulty tags; duplicate-avoidance rule; 15 quiz papers + 2 specimen exams questions-only (leakage scan clean); A/B variant tables. **Conditional because:** H1 (checkpoint keys don't cover paper items 7–8) and C1 (live papers public). Mark totals reconcile (validator); specimen/live item separation enforced.

## 10. Slides & speaker notes — CONDITIONAL PASS [V]

35 decks + template validated: objectives, diagrams with text descriptions, CS+DS examples, lab-demo slides with MVO, case slides with INDEX-verified IDs, notes on every content slide, accessibility theme (contrast computed: 18.9/11.2/10.3/7.5:1 — all pass AA). **Conditional:** rendering pipeline never executed (M1, marp absent).

## 11. Website build — FAIL [V]

Not buildable: no index, no content mirror, anomalous locked `index-template.md` **directory**, empty module dirs (7 of 8). Documented Stage-2 deferral (I6) is consistent with the roadmap, but the tree as it stands is defective (H2).

## 12. GitHub Pages workflow — NOT RUN / ABSENT [V]

No `.github/workflows/pages.yml` exists; documented as deliberate Stage-2 deferral so the site never deploys empty (I6). Workflow requirements are specified in the architecture doc. Nothing to execute; when built, it must exclude `calendar/generated/instructor-calendar.md` and all instructor-only tiers (see M2).

## 13. Internal links — PASS with notes [V]

Repo convention uses backtick paths, not Markdown links: 0 internal md links exist outside the generated calendars (verified twice, including a checker-bug investigation). The calendar generator's own link validator resolves all generated links. Consequence: authored docs are not click-navigable (M5); broken-link risk in authored docs is correspondingly zero but unverifiable by link checkers — path accuracy spot-checked manually (README map, roadmap pointers, syllabus references).

## 14. Technical accuracy — PASS with notes [V]

Spot-verified content: CSRF/`SameSite` mechanics (L07), WPA3-SAE vs WPA2-PSK (L16), GCM nonce-reuse catastrophic failure (L17), argon2id memory-hardness (~100 ms + GB-scale per guess, GPU-unfriendly) (L19), SSRF metadata `169.254.169.254` (L07), TLS 1.3 ephemeral-key derivation (L18). `openssl enc` AEAD limitation reproduced (I5). Lab 15 starter runs (sha256/hmac paths, graceful degradation on aead/kdf). One named-research error (M4). No fabricated statistics found in spot reads; case data is scenario-internal and labeled.

## 15. Ethical & safety compliance — PASS [V]

Standing responsible-use rules in labs README and every lab worksheet (31/31 authorization notes); sandbox-only targets; prohibited-pattern scan hits are ATT&CK terminology in defensive context (I4); fix-verify pairing is enforced across worksheets; no credential-theft, destructive-payload, persistence, or unauthorized-access instructions found in scans or reads. Authoring environment contains none of the offense tooling the labs would need (relevant to H3, not a content defect).

## 16. Accessibility & usability — PASS with notes [V]

Theme contrast all ≥ 7.5:1 (AA pass, computed); diagrams carry text descriptions; large-type baseline in theme.css; calendar HTML print CSS; no color-only meaning found in spot reads. Usability: M5 (non-clickable references) and H2 (website) are the open usability gaps.

## 17. References — PASS with notes [V]

All 32 notes carry reference lists (0 missing); sources are real and attributable (NIST SP 800 series, OWASP cheat sheets, RFC 8446, Sikorski & Honig, Boneh & Shoup, Wi-Fi Alliance, GDPR articles, MITRE ATT&CK/ATLAS). The M4 error adds a missing citation to a named research result. Recency rule (≤ 5 years, classics exempt) documented in the syllabus; per-term vendor-guidance checks flagged in plans.

## 18. Data Science relevance — PASS with notes [V]

DS-specific content verified: Module 6 (analytics, classification, adversarial ML), DS-tracked examples in 31/32 notes (L1 exception), DS-specific cases at every level (073–075, 092–094), DS-flavored bank items and calendar entries, dual-track capstone scopes (L29). Both-cohort requirement met with the L32 gap only.

## 19. Assessment coverage — CONDITIONAL PASS [V]

16 weekly units mapped to weeks and sources (question-bank README); all eight CLOs covered bank-wide across Bloom levels; best-6-of-8 lab grading, checkpoint lowest-drop, capstone floor rules all present and consistent syllabus↔rubrics↔calendar. **Conditional:** H1 key gap; C1 exposure; M6 capstone mark-split ambiguity.

## 20. Course calendar — PASS [V]

Generator + outputs verified: 16 weeks, 32 dated sessions (Mon/Thu), no gaps, live-title verification at build time, lab/assessment/case alignment checks, all generated links resolve, configurable start date (re-run with 2027-01-04 verified), validate-only mode, JSON for LMS. Documentation complete (`calendar/README.md`). Governance note M2 (instructor view location).

## Verdict

The **content package is complete and of high quality** — every teaching artifact exists in both tiers and passes structural validation. The package is **not delivery-ready**: C1 (public exams) is disqualifying for real delivery, H1 blocks consistent marking, and H2/H3 mean the website and lab infrastructure do not exist yet. All findings carry remediations in `findings-register.md`.
