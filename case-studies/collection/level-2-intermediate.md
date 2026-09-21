# Case Collection — Level 2: Intermediate (CS-021–045)

> Simulated teaching scenarios; all organizations, people, and data are fictional. Classroom method as in Level 1. Solutions: instructor-only tier.

---


## CS-021 — The Breach-Corpus Check
**Difficulty:** Level 2 · **Domain:** Password & authentication · **Time:** 6 min + discussion · **CLO:** 1, 5

**Scenario.** The university adopts breach-corpus password screening at registration. A student's chosen password is rejected; she complains it is "private and nobody would guess it." Analytics show 0.3% of students hit the blocklist, but blocked users choose replacements that are *deterministically* weaker patterns (password1, password1!).

**Stakeholders.** Students; the identity team; security leadership (who want the metric "blocked = safer").

**Available evidence.** Blocklist rate; observed replacement patterns; no MFA enforcement yet.

**Student task.** Evaluate the control: is it working? What does the replacement-pattern data tell you, and what policy change do you recommend?

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-022 — Passkeys for the Helpdesk
**Difficulty:** Level 2 · **Domain:** Password & authentication · **Time:** 6 min + discussion · **CLO:** 1

**Scenario.** The university pilots passkeys for staff. Enrollment works well for most, but the service desk reports a spike: users with new phones cannot sign in, and the desk has no verification procedure for identity, so it resets credentials on voice request.

**Stakeholders.** Staff; service desk; identity team; attacker who phones the desk.

**Available evidence.** Passkey platform-lock-in issue; no desk identity-verification standard; reset-on-voice practice.

**Student task.** Where is the new weak point, and what is the minimal desk procedure that keeps passkeys' security without bricking users?

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-023 — The CEO's Signature Style
**Difficulty:** Level 2 · **Domain:** Phishing & social engineering (BEC) · **Time:** 6 min + discussion · **CLO:** 3

**Scenario.** Finance receives an email from the managing director's *real* address (her laptop was compromised): "Pay this invoice today, I'm in meetings." Signature correct, tone correct, amount plausible. The bank details differ from the vendor's previous invoice by two digits.

**Stakeholders.** Finance staff; the MD; the (fictional) vendor; the bank.

**Available evidence.** Real mailbox (authentication would pass); urgency; changed bank details; MD unreachable "in meetings."

**Student task.** Design the verification step that stops this *without* teaching staff to distrust every mail, and decide what happens if the MD is genuinely unavailable.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-024 — The Helpful New Colleague
**Difficulty:** Level 2 · **Domain:** Phishing & social engineering (pretexting) · **Time:** 6 min + discussion · **CLO:** 3

