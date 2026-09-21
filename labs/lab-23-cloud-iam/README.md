# Lab 23 — Cloud IAM Least-Privilege Audit
**Core Lab 5 (vulnerability assessment, cloud variant) · Module 7 (L25) · CLO-7 · Duration: 2 hours · Graded lab**

## 1. Learning Objectives
1. Enumerate identities, roles, and policies in the **course cloud sandbox** and map who-can-do-what.
2. Find privilege-escalation paths with the audit question "what can this identity become?"
3. Rewrite over-broad policies to least privilege and *verify* with a can-I-do-X test script.
4. Grade findings by exposure and produce a remediation plan.

## 2. Prerequisites
Lecture 25 (shared responsibility, IAM primitives, escalation paths). No prior cloud experience assumed.

## 3. Hardware/Software Requirements
- Course cloud sandbox account (instructor-issued, isolated, non-production; credentials from the LMS).
- Browser (sandbox console) + course VM with Python 3.10+ and the provider CLI configured for the sandbox profile only.
- `starter/audit-check.py` (can-I-do-X verifier) and `starter/policies-to-fix.jsonl`.

## 4. Installation and Setup
1. Configure the CLI with the sandbox profile from the LMS:
   ```bash
   aws configure --profile course-sandbox   # keys from LMS
   aws sts get-caller-identity --profile course-sandbox
   ```
2. Confirm you are in the **sandbox account** (account ID must match the LMS value) before any command.
3. Run the verifier once to confirm it works:
   ```bash
   python starter/audit-check.py --profile course-sandbox --identity course-analytics --action s3:ListBucket
   ```
   *(Setup shape tested on the instructor workstation with a fresh sandbox profile; the sandbox's identity/policy set is seeded per section and documented in the key.)*

## 5. Ethical Authorization and Safety Notes
- The sandbox is the *only* authorized target: an instructor-issued, isolated account with no real data and no billing exposure. It is deleted after the term.
- Do **not** attempt to use these credentials against any other account, region outside the sandbox allow-list, or any personal cloud account.
- This is an *audit* lab: you find and fix misconfigurations in your own sandbox; nothing here teaches or practices unauthorized access.

## 6. Step-by-Step Student Tasks
| # | Task | Notes |
|---|---|---|
| 1 | Inventory: list the sandbox's 6 identities and 10 policies (console or CLI); record names/types | worksheet table |
| 2 | Read `policies-to-fix.jsonl` — the three policies with planted over-breadth | seeded set |
| 3 | Map permissions: for each identity, list attached policies and their effective actions/resources | effective-permission view |
| 4 | **Escalation hunt:** for each identity answer "what can it become?" (assumable roles? modifiable policies? wildcard reads?) | worksheet graph |
| 5 | Identify the data path: which identity can read the `pii-raw/` prefix, and via which policy | policy JSON |
| 6 | Rewrite the two worst policies to least privilege (prefix- and action-scoped) | starter templates |
| 7 | **Verify:** run `audit-check.py` for each rewritten pair (allowed action still allowed; forbidden now denied) | script output |
| 8 | Third finding: the contractor's static key age (simulated metadata in the seeded set); write the rotation plan | worksheet |
| 9 | Grade findings: severity × exploitability × exposure (sandbox context — say so) | triage table |
| 10 | Detection rule: write the "role assumed from unusual source" rule in the worksheet format | L25 format |

## 7. Expected Observations
- The `course-analytics` identity's policy grants `s3:*` on the org bucket (planted); the `pii-raw/` prefix is readable through it.
- The `ci-runner` identity can assume the `deploy-role`, which can write the analytics role's policy — the escalation chain (planted).
- After rewriting, `audit-check.py` shows the allowed read of `analytics-out/` still permitted and the read of `pii-raw/` denied.
- Key-age metadata flags a 2-year-old static key for the contractor identity.

## 8. Questions for Analysis
1. The wildcard policy was "convenient" for the analytics team. State the exact incident that convenience makes possible, in one sentence.
2. Your rewrite broke nothing in the can-I-do-X checks for allowed actions — but what legitimate future action might it break, and how do you design for that without re-widening the policy?
3. Why is the escalation chain (identity → role → policy-write) worse than the data-read finding alone, even though no data was touched?

## 9. Troubleshooting
- `AccessDenied` on inventory commands → you are using the audit profile, not the admin-sandbox profile; the LMS shows both — inventory needs the latter.
- Verifier denies an action you intended to keep → your rewrite over-scoped; widen the action list, not the resource wildcard.
- CLI version errors → `aws --version` ≥ 2.x required (course image ships 2.x).

## 10. Cleanup Instructions
- Remove the sandbox profile credentials from your VM (`aws configure --profile course-sandbox` then clear, or delete `~/.aws/credentials` entry) — sandbox keys never persist past the session.
- No resources were created by you (read-only audit + policy rewrites in the seeded set); the instructor resets the sandbox per section.

## 11. Submission Requirements
- `audit-report.md`: inventory table, escalation graph, three findings (evidence: policy JSON excerpts), the rewrites with before/after verifier output, triage, detection rule.
- Answers to the three analysis questions.

## 12. Expected Outputs / Evidence
Report + verifier transcripts. The before/after verifier pair per rewritten policy is the core evidence — a rewrite without verification is incomplete.

---
### Instructor Answer Key (summary — full version in `assessments/instructor-only/`)
- Planted findings: (1) `policy-analytics-wild`: `s3:*` on `org-datalake` bucket incl. `pii-raw/` (CWE-732 class); (2) `policy-ci-broad`: `ci-runner` may assume `deploy-role` which may write `policy-analytics-*` (escalation chain); (3) contractor static key age = 731 days (rotation policy breach).
- Rewrite (model): `s3:ListBucket/GetObject` on `org-datalake/analytics-out/*` only; deny on `pii-raw/*`; verify pairs: ListBucket analytics-out → allow; GetObject pii-raw/x → deny.
- Escalation chain answer: identity → assumable role → policy-write = persistent privilege escalation without touching data; detect via role-assumption + policy-mutation alerts (L27's control-plane logging).
- Exposure grading: all findings are sandbox-scoped; severity reflects *pattern* if deployed to production — "high-pattern/low-current-exposure" framing expected.

### Assessment Rubric (20 pts)
| Criterion | Points |
|---|---|
| Inventory + permission mapping completeness | 4 |
| Escalation hunt (all three planted paths found) | 5 |
| Rewrites with before/after verifier evidence | 5 |
| Triage + rotation plan + detection rule | 4 |
| Analysis answers | 2 |
