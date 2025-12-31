# Production System – DevOps / SRE Example

This repository demonstrates a production-grade system design,
focusing on DevOps and SRE best practices:
CI/CD, Kubernetes, GitOps, observability, and incident management.

## Repository Structure

```text
production-system/
├── app/                    # Sample application (Python API)
│   └── api.py
├── k8s/                    # Kubernetes manifests
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── hpa.yaml
│   ├── pdb.yaml
│   └── probes.yaml
├── observability/          # Metrics, logs, dashboards
│   ├── metrics/
│   ├── logs/
│   └── dashboards/
├── gitops/                 # Argo CD application
├── incidents/              # Incident & postmortem examples
├── .github/workflows/      # CI/CD pipelines (GitHub Actions)
└── README.md
