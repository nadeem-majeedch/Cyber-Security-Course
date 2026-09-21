---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L06 · Module 2 · Week 3'
---

<!-- _class: lead -->
# Lecture 06 — Web Security II
## Injection Attacks: SQL & Command
**Module 2 · Week 3 · 120 min · CLO-2 (primary), CLO-8 (supporting)**

<!--
TIMING: 1 min. Hook: single line — `"SELECT * FROM users WHERE id = " + input` — "who owns the syntax here?"
-->

---

# Learning Objectives

1. Explain how injection merges **data with code**
2. Demonstrate SQLi mechanics on the sandbox app
3. Remediate with **parameterization** + least-priv DB
4. Recognize NoSQL & command-injection variants

<!--
L06 is the CLO-2 anchor lab (Lab 05). 3 min.
-->

---

# SQL injection mechanics

```
Input:   1033' OR '1'='1
Query:   SELECT ... WHERE id='1033' OR '1'='1'
Effect:  WHERE clause always true → all rows
```

*Describe: three lines showing input, the assembled query, and the resulting always-true condition.*

<!--
Walk char by char. MISCONCEPTION: "quotes are the problem" — the problem is CONCATENATION. 6 min.
-->

---

# The fix hierarchy

```
1. Parameterized queries      ← structural fix
2. Least-privilege DB account  ← damage bound
3. Error hygiene               ← info leak cut
4. WAF                         ← compensating only
```

*Describe: four-step ordered list; step 1 removes the bug class, step 4 only slows it.*

<!--
Order matters — WAF last. Recall MCQ-2.2 and the checkpoint B item. 4 min.
-->

---

# Command injection

```python
subprocess.run("ping " + host, shell=True)   # vulnerable
subprocess.run(["ping", host])               # fixed
```

*Describe: two Python lines — the first interpolates into a shell string, the second passes an argument list without shell interpretation.*

<!--
shell=True = metacharacter interpreter. CWE-78 vs CWE-89 — both on checkpoint B. 4 min.
-->

---

# CS example — ORM is not immunity

- Raw `.raw()` calls and string-built ORDER BY skip the ORM's escaping
- Audit rule: grep for `raw(`, `extra(`, f-string SQL

<!--
2 min.
-->

---

# DS example — pandas to SQL pipeline

- Notebook builds query from a form value → same bug in analytics clothing
- Fix: parameter binding in SQLAlchemy; read-only DB role for dashboards

<!--
2 min. DS students meet this in their own stack.
-->

---

# Lab demo — Lab 05 (injection)

- Instructor demonstrates the seeded SQLi in the sandbox app, then applies the fix and re-tests
- **MVO:** working exploit → fixed query → exploit fails
- Sandbox app only; fix-verify pairs mandatory

<!--
DEMO 6 min. This fix-then-verify rhythm is the course signature — name it.
-->

---

# Case session

**CS-033 "Search that returned everything"** (Level 2 · Secure web applications)

→ classify the flaw (CWE), rank against a second finding

<!--
10 min. Model ties ranking to the L02 matrix.
-->

---

# Wrap-up & exit ticket

- Injection = data/code merge; parameterize; bound the blast radius
- **Exit:** rewrite one vulnerable line two ways (param + list args)

<!--
Close 110. Preview L07: XSS/CSRF/SSRF/IDOR.
-->

---

# References

- OWASP SQL Injection Prevention Cheat Sheet; CWE-89, CWE-78
- Lecture plan lecture-06; Lab 05