**Scenario.** A caller claiming to be a new IT contractor asks the receptionist to read out the Wi-Fi password "to finish setup" and mentions two real employee names (from the website's team page). The receptionist is helpful by training.

**Stakeholders.** Receptionist; the real contractor (whose identity is borrowed); IT; the department.

**Available evidence.** Caller knowledge from public sources; pressure via helpfulness norm; the password's blast radius (staff network).

**Student task.** Write the two-sentence receptionist script that stops this, and decide where the authentication boundary should be.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-025 — The Summer of Flat Network
**Difficulty:** Level 2 · **Domain:** Network segmentation · **Time:** 7 min + discussion · **CLO:** 4

**Scenario.** A campus lab runs one flat network for 40 workstations, 3 servers, and 15 student laptops. A worm with credential-reuse behavior lands on one student laptop before term starts.

**Stakeholders.** Lab users; sysadmin; data owners (server shares).

**Available evidence.** Flat topology; cached credentials everywhere; the worm's propagation pattern (SMB + credential reuse).

**Student task.** Design the minimal segmentation (zones + the two rules that matter most) and predict the worm's spread *with* your design.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-026 — The Guest That Wasn't
**Difficulty:** Level 2 · **Domain:** Network segmentation · **Time:** 6 min + discussion · **CLO:** 4

**Scenario.** "Guest Wi-Fi" at a conference hotel turns out to bridge to the internal network because an AP was misconfigured during an upgrade. A guest reports being able to see a printer named "FINANCE-HP-02."

**Stakeholders.** Guests; hotel/venue IT; the finance department whose printer is visible.

**Available evidence.** Misconfiguration report; visible printer on guest segment; upgrade was recent (change window).

**Student task.** Containment steps in order, and the change-control gap that let this ship.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-027 — Seven Years of Updates
**Difficulty:** Level 2 · **Domain:** Endpoint hardening · **Time:** 6 min + discussion · **CLO:** 4

**Scenario.** A research instrument PC runs Windows 7 because "the vendor software requires it." It reads results from the instrument over USB and uploads to a share. It is on the staff network.

**Stakeholders.** Researchers (instrument uptime); IT (patching duty); data owners (the share it writes to).

**Available evidence.** EOL OS; vendor dependency; network placement; single-purpose workload.

**Student task.** Design the risk-acceptance package: isolation, monitoring, compensating controls — and name what you would *stop* accepting if the vendor never ships an update.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-028 — The Admin With Two Jobs
**Difficulty:** Level 2 · **Domain:** Access control · **Time:** 6 min + discussion · **CLO:** 7

**Scenario.** The senior DBA also manages backups. A phishing mail compromises her account; the attacker deletes backups, then encrypts. The post-mortem notes she "had always had both roles."

**Stakeholders.** DBA; backup vendor; the organization's recovery posture; auditors.

**Available evidence.** Role combination (production + recovery); phishing entry; backup deletion succeeded.

**Student task.** Name the principle broken (two candidates) and design the separation that survives a small team.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-029 — Time-Boxed Admin
**Difficulty:** Level 2 · **Domain:** Access control · **Time:** 6 min + discussion · **CLO:** 7

**Scenario.** Developers hold standing admin roles "for occasional deployments" (about 20 minutes per week each). Audit flags 40 standing admin accounts; the team resists change ("we need it fast").

**Stakeholders.** Developers; security; the deployment pipeline.

**Available evidence.** Actual usage pattern (20 min/week); audit finding; resistance based on speed.

**Student task.** Design just-in-time access that meets the speed objection, and predict what happens to the audit finding.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-030 — The Offboarding Gap
**Difficulty:** Level 2 · **Domain:** Access control · **Time:** 6 min + discussion · **CLO:** 7

**Scenario.** A departing sysadmin returns his laptop but keeps: VPN access (forgotten), a personal API token for the CI system, and admin rights on a SaaS tool he bought with his card. Three months later, the SaaS tool's renewal fails and its admin email still points to him.

**Stakeholders.** The leaver; IT; the SaaS vendor; the team that depends on the tool.

**Available evidence.** Three forgotten access paths; dependency on leaver's payment method; no exit checklist.

**Student task.** Build the offboarding checklist that catches all three classes (infrastructure, credentials, vendor-owned).

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-031 — Rotating the Shared Secret
**Difficulty:** Level 2 · **Domain:** Cryptography & data protection · **Time:** 6 min + discussion · **CLO:** 5

**Scenario.** A team encrypts nightly database exports with one static key, rotated "never" because rotation means downtime. A laptop holding the key is stolen. Now what?

**Stakeholders.** The team; data owners of the exported data; the laptop owner.

**Available evidence.** Static key; rotation never rehearsed; key on portable device; exports cover 3 years of data.

**Student task.** Design rotation-without-downtime (re-encryption plan), and decide what must happen *today* vs. this quarter.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-032 — The Backup That Never Restored
**Difficulty:** Level 2 · **Domain:** Cryptography & data protection (availability) · **Time:** 6 min + discussion · **CLO:** 5, 7

**Scenario.** "Backups run green every night" per the dashboard. A small fire damages the server room. The restore fails: the backup server held its own encryption keys, and the offsite copy is 14 months old.

**Stakeholders.** The organization; the backup admin; customers awaiting service restoration.

**Available evidence.** Green dashboards; failed restore; key colocation; stale offsite copy.

**Student task.** What did the dashboard actually measure, and design the restore-test program that would have exposed this.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-033 — The Search That Returned Everything
**Difficulty:** Level 2 · **Domain:** Secure web applications (injection) · **Time:** 7 min + discussion · **CLO:** 2

**Scenario.** A department's document search returns all documents when a user types a single quote. The developer says "I will add a filter for quotes." The search also powers the staff directory page.

**Stakeholders.** Users; the developer; owners of the documents (payroll-adjacent data included).

**Available evidence.** Reproducible behavior; proposed fix (blacklist filtering); second consumer of the same query code.

**Student task.** Evaluate the proposed fix, give the correct one, and explain why the directory page matters for the fix's design.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-034 — The Login Form That Trusts the Browser
**Difficulty:** Level 2 · **Domain:** Secure web applications (client-side trust) · **Time:** 6 min + discussion · **CLO:** 2

**Scenario.** A web app validates "premium user" by checking a JavaScript variable and hiding the invoice button otherwise. The server accepts invoice requests without re-checking. A student finds this in the lab app and reports it (responsible disclosure to the course instructor — fictional).

**Stakeholders.** The app owner; paying users; the reporting student.

**Available evidence.** Client-side-only gating; server accepts unvalidated requests; disclosure handled properly.

**Student task.** State the flaw class, the fix, and what the report's severity should be *in this app's context* (free feature behind a paywall, no personal data).

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-035 — One API, Three Consumers
**Difficulty:** Level 2 · **Domain:** API security · **Time:** 7 min + discussion · **CLO:** 2

**Scenario.** A results API serves a mobile app, a public dashboard, and a partner integration. All three use the same API key with full read scope. The partner's key leaks (their fault, your data). Rotating breaks the other two consumers.

**Stakeholders.** Three consumers; the data owner; the API team; the partner.

**Available evidence.** Shared key; full scope for all; leak at the least-trusted consumer; rotation coupling.

**Student task.** Design the key architecture (per-consumer keys, scopes, rotation) and the migration order that avoids downtime.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-036 — The Rateless Endpoint
**Difficulty:** Level 2 · **Domain:** API security · **Time:** 6 min + discussion · **CLO:** 2

**Scenario.** A student-built API has no rate limiting; a data-science class project scrapes it politely at 10 requests/second and discovers the response includes `user_id` fields the web app never shows.

**Stakeholders.** API owner; the scraping class (acting in good faith); users whose `user_id`s leak.

**Available evidence.** No rate limit; over-broad response fields; good-faith mass access; no terms of use.

**Student task.** Name the two flaws (one availability, one confidentiality), their fixes, and the policy artifact that was missing.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-037 — CVEs by Volume
**Difficulty:** Level 2 · **Domain:** Vulnerability prioritization · **Time:** 7 min + discussion · **CLO:** 2, 7

**Scenario.** The weekly scan lists 300 findings. The team patches by "top severity first" and clears 40. A month later, an incident exploits a *medium*-severity finding on an internet-exposed admin panel (known exploit, no patch yet — mitigations exist).

**Stakeholders.** The team; management (reads severity charts); the exploited service's owner.

**Available evidence.** Patch-by-severity policy; the exploited finding's profile (medium/exposed/known-exploit); mitigation availability.

**Student task.** Build the 3-factor prioritization (severity × exploitability × exposure) as a working rule, and place the exploited finding in it.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-038 — The Dashboard of Shame
**Difficulty:** Level 2 · **Domain:** Security monitoring · **Time:** 6 min + discussion · **CLO:** 6

**Scenario.** A SOC posts each analyst's closed-alert count daily. Alert quality drops: analysts close without enrichment, and a real intrusion's early alerts get auto-closed as "no action possible." The dashboard shows record productivity.

**Stakeholders.** Analysts; SOC lead; management; the organization being defended.

**Available evidence.** Metric choice; observed gaming behavior; missed intrusion; productivity optics.

**Student task.** Diagnose the metric failure and propose the two-metric replacement that resists gaming.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-039 — The Alert Nobody Owned
**Difficulty:** Level 2 · **Domain:** Security monitoring · **Time:** 6 min + discussion · **CLO:** 4, 6

**Scenario.** An alert fires nightly at 02:00 for a data-transfer job. Everyone assumes "someone else handles it." It fires for months. One night it is the exfiltration, hidden inside the same pattern.

**Stakeholders.** The job owner; the SOC; the data owner; the attacker (fictional).

**Available evidence.** Baseline alerting with no ownership; attacker exploited an accepted-noise pattern; volume/timing nearly identical.

**Student task.** Design the ownership model for recurring alerts, and the enrichment that would have distinguished the exfil from the job.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-040 — The Two-Hour Window
**Difficulty:** Level 2 · **Domain:** Incident response · **Time:** 7 min + discussion · **CLO:** 7

**Scenario.** Ransomware begins encrypting a file server Saturday 02:00. Detection (rate alert) fires 02:20. The on-call analyst: isolates the server 02:40, then spends until 04:30 deciding whether to preserve evidence or pull the network cable everywhere.

**Stakeholders.** On-call analyst; incident manager; users of adjacent servers (still healthy); legal (evidence).

**Available evidence.** Timeline with three decision points; adjacent systems untouched; encryption ongoing elsewhere? unknown.

**Student task.** Decide the containment strategy for 02:40–04:30 (isolate-only vs. broader) and what evidence you preserve before each step.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-041 — The Tabletop Surprise
**Difficulty:** Level 2 · **Domain:** Incident response · **Time:** 6 min + discussion · **CLO:** 7

**Scenario.** The IR plan says "notify the regulator within 72 hours." During a tabletop, the team realizes nobody can *identify* affected individuals quickly: the data inventory is a spreadsheet last updated 18 months ago, and the notification clock's start point is disputed (detection? confirmation?).

**Stakeholders.** IR team; the regulator; affected users; leadership.

**Available evidence.** Stale inventory; disputed clock start; working notification text otherwise.

**Student task.** Fix the two plan defects (inventory, clock-start definition) and state who decides the start in a real incident.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-042 — The Image That Wasn't
**Difficulty:** Level 2 · **Domain:** Digital forensics · **Time:** 6 min + discussion · **CLO:** 3

**Scenario.** A junior analyst acquires a suspect laptop's disk, then works directly on it "because copying takes hours." Defense (in a mock hearing exercise) asks: how do we know the file timestamps weren't altered during your analysis? The analyst has no answer.

**Stakeholders.** The analyst; the case officer; the (fictional) suspect; the lab's reputation.

**Available evidence.** No working copy; no hash record; altered access times likely.

**Student task.** What must the analyst have done (procedure), and what can still be *partially* salvaged now?

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-043 — The Deleted Meeting
**Difficulty:** Level 2 · **Domain:** Digital forensics · **Time:** 6 min + discussion · **CLO:** 3

**Scenario.** A project lead deletes a contentious calendar meeting and its notes "by accident" the day before an audit. The mail server retains deleted items 30 days; the audit is in 21 days; retention policy says business records are discoverable.

**Stakeholders.** The project lead; the auditor; the records manager; the team.

**Available evidence.** Deletion event logged; retention window covers the audit date; policy on business records.

**Student task.** What does the records manager do, and what does this teach about deletion vs. retention design?

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-044 — The Camera on the Roof
**Difficulty:** Level 2 · **Domain:** IoT & wireless security · **Time:** 7 min + discussion · **CLO:** 4, 7

**Scenario.** A building's 12 IP cameras use default credentials and stream to a vendor cloud for "remote viewing." The vendor's terms permit "service improvement analytics" on footage metadata. IT was never informed; facilities bought them directly.

**Stakeholders.** Facilities; IT; the vendor; everyone the cameras record; the data-protection office.

**Available evidence.** Default credentials; unvetted vendor flow; metadata-analytics terms; procurement bypassed IT.

**Student task.** Build the remediation plan (credentials, network path, vendor terms, procurement process) in priority order.

---

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---

## CS-045 — The Pilot That Scales
**Difficulty:** Level 2 · **Domain:** Governance & risk management · **Time:** 7 min + discussion · **CLO:** 7

**Scenario.** A university pilots an AI proctoring tool in one course. It works; the dean asks to scale to 400 courses by next term. The pilot's DPIA covered one course's context; the tool's vendor has no data-residency guarantee; students were told "pilot, optional."

**Stakeholders.** Dean; students (scale changes consent context); vendor; data-protection office; lecturers.

**Available evidence.** Pilot-only DPIA; scale change; consent context change; missing vendor guarantee.

**Student task.** Decide: what must be re-done before scaling, and what does "optional at pilot" become at mandatory scale?

---

*Model solutions and instructor material: `instructor-materials/instructor-only/case-solutions/level-2-solutions.md`.*

Safety notes. Paper/discussion exercise on a simulated scenario; no system interaction required or permitted.

---
