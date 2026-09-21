# ⚠️ INSTRUCTOR-ONLY — Level 2 Model Solutions (CS-021–045)

Reveal at step 5. Each solution: model answer, expected reasoning, alternatives, tradeoffs, common mistakes, discussion prompts.

## CS-021 — The Breach-Corpus Check
**Model solution.** The control is partially working: it blocks known-bad passwords (0.3% direct hits) but the deterministic replacement patterns (password1!) show users *migrate along predictable paths* — so the blocklist needs substitution-awareness, not raw-list matching. Recommend: keep blocklist + add MFA enforcement (the structural fix) + measure *replacement strength*, not just block rate.
**Reasoning.** A control's success metric must capture user adaptation, not the control's own hit count.
**Alternatives.** Drop composition rules entirely (800-63B direction) and lean on blocklist+MFA; passphrase education.
**Tradeoffs.** Smarter blocklist = maintenance; MFA = friction; measuring replacements = analytics pipeline.
**Common mistakes.** Declaring success on the 0.3% metric; removing the control because of complaints.
**Prompts.** Why do deterministic replacements matter more than the blocked ones? Who should own the replacement-pattern analysis — identity team or security?

## CS-022 — Passkeys for the Helpdesk
**Model solution.** The weak point moved from passwords to the *recovery path*: desk resets on voice request = account-takeover channel. Minimal desk procedure: identity verification standard (two-factor: known-person vouch + callback to registered number; never reset on a single voice call), plus passkey re-enrollment requires the old device or the verified path. The pilot's technical success hides the process hole.
**Reasoning.** Any strong authentication is only as strong as its weakest recovery flow.
**Alternatives.** Temporarily slow-roll passkeys until the desk procedure exists (delay value); keep passwords for a subset.
**Tradeoffs.** Verification procedure = support latency; slower rollout = less data on real adoption.
**Common mistakes.** Blaming users' new phones (the platform-lock-in issue is real but *manageable*); missing that voice-reset was pre-existing — passkeys just raised its value.
**Prompts.** Why does a strong primary factor raise the recovery path's value? What would you measure in the pilot's next phase?

## CS-023 — The CEO's Signature Style
**Model solution.** Verification step: *out-of-band* payment-detail verification — call the vendor on a number from the *master file* (not the mail), dual approval for any bank-detail change, cooling rule (no same-day new-recipient payments). If the MD is genuinely unavailable, the payment waits — the process must not have a bypass that urgency exploits. Teaching staff "verify unusual requests" fails without a *norm that verification is respectful*.
**Reasoning.** Authentication of the mailbox passed; the *content* is the attack; process controls own content.
**Alternatives.** Technical: payment-platform beneficiary-locking (new accounts require 24h+multi-approval).
**Tradeoffs.** Slight payment delay vs. fraud loss; vendor relationships absorb one verification call fine.
**Common mistakes.** DMARC-style technical answers (the mailbox is real); shame-based training ("check everything!" without workflow).
**Prompts.** Why does the master-file callback work where replying-to-the-mail fails? Who owns the cooling rule — finance or security?

## CS-024 — The Helpful New Colleague
**Model solution.** Script: "I'm not able to share credentials — let me connect you with the IT service desk, they'll set you up properly," + the desk authenticates via ticket/ID, not phone claims. Boundary: credentials are never disclosed verbally; the *authentication boundary* is the service desk's verified process.
**Reasoning.** Social engineering exploits helpfulness norms; the fix is a norm-compatible script, not suspicion training.
**Alternatives.** Manager-vouching (weak — attackers use real names); technical: rotate Wi-Fi PSK regularly + 802.1X (structural).
**Tradeoffs.** Slight awkwardness per call vs. staff-network exposure; 802.1X deployment cost.
**Common mistakes.** Training "be suspicious" (fights the culture you need for reporting); ignoring that public team pages fuel pretexting.
**Prompts.** Should the team page list names at all? How does the script help the *receptionist* (who bears the social cost of refusal)?

