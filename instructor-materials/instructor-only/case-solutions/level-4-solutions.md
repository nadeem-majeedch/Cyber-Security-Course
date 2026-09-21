# ⚠️ INSTRUCTOR-ONLY — Level 4 Model Solutions (CS-076–100)

Reveal at step 5. Level 4 cases are open-ended: these are *reference positions*, not unique answers. Grade: evidence-based reasoning, explicit assumptions, honest limitation statements, and the quality of tradeoff analysis.


## CS-076 — The Zero-Day You Cannot Patch
**Reference position.** Plan layers: (1) reduce surface — VPN restricted to managed devices with posture check (cuts the unmanaged footprints), (2) reduce exposure — WAF/IPS virtual rules in front of the appliance for known exploit shapes (imperfect, documented), (3) increase visibility — flow-based anomaly detection on VPN concentrator traffic (the appliance's blindness is the gap; netflow sees sessions), (4) prepare — rehearsed break-glass alternative (jump-hosts on hardened VMs) for the "appliance must come down" branch, (5) decision tree: exploitation indicators → isolate appliance population → activate jump-hosts → vendor engagement. Costs: posture-checking = device-management prerequisite; jump-hosts = capacity planning; the memo states plainly: risk is *elevated and monitored*, not mitigated.
**Assumptions to challenge.** That staff need full VPN (per-app ZTNA subset?); that the vendor's 6 weeks is credible.
**Discussion.** What triggers the jump-host switch-over, and who decides at 3 a.m.? What does "managed device" mean for contractors?

**Model solution (reference position — one defensible answer among several).** See the reference position above; the graded standard is the *quality of argument*, not convergence with this position.

**Expected reasoning.** Strong responses sequence: evidence inventory → assumptions made explicit → option generation (≥ 3) → evaluation against the scenario's constraints → decision with named residuals. Weak responses jump to a tool or a policy without the option space.

**Alternatives.** Because Level 4 cases are open-ended, the alternatives *are* the other defensible positions generated in class discussion; the instructor should surface at least two that differ structurally from the reference position (not merely re-parameterizations) and compare their risk/cost/feasibility profiles.

**Tradeoffs.** The reference position's named costs stand; push groups to name what their own preferred option sacrifices, and which stakeholder absorbs each cost.

**Common mistakes.** Solving the stated problem while ignoring the scenario's second-order constraint; inventing facts not in evidence; treating "defensible" as "unfalsifiable" (a position with no failure condition is not an analysis); missing that several of these cases make an *organizational* failure the root cause rather than a technical one.

**Discussion prompts.** Which assumption in your answer would you investigate first with real evidence? Whose sign-off does your decision need, and what do they need to see? What early-warning signal would tell you your chosen path is failing?

## CS-077 — Crypto-Agility on Deadline
**Reference position.** Memo core: the quantum risk asymmetry — confidentiality of *harvested traffic* (TLS) is largely protected by forward secrecy (harvest now ≠ decrypt later for modern suites); the real long-lived risks are (1) RSA-signed *archives* (signature forgery risk in 10+ years — authenticity, not secrecy), (2) at-rest AES-256 (safe under stated assumptions but inventory-dependent), (3) unknown crypto (the actual finding: no inventory). Program: crypto inventory (what, where, key lifetimes, protection class), priority migration of long-lived signatures to PQC/hybrid (performance-planned), TLS hygiene as routine, board-facing statement: "inventory-first, phased migration, no date-certain promises." Defensible priorities beat theater.
**Assumptions.** That milestone announcements drive attacker capability (uncertain — say so); that archives' authenticity matters to their consumers.
**Discussion.** Which archive would you migrate first and why? What is the cost of a *wrong* inventory claim to the board?

**Model solution (reference position — one defensible answer among several).** See the reference position above; the graded standard is the *quality of argument*, not convergence with this position.

**Expected reasoning.** Strong responses sequence: evidence inventory → assumptions made explicit → option generation (≥ 3) → evaluation against the scenario's constraints → decision with named residuals. Weak responses jump to a tool or a policy without the option space.

**Alternatives.** Because Level 4 cases are open-ended, the alternatives *are* the other defensible positions generated in class discussion; the instructor should surface at least two that differ structurally from the reference position (not merely re-parameterizations) and compare their risk/cost/feasibility profiles.

**Tradeoffs.** The reference position's named costs stand; push groups to name what their own preferred option sacrifices, and which stakeholder absorbs each cost.

**Common mistakes.** Solving the stated problem while ignoring the scenario's second-order constraint; inventing facts not in evidence; treating "defensible" as "unfalsifiable" (a position with no failure condition is not an analysis); missing that several of these cases make an *organizational* failure the root cause rather than a technical one.

**Discussion prompts.** Which assumption in your answer would you investigate first with real evidence? Whose sign-off does your decision need, and what do they need to see? What early-warning signal would tell you your chosen path is failing?

## CS-078 — The Side Channel in Production
**Reference position.** Path choice: constant-time fix despite 15% latency — partial mitigations (noise, rate limits) shrink but do not close the channel, and 10⁶ requests is within an attacker's patience at 10⁸/day scale. Mitigation hygiene while deploying: per-token-family rate limits + jitter (raises cost), disclosure response: thank researchers, committed timeline, coordinated note. SLO defense: 15% on *token verification* amortizes to ~2–3% of p99 across the API (measure, don't assert); offer SLO owner the per-endpoint carve-out with compensating rate limits as the alternative — but recommend the clean fix.
**Assumptions.** That verification latency is p99-critical (measure per endpoint); that no second channel exists (ask the researchers — they usually checked).
**Discussion.** When *would* rate-limiting be enough (lower-value secret, offline-bound victim)? How do you buy 15% latency back elsewhere?

**Model solution (reference position — one defensible answer among several).** See the reference position above; the graded standard is the *quality of argument*, not convergence with this position.

**Expected reasoning.** Strong responses sequence: evidence inventory → assumptions made explicit → option generation (≥ 3) → evaluation against the scenario's constraints → decision with named residuals. Weak responses jump to a tool or a policy without the option space.

**Alternatives.** Because Level 4 cases are open-ended, the alternatives *are* the other defensible positions generated in class discussion; the instructor should surface at least two that differ structurally from the reference position (not merely re-parameterizations) and compare their risk/cost/feasibility profiles.

**Tradeoffs.** The reference position's named costs stand; push groups to name what their own preferred option sacrifices, and which stakeholder absorbs each cost.

**Common mistakes.** Solving the stated problem while ignoring the scenario's second-order constraint; inventing facts not in evidence; treating "defensible" as "unfalsifiable" (a position with no failure condition is not an analysis); missing that several of these cases make an *organizational* failure the root cause rather than a technical one.

