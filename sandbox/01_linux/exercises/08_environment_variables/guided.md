# Guided Exercise — Lesson 08: Environment Variables & Shell Configuration

## Steps

1. ```bash
   echo $MY_VAR              # empty
   MY_VAR=hello
   echo $MY_VAR               # set in this shell
   bash -c 'echo $MY_VAR'     # empty! not exported
   export MY_VAR=hello
   bash -c 'echo $MY_VAR'     # now inherited
   ```
2. ```bash
   echo $PATH
   which python3
   env | grep WSL
   ```
3. Persist a variable safely:
   ```bash
   echo 'export DECLAB_PRACTICE_VAR=hello' >> ~/.bashrc
   source ~/.bashrc
   echo $DECLAB_PRACTICE_VAR
   ```
4. Clean up (remove the line you added from `~/.bashrc` using a text
   editor, then):
   ```bash
   source ~/.bashrc
   echo $DECLAB_PRACTICE_VAR   # should be empty again after removing the line and re-sourcing
   ```

## Evidence to Record

In `notes/lesson_08_evidence.md`: every command and output, especially the
before/after `export` comparison showing non-exported vs. exported
inheritance.

## Validation

- After cleanup, `echo $DECLAB_PRACTICE_VAR` in a **new** terminal should
  print nothing.

## When You're Done

Move to [`independent.md`](independent.md).
