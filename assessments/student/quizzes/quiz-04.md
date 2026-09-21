# Quiz 4 — Checkpoint B (Week 4, L08) · Module 2: Web Application Security
**Graded formative · recorded /10 · 12 minutes · CLO-2 · Closed book.**

1. A news site lets readers post comments. Name the CWE for SQL injection and the CWE for operating-system command injection. **[1]**

2. In Python, `subprocess.run(cmd, shell=True)` with user-supplied `cmd` is exploitable, while an argument-list call without `shell=True` is not. Why, in one sentence? **[1]**

3. After fixing a report-generation endpoint, the developer asks which *single* remediation matters most for injection resilience at the database layer. Name it. (Accept any secondary compensating control for half credit.) **[1]**

4. A stored payload executes only when the client-side script inserts it into the DOM later — never on the server-rendered page. Which XSS type is this? **[1]**

5. Name the two client-side defenses that, together, block a cross-site request from spending a victim's session on a funds-transfer endpoint. **[1]**

6. Invoice links look like `/invoice/1041`, `/invoice/1042`. What property of these identifiers makes the access-control failure easy to exploit? **[1]**

7. *(Scenario, 2 marks)* A profile page builds its heading with `render_template_string("<h1>" + nickname + "</h1>")`. Identify the vulnerability class (CWE) and state the corrected pattern in one sentence.

8. *(Scenario, 2 marks)* The search endpoint concatenates the query into SQL, and the DB account is `root`. Give the fix and the hardening measure, and say which STRIDE element the flaw exposes.

*Scoring: 1 mark per numbered item; recorded as a fraction of 10.*
