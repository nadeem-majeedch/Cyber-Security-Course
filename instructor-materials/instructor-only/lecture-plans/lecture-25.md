# Lecture 25 — Cloud Security I: Shared Responsibility and IAM
**Module M7 · Week 13, Session 1 · 120 min · CLO-7 (primary)**

## Learning Objectives
1. Allocate security duties across IaaS/PaaS/SaaS using the shared-responsibility model, and name the classic failures at each boundary.
2. Design least-privilege IAM: identities, roles/policies, federation basics, and the dangerous defaults (wildcards, long-lived keys).
3. Analyze a public misconfiguration incident (exposed bucket / over-broad role) end-to-end.
4. Apply the policy-audit loop: evaluate an IAM policy set, find privilege escalations.

## Key Concepts
- Responsibility matrix by service model; "security OF the cloud vs. IN the cloud"
- IAM primitives: users, roles, policies (identity-based vs. resource-based), federation/SSO, service accounts
- Privilege-escalation paths: policy chains, role assumption, wildcard actions/resources; admin-by-default anti-pattern
- Secrets in cloud context: short-lived credentials vs. static access keys (ties to L19)
- Misconfiguration as the top cloud failure class (public post-mortems consistently show it)

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–10 | M7 hook: "the data center didn't get breached — a policy was" — show a famous exposed-bucket post-mortem headline set | Hook |
| 10–30 | Responsibility matrix builder: students fill the matrix for a 3-tier app on IaaS vs. PaaS; boundary failures highlighted | Interactive table |
| 30–52 | IAM workshop: policy JSON anatomy; instructor writes a least-privilege read policy live, then a broken wildcard version; class diffs the risk | Live demo |
| 52–60 | Break | — |
| 60–105 | **Lab block (Lab 23):** course-cloud sandbox — given a pre-built org with 6 identities and 10 policies: (a) map who can do what, (b) find the 3 escalation paths, (c) rewrite the two worst policies, (d) verify least privilege with a can-I-do-X test script | Hands-on |
| 105–115 | Incident replay: the cited misconfiguration case mapped to today's concepts (which boundary failed, which audit would have caught it) | Case discussion |
| 115–120 | Exit ticket; preview L26 (containers) | Q&A |

## Examples
- **CS track:** CI service role can also write to the prod bucket — pipeline compromise becomes data compromise; students write the narrowed policy + the audit test.
- **DS track:** analytics team's read-only warehouse role shares a wildcard bucket policy — PII in one prefix leaks; students design prefix-scoped roles and data-classification tags.

## Discussion Questions
1. Why does "the provider is responsible for security" comfort executives and mislead engineers?
2. Federated SSO reduces password sprawl but concentrates blast radius — design the trade-off for a university.
3. Who audits the auditors' IAM policies? Propose a cadence and tooling sketch.

## Student Activity
Matrix-building; policy diff exercises; sandbox audit with a findings report; escalation-path hunt.

## Problem-Solving Scenario
> A data-science platform in the cloud: notebook service role has `s3:*` on the org bucket; one prefix holds raw PII; a contractor account hasn't rotated keys in 2 years. Produce: the escalation map (3 paths), the rewritten policies with justification, the rotation plan, and the detection rule for "role assumed from an unusual source."

## Summary
Cloud security failures are mostly configuration and identity failures: the platform holds, we configure. Least privilege + auditable policy + short-lived credentials is the discipline. L26 hardens the compute layer itself.

## Formative Assessment
1. In PaaS, who patches the runtime — provider or you?
2. What does `"Action":"*"` on `"Resource":"*"` mean literally, and why does it appear anyway?
3. Name two advantages of roles over static keys.

## Required Resources
- `labs/lab-23-cloud-iam/` sandbox org + audit script
- NIST SP 800-145; provider IAM documentation (selected pages)
- Cited misconfiguration post-mortem (`case-studies/`)
- CLO mapping: **CLO-7** (objectives 1–4).
