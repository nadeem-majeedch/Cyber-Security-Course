# Question Bank — Module 3 (L09–L12) · CLO-3 · ⚠️ INSTRUCTOR-ONLY

Used by weekly quizzes Q3 (W3) and makeup packs. Duplicate-avoidance rule: see `README.md`.

## MCQ-3.1

**Topic:** Static triage · **CLO-3** · **Bloom:** Apply · **Difficulty:** Easy · **Week:** 3
**Used in:** Q3

Before executing an unknown sample, the correct first step is:

- A. Run it and watch Task Manager
- B. Compute a cryptographic hash and check it against threat-intelligence sources ✔
- C. Email it to a colleague for a second opinion
- D. Rename the extension to `.txt` and open it

**Explanation:** Hashing identifies known samples without execution; execution without isolation is unacceptable. Key: B.

## MCQ-3.2

**Topic:** Sandbox isolation · **CLO-3** · **Bloom:** Understand · **Difficulty:** Easy · **Week:** 3
**Used in:** Q3

A snapshot/revert capability in a malware VM exists chiefly to:

- A. Speed up analysis
- B. Ensure each sample meets a clean, known state and contamination never persists ✔
- C. Compress disk usage
- D. Bypass antivirus

**Explanation:** Reversion guarantees reproducibility and containment — the analysis environment never becomes a victim or a launchpad. Key: B.

## MCQ-3.3

**Topic:** ATT&CK mapping · **CLO-3** · **Bloom:** Analyze · **Difficulty:** Medium · **Week:** 3
**Used in:** Q3

A sample writes a scheduled task and registers a Run key after first execution. The correct ATT&CK tactic-technique pair:

- A. Defense Evasion — Masquerading
- B. Persistence — Boot or Logon Autostart Execution ✔
- C. Collection — Screen Capture
- D. Exfiltration — Exfiltration Over C2

**Explanation:** Both actions re-establish the implant after restart — autostart persistence. Key: B.

## MCQ-3.4

**Topic:** Ransomware economics · **CLO-3** · **Bloom:** Analyze · **Difficulty:** Medium · **Week:** 3
**Used in:** Q3

Ransomware double extortion is effective because victims face:

- A. Slower backups
- B. Both operational downtime and threatened publication of stolen data ✔
- C. Higher cloud bills
- D. Loss of source code only

**Explanation:** Two levers — restore pressure (downtime) and reputational/legal pressure (leak) — even with perfect backups. Key: B.

## MCQ-3.5

**Topic:** Backup resilience · **CLO-3** · **Bloom:** Apply · **Difficulty:** Medium · **Week:** 3
**Used in:** Q3

Which backup pattern best resists ransomware that deletes online shares?

- A. Nightly full backups on the same NAS
- B. 3-2-1 with one offline/immutable copy ✔
- C. RAID 6 arrays
- D. Weekly ZIP archives on a user desktop

**Explanation:** An offsite, offline/immutable copy survives host- and share-level deletion; RAID is not backup. Key: B.

## MCQ-3.6

**Topic:** Phishing indicators · **CLO-3** · **Bloom:** Apply · **Difficulty:** Easy · **Week:** 3
**Used in:** Q3

A CEO-fraud email asks payroll to wire funds urgently, with pressure not to verify by phone. The strongest red flag:

- A. The logo looks slightly compressed
- B. The request bypasses normal verification and uses urgency/authority ✔
- C. It was sent at 8:59 a.m.
- D. It has a one-line body

**Explanation:** Process bypass + urgency + authority is the core social-engineering pattern; cosmetics are weak signals. Key: B.

## MCQ-3.7

**Topic:** DMARC/SPF/DKIM · **CLO-3** · **Bloom:** Understand · **Difficulty:** Medium · **Week:** 3
**Used in:** Q3

DMARC's contribution to anti-phishing is:

- A. Encrypting message bodies
- B. A policy telling receivers what to do when SPF/DKIM authentication fails ✔
- C. Scanning attachments
- D. Filtering based on subject lines

**Explanation:** SPF/DKIM authenticate; DMARC adds alignment and receiver policy (quarantine/reject). Key: B.

## MCQ-3.8

**Topic:** Awareness metrics · **CLO-3** · **Bloom:** Evaluate · **Difficulty:** Hard · **Week:** 3
**Used in:** Q3

Which metric best measures a phishing-awareness program's effect on organizational risk?

- A. Click rate on simulations
- B. Time-to-report and report rate of suspicious messages ✔
- C. Training-module completion percentage
- D. Number of emails in quarantine

**Explanation:** Reporting behavior converts employees into sensors; click rate alone can be gamed and doesn't capture the response loop. Key: B.

## SA-3.1 (short answer, 6 marks)

**Topic:** Malware analysis plan · **CLO-3** · **Bloom:** Create · **Difficulty:** Medium · **Week:** 3
**Used in:** Q3

Given a suspicious Word-document sample: outline your static-first analysis order (4 steps) and name the isolation controls you rely on (2 marks).

**Key:** Steps: (1) hash + TI lookup; (2) file-type/strings/imports triage; (3) OLE/macro extraction and static review (vba str decode offline); (4) only then controlled detonation in a snapshot VM with fake-net. Isolation: host-only networking, snapshot/revert, no shared folders, out-of-band evidence collection.

## SA-3.2 (short answer, 4 marks)

**Topic:** Ransomware tabletop · **CLO-3** · **Bloom:** Evaluate · **Difficulty:** Hard · **Week:** 3
**Used in:** makeup MT-4 only

A hospital's file servers are encrypting at 3 a.m. List your first three response actions and the one decision that must NOT be improvised.

**Key:** Isolate affected segments (don't power off — preserve memory), activate IR plan/comms channel, preserve evidence (logs, samples) while switching to immutable backups. The ransom decision follows legal/insurance/executive process — never improvised by the responder.
