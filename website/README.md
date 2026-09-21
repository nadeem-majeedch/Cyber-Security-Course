# Website (GitHub Pages source)

Static course hub — the publish-ready student-facing site. **Status: built; deployment not yet executed (see `../docs-meta/handover-guide.md` for the verified steps).**

## Layout

- `index.md` — course home: all 8 modules, all 32 lecture links, practice-material pointers
- `calendar.md` — fixed weekly structure (16 weeks); the **dated** calendar is copied in at build time from `calendar/generated/student-calendar.md` → published as `calendar-dated.md`
- `lectures/module-0X-*/lecture-NN.md` — mirror of the 32 student-facing notes (synced from `../lectures/`; re-copy after editing notes)
- No instructor-only content is linked, mirrored, or published — the deploy workflow **fails the build** if such files appear here

## Publication (manual — not yet run)

1. Push `main` to GitHub with this tree and `.github/workflows/pages.yml`.
2. Repo **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. The workflow builds with Jekyll and deploys via `actions/deploy-pages` on pushes touching `website/`, `lectures/`, or `calendar/` (also manually via *Run workflow*).
4. Verify: the Actions run goes green **and** the published URL loads `index.md` content — a green run alone is not verification.

Because the repository is public, this tree must stay student-only. The instructor tier (`instructor-materials/instructor-only/`, `assessments/instructor-only/`) is never mirrored here and should move to a private location before term (open decision in `docs-meta/architecture-and-requirements.md` §11).
