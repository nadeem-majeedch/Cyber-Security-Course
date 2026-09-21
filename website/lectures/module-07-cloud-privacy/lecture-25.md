# Lecture 25 — Cloud Security I: Shared Responsibility and IAM
**Module 7 · Week 13, Session 1 · 2 hours · CLO-7**

## Learning Objectives
1. Allocate security duties across IaaS/PaaS/SaaS using the shared-responsibility model.
2. Design least-privilege IAM: identities, roles/policies, federation; recognize dangerous defaults.
3. Analyze a public misconfiguration incident end-to-end.
4. Audit a policy set for privilege-escalation paths.

## Key Concepts and Definitions

**Shared responsibility:** the provider secures what is *theirs* (facilities, hardware, hypervisor — "security **of** the cloud"); you secure what is *yours* (data, identities, configuration — "security **in** the cloud"). The boundary moves with the service model:

| | IaaS | PaaS | SaaS |
|---|---|---|---|
| Provider | Facilities, hardware, virtualization | + OS/runtime patching | + application |
| You | OS, config, data, identities | Data, config, identities | Data, identities, tenant settings |

**The empirical pattern:** public post-mortems consistently show cloud incidents are **configuration and identity failures** (exposed storage, over-broad roles), not provider-side breaks — hence this module's emphasis.

**IAM primitives:** **users** (human/machine identities), **roles** (assumable permission sets — prefer over long-lived keys), **policies** (JSON allow/deny statements; identity-based vs resource-based), **federation/SSO** (your IdP vouches; MFA inherits). Wildcards on wildcard (`Action:"*"`, `Resource:"*"`) grant everything — it appears via copy-paste and console defaults, not malice.

**Privilege-escalation paths (the audit skill):** policy chains that let identity A assume role B; service roles that can modify their own permissions; wildcard reads on buckets that contain credentials. Audit question per identity: *what can this become?*

**Short-lived credentials:** roles/session tokens beat static access keys (which never expire and leak — L19's secrets thread lands here).

## Conceptual Diagram

```text
         ┌──────────────── provider: of the cloud ───────────────┐
layers:  facilities · hardware · hypervisor · [OS/runtime · app]
                        ────────── boundary moves ──────────
         └──────────────── you: in the cloud ───────────────────┘
           identities · policies · configuration · DATA (always yours)

escalation map:  user ──assume──► role ──can-modify──► own policy ──► admin
audit question: "what can this identity BECOME?"
```

## Realistic Examples

- **CS track:** a CI service role that can also write to the production bucket: pipeline compromise becomes data compromise; the fix is a narrowed policy (prefix- and action-scoped) plus an audit test ("can-I-do-X" script).
- **DS track:** an analytics read-only role sharing a wildcard bucket policy with a prefix holding raw PII: fix with prefix-scoped roles and data-classification tags — classification *drives* policy granularity.

## Common Misconceptions

| Misconception | Correction |
|---|---|
| "The provider is responsible for security" | For *their* layers only; most public cloud incidents are customer-side configuration. |
| "MFA on the root account is enough" | Identity design is least privilege everywhere; root is one account among many. |
| "Policies are static once approved" | They drift with the org; periodic audit + policy-as-code review are the control. |
| "Static keys in env vars are fine internally" | They never expire and leak (L19); roles with short-lived tokens are the design. |

## Classroom Activities

1. **Responsibility matrix build (15 min):** a 3-tier app on IaaS vs PaaS — students fill the matrix; boundary failures highlighted.
2. **Policy diff (12 min):** instructor writes a least-privilege read policy, then its wildcard twin; the class diffs the risk.
3. **Lab 23 (45 min):** the course sandbox org — map who-can-do-what, find three escalation paths, rewrite the two worst policies, verify with a can-I-do-X script.

## Discussion Questions

1. Why does "the provider handles security" comfort executives and mislead engineers?
2. Federated SSO reduces password sprawl but concentrates blast radius — design the trade-off for a university.
3. Who audits the auditors' IAM policies? Propose a cadence and tooling sketch.

## Problem-Solving Exercise

> A data-science platform: notebook service role has `s3:*` on the org bucket; one prefix holds raw PII; a contractor's static keys are 2 years old.
> **Deliverable:** the escalation map (≥ 3 paths); rewritten policies with justification; the rotation plan; a detection rule for "role assumed from an unusual source."

## Summary

Cloud security failures are mostly configuration and identity failures: the platform holds, we configure. Least privilege, auditable policy, and short-lived credentials are the discipline. Next: hardening the compute itself.

## Exit Ticket

1. In PaaS, who patches the runtime?
2. What does `Action:"*"` on `Resource:"*"` mean — and why does it appear anyway?
3. Name two advantages of roles over static keys.

## References

- NIST SP 800-145, *The NIST Definition of Cloud Computing*. https://csrc.nist.gov
- NIST SP 800-210 (access control in cloud contexts). https://csrc.nist.gov
- CIS Benchmarks (provider-specific IAM foundations). https://www.cisecurity.org
- The cited misconfiguration post-mortem used in class: see `case-studies/` (per-term selection).
