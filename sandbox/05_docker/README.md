# Phase 05 — Docker and Container Architecture

## Learning Objectives

- Understand containers vs VMs and Docker's architecture (images, containers, layers).
- Write Dockerfiles, use volumes/networks, and run multi-container apps with Compose.
- Understand container logs, health checks, and basic container security.

## Prerequisites

- Phase 01 — Linux basics
- Phase 04 — Configuration (env vars into containers)

## Reference Materials (`ref roadmap/`, read-only)

- [What Docker is and why enterprises use it](../../ref%20roadmap/My%20mentor/BUỔI%208/BÀI%20GIẢNG/DOCKER/LESSON%208%20-%20Docker%20là%20gì%20vì%20sao%20lại%20được%20sử%20dụng%20trong%20doanh%20nghiệp.docx)
- [Docker architecture](../../ref%20roadmap/My%20mentor/BUỔI%208/BÀI%20GIẢNG/DOCKER/LESSON%208%20-%20Kiến%20trúc%20của%20Docker.docx)
- [Installing Docker on Ubuntu](../../ref%20roadmap/My%20mentor/BUỔI%208/BÀI%20GIẢNG/DOCKER/LESSON%208%20-%20Cài%20đặt%20Docker%20trên%20Ubuntu.docx)
- [What Docker Compose is](../../ref%20roadmap/My%20mentor/BUỔI%208/BÀI%20GIẢNG/DOCKER/LESSON%208%20-%20Docker%20Compose%20là%20gì.docx)
- [Docker cheat sheet](../../ref%20roadmap/My%20mentor/BUỔI%208/BÀI%20GIẢNG/DOCKER/LESSON%208%20-%20Cheatsheet%20cho%20Docker.docx)
- [Demo: MySQL to PostgreSQL sync via Kafka using Docker](../../ref%20roadmap/My%20mentor/BUỔI%208/BÀI%20GIẢNG/DOCKER/LESSON%208%20-%20Xây%20dựng%20demo%20đồng%20bộ%20bảng%20customer%20từ%20mysql%20tới%20postgresql%20thông%20qua%20kafka%20bằng%20Docker.docx)

> This phase is moved earlier than the source material's session order (Buổi 8) — architecturally, Docker is infrastructure you want before deep-diving into every later tool install.

## Core Concepts

- Containers vs virtual machines
- Images, containers, Dockerfile, layers and caching
- Volumes, networks, published ports, environment variables in containers
- Docker Compose for multi-container apps
- Container logs, health checks, basic image security (minimal base images, not running as root)

## Exercises

- Write a Dockerfile for a small Python app; optimize it for layer caching and image size.
- Use Docker Compose to run that app alongside a PostgreSQL container, connected over a user-defined network.
- Add a `HEALTHCHECK` to the Dockerfile and observe `docker ps` reflect health status.
- Mount a named volume for Postgres data and prove data survives a container restart.

## Expected Output

- A working `Dockerfile` and `docker-compose.yml` for a two-service app.
- Notes on what changed in image size/build time as you optimized layers.

## Validation Checklist

- [ ] `docker compose up` brings up both services with no manual steps.
- [ ] Data in the Postgres volume survives `docker compose down` (without `-v`) and back up.
- [ ] The health check accurately reflects the app's real readiness.

## Common Mistakes

- Running the app as root inside the container.
- Baking secrets into the image instead of passing them at runtime.

## Optional Challenges

- Multi-stage build to shrink a Python image down using a slim/distroless final stage.

## Reflection Questions

- What's the difference between a container restarting and a container being unhealthy?
