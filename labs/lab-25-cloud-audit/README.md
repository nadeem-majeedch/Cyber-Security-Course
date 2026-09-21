# Lab 25 — Cloud Audit-Trail Investigation
**Enrichment · Module 7 (L27) · CLO-7 · Duration: 2 hours · Check-in lab**

## Learning Objectives
1. Decode control-plane audit events (principal, action, resource, source, MFA context).
2. Reconstruct an incident timeline from the provided audit corpus.
3. Answer the three leadership questions (who / what / contained) with evidence.
4. Write the IaC fix and two detection rules (role anomaly, policy mutation).

## Prerequisites
Lecture 27; Lab 23's IAM vocabulary (roles, assume, policies).

## Hardware/Software Requirements
Course VM: spreadsheet or pandas; the audit corpus `audit-corpus-v2.csv` (synthetic, schema header) + the IaC template `starter/bucket-template.yaml`.

## Installation and Setup
```bash
python - <<'EOF'
import pandas as pd
df = pd.read_csv("audit-corpus-v2.csv")
print(df.shape, df.columns.tolist())
EOF
```

## Ethical Authorization and Safety Notes
- The corpus is synthetic; "identities" are fictional. No cloud account is accessed in this lab — everything is file-based analysis.
- The log-stop *attempt* in the corpus is a scenario element (a denied event), not something to reproduce anywhere.

## Step-by-Step Student Tasks
1. Decode drill: for five provided events, write the plain-sentence reading (who did what, from where, with what auth context).
2. Timeline: filter the corpus to the incident window; build the chronological table with row citations.
3. Identity chain: what did the CI-runner identity become, and when? (AssumeRole events.)
4. Data-plane leg: quantify the anomalous reads (bytes, object count, window).
5. The denied event: find the log-stop attempt; state which control made it fail and why that control is architectural.
6. Leadership answers: who / what / contained — ≤ 3 sentences each.
7. Fixes: the IaC template has the public-bucket flaw — fix it; write the two detection rules (role assumed from unusual source; bucket-policy mutation) in the course rule format.

## Expected Observations
- Chain: CI-runner identity → AssumeRole (analytics role) → bucket-policy mutated public → 200 GB data-plane reads → denied logging change (cross-account write-once).
- The denied event is the corpus's teachable artifact: the logging-account pattern (L27) is why the evidence survived.

## Questions for Analysis
1. Which single event in the corpus is the *root cause* vs. symptom — and would your detection rules have fired on the root cause, the symptom, or both?
2. The logging change was denied. What configuration would have made it *succeed*, and what would that have cost the investigation?

## Troubleshooting
Corpus too large to eyeball → filter by the incident window first (documented in the header note); pivot on `eventSource`. Timeline rows out of order → normalize timestamps (the corpus is UTC; your spreadsheet may localize). Two roles with similar names → the assume-event's `roleArn` field is authoritative.

## Cleanup Instructions
Delete the corpus copy; nothing was executed against any cloud service.

## Submission Requirements
Five decoded events, timeline table (row-cited), identity-chain answer, data-plane quantification, leadership answers, fixed IaC template, two detection rules.

## Expected Outputs / Evidence
Every timeline row cites its corpus row index; the denied event must be in the timeline.

---
### Instructor Answer Key (summary)
- Seeded chain (row ranges in the key's full version): 02:01 AssumeRole (ci-runner → analytics, unusual source IP) → 02:03 PutBucketPolicy (public) → 02:05–02:51 GetObject × 1,412 (200 GB) → 03:07 StopLogging **denied** (cross-account log protection).
- Root cause: the AssumeRole trust condition (missing source check) — symptom: public policy. Rules should fire on both.
- IaC fix: remove the public-read statement + add bucket-public-access block; detection rules (model): "AssumeRole where source != known CI CIDR → alert"; "PutBucketPolicy where statement contains Principal:'*' → high-severity alert."
- Leadership: who = CI-runner identity via role assumption; what = 200 GB from the dataset prefix; contained = logging intact, policy reverted, role trust tightened → "evidence complete, containment partial."

### Assessment Rubric (10 pts — check-in)
| Criterion | Points |
|---|---|
| Timeline completeness with row citations | 3 |
| Identity chain + data-plane quantification | 2 |
| Leadership answers | 2 |
| IaC fix + two detection rules | 3 |
