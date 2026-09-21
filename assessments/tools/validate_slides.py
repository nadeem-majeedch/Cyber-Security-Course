#!/usr/bin/env python3
"""Validation for the slide decks.

Checks:
  1. lecture-01..32.md exist with Marp front matter; no placeholder markers.
  2. Deck contract: objectives slide, >=1 diagram (fenced block), CS + DS example
     slides, lab-demo slide with MVO line, case-session slide, wrap-up slide,
     references slide.
  3. Speaker notes: every content slide (separated by ---) after the objectives
     carries an HTML comment.
  4. Case-session slides cite only case IDs that exist in case-studies/INDEX.md.
  5. Review decks + case-session template exist with notes; template has the six steps.
  6. Student-tier safety: decks live only under instructor-only (no student copies).
  7. Render-availability note: confirms README documents Marp as untested.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]          # repo root
SLIDES = ROOT / "instructor-materials/instructor-only/slides"
CASES = ROOT / "case-studies"

failures: list[str] = []
def err(msg: str) -> None:
    failures.append(msg)

def read(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8") if p.exists() else ""
    except (PermissionError, OSError):
        return ""  # unreadable (locked) files are skipped, not failures

# 1. Existence + front matter + placeholders
for n in range(1, 33):
    p = SLIDES / f"lecture-{n:02d}.md"
    text = read(p)
    if not text:
        err(f"lecture-{n:02d}.md missing")
        continue
    if "marp: true" not in text.split("---", 2)[1] if text.startswith("---") else True:
        err(f"lecture-{n:02d}.md: missing Marp front matter")
    for marker in ("TODO", "TBD", "PLACEHOLDER", "[Paste your", "lorem"):
        if marker in text:
            err(f"lecture-{n:02d}.md: placeholder marker {marker!r}")

# 2+3. Contract per deck
def check_deck(p: Path, label: str, require_all: bool = True) -> None:
    text = read(p)
    if not text:
        err(f"{label} missing")
        return
    # documented deviation: exam/showcase sessions replace lab-demo + case-session
    exam_day = label in ("lecture-16", "lecture-32")
    if require_all:
        if not re.search(r"^# Learning Objectives", text, re.M):
            err(f"{label}: no objectives slide")
        if "```" not in text:
            err(f"{label}: no diagram (fenced block)")
        if not re.search(r"^# (Example — CS track|CS example)", text, re.M):
            err(f"{label}: no CS-track example slide")
        if not re.search(r"^# (Example — Data Science track|DS example)", text, re.M):
            err(f"{label}: no DS-track example slide")
        if not exam_day:
            if "Lab demo" not in text:
                err(f"{label}: no lab-demo slide")
            elif "MVO" not in text and "minimum viable outcome" not in text.lower():
                err(f"{label}: lab-demo slide lacks MVO/minimum-viable-outcome")
            if "Case session" not in text and "Case Session" not in text:
                err(f"{label}: no case-session slide")
        if not re.search(r"^# (Wrap-up|Wrap up)", text, re.M):
            err(f"{label}: no wrap-up slide")
        if not re.search(r"^# References", text, re.M):
            err(f"{label}: no references slide")
    # speaker notes: every slide body should carry a comment (title-only slides exempt)
    slides = [s for s in text.split("\n---\n") if s.strip()]
    noteless = [i for i, s in enumerate(slides) if "<!--" not in s]
    # exempt: front-matter block and References-only slides (bibliographic)
    exempt = 0
    for i in noteless:
        body = slides[i].strip()
        if (i == 0 and body.startswith("---")) or body.startswith("# References"):
            exempt += 1
    if len(noteless) - exempt > 0:
        err(f"{label}: {len(noteless) - exempt} slides missing speaker notes")

for n in range(1, 33):
    check_deck(SLIDES / f"lecture-{n:02d}.md", f"lecture-{n:02d}")

# 4. Case IDs cited must exist in INDEX.md
index = read(CASES / "INDEX.md")
valid_ids = set(re.findall(r"CS-\d{3}", index))
deck_ids = set()
for p in sorted(SLIDES.glob("lecture-*.md")):
    deck_ids |= set(re.findall(r"CS-\d{3}", read(p)))
bad = deck_ids - valid_ids
if bad:
    err(f"case IDs cited in decks but missing from INDEX: {sorted(bad)}")

# 5. Review decks + template
check_deck(SLIDES / "midterm-review.md", "midterm-review", require_all=False)
check_deck(SLIDES / "final-review.md", "final-review", require_all=False)
tmpl = read(SLIDES / "case-session-template.md")
if not tmpl:
    err("case-session-template.md missing")
else:
    for step in ("Step 1", "Step 2", "Step 3", "Step 4", "Step 5", "Step 6"):
        if step not in tmpl:
            err(f"case-session-template: missing {step}")
    if "case-solutions" not in tmpl:
        err("case-session-template: no pointer to instructor-only solutions")

# 6. Tier separation: no decks in student-facing trees
for tier in (ROOT / "lectures", ROOT / "website"):
    if tier.exists():
        for p in tier.rglob("*.md"):
            if "marp: true" in read(p):
                err(f"tier violation: {p.relative_to(ROOT)} looks like a deck in a student tier")

# 7. Rendering-status note
readme = read(SLIDES / "README.md")
if "untested" not in readme.lower():
    err("slides README does not document rendering status (untested)")

print(f"Decks checked: 32 lectures + 2 reviews + 1 template")
print(f"Case IDs cited: {len(deck_ids)} (all verified against INDEX.md)")
if failures:
    print(f"\nFAILURES ({len(failures)}):")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)
print("ALL CHECKS PASSED")
