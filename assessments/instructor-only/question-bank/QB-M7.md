# Question Bank — Module 7 (L25–L28) · CLO-7 · ⚠️ INSTRUCTOR-ONLY

Used by weekly quizzes Q13 (W13), Q15 (W15), and makeup packs. Duplicate-avoidance rule: see `README.md`.

## MCQ-7.1

**Topic:** Shared responsibility · **CLO-7** · **Bloom:** Understand · **Difficulty:** Easy · **Week:** 13
**Used in:** Q13

In IaaS, patching the guest operating system is the responsibility of:

- A. The provider
- B. The customer ✔
- C. The hardware vendor
- D. Nobody — VMs patch themselves

**Explanation:** Provider secures the hypervisor/infrastructure ("of" the cloud); customer secures everything they deploy ("in" the cloud). Key: B.

## MCQ-7.2

**Topic:** Identity — the new perimeter · **CLO-7** · **Bloom:** Analyze · **Difficulty:** Easy · **Week:** 13
**Used in:** Q13

The network perimeter is least useful in cloud environments because:

- A. Clouds have no firewalls
- B. Control-plane access is via authenticated API/identity — anyone with valid credentials is "inside" ✔
- C. VPCs are deprecated
- D. Latency is higher

**Explanation:** Cloud boundaries are identity- and API-driven; credential compromise substitutes for network intrusion. Key: B.

## MCQ-7.3

**Topic:** IAM wildcards · **CLO-7** · **Bloom:** Apply · **Difficulty:** Medium · **Week:** 13
**Used in:** Q13

An IAM policy grants `Action: "*", Resource: "*"`. The immediate risk:

- A. Extra logging
- B. Full administrative compromise if that identity leaks ✔
- C. Slow API responses
- D. Key rotation failures

**Explanation:** Wildcard-on-wildcard is full admin; least privilege demands scoped actions/resources. Key: B.

## MCQ-7.4

**Topic:** Static credentials · **CLO-7** · **Bloom:** Apply · **Difficulty:** Medium · **Week:** 13
**Used in:** Q13

An access key committed to a public code host was exploited within minutes. The best preventive fix:

- A. Longer key names
- B. Replace static keys with short-lived role-based credentials and secret scanning in CI ✔
- C. Private repository
- D. Rotate keys weekly

**Explanation:** Elimination beats rotation: roles issue ephemeral tokens; scanning catches regressions. (Private repos leak via forks/copies.) Key: B.

## MCQ-7.5

**Topic:** Control-plane logging · **CLO-7** · **Bloom:** Understand · **Difficulty:** Medium · **Week:** 15
**Used in:** Q15

"Who deleted this bucket?" is answered by:

- A. Flow logs
- B. Control-plane (management) audit logs ✔
- C. Load-balancer access logs
- D. DNS query logs

**Explanation:** Data-plane logs show traffic; API/control-plane audit logs record account actions (create/delete/modify). Key: B.

## MCQ-7.6

**Topic:** Misconfiguration scanning · **CLO-7** · **Bloom:** Apply · **Difficulty:** Medium · **Week:** 15
**Used in:** Q15

An IaC template that passed review still deploys a public bucket. The systemic fix:

- A. Ask reviewers to look harder
- B. Policy-as-code scanning (e.g., IaC lint/security policies) enforced in CI before deploy ✔
- C. Annual audit
- D. Manual console check

**Explanation:** Machine-enforced policy checks catch misconfig at build time; human review alone does not scale. Key: B.

## MCQ-7.7

**Topic:** Containers · **CLO-7** · **Bloom:** Analyze · **Difficulty:** Medium · **Week:** 15
**Used in:** Q15

Container escape severity is highest when:

- A. Images are large
- B. The runtime is privileged or mounts the host docker socket ✔
- C. The app is Python
- D. Logs go to stdout

**Explanation:** Privileged mode/socket mounts hand the container host-level control — the escape becomes trivial. Key: B.

## MCQ-7.8

**Topic:** Privacy — DPIA trigger · **CLO-7** · **Bloom:** Understand · **Difficulty:** Easy · **Week:** 15
**Used in:** Q15

Under GDPR-style rules, a DPIA is required before large-scale processing that:

- A. Uses any database
- B. Is likely to result in high risk to individuals (e.g., systematic monitoring, sensitive categories) ✔
- C. Runs in the cloud
- D. Stores fewer than 100 rows

**Explanation:** Art. 35 triggers are high-risk processing (systematic monitoring, special categories, large scale). Key: B.

## SA-7.1 (short answer, 6 marks)

**Topic:** Responsibility matrix · **CLO-7** · **Bloom:** Evaluate · **Difficulty:** Medium · **Week:** 15
**Used in:** Q15

For a web app on IaaS using managed Postgres: allocate responsibility (patching, IAM, encryption, logging) across provider/customer, and justify one "shared" item.

**Key:** IaaS: customer patches guest OS/app; provider secures hypervisor/hardware. IAM: customer defines roles/policies; provider enforces API authN. Encryption: customer owns keys/config (provider offers KMS — shared service, customer-owned key policy = the shared item). Logging: customer enables/retains audit logs; provider guarantees log integrity of control plane.

## SA-7.2 (short answer, 4 marks)

**Topic:** Data-subject rights · **CLO-7** · **Bloom:** Apply · **Difficulty:** Hard · **Week:** 15
**Used in:** makeup MT-8 only

A user invokes erasure. Name two rights to verify alongside it, and the two data stores most likely to block compliance.

**Key:** Verify identity/access right and portability (accept: rectification, objection); blockers: backups (restoreable copies) and log/telemetry stores where deletion conflicts with retention duties.
