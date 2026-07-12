# System Architecture — Checkpoint 3 — Local Infrastructure Deployment Lab

## 1. Problem Statement

You need to define infrastructure as versioned code and deploy the Checkpoint 2 container to a local, orchestrated environment instead of running it by hand.

## 2. Scope and Non-Goals

- In scope: TODO — list what this checkpoint must deliver.
- Out of scope: TODO — list what is deferred to a later checkpoint/phase.

## 3. High-Level Architecture Diagram

TODO: replace this placeholder with your own diagram (Mermaid or ASCII) once
you understand how the components below connect.

```
[Source] -> [Terraform config] -> [Kubernetes manifests / Helm] -> [Local cluster] -> [Consumer]
```

## 4. Components

| Component | Responsibility | Technology | Why this technology |
|---|---|---|---|
| Terraform config | Declarative definition of local/dummy resources | Terraform | TODO |
| Kubernetes manifests / Helm | Deployment, Service, ConfigMap for the app | kind/Minikube, kubectl | TODO |
| Local cluster | Where the workload actually runs | kind or Minikube | TODO |

## 5. Scalability Considerations

- TODO: where does this design break first under 10x data volume or load?

## 6. Reliability Considerations

- TODO: what happens when each component fails? Retries? Idempotency?

## 7. Security Considerations

- TODO: what secrets/credentials exist here, and how are they kept out of git?

## 8. Open Questions

- TODO
