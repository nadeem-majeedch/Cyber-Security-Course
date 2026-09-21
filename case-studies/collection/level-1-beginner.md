# Case Collection — Level 1: Beginner (CS-001–020)

> Simulated teaching scenarios; all organizations, people, and data are fictional. Use the classroom method: projector → 5 minutes group reasoning → discussion → model solution → tradeoffs. Solution material is instructor-only.

---

## CS-001 — The Club Committee Password
**Difficulty:** Level 1 · **Domain:** Password & authentication security · **Time:** 5 min + discussion · **CLO:** 1

**Scenario.** A 12-person student media club shares one login for its website CMS. The password is the club name plus "123", has not changed in three years, and is written on the whiteboard "for new members."

**Stakeholders.** Club members (12), the student union IT office (hosts the CMS), anyone whose content is published under club identity.

**Available evidence.** Login is shared; password strength obvious; whiteboard exposure; no individual identity in logs (shared login = no attribution).

**Student task.** Name the three biggest risks, the CIA property each hits, and the one change you would make first.

**Common pitfalls to avoid in your answer.** Solving only the password strength while keeping the *sharing* — the sharing is the structural risk.

**Safety notes.** Discussion only; no demonstration required.

---

## CS-002 — Same Password Everywhere
**Difficulty:** Level 1 · **Domain:** Password & authentication security · **Time:** 5 min + discussion · **CLO:** 1

**Scenario.** A student uses one password for the campus LMS, a gaming forum, and a shopping site. The forum announces (publicly, in its own disclosure) that its password database was stolen. The student says: "the forum is not important."

**Stakeholders.** The student; the university (LMS holds coursework and personal data); the shopping site (payment details).

**Available evidence.** Public disclosure by the forum; identical password across services; LMS supports MFA (unused).

**Student task.** Explain the attack path from "unimportant" site to important accounts, and rank two mitigations.

**Common pitfalls.** Answering "use a stronger password" instead of addressing reuse and MFA.

**Safety notes.** Discussion only.

---

## CS-003 — The Suspended Library Account
**Difficulty:** Level 1 · **Domain:** Phishing & social engineering · **Time:** 5 min + discussion · **CLO:** 1, 3

**Scenario.** An email says: "Your library account will be suspended in 24 hours. Verify now." The link shows `university-library.com` while the real portal is `library.university.edu`. The email greets "Dear Student" and your mail client shows it passed SPF.

**Stakeholders.** Students; the library; the university security team.

**Available evidence.** The two domains; generic greeting; 24-hour urgency; SPF passing.

**Student task.** Decide what you would do, then explain which clues matter and why SPF passing does not clear the mail.

**Common pitfalls.** Treating "SPF passed" as authenticity of the sender identity; clicking to "check safely."

**Safety notes.** Do not click the link even in a lab VM during discussion; reason from the headers shown on the slide.

---

## CS-004 — The 2 a.m. Approval Prompt
**Difficulty:** Level 1 · **Domain:** Phishing & social engineering (MFA fatigue) · **Time:** 5 min + discussion · **CLO:** 1, 3

**Scenario.** Your phone shows an MFA push: "Approve sign-in from Firefox on Windows" at 2:07 a.m. You are in bed. A second prompt arrives. Then a third.

**Stakeholders.** You; the university identity provider; whoever is typing your password somewhere.

**Available evidence.** Three prompts; wrong time; device description you don't own; repeated prompts (implies password is already known).

**Student task.** What do you do, in order? Why is "the attacker already has your password" the key inference?

**Common pitfalls.** Approving one prompt to "make it stop"; treating it as a glitch.

**Safety notes.** Discussion only.

---

## CS-005 — Printers on the Staff Network
**Difficulty:** Level 1 · **Domain:** Network segmentation · **Time:** 5 min + discussion · **CLO:** 4

**Scenario.** A department connects its six multifunction printers to the staff VLAN "so everyone can print." Printers are web-managed, and the manuals note they cache user credentials for scan-to-email.

