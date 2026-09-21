#!/usr/bin/env python3
"""One-click semester calendar generator for the Cyber Security course.

Generates from the repository's ACTUAL content:
  - lecture titles  -> parsed from lectures/module-*/lecture-NN.md H1 lines
  - labs            -> labs/README.md crosswalk (authoritative)
  - assessments     -> syllabus.md §6/§9 + assessments/student/quizzes
  - case studies    -> per-lecture case-session slides (instructor decks)
  - CLO mapping     -> syllabus.md §5

Outputs (default calendar/generated/):
  student-calendar.md        student-friendly weekly view (Markdown)
  student-calendar.html      printable A4 HTML (student view)
  instructor-calendar.md     instructor planning view (Markdown)
  calendar-semester.json     machine-readable (LMS import)

Usage:
  python calendar/tools/generate_calendar.py --start 2026-09-07
  python calendar/tools/generate_calendar.py --start 2026-09-07 --validate-only
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PREFIX = "../.."  # relative path from the output dir to the repo root (recomputed in main)

# --------------------------------------------------------------------------
# Content model (sourced from the repository; see README for provenance)
# --------------------------------------------------------------------------

MODULES = {
    1: ("module-01-fundamentals", "M1 Security Foundations & Threat Modeling"),
    2: ("module-02-web", "M2 Web Application Security"),
    3: ("module-03-malware", "M3 Malware Analysis & Social Engineering"),
    4: ("module-04-network", "M4 Network Security & Monitoring"),
    5: ("module-05-crypto", "M5 Cryptography & Applied Trust"),
    6: ("module-06-ml-security", "M6 Data Science for Security & ML Security"),
    7: ("module-07-cloud-privacy", "M7 Cloud Security & Privacy"),
    8: ("module-08-capstone", "M8 Capstone"),
}

# Condensed per-lecture outcome (syllabus §7 wording) + CLO tags (syllabus §5)
LECTURES = [
    (1, "Security Foundations: CIA, Ethics, and the Defender's Mindset", "CLO-1", ["Define CIA and classify real failures", "Apply responsible-disclosure rules"]),
    (2, "Threat Modeling I: STRIDE and Attack Trees", "CLO-1", ["Build a STRIDE model (≥ 12 entries)", "Decompose threats with attack trees"]),
    (3, "Threat Modeling II: Attack Surface and MITRE ATT&CK", "CLO-1", ["Enumerate and shrink an attack surface", "Map behaviors to ATT&CK techniques"]),
    (4, "Defense in Depth, Least Privilege, and Checkpoint A", "CLO-1", ["Layer preventive/detective/corrective controls", "Apply least privilege and secure defaults"]),
    (5, "Web Foundations: HTTP, Sessions, and Authentication", "CLO-2", ["Read HTTP requests/responses end to end", "Explain session cookies and their attributes"]),
    (6, "Injection Attacks: SQL, NoSQL, and Command Injection", "CLO-2", ["Demonstrate and remediate injection", "Apply parameterization and least-privilege DB"]),
    (7, "XSS, CSRF, SSRF, and IDOR", "CLO-2", ["Distinguish the four flaw classes by mechanism", "Apply encoding, tokens, egress, object authz"]),
    (8, "Secure SDLC, Dependency Hygiene, Security Headers + Checkpoint B", "CLO-2", ["Place SAST/DAST/SCA in the pipeline", "Configure CSP and HSTS with their limits"]),
    (9, "Malware Analysis I: Taxonomy and Static Triage", "CLO-3", ["Triage samples statically (hashes→imports)", "Justify sandbox isolation controls"]),
    (10, "Malware Analysis II: Dynamic Analysis, Sandboxes, and IOCs", "CLO-3", ["Detonate safely with fake-net isolation", "Extract IOCs and map to ATT&CK"]),
    (11, "Ransomware and Worms: Anatomy and Resilience", "CLO-3", ["Walk the ransomware lifecycle", "Design 3-2-1 backup resilience"]),
    (12, "Social Engineering, Phishing & Awareness Programs + Checkpoint C", "CLO-3", ["Dissect phishing/BEC anatomy", "Design awareness programs with report-rate metrics"]),
    (13, "Network Defense I: Packet Analysis with Wireshark", "CLO-4", ["Read TCP conversations and TLS metadata", "Spot scan/beacon/exfil patterns"]),
    (14, "Network Defense II: Firewalls, Segmentation, Zero Trust", "CLO-4", ["Design default-deny zones", "Write minimal, ordered rulesets"]),
    (15, "IDS/IPS and SIEM: Detection and Alert Triage", "CLO-4", ["Contrast signature vs anomaly IDS", "Triage a SIEM queue with metrics"]),
    (16, "Wireless, VPN & Midterm Consolidation", "CLO-4", ["Assess WPA3 and VPN posture honestly", "Consolidate Modules 1–4 in the midterm"]),
    (17, "Symmetric Cryptography and Block Cipher Modes", "CLO-5", ["Choose modes by property", "Demonstrate ECB failure; justify AEAD"]),
    (18, "Asymmetric Cryptography, PKI, and TLS", "CLO-5", ["Walk the TLS 1.3 handshake", "Explain certificates and trust chains"]),
    (19, "Hashing, Password Storage, and Key Management", "CLO-5", ["Select Argon2id/bcrypt with tuned work factors", "Explain salt and cracking economics"]),
    (20, "Cryptographic Failures in the Wild + Checkpoint D", "CLO-5", ["Autopsy misuse patterns (ECB, IV reuse, key co-location)", "Specify a key-management lifecycle"]),
    (21, "Security Analytics I: Anomaly Detection in Logs", "CLO-6", ["Engineer features from auth logs", "Tune isolation forests by SOC capacity"]),
    (22, "Security Analytics II: Classification Pipelines", "CLO-6", ["Build phishing classifiers that survive rewording", "Manage feature drift and label quality"]),
    (23, "Adversarial Machine Learning: Evasion, Poisoning, Extraction", "CLO-6", ["Execute sandbox adversarial demos", "Apply mitigations with named costs"]),
    (24, "Detection Engineering: Metrics, Rules, and the SOC Pipeline + Checkpoint E", "CLO-6", ["Take a rule through shadow→alert→block", "Write coverage statements with measured FPR/TPR"]),
    (25, "Cloud Security I: Shared Responsibility and IAM", "CLO-7", ["Allocate responsibility across service models", "Design least-privilege IAM with roles"]),
    (26, "Cloud Security II: Containers, Serverless, and Secrets", "CLO-7", ["Harden images and runtime surfaces", "Manage secrets without env-as-vault"]),
    (27, "Cloud Security III: Audit Trails, Detection, and Misconfiguration Management", "CLO-7", ["Distinguish control- vs data-plane telemetry", "Run policy-as-code and drift detection"]),
    (28, "Privacy Engineering: Data Protection, GDPR-style Compliance, DPIA + Checkpoint F", "CLO-7", ["Apply minimization and data-subject rights", "Draft a DPIA skeleton"]),
    (29, "Capstone Kickoff: Scenario, Threat Model, Control Backlog", "CLO-8", ["Scope one system with explicit boundaries", "Produce a team threat model and backlog"]),
    (30, "Capstone Build Sprint I: Hardening and Detection", "CLO-8", ["Implement priority controls with fix-verify", "Build one detection with measured metrics"]),
    (31, "Capstone Build Sprint II: Incident-Response Tabletop", "CLO-8", ["Run a tabletop against your own design", "Update runbooks from findings"]),
    (32, "Capstone Showcase and Final Examination", "CLO-8", ["Defend the capstone chain under questioning", "Complete the final examination"]),
]

# Lab crosswalk (labs/README.md is authoritative) — session → labs introduced.
# Graded labs carry their due week (next-session rule, staggered — see README).
LABS = {
    1:  [("Lab 00", "Security Baseline & System Hardening", "Core graded", "Lab 00 due W2")],
    2:  [("Lab 01", "Threat Modeling: STRIDE & Attack Trees", "Enrichment", None)],
    3:  [("Lab 02", "Attack Surface & ATT&CK Mapping", "Enrichment", None)],
    4:  [("Lab 03", "Defense-in-Depth Control Plan", "Enrichment", None)],
    5:  [("Lab 04", "Web Auth Flow Review", "Enrichment", None)],
    6:  [("Lab 05", "Injection: Confirm, Fix, Verify", "Enrichment", None)],
    7:  [("Lab 06", "Web Flaw Stations", "Enrichment", None)],
    8:  [("Lab 07", "Security Headers & Dependency Hygiene", "Enrichment", None)],
    9:  [("Lab 08", "Malware Static Triage", "Enrichment", None)],
    10: [("Lab 09", "Dynamic Analysis & IOCs", "Enrichment", None),
         ("Lab 27", "Digital Forensics (instructor artifacts)", "Core graded", "Lab 27 due W9")],
    11: [("Lab 10", "Ransomware Resilience Scenario", "Enrichment", None)],
    12: [("Lab 11", "Awareness Campaign Design", "Enrichment", None)],
    13: [("Lab 12", "Network Traffic Analysis (prepared captures)", "Core graded", "Lab 12 due W8")],
    14: [("Lab 13", "Segmentation & Ruleset Design", "Enrichment", None)],
    15: [("Lab 14", "Alert Triage & Correlation", "Enrichment", None),
         ("Lab 29", "Authorized-Target Vulnerability Assessment", "Core graded", "Lab 29 due W11")],
    16: [],
    17: [("Lab 15", "Cryptographic Operations & Integrity Checks", "Core graded", "Lab 15 due W10")],
    18: [("Lab 16", "Certificates, PKI & TLS Inspection", "Enrichment", None)],
    19: [("Lab 17", "Password Storage & Secrets Hygiene", "Enrichment", None)],
    20: [("Lab 18", "Crypto Failure Review", "Enrichment", None)],
    21: [("Lab 19", "Log Analysis & Anomaly Detection", "Core graded", "Lab 19 due W12")],
    22: [("Lab 20", "Phishing Classification Pipeline", "Enrichment", None)],
    23: [("Lab 21", "Adversarial ML Stations", "Enrichment", None)],
    24: [("Lab 22", "Detection Engineering Pipeline", "Enrichment", None)],
    25: [("Lab 23", "Cloud IAM Least-Privilege Audit", "Core graded", "Lab 23 due W14")],
    26: [("Lab 24", "Container & Workload Hardening", "Enrichment", None)],
    27: [("Lab 25", "Cloud Audit-Trail Investigation", "Enrichment", None)],
    28: [("Lab 26", "Privacy Engineering & DPIA", "Enrichment", None)],
    29: [("Lab 30", "Capstone Working Labs (1/3)", "Enrichment", None)],
    30: [("Lab 30", "Capstone Working Labs (2/3)", "Enrichment", None)],
    31: [("Lab 28", "Incident Response Simulation", "Core graded", "Lab 28 due W16"),
         ("Lab 30", "Capstone Working Labs (3/3)", "Enrichment", None)],
    32: [],
}

LAB_DIRS = {
    "Lab 00": "lab-00-hardening-baseline", "Lab 01": "lab-01-threat-modeling",
    "Lab 02": "lab-02-attack-surface", "Lab 03": "lab-03-controls-layering",
    "Lab 04": "lab-04-web-foundations", "Lab 05": "lab-05-injection",
    "Lab 06": "lab-06-xss-csrf-ssrf-idor", "Lab 07": "lab-07-headers-sdlc",
    "Lab 08": "lab-08-static-triage", "Lab 09": "lab-09-dynamic-analysis",
    "Lab 10": "lab-10-ransomware-resilience", "Lab 11": "lab-11-awareness-design",
    "Lab 12": "lab-12-packet-analysis", "Lab 13": "lab-13-segmentation",
    "Lab 14": "lab-14-siem-triage", "Lab 15": "lab-15-crypto-integrity",
    "Lab 16": "lab-16-pki-tls", "Lab 17": "lab-17-password-storage",
    "Lab 18": "lab-18-crypto-failures", "Lab 19": "lab-19-log-anomaly",
    "Lab 20": "lab-20-phishing-classifier", "Lab 21": "lab-21-adversarial-ml",
    "Lab 22": "lab-22-detection-engineering", "Lab 23": "lab-23-cloud-iam",
    "Lab 24": "lab-24-containers", "Lab 25": "lab-25-cloud-audit",
    "Lab 26": "lab-26-dpia", "Lab 27": "lab-27-forensics",
    "Lab 28": "lab-28-ir-simulation", "Lab 29": "lab-29-vuln-assessment",
    "Lab 30": "lab-30-capstone",
}

# Assessment units (16 weekly units) — checkpoints = graded quizzes per README map
ASSESSMENTS = {
    1:  [("Quiz Q1 (specimen)", "ungraded", "quizzes/quiz-01.md")],
    2:  [("Checkpoint A (graded, /10)", "graded", "quizzes/quiz-02.md"), ("Lab 00 report due", "graded", None)],
    3:  [("Quiz Q3 (specimen)", "ungraded", "quizzes/quiz-03.md")],
    4:  [("Checkpoint B (graded, /10)", "graded", "quizzes/quiz-04.md")],
    5:  [("Quiz Q5 (specimen)", "ungraded", "quizzes/quiz-05.md")],
    6:  [("Checkpoint C (graded, /10)", "graded", "quizzes/quiz-06.md")],
    7:  [("Quiz Q7 (specimen)", "ungraded", "quizzes/quiz-07.md")],
    8:  [("Midterm examination (15%)", "graded", None), ("Quiz Q8 pre-midterm (specimen)", "ungraded", "quizzes/quiz-08.md"),
         ("Lab 12 report due", "graded", None)],
    9:  [("Quiz Q9 (specimen)", "ungraded", "quizzes/quiz-09.md"), ("Lab 27 report due", "graded", None)],
    10: [("Checkpoint D (graded, /10)", "graded", "quizzes/quiz-10.md"), ("Lab 15 report due", "graded", None)],
    11: [("Quiz Q11 (specimen)", "ungraded", "quizzes/quiz-11.md"), ("Lab 29 report due", "graded", None),
         ("Register case-brief case", "process", "case-study-activity.md")],
    12: [("Checkpoint E (graded, /10)", "graded", "quizzes/quiz-12.md"), ("Case-study brief due (10%)", "graded", "case-study-activity.md"),
         ("Lab 19 report due", "graded", None)],
    13: [("Quiz Q13 (specimen)", "ungraded", "quizzes/quiz-13.md")],
    14: [("Checkpoint F (graded, /10)", "graded", "quizzes/quiz-14.md"), ("Lab 23 report due", "graded", None)],
    15: [("Quiz Q15 pre-final (specimen)", "ungraded", "quizzes/quiz-15.md"), ("Capstone milestone 1 (threat model)", "graded", "capstone-brief.md")],
    16: [("Capstone report + showcase defense (20%)", "graded", "capstone-brief.md"),
         ("Final examination (10%)", "graded", "specimen-final.md"), ("Lab 28 report due", "graded", None)],
}

# Case session per lecture (mirrors instructor deck case-session slides; L16/L32 none)
CASES = {
    1: ("CS-001", 1), 2: ("CS-005", 1), 3: ("CS-020", 1), 4: ("CS-006", 1),
    5: ("CS-034", 2), 6: ("CS-033", 2), 7: ("CS-050", 2), 8: ("CS-049", 3),
    9: ("CS-042", 2), 10: ("CS-016", 1), 11: ("CS-032", 2), 12: ("CS-023", 2),
    13: ("CS-056", 3), 14: ("CS-025", 2), 15: ("CS-039", 2), 16: None,
    17: ("CS-047", 3), 18: ("CS-046", 3), 19: ("CS-021", 2), 20: ("CS-011", 1),
    21: ("CS-055", 3), 22: ("CS-068", 3), 23: ("CS-067", 3), 24: ("CS-085", 4),
    25: ("CS-062", 3), 26: ("CS-064", 3), 27: ("CS-063", 3), 28: ("CS-094", 4),
    29: ("CS-100", 4), 30: ("CS-083", 4), 31: ("CS-058", 3), 32: None,
}
CASE_LEVEL_FILES = {1: "level-1-beginner.md", 2: "level-2-intermediate.md",
                    3: "level-3-advanced.md", 4: "level-4-expert.md"}

GRADED_LABS = {"Lab 00", "Lab 12", "Lab 15", "Lab 19", "Lab 23", "Lab 27", "Lab 28", "Lab 29"}

# --------------------------------------------------------------------------
# Date engine
# --------------------------------------------------------------------------

def session_dates(start: dt.date) -> list[dt.date]:
    """Session 1 = first Monday; session 2 = Thursday of the same week (x16)."""
    if start.weekday() != 0:
        raise SystemExit("--start must be a Monday (configurable cadence is Mon/Thu)")
    out = []
    for w in range(16):
        monday = start + dt.timedelta(weeks=w)
        out += [monday, monday + dt.timedelta(days=3)]
    return out

# --------------------------------------------------------------------------
# Live-repository verification (titles must match the actual notes)
# --------------------------------------------------------------------------

def verify_titles_from_repo() -> list[str]:
    problems = []
    for n, title, _, _ in LECTURES:
        mdir = MODULES[(n - 1) // 4 + 1][0]
        p = ROOT / "lectures" / mdir / f"lecture-{n:02d}.md"
        text = p.read_text(encoding="utf-8") if p.exists() else ""
        m = re.search(r"^# Lecture (\d+) — (.+)$", text, re.M)
        if not p.exists():
            problems.append(f"lecture-{n:02d}: note file missing ({p.relative_to(ROOT)})")
        elif not m or m.group(1) != f"{n:02d}":
            problems.append(f"lecture-{n:02d}: note H1 does not match lecture number")
        elif m.group(2).strip() != title:
            problems.append(f"lecture-{n:02d}: calendar title drift\n    repo: {m.group(2).strip()}\n    cal:  {title}")
    return problems

# --------------------------------------------------------------------------
# Writers
# --------------------------------------------------------------------------

def lab_link_md(name: str) -> str:
    return f"[{name}]({PREFIX}/labs/{LAB_DIRS[name]}/README.md)"

def case_link_md(cid: str, level: int) -> str:
    return f"[{cid}]({PREFIX}/case-studies/collection/{CASE_LEVEL_FILES[level]})"

def quiz_link_md(rel: str | None) -> str:
    return f"[details]({PREFIX}/assessments/student/{rel})" if rel else ""

def week_rows(week: int):
    s1, s2 = 2 * week - 1, 2 * week
    return s1, s2

def student_markdown(start: dt.date) -> str:
    dates = session_dates(start)
    lines = [
        "# Semester Calendar — Cyber Security (student view)",
        f"**BS CS / BS Data Science · 7th semester · 16 weeks · 32 lectures × 2 h (64 contact hours)**",
        f"**Semester start (configurable): {start.isoformat()}** — sessions are Mondays & Thursdays; "
        "regenerate with `python calendar/tools/generate_calendar.py --start YYYY-MM-DD`.",
        "",
        "Legend: 🔬 lab · 📝 assessment · 💬 case discussion · 🔗 links go to the live course files.",
        "",
        "| Week | Session 1 (Mon) | Session 2 (Thu) |",
        "|---|---|---|",
    ]
    for w in range(1, 17):
        s1, s2 = week_rows(w)
        lines.append(f"| **W{w}** | **{dates[2*(w-1)].isoformat()}** · L{s1:02d} | **{dates[2*(w-1)+1].isoformat()}** · L{s2:02d} |")
    lines.append("")
    for w in range(1, 17):
        s1, s2 = week_rows(w)
        d1, d2 = dates[2 * (w - 1)], dates[2 * (w - 1) + 1]
        lines.append(f"## Week {w} · {d1.isoformat()} – {d2.isoformat()}")
        wk_items = ASSESSMENTS.get(w, [])
        if wk_items:
            lines.append("**Due / happen this week:**")
            for label, kind, rel in wk_items:
                link = f" — {quiz_link_md(rel)}" if rel and kind != "process" else (f" — [task]({PREFIX}/assessments/student/{rel})" if rel else "")
                icon = "📝" if kind != "process" else "🗓"
                lines.append(f"- {icon} **{label}**{link}")
        for sess, d in ((s1, d1), (s2, d2)):
            n, title, clo, outcomes = next(l for l in LECTURES if l[0] == sess)
            mdir, mlabel = MODULES[(n - 1) // 4 + 1]
            lines.append(f"### Lecture {n:02d} — {title}")
            lines.append(f"*{d.strftime('%a %d %b %Y')} · {mlabel} · {clo}*")
            for o in outcomes:
                lines.append(f"- {o}")
            labs = LABS.get(sess, [])
            if labs:
                parts = []
                for name, ltitle, ltype, due in labs:
                    graded = " **(graded)**" if ltype.startswith("Core") else ""
                    parts.append(f"🔬 {lab_link_md(name)} — {ltitle}{graded}" + (f" · *{due}*" if due else ""))
                lines += ["- " + p for p in parts]
            case = CASES.get(sess)
            if case:
                cid, lvl = case
                lines.append(f"- 💬 Case discussion: {case_link_md(cid, lvl)}")
            lines.append(f"- 🔗 [Lecture notes]({PREFIX}/lectures/{mdir}/lecture-{n:02d}.md)")
            lines.append("")
    lines.append("---")
    lines.append("*Generated from the repository's actual content — do not hand-edit; regenerate instead "
                 "(`calendar/tools/generate_calendar.py`). Answer keys are never linked here.*")
    return "\n".join(lines) + "\n"

def _esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def student_html(start: dt.date) -> str:
    dates = session_dates(start)
    css = """
    body{font-family:'Segoe UI',Arial,sans-serif;margin:24px auto;max-width:860px;color:#111;background:#fff}
    h1{color:#0b3d66} h2{color:#0b3d66;border-bottom:2px solid #0b3d66;padding-bottom:4px;margin-top:28px}
    .card{border:1px solid #c9d3dc;border-radius:8px;padding:12px 16px;margin:10px 0;page-break-inside:avoid}
    .date{display:inline-block;background:#0b3d66;color:#fff;border-radius:4px;padding:2px 8px;font-size:.85em}
    .mod{color:#555;font-size:.9em} ul{margin:6px 0}
    .assess{background:#fff6e5;border-left:5px solid #b26a00;padding:4px 10px;border-radius:4px;display:inline-block}
    .graded{background:#e8f2ff;border-left:5px solid #0b3d66;padding:4px 10px;border-radius:4px;display:inline-block}
    a{color:#0b3d66} .legend{font-size:.9em;color:#444}
    @media print{body{margin:0;font-size:11pt} .card{break-inside:avoid} h2{break-after:avoid} a{color:#111;text-decoration:none}
      .noprint{display:none}}
    """
    out = [
        "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>",
        "<title>Cyber Security — Semester Calendar</title>",
        f"<style>{css}</style></head><body>",
        "<h1>Cyber Security — Semester Calendar</h1>",
        f"<p><strong>BS CS / BS Data Science · 7th semester · 16 weeks · 32 lectures × 2 h (64 contact hours)</strong><br>",
        f"Semester start: <strong>{start.isoformat()}</strong> · sessions Mondays &amp; Thursdays "
        f"<span class='noprint'>· regenerate: <code>python calendar/tools/generate_calendar.py --start YYYY-MM-DD</code></span></p>",
        "<p class='legend'>🔬 lab · 📝 assessment · 💬 case discussion · <span class='graded'>blue chip = graded</span></p>",
    ]
    for w in range(1, 17):
        s1, s2 = week_rows(w)
        d1, d2 = dates[2 * (w - 1)], dates[2 * (w - 1) + 1]
        out.append(f"<h2>Week {w} <small>({d1.strftime('%d %b')} – {d2.strftime('%d %b %Y')})</small></h2>")
        wk_items = ASSESSMENTS.get(w, [])
        if wk_items:
            out.append("<p>" + " ".join(
                (f"<span class='assess'>📝 <strong>{_esc(lbl)}</strong>"
                 + (f" · <a href='{PREFIX}/assessments/student/{rel}'>details</a>" if rel else "") + "</span>")
                if kind == "graded" else
                (f"🗓 {_esc(lbl)}" + (f" · <a href='{PREFIX}/assessments/student/{rel}'>task</a>" if rel else ""))
                if kind == "process" else
                (f"📝 {_esc(lbl)}" + (f" · <a href='{PREFIX}/assessments/student/{rel}'>paper</a>" if rel else ""))
                for lbl, kind, rel in wk_items) + "</p>")
        for sess, d in ((s1, d1), (s2, d2)):
            n, title, clo, outcomes = next(l for l in LECTURES if l[0] == sess)
            mdir, mlabel = MODULES[(n - 1) // 4 + 1]
            out.append("<div class='card'>")
            out.append(f"<p><span class='date'>{d.strftime('%a %d %b')}</span> "
                       f"<strong>Lecture {n:02d} — {_esc(title)}</strong><br><span class='mod'>{_esc(mlabel)} · {clo}</span></p>")
            out.append("<ul>" + "".join(f"<li>{_esc(o)}</li>" for o in outcomes) + "</ul>")
            labs = LABS.get(sess, [])
            if labs:
                out.append("<ul>" + "".join(
                    f"<li>🔬 <a href='{PREFIX}/labs/{LAB_DIRS[nm]}/README.md'>{nm} — {_esc(lt)}</a>"
                    + (" <span class='graded'>graded</span>" if ltype.startswith("Core") else "")
                    + (f" · <em>{_esc(due)}</em>" if due else "") + "</li>"
                    for nm, lt, ltype, due in labs) + "</ul>")
            case = CASES.get(sess)
            if case:
                cid, lvl = case
                out.append(f"<p>💬 Case: <a href='{PREFIX}/case-studies/collection/{CASE_LEVEL_FILES[lvl]}'>{cid}</a></p>")
            out.append(f"<p class='noprint'><a href='{PREFIX}/lectures/{mdir}/lecture-{n:02d}.md'>Open lecture notes →</a></p>")
            out.append("</div>")
    out.append("<p class='legend'>Generated from the repository's actual content — regenerate, don't hand-edit. "
               "Answer keys are never included.</p></body></html>")
    return "\n".join(out)

def instructor_markdown(start: dt.date) -> str:
    dates = session_dates(start)
    lines = [
        "# ⚠️ INSTRUCTOR-ONLY — Semester Planning Calendar",
        f"**Start: {start.isoformat()} (Mon/Thu × 16 weeks) · regenerate: `python calendar/tools/generate_calendar.py --start YYYY-MM-DD`**",
        "",
        "Per-session prep pointers: deck (slides/), teaching guide, checkpoint/exam keys (assessments/instructor-only).",
        "",
        "| Wk | Date | Lec | Title (CLOs) | Objectives | Labs (type · due) | Assessment (week) | Case | Prep |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for w in range(1, 17):
        for k, sess in enumerate(week_rows(w)):
            d = dates[2 * (w - 1) + k]
            n, title, clo, outcomes = next(l for l in LECTURES if l[0] == sess)
            mdir, _ = MODULES[(n - 1) // 4 + 1]
            labs = " · ".join(f"{nm} ({lt} — {ltype}{'; ' + due if due else ''})" for nm, lt, ltype, due in LABS.get(sess, [])) or "—"
            assess = " · ".join(lbl for lbl, _, _ in ASSESSMENTS.get(w, [])) or "—"
            case = CASES.get(sess)
            case_s = f"{case[0]} (L{case[1]})" if case else "—"
            objectives = "; ".join(outcomes)
            prep = (f"[deck]({PREFIX}/instructor-materials/instructor-only/slides/lecture-{n:02d}.md) · "
                    f"[guide]({PREFIX}/instructor-materials/instructor-only/teaching-guides/lecture-{n:02d}.md) · "
                    f"[plan]({PREFIX}/instructor-materials/instructor-only/lecture-plans/lecture-{n:02d}.md)")
            lines.append(f"| {w} | {d.isoformat()} | L{n:02d} | {title} ({clo}) | {objectives} | {labs} | {assess} | {case_s} | {prep} |")
    lines += [
        "",
        "## Logistics per assessment window",
        "- Checkpoints A–F (W2/4/6/10/12/14): print `quizzes/quiz-NN.md` (student) + carry `checkpoint-keys.md`; 12 min, closed book, record /10.",
        "- Midterm W8 & Final W16: papers + marking schemes in `assessments/instructor-only/`; follow logistics sections; Variant B swaps per bank tables.",
        "- Graded-lab due weeks: W2 Lab 00 · W8 Lab 12 · W9 Lab 27 · W10 Lab 15 · W11 Lab 29 · W12 Lab 19 · W14 Lab 23 · W16 Lab 28 (best 6 of 8 count).",
        "- Case briefs: registration W11, submission W12 (10%); rubric in `case-studies/rubrics.md`.",
        "- Capstone: milestone 1 W15 · showcase + defense W16 (moderation: `assessments/instructor-only/capstone-rubric.md`).",
    ]
    return "\n".join(lines) + "\n"

# --------------------------------------------------------------------------
# Validation
# --------------------------------------------------------------------------

def validate(outdir: Path, start: dt.date) -> list[str]:
    problems = []
    dates = session_dates(start)

    # 1-3. structure
    if len(LECTURES) != 32:
        problems.append(f"lecture count {len(LECTURES)} != 32")
    if len(dates) != 32:
        problems.append(f"session dates {len(dates)} != 32")
    nums = [l[0] for l in LECTURES]
    if nums != list(range(1, 33)):
        problems.append("lecture numbering has gaps/duplicates")
    weeks = sorted({(n + 1) // 2 for n, _, _, _ in LECTURES})
    if weeks != list(range(1, 17)):
        problems.append("week mapping is not exactly 1..16")

    # 4. lab & assessment alignment
    graded = [nm for sess in LABS for nm, _, lt, _ in LABS[sess] if lt.startswith("Core")]
    if sorted(graded) != sorted(GRADED_LABS):
        problems.append(f"graded-lab set mismatch: calendar {sorted(graded)}")
    for w, items in ASSESSMENTS.items():
        for label, kind, rel in items:
            if rel and not (ROOT / "assessments/student" / rel).exists():
                problems.append(f"W{w}: assessment link target missing: {rel}")
    cp_weeks = {2: "A", 4: "B", 6: "C", 10: "D", 12: "E", 14: "F"}
    for w, letter in cp_weeks.items():
        labels = [lbl for lbl, _, _ in ASSESSMENTS.get(w, [])]
        if not any(f"Checkpoint {letter}" in l for l in labels):
            problems.append(f"W{w}: expected Checkpoint {letter}")

    # 5. link resolution in generated artifacts
    for fname in ("student-calendar.md", "instructor-calendar.md", "student-calendar.html"):
        text = (outdir / fname).read_text(encoding="utf-8")
        links = re.findall(r"\]\(([^)#\s]+)\)", text)
        for link in links:
            if link.startswith(("http://", "https://")):
                continue
            if not (outdir / link).resolve().exists():
                problems.append(f"{fname}: broken link {link}")

    # 6. dates are Mondays/Thursdays
    for d in dates:
        if d.weekday() not in (0, 3):
            problems.append(f"session date {d} is not Mon/Thu")
    return problems

# --------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(description="Generate the semester calendar (student + instructor views).")
    ap.add_argument("--start", default="2026-09-07", help="semester start, a Monday (default 2026-09-07)")
    ap.add_argument("--outdir", default=str(ROOT / "calendar/generated"))
    ap.add_argument("--validate-only", action="store_true", help="validate existing output without regenerating")
    args = ap.parse_args()

    start = dt.date.fromisoformat(args.start)
    dates = session_dates(start)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    global PREFIX
    PREFIX = os.path.relpath(ROOT, outdir).replace("\\", "/")

    problems = verify_titles_from_repo()
    if problems:
        print("Repository/title verification FAILED:")
        for p in problems:
            print("  -", p)
        sys.exit(1)

    if not args.validate_only:
        (outdir / "student-calendar.md").write_text(student_markdown(start), encoding="utf-8")
        (outdir / "student-calendar.html").write_text(student_html(start), encoding="utf-8")
        # Instructor planning view routes to the instructor-only tier (finding M2):
        instr_dir = ROOT / "instructor-materials" / "instructor-only" / "calendar"
        instr_dir.mkdir(parents=True, exist_ok=True)
        (instr_dir / "instructor-calendar.md").write_text(instructor_markdown(start), encoding="utf-8")
        (outdir / "instructor-calendar.md").write_text(
            "# ⚠️ INSTRUCTOR-ONLY — moved\n\n"
            "The instructor planning calendar is generated directly to "
            "`instructor-materials/instructor-only/calendar/instructor-calendar.md` so it never sits in a "
            "publishable directory. Regenerate with `python calendar/tools/generate_calendar.py --start YYYY-MM-DD`.\n",
            encoding="utf-8")
        payload = {
            "course": "Cyber Security — BS CS/DS, 7th semester",
            "semester_start": start.isoformat(),
            "cadence": "Mon/Thu",
            "weeks": 16,
            "sessions": [
                {
                    "week": (n + 1) // 2, "lecture": n, "date": dates[n - 1].isoformat(),
                    "title": title, "clos": clo, "outcomes": outcomes,
                    "module": MODULES[(n - 1) // 4 + 1][1],
                    "labs": [{"name": nm, "title": lt, "type": ltype, "due": due} for nm, lt, ltype, due in LABS.get(n, [])],
                    "assessments_week": [{"label": lbl, "kind": kind, "ref": rel} for lbl, kind, rel in ASSESSMENTS.get((n + 1) // 2, [])],
                    "case": CASES.get(n),
                } for n, title, clo, outcomes in LECTURES
            ],
        }
        (outdir / "calendar-semester.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")

    problems = validate(outdir, start)
    if problems:
        print(f"VALIDATION FAILED ({len(problems)}):")
        for p in problems:
            print("  -", p)
        sys.exit(1)

    print("Calendar generated & validated:")
    for f in sorted(outdir.iterdir()):
        print("  -", f.name)
    print("16 weeks · 32 lectures · Mon/Thu cadence · lab+assessment alignment OK · links resolve")


if __name__ == "__main__":
    main()
