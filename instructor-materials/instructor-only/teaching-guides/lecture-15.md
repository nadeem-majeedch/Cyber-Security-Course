# Teaching Guide — Lecture 15 (IDS/IPS, SIEM, Alert Triage)
**Instructor-only.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–08 | Recap: reachability highlights | Matrix photos from teams. |
| 08–28 | Rule anatomy + live authoring | Write the scan rule together; test on capture B. |
| 28–48 | Signature vs. anomaly | Two failure stories; placement trade-offs. |
| 48–60 | Break | — |
| 60–100 | Lab 14 (SIEM triage simulation) | 12 alerts; roles: analyst, lead, auditor. |
| 100–110 | Metrics | TPR/FPR vs. answer sheet; coverage gaps. |
| 110–120 | Exit ticket + preview | Midterm scope walkthrough (5 min). |

## Board/Projector Activities

- **Projector:** the rule written live in the editor; the capture-B test firing the alert.
- **Board:** the SIEM pipeline diagram; the triage queue table filled with verdicts during debrief.

## Speaker Notes (key beats)

1. Placement decides visibility: an IDS behind the VPN never sees the internet handshake — placement is analysis design.
2. Signature vs. anomaly failure modes: novelty vs. drift; both need enrichment to become decisions.
3. Rule anatomy: action/proto/src→dst/options; sid conventions; scoping ($HOME_NET over any) is quality.
4. Enrichment turns an IP into a decision: asset criticality, user context, TI verdict.
5. Verdict vocabulary: TP / FP / BTP — benign true positives are real work, document and suppress with justification.
6. Midterm scope walkthrough: CLO-1..4, scenario format, timing.

## Expected Student Difficulties

- Rules written with `any` everywhere. Fix: the scoping rule — narrow beats broad; the FP test proves it.
- Triage paralysis (all alerts "important"). Fix: the verdict-first protocol — classify, then enrich, then act.
- Students fear the metrics math. Fix: TPR/FPR from the 12-alert answer sheet is arithmetic; do it together.

## Teaching Tips

- Seed one alert that *looks* benign but is the TP (the beacon host's scheduled-task alert) — teaches "verify, don't pattern-match."
- The printer FP-storm teaches rule hygiene: the fix (scope, threshold) is the lesson, not the annoyance.
- Midterm prep: 5 minutes, explicit scope, no surprises — anxiety down, performance up.

## Answer Keys **[KEY]**

- Triage answer sheet (12 alerts): escalate = host with beacon-45s + scheduled task + egress spike (chain = persistence + C2 + collection/exfil indicators); printer storm = FP (suppression + rule scope fix); dev's nmap = BTP (documented scan); brute-force against lab account = BTP with lockout check; remaining per your seed design.
- Rule fix for printer storm: add threshold + scope to printer-zone assets, or suppress with justification per asset list.
- Exit ticket: 1 sid in options, local range reserved (e.g., 1000000+); 2 anomaly detection; 3 asset criticality + user context (accept TI verdict).

## Lab Delivery (Lab 14)

- Minimum viable outcome: 12 verdicts documented with evidence; one escalation justified.
- Expected failure points: students skip enrichment and guess; require the enrichment column filled before verdicts are accepted.

## Discussion Facilitation

Q3 (auto-close low severity) is the values question — what is silently accepted? Let them name the risk in one sentence each; park the ML pre-sort idea (their own suggestion will surface) for L21.

## Accessibility

- Triage simulation: the queue exists as structured text (CSV) alongside the UI so screen-reader users triage from the same data.
- Metrics: provide the answer sheet as a spreadsheet with formula scaffolding.
- Midtime accommodations for the practice portions per manual §6.
