# Lesson 02 — Repository Setup, Configuration, `.gitignore` & `.gitattributes`

**Estimated effort:** Theory ~25 min · Guided practice ~25 min · Independent practice ~20 min

## Why This Matters

`Learn-DE` already exists — you won't `git init` it. But you'll `git init`
plenty of other things across this path (Checkpoint repos, later
experiments), and you'll configure `.gitignore`/`.gitattributes` on nearly
every project you ever touch. Data Engineering repos in particular mix
code with data samples (`.csv`, `.parquet`, notebooks) — getting these two
files right early prevents a repo full of noisy diffs and accidentally
committed data files later.

## Learning Objectives

- Know what `git init` actually creates, by seeing it happen once.
- Understand git config's three scopes (system/global/local) and which one to use when.
- Write an effective `.gitignore` and understand its one real limitation.
- Write a `.gitattributes` for line-ending normalization and binary file handling — directly relevant to a Data Engineering repo.

## Terminology

| Term | Definition |
|---|---|
| `git init` | Creates a new, empty `.git/` directory — turns a folder into a repository. |
| Config scope | Where a setting applies: `--system` (whole machine), `--global` (your user), `--local` (this repo only, default). |
| `.gitignore` | Tells Git which *untracked* files to stop suggesting/showing — has no effect on files already tracked. |
| `.gitattributes` | Tells Git how to *treat* certain paths — line endings, diff/merge behavior, marking files as binary. |

## Mental Model

```
git config --system   <- rarely used, affects every user on the machine
git config --global   <- your identity, your editor, your defaults (~/.gitconfig)
git config --local    <- this repo only (.git/config) — overrides global
```

Precedence: local beats global beats system. This is why `Learn-DE` can
use your normal identity from `--global` without any extra `--local`
config — you already confirmed this in the guided exercise below.

## Theory: Why `.gitignore` Has a Limit

`.gitignore` only affects **untracked** files. If a file is already
committed, adding it to `.gitignore` does nothing — Git keeps tracking it
because you're already tracking it; the ignore rule only stops *new*,
never-tracked files from showing up as untracked noise. To stop tracking a
file that's already committed, you need `git rm --cached <file>` in
addition to the ignore rule. This trips up almost everyone once.

## Theory: What `.gitattributes` Solves

Two Data-Engineering-relevant problems `.gitignore` can't touch:

1. **Line endings across machines.** Phase 01 already flagged that editing
   a file from `/mnt/c` can introduce `\r\n` line endings. A `.gitattributes`
   rule like `* text=auto` tells Git to normalize line endings consistently
   regardless of what OS/editor touched the file last — much more reliable
   than hoping every contributor's editor is configured the same way.
2. **Data files that shouldn't be diffed as text.** A `.csv` or `.parquet`
   sample file, or a binary export, produces a useless, huge, line-by-line
   diff if Git treats it as text. Marking paths as `binary` in
   `.gitattributes` tells Git "don't try to diff/merge this as text."

## Command Syntax and Safety Notes

| Command | What it changes | Why it matters | Risk level |
|---|---|---|---|
| `git init` | Creates `.git/` in the current directory | Turns a folder into a repo | **None** on an empty folder; **do not** run inside `Learn-DE` itself — it already has a `.git/` (harmless no-op if run there by mistake, but confusing — practice it in `workspace/` instead) |
| `git config --global <key> <value>` | Your user-wide git settings (`~/.gitconfig`) | Identity, default editor, default branch name | **Low** — affects only future commits' authorship metadata |
| `git config --local <key> <value>` | This repo's settings only (`.git/config`) | Overrides global for just this repo | **Low**, but be deliberate — a mismatched local identity on a shared machine causes confusing commit authorship |
| Editing `.gitignore` / `.gitattributes` | Tracked files in the repo | Real, committed changes | **Low** — these are plain text files; commit them like any other change, on a feature branch (see Repository Usage Policy) |

## Step-by-Step Example

**Part 1 — see `git init` happen once, in disposable practice space (never inside `Learn-DE` itself):**