## CS-025 — The Summer of Flat Network
**Model solution.** Minimal segmentation: three zones (students / servers / lab-infrastructure), two rules that matter most: (1) deny student→server SMB, (2) deny zone→zone default with explicit server-access allow-list. With this design the worm dies at the first hop: student laptop → other students only; servers unreachable via SMB even with stolen credentials.
**Reasoning.** Blast-radius design: the worm's propagation pattern (SMB + creds) defines which rule is load-bearing.
**Alternatives.** Full NAC/deployment (overkill before term); host firewalls only (management burden at 40 PCs).
**Tradeoffs.** Some student-server workflows need explicit rules (map them first!); switch config effort.
**Common mistakes.** Designing zones without the must-work list (breaking lab workflows); trusting "the worm would need credentials" — the case says reuse is its pattern.
**Prompts.** Which must-work flow would you discover *only* after the segmentation ships? How do you test before students arrive?

## CS-026 — The Guest That Wasn't
**Model solution.** Containment: (1) re-isolate the AP (undo the bridging config), (2) audit *all* APs from the upgrade window (same change = same error class), (3) check guest-segment logs for what the bridging actually exposed (reachability evidence), (4) notify FINANCE printer's owner to rotate its management credentials if reachable. Change-control gap: post-change verification didn't test *isolation*, only *function* (guests could connect = pass; guests could only see guests = not tested).
**Reasoning.** The same misconfiguration is probably fleet-wide; verification must test the security property, not the feature.
**Alternatives.** Automated isolation-testing in change process (long-term fix).
**Tradeoffs.** Audit effort vs. unknown exposure duration.
**Common mistakes.** Fixing one AP; treating the guest report as the whole blast radius.
**Prompts.** What does "test the security property" mean concretely in your change checklist? Who owns guest-network design?

## CS-027 — Seven Years of Updates
**Model solution.** Risk-acceptance package: move the PC to an instrument-only zone (no staff network), allow-list its exact flows (USB instrument → PC → one share path), monitor its tiny traffic baseline (anything else = alert), credential hygiene (no interactive login reuse), documented acceptance with *annual* review and a trigger for re-assessment ("if the instrument needs internet, this changes"). Stop accepting when: the share it writes holds higher-class data, or the OS gets network-reachable exploit class.
**Reasoning.** Risk acceptance is a *managed state* — monitored, bounded, reviewed — not neglect.
**Alternatives.** Virtualization (host patched, guest frozen) — decent, vendor may still complain; replacement via vendor pressure.
**Tradeoffs.** Isolation = switch/effort; VM = support complexity; acceptance = documented exposure.
**Common mistakes.** Accepting without monitoring; accepting forever (no review trigger); banning outright without weighing research value.
**Prompts.** Who signs an acceptance like this, and what do they need to see? What would your monitoring alert on first?

## CS-028 — The Admin With Two Jobs
**Model solution.** Principles: separation of duties (production vs. recovery) and least privilege. Design for a small team: backup administration requires *different credentials* (separate identity, separate MFA token), production DBA cannot touch the backup plane; restore requests go through a second person (two-person integrity). In a 3-person team, split DBA/backup roles across people, not within one identity.
**Reasoning.** The phishing compromised *her* — role separation would have left backups outside the compromised identity's reach.
**Alternatives.** Immutable backups (attacker with any credential cannot delete) — arguably the stronger control for ransomware specifically.
**Tradeoffs.** Immutability = storage design; role split = staffing constraint.
**Common mistakes.** Fixing the phishing (MFA) and calling it done; separating roles on paper but with one human holding both passwords.
**Prompts.** Why does immutability beat role-splitting for this attack? What does the auditor ask for as evidence?

