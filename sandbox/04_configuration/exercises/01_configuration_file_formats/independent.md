# Independent Exercise — Lesson 01: Configuration File Formats

## Goal

Represent a more complex, realistic DE config in a format you didn't use
in the guided exercise, and in INI — proving you understand each format's
real limitations, not just its happy path.

## Task

Design a slightly more complex configuration than the guided exercise's —
e.g., add a second data source (a second API endpoint with its own
timeout and retry policy) to the same pipeline config. Represent it in
**INI** and in **XML**. For INI specifically, work through how you'd
represent two similarly-shaped sections (`[api_primary]`, `[api_secondary]`)
given INI's weak support for nested/repeated structures.

## Constraints

- The two data sources must have genuinely different values (not copies)
  so the representation actually has to distinguish them.

## Expected Behavior

Both files represent the same real information; you can explain, in
writing, where INI's format felt limiting compared to YAML/JSON/TOML for
this specific two-source case.

## Validation Commands

- Manual inspection — INI/XML don't have as convenient a one-line CLI
  validator as the guided exercise's three formats; instead, write out
  by hand what the parsed structure *should* look like and confirm your
  file matches it.

## Evidence to Submit

In `notes/lesson_01_evidence.md`: both files' contents, and a short
written comparison of how INI vs. XML each handled (or struggled with)
representing two similarly-shaped sections.

## Do Not

- Do not use a trivial single-value example — the point is stress-testing
  the format against a genuinely two-part structure.