```bash
$ mkdir -p ~/Projects/Learn-DE/sandbox/02_git_github/workspace/init_demo
$ cd ~/Projects/Learn-DE/sandbox/02_git_github/workspace/init_demo
$ git init
Initialized empty Git repository in .../workspace/init_demo/.git/
$ ls -la .git
HEAD  config  description  hooks/  info/  objects/  refs/
```

That's it — an empty repo is just this handful of files/folders. This
practice folder lives under `workspace/`, so it's gitignored and disposable.

**Part 2 — inspect the real repo's actual configuration (read-only, safe):**

```bash
$ cd ~/Projects/Learn-DE
$ git config --list --show-origin
file:/home/<user>/.gitconfig	user.name=Linh Tran
file:/home/<user>/.gitconfig	user.email=linhsmiler47@gmail.com
file:/home/<user>/.gitconfig	init.defaultbranch=main
file:.git/config	core.repositoryformatversion=0
file:.git/config	remote.origin.url=https://github.com/Linhsmiler47/Learn-DE.git
...
```

Your identity is set at `--global` scope, so it applies automatically to
every repo, including this one — no `--local` override needed here.

**Part 3 — real, committed improvement on a feature branch:**

```bash
$ git switch -c phase-02/gitattributes
$ cat > .gitattributes <<'EOF'
* text=auto

*.csv binary
*.parquet binary
*.xlsx binary
*.docx binary
*.pdf binary
EOF
$ git check-attr text -- README.md
README.md: text: auto
$ git check-attr binary -- some_sample.csv   # (against any real .csv this repo has, if one exists)
$ git add .gitattributes
$ git commit -m "Add .gitattributes for line-ending normalization and binary data files"
```

This branch is exactly the kind of small, real, lasting contribution the
Repository Usage Policy calls for — it doesn't need to wait for the Phase
02 assessment to land; you can open a real PR for it now if you want the
practice (Lesson 08 covers exactly that).

## Guided Practice

See [`exercises/02_repo_setup_configuration/guided.md`](../exercises/02_repo_setup_configuration/guided.md).

## Common Mistakes

- Adding a file to `.gitignore` and expecting it to stop being tracked —
  it won't, until you also `git rm --cached` it.
- Setting identity with `--local` on every repo out of habit instead of
  once with `--global`.
- Writing `.gitattributes` rules that are too broad (e.g., marking an
  entire directory `binary` when only some files in it need it).

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| A file still shows as tracked/changed after adding it to `.gitignore` | It was already tracked before the ignore rule existed | `git rm --cached <file>`, then commit |
| `git check-attr` shows no attributes applied | Path pattern in `.gitattributes` doesn't match, or file is outside the repo root | Check the exact pattern and path; patterns are relative to where `.gitattributes` lives |
| Commit author shows the wrong name/email | Wrong config scope, or a stale `--local` override | `git config --list --show-origin` to see exactly which file set it |

## Knowledge Check

1. **Why doesn't adding a file to `.gitignore` untrack it?**
   *Answer: `.gitignore` only affects untracked files; an already-tracked file needs `git rm --cached` in addition.*
2. **What problem does `.gitattributes` solve that `.gitignore` can't?**
   *Answer: How Git treats tracked files — line-ending normalization and marking files as binary so they aren't diffed as text.*
3. **Which config scope should your personal name/email live in, and why?**
   *Answer: `--global` — so it applies automatically to every repository without repeating it.*

## Completion Checklist

- [ ] You've seen `git init` create a `.git/` directory firsthand, in `workspace/`.
- [ ] You can explain the three config scopes and their precedence.
- [ ] You've added a real, committed `.gitattributes` to `Learn-DE` on a feature branch.

## Connects to Later Phases

`.gitattributes`' line-ending and binary-file handling becomes directly
relevant again in Phase 09 (Python) and every Data Engineering checkpoint
that touches sample data files — this is the first time you'll set it up,
not the last.

## Reference Materials

No source material exists in `ref roadmap/` for Git configuration —
authored fresh.

## Next

Guided practice: [`exercises/02_repo_setup_configuration/guided.md`](../exercises/02_repo_setup_configuration/guided.md)
Independent exercise: [`exercises/02_repo_setup_configuration/independent.md`](../exercises/02_repo_setup_configuration/independent.md)
Next lesson: [03 — Staging, Committing & Commit Hygiene](03_staging_commit_hygiene.md)
