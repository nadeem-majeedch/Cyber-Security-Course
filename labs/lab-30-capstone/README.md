# Lab 30 — Capstone Working Labs
**Enrichment · Module 8 (L29–L32) · CLO-8 · Duration: 3 × 2 hours (working sessions) · Contract-driven**

## Learning Objectives
1. Implement, verify, and evidence capstone backlog items across three working sessions.
2. Deploy detection content with test events against the capstone environment.
3. Exercise the runbooks in the L31 tabletop and patch them.
4. Assemble the showcase deliverable with the evidence hierarchy (demo > artifact > narrative).

## Prerequisites
Lecture 29 kickoff + signed milestone contract; all prior graded labs (the capstone reuses their techniques).

## Hardware/Software Requirements
The capstone environment (instructor-provisioned per team): web app + analytics job + cloud storage + CI, mirroring the course scenario; team workspace with shared evidence folder.

## Installation and Setup
Per the kickoff briefing: team workspace, evidence folder naming convention (`NN-descriptor-evidence.ext`), contract filed. Session structure mirrors L30 (build) → L31 (tabletop) → L32 (showcase).

## Ethical Authorization and Safety Notes
- The capstone environment is course-owned and team-isolated; cross-team probing is prohibited (and technically firewalled).
- All findings and fixes stay within the team's own environment; the descope log is public to the instructor team by design.
- No real personal data enters the environment: seeded synthetic data only.

## Step-by-Step Student Tasks
**Session 1 (L30 — build):**
1. Implement top-2 backlog items; verify each with before/after probes.
2. Deploy one detection rule + test event; fire it on demand.
3. Demo checkpoint: one verified control + one firing detection.
4. Descope-log entries for anything cut (reason + residual risk + acceptor role).

**Session 2 (L31 — tabletop):**
5. Run the inject deck with the decision log (≥ 10 entries, five fields each).
6. Hot wash: three gaps; patch two runbooks concretely.
7. Residual-risk statement finalized.

**Session 3 (L32 — showcase):**
8. Assemble the defense: problem → model → controls (evidence) → detection demo → tabletop findings.
9. Peer-review exchange (rubric-anchored forms).
10. Final examination (separate instrument).

## Expected Observations
- Teams that capture evidence *as they build* (session 1 discipline) assemble the showcase in minutes; teams that defer it reconstruct for hours.
- The tabletop targets descope items — the cuts you logged become the incident path (by design).

## Questions for Analysis
1. Which backlog item's verification was hardest to evidence, and what does that say about the control's *testability* at design time?
2. If the budget halved, which control goes — and what compensates? (Have this answer ready; the panel asks.)

## Troubleshooting
Environment unreachable → team workspace firewall rule (instructor ticket, 2-minute turnaround — file it early). Evidence folder chaos → the naming convention is mandatory; the rubric's evidence criterion reads it. Detection won't fire → test-event first (Lab 22 discipline); a silent rule is an unverified rule.

## Cleanup Instructions
Per the instructor's end-of-term schedule: export your report/evidence, then stop team containers. The environment is destroyed (not archived) after grades post.

## Submission Requirements
Capstone report (per the L32 rubric structure), evidence folder, decision log, runbook patches, residual-risk statement.

## Expected Outputs / Evidence
Evidence hierarchy enforced: live demo > artifact citation > narrative claim. Claims without artifacts are opinions and grade as such.

---
### Instructor Answer Key (summary — full rubric in `assessments/instructor-only/`)
- Desk-check criteria per session: S1 = two verified items + one firing detection + descope log; S2 = complete decision log + two runbook patches; S3 = defense with evidence-cited claims + named residual risks.
- Rubric bands (20 pts): integration arc (4), evidence quality (4), detection demo (2), tabletop findings honesty (2), defense under questioning (4), peer-form average (4).
- Expected strong answers: budget-halving choices that name the compensating control (e.g., "drop the WAF, keep parameterization + add egress monitoring").

### Assessment Rubric (20 pts — see bands above)
| Criterion | Points |
|---|---|
| Integration arc (model → controls → detection → response) | 4 |
| Evidence quality (hierarchy respected) | 4 |
| Live detection demo | 2 |
| Tabletop findings honesty (residual risks named) | 2 |
| Defense under questioning | 4 |
| Peer-review form average | 4 |
