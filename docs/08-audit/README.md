# 08 - Audit & Traceability

**O.N.I.O.N Layer:** L8 (Audit)  
**Purpose:** Audit logging, evidence collection, and accountability

---

## 📋 Overview

This folder documents the audit logging strategy, evidence collection methods, and accountability mechanisms for the O.N.I.O.N system.

---

## 🎯 Audit Philosophy

**Everything Logged. Everything Traceable. Everything Accountable.**

Every decision, action, and event must:
- Be logged with sufficient detail
- Include correlation IDs for traceability
- Contain reason codes for explainability
- Be tamper-evident
- Be retained per compliance requirements

---

## 📝 Audit Log Schema

### Standard Log Entry

```json
{
  "event_id": "uuid",
  "correlation_id": "workflow-123-456",
  "timestamp": "2026-05-21T05:00:00.000Z",
  "event_type": "policy_decision|access_attempt|deployment|config_change",
  "severity": "info|warning|error|critical",
  "layer": "L1|L2|L3|L4|L5|L6|L7|L8|L9",
  "actor": {
    "type": "user|service|system",
    "id": "identifier",
    "ip_address": "IP (if applicable)",
    "user_agent": "string (if applicable)"
  },
  "action": {
    "type": "create|read|update|delete|execute|approve|deny",
    "resource": "resource identifier",
    "result": "success|failure|conditional"
  },
  "context": {
    "environment": "dev|staging|prod",
    "session_id": "session identifier",
    "request_id": "request identifier"
  },
  "decision": {
    "decision": "allow|deny|conditional",
    "reason_codes": ["CODE_1", "CODE_2"],
    "policy_version": "1.0.0",
    "confidence": 0.95
  },
  "metadata": {
    "git_sha": "commit hash (if applicable)",
    "build_id": "build identifier",
    "deployment_id": "deployment identifier"
  }
}
```

---

## 🔍 What We Audit

### L1 - Entry/Trigger Events
**Events:**
- Code commits
- Pull request creation/merge
- Workflow triggers
- Branch protection violations

**Evidence:**
```json
{
  "event_type": "source_commit",
  "actor": { "type": "user", "id": "developer@example.com" },
  "action": { "type": "create", "resource": "commit/abc123" },
  "metadata": {
    "git_sha": "abc123...",
    "branch": "feature/new-feature",
    "commit_message": "Add feature X"
  }
}
```

---

### L2 - Build Events
**Events:**
- Build started/completed
- Dependency installation
- Artifact creation
- Build failures

**Evidence:**
```json
{
  "event_type": "build_complete",
  "action": { "type": "execute", "resource": "build/123", "result": "success" },
  "metadata": {
    "git_sha": "abc123...",
    "build_id": "build-123",
    "artifacts": ["image:sha256:def456..."],
    "duration_ms": 120000
  }
}
```

---

### L3 - Test Events
**Events:**
- Test execution
- Test results
- Security scan results
- Code quality checks

**Evidence:**
```json
{
  "event_type": "test_execution",
  "action": { "type": "execute", "resource": "test_suite", "result": "success" },
  "metadata": {
    "test_count": 245,
    "passed": 245,
    "failed": 0,
    "coverage": 84.5,
    "duration_ms": 45000
  }
}
```

---

### L4 - Policy Decision Events
**Events:**
- Policy evaluation requests
- Policy decisions
- Reason code generation
- Obligations issued

**Evidence:**
```json
{
  "event_type": "policy_decision",
  "actor": { "type": "system", "id": "pdp" },
  "action": { "type": "evaluate", "resource": "deployment_request" },
  "decision": {
    "decision": "conditional",
    "reason_codes": ["DEPLOY_APPROVAL_PENDING"],
    "policy_version": "1.0.0",
    "obligations": [
      { "type": "approval", "description": "Require human approval" }
    ]
  }
}
```

---

### L5 - Approval Events
**Events:**
- Approval requests
- Approval granted/denied
- Approval timeouts

**Evidence:**
```json
{
  "event_type": "approval_granted",
  "actor": { "type": "user", "id": "approver@example.com" },
  "action": { "type": "approve", "resource": "deployment/prod/123" },
  "context": {
    "approval_reason": "Approved after review",
    "approval_timestamp": "2026-05-21T06:00:00Z"
  }
}
```

---

### L6 - Deployment Events
**Events:**
- Deployment started/completed
- Configuration changes
- Secret access
- Runtime policy enforcement

**Evidence:**
```json
{
  "event_type": "deployment_complete",
  "action": { "type": "execute", "resource": "deployment/prod/123", "result": "success" },
  "metadata": {
    "environment": "production",
    "git_sha": "abc123...",
    "image": "myregistry.azurecr.io/onion:abc123",
    "deployment_id": "deploy-123"
  }
}
```

---

