# ⚠️ INSTRUCTOR-ONLY — Level 3 Model Solutions (CS-046–075)

Reveal at step 5. Level 3 cases: multiple defensible solutions — grade the argument quality, tradeoff awareness, and named assumptions.

## CS-046 — The Cipher-Suite Debate
**Model solution.** Proposal package: (1) present the *measured* constraint (30% battery), (2) map the requirement's intent ("modern authenticated encryption") rather than its literal "256", (3) offer the written standard: AES-128-GCM in transit (TLS 1.3 suites), AES-256-GCM at rest for 10-year archives (harvest-risk asymmetry), documented in the crypto policy with review triggers. Ask the auditor what threat 256-vs-128 mitigates in *their* model — brute-force key search is not a realistic path for either.
**Reasoning.** Compliance literals vs. security intent; asymmetric archive exposure justifies the split.
**Alternatives.** Full 256 everywhere (cost accepted to close the audit); escalate to the auditor's governing body (political).
**Tradeoffs.** Two standards = documentation burden; full-256 = real battery cost for marginal gain.
**Common mistakes.** Framing as security-vs-compliance war; no measurement behind the engineering claim.
**Prompts.** When is the literal reading *reasonable* (defensible if breached)? What review trigger would move 128→256?

## CS-047 — Deterministic by Necessity
**Model solution.** Least-bad: deterministic encryption on the identifier column with a *domain-limited* key (dedup key ≠ other columns), plus tokenization vault alternative: replace identifiers with random tokens at ingestion (vault holds the mapping) — queries work on tokens; strongest option when vault custody can be separated. Name leaks: deterministic = equality leakage (frequency analysis on the identifier column); tokenization = vault is the crown jewel. Recommend tokenization if a separate custodian exists; otherwise scoped deterministic with documented leakage.
**Reasoning.** Equality queries require either deterministic ciphertext or an indirect index — the choice is *where* to concentrate risk.
**Alternatives.** Blind indexes (HMAC-based) — similar leakage profile, simpler ops; application-level dedup cache.
**Tradeoffs.** Vault = new critical component + custody question; deterministic = permanent, documented leakage.
**Common mistakes.** Random-encrypting the identifier "for safety" (breaks the function); ignoring that the DPO may accept *documented* leakage that unauthorized frequency analysis enables.
**Prompts.** Who holds the vault and why does custody separation matter? What queries would you *forbid* against a deterministic column?