**Discussion prompts.** Which assumption in your answer would you investigate first with real evidence? Whose sign-off does your decision need, and what do they need to see? What early-warning signal would tell you your chosen path is failing?

## CS-079 — Framework on Fire
**Reference position.** Sequence: (1) WAF virtual patch on all 30 immediately (imperfect coverage — document bypass risk), (2) patch the 12 internet-exposed services first (staged: canary → batch), (3) PCI-scoped two: negotiate emergency change with the auditor (change freezes have security-exception clauses — *invoke them with evidence*; the alternative, unpatched PCI systems, is the worse audit outcome), (4) internal services in batches over the week. User comms: forced logout email (security maintenance, session reset required — one honest line, no fear); support prepped for volume.
**Assumptions.** That virtual patch covers the observed exploitation pattern (test with the public PoC in staging); that the auditor will bend (they usually do for documented risk).
**Discussion.** What does "the freeze" exist to protect, and does this event qualify? How do you sequence logout messaging to avoid panic?

**Model solution (reference position — one defensible answer among several).** See the reference position above; the graded standard is the *quality of argument*, not convergence with this position.

**Expected reasoning.** Strong responses sequence: evidence inventory → assumptions made explicit → option generation (≥ 3) → evaluation against the scenario's constraints → decision with named residuals. Weak responses jump to a tool or a policy without the option space.

**Alternatives.** Because Level 4 cases are open-ended, the alternatives *are* the other defensible positions generated in class discussion; the instructor should surface at least two that differ structurally from the reference position (not merely re-parameterizations) and compare their risk/cost/feasibility profiles.

**Tradeoffs.** The reference position's named costs stand; push groups to name what their own preferred option sacrifices, and which stakeholder absorbs each cost.

**Common mistakes.** Solving the stated problem while ignoring the scenario's second-order constraint; inventing facts not in evidence; treating "defensible" as "unfalsifiable" (a position with no failure condition is not an analysis); missing that several of these cases make an *organizational* failure the root cause rather than a technical one.

**Discussion prompts.** Which assumption in your answer would you investigate first with real evidence? Whose sign-off does your decision need, and what do they need to see? What early-warning signal would tell you your chosen path is failing?

