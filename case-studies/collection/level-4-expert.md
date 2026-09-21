# Case Collection — Level 4: Expert (CS-076–100)

> Simulated teaching scenarios; all organizations, people, and data are fictional. Level 4 cases are open-ended: multiple defensible strategies exist, evidence is incomplete on purpose, and the discussion of *assumptions and limitations* is the assessment. Solutions: instructor-only tier.

---


## CS-076 — The Zero-Day You Cannot Patch
**Difficulty:** Level 4 · **Domain:** Vulnerability prioritization / IR · **Time:** 12 min · **CLO:** 2, 7

**Scenario.** A vulnerability in your edge VPN appliance is disclosed; the vendor has no patch ("6 weeks"). Exploitation is observed in the wild against other organizations. You have 3,000 remote staff on it. Telemetry: the appliance logs only success/failure, not payloads.

**Stakeholders.** Remote staff (productivity); CISO; the vendor; the board.

**Available evidence.** No patch; active exploitation ecosystem; limited appliance telemetry; measured VPN dependence (89% of staff need it daily); possible mitigations (WAF in front? restrict to managed devices? jump-host pattern?).

**Student task.** Produce the interim-risk plan with named mitigations, their costs, and the decision tree for "what if we see exploitation here."

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-077 — Crypto-Agility on Deadline
**Difficulty:** Level 4 · **Domain:** Cryptography & data protection · **Time:** 12 min · **CLO:** 5, 7

**Scenario.** A quantum-computing milestone announcement (fictional but plausible-sounding) makes your board demand a "harvest-now-decrypt-later" risk assessment for 10 years of archived data. Your inventory: TLS 1.2+1.3 in transit; AES-256 at rest; RSA-2048 signatures on 5 years of archived artifacts; no crypto inventory beyond that.

**Stakeholders.** Board; security architecture; the archive owners; auditors.

**Available evidence.** Inventory gaps; data-sensitivity classes in the archive; retention periods (up to 10 years); migration cost estimates for PQC signature schemes (performance-heavy).

**Student task.** Write the risk memo: what is actually at risk (signature long-term integrity vs. confidentiality), the inventory program, and a phased migration plan with defensible priorities.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-078 — The Side Channel in Production
**Difficulty:** Level 4 · **Domain:** Cryptography · **Time:** 12 min · **CLO:** 5

**Scenario.** Researchers (responsible disclosure to your team — fictional) demonstrate a timing side channel against your API's token-verification path: response-time distribution leaks whether a token prefix is valid. Exploitation requires ~10⁶ requests; you serve 10⁸/day.

**Stakeholders.** The researchers; the API team; customers (latency SLO); security.

**Available evidence.** Constant-time fix available but costs 15% latency; alternative: rate-limit + noise (partial mitigation); the secret is a *verification* path (mitM required first); disclosure timeline running.

**Student task.** Choose the remediation path and the disclosure response; defend the latency tradeoff to the SLO owner.

---

Safety notes. Simulated scenario for classroom discussion. Any demonstration the instructor chooses to stage runs only on course-owned loopback targets; students never interact with real systems for this case.

---

## CS-079 — Framework on Fire
**Difficulty:** Level 4 · **Domain:** Secure web applications / IR · **Time:** 12 min · **CLO:** 2, 7

**Scenario.** A critical RCE lands in the web framework all 30 of your services use. Patch available but changes session format (all users logged out). Two services are PCI-scoped (change freeze in 48 hours for audit). Exploitation observed in the wild.

**Stakeholders.** 30 service teams; PCI compliance; users (sessions drop); security.

**Available evidence.** Patch + session-format break; freeze window; observed exploitation elsewhere; virtual-patch option at the WAF (imperfect); 12 services internet-exposed.

**Student task.** Sequence the rollout (who patches first, what virtual patch covers, how the freeze is handled), and decide the user-communication for forced logouts.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-080 — The Host Header
**Difficulty:** Level 4 · **Domain:** Secure web applications · **Time:** 12 min · **CLO:** 2

**Scenario.** Bug-bounty report (fictional program): password-reset links are generated using the attacker-controllable `Host` header, so a crafted request sends a victim a reset link pointing at the attacker's domain. The app team says "the reverse proxy should normalize that"; the platform team says "the app should use configured base URLs."

**Stakeholders.** The reporter; app team; platform team; users receiving crafted mails.

**Available evidence.** Confirmed behavior; two teams with plausible ownership; fix on either side works; proxy config affects 40 apps (blast radius); the reporter's deadline for publication.