## CS-029 — Time-Boxed Admin
**Model solution.** Just-in-time access: standing role removed; developer requests elevation via ticket/self-service (reason + duration), approval automated for pre-approved scopes, session logged, auto-expiry (≤ 4h). Meets the speed objection (seconds, not weeks, for pre-approved scopes) and converts the audit finding into a monitoring artifact.
**Reasoning.** The usage data (20 min/week) proves standing access is over-provisioning by 99%+ of the time.
**Alternatives.** Break-glass accounts (for emergencies only, sealed + monitored); dedicated deploy role with narrow scope.
**Tradeoffs.** Platform build effort; approval friction for *novel* scopes.
**Common mistakes.** Building JIT with manual approvals (recreates the slowness); forgetting break-glass for real outages.
**Prompts.** What happens in a 3 a.m. production incident under JIT? What does the audit finding become after rollout?

## CS-030 — The Offboarding Gap
**Model solution.** Checklist classes: (1) infrastructure access (VPN, SSO, cloud IAM — revocation list per system), (2) credentials the person *owns* (API tokens, service accounts they created — inventory from logs, not memory), (3) vendor/business dependencies (payment methods, admin email addresses, contract owner contacts). Process: triggered by HR event; owner per item; verification step (try the old access — test, don't assume).
**Reasoning.** Three forgotten paths = three different ownership domains (IT, platform, finance); the checklist must span them.
**Alternatives.** SSO-everything (shrinks class 1); secrets-scanning for class 2.
**Tradeoffs.** Checklist maintenance vs. forgotten access; SSO migration is the structural fix with its own project cost.
**Common mistakes.** Laptop-and-badge-only checklists; assuming the leaver acts against you (most gaps are innocent — design for *all* cases anyway).
**Prompts.** Who signs the checklist's completion — HR or IT? How do you *find* access nobody remembers granting (log-based discovery)?

## CS-031 — Rotating the Shared Secret
**Model solution.** Today: treat the stolen key as compromised — rotate immediately (accept one re-encryption window), revoke old key, verify backup integrity, assess what the laptop's key could decrypt (all 3 years of exports). This quarter: rotation-without-downtime design — versioned keys (v1/v2 headers), write-new-with-v2, lazy re-encrypt on read or batch re-encrypt during off-peak, dual-key decryption window, then retire v1. Rehearse the rotation once before you need it for real.
**Reasoning.** Rotation fails when it's an emergency improvisation; versioning makes it a routine operation.
**Alternatives.** Per-export data keys wrapped by a master (envelope) — makes rotation a master-key operation only.
**Tradeoffs.** Lazy re-encryption = long dual-key window; batch = compute cost; envelope = design change.
**Common mistakes.** Rotating without a decryption plan for old data (data loss); "rotation later" without versioning (later never comes).
**Prompts.** What does the 3-year archive mean for the *value* of the stolen key? Who decides the re-encryption window?

## CS-032 — The Backup That Never Restored
**Model solution.** The dashboard measured *job success*, not *restorability*. Program: scheduled restore tests (quarterly full, monthly spot) with restore-time measurement, key-management separation (keys never colocate with backups alone — escrow/vault), offsite copy age alarm (RPO monitor), documented restore runbook. The fire scenario then becomes: keys available, offsite 1 day old, rehearsed runbook.
**Reasoning.** Untested backup = hypothesis; the test is the control.
**Alternatives.** Immutable cloud backup with independent account; managed BaaS.
**Tradeoffs.** Restore tests = environment cost + staff time; independence = account architecture.
**Common mistakes.** More dashboards instead of restore drills; testing only file-level restores (not full-system).
**Prompts.** What does "green" mean on your backup dashboard today? Who has *ever* done a full restore here?

## CS-033 — The Search That Returned Everything
**Model solution.** Fix: parameterized queries (the only structural fix) — reject the filter proposal: blacklists break valid inputs (O'Brien) and miss encoding variants; the sanitizer's over-sanitization already demonstrates blacklist failure. The directory page matters because the *same query code* serves it — fix at the shared data layer or both pages remain vulnerable; centralize correctly (parameterization) so all consumers inherit safety.
**Reasoning.** Input blacklisting is fighting encoding; output needs encoding, input needs parameterization — different tools for different jobs.
**Alternatives.** ORM parameter binding; least-privilege DB account as blast-radius control.
**Tradeoffs.** Refactor of ten routes = staged migration; test coverage per route.
**Common mistakes.** Believing the sanitizer is a security layer; fixing only the reported page.
**Prompts.** How do you *find* all consumers of a query pattern (code search, tests)? What does mojibake tell you about the sanitizer's design?

## CS-034 — The Login Form That Trusts the Browser
**Model solution.** Flaw class: broken access control / client-side trust (CWE-602 class). Fix: server-side authorization check on the invoice-request endpoint (the 12-line recompute); severity in context: medium — no personal data, but direct revenue/feature-integrity impact; the *class* would be critical if it gated anything sensitive.
**Reasoning.** Client-side checks are UX, not security; the server defines the trust boundary.
**Alternatives.** Signed client-side computations (complex, still server-verify); feature-flag on server.
**Tradeoffs.** 40 ms latency vs. free unlocks; report severity calibration (inflating to critical damages trust in reports).
**Common mistakes.** "Fix the JS variable" (bypassed forever); misjudging severity in context.
**Prompts.** What does the responsible-disclosure flow owe this student? Which other routes trust client state (audit question)?

## CS-035 — One API, Three Consumers
**Model solution.** Key architecture: per-consumer keys with least-privilege scopes (mobile: read+write-own, dashboard: read-public, partner: read-grades only), rotation mechanics (dual-key window per consumer), independent revocation. Migration order: partner first (least trusted, the leak source), then dashboard (low risk), then mobile (needs app release coordination).
**Reasoning.** Blast-radius isolation: one consumer's compromise must not force all consumers to rotate.
**Alternatives.** OAuth per-consumer clients (stronger, bigger migration); signed requests.
**Tradeoffs.** Key infra build vs. shared-key risk; mobile migration = release-cycle coupling.
**Common mistakes.** Rotating the shared key immediately (breaks everything at once); scoping partner keys by *asking partners* what they need (verify by usage logs).
**Prompts.** What did the usage logs say the partner actually called? Who owns consumer-key lifecycle?

## CS-036 — The Rateless Endpoint
**Model solution.** Flaws: (1) availability/abuse — no rate limit (fix: per-key/per-IP rate limits + caching); (2) confidentiality — response over-collection (`user_id` fields consumers don't need; fix: response-shaping per consumer/endpoint). Missing policy artifact: published terms of use / API policy (what automated access is permitted).
**Reasoning.** Good-faith mass access still creates the exposure; the fields are the confidentiality flaw, the limit is the availability one.
**Alternatives.** Auth-gating the endpoint; a dedicated bulk-export API for legitimate bulk needs.
**Tradeoffs.** Limits = friction for legit users; response-shaping = API versioning discipline.
**Common mistakes.** Treating scraping as the crime (policy gap is yours); removing fields without consumer impact analysis.
**Prompts.** When is bulk access *legitimate* (design for it rather than fight it)? What would you do about the already-scraped data?

## CS-037 — CVEs by Volume
**Model solution.** Rule: priority = severity × exploitability (public exploit/KEV?) × exposure (internet/internal). The exploited finding: medium severity but exposed + known exploit → *high priority* — above most unexposed criticals. Interim for unpatched exposed items: virtual patch/WAF rule, restrict access. Working rule for the team: "exposed + known-exploit = this sprint, regardless of severity number."
**Reasoning.** The month-late incident is the rule's proof: severity-first ordering is structurally wrong for risk.
**Alternatives.** KEV-catalog-driven patching (public evidence of exploitation); threat-intel feeds.
**Tradeoffs.** Model maintenance; stakeholder education (charts stop sorting by CVSS).
**Common mistakes.** Abandoning severity entirely (it still matters within equal exposure); no interim mitigation for deferred items.
**Prompts.** How do you explain to management why a medium outranks a critical? Where does asset-criticality data come from?

## CS-038 — The Dashboard of Shame
**Model solution.** Diagnosis: single-metric gaming (Goodhart). Replacement: (1) *quality-weighted* closure (sampled QA of closed alerts: enrichment present? verdict justified?) and (2) outcome metrics (missed-detection rate in purple-team tests), NOT raw counts. Plus: make auto-close visible (who closed, why) to keep speed honest.
**Reasoning.** Measure the behavior you want (accurate triage), not its byproduct (closures).
**Alternatives.** Team-level metrics (reduce individual gaming); remove the public leaderboard entirely.
**Tradeoffs.** QA sampling = lead-analyst time; outcome metrics = slow feedback.
**Common mistakes.** Adding more count metrics (more gaming surfaces); blaming analysts (the metric designed the behavior).
**Prompts.** Which metric would you show management and why? How does the leaderboard affect *reporting* of near-misses?

## CS-039 — The Alert Nobody Owned
**Model solution.** Ownership model: every recurring alert class has a named owner + disposition SLA + quarterly review (still true positive? still the right threshold?). Enrichment that separates exfil from job: transfer *destination* (known job target vs. new external), volume delta vs. the job's baseline, initiator identity (service account vs. user session). The nightly alert becomes two alerts: the job (auto-suppressed with justification) and any *other* transfer of that shape (high severity).
**Reasoning.** Baseline noise without ownership hides anomalies *inside* the pattern it normalizes.
**Alternatives.** Suppress-and-monitor-delta (alert only on deviation from baseline).
**Tradeoffs.** Delta monitoring = baseline math; suppression needs justification hygiene or it becomes a dump.
**Common mistakes.** "Someone should look at it" (no owner); killing the alert (removes the tripwire the attacker disguised himself within).
**Prompts.** What is the maintenance cost of suppression rules? Who reviews them, and how often?

## CS-040 — The Two-Hour Window
**Model solution.** Strategy: staged containment with evidence preservation — 02:40: isolate the confirmed server (VM network cut or switch ACL) but keep memory/storage intact (snapshot before shutdown; memory capture first if trained), 03:00: parallel — identify scope (which other servers share credentials/shares), 04:00: broader containment of *identified* systems rather than carpet-isolation; document each decision's options. Carpet-isolation at 02:40 destroys evidence on adjacent servers and business function without scope knowledge; isolation-only risks spread — the staged plan is the defensible middle.
**Reasoning.** Containment vs. evidence is managed per-step, not decided once; scope identification *is* the containment work.
**Alternatives.** Full isolation (if spread is fast/ransomware-aggressive — the tradeoff shifts).
**Tradeoffs.** Speed vs. evidence; business impact vs. containment certainty.
**Common mistakes.** The 110-minute deliberation itself (decide *how to decide* in advance); snapshots after shutdown (memory lost).
**Prompts.** What would your runbook say at 02:40? Who decides "broader containment" — analyst or incident commander?

## CS-041 — The Tabletop Surprise
**Model solution.** Fix 1: living data inventory — the notification plan points at an *automated* data map (from processing records/scan), not a spreadsheet; quarterly reconciliation. Fix 2: define clock-start explicitly in the plan: at *reasonable confirmation of a personal-data breach* (not first alert, not full forensics) — with the assessment owner named. In a real incident, the DPO/IR lead decides and documents the timestamp rationale.
**Reasoning.** Both defects are plan defects (pointing at stale artifacts; undefined triggers), not execution failures.
**Alternatives.** Pre-drafted notification templates per data class (speeds the 72-hour path).
**Tradeoffs.** Automated inventory = tooling; template maintenance vs. speed at 2 a.m.
**Common mistakes.** Treating the clock as starting at detection (over-notifies) or at forensics-completion (under-notifies); assuming the spreadsheet is "approximately right."
**Prompts.** What evidence would you accept as "reasonable confirmation"? Who is on the 72-hour rota?

## CS-042 — The Image That Wasn't
**Model solution.** Required procedure: acquire → hash (original) → work only on verified copy → log every access; hash the copy before and after analysis. Salvage now: the analyst's contemporaneous notes and the *timestamps of his own tool outputs* provide partial reconstruction, but authenticity is contestable — the correct answer is to disclose the defect (candor preserves credibility) and re-image if the laptop is still held.
**Reasoning.** Forensics = provable integrity of process, not just findings.
**Alternatives.** Write-blockers, network acquisition, live-response protocols.
**Tradeoffs.** Copy time vs. admissibility; re-image availability decides salvage strategy.
**Common mistakes.** "I documented what I found" (the *process* is in question); hiding the defect from the case officer.
**Prompts.** What makes digital evidence different from physical chain-of-custody? When can defects be acceptable (with disclosure)?

## CS-043 — The Deleted Meeting
**Model solution.** Records manager: issue a legal-hold/preservation notice immediately (covering mail store + backups), restore the deleted items (within the 30-day window — act now), document the deletion event itself (it is logged), and treat the *deletion before audit* as a reportable governance event for the auditor to weigh. Deletion-vs-retention design: business-record classes must be non-deletable by end users (policies at the platform level); personal convenience deletions live in a separate class.
**Reasoning.** The retention window is the recovery runway; the hold freezes it.
**Alternatives.** Accept loss and disclose (weaker; the record exists — restore it).
**Tradeoffs.** Preservation vs. privacy of personal content in the same store (scope the hold precisely).
**Common mistakes.** Waiting for the audit to "see what's needed"; treating deletion as neutral because "it was an accident."
**Prompts.** What converts a document into a "business record"? Who may grant deletion exceptions?

## CS-044 — The Camera on the Roof
**Model solution.** Priority order: (1) credentials — change defaults, management interface off the open network, (2) network path — cameras to their own zone; vendor cloud flow via explicit allow-list (or block + local recorder), (3) vendor terms — DPO review of metadata-analytics clause; contract amendment or replacement, (4) procurement process — IoT/OT purchases require IT/DPO sign-off (the systemic fix).
**Reasoning.** The procurement bypass is the root cause; the credentials are the live exposure.
**Alternatives.** Replace with managed cameras (cost); full air-gap (breaks remote viewing legitimately wanted).
**Tradeoffs.** Vendor cloud convenience vs. data-flow control; retrofit effort across 12 cameras.
**Common mistakes.** Stopping at default-password rotation; ignoring that metadata-analytics is itself a privacy finding.
**Prompts.** Who else buys IT-adjacent kit without IT? What would make the DPO sign-off easy rather than blocking?

## CS-045 — The Pilot That Scales
**Model solution.** Re-do before scaling: (1) DPIA refresh for scale (400 courses changes risk profile: volume, fairness/bias surface, appeal flows), (2) vendor data-residency guarantee in contract (or reject), (3) consent redesign — "optional pilot" becomes a governance decision with real alternatives for students and an appeals path. Also: bias/fairness evaluation at scale, incident path for false accusations.
**Reasoning.** Scale changes the *nature* of the risks, not just their size; consent under practical necessity isn't free.
**Alternatives.** Phased scaling with gates (per-faculty rollout with checkpoints); alternative tooling for lower-risk courses.
**Tradeoffs.** Delay vs. dean's timeline; phased = more overhead but safer.
**Common mistakes.** Treating the pilot DPIA as transferable; letting "optional" quietly become mandatory.
**Prompts.** What is your gate between phases? Who represents students in this decision?