### L7 - Runtime Events
**Events:**
- Service start/stop
- Health check results
- Runtime errors
- Performance anomalies

**Evidence:**
```json
{
  "event_type": "runtime_error",
  "severity": "error",
  "action": { "type": "execute", "resource": "api/endpoint", "result": "failure" },
  "context": {
    "error_message": "Database connection timeout",
    "stack_trace": "...",
    "affected_users": 0
  }
}
```

---

### L8 - Audit Events
**Events:**
- Audit log access
- Audit log export
- Log retention policy enforcement

**Evidence:**
```json
{
  "event_type": "audit_log_access",
  "actor": { "type": "user", "id": "auditor@example.com" },
  "action": { "type": "read", "resource": "audit_logs/2026-05" },
  "context": {
    "access_reason": "Compliance audit",
    "records_accessed": 15420
  }
}
```

---

### L9 - Monitoring Events
**Events:**
- Alerts triggered
- Anomalies detected
- Incident creation
- Remediation actions

**Evidence:**
```json
{
  "event_type": "alert_triggered",
  "severity": "critical",
  "action": { "type": "alert", "resource": "service/api", "result": "triggered" },
  "context": {
    "alert_name": "High Error Rate",
    "metric_value": 5.2,
    "threshold": 1.0,
    "affected_service": "api"
  }
}
```

---

## 🔗 Correlation & Traceability

### Correlation IDs
Every request/workflow gets a correlation ID:
```
{workflow_id}-{run_number}
Example: commit-abc123-run-456
```

### Trace Example
```
Correlation ID: deploy-prod-20260521-001

L1: source_commit → abc123
L2: build_started → build-456
L2: build_complete → build-456 (SUCCESS)
L3: test_started → test-789
L3: test_complete → test-789 (PASSED)
L4: policy_decision → CONDITIONAL (APPROVAL_REQUIRED)
L5: approval_request → approval-012
L5: approval_granted → approval-012 (APPROVED)
L6: deployment_started → deploy-345
L6: deployment_complete → deploy-345 (SUCCESS)
L7: health_check → deploy-345 (HEALTHY)
L8: audit_log_written → events: 12
L9: monitoring_active → deploy-345
```

---

## 🔒 Audit Log Security

### Protection Measures
1. **Immutability:** Write-once, cannot be modified
2. **Integrity:** Cryptographic hashes for tamper detection
3. **Encryption:** Encrypted at rest (AES-256)
4. **Access Control:** Strict RBAC, auditor-only access
5. **Retention:** Automated retention per compliance requirements

### Access Logging
All audit log access is itself logged:
- Who accessed
- What was accessed
- When it was accessed
- Why (reason code)

---

## 📊 Audit Reports

### Standard Reports

#### 1. Compliance Report
**Frequency:** Monthly  
**Contains:**
- Policy decision summary
- Approval gate usage
- Security event summary
- Data access summary

#### 2. Security Report
**Frequency:** Weekly  
**Contains:**
- Security events
- Failed authentication attempts
- Vulnerability scan results
- Incident summary

#### 3. Safety Report
**Frequency:** Daily (if safety incidents)  
**Contains:**
- Safety incidents
- Content moderation actions
- Parent approval requests
- Child protection events

---

## 📋 Retention Policy

### Retention Periods

| Log Type | Retention Period | Reason |
|----------|-----------------|--------|
| Policy Decisions | 7 years | Compliance (SOC 2, GDPR) |
| Security Events | 3 years | Security investigation |
| Access Logs | 1 year | Security monitoring |
| Application Logs | 90 days | Debugging |
| Performance Logs | 30 days | Performance analysis |

### Retention Enforcement
- Automated deletion after retention period
- Legal hold capability (freezes deletion)
- Archival to cold storage after 1 year

---

## ✅ Audit Readiness Checklist

### Implementation
- [ ] All layers logging to centralized system
- [ ] Correlation IDs in all logs
- [ ] Reason codes in policy decisions
- [ ] Tamper-evident logging enabled
- [ ] Log encryption enabled
- [ ] Access controls configured

### Compliance
- [ ] Retention policies configured
- [ ] Audit reports automated
- [ ] Log export capability tested
- [ ] Access logging enabled
- [ ] Legal hold process documented

### Operational
- [ ] Log monitoring active
- [ ] Alert rules configured
- [ ] On-call escalation defined
- [ ] Incident response playbooks ready

---

## 📚 Related Documentation

- [Governance](../00-governance/) — Audit governance
- [Policy](../02-policy/) — Policy decisions to audit
- [Security](../04-security/) — Security event logging
- [Compliance](../06-compliance/) — Compliance requirements

---

## 📝 Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-05-21 | Initial | Initial audit documentation |

---

**🧅 Everything logged. Everything traceable. Every decision explained. Accountability guaranteed.**
