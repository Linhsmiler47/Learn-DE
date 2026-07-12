# Phase 08 — Kubernetes Fundamentals

## Learning Objectives

- Understand why Kubernetes exists and its control-plane/worker-node architecture.
- Understand Pods, Deployments, ReplicaSets, Services, ConfigMaps, Secrets, Namespaces.
- Deploy a simple multi-container app locally (kind/Minikube) and perform rolling updates.

## Prerequisites

- Phase 05 — Docker
- Phase 07 — Terraform

## Reference Materials (`ref roadmap/`, read-only)

_(see note below)_

> **No direct source material in `ref roadmap/`.** This phase is built from external documentation and hands-on practice rather than the reference folder — call this out in your own notes so it's clear this knowledge didn't come pre-packaged.

## Core Concepts

- Why container orchestration: the problem Kubernetes solves beyond Docker Compose
- Control plane vs worker nodes
- Pods, Deployments, ReplicaSets, Services, Ingress
- ConfigMaps, Secrets, Namespaces, Persistent Volumes
- Scaling, health checks, rolling updates, Helm fundamentals

## Exercises

- Stand up a local cluster (kind or Minikube) and deploy a simple app via a raw manifest.
- Convert env vars into a ConfigMap and a Secret, mounted into the pod.
- Scale the Deployment manually, then perform a rolling update by changing the image tag.
- Package the manifests as a minimal Helm chart.

## Expected Output

- Working manifests or a Helm chart deploying a simple multi-container app.
- Notes on what `kubectl describe` showed during a rollout and a simulated pod crash.

## Validation Checklist

- [ ] A rolling update completes with zero downtime (old pods stay up until new ones are ready).
- [ ] A killed pod is automatically replaced by the ReplicaSet controller.

## Common Mistakes

- Putting secrets directly in a ConfigMap instead of a Secret object.
- Skipping resource requests/limits and being surprised by scheduling behavior.

## Optional Challenges

- Add a liveness and readiness probe and observe the difference in failure handling.

## Reflection Questions

- Do NOT go into production-level Kubernetes administration yet — note what you're deliberately deferring and why.