## CS-048 — The Key Ceremony
**Model solution.** Recommendation: (b) HSM + 3-person ceremony *if* artifact signing will touch customers next year (the "next year trap" in (c): managed-KMS keys can sign fine, but the *sovereignty* question — who can export/revoke, what the provider's operators can do — becomes contractual with customers). Ceremony design: M-of-3 shares, offline generation, recorded (two-person integrity), test-sign + verify procedure, documented recovery. (a) rejected: laptop-held root keys are CS-014 with a budget.
**Reasoning.** Match the trust boundary to the *future* relying party, not today's internal scope.
**Alternatives.** Start (c) with contractual exit criteria ("customer-facing signing requires HSM") — pragmatic hybrid.
**Tradeoffs.** €4k + process vs. provider-trust; ceremony ops cost per rotation.
**Common mistakes.** Optimizing for today's scope; ceremony as theater (no recorded procedure = the shares are just three laptops).
**Prompts.** What does "the provider holds the boundary" mean contractually? Who are your ceremony witnesses?

## CS-049 — Ten Routes, One Sanitizer
**Model solution.** Migration: (1) freeze new blacklist edits, (2) introduce output-encoding helpers per context (HTML/attribute/JS) alongside the sanitizer, (3) migrate routes one at a time with tests (golden inputs incl. O'Brien, quotes, unicode), (4) the JSON API route: context-appropriate encoding for its consumer, (5) retire the sanitizer last (flag-only first: log would-be-strips). The stored mojibake report is the political lever: the sanitizer already corrupts legitimate data — it is a bug factory, not a defense.
**Reasoning.** Encoding belongs at output, in context; input blacklists corrupt and bypass simultaneously.
**Alternatives.** Framework auto-escaping adoption; CSP as interim net.
**Tradeoffs.** Staged migration = long dual-path period; big-bang = outage risk.
**Common mistakes.** Keeping the sanitizer during migration (double-encoding); testing only attack strings (legitimate-input regressions are the political risk).
**Prompts.** What would you *measure* to prove the migration is safe? Who signs off a route's migration?

## CS-050 — The Client-Side Price
**Model solution.** Fix: server-side recompute of the discount from the rule set (12 lines, 40 ms measured) — client-computed totals become display-only. Disclosure: honor coordinated disclosure (acknowledge fast, fix, credit the researcher per policy), and *do* honor orders placed during the window if placed through the normal UI in good faith — but analyze logs for the researcher's crafted requests (they disclosed, so no debt collection; the point is knowing the window's real cost).
**Reasoning.** The server is the trust boundary; the disclosure window cost is measurable and probably small.
**Alternatives.** Signed pricing tokens (heavier); anomaly-detection on discount distributions.
**Tradeoffs.** 40 ms vs. unlimited revenue leak; honoring orders costs little and buys goodwill.
**Common mistakes.** Prosecutorial response to a good-faith report (kills future reports); client-side "fixes."
**Prompts.** What does the researcher's report quality earn them? Which other totals are client-computed (audit question)?

## CS-051 — OAuth in the Middle
**Model solution.** Corrected flow: authorization-code + PKCE (SFS256), system browser (no webviews), redirect via app-claimed URI scheme/universal link, token exchange server-side where possible. Migration: server accepts old flow until version-X deadline; new app releases enforce; backend drops webview-client registration after sunset; telemetry on remaining old versions decides extension or break.
**Reasoning.** Webview + no PKCE = interception by design; the OS browser is the trusted UI.
**Alternatives.** App-attestation (device integrity layer) as defense in depth.
**Tradeoffs.** Old-version sunset = forced upgrades; attestation = platform coupling.
**Common mistakes.** PKCE as "optional hardening" (it is the flow for public clients); silently changing flows without sunset plan (breaks active sessions).
**Prompts.** Why does the *system browser* matter beyond PKCE? What do you owe users on forced sunset?

## CS-052 — Scope Creep in Tokens
**Model solution.** Scope model: resource-type + action granularity (grades:read, attendance:read, attendance:write), per-client scope grants, admin-visible client/permission registry. Deprecation path: introduce v2 scopes alongside, migrate clients with a published timeline (90 days), dual-validate during overlap, then hard-revoke `write:all` for new tokens and set expiry for existing. The partner gets `grades:read` only — verified against their *usage*, not their request.
**Reasoning.** Coarse scopes make least privilege impossible at the token layer; usage data is the truth for scoping.
**Alternatives.** API-gateway-level policy as a faster stopgap while token scopes ship.
**Tradeoffs.** Gateway policy = another config surface; client migration = integration effort.
**Common mistakes.** Grandfathering existing tokens forever; trusting partner self-assessment of scope needs.
**Prompts.** Who approves a client's scope request? What does the audit ask to see (registry, grants, usage evidence)?

## CS-053 — Fifty Criticals, One Cause
**Model solution.** Strategy: fix the base image once (staged rollout: dev → internal → exposed-last... *inverted*: exposed two services first as targeted patch or WAF virtual-patch, then full staged image rollout) — per-service patching multiplies change risk 12× and leaves drift. Fast path: the two internet-exposed services get immediate mitigation (patch or virtual-patch) inside the staged program.
**Reasoning.** Concentrated root cause = platform fix; exposure = immediate targeted exception.
**Alternatives.** Emergency full rollout (change-advisory risk); accept-until-patched (exposure window).
**Tradeoffs.** Staging time vs. rollout safety; virtual patch imperfection documented.
**Common mistakes.** Treating all 50 as independent tickets; letting CAB latency govern the exposed pair.
**Prompts.** How does the CAB handle *security-velocity* changes? What evidence convinced you the 47 were one root cause?

## CS-054 — The Unpatchable Legacy
**Model solution.** Mix: (c) virtual patch via filtering proxy (vendor-unsupported — document that) *plus* (a) isolation + monitoring *now*, with (b) replacement budgeted as the real fix (start the 6-month clock). Monitoring: baseline the documented 3 flows; anything else alerts; proxy blocks anything but the inbound protocol shape. Review trigger: any new exposure of the controller's protocol class accelerates (b).
**Reasoning.** Defense in depth on an unpatchable asset; interim ≠ permanent — the clock is the control.
**Alternatives.** Replacement-first if downtime cost is bearable; insurance/risk-transfer for the residual.
**Tradeoffs.** Proxy = single point of failure for the line (bypass/HA design); isolation = ops friction.
**Common mistakes.** Accepting indefinitely ("we've always run it"); virtual patch as invisible SPOF.
**Prompts.** Who owns the review trigger? What would you need to *prove* the proxy doesn't break the line?

## CS-055 — The 3 a.m. Tuning Call
**Model solution.** Fate: tune, don't kill — scope the rule (the historical TP's actual shape: specific source + asset class), raise threshold, add enrichment-gating (only alert when the enrichment matches the TP profile). Metric: precision-per-rule tracked over time with a review trigger (< 1% precision for 2 weeks → mandatory tuning review). The "found a thing once" argument ends with the base-rate framing: at 99.4% FP, analyst attention spent here costs more true positives elsewhere.
**Reasoning.** Alert volume is a budget; the rule must earn its share with precision.
**Alternatives.** Kill + memorialize as a correlation-detection lesson; shadow-mode rework.
**Tradeoffs.** Scoping = might miss variant TPs; shadow = no alerting during rework.
**Common mistakes.** Volume-chart politics driving the decision; killing without losing the TP-class coverage the rule actually had.
**Prompts.** What precision would *you* require to keep a rule alive? How do you explain base rates to management?

