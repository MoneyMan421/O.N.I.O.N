# 🧅 ONION Guardian Agent
**Verified, Responsible, Safety‑First AI System (Child‑Centered)**

[![GitHub Best Practices](https://img.shields.io/badge/GitHub-Best%20Practices-blue)](https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories)
[![Responsible AI](https://img.shields.io/badge/Responsible%20AI-6%20Principles-green)](https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai?view=azureml-api-2)
[![OWASP CI/CD Security](https://img.shields.io/badge/OWASP-CI%2FCD%20Security-orange)](https://cheatsheetseries.owasp.org/cheatsheets/CI_CD_Security_Cheat_Sheet.html)

---

## 🎯 Mission (Merged with Responsible AI)

Build systems that **never operate without verification** and **never make decisions without responsibility**.

ONION is a **zero‑trust, policy‑driven architecture** where:
- Every action is **validated** before execution
- Every decision is **explainable** and **traceable**
- Every outcome is **accountable** to a responsible owner
- Every system is **safe, secure, and compliant**

### Responsible AI Commitment

ONION is built and governed according to the **six Responsible AI principles**:

| Principle | Description |
|---|---|
| ⚖️ **Fairness** | AI systems treat all people fairly and avoid bias |
| 🛡️ **Reliability & Safety** | AI systems perform reliably and safely under all conditions |
| 🔒 **Privacy & Security** | AI systems respect privacy and maintain security |
| 🌍 **Inclusiveness** | AI systems empower everyone and engage all people |
| 🔍 **Transparency** | AI systems are understandable; humans understand what they do |
| ✅ **Accountability** | People are accountable for AI systems and their outcomes |

> These six principles are the foundation of Microsoft's Responsible AI Standard.  
> References: [Azure ML Responsible AI](https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai?view=azureml-api-2) · [Azure Security & Responsible AI Guide](https://azure.github.io/Security-and-Responsible-AI-Guide/chapters/chapter_01_understanding_security_and_responsible_ai)

**One-line principle:**
> Verified systems + Responsible AI at every layer = trustworthy execution.

---

## 🧅 What "ONION" Means (Kid‑Friendly + AI‑Accurate Acronym)

ONION describes how the system "thinks" — in simple words kids can understand, but still accurate for AI systems:

| Letter | AI Term | Kid Term | What It Does |
|---|---|---|---|
| **O** | Observe / Origin | 👀 Look | Collect safe inputs from the environment |
| **N** | Notice / Navigate | 🔎 Notice | Detect patterns & risk signals |
| **I** | Infer / Imagine | 🤔 Think | Reason and choose safe options |
| **O** | Operate / Organize | ✅ Do | Apply policy and enforce constraints |
| **N** | Narrate / Notify | 📢 Tell | Explain decisions and alert parents/guardians |

**Kid version:** Look → Notice → Think → Do → Tell.

---

## 🧠 Core Architecture

ONION is built as **multi‑level + multi‑layer defense**, so **no single control is trusted**.

```
┌─────────────────────────────────────────────────────────────────┐
│                      ONION Guardian Agent                       │
├─────────────────────────────────────────────────────────────────┤
│  Layer 1 (Outermost): Input Validation & Origin Trust           │
│  Layer 2:             Threat Detection & Risk Scoring           │
│  Layer 3:             Inference Engine & Policy Evaluation      │
│  Layer 4:             Enforcement & Constraint Application      │
│  Layer 5 (Innermost): Audit, Narration & Guardian Notification  │
└─────────────────────────────────────────────────────────────────┘
```

### Core Services

| Service | Role | Description |
|---|---|---|
| `api-gateway` | Policy Enforcement Point (PEP) | Entry point; validates every request |
| `policy-pdp` | Policy Decision Point (PDP) | Evaluates policy rules; approves/denies actions |
| `approval-service` | Parent / Guardian Approvals | Handles overrides and parent consent flows |
| `telemetry-ingest` | Device Telemetry Intake | Ingests wearable/device data streams |
| `notification-service` | Alerts & Communications | Real-time alerts to guardians |
| `audit-service` | Immutable Audit Trail | Stores tamper-proof evidence of every decision |

---

## 🔁 Full Flow Diagram (GitHub → CI/CD → Azure → Runtime → Audit)

This is the full beginning-to-end system flow, with verification and Responsible AI embedded at every step.

```
Developer Workstation
        │
        │  git push (signed commits)
        ▼
┌───────────────────┐
│   GitHub Repo     │  ← Branch protection, CODEOWNERS, secret scanning,
│                   │    dependency review, Dependabot alerts
└────────┬──────────┘
         │  PR created → required reviewers + status checks
         ▼
┌───────────────────┐
│  GitHub Actions   │  ← OIDC auth (no long-lived secrets)
│  CI/CD Pipeline   │    • SAST (CodeQL)
│                   │    • Dependency audit
│                   │    • Container image scan
│                   │    • Policy-as-code lint (OPA/Conftest)
│                   │    • Unit + integration tests
└────────┬──────────┘
         │  Artifacts signed (cosign / SLSA provenance)
         ▼
┌───────────────────┐
│  Azure Container  │  ← Image pulled only if signature verified
│  Registry (ACR)   │    Quarantine policy for unscanned images
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│  Azure Kubernetes │  ← Pod Security Standards (restricted)
│  Service (AKS)    │    OPA Gatekeeper policies enforced
│                   │    Workload Identity (no secret mounts)
│                   │    Network policies (zero-trust east-west)
└────────┬──────────┘
         │
         ▼
┌───────────────────────────────────────────────────────┐
│                   ONION Runtime                       │
│                                                       │
│  [api-gateway] ──► [policy-pdp] ──► [approval-svc]   │
│       │                 │                             │
│       │           Policy DENY?──► [notification-svc]  │
│       │                 │           (alert guardian)  │
│       ▼                 ▼                             │
│  [telemetry-ingest]  Policy ALLOW                     │
│       │                 │                             │
│       ▼                 ▼                             │
│  [audit-service] ◄──────┘  (every decision logged)   │
└────────┬──────────────────────────────────────────────┘
         │
         ▼
┌───────────────────┐
│  Azure Monitor /  │  ← Metrics, logs, distributed traces
│  Defender for     │    Anomaly detection alerts
│  Cloud            │    Compliance posture dashboard
└───────────────────┘
```

---

## ✅ Verification at Every Layer

| Layer | What Is Verified | How |
|---|---|---|
| **Source Code** | No secrets committed | GitHub secret scanning + pre-commit hooks |
| **Dependencies** | No known CVEs | Dependabot + `npm audit` / `pip audit` |
| **Build** | Code quality & security | CodeQL SAST, lint, unit tests |
| **Artifact** | Image integrity | cosign signature + SLSA provenance attestation |
| **Registry** | Image not tampered | ACR content trust + quarantine policy |
| **Deployment** | Config matches policy | OPA Gatekeeper + Conftest |
| **Runtime** | Requests are authorized | PEP → PDP policy evaluation |
| **Data** | Inputs are safe | Input validation + schema enforcement |
| **Decisions** | Decisions are explainable | Audit log entry per decision |
| **Alerts** | Guardians are notified** | Notification service + escalation rules |

---

## 🔒 Compliance, Safety & Security Guidelines

### Security Principles (OWASP CI/CD Top 10 Mitigations)
- **No long-lived credentials** — use OIDC/workload identity everywhere
- **Least-privilege** — every service account has minimum required permissions
- **Immutable artifacts** — built once, signed, deployed; never rebuilt in prod
- **Dependency pinning** — lock file committed; Dependabot monitors drift
- **Audit everything** — every pipeline run, deployment, and runtime decision is logged

### Safety Rules
- **No autonomous action without policy approval** — `policy-pdp` must return `ALLOW`
- **No silent failures** — all errors surface to `notification-service`
- **Guardian override always available** — `approval-service` enables human-in-the-loop
- **Data minimization** — collect only what is needed; purge on schedule

### Privacy
- All telemetry is anonymized at ingestion before storage
- PII is encrypted at rest (AES-256) and in transit (TLS 1.3+)
- Data retention policies enforced automatically

### Regulatory Alignment
- GDPR / COPPA — child data protection by design
- ISO 27001 — information security controls
- NIST AI RMF — AI risk management framework alignment
- OWASP ASVS Level 2 — application security verification

---

## 📋 GitHub "Everything You Need" Checklist

### Repository Files
- [ ] `README.md` — this file; purpose, architecture, usage
- [ ] `SECURITY.md` — vulnerability reporting policy
- [ ] `CONTRIBUTING.md` — how to contribute; code of conduct reference
- [ ] `CODE_OF_CONDUCT.md` — community standards
- [ ] `CODEOWNERS` — mandatory reviewers per path
- [ ] `LICENSE` — open-source license declaration
- [ ] `.gitignore` — exclude build artifacts, secrets, temp files
- [ ] `.github/PULL_REQUEST_TEMPLATE.md` — PR checklist
- [ ] `.github/ISSUE_TEMPLATE/` — bug report & feature request templates
- [ ] `.github/workflows/ci.yml` — CI pipeline (lint, test, scan)
- [ ] `.github/workflows/cd.yml` — CD pipeline (build, sign, deploy)
- [ ] `.github/dependabot.yml` — automated dependency updates

### Repository Settings
- [ ] **Branch protection on `main`** — require PR, require status checks, no force push
- [ ] **Required status checks** — CI must pass before merge
- [ ] **Required reviewers** — minimum 1 (CODEOWNERS enforced)
- [ ] **Signed commits** — required on protected branches
- [ ] **Auto-delete head branches** — keep repo clean after merge
- [ ] **Discussions** — enabled for community Q&A

### Security Features (GitHub Advanced Security)
- [ ] **Secret scanning** — enabled; push protection on
- [ ] **Dependabot alerts** — enabled
- [ ] **Dependabot security updates** — auto PRs for vulnerable deps
- [ ] **Dependency review** — block PRs that introduce vulnerable packages
- [ ] **Code scanning (CodeQL)** — enabled on push + PR
- [ ] **Private vulnerability reporting** — enabled

### CI/CD Security (GitHub Actions)
- [ ] **OIDC** — use `permissions: id-token: write` instead of stored secrets
- [ ] **Pin third-party actions to SHA** — use `@<sha>` for unverified/third-party actions; semantic versions (e.g. `@v4`) are acceptable for GitHub's own verified actions
- [ ] **Minimal permissions** — `permissions:` block on every workflow
- [ ] **No `pull_request_target`** — unless strictly required and reviewed
- [ ] **Artifact attestation** — `actions/attest-build-provenance` on release

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/Big-Orga/O.N.I.O.N.git
cd O.N.I.O.N

# Review the architecture docs
cat README.md

# (Coming soon) Start local development environment
# docker compose up
```

---

## 🤝 Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting pull requests.  
All contributors must follow our [Code of Conduct](CODE_OF_CONDUCT.md).

---

## 📜 License

See [LICENSE](LICENSE) for details.

---

## 🔗 References

- [GitHub Best Practices for Repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories)
- [Microsoft Responsible AI Principles](https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai?view=azureml-api-2)
- [Azure Security and Responsible AI Guide](https://azure.github.io/Security-and-Responsible-AI-Guide/chapters/chapter_01_understanding_security_and_responsible_ai)
- [OWASP CI/CD Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/CI_CD_Security_Cheat_Sheet.html)
- [NIST AI Risk Management Framework](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf)
- [SLSA Supply Chain Levels for Software Artifacts](https://slsa.dev/)
