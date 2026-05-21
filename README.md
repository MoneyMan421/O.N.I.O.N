# 🧅 ONION Guardian Agent — Verified, Responsible, Child‑First AI

[![Repo Best Practices](https://img.shields.io/badge/GitHub-Best%20Practices-blue)](https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories)
[![Responsible AI](https://img.shields.io/badge/Responsible%20AI-6%20Principles-green)](https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai?view=azureml-api-2)
[![CI/CD Security](https://img.shields.io/badge/OWASP-CI%2FCD%20Security-orange)](https://cheatsheetseries.owasp.org/cheatsheets/CI_CD_Security_Cheat_Sheet.html)

> **ONION** is a safety-first, policy-driven AI system designed to protect children with layered verification, parent controls, and explainable decisions.

---

## 🎯 Mission (Merged with Responsible AI)

Build systems that **never operate without verification** and **never make decisions without responsibility**.

ONION is a **zero‑trust, policy‑driven architecture** where:
- Every action is **validated** before execution  
- Every decision is **explainable** and **traceable**  
- Every outcome is **accountable** to a responsible owner  
- Every system is **safe, secure, and compliant**  

### Responsible AI Commitment (6 Principles)
ONION is built and governed using these Responsible AI principles:
- **Fairness**
- **Reliability & Safety**
- **Privacy & Security**
- **Inclusiveness**
- **Transparency**
- **Accountability**

**One‑line principle:**  
> Verified systems + Responsible AI at every layer = trustworthy execution.

---

## 🧅 ONION Acronym (Kid‑Friendly + AI‑Accurate, merged)

ONION describes how the system "thinks" in simple terms kids can understand, while staying accurate to AI workflows:

**O — Observe / Origin** (collect safe inputs)  
**N — Notice / Navigate** (detect patterns & risk signals)  
**I — Infer / Imagine** (reason and choose safe options)  
**O — Operate / Organize** (apply policy + enforce constraints)  
**N — Narrate / Notify** (explain decisions + alert guardians)

**Kid version:** Look → Notice → Think → Do → Tell.

---

## 🧠 Core Architecture (What ONION Is)

ONION is multi-level + multi-layer by design:
- **Agents propose** (signals and suggestions)
- **PDP decides** (policy decision point)
- **PEP enforces** (policy enforcement point)
- **Audit proves** (traceability)
- **Verification validates** (continuous checks)

### Typical Services
- **api-gateway** → PEP (enforcement boundary)
- **policy-pdp** → PDP (single source of truth decisions)
- **approval-service** → parent approvals & overrides
- **telemetry-ingest** → device/wearable telemetry validation + ingestion
- **notification-service** → parent/kid/ops notifications
- **audit-service** → decision/event trace and evidence

---

# 🔁 FULL FLOW DIAGRAM (Beginning → End)  
## GitHub → CI/CD → Policy → Azure → Runtime → Audit → Monitoring  
### (Verification + Responsible AI embedded in every layer)

```
──────────────────────────────────────────────────────────────────────── 
Verified • Safe • Secure • Explainable • Accountable • Compliant 
Responsible AI enforced everywhere: 
Fairness • Reliability & Safety • Privacy & Security • Inclusiveness 
Transparency • Accountability 
─────────────────────────────────────────────────────────────────────────
👤 Developer 
     │ 
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
     🧠 RAI: Reliability & Safety (tests), Fairness (edge checks where applicable) 
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
```

---

## ✅ Verification Steps (README‑Friendly Summary)

**Every change must pass verification at ALL layers (not only CI):**

1) **Source Verification**  
   - PR required for main  
   - Required status checks pass  
   - Ownership traceable via commits

2) **Build Verification**  
   - Reproducible artifacts (build once, deploy many)  
   - Immutable tags (commit SHA)  
   - Dependency integrity enforced

3) **Test Verification**  
   - Unit + integration tests  
   - Lint + quality gates  
   - Safety checks for edge conditions

4) **Policy Verification (PDP)**  
   - Default deny if uncertain  
   - Structured decision required:
     - decision (ALLOW/DENY)
     - reason codes
     - obligations (e.g., REQUIRE_PARENT_APPROVAL)
     - policy version

5) **Approval Verification**  
   - Human oversight for high‑risk actions  
   - Environment protection for production releases

6) **Deployment Verification (PEP)**  
   - Enforce PDP result (no bypass)  
   - Least privilege identity  
   - Correct environment targeting

