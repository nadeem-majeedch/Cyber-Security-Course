# Teaching Guide — Lecture 16 (Wireless, VPN, Midterm)
**Instructor-only.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–10 | Review game | 8 rapid questions, teams, mini-whiteboards. |
| 10–30 | Wireless postures | Table walk; evil-twin storyboard. |
| 30–45 | VPN comparison | Split-tunnel sketch; ZTNA contrast. |
| 45–55 | Q&A sweep | Students nominate the two topics to re-explain. |
| 55–60 | Break + exam setup | A/B seating; time announcements. |
| 60–115 | **Midterm** | Closed book; scenario questions. |
| 115–120 | Collection + M5 teaser | One-minute retrospective collected. |

## Board/Projector Activities

- **Board:** posture table (open/PSK/SAE/Enterprise) with invited attacks; the split-tunnel route sketch.
- **Projector:** none during the exam; during review, the M1–M4 concept map as a recap poster.

## Speaker Notes (key beats)

1. WPA3-SAE's win: per-try handshake kills the offline dictionary angle; enterprise adds per-user identity.
2. Evil twin: the attack is *trust*, not crypto — portal domain and certificate tells are the human layer.
3. Split tunnel: name exactly what becomes unmanaged; egress discipline returns.
4. ZTNA vs. VPN: application-level vs. network-level reach.
5. Before the exam: scope, timing, A/B reminder, "answer the scenario, not the keyword."

## Expected Student Difficulties

- Exam anxiety degrades recall in the first 10 minutes. Fix: the review game *is* the warm-up; the Q&A sweep addresses the nominated fears.
- Students answer keywords instead of scenarios. Fix: the instruction "name the control AND say why it applies here" is printed on the paper.
- Time pressure on the last question. Fix: point-per-minute guidance on the cover (e.g., "55 points, 55 minutes").

## Teaching Tips

- The retrospective ("one topic I still fear") is your post-midterm office-hours curriculum — read it before planning help sessions.
- Have a quiet activity ready for early finishers (the M5 "ECB penguin" teaser image, no discussion during others' exams).
- Seating plan for A/B variants printed in advance; alternates by row.

## Answer Keys **[KEY]**

- Midterm A/B: see `assessments/instructor-only/` (midterm papers + marking scheme). Marking notes: scenario items award points for control naming + application reasoning; partial credit table included in the scheme.
- Warm-up answer: hypothesis = evil twin with credential-harvest portal; tells = cert warning, portal domain mismatch, SSID behavior, unexpected latency; detections = BSSID inventory drift, portal-domain mismatch alert.
- Review game answers: built from M1–M4 exit-ticket item pools (see keys A–C and lecture guides 5–15).

## Lab Delivery

No lab this session (exam). The review game and posture-matching use printed cards only.

## Discussion Facilitation

The Q&A sweep: collect nominations on the board, pick the top two, timebox 5 minutes each. If a nomination needs more than 5 minutes, name the office-hours slot — do not over-run into the exam window.

## Accessibility

- Exam: extended-time room, separate invigilation per manual §6; A/B variants support this; large-print and screen-reader-compatible formats prepared in advance from the same source.
- Review game: written answer boards let non-verbal contributors score for their teams.
