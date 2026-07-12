# Guided Exercise — Lesson 11: Secret Management, Repository Hygiene & Maintenance

## Steps

1. Audit whether any secret was ever committed:
   ```bash
   cd ~/Projects/Learn-DE
   git log --all --full-history -- .env
   find . -iname "*.pem" -o -iname "id_rsa*" -o -iname "id_ed25519*" 2>/dev/null | grep -v "^\./\.git"
   ```
2. Confirm `.gitignore` actually covers secrets:
   ```bash
   cat .gitignore | grep -A3 Secrets
   ```
3. Write (or review, if one already exists somewhere in this repo for a
   later phase) a real `.env.example` pattern for a hypothetical future
   need — e.g., for Checkpoint 4's eventual API credentials:
   ```bash
   mkdir -p sandbox/02_git_github/workspace/env_pattern_demo
   cat > sandbox/02_git_github/workspace/env_pattern_demo/.env.example <<'EOF'
   DATABASE_URL=postgresql://user:password@localhost:5432/dbname
   API_KEY=your-api-key-here
   EOF
   ```
   (This stays in `workspace/`, disposable — the real pattern gets built
   for real starting in Phase 04 and Checkpoint 4.)
4. Check GitHub's actual security settings for this repo:
   ```bash
   gh api repos/Linhsmiler47/Learn-DE | grep -i "security\|visibility"
   ```
   Or check via the web UI: **Settings → Code security and analysis** —
   note what's actually enabled right now.
5. Document your real push-protection incident (see the lesson's Case
   Study section) in your evidence file.

## Evidence to Record

In `notes/lesson_11_evidence.md`: all audit command output, your
`.env.example` example, the actual current state of this repo's security
settings, and your real incident case study (or an honest note that none
has occurred yet, with a deliberately-practiced scenario instead — see the
lesson for the practice-scenario framing).

## Validation

- `git log --all --full-history -- .env` should show no output (no `.env`
  was ever committed) — if it shows something, that's a real finding to
  act on, not to ignore.

## When You're Done

Move to [`independent.md`](independent.md).
