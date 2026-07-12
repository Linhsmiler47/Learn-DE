# Phase 09 — Python for Data Engineering

## Learning Objectives

- Write maintainable Python: functions, modules, packages, virtual environments.
- Handle files, exceptions, logging, and type hints idiomatically.
- Use pandas, connect to databases, and integrate with APIs.

## Prerequisites

- Phase 01 — Linux basics

## Reference Materials (`ref roadmap/`, read-only)

- [Python install notes](../../ref%20roadmap/My%20mentor/BUỔI%201/LESSON%201%20-%20Cài%20đặt%20Python.docx)
- [Concurrency comparison scripts: threads vs multiprocessing vs dask](../../ref%20roadmap/My%20mentor/BUỔI%203/BÀI%20GIẢNG/BIGDATA/SPARK/CODE%20SAMPLE/test_da_luong_with_ThreadPoolExecutor.py)
- [More concurrency examples in the same folder](../../ref%20roadmap/My%20mentor/BUỔI%203/BÀI%20GIẢNG/BIGDATA/SPARK/CODE%20SAMPLE/test_da_luong_with_multi_process.py)

> The concurrency scripts under Buổi 3's `CODE SAMPLE` folder are a good advanced reference once you've covered the fundamentals — read, don't copy, and re-derive the pattern yourself.

## Core Concepts

- Functions, modules, packages, virtual environments (venv/conda/uv), dependency management
- File processing, exception handling, logging, type hints
- OOP fundamentals as applied to data pipeline code
- Testing (pytest), pandas basics, database connections, API integration

## Exercises

- Set up a virtual environment and a `pyproject.toml`/`requirements.txt` for a small project.
- Write a file-processing script with proper exception handling and structured logging (not print statements).
- Write pytest tests for a small pandas transformation function.
- Connect to a local PostgreSQL instance from Python and run a parameterized query safely (no string-formatted SQL).

## Expected Output

- A small Python package (not a single script) with tests, type hints, and logging.

## Validation Checklist

- [ ] `pytest` passes and covers at least the core transformation logic.
- [ ] No SQL is built via string concatenation/f-strings (SQL injection risk).

## Common Mistakes

- Using `print()` instead of the `logging` module.
- Catching bare `except:` instead of specific exceptions.

## Optional Challenges

- Re-implement one of the reference concurrency scripts from scratch and benchmark threads vs multiprocessing yourself.

## Reflection Questions

- Where does pandas stop being the right tool, and why (this sets up Phase 16 — Spark)?