## CS-056 — Two Logs, One Story
**Model solution.** Investigation order: (1) verify MFA approval source (was the phone's IP also Country B? device compromise vs. credential compromise), (2) badge system integrity check (could the badge event be tailgated/proxied?), (3) session forensics (what did each session *do* — read vs. write), (4) contact user via *alternate* verified channel. Conclude nothing yet. Policy change: concurrent-session policy (kill-on-new-login or geo-velocity challenge).
**Reasoning.** Two impossible-facts scenarios: device compromise (traveling phone?) or badge spoofing — the evidence discriminates if you look at the *right* correlated field.
**Alternatives.** Immediate lockout (safe, disruptive — defensible for finance-class users).
**Tradeoffs.** Lockout = user disruption vs. exposure window; watch-only = evidence quality.
**Common mistakes.** "Users travel" as closure (the *concurrency* is the anomaly, not the geography); interrogating the user as suspect instead of victim-first.
**Prompts.** Which log would you subpoena first and why? What session policy would have auto-resolved this?

## CS-057 — The Insider Pattern
**Model solution.** Proportionate response: (1) document the legal basis + scope *before* looking (works council/legal sign-off; monitoring limited to work-related systems, defined window), (2) passive: preserve existing logs (no new collection), analyze access patterns already collected, (3) manager context check (HR performance file independent), (4) decision point: escalate to targeted DLP only with documented specific suspicion + approval. Everything documented; the employee's rights (notice laws vary) respected; the *innocent* outcome is the default assumption.
**Reasoning.** Insider programs fail on proportionality and documentation; the evidence you already have may answer the question without new surveillance.
**Alternatives.** Do nothing pending more signals; immediate DLP (likely unlawful/disproportionate here).
**Tradeoffs.** Slower = evidence may age; faster = legal exposure and trust destruction.
**Common mistakes.** Acting on the rumor (rumormill ≠ evidence); "watch them closely" without scope or end-date.
**Prompts.** What would you do if the pattern *stopped* after the employee noticed? Who decides proportionality — security, legal, or HR?

## CS-058 — Friday 17:00 Incident
**Model solution.** Recommendation: (c+) notify regulator immediately (duty triggered at confirmation), notify affected staff *same evening* with facts + what we're doing + next-update time — because leak-site publication risk makes "Monday" indefensible; works council consulted within hours (their staff are the data subjects). First communication's three sentences: what happened (confirmed exfiltration of HR salary data), what we're doing (containment, investigation, support), what you can do (watch for targeted phishing using salary info; here's the help channel). Clock start: at confirmation (17:00 Friday) — document it.
**Reasoning.** Exfil of salary data enables targeted fraud *this weekend*; delay converts victims into attack surface.
**Alternatives.** (a) indefensible; (b) without regulator-first sequencing risks procedural missteps.
**Tradeoffs.** Weekend chaos vs. targeted-fraud exposure; imperfect facts vs. silence.
**Common mistakes.** Waiting for "complete picture"; forgetting the *derived* risk (phishing using leaked salaries) in the comms.
**Prompts.** What would you put in the "what you can do" section and why does it matter most? Who staffs the weekend channel?

