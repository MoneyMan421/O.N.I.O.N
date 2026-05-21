# 03 - Architecture

**O.N.I.O.N Layers:** All (L1-L9)  
**Purpose:** System design, architecture diagrams, and service mapping

---

## 📋 Overview

This folder contains architectural documentation for the O.N.I.O.N system, including diagrams, service descriptions, and integration patterns.

---

## 🏗️ System Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     GitHub (Source)                          │
│  - Repository                                                │
│  - Branch Protection                                         │
│  - Required Reviews                                          │
└──────────────────────┬──────────────────────────────────────┘
                       │ L1: Trigger
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              GitHub Actions (CI/CD Pipeline)                 │
│  L2: Build  → L3: Test → L4: Policy → L5: Approval         │
└──────────────────────┬──────────────────────────────────────┘
                       │ L6: Deploy
                       ▼
┌─────────────────────────────────────────────────────────────┐
│          Azure / Kubernetes (Runtime Environment)            │
│  - Container Apps / AKS                                      │
│  - Policy Enforcement Point (PEP)                            │
│  - Network Policies                                          │
└──────────────────────┬──────────────────────────────────────┘
                       │ L7: Runtime Verification
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              Monitoring & Logging                            │
│  - Application Insights                                      │
│  - Log Analytics                                             │
│  - Azure Monitor                                             │
│  L8: Audit  →  L9: Monitor & Feedback                       │
└─────────────────────────────────────────────────────────────┘
```

---

## 🧅 Layer-by-Layer Architecture

### L1 - Entry/Trigger
**Components:**
- GitHub repository with branch protection
- Webhook triggers for GitHub Actions
- Protected branch policies

**Security Controls:**
- Required code reviews
- Status check requirements
- Push protection for secrets

### L2 - Build
**Components:**
- Build environment (GitHub Actions runners)
- Dependency management
- Container image registry

**Artifacts:**
- Container images (tagged by SHA)
- Build manifests
- SBOMs (Software Bill of Materials)

### L3 - Test
**Components:**
- Test frameworks
- Linters and formatters
- Security scanners (SAST/DAST)

**Outputs:**
- Test results
- Code coverage reports
- Security scan results

### L4 - Policy Decision Point (PDP)
**Components:**
- Policy evaluation engine
- Reason code generator
- Compliance checker

**Inputs:**
- Test results
- Security scan results
- Deployment request context

**Outputs:**
- Decision (Allow/Deny/Conditional)
- Reason codes
- Obligations

### L5 - Control/Approval
**Components:**
- GitHub environment protection rules
- Approval workflow
- Notification system

**Controls:**
- Required approvals by environment
- Approval timeout
- Approval reviewers

### L6 - Deploy
**Components:**
- Deployment orchestrator
- Container registry
- Target environment (Azure/K8s)
- Policy Enforcement Point (PEP)

**Configurations:**
- Environment variables
- Secrets (from Azure Key Vault)
- Network policies
- Ingress rules

### L7 - Runtime Verification
**Components:**
- Health check endpoints
- Readiness probes
- Liveness probes
- Smoke test suite

**Checks:**
- Service health
- Dependency availability
- Policy enforcement active
- Performance baselines

### L8 - Audit
**Components:**
- Logging infrastructure
- Audit log storage
- Correlation ID tracking
- Evidence collection

**Data Collected:**
- All policy decisions
- Deployment events
- Access logs
- Configuration changes

### L9 - Monitor & Feedback
**Components:**
- Metrics collection (Prometheus/Azure Monitor)
- Alerting system
- Anomaly detection
- Feedback loop processor

**Monitors:**
- Application performance
- Error rates
- Security events
- Policy violations

---

## 🔄 Data Flow

### Deployment Flow
1. Developer commits code to feature branch
2. PR created → L1 triggers CI workflow
3. L2 builds artifact with SHA-tagged image
4. L3 runs tests and security scans
5. L4 PDP evaluates results and returns decision
6. L5 (if required) waits for human approval
7. L6 deploys to target environment with PEP enforcement
8. L7 verifies deployment health and readiness
9. L8 logs all decisions and events with correlation ID
10. L9 monitors runtime behavior and feeds back to policies

### Request Flow (Runtime)
1. User/client makes request to service
2. PEP intercepts request
3. PDP evaluates request against policies
4. Decision returned (Allow/Deny/Conditional)
5. If Allow: Request processed, response returned
6. If Deny: Error response with reason code
7. All decisions logged to L8
8. Metrics sent to L9 for monitoring

---

## 🔌 Integration Points

### External Systems
- **GitHub:** Source control and CI/CD
- **Azure:** Cloud hosting and services
- **Container Registry:** Docker images (Azure CR, GitHub CR)
- **Key Vault:** Secrets management
- **Application Insights:** Monitoring and logging
- **Identity Provider:** Authentication (Azure AD, Auth0, etc.)

### Internal Components
- **PDP Service:** Policy decisions
- **PEP Service:** Policy enforcement
- **Audit Service:** Logging and evidence
- **Monitoring Service:** Metrics and alerts

---

## 🛡️ Security Architecture

### Defense in Depth

```
┌─────────────────────────────────────────┐
│  L1: Source Verification                 │  ← Branch protection, code review
├─────────────────────────────────────────┤
│  L2: Build Integrity                     │  ← Reproducible builds, SBOM
├─────────────────────────────────────────┤
│  L3: Quality & Security Testing          │  ← SAST, DAST, dependency scan
├─────────────────────────────────────────┤
│  L4: Policy Evaluation                   │  ← PDP decisions, reason codes
├─────────────────────────────────────────┤
│  L5: Human Oversight                     │  ← Approval gates
├─────────────────────────────────────────┤
│  L6: Runtime Enforcement                 │  ← PEP, network policies
├─────────────────────────────────────────┤
│  L7: Runtime Verification                │  ← Health checks, smoke tests
├─────────────────────────────────────────┤
│  L8: Audit & Accountability              │  ← Comprehensive logging
├─────────────────────────────────────────┤
│  L9: Continuous Monitoring               │  ← Anomaly detection, alerts
└─────────────────────────────────────────┘
```

---

## 📊 Scalability & Performance

### Horizontal Scaling
- Container orchestration via Kubernetes
- Auto-scaling based on metrics
- Load balancing across instances

### Performance Targets
- **API Response Time:** < 200ms (p95)
- **Build Time:** < 5 minutes
- **Deployment Time:** < 10 minutes
- **Health Check Response:** < 100ms

---

## 🔄 Disaster Recovery

### Backup Strategy
- Source code: GitHub (automatically backed up)
- Configuration: Infrastructure as Code (version controlled)
- Data: Regular backups to Azure Backup
- Logs: Long-term storage in Azure Storage

### Recovery Time Objectives (RTO)
- **Critical Services:** < 1 hour
- **Standard Services:** < 4 hours
- **Non-Critical Services:** < 24 hours

### Recovery Point Objectives (RPO)
- **User Data:** < 15 minutes
- **Configuration:** No data loss (IaC)
- **Audit Logs:** No data loss (redundant storage)

---

## 📚 Related Documentation

- [Security Controls](../04-security/) — Security implementation details
- [Verification](../07-verification/) — Testing and verification
- [Audit](../08-audit/) — Audit logging architecture
- [Agents](../09-agents/) — Agent architecture

---

## 📝 Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-05-21 | Initial | Initial architecture documentation |

---

**🧅 Architecture verified at every layer. Design documented. Integration mapped.**
