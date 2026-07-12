# Phase 07 — Infrastructure as Code with Terraform

## Learning Objectives

- Understand IaC principles and Terraform's provider/resource/state model.
- Write and apply Terraform configs locally without requiring paid cloud resources.
- Understand modules, variables, outputs, and the plan/apply/destroy workflow.

## Prerequisites

- Phase 01 — Linux
- Phase 04 — Configuration

## Reference Materials (`ref roadmap/`, read-only)

_(see note below)_

> **No direct source material in `ref roadmap/`.** This phase is built from external documentation and hands-on practice rather than the reference folder — call this out in your own notes so it's clear this knowledge didn't come pre-packaged.

## Core Concepts

- Why Infrastructure as Code, vs manual/console-driven infra
- Terraform architecture: providers, resources, variables, outputs, state, remote state
- Modules and reuse
- Workflow: `plan`, `apply`, `destroy`
- Environment management (dev/test/prod) with Terraform workspaces or directory separation

## Exercises

- Use the Terraform `local` or `docker` provider (both free, no cloud account needed) to define and manage a resource declaratively.
- Extract repeated config into a reusable module with variables and outputs.
- Practice the full `plan` -> `apply` -> `destroy` cycle and read the plan output critically before applying.
- Break something on purpose (manually change a resource outside Terraform) and observe drift on the next `plan`.

## Expected Output

- A small Terraform project with at least one module.
- Documented `plan` output showing you understand exactly what would change before applying.

## Validation Checklist

- [ ] You can explain what Terraform state is for and why it shouldn't be hand-edited.
- [ ] You've observed and explained a drift scenario.

## Common Mistakes

- Applying without reading the plan output.
- Committing the Terraform state file when it contains sensitive data.

## Optional Challenges

- Use the Docker provider to declaratively manage the Checkpoint 2 container instead of `docker run`.

## Reflection Questions

- Why does 'no paid cloud resources at the beginning' still teach the same core skill you'd use on Azure/AWS later?
