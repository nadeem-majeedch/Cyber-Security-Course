# ⚠️ INSTRUCTOR-ONLY — Checkpoint Answer Keys (A–F)

Keys for the six module checkpoints, delivered as weekly quizzes **2, 4, 6, 10, 12, and 14** (papers in `../../student/quizzes/`). Marking guide: items 1–6 = 1 mark each unless noted; items 7–8 are the scenario items worth **2 marks each** (Checkpoint A item 7 is a +1 bonus). Checkpoints B–F have a raw maximum of **10 — record raw**; Checkpoint A has a raw maximum of **8 (incl. bonus) — record (raw ÷ 8) × 10**. Checkpoint scores are formative-weight (15% total, lowest dropped).

## Checkpoint A — Module 1 (L04) · CLO-1

1. **I (integrity)** — data was altered.
2. **Coordinated/responsible disclosure** is required by this course; full disclosure is the other route.
3. **D (information disclosure)** from STRIDE; typically applies to data flows and stores.
4. Spoofing **S** — the property violated is *authenticity*.
5. **Attack tree min-cut** = the cheapest set of AND-leaf groups (cost table answer: `steal-physical-key` OR (`bribe-custodian` AND `forge-request`) at 15 — accept equivalent readings).
6. Any two of: physical, supply chain, human/social-engineering surface. **[1 mark each]**
7. **(Bonus, +1)** Removing the unused admin API *eliminates an attack path entirely* — nothing exposed means nothing to exploit; an IDS only observes and alerts *after* an attempt, so the path still exists. Full credit requires the removal-vs-detection distinction.

## Checkpoint B — Module 2 (L08) · CLO-2

1. CWE-89 (SQL injection); CWE-78 (command injection).
2. `shell=True` passes the command through a shell → metacharacters interpret user input as code; list-form args prevent interpretation.
3. Least-privilege DB account (accept: error hygiene, WAF as secondary, input allow-listing).
4. DOM-based XSS lives only in client-side JS.
5. Token + `SameSite` (accept origin/referer check as second).
6. Sequential IDs are predictable/enumerable.
7. **(2)** Vulnerability: server-side template injection from concatenated user input — CWE-1336 (accept CWE-94/95 family with justification). Corrected pattern: pass `nickname` as a template *context variable* into a static template; never concatenate user input into template source.
8. **(2)** Fix: parameterized queries/prepared statements (1). Hardening: least-privilege DB account (accept error hygiene or input allow-listing) (0.5). STRIDE element: Tampering or Information Disclosure, accepted with a one-line justification of the injection's effect (0.5).

## Checkpoint C — Module 3 (L12) · CLO-3

1. DMARC (policy record consulted by the receiver).
2. Any two pretexts: authority, urgency, scarcity, social proof (accept familiarity).
3. Report rate (and time-to-report) beat click rate.
4. SHA-256 identifies exactly; ssdeep (fuzzy) finds near-variants.
5. Persistence: Run key, scheduled task (accept service install).
6. Fake-net prevents real C2 contact / evidence contamination and contains the sample.
7. **(2)** Order: (1) hash + threat-intel check, (2) file-type/header/metadata review, (3) macro/script + strings/imports static extraction — any defensible static-first order (1). Detonation isolation: snapshot/revert VM, host-only or fake-net networking, shared folders off (any one named control, per the course contract) (1).
8. **(2)** Order: isolate affected segments (keep systems powered), activate the IR plan and comms channel, preserve evidence (logs, samples, memory) while preparing the immutable/offline restore path (1). Not improvised: the ransom-payment decision — it belongs to legal/insurer/executive (accept public-disclosure decision) (1).

## Checkpoint D — Module 5 (L20) · CLO-5

1. ECB leaks plaintext patterns.
2. CBC needs a random IV so equal plaintext blocks encrypt differently.
3. GCM gives authenticated encryption (integrity tag with confidentiality).
4. A certificate binds a public key to an identity/name.
5. TLS 1.3: forward secrecy by default; fewer rounds/1-RTT; deprecated weak suites (any two).
6. CWE-330 = insufficient randomness/entropy.
7. **(2)** Flaws (any two): MD5 is broken/unsuitable for security tokens; the token space is guessable (small `user_id` + fixed secret → brute-forceable, no per-token entropy) (1). Corrected: random ≥ 128-bit token from a CSPRNG stored server-side (hashed), or an HMAC-signed token over a random ID with expiry and constant-time comparison (1).
8. **(2)** Failure: key and data co-located — one compromise steals both (no independent protection boundary) (1). Corrected: external key management (KMS/HSM) with envelope encryption and a key lifecycle independent of the data store (1).

## Checkpoint E — Module 6 (L24) · CLO-6

1. At 0.1% prevalence, a degenerate "always benign" classifier scores 99.9% accuracy while catching nothing.
2. Contamination parameter sets the expected anomaly proportion (isolation forest).
3. Features e.g.: failed-login streak, new source country, off-hours ratio (any two defensible).
4. PR-AUC focuses on the positive (attack) class; ROC inflates under heavy imbalance.
5. Random splitting leaks near-duplicate/temporal samples into train and test.
6. Rule rollout: shadow → alert → block.
7. **(2)** Features (any two, window stated): failed-login velocity per (user, source); distinct-username count per source; off-hours/new-device deviation (0.5 each, max 1). Precision matters: false positives lock out users and erode analyst trust (0.5). Adversarial adaptation: slow, distributed attempts across sources/hours — requires aggregate/velocity features, not per-attempt rules (0.5). *(0.5 reserve for coherent extras.)*
8. **(2)** Mitigations (any two, one tradeoff required): adversarial training on expected perturbation families — costs retraining cycles, biased to known families; feature hardening toward structural/behavioral signals — loses some lexical sensitivity; input normalization + drift monitoring — maintenance overhead (2).

## Checkpoint F — Module 7 (L28) · CLO-7

1. PaaS runtime patching = provider ("of the cloud").
2. Wildcard-on-wildcard = grant every action on every resource — appears via copy-paste/console defaults.
3. Roles: short-lived, no static keys, auditable assumption (any two).
4. Control-plane log answers "who deleted the bucket."
5. Drift = deployed state ≠ declared IaC state; prevented by PR-only changes + policy-as-code scans (accept console-lock + drift detection).
6. Pseudonymized data is still personal data (re-identifiable); backups are typically the first "delete me" blocker (logs second).
7. **(2)** Patching: PaaS runtime = provider ("of the cloud") (0.5). IAM/keys/audit logging = customer ("in the cloud") (0.5). Genuinely shared: encryption-key management — the provider operates the KMS service, the customer owns key policy and usage (1).
8. **(2)** Rights verified alongside erasure: identity verification and access/portability (accept rectification or objection) (1). Blockers: backups (retained/restorable copies) and log/telemetry stores (retention duties) (1).

## Marking and moderation notes

- Accept any equivalent wording that demonstrates the concept; do not require verbatim matches.
- Items marked **[1 mark each]** in A are the only multi-part ones; all checkpoints total 6–10 marks — record /10 for comparability.
- Common wrong answers to watch: students conflate authentication vs. authorization (B3), salt vs. pepper (D6 if asked), ROC vs. PR (E4), pseudonymization vs. anonymization (F6). Use these as whole-class feedback items, not just marks.
- See the relevant teaching guides for the "what the wrong answers teach" discussion hooks.
