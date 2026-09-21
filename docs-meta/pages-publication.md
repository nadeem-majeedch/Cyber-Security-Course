# GitHub Pages — Publication Instructions

**Honest status: NOT PUBLISHED.** The workflow and publish tree are built; deployment has never been executed (requires repository-owner access to GitHub). Follow these steps and verify each one.

## Prerequisites

- Repository pushed to GitHub with `main` as the default branch.
- Repo visibility is **public** (Pages on private repos requires a paid plan) — which makes the instructor-only migration (finding C1) a hard precondition: instructor material must already be out of this repository before publishing.
- The publish tree (`website/`) contains no instructor-only content — the workflow's guard step enforces this at build time.

## Steps

1. **Enable Pages:** repository *Settings → Pages → Build and deployment → Source: **GitHub Actions*** (not "deploy from branch" — the workflow handles the build).
2. **Trigger the workflow:** push to `main` touching `website/`, `lectures/`, or `calendar/` — or run it manually: *Actions → "Deploy course website to GitHub Pages" → Run workflow*.
3. **Watch the build:** the workflow (a) fails if instructor-only files appear under `website/`, (b) copies `calendar/generated/student-calendar.md` into the site as `calendar-dated.md` (warning, not failure, if the calendar has not been generated yet), (c) builds with Jekyll, (d) uploads and deploys the artifact.
4. **Verify — both checks, not just the first:**
   - The Actions run is **green**.
   - The published URL (shown in the deploy step's output and in *Settings → Pages*) actually loads and shows the `index.md` content — click one lecture link and the schedule link to confirm relative paths resolve at the site root.
5. **Content freshness:** the mirrored notes in `website/lectures/` are copies. After editing any student note, re-mirror:
   ```bash
   for d in lectures/module-*/; do mkdir -p "website/lectures/$(basename "$d")" && cp "$d"lecture-*.md "website/lectures/$(basename "$d")/"; done
   ```
   Then commit and push (the workflow redeploys automatically).

## What the site deliberately omits

- Instructor-only tiers (plans, guides, decks, keys, exam papers, solutions, planning calendar) — never mirrored, never linked, build fails if present.
- Lab answer keys and assessment keys — student quiz papers and specimen exams are repository-only, not mirrored into the site.
- The dated calendar enters the site only through the build-time copy of the *student* view; the instructor view lives outside `website/` entirely.

## Rollback

Redeploy a previous commit: *Actions → select the last known-good run → Re-run all jobs* after reverting the content commit, or temporarily disable Pages (*Settings → Pages → Source: None*).
