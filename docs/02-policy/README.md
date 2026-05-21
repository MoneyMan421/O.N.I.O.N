# 02 - Policy Framework

**O.N.I.O.N Layer:** L4 (Policy Decision Point)  
**Purpose:** PDP contracts, reason codes, obligations, and policy versioning

---

## 📋 Overview

This folder defines the Policy Decision Point (PDP) framework, including decision contracts, reason codes, obligations, and policy versioning strategy.

---

## 🎯 PDP Philosophy

**"Agents Propose, PDP Decides"**

The PDP is the authoritative decision-making component that:
- Evaluates requests against policies
- Returns structured decisions with reason codes
- Specifies obligations for enforcement
- Maintains policy version traceability

---

## 📜 Policy Decision Contract

### Request Format

```json
{
  "request_id": "uuid",
  "correlation_id": "workflow-id",
  "timestamp": "ISO-8601 timestamp",
  "subject": {
    "type": "user|system|service",
    "id": "identifier",
    "attributes": {
      "role": "string",
      "age_verified": "boolean"
    }
  },
  "action": {
    "type": "deploy|access|modify|execute",
    "resource": "resource identifier",
    "context": {
      "environment": "dev|staging|prod",
      "risk_level": "low|medium|high|critical"
    }
  },
  "resource": {
    "type": "data|service|content",
    "classification": "public|internal|confidential|restricted"
  }
}
```

### Response Format

```json
{
  "request_id": "uuid",
  "correlation_id": "workflow-id",
  "timestamp": "ISO-8601 timestamp",
  "decision": "allow|deny|conditional",
  "reason_codes": ["REASON_CODE_1", "REASON_CODE_2"],
  "reason_text": {
    "technical": "Detailed technical explanation",
    "user_friendly": "Simple explanation for users",
    "child_friendly": "Explanation appropriate for children"
  },
  "obligations": [
    {
      "type": "log|notify|approval|verify",
      "description": "What must be done",
      "deadline": "ISO-8601 timestamp or duration"
    }
  ],
  "policy": {
    "version": "1.0.0",
    "applicable_rules": ["rule-1", "rule-2"]
  },
  "metadata": {
    "confidence": 0.95,
    "processing_time_ms": 42
  }
}
```

---

## 🔢 Reason Codes

### Authorization Codes (1000-1999)

| Code | Name | Description |
|------|------|-------------|
| 1000 | AUTH_SUCCESS | Request authorized |
| 1001 | AUTH_INSUFFICIENT_PERMISSIONS | User lacks required permissions |
| 1002 | AUTH_EXPIRED_CREDENTIALS | Credentials expired |
| 1003 | AUTH_INVALID_TOKEN | Invalid authentication token |
| 1004 | AUTH_RATE_LIMITED | Too many requests |

### Safety Codes (2000-2999)

| Code | Name | Description |
|------|------|-------------|
| 2000 | SAFETY_APPROVED | Safety checks passed |
| 2001 | SAFETY_CHILD_PROTECTION | Child protection rule triggered |
| 2002 | SAFETY_CONTENT_FLAGGED | Content flagged for review |
| 2003 | SAFETY_PARENT_APPROVAL_REQUIRED | Parent approval needed |
| 2004 | SAFETY_AGE_INAPPROPRIATE | Content not age-appropriate |

### Security Codes (3000-3999)

| Code | Name | Description |
|------|------|-------------|
| 3000 | SECURITY_APPROVED | Security checks passed |
| 3001 | SECURITY_VULNERABILITY_DETECTED | Known vulnerability found |
| 3002 | SECURITY_UNTRUSTED_SOURCE | Source not trusted |
| 3003 | SECURITY_ENCRYPTION_REQUIRED | Encryption required but missing |
| 3004 | SECURITY_SECRETS_EXPOSED | Secrets detected in request |

### Compliance Codes (4000-4999)

| Code | Name | Description |
|------|------|-------------|
| 4000 | COMPLIANCE_APPROVED | Compliance checks passed |
| 4001 | COMPLIANCE_GDPR_VIOLATION | GDPR compliance issue |
| 4002 | COMPLIANCE_COPPA_VIOLATION | COPPA compliance issue |
| 4003 | COMPLIANCE_DATA_RETENTION | Data retention policy violation |
| 4004 | COMPLIANCE_AUDIT_REQUIRED | Audit evidence required |

