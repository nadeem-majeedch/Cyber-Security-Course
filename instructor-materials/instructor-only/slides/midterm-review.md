---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · Midterm Review · M1–M4'
---

<!-- _class: lead -->
# Midterm Review — Modules 1–4
**Strategy session · 45 min · pairs with `../../student/specimen-midterm.md`**

<!--
TIMING: run in L16 slot (plan §timing). This deck walks the SPECIMEN strategy; live paper items differ.
-->

---

# What the midterm tests

| Module | Core skill | Where it shows up |
|---|---|---|
| M1 | classify, model, rank | MCQ 1–5, Section D |
| M2 | flaw mechanics + fixes | MCQ 6–7, Section C |
| M3 | static-first discipline | MCQ 8, Section B |
| M4 | design + monitor | MCQ 9–10, Section B/C |

*Describe: coverage map linking modules to sections.*

<!--
4 min. Students self-locate their weak module and study that block first.
-->

---

# Section strategy

```
A (MCQ):    30 s each, flag & return — never stall
B (6-mark): name → mechanism → fix → tradeoff (4 beats)
C (choose 2 of 3): READ ALL THREE FIRST
D (essay):  position + cost + residual risk + owner
```

*Describe: per-section timing and answer templates; the four beats of B apply to nearly every scenario item.*

|
<!--
8 min. The four beats ARE the marking scheme's row structure — say so.
-->
|

---

# Worked walk-through (specimen Q13 pattern)

```
prompt: code excerpt → identify, rank, fix
answer shape:  CWE-89 + parameterize    (mechanism 1 line)
               CWE-1336 + static template
               CWE-639 + object authz
               ranking + WHY (impact × likelihood)
```

*Describe: a model answer skeleton for the code-analysis item; CWE plus one-line mechanism plus fix, then a justified ranking.*

<!--
10 min live walk-through on the board using the specimen's structure (not live items).
-->

---

# Common failure patterns (from prior checkpoints)

```
writing "SQL injection" without the FIX      → half marks
unordered IR steps                           → order matters
"we'd use a WAF" as the primary answer       → compensating only
Section D with no stated residual risk       → ceiling ~60%
```

*Describe: four recurring mark-losing patterns with their consequences.*

|
<!--
Drawn from checkpoint item analysis — real patterns from THIS class's checkpoint data. 8 min.
-->
|

---

# The night-before checklist

- Lecture notes' exit tickets (they mirror item types)
- Lab fix-verify pairs (Section C loves them)
- Checkpoint keys discussed in class — revisit those items
- Sleep beats cramming; the paper rewards reasoning, not recall

<!--
5 min. Close with confidence framing: the class's checkpoint median.
-->

---

# Q&A

Bring the specimen; mark it together.

<!--
Remaining time: open Q&A on the specimen paper.
-->

---

# References

- `../../student/specimen-midterm.md`; checkpoint keys (instructor use only)
