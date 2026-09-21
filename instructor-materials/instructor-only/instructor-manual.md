# Instructor Manual — Cyber Security (BS CS / BS DS, 7th Semester)

**Audience for this file: teaching staff only.** Student-facing content lives in `lectures/`, `labs/`, and `syllabus.md`. This manual explains how to use the per-lecture teaching guides in `teaching-guides/` and the standing rules that apply to every session.

## 1. Course package map

| What you need | Where it is |
|---|---|
| Per-lecture teaching guides (timing, speaker notes, board activities, difficulties, tips, facilitation, accessibility) | `teaching-guides/lecture-01..32.md` |
| Student lecture notes (the handout students receive) | `lectures/module-0X-*/lecture-NN.md` |
| Detailed session plans (activity logistics, station rotations) | `instructor-materials/instructor-only/lecture-plans/lecture-NN.md` |
| Lab worksheets + starter code | `labs/lab-NN-name/` |
| Checkpoints and keys | `assessments/student/` and `assessments/instructor-only/` |
| Syllabus (student copy) | `syllabus.md` |

## 2. How to run a session (the standing 120-minute pattern)

The teaching guides and session plans assume: **recap 8–12′ → theory with worked examples 40–50′ → break 5′ → lab/activity 35–50′ → consolidation + exit ticket 8–15′**. The first time you teach a guide, rehearse the two live demos it names; they are chosen because they fail instructively when skipped.

## 3. Standing lab-delivery rules (all labs)

1. **Isolation first:** students boot the course VM and take a snapshot before any activity; analysis VMs have no shared folders and use a simulated network (fake DNS/HTTP). Network-activity labs run only against capture files or the lab's own sandboxed targets.
2. **Targets are local and synthetic:** every "attack" activity in this course is performed against course-owned sandboxed targets or provided artifacts (captures, logs, binaries built for teaching). No activity may be aimed at real third-party systems, and tooling used is standard defensive/analysis tooling, not weaponized exploit frameworks.
3. **Evidence discipline:** students capture before/after evidence as they go (screenshots with visible clock, command transcripts). Reports without personally produced evidence do not pass the rubric.
4. **Failure is curriculum:** if a lab step fails for a student, that is a debugging exercise, not a derailment — the guides list expected failure points per lab.
5. **Time-boxing:** each lab block in the guides has a "minimum viable outcome" line. If the class is behind, cut the stretch goal, never the evidence step.

## 4. Discussion facilitation guidance (standing)

- Use the **cold-call-then-volunteer** pattern: give 30 seconds of silent think-time before any name is called; call on volunteers first in Week 1–2, then rotate.
- For ethical debates (L01, L11, L12, L23, L28), assign positions randomly — students argue better when the position is not their own — and close by returning to the course's authorization-first rule.
- Park deep tangent questions on a visible "parking lot" board; answer the top-voted one in the first 5 minutes of the next session.
- The discussion questions in each student note are ordered easy→hard; use the first as a warm-up and the last only if the class has 5+ spare minutes.

## 5. Expected difficulties and how to anticipate them (standing)

Three difficulty classes recur across the course; the per-lecture guides name the specific instances:

1. **Tool-vs-concept confusion** (students think they learned Wireshark, not TCP). Countermeasure: every tool demo ends with a "what did we actually observe?" question.
2. **Premature tool use** — students reaching for attack tooling before modeling. Countermeasure: the threat-model-first sequence in M1 is enforced in M2+ labs (no probing until the worksheet's modeling section is done).
3. **Math/ML anxiety in DS topics for CS students** (and protocol anxiety for DS students). Countermeasure: each track-bridge example in the notes is written for the other track; point cross-track students to it.

## 6. Accessibility considerations (standing; per-lecture specifics in the guides)

- All live demos are paired with a screen-reader-friendly textual description in the student notes ("what you would see" boxes) so visually impaired students get the same content.
- Diagrams in the notes carry alt text; board work is photographed and posted to the LMS after each session.
- Color never encodes meaning alone (critical for the crypto visual labs); label shapes/patterns too.
- Captions/transcripts for any video; the exit ticket has a large-print version on request.
- Lab VMs allow OS-level magnification and keyboard-only navigation for all worksheet steps; if a step cannot be made keyboard-accessible, the guide must offer a script alternative — flag any gap to the course owner.
- Timing flexibility: students registered with disability services get extended checkpoint time in a separate room (papers are in `assessments/instructor-only/` with A/B variants to support this).

## 7. Academic integrity and evidence

Screenshots and transcripts must be the student's own; template answers are fine, duplicated evidence is not. The A/B assessment variants and the randomized station order in labs reduce copying. Discuss the policy in L01 and again before the midterm.

## 8. Answer keys

Checkpoint A–F keys are in `assessments/instructor-only/checkpoint-keys.md`. Where a teaching guide contains exercise answers, the answers are marked **[KEY]** inside the guide and must not be projected. Lab answer checks live in the lab directories' instructor notes where present.

## 9. Safety and legality (standing, non-negotiable)

All practical content is authorized, defensive, and isolated — see rule 3 above. If a student proposes attacking a real target "to test it," redirect to the responsible-disclosure flow taught in L01 and inform the course owner. Materials must never include instructions intended to compromise real-world systems or to evade detection in unauthorized environments; keep everything inside the sandboxed course targets.

## 10. Maintenance notes

- Terminology is standardized in `syllabus.md` §4 (CLO table) and the glossary embedded in each module's first student note; keep new material consistent with it.
- Reference recency rule: prefer sources ≤ 5 years old except foundational texts; verify links each term.
- Report content errors as GitHub issues tagged `content-bug`; do not edit lecture notes mid-week without noting the change in the module overview.