### Deployment Codes (5000-5999)

| Code | Name | Description |
|------|------|-------------|
| 5000 | DEPLOY_APPROVED | Deployment authorized |
| 5001 | DEPLOY_TESTS_FAILED | Required tests failed |
| 5002 | DEPLOY_APPROVAL_PENDING | Human approval required |
| 5003 | DEPLOY_ENVIRONMENT_MISMATCH | Wrong environment for deployment |
| 5004 | DEPLOY_CHANGE_WINDOW_VIOLATION | Outside approved change window |

---

## ⚖️ Policy Rules

### Default Policies

#### 1. Default Deny
```yaml
name: default-deny
version: 1.0.0
description: Deny requests when policy cannot be evaluated
rule: |
  IF policy_evaluation_fails OR insufficient_information THEN
    decision = DENY
    reason_code = POLICY_EVALUATION_ERROR
```

#### 2. Child Safety First
```yaml
name: child-safety-first
version: 1.0.0
description: Protect children by default
rule: |
  IF user.age < 18 AND action.risk_level >= medium THEN
    decision = CONDITIONAL
    reason_code = SAFETY_PARENT_APPROVAL_REQUIRED
    obligation = REQUIRE_PARENT_APPROVAL
```

#### 3. Production Deployment Protection
```yaml
name: production-protection
version: 1.0.0
description: Require approval for production deployments
rule: |
  IF environment = production AND action = deploy THEN
    decision = CONDITIONAL
    reason_code = DEPLOY_APPROVAL_PENDING
    obligation = REQUIRE_HUMAN_APPROVAL
```

#### 4. Security Vulnerability Block
```yaml
name: security-vulnerability-block
version: 1.0.0
description: Block deployment with known vulnerabilities
rule: |
  IF security_scan.critical_vulnerabilities > 0 THEN
    decision = DENY
    reason_code = SECURITY_VULNERABILITY_DETECTED
```

---

## 📋 Obligations

### Obligation Types

1. **LOG** — Must be logged for audit trail
2. **NOTIFY** — Must notify stakeholders
3. **APPROVAL** — Requires human approval
4. **VERIFY** — Must verify after action
5. **MONITOR** — Must monitor for specific duration
6. **ENCRYPT** — Must encrypt data
7. **SANITIZE** — Must sanitize input
8. **REPORT** — Must generate report

### Example Obligations

```json
{
  "obligations": [
    {
      "type": "log",
      "description": "Log decision to audit trail with correlation ID",
      "deadline": "immediate"
    },
    {
      "type": "approval",
      "description": "Obtain parent approval for action",
      "deadline": "PT24H"
    },
    {
      "type": "monitor",
      "description": "Monitor service health for 1 hour post-deployment",
      "deadline": "PT1H"
    }
  ]
}
```

---

## 📦 Policy Versioning

### Version Format
`MAJOR.MINOR.PATCH`

- **MAJOR:** Breaking changes in policy logic
- **MINOR:** New policies or reason codes
- **PATCH:** Bug fixes or clarifications

### Version Tracking
All policy decisions must include the policy version used:
```json
{
  "policy": {
    "version": "1.2.3",
    "applicable_rules": ["default-deny", "child-safety-first"]
  }
}
```

---

## 🔄 Policy Lifecycle

1. **Draft** — Policy being developed
2. **Review** — Under review by stakeholders
3. **Approved** — Approved for implementation
4. **Active** — Currently enforced
5. **Deprecated** — Scheduled for removal
6. **Retired** — No longer in use

---

## 📚 Related Documentation

- [Governance](../00-governance/) — Policy approval process
- [Risk Management](../01-risk/) — Risk-based policies
- [Security](../04-security/) — Security policies
- [Safety](../05-safety/) — Child safety policies
- [Compliance](../06-compliance/) — Regulatory compliance
- [Audit](../08-audit/) — Policy audit logging

---

## 📝 Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-05-21 | Initial | Initial policy framework |

---

**🧅 Policies decide. Reason codes explain. Obligations enforce. Every decision accountable.**
