# Component Design — Checkpoint 3 — Local Infrastructure Deployment Lab

## Component: Terraform config

- **Responsibility**: Declarative definition of local/dummy resources
- **Inputs**: TODO
- **Outputs**: TODO
- **Configuration**: TODO (see `04_configuration`)
- **Dependencies**: TODO
- **Failure mode**: TODO
- **Trade-offs considered**: TODO — alternatives to Terraform you considered and why you didn't pick them

## Component: Kubernetes manifests / Helm

- **Responsibility**: Deployment, Service, ConfigMap for the app
- **Inputs**: TODO
- **Outputs**: TODO
- **Configuration**: TODO (see `04_configuration`)
- **Dependencies**: TODO
- **Failure mode**: TODO
- **Trade-offs considered**: TODO — alternatives to kind/Minikube, kubectl you considered and why you didn't pick them

## Component: Local cluster

- **Responsibility**: Where the workload actually runs
- **Inputs**: TODO
- **Outputs**: TODO
- **Configuration**: TODO (see `04_configuration`)
- **Dependencies**: TODO
- **Failure mode**: TODO
- **Trade-offs considered**: TODO — alternatives to kind or Minikube you considered and why you didn't pick them


## Cross-Component Contracts

- TODO: interfaces/APIs/topics/tables shared between components above.
- TODO: versioning approach for those contracts.