## CS-059 — The Restore That Wouldn't
**Model solution.** Restore path: immutable backup #3 (clean, 9-day-old) + differential recovery of newer data from *other* sources (mail, endpoints, the corrupted backup's partial integrity — forensically examine #1: corruption may be partial). Communicate data loss honestly with a per-dataset impact list. Backup-design change: RPO tiering (immutable daily for crown jewels), restore-rehearsal program, key-separation (CS-032 callback).
**Reasoning.** Clean-but-old beats infected-but-new; differential recovery narrows the gap from other sources.
**Alternatives.** Attempt cleaning backup #2 (forensically risky; malware in restore path).
**Tradeoffs.** 9-day loss vs. reinfection risk; recovery effort vs. business demand for "yesterday."
**Common mistakes.** Restoring #2 (the classic reinfection); promising "yesterday" without sources.
**Prompts.** Which datasets would you *prioritize* in differential recovery and why? What RPO tiering do you propose?

## CS-060 — Timeline Under Tampering
**Model solution.** Reconciliation: establish clock offsets (NTP records, event correlations — e.g., network events visible in both), merge streams with source-tagged entries, document the 90-minute local gap as attacker `rm` events *visible in the remote stream* (the deletion is itself evidence). Chain of custody for remote logs: export with hashes, storage-system timestamps, collection notes; the sysadmin's config history corroborates the stream's long-standing presence.
**Reasoning.** Tampering visible in a surviving source strengthens, not weakens, the timeline — attacker intent is now documented.
**Alternatives.** Additional sources (EDR telemetry, flow records) to fill gaps.
**Tradeoffs.** Offset uncertainty = ±seconds in the timeline (state it); deep verification vs. investigation velocity.
**Common mistakes.** Treating the local gap as missing evidence (the *deletion* is the evidence); merging timelines without offset documentation.
**Prompts.** What makes the remote stream trustworthy (its own integrity chain)? How would you defend this timeline to a disciplinary panel?

## CS-061 — The Acquired Company's Secrets
**Model solution.** Recommendation: do *not* accept the drive into the acquirer's environment; instead: (1) document the admission (it is itself a reportable event for the target — their data, their breach), (2) legal reviews under deal NDA; if the drive is needed for diligence, image and review *inside* counsel's control with a written protocol, (3) the admission feeds the deal's risk assessment (an admin who keeps "a copy of everything" is a finding about the target's offboarding culture), (4) the personal-files problem means custody creates liability — never browse.
**Reasoning.** Possession adopts obligations; the admission changes the deal's risk model more than the drive changes your knowledge.
**Alternatives.** Refuse entirely (cleanest); target's counsel manages review and reports findings.
**Tradeoffs.** Diligence completeness vs. liability adoption; relationship impact vs. process purity.
**Common mistakes.** Plugging it in "just to look"; treating the admin as a resource rather than an incident.
**Prompts.** Whose breach is the copying? What does your own offboarding look like by comparison?

