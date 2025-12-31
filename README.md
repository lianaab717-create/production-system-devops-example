# Production System – DevOps / SRE Portfolio

This repository demonstrates a production-grade system design,
showcasing practical DevOps and Site Reliability Engineering (SRE) principles.

---

## 🏆 Highlights

- **Kubernetes deployment** with autoscaling, resilience, and network policies
- **GitOps** using Argo CD for declarative infrastructure
- **CI/CD pipeline** with GitHub Actions & Docker builds
- **Observability**: Prometheus metrics, ELK logging, SLO-focused dashboards
- **Incident & postmortem examples** for reliability culture
- **Security**: Network policies & pod security best practices

---

## 📂 Repository Structure

```text
production-system/
├── app/                    # Sample API & Dockerfile
│   └── api.py
│
├── k8s/                    # Kubernetes manifests
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── hpa.yaml
│   ├── pdb.yaml
│   ├── probes.yaml
│   └── security.yaml
│
├── observability/          # Metrics, logs, dashboards
│   ├── metrics/
│   │   ├── prometheus.yml
│   │   ├── recording-rules.yaml
│   │   ├── alert-burn-rate.yaml
│   │   └── alert-latency.yaml
│   ├── logs/
│   │   └── logstash.conf
│   └── dashboards/
│       └── slo-focused.json
│
├── gitops/                 # Argo CD application
│   └── argo-application.yaml
│
├── incidents/              # Incident reports & postmortem template
│   ├── incident-latency.md
│   └── postmortem-template.md
│
├── .github/workflows/      # CI/CD pipelines
│   └── ci-cd.yaml
│
└── README.md
