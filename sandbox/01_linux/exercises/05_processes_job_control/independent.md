# Independent Exercise — Lesson 05: Processes & Job Control

## Goal

Find and terminate a background process by name, without already knowing
its PID, and using the correct signal escalation order.

## Task

Write a tiny script in `workspace/processes_practice/` (a few lines of
bash) that loops forever printing a timestamp every few seconds, similar in
spirit to Lesson 06's service script but simpler. Start it in the
background. Without noting its PID at launch time, use process-inspection
commands to find it by name, confirm it's the right one (check its command
line, not just its name), then terminate it — trying a plain `kill` first
and only escalating to `kill -9` if it doesn't respond.

## Constraints

- The script must live under `workspace/processes_practice/`.
- You must locate the process by name/pattern, not by reusing a PID you
  happened to note down at launch.

## Expected Behavior

The process should stop running, confirmed by no longer appearing in a
process listing, and you should be able to state which signal actually
stopped it.

## Validation Commands

- `pgrep -af <part of your script's name>` (before and after)
- `ps aux | grep <script name>`

## Evidence to Submit

In `notes/lesson_05_evidence.md`: the script's contents, how you located
the running process without a pre-noted PID, which signal you tried first,
whether it was sufficient, and the final proof the process is gone.

## Do Not

- Do not jump straight to `kill -9` without first trying a plain `kill`.
- Do not run this against any process you didn't start yourself.