## CS-062 — IAM Archaeology
**Model solution.** Sequence: (1) freeze new `*:*` grants, (2) 90-day usage evidence per policy (access advisor/logs) → tag used/unused, (3) the self-modifying trio: immediate remediation (trust conditions, external control), (4) unused-60: revoke in staged batches with a 2-week rollback window (cloudtrail shows nothing breaks), (5) used-`*:*`: rewrite to least privilege from *observed* actions, staged, (6) guardrail: policy-as-code linting (no `*:*`, mandatory review), drift detection. "Delete and see what breaks" fails because production criticality is unknown — evidence replaces archaeology.
**Reasoning.** Usage logs convert archaeology into measurement; staged revocation with rollback converts risk into process.
**Alternatives.** Parallel clean account + migration (bigger project, cleaner result).
**Tradeoffs.** Staging time vs. exposure; guardrails = platform investment.
**Common mistakes.** Revoking by age instead of usage; fixing the trio *last* (they're first: active escalation paths).
**Prompts.** What does the rollback window cost you? Which guardrail prevents recurrence most cheaply?

## CS-063 — The Cross-Tenant Curiosity
**Model solution.** For Tenant B: (1) contain — verify the misconfiguration scope (metadata-only confirmed? any content access in logs?), (2) notification analysis: bucket *names* containing customer identifiers may constitute personal data — assess per regulation; even if not reportable, contractual breach terms with A apply, (3) fix — trust policy conditions (external account allow-lists), (4) demand from A: root cause, assurance the engineer acted alone/in good faith, contract breach handling — *not* punishment of the discloser (that kills future reports). The engineer gets thanks through A's channel; the report is a gift.
**Reasoning.** Good-faith cross-boundary disclosure is rare and valuable; the response teaches every future engineer what reporting earns.
**Alternatives.** Formal legal escalation only (relationship damage); ignore metadata-as-personal-data question (analysis is owed regardless).
**Tradeoffs.** Over-notification costs trust; under-notification risks regulatory breach.
**Common mistakes.** Shooting the messenger (via A); skipping the metadata-is-personal-data analysis because "only names of buckets."
**Prompts.** When is a bucket name personal data? What would you write into the contract's security-incident clause after this?

## CS-064 — Serverless Hours
**Model solution.** Redesign: per-function role (read-input-bucket, write-its-output-bucket only), output-bucket as *code constant* (never from payload), payload schema validation, function-level invocation auth. First-breaking control: output-bucket-as-constant — the payload redirect dies immediately; scoping limits what any future exploit reaches. Monitoring: invocation-parameter anomaly alert (output bucket ≠ constant = page).
**Reasoning.** Trusting payload-parameters for destination = the whole vuln class; constants + validation kill it.
**Alternatives.** Split the function (ingest vs. process) so the fat role never exists; deny-by-default egress policy.
**Tradeoffs.** Refactor effort; some legitimate multi-destination flows need redesign.
**Common mistakes.** Only scoping the role (redirect still works *within* scope if output bucket is payload-controlled); blaming the dependency alone.
**Prompts.** Which parameters in your own functions are trust decisions wearing config costumes? What would your invocation-anomaly alert look like?

## CS-065 — The Doorbell DDoS
**Model solution.** Recommend QoS shaping first (cap the vendor endpoint aggregate; immediate, no user impact — syncs take minutes longer, invisible), plus vendor negotiation for stagger (real fix), plus DNS-interception stagger only as last resort (fragile, maintenance burden, becomes your system to own). User-experience cost of shaping: midnight syncs may span ~30 min — nobody notices.
**Reasoning.** Shape the symptom cheaply, fix the cause contractually, avoid owning a hack.
**Alternatives.** Block entirely (800 angry residents); dedicated IoT egress link (over-engineering).
**Tradeoffs.** QoS = config + monitoring; negotiation = time and may fail; interception = permanent ops debt.
**Common mistakes.** Starting with the clever hack; forgetting to *measure* saturation window before/after.
**Prompts.** Who owns vendor negotiation — network team or procurement? What does your QoS policy do when *legitimate* traffic saturates next?

## CS-066 — The Guest Lab Network
**Model solution.** Zones: Laptops / Robots / Telemetry-egress / (services). Rules: robots: no internet (deny all egress except NTP if needed), laptops→robots only on dashboard ports (documented), robots→laptops denied (initiation from laptops), telemetry→cloud via proxy allow-list, all zone-pairs default-deny. Contested exception: ROS discovery traffic (multicast) doesn't cross zone boundaries cleanly — options: reflector service in the middle, or a narrow L2 bridge for multicast only with monitoring. Process: exception with owner, review date, and documented compensating monitoring.
**Reasoning.** Directionality (who initiates) is the design lever; the multicast exception is where discipline is won or lost.
**Alternatives.** Whole-lab segregation at L2 with policy at the gateway (simpler, less granular).
**Tradeoffs.** Reflector = extra component; L2 bridge = wider blast radius if abused.
**Common mistakes.** Allowing multicast broadly (the exception swallows the design); forgetting robots' vendor-support flows (they'll phone home — decide now).
**Prompts.** Who signs the exception and what does the review check? What breaks first when the vendor updates the robots?

## CS-067 — The Feature That Leaks Training Data
**Model solution.** Immediate: output filtering for HR-policy-class content (similarity threshold → refuse + log), rate/abuse monitoring. Corpus hygiene: remove personal-grade request logs from future training; document retention. Breach decision: reproduction of *policy text* is not personal data (policy is internal IP, not PII) — but reproduction of *past user prompts* with personal content likely is → assess as potential personal-data breach, notify DPO, evaluate affected prompts. Longer term: RAG-with-permissions instead of fine-tuned memorization for sensitive corpora.
**Reasoning.** Separate the two leak classes: IP (policy text) vs. personal data (prompt memorization) — they have different obligations.
**Alternatives.** Take the bot offline pending fixes (defensible if personal-data reproduction is confirmed); restrict to non-sensitive corpora.
**Tradeoffs.** Filtering = false refusals; RAG rebuild = project cost; offline = user impact.
**Common mistakes.** Treating all of it as "just IP loss"; leaving personal prompts in the next training run.
**Prompts.** What threshold converts "occasionally reproduces" into "reportable"? Who owns the corpus-composition decision?

