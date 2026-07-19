# Guided Exercise — Lesson 02: Application Configuration

## Goal

Build a real config loader with fail-fast validation and demonstrate
precedence.

## Steps

1. ```bash
   mkdir -p ~/Projects/Learn-DE/sandbox/04_configuration/workspace/config_loader_practice
   cd ~/Projects/Learn-DE/sandbox/04_configuration/workspace/config_loader_practice
   cat > .env.example <<'EOF'
   DATABASE_URL=postgresql://user:password@localhost:5432/pipeline_db
   API_KEY=your-api-key-here
   BATCH_SIZE=250
   MAX_RETRIES=3
   EOF
   cp .env.example .env
   ```
2. Write `load_config.py` implementing the fail-fast loader shown in the
   lesson (validate `DATABASE_URL` and `API_KEY` are present; default
   `BATCH_SIZE`/`MAX_RETRIES` if absent).
3. Test the happy path:
   ```bash
   export $(grep -v '^#' .env | xargs)
   python3 load_config.py
   ```
4. Test the fail-fast path — remove `API_KEY` from your exported
   environment and re-run; confirm it refuses to proceed with a clear message.
5. Test precedence — override `BATCH_SIZE` with an inline env var and
   confirm it wins:
   ```bash
   BATCH_SIZE=1000 python3 load_config.py
   ```

## Evidence to Record

In `notes/lesson_02_evidence.md`: `load_config.py`'s contents, the
happy-path output, the fail-fast error message (real, not paraphrased),
and the precedence-override output.

## Validation

- The fail-fast test must exit non-zero with a clear message naming the
  missing variable — not a generic Python traceback.
- The precedence test must show `1000`, not `250` or the `.env` value.

## When You're Done

Move to [`independent.md`](independent.md).
