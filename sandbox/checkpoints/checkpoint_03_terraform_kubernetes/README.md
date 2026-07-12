# Checkpoint 3 — Local Infrastructure Deployment Lab

**Builds on:** [`07_terraform`](../../07_terraform/README.md), [`08_kubernetes`](../../08_kubernetes/README.md)

## Business / Learning Problem

Running `docker run` by hand doesn't scale past one container on one
machine. This checkpoint deploys Checkpoint 2's containerized app onto a
local, orchestrated cluster, defined as code rather than clicked together.

## Requirements

- A local Kubernetes cluster (kind or Minikube).
- Kubernetes manifests (or a Helm chart) deploying Checkpoint 2's image:
  Deployment, Service, ConfigMap/Secret for config.
- Terraform used for at least one piece of local, declarative setup (this
  can be conceptual/local-provider-based — no paid cloud resources).
- A working health check and at least one demonstrated rolling update.

## Milestones

1. Architecture docs completed.
2. `kind`/Minikube cluster running locally.
3. App deployed via manifests/Helm, reachable via `kubectl port-forward` or
   Ingress.
4. Terraform applied at least one resource/config, with `plan` → `apply` →
   `destroy` all demonstrated.
5. Rolling update performed (change the image tag, watch the rollout).

## Expected Outputs

- `terraform/` directory with `.tf` files, `plan` output captured in docs.
- `k8s/` directory with manifests or a Helm chart.
- A recorded (in docs, not video) walkthrough of a rolling update.

## Testing Requirements

- Health check endpoint used by a Kubernetes readiness/liveness probe.
- Demonstrate the pod restarting automatically after a simulated crash.

## Documentation Requirements

- Full `architecture/` folder, with an ADR comparing kind vs Minikube vs
  Docker Desktop Kubernetes, and why you picked one.

## Validation Checklist

- [ ] `terraform plan` and `apply` run without errors, `destroy` cleans up.
- [ ] App is reachable through the cluster, not just a bare container.
- [ ] Rolling update completes with zero manual pod deletion.
- [ ] Crash of a pod is auto-recovered by Kubernetes.

## Completion Criteria

You can `terraform destroy` and delete the cluster, then rebuild both from
code alone and reach a working deployed app again.