**Stakeholders.** Staff; department IT; anyone who can reach the printer web UI.

**Available evidence.** Printers on staff VLAN; web management enabled; credential caching feature documented.

**Student task.** Why does printer placement matter for *credential* risk, and what is the minimal segmentation fix?

**Common pitfalls.** Treating printers as harmless peripherals; proposing a full redesign when a VLAN move plus rules is enough.

**Safety notes.** Discussion only.

---

## CS-006 — The Logged-In Lab Machine
**Difficulty:** Level 1 · **Domain:** Endpoint hardening · **Time:** 5 min + discussion · **CLO:** 1

**Scenario.** A lab PC in the 24-hour room is left logged in as a student with local administrator rights, screen unlocked, at 3 a.m. The room has no camera.

**Stakeholders.** The logged-in student; every user of that machine; the university (software licensing, data on disk).

**Available evidence.** Unlocked session; admin rights; unattended; no camera.

**Student task.** List the harms that follow in the next hour, and the two controls (technical + procedural) that prevent the situation.

**Common pitfalls.** Only proposing "lock your screen" without the admin-rights and session-timeout layers.

**Safety notes.** Discussion only.

---

## CS-007 — The USB Stick in the Library
**Difficulty:** Level 1 · **Domain:** Endpoint hardening (removable media) · **Time:** 5 min + discussion · **CLO:** 1

**Scenario.** A USB stick labeled "Coursework Backup 2024" is found in the library. A student plans to plug it in "to find the owner."

