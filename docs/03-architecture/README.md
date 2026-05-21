# Layer 03: Architecture

**Layer Purpose**: System design and 9-layer verification flow

## O.N.I.O.N Architecture Overview

O.N.I.O.N implements a 9-layer verification architecture with Responsible AI integrated at every layer.

## 9-Layer Verification Flow

```
──────────────────────────────────────────────────────────────────────────
Verified • Safe • Secure • Explainable • Accountable • Compliant
Responsible AI enforced everywhere:
Fairness • Reliability & Safety • Privacy & Security • Inclusiveness
Transparency • Accountability
──────────────────────────────────────────────────────────────────────────

👤 Developer │
             ▼
┌───────────────────────────────────────────────────────────┐
│ GitHub Source (Commit / PR / Merge)                        │
└───────────────────────────────────────────────────────────┘
             │
             ✅ VERIFY: code integrity + review trail
             🧠 RAI: Accountability (ownership), Transparency (history)
             ▼

🧅 L1 — ENTRY / TRIGGER (Verification + Governance)
┌───────────────────────────────────────────────────────────┐
│ GitHub Actions Trigger                                      │
│ - workflow events (push/PR)                                 │
│ - protected branches                                        │
└───────────────────────────────────────────────────────────┘
             │
             ✅ VERIFY: trigger correctness + permissions
             🧠 RAI: Governance + accountability at entry
             ▼

🧅 L2 — BUILD (Artifact Integrity)
┌───────────────────────────────────────────────────────────┐
│ Build & Package                                              │
│ - install dependencies                                       │
│ - build container image                                      │
└───────────────────────────────────────────────────────────┘
             │
             ✅ VERIFY: reproducible artifact
             ✅ INTEGRITY: trusted build outputs
             🧠 RAI: Reliability (repeatability)
             ▼

🧅 L3 — TEST (Quality + Safety)
┌───────────────────────────────────────────────────────────┐
│ Test & Quality Gates                                         │
│ - unit / integration tests                                  │
│ - lint / static checks                                      │
└───────────────────────────────────────────────────────────┘
             │
             ✅ VERIFY: correctness + quality
             🛡️ SAFETY: prevent unsafe regressions
             🧠 RAI: Reliability & Safety (tests), Fairness (edge checks)
             ▼

🧅 L4 — POLICY (PDP Decision)
┌───────────────────────────────────────────────────────────┐
│ Policy Decision Point (PDP)                                  │
│ - security checks + compliance rules                         │
│ - produces decision + reasons + obligations                  │
└───────────────────────────────────────────────────────────┘
             │
             ✅ VERIFY: compliance + security gates
             ✅ EXPLAINABILITY: reason codes required
             🧠 RAI: Fairness + Transparency + Accountability
             ▼

🧅 L5 — CONTROL (Approval / Human Oversight)
┌───────────────────────────────────────────────────────────┐
│ Approval Gate                                                 │
│ - parent approval for sensitive actions                       │
│ - release approval for production (if required)               │
└───────────────────────────────────────────────────────────┘
             │
             ✅ VERIFY: authorized oversight
             🧠 RAI: Accountability + human control
             ▼

🧅 L6 — DEPLOY (PEP Enforcement on Azure)
┌───────────────────────────────────────────────────────────┐
│ Deploy to Azure (Container Apps / Kubernetes)                 │
│ - deploy revision                                             │
│ - enforce ingress policies                                    │
└───────────────────────────────────────────────────────────┘
             │
             ✅ VERIFY: correct environment + constraints
             🔐 SECURITY: no bypass allowed (PEP)
             🧠 RAI: Privacy & Security
             ▼

🧅 L7 — RUNTIME VERIFICATION
┌───────────────────────────────────────────────────────────┐
│ Runtime Checks                                                │
│ - health / readiness / liveness                               │
│ - smoke tests                                                 │
└───────────────────────────────────────────────────────────┘
             │
             ✅ VERIFY: safe operation + stability
             🧠 RAI: Reliability & Safety monitoring
             ▼

🧅 L8 — AUDIT / TRACEABILITY
┌───────────────────────────────────────────────────────────┐
│ Audit Evidence                                                │
│ - decision logs + correlation IDs                             │
│ - policy versions + reason codes                              │
└───────────────────────────────────────────────────────────┘
             │
             ✅ VERIFY: accountability evidence
             🧠 RAI: Transparency + accountability
             ▼

🧅 L9 — MONITOR / FEEDBACK LOOP
┌───────────────────────────────────────────────────────────┐
│ Monitoring / Observability                                    │
│ - logs/metrics/alerts                                         │
│ - anomaly detection                                           │
└───────────────────────────────────────────────────────────┘
             │
             ✅ VERIFY: drift detection + continuous evaluation
             🧠 RAI: ongoing monitoring & evaluation
             ▼

🔁 Continuous loop: Commit → Verify → Decide → Deploy → Verify → Monitor → Improve
```

## Architecture Principles

### 1. Agents Propose, PDP Decides

- **Agents**: Analyze, propose, provide context (non-authoritative)
- **PDP**: Evaluate policies, make decisions (authoritative)
- **PEP**: Enforce decisions (no discretion)
- **Audit**: Log everything (immutable)

### 2. Defense in Depth

Multiple independent verification layers:
- Entry validation (L1)
- Build integrity (L2)
- Quality gates (L3)
- Policy decisions (L4)
- Human oversight (L5)
- Enforcement (L6)
- Runtime verification (L7)
- Audit trail (L8)
- Continuous monitoring (L9)

### 3. Default Deny

- Unknown actions are denied
- Uncertain situations require approval
- Fail secure on errors

### 4. Explainability Required

- Every decision has a reason code
- Age-appropriate explanations
- Full audit trail

### 5. Immutable Audit

- All decisions logged
- Tamper-evident
- Correlation IDs for tracing

## Component Architecture

### Services (Authoritative)

- **API Gateway (PEP)**: Enforces policies, routes requests
- **Policy PDP**: Makes policy decisions
- **Approval Service**: Manages human oversight
- **Audit Service**: Immutable logging
- **Telemetry Ingest**: Signal collection
- **Notification Service**: User communications

### Agents (Non-Authoritative)

- **Behavior Agent**: Risk pattern detection
- **Anomaly Agent**: Safety violation detection
- **Context Agent**: Signal enrichment
- **Explanation Agent**: Decision explanations

## Data Flow

1. **Request** → API Gateway (PEP)
2. **Validation** → Check authentication/authorization
3. **Signal Collection** → Agents propose assessments
4. **Policy Evaluation** → PDP makes decision
5. **Approval** (if required) → Parent/guardian approval
6. **Enforcement** → PEP enforces decision
7. **Audit** → Log decision with full context
8. **Response** → Return to user with explanation

## Deployment Architecture

- **Azure Container Apps**: Microservices hosting
- **Azure Key Vault**: Secrets management
- **Azure Application Insights**: Monitoring
- **Azure Database**: Audit storage
- **GitHub Actions**: CI/CD pipeline

## Responsible AI Integration

Each layer integrates Responsible AI principles:

- **L1-L3**: Reliability, Transparency, Accountability
- **L4**: Fairness, Transparency, Accountability
- **L5**: Human oversight, Accountability
- **L6**: Privacy & Security
- **L7-L9**: Reliability & Safety, Transparency

## Document Control

- **Version**: 1.0.0
- **Last Updated**: 2026-05-21
- **Owner**: Architecture Team