## CS-080 — The Host Header
**Reference position.** Fix location: *both*, prioritized — (1) app-level: generate reset URLs from configured base URL only (the durable fix; apps must not trust routing metadata), (2) platform-level: proxy allow-list normalization for known hosts (fleet-wide mitigation for the other 39 apps' *unknown* similar bugs). Ownership resolution: app team owns their fix; platform team owns the fleet mitigation; security tracks both with dates. Disclosure: acknowledge within 48h, fix timeline ~2 weeks, bounty per program, publication coordinated; the reporter's deadline is negotiated, not ignored.
**Assumptions.** That no other app depends on Host for generation (audit the other 39 — that is the real finding's scale).
**Discussion.** Why is defense-in-depth mandatory here rather than optional? What does the fleet audit look like?

**Model solution (reference position — one defensible answer among several).** See the reference position above; the graded standard is the *quality of argument*, not convergence with this position.

**Expected reasoning.** Strong responses sequence: evidence inventory → assumptions made explicit → option generation (≥ 3) → evaluation against the scenario's constraints → decision with named residuals. Weak responses jump to a tool or a policy without the option space.

**Alternatives.** Because Level 4 cases are open-ended, the alternatives *are* the other defensible positions generated in class discussion; the instructor should surface at least two that differ structurally from the reference position (not merely re-parameterizations) and compare their risk/cost/feasibility profiles.

**Tradeoffs.** The reference position's named costs stand; push groups to name what their own preferred option sacrifices, and which stakeholder absorbs each cost.

**Common mistakes.** Solving the stated problem while ignoring the scenario's second-order constraint; inventing facts not in evidence; treating "defensible" as "unfalsifiable" (a position with no failure condition is not an analysis); missing that several of these cases make an *organizational* failure the root cause rather than a technical one.

**Discussion prompts.** Which assumption in your answer would you investigate first with real evidence? Whose sign-off does your decision need, and what do they need to see? What early-warning signal would tell you your chosen path is failing?

## CS-081 — The Token That Lives Forever
**Reference position.** Strategy: layered enforcement — (1) new tokens versioned with short TTL + refresh, (2) proxy-layer: old-version tokens get *read-scoped* enforcement at the gateway (unknown to the old clients) — they keep working but lose sensitive scopes, (3) kill-switch per token kept available; brute revocation reserved for compromise, not migration (400k support calls ≠ acceptable), (4) comms: value messaging for update ("new features"), not threat messaging. Support-cost model built before decision.
**Assumptions.** That the gateway can distinguish token versions (verify); that sensitive scopes are enumerable.
**Discussion.** Is silently downscoping old devices ethical (transparency vs. security)? What is the sunset line for the 400k?

**Model solution (reference position — one defensible answer among several).** See the reference position above; the graded standard is the *quality of argument*, not convergence with this position.

**Expected reasoning.** Strong responses sequence: evidence inventory → assumptions made explicit → option generation (≥ 3) → evaluation against the scenario's constraints → decision with named residuals. Weak responses jump to a tool or a policy without the option space.

**Alternatives.** Because Level 4 cases are open-ended, the alternatives *are* the other defensible positions generated in class discussion; the instructor should surface at least two that differ structurally from the reference position (not merely re-parameterizations) and compare their risk/cost/feasibility profiles.

**Tradeoffs.** The reference position's named costs stand; push groups to name what their own preferred option sacrifices, and which stakeholder absorbs each cost.

**Common mistakes.** Solving the stated problem while ignoring the scenario's second-order constraint; inventing facts not in evidence; treating "defensible" as "unfalsifiable" (a position with no failure condition is not an analysis); missing that several of these cases make an *organizational* failure the root cause rather than a technical one.

**Discussion prompts.** Which assumption in your answer would you investigate first with real evidence? Whose sign-off does your decision need, and what do they need to see? What early-warning signal would tell you your chosen path is failing?

## CS-082 — BOLA Across Tenants
**Reference position.** Incident-vs-vulnerability: treat as *incident* — cross-tenant data access was demonstrated (even if researcher-only); contractual terms likely require notification of affected-tenant customers *if data exposure is provable from logs* — the log analysis (was anything but the tester's UUID accessed?) is the pivot; UUID infeasibility plus no exploitation evidence may support "vulnerability, patched, no evidence of abuse" — document either way. Remediation: tenant-scoping middleware (object ownership/tenancy check centralized — never per-endpoint again), the search-by-title endpoint scoped immediately (the ID-leak source), regression tests for cross-tenant access as CI gate. Tester coordination: extended embargo for the fix window.
**Assumptions.** That log completeness is trustworthy (verify log integrity first).
**Discussion.** What would change your notification decision (one content-access log line)? Where else does authorization live per-endpoint in this codebase?

**Model solution (reference position — one defensible answer among several).** See the reference position above; the graded standard is the *quality of argument*, not convergence with this position.

**Expected reasoning.** Strong responses sequence: evidence inventory → assumptions made explicit → option generation (≥ 3) → evaluation against the scenario's constraints → decision with named residuals. Weak responses jump to a tool or a policy without the option space.

**Alternatives.** Because Level 4 cases are open-ended, the alternatives *are* the other defensible positions generated in class discussion; the instructor should surface at least two that differ structurally from the reference position (not merely re-parameterizations) and compare their risk/cost/feasibility profiles.

**Tradeoffs.** The reference position's named costs stand; push groups to name what their own preferred option sacrifices, and which stakeholder absorbs each cost.

**Common mistakes.** Solving the stated problem while ignoring the scenario's second-order constraint; inventing facts not in evidence; treating "defensible" as "unfalsifiable" (a position with no failure condition is not an analysis); missing that several of these cases make an *organizational* failure the root cause rather than a technical one.

**Discussion prompts.** Which assumption in your answer would you investigate first with real evidence? Whose sign-off does your decision need, and what do they need to see? What early-warning signal would tell you your chosen path is failing?

## CS-083 — Prioritization Under Protest
**Reference position.** Model redesign — missing criteria: (1) interconnection/blast radius (a finding on a hub asset outranks its severity), (2) threat-actor targeting signal (KEV, intel reports on *this* stack), (3) compensating-control presence (mitigated findings demote honestly), (4) remediation feasibility (quick wins ride up). Exception process: owners contest with evidence (their asset data, threat context), security adjudicates within 5 days, exceptions expire (90 days) and are logged — protest becomes process, not politics. The eventual incident: retrospective shows the finding was *correctly* demoted by incomplete criteria — the fix is criteria, not blame; the retro writes the model's v2.
**Assumptions.** That asset-criticality data exists (if not, that's the real project).
**Discussion.** Which criterion would have caught the demoted finding? How do you prevent the exception process from becoming the new backlog?

**Model solution (reference position — one defensible answer among several).** See the reference position above; the graded standard is the *quality of argument*, not convergence with this position.

**Expected reasoning.** Strong responses sequence: evidence inventory → assumptions made explicit → option generation (≥ 3) → evaluation against the scenario's constraints → decision with named residuals. Weak responses jump to a tool or a policy without the option space.

**Alternatives.** Because Level 4 cases are open-ended, the alternatives *are* the other defensible positions generated in class discussion; the instructor should surface at least two that differ structurally from the reference position (not merely re-parameterizations) and compare their risk/cost/feasibility profiles.

**Tradeoffs.** The reference position's named costs stand; push groups to name what their own preferred option sacrifices, and which stakeholder absorbs each cost.

**Common mistakes.** Solving the stated problem while ignoring the scenario's second-order constraint; inventing facts not in evidence; treating "defensible" as "unfalsifiable" (a position with no failure condition is not an analysis); missing that several of these cases make an *organizational* failure the root cause rather than a technical one.

**Discussion prompts.** Which assumption in your answer would you investigate first with real evidence? Whose sign-off does your decision need, and what do they need to see? What early-warning signal would tell you your chosen path is failing?

## CS-084 — The Sensor That Lies
**Reference position.** Compensating detection now: network-side sensors ( Zeek/flow class) on the finance segment — different visibility plane, temporally reliable; correlation layer tags delayed-EDR hosts so analysts know which timeline to trust. Trust model for sensors generally: (1) sensor self-tests (heartbeat with known-event injection: the "canary process" — if it arrives late, the sensor declares itself degraded), (2) cross-plane validation sampling (EDR event vs. netflow event for same action), (3) telemetry-SLO per sensor with alerting. Vendor bug: escalate with the canary data (you can *prove* the delay pattern).
**Assumptions.** That network sensors see the relevant events (process-creation ≠ network events — coverage differs; state the gap).
**Discussion.** How would you have detected the lying sensor *without* the incident? What is your "sensor trust" model in the SOC runbook?

**Model solution (reference position — one defensible answer among several).** See the reference position above; the graded standard is the *quality of argument*, not convergence with this position.

**Expected reasoning.** Strong responses sequence: evidence inventory → assumptions made explicit → option generation (≥ 3) → evaluation against the scenario's constraints → decision with named residuals. Weak responses jump to a tool or a policy without the option space.

**Alternatives.** Because Level 4 cases are open-ended, the alternatives *are* the other defensible positions generated in class discussion; the instructor should surface at least two that differ structurally from the reference position (not merely re-parameterizations) and compare their risk/cost/feasibility profiles.

**Tradeoffs.** The reference position's named costs stand; push groups to name what their own preferred option sacrifices, and which stakeholder absorbs each cost.

**Common mistakes.** Solving the stated problem while ignoring the scenario's second-order constraint; inventing facts not in evidence; treating "defensible" as "unfalsifiable" (a position with no failure condition is not an analysis); missing that several of these cases make an *organizational* failure the root cause rather than a technical one.

**Discussion prompts.** Which assumption in your answer would you investigate first with real evidence? Whose sign-off does your decision need, and what do they need to see? What early-warning signal would tell you your chosen path is failing?

## CS-085 — Detection Debt
**Reference position.** Program: (1) triage the 2,400: never-fired → candidate-retire (but check: silence ≠ useless — coverage rules get *synthetic tests*), FP-only → fix-or-retire, broken → fix via schema-mapping; (2) testing-as-code: every rule ships with a test event; CI runs rule-vs-tests on schema changes (breakage detected in hours, not years); (3) retirement criteria: no true hits + no coverage rationale + failing test = retire with sign-off; (4) coverage measurement: ATT&CK-mapped, purple-team-validated quarterly — "would I bet the company" = the validated subset, published as such. 6-month plan: months 1–2 triage automation, 3–4 fix/retire waves + CI, 5–6 purple-validation cycle 1.
**Assumptions.** Engineer capacity holds; retiring rules survives the "we might need it" politics (sign-off process is the shield).
**Discussion.** Which is riskier: a never-fired rule or a silently-broken one? How do you decide what "coverage" promises?

**Model solution (reference position — one defensible answer among several).** See the reference position above; the graded standard is the *quality of argument*, not convergence with this position.

**Expected reasoning.** Strong responses sequence: evidence inventory → assumptions made explicit → option generation (≥ 3) → evaluation against the scenario's constraints → decision with named residuals. Weak responses jump to a tool or a policy without the option space.

**Alternatives.** Because Level 4 cases are open-ended, the alternatives *are* the other defensible positions generated in class discussion; the instructor should surface at least two that differ structurally from the reference position (not merely re-parameterizations) and compare their risk/cost/feasibility profiles.

**Tradeoffs.** The reference position's named costs stand; push groups to name what their own preferred option sacrifices, and which stakeholder absorbs each cost.

**Common mistakes.** Solving the stated problem while ignoring the scenario's second-order constraint; inventing facts not in evidence; treating "defensible" as "unfalsifiable" (a position with no failure condition is not an analysis); missing that several of these cases make an *organizational* failure the root cause rather than a technical one.

**Discussion prompts.** Which assumption in your answer would you investigate first with real evidence? Whose sign-off does your decision need, and what do they need to see? What early-warning signal would tell you your chosen path is failing?

## CS-086 — The Phantom Admin
**Reference position.** Hypothesis assessment: (3-month-cadence, 3 a.m., datacenter source IP) pattern fits (b) forgotten service account (automation run monthly — backup/audit job?) *most likely*; (c) former-employee plausible if IP maps to their later employer (check who operated that IP block then); (a) attacker persistence over 3 years with *no other indicators* and *regular monthly* usage is least consistent (attackers don't keep schedules). Discriminating evidence: what the account *does* each use (job-like commands → (b)); creation-era context (was there a contractor engagement 3 years ago?); IP ownership at first-use date. Containment: disable + preserve (don't delete — the account is evidence; monitoring on any re-enable attempt). Governance finding: identity lifecycle has no registry-of-accounts reconciliation — the real fix.
**Assumptions.** That the IP attribution data is obtainable; that HR-contractor records are complete (verify — they may not be).
**Discussion.** Why is "disable + preserve" better than delete here? What process would have made this account self-documenting?

**Model solution (reference position — one defensible answer among several).** See the reference position above; the graded standard is the *quality of argument*, not convergence with this position.

**Expected reasoning.** Strong responses sequence: evidence inventory → assumptions made explicit → option generation (≥ 3) → evaluation against the scenario's constraints → decision with named residuals. Weak responses jump to a tool or a policy without the option space.

**Alternatives.** Because Level 4 cases are open-ended, the alternatives *are* the other defensible positions generated in class discussion; the instructor should surface at least two that differ structurally from the reference position (not merely re-parameterizations) and compare their risk/cost/feasibility profiles.

**Tradeoffs.** The reference position's named costs stand; push groups to name what their own preferred option sacrifices, and which stakeholder absorbs each cost.

**Common mistakes.** Solving the stated problem while ignoring the scenario's second-order constraint; inventing facts not in evidence; treating "defensible" as "unfalsifiable" (a position with no failure condition is not an analysis); missing that several of these cases make an *organizational* failure the root cause rather than a technical one.

**Discussion prompts.** Which assumption in your answer would you investigate first with real evidence? Whose sign-off does your decision need, and what do they need to see? What early-warning signal would tell you your chosen path is failing?

## CS-087 — Attribution Pressure
**Reference position.** Board answer structure: (1) what the evidence supports: "tooling and procedures match a financially-motivated ransomware affiliate program (moderate confidence)" — cite the public reporting basis, (2) what it does not support: nation-state narrative (no indicators), (3) why the distinction matters: response obligations, insurance, law-enforcement referral paths, and *accuracy under future discovery*. Confidence language standard: defined terms (low/moderate/high) with evidence-class definitions — published in the IR plan so the board reads the same dictionary. The risk of narrative capture: credibility loss when forensics/LE later say otherwise — investors punish corrected narratives harder than honest uncertainty.
**Assumptions.** That analysts' tooling assessment is sound (second-opinion via IR retainer is cheap insurance).
**Discussion.** Who owns attribution confidence standards? When would you *publish* attribution at all?

**Model solution (reference position — one defensible answer among several).** See the reference position above; the graded standard is the *quality of argument*, not convergence with this position.

**Expected reasoning.** Strong responses sequence: evidence inventory → assumptions made explicit → option generation (≥ 3) → evaluation against the scenario's constraints → decision with named residuals. Weak responses jump to a tool or a policy without the option space.

**Alternatives.** Because Level 4 cases are open-ended, the alternatives *are* the other defensible positions generated in class discussion; the instructor should surface at least two that differ structurally from the reference position (not merely re-parameterizations) and compare their risk/cost/feasibility profiles.

**Tradeoffs.** The reference position's named costs stand; push groups to name what their own preferred option sacrifices, and which stakeholder absorbs each cost.

**Common mistakes.** Solving the stated problem while ignoring the scenario's second-order constraint; inventing facts not in evidence; treating "defensible" as "unfalsifiable" (a position with no failure condition is not an analysis); missing that several of these cases make an *organizational* failure the root cause rather than a technical one.

**Discussion prompts.** Which assumption in your answer would you investigate first with real evidence? Whose sign-off does your decision need, and what do they need to see? What early-warning signal would tell you your chosen path is failing?

## CS-088 — Landing Zone From Chaos
**Reference position.** Choice: (c) hybrid — but with a hard rule: *every* workload passing through migration gets landing-zone identity/network/logging baselines *even if it lands in the old structure* (migration as the forcing function). Guardrails (non-negotiable): central logging account (immutable), identity federation with MFA everywhere, no standing `*:*`, network baseline (egress allow-lists), IaC-only changes. Ordering: least-critical first (learn the pipeline), crown jewels last (by then the pipeline is rehearsed) — except one early *representative* crown-jewel pilot to surface hard problems while there's schedule slack.
**Assumptions.** That the 9-month date is truly fixed (verify — boards move dates less than they say); that app-team anger is survivable with good enablement.
**Discussion.** What would make you switch to full (b)? Which guardrail would teams contest first and how do you hold it?

**Model solution (reference position — one defensible answer among several).** See the reference position above; the graded standard is the *quality of argument*, not convergence with this position.

**Expected reasoning.** Strong responses sequence: evidence inventory → assumptions made explicit → option generation (≥ 3) → evaluation against the scenario's constraints → decision with named residuals. Weak responses jump to a tool or a policy without the option space.

**Alternatives.** Because Level 4 cases are open-ended, the alternatives *are* the other defensible positions generated in class discussion; the instructor should surface at least two that differ structurally from the reference position (not merely re-parameterizations) and compare their risk/cost/feasibility profiles.

**Tradeoffs.** The reference position's named costs stand; push groups to name what their own preferred option sacrifices, and which stakeholder absorbs each cost.

**Common mistakes.** Solving the stated problem while ignoring the scenario's second-order constraint; inventing facts not in evidence; treating "defensible" as "unfalsifiable" (a position with no failure condition is not an analysis); missing that several of these cases make an *organizational* failure the root cause rather than a technical one.

**Discussion prompts.** Which assumption in your answer would you investigate first with real evidence? Whose sign-off does your decision need, and what do they need to see? What early-warning signal would tell you your chosen path is failing?

## CS-089 — The Cloud Key That Saw Everything
**Reference position.** Redesign: (1) no human/pipeline credential *storage* — brokered access (vault issues short-lived, per-use credentials scoped to the requested system), (2) the aggregation point dissolves: secrets-bucket abolished; each system's secret lives with its system, (3) pipeline gets *workload identity* per-deployment (no static anything), (4) portfolio-level least privilege: define as "no single identity can reach >1 system's crown-jewel class" — the *composition* rule, audited as such. Audit trail note: the breach was survivable forensically *because* logging existed — that part worked.
**Assumptions.** That 14 systems can adopt brokered access within the year (sequenced plan needed).
**Discussion.** What is least privilege for a *fleet* vs. a key? Which system resists the redesign and why?

**Model solution (reference position — one defensible answer among several).** See the reference position above; the graded standard is the *quality of argument*, not convergence with this position.

**Expected reasoning.** Strong responses sequence: evidence inventory → assumptions made explicit → option generation (≥ 3) → evaluation against the scenario's constraints → decision with named residuals. Weak responses jump to a tool or a policy without the option space.

**Alternatives.** Because Level 4 cases are open-ended, the alternatives *are* the other defensible positions generated in class discussion; the instructor should surface at least two that differ structurally from the reference position (not merely re-parameterizations) and compare their risk/cost/feasibility profiles.

**Tradeoffs.** The reference position's named costs stand; push groups to name what their own preferred option sacrifices, and which stakeholder absorbs each cost.

**Common mistakes.** Solving the stated problem while ignoring the scenario's second-order constraint; inventing facts not in evidence; treating "defensible" as "unfalsifiable" (a position with no failure condition is not an analysis); missing that several of these cases make an *organizational* failure the root cause rather than a technical one.

**Discussion prompts.** Which assumption in your answer would you investigate first with real evidence? Whose sign-off does your decision need, and what do they need to see? What early-warning signal would tell you your chosen path is failing?

## CS-090 — The Firmware You Cannot See
**Reference position.** Without-vendor-cooperation plan: (1) network containment — controllers on dedicated zone; update-over-HTTP intercepted by a verification proxy (you cannot verify signatures that don't exist — you *can* pin expected image hashes per controller and alert on mismatch), (2) monitoring — baseline each controller's flows; HVAC protocols are stable (deviations alert), (3) exposure reduction — no inbound from general networks; management only via jump path, (4) contract strategy: renewal leverage = the unsigned-update finding + SBOM refusal documented as supply-chain risk; demands: signed firmware, SBOM, vuln-disclosure SLA; alternative-vendor evaluation started now (8 months is enough).
**Assumptions.** That pinning hashes is feasible across 300 controllers (inventory effort); that facilities' comfort can be maintained through containment (test before full rollout).
**Discussion.** What does "trust" mean for a vendor who refuses transparency? Which demand is the walk-away line?

**Model solution (reference position — one defensible answer among several).** See the reference position above; the graded standard is the *quality of argument*, not convergence with this position.

**Expected reasoning.** Strong responses sequence: evidence inventory → assumptions made explicit → option generation (≥ 3) → evaluation against the scenario's constraints → decision with named residuals. Weak responses jump to a tool or a policy without the option space.

**Alternatives.** Because Level 4 cases are open-ended, the alternatives *are* the other defensible positions generated in class discussion; the instructor should surface at least two that differ structurally from the reference position (not merely re-parameterizations) and compare their risk/cost/feasibility profiles.

**Tradeoffs.** The reference position's named costs stand; push groups to name what their own preferred option sacrifices, and which stakeholder absorbs each cost.

**Common mistakes.** Solving the stated problem while ignoring the scenario's second-order constraint; inventing facts not in evidence; treating "defensible" as "unfalsifiable" (a position with no failure condition is not an analysis); missing that several of these cases make an *organizational* failure the root cause rather than a technical one.

**Discussion prompts.** Which assumption in your answer would you investigate first with real evidence? Whose sign-off does your decision need, and what do they need to see? What early-warning signal would tell you your chosen path is failing?

## CS-091 — Rogue AP Geometry
**Reference position.** Hunt: (1) detection — WIDS with BSSID-inventory drift alerting (new MAC on corporate SSID = page), (2) localization — layered triangulation across APs floor-by-floor (the mobility pattern means *containment windows*, not one sweep), (3) legal/HR interface: if the source is a person with university affiliation, it's a disciplinary/police matter — evidence handled accordingly (photograph, logs, chain-of-custody); physical security leads contact once located. Architectural fix: PSK and 802.1X on the *same SSID* is the flaw — the SSID clones harvest PSK credentials; split identities (eduroam/802.1X for people, separate portal-based guest), plus WPA3/SAE where PSK remains, plus client-side certificate validation guidance. The credential class that can be *spoken* is the harvestable class — remove spoken credentials.
**Assumptions.** That the actor is reachable (may be external — theft of hardware resale, adjust response); that WIDS coverage exists in the building (deploy if not — first purchase).
**Discussion.** Why does splitting SSIDs defeat the harvest even before WIDS? What is your evidence threshold for involving police?

**Model solution (reference position — one defensible answer among several).** See the reference position above; the graded standard is the *quality of argument*, not convergence with this position.

**Expected reasoning.** Strong responses sequence: evidence inventory → assumptions made explicit → option generation (≥ 3) → evaluation against the scenario's constraints → decision with named residuals. Weak responses jump to a tool or a policy without the option space.

**Alternatives.** Because Level 4 cases are open-ended, the alternatives *are* the other defensible positions generated in class discussion; the instructor should surface at least two that differ structurally from the reference position (not merely re-parameterizations) and compare their risk/cost/feasibility profiles.

**Tradeoffs.** The reference position's named costs stand; push groups to name what their own preferred option sacrifices, and which stakeholder absorbs each cost.

**Common mistakes.** Solving the stated problem while ignoring the scenario's second-order constraint; inventing facts not in evidence; treating "defensible" as "unfalsifiable" (a position with no failure condition is not an analysis); missing that several of these cases make an *organizational* failure the root cause rather than a technical one.

**Discussion prompts.** Which assumption in your answer would you investigate first with real evidence? Whose sign-off does your decision need, and what do they need to see? What early-warning signal would tell you your chosen path is failing?

## CS-092 — The Data Poisoning Audit
**Reference position.** Remediation: (1) label-source diversification — add bank-side investigation labels as second source; merchant self-reports become *features*, not labels, (2) poisoning detection on label streams: per-source label-rate anomaly monitoring (the cartel's 2,000/week signature is detectable in hindsight — make it detectable in advance), (3) model action: retrain on clean labels only for the affected segment; consider score-rollback for decisions made in the drift window (list of affected merchants → re-review), (4) earlier-detection monitor: segment-level precision drift against confirmed fraud (the metric that was missing — drift was only visible in *aggregate*).
**Assumptions.** That clean labels exist for the affected window (investigation capacity); that the cartel's behavior doesn't adapt (it will — monitor the monitor).
**Discussion.** Which is the *system* fix: label governance or drift detection? What does "trust your labels" mean in procurement-linked data?

**Model solution (reference position — one defensible answer among several).** See the reference position above; the graded standard is the *quality of argument*, not convergence with this position.

**Expected reasoning.** Strong responses sequence: evidence inventory → assumptions made explicit → option generation (≥ 3) → evaluation against the scenario's constraints → decision with named residuals. Weak responses jump to a tool or a policy without the option space.

**Alternatives.** Because Level 4 cases are open-ended, the alternatives *are* the other defensible positions generated in class discussion; the instructor should surface at least two that differ structurally from the reference position (not merely re-parameterizations) and compare their risk/cost/feasibility profiles.

**Tradeoffs.** The reference position's named costs stand; push groups to name what their own preferred option sacrifices, and which stakeholder absorbs each cost.

**Common mistakes.** Solving the stated problem while ignoring the scenario's second-order constraint; inventing facts not in evidence; treating "defensible" as "unfalsifiable" (a position with no failure condition is not an analysis); missing that several of these cases make an *organizational* failure the root cause rather than a technical one.

**Discussion prompts.** Which assumption in your answer would you investigate first with real evidence? Whose sign-off does your decision need, and what do they need to see? What early-warning signal would tell you your chosen path is failing?

## CS-093 — Privacy Budget Exhausted
**Reference position.** Semester path: (1) stop free-form querying; move to a *published-tables* model (fixed releases, pre-computed — no incremental budget burn), (2) remaining budget reserved for the highest-value planned releases (DPO + research-lead committee picks), (3) parameter process for next term: epsilon set per *release class* with statistical justification + DPO sign-off, per-user quotas to prevent concentration, and public accounting (researchers see the budget — scarcity becomes governable). The arbitrary initial parameter gets documented honestly: it was a placeholder; the fix is process, not blame.
**Assumptions.** That fixed-table releases satisfy most research needs (survey the researchers — demand shapes design); that composition/accounting is implemented correctly (audit it — budget math errors are common).
**Discussion.** What does the DPO need to see to defend *any* epsilon? How do you handle the researcher whose project dies with the budget?

**Model solution (reference position — one defensible answer among several).** See the reference position above; the graded standard is the *quality of argument*, not convergence with this position.

**Expected reasoning.** Strong responses sequence: evidence inventory → assumptions made explicit → option generation (≥ 3) → evaluation against the scenario's constraints → decision with named residuals. Weak responses jump to a tool or a policy without the option space.

**Alternatives.** Because Level 4 cases are open-ended, the alternatives *are* the other defensible positions generated in class discussion; the instructor should surface at least two that differ structurally from the reference position (not merely re-parameterizations) and compare their risk/cost/feasibility profiles.

**Tradeoffs.** The reference position's named costs stand; push groups to name what their own preferred option sacrifices, and which stakeholder absorbs each cost.

**Common mistakes.** Solving the stated problem while ignoring the scenario's second-order constraint; inventing facts not in evidence; treating "defensible" as "unfalsifiable" (a position with no failure condition is not an analysis); missing that several of these cases make an *organizational* failure the root cause rather than a technical one.

**Discussion prompts.** Which assumption in your answer would you investigate first with real evidence? Whose sign-off does your decision need, and what do they need to see? What early-warning signal would tell you your chosen path is failing?

## CS-094 — The Synthetic Cover-Up
**Reference position.** Technical audit: (1) membership-inference attacks against the generator/model (state of the art: per-record and population-level), (2) distance-to-closest-record metrics on synthetic outputs (rare-combination reproduction quantified), (3) lineage review (what exactly trained the generator). Governance resolution: "synthetic" is *not* a magic word — the university standard becomes: synthesis claims require documented generator lineage + MIA testing + residual-risk statement with DPO sign-off; the team's obstruction goes to their management as a governance-process finding (not punishment theater — process). Timeline pressure: deployment waits for the audit; interim: restrict outputs to non-sensitive domains.
**Assumptions.** That MIA testing is competent (methodology review by a second party); that rare-combination risk matters for this data class (depends on records — assess).
**Discussion.** When *is* synthetic data genuinely low-risk? What does the standard cost legitimate synthetic-data projects?

**Model solution (reference position — one defensible answer among several).** See the reference position above; the graded standard is the *quality of argument*, not convergence with this position.

**Expected reasoning.** Strong responses sequence: evidence inventory → assumptions made explicit → option generation (≥ 3) → evaluation against the scenario's constraints → decision with named residuals. Weak responses jump to a tool or a policy without the option space.

**Alternatives.** Because Level 4 cases are open-ended, the alternatives *are* the other defensible positions generated in class discussion; the instructor should surface at least two that differ structurally from the reference position (not merely re-parameterizations) and compare their risk/cost/feasibility profiles.

**Tradeoffs.** The reference position's named costs stand; push groups to name what their own preferred option sacrifices, and which stakeholder absorbs each cost.

**Common mistakes.** Solving the stated problem while ignoring the scenario's second-order constraint; inventing facts not in evidence; treating "defensible" as "unfalsifiable" (a position with no failure condition is not an analysis); missing that several of these cases make an *organizational* failure the root cause rather than a technical one.

**Discussion prompts.** Which assumption in your answer would you investigate first with real evidence? Whose sign-off does your decision need, and what do they need to see? What early-warning signal would tell you your chosen path is failing?

## CS-095 — Third-Party Breach, First-Party Data
**Reference position.** Response: (1) notification duty analysis — as controller of your employees' data, your notification obligations to them likely stand regardless of the vendor's role; regulator notification per your jurisdiction; don't outsource the duty to the vendor's comms, (2) employee support: dedicated channel, credit/fraud monitoring offer, plain-language facts (including "the vendor was breached; your data was in their system"), (3) vendor remedy: contract terms — notification breach, liability cap fight (cap likely irrelevant to regulatory exposure), audit rights *now exercised*, (4) program redesign: Tier-1 = any processor of PII at scale (not by spend!) — full assessment, SSO, data-export/portability clauses, exit plan; questionnaires alone never qualify a Tier 1.
**Assumptions.** That your contract has cooperation/audit clauses (read it now, in the case, as practice); that insurer notification is timely.
**Discussion.** Why is "by spend" tiering wrong? What would you have asked *before* signing this vendor?

**Model solution (reference position — one defensible answer among several).** See the reference position above; the graded standard is the *quality of argument*, not convergence with this position.

**Expected reasoning.** Strong responses sequence: evidence inventory → assumptions made explicit → option generation (≥ 3) → evaluation against the scenario's constraints → decision with named residuals. Weak responses jump to a tool or a policy without the option space.

**Alternatives.** Because Level 4 cases are open-ended, the alternatives *are* the other defensible positions generated in class discussion; the instructor should surface at least two that differ structurally from the reference position (not merely re-parameterizations) and compare their risk/cost/feasibility profiles.

**Tradeoffs.** The reference position's named costs stand; push groups to name what their own preferred option sacrifices, and which stakeholder absorbs each cost.

**Common mistakes.** Solving the stated problem while ignoring the scenario's second-order constraint; inventing facts not in evidence; treating "defensible" as "unfalsifiable" (a position with no failure condition is not an analysis); missing that several of these cases make an *organizational* failure the root cause rather than a technical one.

**Discussion prompts.** Which assumption in your answer would you investigate first with real evidence? Whose sign-off does your decision need, and what do they need to see? What early-warning signal would tell you your chosen path is failing?

## CS-096 — The Board Wants a Number
**Reference position.** The answer: a range with a loss-exceedance framing — "annual expected loss between €X and €Y (P50–P95), driven primarily by [top 3 scenarios]" — built from FAIR-class estimation: industry loss data calibrated to your size, your 5-year incident history as a frequency anchor (with its small-sample caveat stated), control-maturity deltas as scenario modifiers. Communication: one page, the range, the three scenarios, what would move the number. Stop collecting: nothing. Start collecting: incident-impact data (actual costs per incident — the scarcest input), control-failure data (which controls fired vs. failed in incidents).
**Assumptions.** That the board can handle ranges (test with the CFO first); that scenario selection is defensible (workshop it).
**Discussion.** What is the ethical line between honest uncertainty and useless vagueness? Which measurement improves next year's number most?

**Model solution (reference position — one defensible answer among several).** See the reference position above; the graded standard is the *quality of argument*, not convergence with this position.

**Expected reasoning.** Strong responses sequence: evidence inventory → assumptions made explicit → option generation (≥ 3) → evaluation against the scenario's constraints → decision with named residuals. Weak responses jump to a tool or a policy without the option space.

**Alternatives.** Because Level 4 cases are open-ended, the alternatives *are* the other defensible positions generated in class discussion; the instructor should surface at least two that differ structurally from the reference position (not merely re-parameterizations) and compare their risk/cost/feasibility profiles.

**Tradeoffs.** The reference position's named costs stand; push groups to name what their own preferred option sacrifices, and which stakeholder absorbs each cost.

**Common mistakes.** Solving the stated problem while ignoring the scenario's second-order constraint; inventing facts not in evidence; treating "defensible" as "unfalsifiable" (a position with no failure condition is not an analysis); missing that several of these cases make an *organizational* failure the root cause rather than a technical one.

**Discussion prompts.** Which assumption in your answer would you investigate first with real evidence? Whose sign-off does your decision need, and what do they need to see? What early-warning signal would tell you your chosen path is failing?

## CS-097 — Culture vs. Controls
**Reference position.** Resolution: (1) workflow redesign *with* clinical staff — the 14-interruptions/hour data says the session-sharing is a workaround for a real design gap (shared emergencies need shared access: role-based *shared-workstation fast-user-switching* with proximity badge (tap = 2-second identity), per-action audit (who did what — the actual clinical-governance need), (2) technology: badge-tap unlock (cost justified by the two defeated enforcement attempts), (3) governance: clinical governance owns the policy (security advises); the memo-era relationship repaired via a joint walkthrough of the ward's actual rhythms, (4) the audit trail *protects staff* in incidents (attribution is exculpatory too — lead with that).
**Assumptions.** That badge infrastructure cost is fundable (build the case from the two defeated attempts); that clinical governance has authority (engage, don't route around).
**Discussion.** Why did the memo make things worse? What does "security as clinical safety" change in the pitch?

**Model solution (reference position — one defensible answer among several).** See the reference position above; the graded standard is the *quality of argument*, not convergence with this position.

**Expected reasoning.** Strong responses sequence: evidence inventory → assumptions made explicit → option generation (≥ 3) → evaluation against the scenario's constraints → decision with named residuals. Weak responses jump to a tool or a policy without the option space.

**Alternatives.** Because Level 4 cases are open-ended, the alternatives *are* the other defensible positions generated in class discussion; the instructor should surface at least two that differ structurally from the reference position (not merely re-parameterizations) and compare their risk/cost/feasibility profiles.

**Tradeoffs.** The reference position's named costs stand; push groups to name what their own preferred option sacrifices, and which stakeholder absorbs each cost.

**Common mistakes.** Solving the stated problem while ignoring the scenario's second-order constraint; inventing facts not in evidence; treating "defensible" as "unfalsifiable" (a position with no failure condition is not an analysis); missing that several of these cases make an *organizational* failure the root cause rather than a technical one.

**Discussion prompts.** Which assumption in your answer would you investigate first with real evidence? Whose sign-off does your decision need, and what do they need to see? What early-warning signal would tell you your chosen path is failing?

## CS-098 — The University Research Cloud
**Reference position.** Platform strategy: (1) tiered catalog: Public (self-service, minutes), Internal (day onboarding, standard guardrails), Restricted (templated secure enclaves: PII/encrypted/compute-isolated, week onboarding), Export-controlled (physically/logically separated, dedicated process) — control inheritance baked into templates so "restricted" is a *configuration*, not a negotiation, (2) fast path honesty: the 3-week friction was mostly manual security review — replace with templated pre-approved patterns + exception process only for non-standard, (3) monitoring for shadow: egress/DNS/cloud-account discovery program (researchers currently on personal accounts get *amnesty + migration*, not punishment — they're the design feedback), (4) governance: DPO/export-officer pre-approve the *templates* (not each project) — approvals scale, projects flow.
**Assumptions.** That templates can be pre-approved by DPO/export-control (engage early — this is the whole strategy); that GPU capacity reality matches the demand (if not, the platform loses regardless of security).
**Discussion.** What would you do about the researcher who *refuses* templates? Where does academic freedom meet data protection in this design?

**Model solution (reference position — one defensible answer among several).** See the reference position above; the graded standard is the *quality of argument*, not convergence with this position.

**Expected reasoning.** Strong responses sequence: evidence inventory → assumptions made explicit → option generation (≥ 3) → evaluation against the scenario's constraints → decision with named residuals. Weak responses jump to a tool or a policy without the option space.

**Alternatives.** Because Level 4 cases are open-ended, the alternatives *are* the other defensible positions generated in class discussion; the instructor should surface at least two that differ structurally from the reference position (not merely re-parameterizations) and compare their risk/cost/feasibility profiles.

**Tradeoffs.** The reference position's named costs stand; push groups to name what their own preferred option sacrifices, and which stakeholder absorbs each cost.

**Common mistakes.** Solving the stated problem while ignoring the scenario's second-order constraint; inventing facts not in evidence; treating "defensible" as "unfalsifiable" (a position with no failure condition is not an analysis); missing that several of these cases make an *organizational* failure the root cause rather than a technical one.

**Discussion prompts.** Which assumption in your answer would you investigate first with real evidence? Whose sign-off does your decision need, and what do they need to see? What early-warning signal would tell you your chosen path is failing?

## CS-099 — The Resignation of the Only Expert
**Reference position.** 4-week plan: (1) week 1: ruleset export + annotation sprint (the engineer narrates while a junior drives — recorded; 60% unknown-owner rules get best-effort attribution), (2) the 3 orphan-critical rules: identify the protected system via traffic analysis (what do these rules *shield*?), document, assign owner, (3) incident-during-notice contingency: named escalation path to the engineer (contractual consultation clause if willing — paid), vendor TAC engagement pre-authorized, and a second engineer starts cross-training immediately (not after departure), (4) long-term fix: documentation-as-code (rulesets in git with annotations), bus-factor policy (no critical system with N<2 knowledgeable people), hiring plan. The exit interview question that matters: "what would you not have time to tell us?"
**Assumptions.** That the engineer cooperates professionally (notice-period obligations + goodwill — do not make this adversarial); that the competitor relationship stays clean (legal check on solicitation, low value here).
**Discussion.** What made knowledge concentrated for 12 years — and what *systemically* prevents the next concentration? What do you *owe* the departing engineer?

**Model solution (reference position — one defensible answer among several).** See the reference position above; the graded standard is the *quality of argument*, not convergence with this position.

**Expected reasoning.** Strong responses sequence: evidence inventory → assumptions made explicit → option generation (≥ 3) → evaluation against the scenario's constraints → decision with named residuals. Weak responses jump to a tool or a policy without the option space.

**Alternatives.** Because Level 4 cases are open-ended, the alternatives *are* the other defensible positions generated in class discussion; the instructor should surface at least two that differ structurally from the reference position (not merely re-parameterizations) and compare their risk/cost/feasibility profiles.

**Tradeoffs.** The reference position's named costs stand; push groups to name what their own preferred option sacrifices, and which stakeholder absorbs each cost.

**Common mistakes.** Solving the stated problem while ignoring the scenario's second-order constraint; inventing facts not in evidence; treating "defensible" as "unfalsifiable" (a position with no failure condition is not an analysis); missing that several of these cases make an *organizational* failure the root cause rather than a technical one.

**Discussion prompts.** Which assumption in your answer would you investigate first with real evidence? Whose sign-off does your decision need, and what do they need to see? What early-warning signal would tell you your chosen path is failing?

## CS-100 — The Capstone Dilemma
**Reference position (one defensible strategy among several).** 12-month strategy, 5 funded programs: (1) **Visibility & IR baseline** (months 1–4): SIEM on existing logs, MTTD/MTTR instrumentation, IR runbook + tabletop — the board's "never again" needs *detection*, and logs exist, (2) **Exposure & patching program**: the 400-finding backlog triaged by exposure-weighted model (CS-083), exposed-criticals first, (3) **Identity & access**: MFA everywhere, JIT admin, offboarding fix — cheapest incident-class reduction, (4) **Team & culture rebuild**: replace the shame-program with reporting-culture design; hire 2 (analyst + platform) — 3 burned-out FTE cannot hold the above, (5) **Third-party minimum**: Tier-1 vendor classification + SSO. Deferred (3): full data-governance program (partial via identity work), IoT/OT program (interim: discovery + containment), certification ambitions (ISO/SOC2 — the 6-month auditor gets *evidence of operation*, not a certificate; say so plainly). Board narrative: "never again" honestly = "detect in hours, not months; prove it with exercises" — the trauma-driven alternative (promise prevention) is indefensible and sets up the next breach. Budget narrative maps each program to incident-classes it prevents/detects.
**Assumptions to surface.** That the board accepts deferrals (the auditor-scope overlap helps); that hiring happens (if not, programs 1–3 shrink honestly).
**Discussion.** What would *you* defer and why — defend a different five? What is the first thing you do in week 1, and what does it signal to the team of 3?

**Model solution (reference position — one defensible answer among several).** See the reference position above; the graded standard is the *quality of argument*, not convergence with this position.

**Expected reasoning.** Strong responses sequence: evidence inventory → assumptions made explicit → option generation (≥ 3) → evaluation against the scenario's constraints → decision with named residuals. Weak responses jump to a tool or a policy without the option space.

**Alternatives.** Because Level 4 cases are open-ended, the alternatives *are* the other defensible positions generated in class discussion; the instructor should surface at least two that differ structurally from the reference position (not merely re-parameterizations) and compare their risk/cost/feasibility profiles.

**Tradeoffs.** The reference position's named costs stand; push groups to name what their own preferred option sacrifices, and which stakeholder absorbs each cost.

**Common mistakes.** Solving the stated problem while ignoring the scenario's second-order constraint; inventing facts not in evidence; treating "defensible" as "unfalsifiable" (a position with no failure condition is not an analysis); missing that several of these cases make an *organizational* failure the root cause rather than a technical one.

**Discussion prompts.** Which assumption in your answer would you investigate first with real evidence? Whose sign-off does your decision need, and what do they need to see? What early-warning signal would tell you your chosen path is failing?