## CS-068 — Poisoned by the Crowd
**Model solution.** Mitigation set: (1) report authentication (reports weigh by account age/history), (2) report-pattern anomaly detection (spike in reports *for one sender* from one cohort = flag for human review, not auto-block), (3) high-impact labels (blocking a whole sender) require human sign-off above a size threshold, (4) appeal path for senders with measured recovery metric (block list decay analysis). Recovery metric: time-to-unblock + false-block rate trend after deployment.
**Reasoning.** The feedback loop is a label source; label sources need the same trust architecture as any data source.
**Alternatives.** Kill crowd-reporting entirely (loses the best signal); reputation weighting only.
**Tradeoffs.** Authentication = friction on genuine reporting; human review = staffing.
**Common mistakes.** Tuning thresholds only (the attack adapts); no sender-appeal path (uncontested blocks compound).
**Prompts.** What is the *cost* to the attacker under your design? How do you measure false-block harm to senders?

## CS-069 — The Model That Believes
**Model solution.** Authority architecture: the model's *capability* is the enforcement point — refund-approval tool enforces ≤ €50 hard limit server-side (prompt text can grant nothing), input treatment: treat ticket text as untrusted data (delimit + instruct), output treatment: tool calls logged with input citation, above-limit refunds always human. Audit trail: every auto-action traceable to (ticket, model version, rule set). The prompt-injection did not "trick" the system — the system's authority was wrongly implemented in prose.
**Reasoning.** Separate what the model *says* from what it may *do*; capability boundaries live in code.
**Alternatives.** Remove tool access entirely (loses the value); two-model pattern (propose/verify).
**Tradeoffs.** Hard limits = support friction for legit edge cases; propose/verify = latency.
**Common mistakes.** Prompt-hardening as the fix (attackers iterate); trusting the human-review catch as the control.
**Prompts.** Where else is authority implemented in prose (system prompts as policy)? What would the audit trail need to show finance?

## CS-070 — Third-Party Risk by Spreadsheet
**Model solution.** Tiered program: Tier 1 (the six PII-heavy + anything with >1k users): full assessment + contract terms + SSO enforcement. Tier 2: standardized questionnaire (auto-graded) with SSO required. Tier 3 (rest): automated inference — SSO logs reveal which tools see what identity data; DNS/egress data reveals data flows; classification by *observed behavior*, not vendor self-report. Deliverable by Friday: Tier 1 done, Tier 2 shipped, Tier 3 classified-by-inference with documented method. Defensible because it matches depth to risk.
**Reasoning.** 214 assessments by 2 people is arithmetically impossible — inference from telemetry is the only scalable truth source.
**Alternatives.** Refuse-and-triage (political cost); buy a TPRM platform (time-to-value problem).
**Tradeoffs.** Inference = probabilistic classification (document confidence); questionnaire refusal itself is a risk signal.
**Common mistakes.** Treating all tools equally (the deadline forces honesty — use it); vendor self-attestation as classification evidence.
**Prompts.** What does SSO-log analysis reveal that questionnaires can't? Which six tools are Tier 1 in *your* university and why?

## CS-071 — The Risk Acceptance That Grew
**Model solution.** Decision: the acceptance is void (expired + material change) — it becomes an *unmanaged* risk today; options: re-accept with new signature and new terms (if a compensating case exists for the 5× cost gap), or fund remediation phased (segment A-B now, C contingent). The original director: no blame session — the *system* failed (no expiry enforcement). Mechanism: acceptance registry with expiry dates, auto-review calendar, change-triggers (new connections to an accepted scope re-open the acceptance), CISO dashboard of aging acceptances.
**Reasoning.** Acceptances are liabilities with terms; change without re-review voids the analysis.
**Alternatives.** Remediate immediately regardless of cost (audit-clean, budget-hostile).
**Tradeoffs.** Re-acceptance = defensible only with fresh compensating controls; phased = interim exposure documented.
**Common mistakes.** Retroactively "renewing" without re-analysis; blaming the promoted director (destroys future honest acceptances).
**Prompts.** What makes an acceptance *honest*? Who may accept which size of risk in your organization?

