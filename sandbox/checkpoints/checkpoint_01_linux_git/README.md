# Checkpoint 1 — Repository & Development-Environment Management

**Builds on:** [`01_linux`](../../01_linux/README.md), [`02_git_github`](../../02_git_github/README.md)

## Business / Learning Problem

Every later checkpoint assumes a working, version-controlled Ubuntu/WSL
environment. This checkpoint builds and documents that environment so it
stops being an unstated assumption.

## Requirements

- A dedicated Git repository (can be a subfolder of this repo or a separate
  one — decide and record the choice as an ADR) for your personal environment
  config (shell profile, aliases, installed-package list).
- A documented, repeatable setup procedure: starting from a bare Ubuntu/WSL
  install, one script or README gets you to a working dev environment.
- Demonstrated use of: branches, at least one merge, one intentionally
  created and resolved merge conflict, `.gitignore`, and one GitHub pull
  request opened against your own repo.

## Milestones

1. Architecture docs completed (see `architecture/`).
2. Environment setup script/checklist written and tested from a clean shell.
3. Git workflow exercised: branch → commit → conflict → resolve → merge → PR.
4. README documenting how a future you (or Claude) would rebuild this
   environment from scratch.

## Expected Outputs

- `setup.sh` or equivalent, with comments explaining each step (TODO markers
  for you to fill in — do not copy a solution).
- Git history showing the branch/merge/conflict workflow.
- A merged (self-reviewed) pull request.

## Testing Requirements

- Setup script re-run on a clean shell (or new WSL distro instance) succeeds
  without manual intervention.

## Documentation Requirements

- `architecture/system_architecture.md`, `data_flow.md` (yes, even config has
  a "flow": install → configure → verify), `component_design.md`, and one ADR
  explaining why you chose your specific shell/tooling setup.

## Validation Checklist

- [ ] Clean-environment setup script exists and is tested.
- [ ] At least one real merge conflict was created and resolved (not staged).
- [ ] `.gitignore` excludes secrets/credentials appropriately.
- [ ] A PR was opened and merged on GitHub.
- [ ] Architecture docs are filled in, not left as templates.

## Completion Criteria

You can destroy your WSL distro, recreate it, run your setup script, and be
back to a working state without consulting memory.
