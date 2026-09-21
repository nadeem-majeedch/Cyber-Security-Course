# Teaching Guide — Lecture 09 (Malware Static Triage)
**Instructor-only.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–08 | M3 hook + safety contract | Read the safety contract aloud; this is the module's license to operate. |
| 08–28 | Isolation setup drill | Every student snapshots; instructor demos the wrong way briefly. |
| 28–50 | Guided static triage | Sample 1 triaged aloud; class co-writes the analyst note. |
| 50–60 | Break | — |
| 60–105 | Lab 08 (samples 2–3) | One analyst note per student; template-driven. |
| 105–115 | Peer cross-check | Pairs swap notes; hunt for missed import stories. |
| 115–120 | Exit ticket + preview | Tease L10: "hypotheses meet evidence." |

## Board/Projector Activities

- **Projector:** the triage tool sequence on sample 1 (hash → strings → imports → entropy), each output annotated.
- **Board:** the analyst-note template skeleton, filled left-to-right during the guided demo.

## Speaker Notes (key beats)

1. State plainly: we analyze only synthetic teaching samples; the skills transfer, the risk stays in the sandbox.
2. Imports are *capability hints*: read the three import groups (network, injection, persistence) as sentences.
3. Entropy: give the 0–8 scale intuition (7.0+ suspicious for code sections); immediately give the false-positive (media/firmware).
4. The note format is the deliverable: identifiers → capabilities → verdict → confidence. Verdict without confidence is noise.

## Expected Student Difficulties

- Students over-claim verdicts from single indicators. Fix: every claim in the note must cite the artifact line that supports it.
- VM setup stalls (virtualization disabled, license prompts). Fix: troubleshooting card at each seat; pre-verify two spares.
- DS students disengage at PE headers. Fix: the feature-table framing — this *is* their ML data, built live.

## Teaching Tips

- Pre-hash all samples and keep the expected hash sheet — catches corrupted downloads fast.
- The "wrong way" demo (shared folder enabled) is 90 seconds and unforgettable; keep it brief but do it.
- Collect one strong analyst note (with permission) as the exemplar for next term.

## Answer Keys **[KEY]**

- Sample 2 expected triage: URL string + `WSAStartup`/`connect` → network-capable, low persistence evidence; verdict "network dropper hypothesis, medium confidence."
- Sample 3 expected triage: Run-key strings + scheduled-task API imports + DDNS domain → persistence + C2; verdict "backdoor hypothesis, medium-high confidence."
- Exit ticket: 1 SHA-256 / ssdeep; 2 `WSAStartup`, `connect` (accept `getaddrinfo`); 3 rollback point + contamination containment.

## Lab Delivery (Lab 08)

- Minimum viable outcome: one complete analyst note per student with artifact citations.
- Expected failure points: strings missing UTF-16 variants (remind the flag); entropy tool disagreement — accept any documented method.

## Discussion Facilitation

Q2 (high entropy) rewards the three-explanation habit (packed code, encrypted payload, non-code content). Q3 (what static can never tell) sets up L10 perfectly — collect answers and re-ask them after the sandbox run next session.

## Accessibility

- Tool outputs (hex/ASCII dumps) are hard screen-reader terrain: provide the annotated text transcript of sample 1's outputs; pair visually impaired students with a scribe for the cross-check step.
- The isolation drill: step cards with numbered large-print checklist; keyboard-only paths verified per manual §6.