**Student task.** Decide the fix location (defense in depth answer expected: both, prioritized), the ownership resolution, and the coordinated disclosure plan.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-081 — The Token That Lives Forever
**Difficulty:** Level 4 · **Domain:** API security · **Time:** 12 min · **CLO:** 2, 7

**Scenario.** Your mobile app's API tokens never expire (2M active devices). Rotation plan proposed: version tokens, force re-auth on old versions via API response. Risk: 400k devices run an app version 3 years old that ignores the header. You cannot force-update them.

**Stakeholders.** App team; 400k legacy-device users; security; support (call volume).

**Available evidence.** Token inventory; version distribution; the old version's behavior (ignores kill headers); revocation option exists but bricks old devices.

**Student task.** Design the migration strategy (server-side enforcement vs. brute revocation vs. proxy-layer checks) with the user-impact and support-cost analysis.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-082 — BOLA Across Tenants
**Difficulty:** Level 4 · **Domain:** API security · **Time:** 12 min · **CLO:** 2

**Scenario.** Pentest (authorized, fictional) finds: `GET /api/v2/documents/{id}` returns any tenant's document with a valid token from any tenant. ID space is UUID (not sequential) — the tester found leakage via a *response inconsistency* (404 vs 403 timing). Millions of documents; UUID enumeration infeasible, but search-by-title endpoint leaks IDs cross-tenant.

**Stakeholders.** Customers (all tenants); the API team; the pentest firm; legal (contractual security terms).

**Available evidence.** The two endpoints involved; fix requires tenant-scoping middleware (architectural); contractual breach likely; no evidence of third-party exploitation (logs).

**Student task.** Produce the incident-vs-vulnerability decision, the remediation architecture, and the customer-notification analysis (if treated as incident).

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-083 — Prioritization Under Protest
**Difficulty:** Level 4 · **Domain:** Vulnerability prioritization · **Time:** 12 min · **CLO:** 2, 7

**Scenario.** You must cut the remediation backlog by 60% (headcount). The proposed model (severity × exposure × exploitability × business criticality) demotes many findings the loudest team owner calls "critical." One demoted finding later becomes the incident (fictional outcome, presented at the case's end as a governance question).

**Stakeholders.** The model's designers; team owners; the CISO; the auditor.

**Available evidence.** The model; the protest pattern; the eventual incident's finding profile (was demoted correctly *by the model's stated criteria* — the criteria were incomplete, not misapplied).

**Student task.** Redesign the model's criteria (what was missing: e.g., blast-radius interconnection, threat-actor targeting data), and design the exception process that lets owners contest *with evidence*.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-084 — The Sensor That Lies
**Difficulty:** Level 4 · **Domain:** Security monitoring · **Time:** 12 min · **CLO:** 6

**Scenario.** Your EDR fleet's telemetry shows a strange pattern: on 4% of hosts, process-creation events arrive in bursts 20 minutes late. During an actual incident, this means the attack graph is temporally scrambled for those hosts. Vendor confirms a bug "in a future release." The 4% are your finance servers.

**Stakeholders.** SOC; the vendor; finance; the incident commander mid-case.

**Available evidence.** Delay pattern; vendor roadmap; network-based sensors cover the same segment (different visibility); incident in progress.

**Student task.** Design the compensating detection for the affected segment *now* (network-side) and the trust model for sensor data generally (how would you have detected the sensor lying?).

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-085 — Detection Debt
**Difficulty:** Level 4 · **Domain:** Security monitoring · **Time:** 12 min · **CLO:** 6

**Scenario.** Five years of SOC work produced 2,400 rules. 400 have never fired; 90 fire only FPs; 60 have broken silently (log schema changed 2 years ago). No tests exist. New CISO asks: "which rules would I bet the company on?"

**Stakeholders.** SOC engineers; the CISO; rule authors (some departed); management.

**Available evidence.** Rule census with fire-history; schema-change timeline; purple-team capability (can generate test events); engineer capacity (2 people, 20% time).

**Student task.** Design the detection-debt reduction program (triage, testing-as-code, retirement criteria, coverage measurement) with a defensible 6-month plan.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-086 — The Phantom Admin
**Difficulty:** Level 4 · **Domain:** Digital forensics / IR · **Time:** 14 min · **CLO:** 3, 7

**Scenario.** Forensic examination finds an admin account created 3 years ago, used "occasionally," never in HR records. Candidates: (a) attacker persistence (3 years undetected — unusual but not impossible), (b) forgotten legitimate account (contractor? script?), (c) former employee retained access. Logs for creation are beyond retention; usage logs exist for 12 months.

