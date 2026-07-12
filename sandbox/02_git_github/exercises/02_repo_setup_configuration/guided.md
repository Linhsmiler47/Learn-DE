# Guided Exercise — Lesson 02: Repository Setup, Configuration, `.gitignore` & `.gitattributes`

## Steps

1. See `git init` happen once, in disposable space:
   ```bash
   mkdir -p ~/Projects/Learn-DE/sandbox/02_git_github/workspace/init_demo
   cd ~/Projects/Learn-DE/sandbox/02_git_github/workspace/init_demo
   git init
   ls -la .git
   ```
2. Inspect the real repo's actual configuration (read-only):
   ```bash
   cd ~/Projects/Learn-DE
   git config --list --show-origin
   ```
3. Create a real feature branch and add a real `.gitattributes`:
   ```bash
   git switch main
   git switch -c phase-02/gitattributes
   cat > .gitattributes <<'EOF'
   * text=auto

   *.csv binary
   *.parquet binary
   *.xlsx binary
   *.docx binary
   *.pdf binary
   EOF
   git add .gitattributes
   git commit -m "Add .gitattributes for line-ending normalization and binary data files"
   ```
4. Verify it's being applied:
   ```bash
   git check-attr text -- README.md
   git check-attr binary -- some_file.csv   # substitute a real path if one exists in the repo
   ```

## Evidence to Record

In `notes/lesson_02_evidence.md`: all four steps' output, including the
`.git/` directory listing from step 1 and the `git check-attr` confirmation
from step 4.

## Validation

- `git check-attr text -- README.md` should report `text: auto`.
- `git log --oneline phase-02/gitattributes -1` should show your real commit.

## When You're Done

Move to [`independent.md`](independent.md). Keep the `phase-02/gitattributes`
branch — it becomes a real PR in Lesson 08's independent exercise.