7) **Runtime Verification**  
   - Health/readiness checks  
   - Smoke tests  
   - Behavior consistency checks

8) **Audit Verification**  
   - Correlation ID across services  
   - Immutable audit trail  
   - Evidence stored for compliance

9) **Monitoring Verification**  
   - Alerts on anomalies and drift  
   - Incident response hooks  
   - Continuous improvement loop

---

# 🛡 Child Safety Guidelines (Safety‑First Defaults)

## Safety Defaults (Non‑Negotiable)
- **Default Deny:** uncertain/unknown → deny or require approval
- **Parent Authority:** sensitive actions require parent approval
- **Explainability Required:** no decision without reason codes and human explanation

## Prohibited System Behavior
- No autonomous high‑risk action without PDP + approval
- No silent decisions (must be logged)
- No fabricated explanations (explanations must map to reason codes)
- No leakage of sensitive child data (minimize + protect)

---

# 🧱 Guardrails (Agents + Policy System)

## Agent Guardrails
- Agents **propose**, never enforce
- Agents output **signals** only (riskScore, flags, context)
- PDP is the only component that can return final allow/deny decisions

## PDP Guardrails
- Deny by default on missing/invalid inputs
- Return structured decision + obligations + reason codes
- Include policy version and timestamp in every decision record

---

# ✅ Compliance Checklist (Audit‑Ready)

## Governance & Oversight
- [ ] Clear owner per service and per policy set
- [ ] PR review required for policy changes
- [ ] Human approval gate for high-risk actions and production deploys

## Security Controls
- [ ] Least privilege for CI/CD and runtime identities
- [ ] Secrets never committed to repo
- [ ] Dependency monitoring enabled
- [ ] Code scanning enabled
- [ ] Secret scanning + push protection enabled

## Privacy & Data Protection
- [ ] Minimize child data collection (only what is required)
- [ ] Encrypt in transit (TLS)
- [ ] Mask sensitive fields in logs
- [ ] Define retention policy for telemetry + audit

## Explainability & Transparency
- [ ] Reason codes mandatory
- [ ] Child-safe explanation and parent explanation supported
- [ ] Policy version included in audit log

## Reliability & Safety
- [ ] Health checks required
- [ ] Rollback plan in place
- [ ] Monitoring and alerting configured

## Evidence & Audit
- [ ] Immutable audit records
- [ ] Correlation IDs across services
- [ ] Deployment and decision events recorded

---

# 📦 "Everything GitHub Needs" (Repo Requirements Checklist)

GitHub‑complete repositories typically include: documentation, contribution, security, licensing, templates, and automation.

## Required Files
- [ ] README.md (this file)
- [ ] LICENSE
- [ ] CODE_OF_CONDUCT.md
- [ ] CONTRIBUTING.md
- [ ] SECURITY.md
- [ ] CHANGELOG.md

## GitHub Templates
- [ ] .github/PULL_REQUEST_TEMPLATE.md
- [ ] .github/ISSUE_TEMPLATE/bug_report.md
- [ ] .github/ISSUE_TEMPLATE/feature_request.md

## GitHub Actions
- [ ] .github/workflows/ci.yml
- [ ] .github/workflows/deploy.yml

## Repo Settings (Recommended)
- [ ] Protect main branch
- [ ] Require PR reviews
- [ ] Require status checks to pass before merge
- [ ] Enable Dependabot alerts
- [ ] Enable secret scanning + push protection
- [ ] Enable code scanning

---

# 📁 Compliance‑Ready Docs Structure (Recommended)

Recommended docs layout:
- `docs/00-governance/` — mission, principles, roles
- `docs/01-risk/` — threat model, risk register
- `docs/02-policy/` — PDP contract, reason codes, obligations
- `docs/03-architecture/` — diagrams, service mapping
- `docs/04-security/` — authn/authz, secrets handling
- `docs/05-safety/` — child safety, guardrails
- `docs/06-compliance/` — mappings to required frameworks
- `docs/07-verification/` — test strategy, runtime checks
- `docs/08-audit/` — audit schema, evidence
- `docs/09-agents/` — agent contracts + "agents propose, PDP decides"

---

## 🧩 Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md)

## 🛡 Security
See [SECURITY.md](SECURITY.md)

## 📜 License
See [LICENSE](LICENSE)