**Stakeholders.** The CISO (what does this say about our controls?); legal; IT operations; the current IR case that surfaced it.

**Available evidence.** Creation beyond log retention; usage pattern (monthly, 3 a.m.-ish, consistent source IP — a datacenter, not residential); naming convention matches old contractor scheme; no owner found in records.

**Student task.** Assess the three hypotheses with likelihoods and the evidence you'd seek to discriminate; decide containment vs. preservation for the account; state what the case says about identity-governance gaps.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-087 — Attribution Pressure
**Difficulty:** Level 4 · **Domain:** Digital forensics / governance · **Time:** 12 min · **CLO:** 3, 7

**Scenario.** After a significant intrusion, the board demands to know "who did it" before the press conference. The evidence suggests a financially motivated crew (tooling matches a known RaaS affiliate pattern), but the board wants a nation-state narrative (more "defensible" to investors). Your analysts are confident but not certain.

**Stakeholders.** Board; analysts; legal; insurers; possibly law enforcement.

**Available evidence.** Tooling/TTP overlap with a named (public) affiliate program; no geo-political indicators; attribution confidence levels properly assessed as "moderate"; the board's narrative preference.

**Student task.** Draft the board's answer (what you can and cannot claim), the confidence-language standard you use, and the risk of narrative capture in your incident comms.

---

Safety notes. Simulated scenario for classroom discussion. Any demonstration the instructor chooses to stage runs only on course-owned loopback targets; students never interact with real systems for this case.

---

## CS-088 — Landing Zone From Chaos
**Difficulty:** Level 4 · **Domain:** Cloud security · **Time:** 14 min · **CLO:** 7

**Scenario.** Migrating 200 workloads to cloud in 9 months. Options: (a) lift-and-shift into the current account structure (fast, carries the chaos), (b) design a landing zone first (6-week delay, teams angry), (c) hybrid: landing zone for new workloads, remediate old in place.

**Stakeholders.** Migration program office; 12 app teams; security; finance (egress costs).

