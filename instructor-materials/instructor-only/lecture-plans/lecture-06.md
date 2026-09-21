# Lecture 06 — Injection Attacks: SQL, NoSQL, and Command Injection
**Module M2 · Week 3, Session 2 · 120 min · CLO-2 (primary) · CLO-8 (supporting)**

## Learning Objectives
1. Explain how untrusted input reaches interpreters (SQL, NoSQL, shell) and why concatenation fails.
2. Detect injection flaws in code and in live behavior (error messages, timing, boolean responses).
3. Remediate with parameterized queries/prepared statements, ORM-safe patterns, and library APIs that avoid shell interpretation.
4. Apply defense-in-depth to data layers: least-privilege DB accounts, error hygiene, WAF as a secondary layer (CWE-89, CWE-78, CWE-943).

## Key Concepts
- Taint flow: source → sink; interpreter context switching (string vs. code)
- SQL injection: classic, boolean-blind, time-based; UNION-based extraction (concepts only — practiced only against the lab target)
- NoSQL injection: operator injection in Mongo-style queries (`$gt`, `$where`)
- Command injection: shell metacharacters; argument-injection; the safe-API alternative (`subprocess` list form, `execve`-style)
- Remediation hierarchy: parameterize → validate/allow-list → least-privilege → monitor

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–08 | Recap L05 exit-ticket answers | Q&A |
| 08–35 | Live teaching demo against the course-vulnerable app: one parameterized vs. one concatenated login query — show behavior difference; walk the taint path in code | Live code demo |
| 35–55 | The injection family tour: SQL variants, NoSQL operators, command injection; CWE IDs on every slide | Slides |
| 55–60 | Break | — |
| 60–105 | **Lab block (Lab 05):** against the sandboxed vulnerable app — (a) confirm 3 seeded SQLi points via boolean-blind behavior, (b) exploit ONLY the provided target, (c) fix each in the starter repo with parameterization, (d) re-test that the fix holds | Hands-on (sandboxed target only) |
| 105–115 | Remediation code review: two student fixes projected; class checks for residual sink paths | Code review |
| 115–120 | Exit ticket; ethics reminder (target = lab only); preview L07 | Q&A |

## Examples
- **CS track:** search feature built with `"SELECT * FROM items WHERE name LIKE '%" + q + "%'"` — show the boolean-blind probe `x' OR '1'='1` and the parameterized replacement.
- **DS track:** a notebook that shells out to `pip install ` + user-supplied package name for an internal tool — command injection into a data pipeline; fix with `subprocess.run([...], shell=False)` and pinned allow-list.

## Discussion Questions
1. Why doesn't escaping quotes fully fix SQLi? (context switching, encoding, second-order injection)
2. An ORM "prevents injection" — when is that claim false? (raw query escape hatches, dynamic ORDER BY)
3. Where does a WAF belong in the defense hierarchy, and why is it last?

## Student Activity
Fix-and-verify pairs: each pair owns one seeded sink, writes the parameterized fix, and verifies another pair's fix by attempting their documented probe against the fixed build — inside the sandbox only.

## Problem-Solving Scenario
> Legacy reporting endpoint: builds a query from three GET parameters and runs a nightly export via shell with user-named output file. Produce: the taint-path diagram (source→sink for both flows), the two fixes in code, the DB-account privilege change that limits blast radius, and one detection idea (what log line would a blind SQLi probe leave?).

## Summary
Injection is the canonical input-validation failure: data interpreted as code. Parameterization removes interpretation; least privilege shrinks the blast radius; detection closes the loop. L07 moves from interpreter abuse to client-side and request-forgery flaws.

## Formative Assessment
1. Which CWE covers SQL injection? Command injection?
2. Why is `subprocess.run(cmd, shell=True)` dangerous with user input?
3. Name one defense that limits damage even when injection succeeds.

## Required Resources
- `labs/lab-05-injection/` vulnerable target + starter repo (sandboxed, local-only)
- OWASP SQL Injection Prevention Cheat Sheet; CWE-89/78/943 pages
- Code-review checklist handout
- CLO mapping: **CLO-2** (objectives 1–4); **CLO-8** seed (layered remediation).
