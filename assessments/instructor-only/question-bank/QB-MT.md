# Question Bank — Midterm Items (Modules 1–4) · ⚠️ INSTRUCTOR-ONLY

Scenario-based and analytical items for the live midterm (`../midterm-paper.md`). Variant B swaps marked items; the swap set is listed at the end. Duplicate-avoidance: none of these appear in weekly quizzes or specimens.

## MT-A (scenario, 6 marks) · CLO-1 · Bloom: Analyze · Difficulty: Medium

The registrar's server (transcripts, staff SSH, backup agent) sits on the campus flat network. A phishing email harvested a staff password; the attacker is enumerating shares.

**(a)** Name the initial access technique in ATT&CK terms (T1566 family) and one probable discovery technique. **[2]**
**(b)** Propose a minimal containment action that preserves evidence. **[2]**
**(c)** Give one preventive and one detective control that would have reduced impact, mapped to STRIDE elements. **[2]**

**Key:** (a) Phishing (T1566) for initial access; accept Network Share Discovery (T1135) or Account Discovery (T1087). (b) Isolate the host/segment at the switch (keep powered; memory intact; note time). (c) Preventive: MFA + phishing-resistant auth (spoofing/credential access); Detective: share-enumeration alert / EDR process telemetry (information disclosure attempt).

## MT-B (design, 6 marks) · CLO-4 · Bloom: Create · Difficulty: Medium

Design the network placement and ruleset summary for: a public web tier, an internal API, a database, and an admin jump host. Default-deny inter-zone. List zones, three rules, and the single most important logging point, justifying each in one line.

**Key:** Zones: DMZ (web), APP (API), DATA (DB), MGMT (jump). Rules: internet→DMZ 443; DMZ→APP (API port, specific SG); MGMT→APP/DATA (SSH/22, from jump only); default-deny elsewhere. Logging: inter-zone firewall (all east-west) — lateral movement is visible only there.

## MT-C (analysis, 8 marks) · CLO-2 · Bloom: Analyze · Difficulty: Hard

Given a code excerpt (provided on the paper):

```python
@app.route("/user")
def get_user():
    uid = request.args.get("id")
    row = db.execute(f"SELECT name, email FROM users WHERE id = {uid}").fetchone()
    return render_template_string("<h1>" + request.args.get("title", "Profile") + "</h1>" + str(row))
```

Identify **all** vulnerabilities with CWE IDs, rank them by impact, and give the corrected code pattern for each.

**Key:** (1) SQL injection — CWE-89 (f-string into execute): parameterized query `WHERE id = ?`. (2) Server-side template injection — CWE-1336 (render_template_string with user input): pass data as context, never concatenate; use static template. (3) Missing object-level authorization — CWE-639 (any caller reads any id): check session user owns/reads id. Impact ranking: SQLi/IDOR = data breach (high); SSTI = RCE potential (highest); accept reasoned orders with justification. Full marks require CWE + fix for each.

## MT-D (analytical, 8 marks) · CLO-1 · Bloom: Evaluate · Difficulty: Hard

A vendor's default deployment: admin UI on port 8080 open to the internet, default credentials, verbose errors, nightly backups to an unprotected share. Apply the attack-surface reduction and least-privilege principles: list five distinct weaknesses, each with the principle violated and the concrete fix.

**Key:** (1) Default creds — secure defaults → force set on first boot. (2) Admin UI exposed — least attack surface → bind to VPN/localhost, or IP-allowlist. (3) Verbose errors — information disclosure → generic errors + server-side logs. (4) Open 8080 — least privilege → reverse proxy on 443, admin path behind auth. (5) Unprotected backups — defense in depth/integrity → encrypted, access-controlled, immutable copy. (Any five coherent pairs; 1.5 marks each when principle is named.)

## MT-E (scenario, 6 marks) · CLO-3 · Bloom: Analyze · Difficulty: Medium

A student lab VM (authorized course target) shows: outbound HTTPS beacon every 60 s to one IP, a new scheduled task `SyncMgr`, and `svchost.exe` running from `%TEMP%`.

**(a)** Give the ATT&CK techniques for the beacon, the task, and the masquerading path. **[3]**
**(b)** Which artifacts would you collect first and why? **[2]**
**(c)** One sentence: why keep the VM powered but disconnected? **[1]**

**Key:** (a) T1071.001 (Web Protocols) / T1053 (Scheduled Task) — Persistence; T1036 (Masquerading) — running from %TEMP% with system-name lookalike. (b) Memory capture + autoruns/task XML + network logs (PCAP): volatile first; persistence config next. (c) Isolation stops C2 while memory stays for forensics.

## MT-F (analytical, 6 marks) · CLO-2 · Bloom: Evaluate · Difficulty: Medium

Same-origin policy: explain in ≤ 150 words why CSRF is possible against a state-changing POST endpoint that relies only on cookies, why CORS headers do not prevent CSRF, and the two defenses that do.

**Key:** Browser sends cookies automatically on cross-site form posts; SOP restricts *reading* responses, not *sending* requests — so the attack writes but never needs to read. CORS governs reading responses, irrelevant to the write. Defenses: CSRF token (attacker cannot read/place it), SameSite cookies (Lax/Strict), accept origin/referer checks.

## MT-G (analytical, 8 marks) · CLO-4 · Bloom: Analyze · Difficulty: Hard

You receive a 5-minute sanitized PCAP (course-provided) from a suspected incident: repeated SYN to 3389 across 200 hosts, then one host shows 40 MB outbound to a single external IP over 445.

**(a)** Characterize both behaviors (scan vs. exfil) with the evidence lines you'd cite. **[4]**
**(b)** Which two telemetry sources beyond the PCAP would confirm the exfil hypothesis? **[2]**
**(c)** Containment order if (a) confirms compromise: three actions. **[2]**

**Key:** (a) Vertical scan RDP (SYN, no completion, many destinations); SMB bulk transfer (single pair, large volume, sustained). (b) Host EDR/netflow on the source; firewall/flow logs for the destination session totals; accept endpoint file-access logs. (c) Isolate source at switch; block destination at egress; preserve PCAP + host memory before remediation.

## MT-H (open-ended, 6 marks) · CLO-1 · Bloom: Evaluate · Difficulty: Medium

Your team has budget for **either** MFA on all student accounts **or** an EDR on all lab machines — not both. Argue a position with a risk-based justification, state what you give up, and name the residual risk you would formally accept.

**Key:** Full-credit logic: MFA kills the credential-access path (highest-frequency vector per the module's threat data); EDR mitigates post-compromise. Defensible either way; must (1) tie to likelihood/impact, (2) name the forgone benefit concretely, (3) propose documented risk acceptance with owner/review — rubric rewards reasoning quality, not the choice.

## Variant B swap table (instructor use)

| A/B item | Variant A | Variant B |
|---|---|---|
| Section B scenario | MT-C (code analysis) | same structure, NoSQL/command-injection excerpt from QB-M2 SA pool re-derived — do not reuse SA-2.1 text |
| Section B scenario | MT-G (PCAP) | same structure, DNS-tunneling capture variant |
| Section D item 4 | MT-H (MFA vs EDR) | "backups vs segmentation" budget dilemma |

Variant B items must be drafted per-term from the same rubric; mark schemes transfer 1:1.
