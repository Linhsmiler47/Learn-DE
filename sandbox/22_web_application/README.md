# Phase 22 — Simple Web Application

## Learning Objectives

- Build a small web app that consumes the FastAPI backend and displays processed data.
- Show metrics, tables, and basic charts, and handle API errors gracefully.

## Prerequisites

- Phase 21 — FastAPI backend

## Reference Materials (`ref roadmap/`, read-only)

_(see note below)_

> **No direct source material in `ref roadmap/`.** This phase is built from external documentation and hands-on practice rather than the reference folder — call this out in your own notes so it's clear this knowledge didn't come pre-packaged.

## Core Concepts

- Frontend options for a beginner: Streamlit vs React vs Next.js trade-offs
- Consuming a REST API from a frontend
- Displaying metrics, tables, basic charts
- Handling API errors in the UI (not just the happy path)

## Exercises

- Start with Streamlit (simplest option) to build a dashboard consuming Phase 21's API.
- Display at least one metric, one table, and one chart backed by live API data.
- Simulate the API being down and verify the UI degrades gracefully instead of crashing.
- Optional stretch: rebuild the same dashboard in React/Next.js and compare the development experience.

## Expected Output

- A working web app consuming the FastAPI backend, showing real pipeline data.

## Validation Checklist

- [ ] The app clearly communicates an API error to the user instead of showing a blank page or stack trace.
- [ ] Charts/tables reflect live data, not hardcoded samples.

## Common Mistakes

- Hardcoding the API URL instead of reading it from configuration (see Phase 04).
- No loading/error states — the UI just breaks silently on a slow or failed request.

## Optional Challenges

- Add a simple filter/date-range control that changes the API query parameters.

## Reflection Questions

- Why does the requirements doc recommend starting with the simplest frontend option before more complex frameworks?