**Stakeholders.** The student; the owner (if reachable); the university (malware risk, privacy of the owner's files).

**Available evidence.** Unlabeled origin; the label invites curiosity; plugging unknown media executes nothing visible but can auto-run or exploit flaws.

**Student task.** What are the risks, what should the student do instead, and what should the university's procedure be?

**Common pitfalls.** "Modern systems disable autorun so it's safe" — auto-run is not the only risk path; the correct answer is procedural.

**Safety notes.** Never test unknown media on any machine in class; discussion only.

---

## CS-008 — Cloned Access for the New Hire
**Difficulty:** Level 1 · **Domain:** Access control · **Time:** 5 min + discussion · **CLO:** 1, 7

**Scenario.** A new lab assistant is granted "the same access as Tom," a senior assistant of five years, because it is faster than defining the role.

**Stakeholders.** The new assistant; Tom; the lab's data owners; IT.

**Available evidence.** Cloning approach; Tom's access accumulated over five years (projects since closed).

**Student task.** Name the principle violated, the two risks created, and the cheap correct alternative.

**Common pitfalls.** Treating it as an HR inconvenience rather than a least-privilege violation.

**Safety notes.** Discussion only.

---

## CS-009 — One Account, Three Interns
**Difficulty:** Level 1 · **Domain:** Access control · **Time:** 5 min + discussion · **CLO:** 1

**Scenario.** Three summer interns share one database account "because provisioning takes two weeks." At the end of summer, a table of test data is found modified; nobody can say who.

**Stakeholders.** The interns; the data owner; the DBA; the team lead.

**Available evidence.** Shared account; no attribution in logs; modification discovered after the fact.

**Student task.** Which CIA properties failed, and what is the minimum change that fixes accountability?

**Common pitfalls.** Blaming interns without fixing the structural attribution gap.

**Safety notes.** Discussion only.

---

## CS-010 — Grades by Email
**Difficulty:** Level 1 · **Domain:** Cryptography & data protection · **Time:** 5 min + discussion · **CLO:** 5, 7

**Scenario.** A lecturer emails a spreadsheet of 240 students' names, matriculation numbers, and grades to a colleague — unencrypted, with three colleagues cc'd in error on a similar surname.

**Stakeholders.** 240 students; the lecturer; the department's data-protection officer.

**Available evidence.** Unencrypted attachment; misdirected copy; personal data at scale.

**Student task.** Classify the incident (what just happened?), and propose the two controls that prevent a repeat.

**Common pitfalls.** Focusing on the typo rather than the lack of a protected channel and distribution checks.

**Safety notes.** Discussion only.

---

## CS-011 — The Password on the Router
**Difficulty:** Level 1 · **Domain:** Cryptography & data protection (secrets handling) · **Time:** 5 min + discussion · **CLO:** 5

**Scenario.** A department's Wi-Fi password is on a sticky note on the access point in a shared office. Twelve people have the password; three have left the university.

**Stakeholders.** Department staff; leavers; IT (network ownership).

**Available evidence.** Physical exposure; unrotated credential; ex-staff retain knowledge.

**Student task.** What does the sticky note cost, and what are the two fixes (one technical, one procedural)?

**Common pitfalls.** Only saying "remove the note" without handling leavers and rotation.

**Safety notes.** Discussion only.

---

## CS-012 — The Club Site Login Page
**Difficulty:** Level 1 · **Domain:** Secure web applications · **Time:** 5 min + discussion · **CLO:** 2

**Scenario.** A student club's website serves its login form over `http://` (no TLS). The club says "there is nothing secret on the site."

**Stakeholders.** Members logging in; the club; the hoster (offers free TLS).

**Available evidence.** No TLS on the login route; password submitted in cleartext; TLS available at zero cost.

**Student task.** What exactly is exposed, to whom, and what is the fix (including the one-line config change)?

**Common pitfalls.** "Nothing secret" ignores that the *password itself* is the secret being transmitted.

**Safety notes.** If demonstrating, use only a loopback demo app — never intercept a real network.

---

## CS-013 — Guessable Recovery Answers
**Difficulty:** Level 1 · **Domain:** Secure web applications (account recovery) · **Time:** 5 min + discussion · **CLO:** 2

**Scenario.** A platform's account recovery asks: mother's maiden name, first school, favorite football team. A classmate you barely know resets your account in four minutes from your public social profile.

**Stakeholders.** The account owner; the platform; everyone whose recovery answers are public.

**Available evidence.** The three questions; public social profiles; successful four-minute reset.

**Student task.** Why is knowledge-based recovery broken by design, and what are two better designs?

**Common pitfalls.** Proposing "harder questions" — the class of answer is the problem, not the difficulty.

**Safety notes.** Discussion only.

---

## CS-014 — The Key in the Repository
**Difficulty:** Level 1 · **Domain:** API security · **Time:** 5 min + discussion · **CLO:** 2, 5

**Scenario.** A student project pushes a mapping-service API key directly in the source code to a public repository. It works; the demo impresses; the key stays.

**Stakeholders.** The student (pays the bill); the service provider; anyone who finds the key.

**Available evidence.** Public repo; key in code; no rotation; automated scrapers scan public repos for exactly this.

**Student task.** What happens next (realistic sequence), and what are the three fixes in order?

**Common pitfalls.** "Delete it from the file" — the key persists in history and in clones; the order is revoke → rotate → redesign.

**Safety notes.** Discussion only.

---

## CS-015 — Two Findings, One Weekend
**Difficulty:** Level 1 · **Domain:** Vulnerability prioritization · **Time:** 5 min + discussion · **CLO:** 2, 7

**Scenario.** A scan reports: (A) a web framework with a critical vulnerability, public exploit available, service exposed to the internet; (B) an internal file server with an outdated TLS library, no known exploit, not exposed. The team can patch one before Monday.

**Stakeholders.** The team; the service owners; users of both systems.

**Available evidence.** Severity, exploitability, and exposure for both findings.

**Student task.** Which do you patch and why — and what do you *do* about the other one meanwhile?

**Common pitfalls.** Patching by severity score alone; ignoring exposure and exploitability; forgetting interim mitigation for the deferred item.

**Safety notes.** Discussion only.

---

## CS-016 — Failures Nobody Watched
**Difficulty:** Level 1 · **Domain:** Security monitoring · **Time:** 5 min + discussion · **CLO:** 4, 6

**Scenario.** After a compromise is discovered, review shows 500 failed logins on one account over two weeks — logged correctly, never looked at. The logs "were working fine."

**Stakeholders.** The account owner; the SOC/IT; management (assumed "we have logs = we detect").

**Available evidence.** Logs complete; no alerting; no review ownership; 14-day attack window.

**Student task.** Which capability was missing between logging and detection, and what is the minimal monitoring fix?

**Common pitfalls.** "Buy a SIEM" as the first answer — a threshold or budget alert may fix this class today.

**Safety notes.** Discussion only.

---

## CS-017 — The Laptop on the Bus
**Difficulty:** Level 1 · **Domain:** Incident response · **Time:** 5 min + discussion · **CLO:** 7

**Scenario.** A lecturer's laptop holding 60 students' project submissions (names, emails, draft grades) is left on a bus. It was password-protected; the disk was not encrypted. Reporting happened "the next morning."

**Stakeholders.** 60 students; the lecturer; the department; the data-protection officer.

**Available evidence.** Unencrypted disk; sensitive data present; delay in reporting.

**Student task.** What are the first three response actions, and what should have prevented this?

**Common pitfalls.** Full-disk encryption as the only answer — the response actions (inventory, notification duty, credential resets) matter *now*.

**Safety notes.** Discussion only.

---

## CS-018 — Who Deleted the File?
**Difficulty:** Level 1 · **Domain:** Digital forensics · **Time:** 5 min + discussion · **CLO:** 3

**Scenario.** A shared drive's project folder is missing its final report. The team suspects accidents. The file server logs every delete with username and timestamp, and the retention policy keeps logs for 90 days.

**Stakeholders.** The team; the (unknown) deleter; IT forensics.

**Available evidence.** Complete delete logging; retention window; no versioning on the share.

**Student task.** What would you look at, in what order — and what does the absence of versioning mean for recovery?

**Common pitfalls.** Jumping to accusations before establishing what the logs can and cannot prove (a delete event ≠ intent).

**Safety notes.** Discussion only.

---

## CS-019 — The Smart TV on Staff Wi-Fi
**Difficulty:** Level 1 · **Domain:** IoT & wireless security · **Time:** 5 min + discussion · **CLO:** 4, 7

**Scenario.** A lecture room's smart TV joins the staff Wi-Fi for "easy casting." The TV runs a two-year-old firmware, phones home to its vendor, and cannot join MFA or device management.

**Stakeholders.** Lecturers (casting convenience); IT (network ownership); the vendor.

**Available evidence.** Old firmware; unmanaged device on staff network; outbound telemetry; no management hooks.

**Student task.** Place the TV in a zone: which, why, and what two rules would you write for it?

**Common pitfalls.** Banning the device outright without weighing the legitimate use case — segmentation with purpose-built rules is the balanced answer.

**Safety notes.** Discussion only.

---

## CS-020 — The Startup With No Rules
**Difficulty:** Level 1 · **Domain:** Governance & risk management · **Time:** 5 min + discussion · **CLO:** 7

**Scenario.** A five-person startup has no acceptable-use policy, no laptop rules, and no offboarding checklist. The founder says "policies are for big companies." A departing intern still has the production dashboard bookmarked — and the password saved in the browser.

**Stakeholders.** The founder; employees; the departing intern; customers whose data the dashboard shows.

**Available evidence.** No policy set; leaver retains working access; single-dashboard access to customer data.

**Student task.** Name the three minimal governance artifacts this five-person team actually needs, in priority order.

**Common pitfalls.** Drafting enterprise-grade policy libraries — the level-appropriate answer is three pages, not three hundred.

**Safety notes.** Discussion only.

---

*Model solutions, expected reasoning, alternatives, tradeoffs, common mistakes, and discussion prompts for these cases: instructor-only tier (`instructor-materials/instructor-only/case-solutions/level-1-solutions.md`).*
