# ⚠️ INSTRUCTOR-ONLY — Level 1 Model Solutions (CS-001–020)

Reveal at step 5 of the classroom method. Each solution: model answer, expected reasoning, alternatives, tradeoffs, common mistakes, discussion prompts.

## CS-001 — The Club Committee Password
**Model solution.** Risks: (1) no attribution — any member's action is unattributable (accountability, C+I); (2) weak+exposed password — external takeover (C); (3) no revocation path — a member who leaves keeps access (C/I). First change: individual accounts (identity layer), *then* password policy — because with individual accounts you can actually revoke and attribute.
**Reasoning to draw out.** The structural risk is *sharing*, not strength; a strong shared password stays unattributable and unrevocable.
**Alternatives.** Password manager for the club (fixes strength/sharing partially, keeps attribution gap); SSO via student union (best if available).
**Tradeoffs.** Individual accounts = provisioning effort; password manager = one more secret (its master password) and a sharing workflow.
**Common mistakes.** Proposing "make the password stronger" only; forgetting leavers; not naming the accountability failure.
**Discussion prompts.** Who is accountable when a shared login posts something defamatory? At what team size does sharing stop being "practical"? What does the student-union IT office owe you (individual accounts available?).

## CS-002 — Same Password Everywhere
**Model solution.** Attack path: attackers crack forum DB → credential-stuff LMS/shopping (reuse) → success on LMS (coursework, personal data) → account recovery loops to email. Mitigation ranking: (1) enable MFA on LMS (breaks stuffing regardless of password), (2) unique passwords via manager (limits blast radius).
**Reasoning.** "Unimportant site" is wrong because *you* are the asset — the reused credential is the link between sites.
**Alternatives.** Breach-notification monitoring; passphrases per class of service (tiering).
**Tradeoffs.** MFA friction; manager adoption cost; tiering is weaker but cheaper.
**Common mistakes.** "Stronger password on the forum" (already stolen); missing the MFA ranking.
**Prompts.** Whose responsibility is cross-site reuse? Why do platforms care (they get blamed for other sites' breaches)?

## CS-003 — The Suspended Library Account
**Model solution.** Do not click; verify via the known portal/bookmark; report via the university's phishing-report button. Clues: lookalike domain (`university-library.com` vs `library.university.edu`), generic greeting, artificial deadline. SPF passing only says *some* server was authorized for *some* domain — the visible `From:` domain itself is the attacker's; authentication ≠ trustworthiness of identity.
**Reasoning.** Urgency + generic greeting + infrastructure mismatch = classic harvest pattern.
**Alternatives.** Forward to IT as attachment (preserves headers) — better than deleting silently because the community benefits from detection.
**Tradeoffs.** Reporting takes 30 seconds vs. deleting takes 5; the difference is ecosystem defense.
**Common mistakes.** "SPF passed so it's fine"; clicking in a "safe" VM to check (normalizes the click; the credential harvest happens at the destination, not the click).
**Prompts.** Why do attackers include deadlines? How would the university detect this campaign (reports from users are telemetry)?

## CS-004 — The 2 a.m. Approval Prompt
**Model solution.** Order: (1) deny nothing / approve nothing; (2) treat password as compromised: change it now from a trusted device; (3) check active sessions and revoke; (4) report to IT. Key inference: three prompts means the password is already known — prompts are the *second* factor being attacked, the first already fell.
**Reasoning.** MFA fatigue is an attacker technique; the repetition is the tell.
**Alternatives.** Number-matching / push with location display (platform fix); passkeys (eliminates the prompt class).
**Tradeoffs.** Changing password at 2 a.m. from the same phone (if the phone were compromised — unlikely here, the prompts imply remote login attempts).
**Common mistakes.** Approving to stop the noise; not reporting (the identity team wants the campaign signal).
**Prompts.** Why number-matching beats plain push? What should the platform do after N denied prompts?

## CS-005 — Printers on the Staff Network
**Model solution.** Cached credentials on a web-managed, weakly-patched device on the staff VLAN = a credential-exfiltration foothold adjacent to your real assets. Minimal fix: printers own VLAN; allow printer→print-server/vendor-update flows; deny printer→staff-client and printer→servers; keep staff→printer printing path.
**Reasoning.** Segmentation maps to blast radius; printers are the classic forgotten credential cache.
**Alternatives.** Disable scan-to-email caching (feature-level); credential rotation on printers.
**Tradeoffs.** VLAN move = switch work + reconfiguration; feature disable = some users lose scan-to-email.
**Common mistakes.** "Printers don't hold anything valuable" (they hold *your* credentials).
**Prompts.** What else behaves like a printer in your environment (cameras, badge readers, HVAC)?

## CS-006 — The Logged-In Lab Machine
**Model solution.** Harms: data theft from the session (email, files), actions attributed to the student, malware under admin rights, lateral movement if domain-joined. Controls: technical — short auto-lock + standard-user defaults (why does a student PC need admin?); procedural — session-timeout policy + lab rules.
**Reasoning.** Two independent failures (unlocked + admin) compound; each alone would halve the harm.
**Alternatives.** Badge-tap login; remote-kill sessions at night.
**Tradeoffs.** Auto-lock annoyance vs. exposure; removing admin = support tickets.
**Common mistakes.** Only the human fix ("be careful"); ignoring that admin rights turn a nuisance into a compromise.
**Prompts.** Who bears the cost of each control? Which layer would you deploy first with zero budget?

## CS-007 — The USB Stick in the Library
**Model solution.** Risks: malware execution, legal exposure (reading someone's private files), the curiosity exploit itself. Student action: hand it to IT/service desk. University procedure: isolated analysis VM by IT, documented found-property process.
**Reasoning.** The label is social engineering; autorun-off ≠ safe (exploit-by-parser class, deliberate droppers).
**Alternatives.** "Plug into a sacrificial machine" — only with isolation and IT ownership, never personally.
**Tradeoffs.** Owner may lose the stick; that is the correct outcome vs. the risk.
**Common mistakes.** "Nothing runs without autorun" — parsers (thumbnail, filesystem) have been exploit surfaces.
**Prompts.** Why do real-world campaigns still seed USBs (simulated exercises aside)? What makes curiosity stronger than caution?

## CS-008 — Cloned Access for the New Hire
**Model solution.** Principle violated: least privilege (access accumulation over 5 years ≠ current role needs). Risks: new hire gets access to closed projects (C) and inherits Tom's standing exceptions. Cheap fix: define the *current* role's access list once, grant that.
**Reasoning.** Cloning copies history, not requirements.
**Alternatives.** Role-based access control (RBAC) long-term; time-boxed elevated access.
**Tradeoffs.** Role definition takes an hour now vs. cleanup projects later.
**Common mistakes.** Framing as speed-vs-security: defining the role IS the fast path over time.
**Prompts.** When is cloning acceptable (truly identical roles)? Who owns role definitions — IT or data owners?

## CS-009 — One Account, Three Interns
**Model solution.** Failed properties: accountability/non-repudiation (who modified?) — an integrity *governance* failure enabling integrity failures. Minimum fix: individual accounts (even with identical privileges) — attribution restored without re-designing permissions.
**Reasoning.** You don't need fewer privileges to fix attribution; you need identity.
**Alternatives.** Break-glass shared account + personal accounts as default (the shared one becomes exceptional and monitored).
**Tradeoffs.** Three accounts = three passwords/lifecycles; negligible vs. an unattributable data change.
**Common mistakes.** Blaming individuals; proposing complex audit tooling before fixing identity.
**Prompts.** What does "non-repudiation" add over plain logging? When is a shared account legitimate?

## CS-010 — Grades by Email
**Model solution.** Classification: personal-data breach (misdirected confidential data, 240 subjects) — availability of confidentiality. Controls: (1) protected channel/portal for grade submission (structural), (2) recipient-verification workflow (double-check + distribution-list hygiene; a "confirm external recipients" gate).
**Reasoning.** The typo is the trigger, not the cause; the cause is sensitive data in a lossy channel.
**Alternatives.** Encryption-at-rest attachments (helps if recipient is honest, not if address is wrong — the wrong recipient *can* open it).
**Tradeoffs.** Portal = development effort; verification gate = tiny friction, big coverage.
**Common mistakes.** Solving the typo (cannot be solved — humans err); assuming encryption would have prevented this misdirection.
**Prompts.** Does the DPO notify 240 students? What does "minimization" say about emailing grades at all?

## CS-011 — The Password on the Router
**Model solution.** Cost: anyone entering the office gets staff Wi-Fi (pivot point), leavers retain access indefinitely, no rotation in practice. Technical fix: individual credentials or certificate-based Wi-Fi (802.1X); procedural: leaver checklist item + no-written-credentials policy.
**Reasoning.** Shared PSK makes offboarding structurally impossible.
**Alternatives.** Guest SSID for low-risk needs; portal-based captive auth for visitors.
**Tradeoffs.** 802.1X = RADIUS setup effort; guest SSID = classification of what "guest" may reach.
**Common mistakes.** Only removing the note; forgetting that the *knowledge* is already out (rotation is mandatory once exposed).
**Prompts.** Rotation is useless without a distribution mechanism that isn't sticky notes — what is yours?

## CS-012 — The Club Site Login Page
**Model solution.** Exposed: credentials in transit to any network observer (open Wi-Fi, ISP, parallel paths). Fix: enable TLS (Let's Encrypt, free) + redirect HTTP→HTTPS; one config block plus renewal automation.
**Reasoning.** "Nothing secret" fails because the password is the secret; also session cookies afterward.
**Alternatives.** Third-party hosted auth (move the problem to someone competent).
**Tradeoffs.** Cert renewal automation = small ops duty; hosted auth = dependency.
**Common mistakes.** "The site has nothing valuable"; forgetting HSTS as the follow-up.
**Prompts.** Why is free TLS still not everywhere? What does the browser padlock *not* guarantee?

## CS-013 — Guessable Recovery Answers
**Model solution.** Knowledge-based recovery is broken by design: the answers are *public-by-convention* (social media) and *static*. Better designs: (1) verified recovery to an owned channel (email/phone with possession check), (2) pre-registered recovery codes, (3) passkey/account recovery via platform.
**Reasoning.** The class of answer (biographical facts) is researchable; difficulty tuning doesn't fix publicness.
**Alternatives.** Delayed recovery with notifications; in-app verification of trusted device.
**Tradeoffs.** Possession-channel recovery fails if the email is also lost; recovery codes get stored badly.
**Common mistakes.** "Use more obscure questions" (obscure = unforgettable by the legitimate user too).
**Prompts.** Who is the "attacker" here — a classmate. What does that say about threat modeling for recovery flows?

## CS-014 — The Key in the Repository
**Model solution.** Sequence: scrapers find it within hours; usage appears on the bill; worst case: data exfiltration if the key is broad. Fixes in order: (1) revoke immediately, (2) rotate to a new key, (3) redesign: env/secret-manager + pre-commit scanning + git-history purge (optional, team-costly).
**Reasoning.** Deletion ≠ removal: clones and history retain the key; revocation is the only real fix.
**Alternatives.** Restrict key by referrer/API restrictions (defense in depth), spend alerts.
**Tradeoffs.** History rewrite breaks forks/CLAs; restrictions limit functionality.
**Common mistakes.** Delete-and-forget; no revocation; blaming the student instead of fixing the pipeline.
**Prompts.** Who pays for leaked keys, and what does that incentive produce? Why do scrapers exist as a business?

## CS-015 — Two Findings, One Weekend
**Model solution.** Patch A (critical + public exploit + exposed = active-risk). For B: schedule, interim mitigation (restrict access/exploit not public), communicate the decision. Rule: severity × exploitability × exposure — a *medium* finding that is exposed with a public exploit can outrank a critical that is internal and hard to exploit.
**Reasoning.** Risk is contextual, not categorical.
**Alternatives.** Patch both by pulling people in (real option if change cost is low — note it).
**Tradeoffs.** Weekend work vs. exposure window; deferral needs a named interim control, not just "later."
**Common mistakes.** Patching B first because its severity number is bigger on the report; forgetting to *decide about* B (defer ≠ ignore).
**Prompts.** Who decides "exposed"? What does the interim mitigation for B look like concretely?

## CS-016 — Failures Nobody Watched
**Model solution.** Missing: the *detection* capability between logging and response — ownership + alerting + budget. Minimal fix: a threshold alert (e.g., >100 failures/24h on one account) + a named owner for the alert class; logs are necessary, not sufficient.
**Reasoning.** Logging without alerting is a diary, not a tripwire.
**Alternatives.** Full SIEM (right at scale, overkill for this single gap); managed monitoring service.
**Tradeoffs.** Threshold alert = some tuning (FPs); SIEM = cost/integration project.
**Common mistakes.** Tool-first answer; not assigning ownership (the alert will become CS-039).
**Prompts.** What threshold would you set, and what legitimate behavior would trip it? Who gets the alert at 2 a.m.?

## CS-017 — The Laptop on the Bus
**Model solution.** First three actions: (1) inventory exactly what data the laptop held (submissions list), (2) notify the DPO/lead immediately (delay is itself the finding), (3) determine notification duty to students (their data; likely a reportable personal-data breach), plus credential resets if the laptop had account access. Prevention: full-disk encryption (would have reduced this to a loss-of-hardware event), minimization (why were drafts on a laptop at all?).
**Reasoning.** Encryption converts a data breach into a hardware loss; the delay converts an incident into a compliance failure.
**Alternatives.** Portal-only submissions (structural fix); device management with remote wipe.
**Tradeoffs.** Portal = change to workflow; FDE = negligible cost, must be enforced centrally.
**Common mistakes.** FDE as the only answer; not treating the reporting delay as its own problem.
**Prompts.** Why is "the next morning" a finding? What would you say to the 60 students?

## CS-018 — Who Deleted the File?
**Model solution.** Order: (1) confirm the delete event exists in logs (username, timestamp), (2) check for other deletions/modifications in the window (pattern = intent indicator), (3) recover: without versioning, only backups hold the content — check backup schedule vs. deletion time. Logs prove the *act*, not the *intent*; intent needs context (interview, pattern).
**Reasoning.** Evidence discipline: establish what happened, then why; recovery feasibility is a design question (versioning absent = backup-precision question).
**Alternatives.** Enable versioning/share recycle bin after the fact (prevention for next time).
**Tradeoffs.** Versioning costs storage; retention policies trade forensics depth vs. cost.
**Common mistakes.** Accusing from a single log line; forgetting that absence of versioning constrains recovery before the interview.
**Prompts.** Should delete be a two-step (soft-delete) by default? What would the logs *not* show even with versioning?

## CS-019 — The Smart TV on Staff Wi-Fi
**Model solution.** Zone: dedicated IoT/AV zone. Rules: TV→vendor-update/telemetry endpoints only (if tolerated), deny TV→staff/servers, allow casting sources→TV on the specific protocol ports. Rationale: unmanaged, unpatchable-by-policy device with outbound telemetry must not sit adjacent to staff assets.
**Reasoning.** Segmentation by trust, not by device type convenience; the casting use case survives zoning.
**Alternatives.** Full ban (loses function); vendor firmware program (out of your control).
**Tradeoffs.** Zone = switch port work; some casting protocols hate segmentation (multicast — document the exception).
**Common mistakes.** Treating "it can't be hacked for data" as the bar — it is a foothold and a telemetry leak.
**Prompts.** What is your policy for devices that *cannot* be patched? Who owns the exception list?

## CS-020 — The Startup With No Rules
**Model solution.** Priority order: (1) offboarding checklist (revokes access — the live risk), (2) access-control baseline (who has what, incl. the dashboard), (3) one-page acceptable-use/laptop rules (sets expectations). Enterprise policy libraries are premature; the three artifacts fit on three pages.
**Reasoning.** Governance = the smallest set of agreements that prevents the failures you actually fear.
**Alternatives.** Adopt a lightweight framework (e.g., CIS Controls IG1) as scaffolding.
**Tradeoffs.** Writing policy = founder time; skip it and the next leaver repeats this case.
**Common mistakes.** Copying enterprise policies (unfollowable); treating policy as documentation rather than behavior design.
**Prompts.** At what size does each artifact start to matter? Who enforces policy in a 5-person company?