## CS-072 — Metrics That Move Nothing
**Model solution.** Redesign: (1) patch compliance → *exposure-weighted* remediation SLA (are the exposed-critical items closed in time? — resists scan-time gaming), (2) training completion → behavioral measure (phishing-report rate/time-to-report), (3) "incidents down" → replace with detection-quality metrics (MTTD on purple-team exercises) + near-miss reporting *encouraged* (a rising near-miss count is health, not failure). Stop reporting: raw incident counts (they measure reporting culture, not security).
**Reasoning.** Each metric must measure the outcome you want, or it measures the metric.
**Alternatives.** Third-party assessment for maturity scoring; OKR-style security objectives.
**Tradeoffs.** Behavioral metrics = program investment; purple-team exercises = engineering cost.
**Common mistakes.** Replacing with equally-gameable proxies; keeping the blame culture while changing dashboards.
**Prompts.** What does your near-miss reporting rate say today? Who audits the metric definitions annually?

## CS-073 — The Dataset That Shouldn't Be There
**Model solution.** Decision: cannot proceed as-is. Required changes: (1) provenance documentation and legality assessment (ToS breach = collection-violation; public availability ≠ consent), (2) remove the three staff records (they are data subjects with a relationship to the institution — heightened duty), (3) minimize: does the model need bios at all, or only graph structure?, (4) documented lawful-basis/path: either re-collect via permitted means/API or restrict to the permitted subset, (5) supervisor duty: the project continues only with a compliant corpus — the *technique* is learnable on lawful data.
**Reasoning.** Illegally-sourced data poisons the project's outputs (publication, defense) regardless of model quality.
**Alternatives.** Anonymized/published research subsets (platform-provided datasets with licenses).
**Tradeoffs.** Re-collection effort vs. legal exposure; smaller corpus = weaker results (honest limitation).
**Common mistakes.** "It's public anyway" (availability ≠ permission); deleting quietly without documenting the decision.
**Prompts.** What would the platform's lawyers say vs. their ToS? What does your university's research-ethics process require *here*?

## CS-074 — Feature Store Confidentiality
**Model solution.** Fix set with quality tradeoffs: (1) query budgets per analyst (differencing needs many queries — cap them), (2) minimum-aggregate-size (suppression of small cells), (3) noise on sensitive aggregates (calibrated — model-quality hit is measurable), (4) row-level security by segment (analyst sees their business line only). Recommendation: budgets + cell-size first (cheap, preserves most quality), noise only for the executive-segment features where reconstruction risk concentrates.
**Reasoning.** Differencing is arithmetic; defenses are query-economics and disclosure-control, applied where risk concentrates.
**Alternatives.** Full differential-privacy deployment (strong, quality-expensive); access logs + periodic audit (detective only).
**Tradeoffs.** Each control taxes model retraining/reproducibility; RLS breaks cross-segment features.
**Common mistakes.** "Aggregates are safe" as policy (they are not); applying noise everywhere (quality collapse + revolt).
**Prompts.** Which features would you *noise* and why those? Who approves a query-budget exception?

## CS-075 — The Shadow Model
**Model solution.** Model's fate: quarantined pending compliance review — performance is irrelevant if lineage is void. Data-handling violation: the bulk export was granted "temporarily" — access-governance failure on both sides; consequences per policy (documented warning + process for the scientist; export-approval process fix). Legitimate path forward: if the model's improvements are real, re-derive it *inside* governance (official compute, documented data lineage, approval) — the scientist joins the official team's effort. Guardrails: egress monitoring for bulk extracts, register for non-production training runs, time-boxed extracts with auto-revocation.
**Reasoning.** Punish the process, recycle the insight: zero-tolerance on data handling, zero-waste on the innovation.
**Alternatives.** Hard dismissal (loses talent, chills R&D); full amnesty (gutfires governance).
**Tradeoffs.** Re-derivation cost vs. precedent; churn risk of the scientist either way.
**Common mistakes.** Adopting the model with a shrug (governance dead); banning all experimental training (drives it further underground).
**Prompts.** What made the "temporary" export permanent — technically or culturally? What would make the *official* path fast enough to compete with shadow work?