**Available evidence.** Workload criticality mix; current account chaos (documented in CS-062's scenario); the 9-month commitment; the security guardrails the landing zone would bake in (logging account, SCPs, network baseline).

**Student task.** Choose and defend the strategy; specify the 5 non-negotiable guardrails regardless of choice; design the migration-ordering logic (what moves first and why).

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-089 — The Cloud Key That Saw Everything
**Difficulty:** Level 4 · **Domain:** Cloud security · **Time:** 12 min · **CLO:** 7

**Scenario.** Post-incident review (fictional): a compromised CI pipeline used its role to read a secrets bucket, which held keys for 14 production systems. Each key had "least privilege" *within its own system* — but the bucket aggregated them. Individually least-privilege, collectively admin.

**Stakeholders.** All 14 system owners; the platform team; security architecture; auditors.

**Available evidence.** The bucket's role as aggregation point; per-system key hygiene (good); no segmentation on the bucket; audit trail complete (who read what when).

**Student task.** Redesign secret distribution (brokered access, short-lived credentials, per-consumer vault paths) and define "least privilege" at the *portfolio* level, not per-key.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-090 — The Firmware You Cannot See
**Difficulty:** Level 4 · **Domain:** IoT & wireless security · **Time:** 12 min · **CLO:** 4, 7

**Scenario.** A building-management vendor refuses to provide firmware images or SBOMs ("trade secret") for 300 controllers running HVAC across campus. The controllers are networked, update over HTTP (unsigned), and the vendor's answer to vulnerabilities is "we'll tell you when we tell you."

**Stakeholders.** Facilities (they just want heating); security; the vendor; the university's research mission (the buildings include labs).

**Available evidence.** Update mechanism unsigned (tamperable); no SBOM; refusal of transparency; the controllers' network reachability; contract renewal in 8 months.

**Student task.** Design the treatment plan you can execute *without vendor cooperation* (network containment, update-path interception with verification, monitoring), and the contract-leverage strategy for renewal.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-091 — Rogue AP Geometry
**Difficulty:** Level 4 · **Domain:** IoT & wireless security · **Time:** 12 min · **CLO:** 4

**Scenario.** Users report intermittent credential prompts near one building. Survey finds an AP matching the corporate SSID but stronger signal, MAC not in inventory. It moves between floors weekly (mobile — a person, not an install). Corporate policy: never enter credentials outside the portal's exact domain.

**Stakeholders.** The users being harvested; the physical-security team; IT; the person doing it (fictional — could be theft-motivated or research-curious).

**Available evidence.** Mobile AP behavior; harvesting design; client-side policy exists but is not enforced technically (users type passwords anyway); 802.1X is deployed for staff but the SSID also runs PSK for guests.

**Student task.** Design the hunt (detection, localization, legal/HR interface) and the architectural fix that removes the harvestable credential class (why does PSK-on-the-same-SSID break the story?).

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-092 — The Data Poisoning Audit
**Difficulty:** Level 4 · **Domain:** AI security / Data Science · **Time:** 14 min · **CLO:** 6, 7

**Scenario.** Your fraud model's quarterly review shows performance drift on one segment (transactions from one region). Root-cause analysis reveals: merchants in that region can self-report "chargeback resolved" events, which feed the labels. A merchant cartel (fictional) has learned to self-confirm frauds as "resolved" to keep them out of training data, keeping their fraud scores low.

**Stakeholders.** The fraud team; legitimate merchants in the region; the cartel (fictional); customers who absorb fraud losses.

**Available evidence.** Drift localized to label source; self-report mechanism; no second label source; the model's regional importance; retraining pipeline automated.

**Student task.** Design the remediation: label-source diversification, poisoning detection on label streams, the model-rollback decision, and how you would have detected this *earlier* (what monitor was missing?).

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-093 — Privacy Budget Exhausted
**Difficulty:** Level 4 · **Domain:** Data Science security / privacy · **Time:** 12 min · **CLO:** 6, 7

**Scenario.** A university publishes a "differentially private" dataset of student outcomes monthly. A researcher's repeated queries (they are a legitimate user) have consumed 90% of the privacy budget for the semester; the remaining releases will be so noisy they are useless; the researchers revolt; the DPO notes the budget was set arbitrarily.

**Stakeholders.** Researchers; students (whose privacy the budget protects); the DPO; the university's research mission.

**Available evidence.** Budget mechanics (epsilon accounting); the 90% consumption; the noise-utility tradeoff now binding; arbitrary initial parameter; alternative: per-query budgeting, or trusted-curator model.

**Student task.** Decide the semester's path (stop releases? re-parameterize with justification? move to per-user quotas?) and design the parameter-setting process that is defensible *both* statistically and to a DPO.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-094 — The Synthetic Cover-Up
**Difficulty:** Level 4 · **Domain:** Data Science security / governance · **Time:** 12 min · **CLO:** 6, 7

**Scenario.** A team claims their training data is "fully synthetic, no privacy risk." Audit finds: the generator was trained on real records; synthetic outputs occasionally reproduce rare real-record combinations (a documented property of generative models); the team didn't measure membership-inference risk and calls the audit "obstruction."

**Stakeholders.** The team; the DPO; the model's users; the individuals in the source data.

**Available evidence.** Generator lineage (real-data trained); rare-combination reproduction demonstrated; no MIA testing; the team's governance resistance; deployment timeline pressure.

**Student task.** Design the technical audit (MIA test plan, distance-to-closest-record metrics) and the governance resolution — is "synthetic" a magic word, and what standard should the university adopt?

---

Safety notes. Simulated scenario for classroom discussion. Any demonstration the instructor chooses to stage runs only on course-owned loopback targets; students never interact with real systems for this case.

---

## CS-095 — Third-Party Breach, First-Party Data
**Difficulty:** Level 4 · **Domain:** Governance & risk · **Time:** 12 min · **CLO:** 7

**Scenario.** Your HR SaaS vendor is breached (fictional): attackers exfiltrate all customer tenants' data, including your employees' salaries, home addresses, and bank details. Your contract's liability cap is 12 months of fees. Employees ask you — not the vendor — what happened to their data.

**Stakeholders.** Your employees; the vendor; your board; your insurer; the regulator (your employees' data, your responsibility?).

**Available evidence.** Vendor breach confirmed; your data classes; contract terms (cap, notification duty, audit rights unused); your third-party risk program (this vendor was Tier 2, assessed by questionnaire only).

**Student task.** Produce the response plan (notification duty analysis — whose obligation is it?, employee support, vendor remedy), and the third-party program redesign (what makes a vendor Tier 1?).

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-096 — The Board Wants a Number
**Difficulty:** Level 4 · **Domain:** Governance & risk management · **Time:** 12 min · **CLO:** 7

**Scenario.** The board demands "our cyber risk in euros, annually." You know: loss-exceedance curves require data you don't have; credible interval estimates span two orders of magnitude; a single number invites false precision and false comfort. The board is sophisticated but impatient.

**Stakeholders.** The board; the CISO (you); risk management; internal audit.

**Available evidence.** Industry loss data (public reports, coarse); your own incident history (5 years, small counts); control-maturity self-assessment (biased); FAIR-class methodology training available.

**Student task.** Design the answer: the estimation methodology (ranges, not points), the communication format, and the two measurements you will start collecting so next year's number is better.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-097 — Culture vs. Controls
**Difficulty:** Level 4 · **Domain:** Governance & risk · **Time:** 12 min · **CLO:** 7

**Scenario.** A hospital ward's staff consistently share one workstation session "because emergencies don't wait for logins." Technical enforcement (auto-lock 60s) was deployed and defeated twice (registry hacks, mouse-jigglers). Patient care is genuinely time-critical; the security team's memo made things worse.

**Stakeholders.** Ward staff (patient outcomes); patients (privacy and care); security; clinical governance.

**Available evidence.** Two enforcement defeats; clinical workflow reality (measured: 14 interruptions per nurse per hour); proximity-badge option cost; the failed-memo history.

**Student task.** Design the resolution: what workflow change, what technology, what governance — and how you rebuild the relationship after the memo.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-098 — The University Research Cloud
**Difficulty:** Level 4 · **Domain:** Cloud security / governance · **Time:** 14 min · **CLO:** 7

**Scenario.** Researchers demand: GPU clusters, custom images, admin rights on their VMs, and the freedom to install anything — while processing grant data with protection requirements (personal data, export-controlled datasets). The current shared platform "is too slow for research." Blocking research means losing grants; the controls exist but slow onboarding from weeks to months.

**Stakeholders.** Researchers; grant funders; the DPO; export-control officer; IT; ethics committees.

**Available evidence.** Workload taxonomy (public, internal, restricted, export-controlled); measured platform friction (3-week onboarding); researcher attrition to personal cloud accounts (shadow IT occurring *now*); the funding at stake.

**Student task.** Design the platform strategy that satisfies both constituencies: tiered service catalogs, control inheritance, the fast path for low-risk work, and the monitoring that finds research that *doesn't* use the platform.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-099 — The Resignation of the Only Expert
**Difficulty:** Level 4 · **Domain:** Governance & risk · **Time:** 12 min · **CLO:** 7

**Scenario.** Your sole firewall engineer — 12 years of tenure, all rulesets in his head, documentation "in his own style," resignation effective in 4 weeks — leaves for a competitor. Half the rules have unknown owners; three rules protect a system nobody can name. An incident mid-notice-period would need him.

**Stakeholders.** The engineer (professional obligations); the team; the CISO; the unknown system's owners; the competitor (ethically bound?).

**Available evidence.** Documentation audit results (60% rules owned, 3 orphan-critical, 12 unknown-purpose); notice period; knowledge-transfer plan template that doesn't exist yet; non-compete clause (unenforceable in this jurisdiction).

**Student task.** Design the 4-week plan (knowledge capture prioritization, the three orphan-critical rules, the incident-during-notice contingency) and the long-term fix (why did one person hold all this?).

---

Safety notes. Simulated scenario for classroom discussion. Any demonstration the instructor chooses to stage runs only on course-owned loopback targets; students never interact with real systems for this case.

---

## CS-100 — The Capstone Dilemma
**Difficulty:** Level 4 · **Domain:** Governance & risk (capstone synthesis) · **Time:** 15 min · **CLO:** 8, all supporting

**Scenario.** You are the newly hired security lead of a fictional mid-size company (600 staff, cloud-first, one breach 2 years ago, board trauma from it). You inherit: a security team of 3 (burned out), a 400-finding backlog, no SIEM (logs exist, unwatched), an awareness program that shames users, a CISO mandate of "never again" — and a budget request deadline in 10 days. Everything cannot be fixed at once.

**Stakeholders.** The board; your team of 3; every employee; the customers; the auditor arriving in 6 months.

**Available evidence.** Full inventory (as listed); the board's trauma-driven priorities (visibility first? prevention first?); team capacity (measured: 3 FTE); the budget template with categories; the auditor's scope.

**Student task.** Produce the 12-month security strategy: the 5 programs you fund, the 3 you explicitly defer (with risk acceptance), the team-structure change, and the board narrative. Defend every deferral.

---

*Model solutions and instructor material: `instructor-materials/instructor-only/case-solutions/level-4-solutions.md`.*

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---
