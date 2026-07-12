# System Architecture — Checkpoint 2 — Containerized Python Application with CI

## 1. Problem Statement

A small Python application must run identically on your laptop and in CI, and be validated automatically on every push.

## 2. Scope and Non-Goals

- In scope: TODO — list what this checkpoint must deliver.
- Out of scope: TODO — list what is deferred to a later checkpoint/phase.

## 3. High-Level Architecture Diagram

TODO: replace this placeholder with your own diagram (Mermaid or ASCII) once
you understand how the components below connect.

```
[Source] -> [Python app] -> [Container image] -> [CI workflow] -> [Configuration] -> [Consumer]
```

## 4. Components

| Component | Responsibility | Technology | Why this technology |
|---|---|---|---|
| Python app | Minimal service or script with tests | Python | TODO |
| Container image | Reproducible runtime packaging | Docker | TODO |
| CI workflow | Lint, test, build image on every push | GitHub Actions | TODO |
| Configuration | Environment-specific settings via env vars/.env | dotenv/YAML | TODO |

## 5. Scalability Considerations

- TODO: where does this design break first under 10x data volume or load?

## 6. Reliability Considerations

- TODO: what happens when each component fails? Retries? Idempotency?

## 7. Security Considerations

- TODO: what secrets/credentials exist here, and how are they kept out of git?

## 8. Open Questions

- TODO
