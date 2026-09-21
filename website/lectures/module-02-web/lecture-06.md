# Lecture 06 — Injection Attacks: SQL, NoSQL, and Command Injection
**Module 2 · Week 3, Session 2 · 2 hours · CLO-2 (primary), CLO-8 (supporting)**

> **Ethics reminder:** all practice in this course happens only against the sandboxed lab target. The same actions against systems you lack written permission to test are illegal.

## Learning Objectives
1. Explain how untrusted input reaches interpreters (SQL, NoSQL, shell) and why string concatenation fails.
2. Detect injection flaws in code and in behavior (error messages, boolean/timing responses).
3. Remediate with parameterized queries, safe library APIs, and least-privilege data layers.
4. Name the relevant CWEs (89, 78, 943) and the defense hierarchy.

## Key Concepts and Definitions

**Taint flow:** untrusted data (*source*) travels to a dangerous function (*sink*). Injection happens when the sink *interprets* data as code — the boundary between "data" and "program" is crossed.

**SQL injection (CWE-89):** crafted input changes query structure. Patterns you will meet: **boolean-blind** (the page truthfully answers yes/no questions), **time-based** (delays leak answers), **UNION extraction** (results appear in-page). *We study the patterns to detect and defend; exploitation practice is confined to the lab target.*

**Why concatenation fails:** the query is built by string glue, so `' OR '1'='1` changes meaning. **Parameterization (prepared statements)** sends the query structure and the data separately — data can never become structure. This is the *primary* fix.

**NoSQL operator injection (CWE-943):** JSON-style query APIs accept operators (`$gt`, `$where`); user input containing `{"$gt": ""}` can alter matching logic.

**Command injection (CWE-78):** shell metacharacters (`;`, `|`, `$()`) turn arguments into programs. The fix is API design that never invokes a shell: `subprocess.run([...], shell=False)` with argument lists — and allow-lists for anything user-named.

**Defense hierarchy:** parameterize → validate/allow-list → least-privilege data account → error hygiene → (last) WAF.

## Conceptual Diagram

```text
concatenated:   "SELECT * FROM u WHERE name='" + q + "'"   ← structure+data mixed
parameterized:  db.query("SELECT * FROM u WHERE name=?", q) ← structure fixed, data separate

taint flow:  HTTP param (source) ──► string building ──► db.execute (sink)
                                    ✂ validate/allow-list        ▲ parameterize here
```

## Realistic Examples

- **CS track:** a search endpoint built as `"SELECT * FROM items WHERE name LIKE '%" + q + "%'"`. The boolean-blind probe `x' OR '1'='1` returns everything; the parameterized replacement ends the class of flaw.
- **DS track:** an internal tool that shells out as `pip install <user package>` to set up notebooks — a command-injection path into the data platform. Fix: pinned allow-list + list-form subprocess, and least-privilege service identity.

## Common Misconceptions

| Misconception | Correction |
|---|---|
| "Escaping quotes fixes SQLi" | Encoding edge cases, second-order injection, and non-quote contexts break escaping; parameterization is structural. |
| "ORMs prevent injection" | Only when you stay in their query builders; raw-query escape hatches and dynamic `ORDER BY` reintroduce it. |
| "A WAF is the fix" | A WAF is a secondary layer; it sees payloads, not intent, and can be evaded by encoding variants. |
| "Stored procedures are automatically safe" | Only if they parameterize internally; string-building inside the procedure is the same flaw. |

## Classroom Activities

1. **Teaching demo (15 min):** the vulnerable-vs-parameterized login query run side by side on the lab target; students narrate the difference.
2. **Taint-path tracing (10 min):** given a controller snippet, draw source → sink and mark the fix point.
3. **Lab 05 (45 min):** confirm three seeded SQLi points via boolean-blind behavior, fix each with parameterization, verify the fix blocks the original probe (sandbox target only).

## Discussion Questions

1. Why doesn't escaping quotes fully fix SQLi? Give two reasons.
2. When is "the ORM prevents injection" a false claim?
3. Where does a WAF belong in the defense hierarchy, and why last?

## Problem-Solving Exercise

> A legacy reporting endpoint builds a query from three GET parameters and runs a nightly export via a shell command with a user-named output file.
> **Deliverable:** the taint-path diagram for both flows; the two fixes in code; the DB-account privilege change that limits blast radius; one log line that would reveal a blind-SQLi probe.

## Summary

Injection is the canonical input-validation failure: data interpreted as code. Parameterization removes interpretation; least privilege shrinks blast radius; detection closes the loop. Next lecture: flaws where the trust violation is client-side or request-level rather than interpreter-level.

## Exit Ticket

1. Which CWE covers SQL injection? Command injection?
2. Why is `subprocess.run(cmd, shell=True)` dangerous with user input?
3. Name one defense that limits damage even when injection succeeds.

## References

- OWASP Cheat Sheet Series, *SQL Injection Prevention*. https://cheatsheetseries.owasp.org
- MITRE CWE-89, CWE-78, CWE-943. https://cwe.mitre.org
- OWASP, *OWASP Top 10* (current ed.), categories A03 Injection. https://owasp.org
- PostgreSQL/SQLite official docs, prepared statements chapters.
