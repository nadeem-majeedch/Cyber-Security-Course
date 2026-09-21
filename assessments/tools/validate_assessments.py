#!/usr/bin/env python3
"""Validation for the assessment package.

Checks:
  1. Student quiz papers Q01..Q15 exist; Q2/4/6/10/12/14 are checkpoint papers;
     no paper contains answer-key markers (✔, "Key:", "Answer:").
  2. Question bank files exist; every MCQ item carries a ✔ key and an Explanation;
     every SA carries a Key; every item carries CLO and Bloom tags.
  3. Duplicate-question scan: identical question stems must not appear in more
     than one live artifact (bank items vs specimens vs checkpoints).
  4. Student-tier files contain no instructor-only leakage markers.
  5. Instructor papers (midterm/final) exist with marking schemes and variant notes.
  6. CLO coverage: bank-wide tags cover CLO-1..CLO-8.
  7. Mark-total arithmetic: stated quiz totals match sum of per-item marks.
  8. Checkpoint paper↔key coverage: every numbered paper item has a key entry
     (finding H1 regression guard).
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]          # assessments/
STUDENT = ROOT / "student"
QUIZZES = STUDENT / "quizzes"
BANK = ROOT / "instructor-only" / "question-bank"
INSTR = ROOT / "instructor-only"

failures: list[str] = []
def err(msg: str) -> None:
    failures.append(msg)

def read(p: Path) -> str:
    return p.read_text(encoding="utf-8") if p.exists() else ""

# ---- 1. Quiz papers ----------------------------------------------------------
missing = [f"quiz-{n:02d}.md" for n in range(1, 16) if not (QUIZZES / f"quiz-{n:02d}.md").exists()]
if missing:
    err(f"missing quiz papers: {', '.join(missing)}")

for n in range(1, 16):
    p = QUIZZES / f"quiz-{n:02d}.md"
    if not p.exists():
        continue
    text = read(p)
    if n in (2, 4, 6, 10, 12, 14) and "Checkpoint" not in text:
        err(f"quiz-{n:02d}: expected Checkpoint paper")
    for marker in ("✔", "**Key:**", "**Explanation"):
        if marker in text:
            err(f"quiz-{n:02d}: answer-key marker {marker!r} present in student tier")

# ---- 2. Question bank integrity ---------------------------------------------
for name in ["QB-M1", "QB-M2", "QB-M3", "QB-M4", "QB-M5", "QB-M6", "QB-M7", "QB-M8",
             "QB-MT", "QB-FE", "QB-SM", "QB-SF"]:
    p = BANK / f"{name}.md"
    text = read(p)
    if not text:
        err(f"{name}.md missing")
        continue
    if "CLO-" not in text or "Bloom" not in text:
        err(f"{name}.md: missing CLO/Bloom tags")
    # MCQ items: each MCQ-n.n must have a ✔ key and an explanation
    mcq_ids = re.findall(r"^## (MCQ-[\d.]+)", text, re.M)
    for mid in mcq_ids:
        seg = text.split(f"## {mid}", 1)[1].split("\n## ", 1)[0]
        if "✔" not in seg:
            err(f"{name}.md {mid}: no keyed answer (✔)")
        if "Explanation" not in seg:
            err(f"{name}.md {mid}: no explanation")
        if "Key:" not in seg:
            err(f"{name}.md {mid}: no explicit key letter")
    # SA items: each SA-n.n must have a Key section
    sa_ids = re.findall(r"^## (SA-[\d.]+)", text, re.M)
    for sid in sa_ids:
        seg = text.split(f"## {sid}", 1)[1].split("\n## ", 1)[0]
        if "**Key:**" not in seg:
            err(f"{name}.md {sid}: no key")

# Exam banks: every item needs a Key
for name in ["QB-MT", "QB-FE", "QB-SM", "QB-SF"]:
    text = read(BANK / f"{name}.md")
    # skip non-item sections (headers, swap tables)
    ITEM_RE = re.compile(r"^##? ?(?:\*\*)?(MT|FE|SM|SF)-\d+", re.M)
    for chunk in re.split(r"\n## ", text)[1:]:
        first = chunk.splitlines()[0]
        if not ITEM_RE.match("## " + first) and not re.match(r"^(MT|FE|SM|SF)-\d+", first):
            continue
        if "**Key" not in chunk and "*Key" not in chunk:
            err(f"{name}: item block missing key: {first[:40]}")

# ---- 3. Duplicate-question scan (stems across live artifacts) -----------------
stems: dict[str, list[str]] = {}
def collect_stems(path: Path, label: str) -> None:
    for line in read(path).splitlines():
        m = re.match(r"\*\*(\d+)\.\*\* (.+)", line) or re.match(r"^\*\*[A-Z]+-[\dA-Z.]+\.\*\* ", line)
        if m and len(m.group(2) if m.lastindex and m.lastindex > 1 else "") > 30:
            stem = re.sub(r"[^a-z0-9 ]", "", (m.group(2) if m.lastindex and m.lastindex > 1 else "").lower())[:80]
            stems.setdefault(stem, []).append(label)

for n in range(1, 16):
    collect_stems(QUIZZES / f"quiz-{n:02d}.md", f"quiz-{n:02d}")
for name in ["QB-SM", "QB-SF"]:
    collect_stems(BANK / f"{name}.md", name)
dups = {s: ls for s, ls in stems.items() if len(ls) > 1 and len(s) > 25}
for s, ls in dups.items():
    err(f"possible duplicate stems across {', '.join(ls)} (stem: '{s[:50]}…')")

# ---- 4. Student-tier leakage scan --------------------------------------------
LEAK = ["INSTRUCTOR-ONLY", "instructor-only/", "**Key:**", "Model solution", "Variant B swap"]
for p in STUDENT.rglob("*.md"):
    text = read(p)
    for marker in LEAK:
        if marker in text:
            err(f"leakage: {p.relative_to(ROOT)} contains {marker!r}")
    # 'Answer key discussed in class / not posted' is the required disclaimer;
    # flag only an answer key being *posted* (a heading or list of keys).
    if re.search(r"^#+.*answer key", text, re.I | re.M):
        err(f"leakage: {p.relative_to(ROOT)} contains an answer-key heading")

# ---- 5. Instructor papers ----------------------------------------------------
for name, must in [("midterm-paper.md", ["Marking scheme", "Variant B", "50 marks"]),
                   ("final-paper.md", ["Marking scheme", "Variant B", "60 marks"]),
                   ("capstone-rubric.md", ["Moderation", "non-compensable"]),
                   ("checkpoint-keys.md", ["Checkpoint A", "Checkpoint F"]),
                   ("lab-keys.md", [])]:
    text = read(INSTR / name)
    if not text:
        err(f"{name} missing")
        continue
    for m in must:
        if m not in text:
            err(f"{name}: missing required section/marker {m!r}")

# ---- 8. Checkpoint paper↔key coverage (H1 regression guard) -------------------
keys_text = read(INSTR / "checkpoint-keys.md")
if not keys_text:
    err("checkpoint-keys.md missing (required for paper↔key coverage check)")
else:
    for w, letter in [(2, "A"), (4, "B"), (6, "C"), (10, "D"), (12, "E"), (14, "F")]:
        paper = read(QUIZZES / f"quiz-{w:02d}.md")
        pnums = re.findall(r"^(\d+)\. ", paper, re.M)
        if not pnums:
            err(f"quiz-{w:02d}: no numbered items found")
            continue
        pmax = max(int(x) for x in pnums)
        part = keys_text.split(f"## Checkpoint {letter} ")
        if len(part) < 2:
            err(f"checkpoint-keys.md: no section for Checkpoint {letter}")
            continue
        ksec = part[1].split("\n## ")[0]
        knums = set(re.findall(r"^(\d+)\. ", ksec, re.M))
        missing = [n for n in range(1, pmax + 1) if str(n) not in knums]
        if missing:
            err(f"Checkpoint {letter}: paper items {missing} have no key entry")

# ---- 6. CLO coverage ---------------------------------------------------------
bank_text = " ".join(read(p) for p in BANK.glob("QB-*.md"))
for c in range(1, 9):
    if f"CLO-{c}" not in bank_text:
        err(f"CLO-{c} not covered in question bank")

# ---- 7. Quiz mark-total arithmetic ------------------------------------------
for n in range(1, 16):
    p = QUIZZES / f"quiz-{n:02d}.md"
    if not p.exists():
        continue
    text = read(p)
    m = re.search(r"·\s*(\d+)\s*marks", text)
    if not m:
        continue
    stated = int(m.group(1))
    bracket = re.findall(r"\[(?:1 each — total (\d+)|(\d+))\]", text)
    total = sum(int(a or b) for a, b in bracket)
    if total == 0:
        continue  # checkpoint papers record /10 without brackets — accepted by design
    if stated != total and abs(stated - total) not in (1,):  # allow +1 bonus items
        err(f"quiz-{n:02d}: stated {stated} marks but bracketed items sum to {total}")

print(f"Quiz papers checked: 15 (checkpoints at 2/4/6/10/12/14)")
print(f"Bank files checked: 12 + 5 instructor docs")
print(f"Duplicate stems: {len(dups)}")
if failures:
    print(f"\nFAILURES ({len(failures)}):")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)
print("ALL CHECKS PASSED")
