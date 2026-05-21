# Layer 08: Audit & Traceability

**Layer Purpose**: Immutable audit trail and evidence collection

## Audit Philosophy

Every significant event in O.N.I.O.N is logged immutably for accountability and compliance.

## Audit Service Architecture

The Audit Service provides:
- **Immutable logging**: Events cannot be modified or deleted
- **Tamper-evidence**: Cryptographic integrity verification
- **Correlation**: Link related events across services
- **Retention**: Configurable retention per compliance requirements
- **Queryability**: Fast search and retrieval

## Audit Event Schema

### Standard Event Structure

```json
{
  "eventId": "evt-uuid",
  "correlationId": "corr-uuid",
  "timestamp": "2026-05-21T06:00:00.000Z",
  "eventType": "policy_decision",
  "layer": "L4",
  "service": "policy-pdp",
  "actor": {
    "type": "user | service | system",
    "id": "actor-identifier",
    "ip": "anonymized-ip",
    "userAgent": "client-info"
  },
  "action": "evaluate_policy",
  "resource": {
    "type": "policy | data | service",
    "id": "resource-identifier"
  },
  "outcome": "success | failure | conditional",
  "reasonCode": "REASON_CODE",
  "context": {
    "policyVersion": "1.0.0",
    "obligations": ["REQUIRE_APPROVAL"],
    "additionalData": {}
  },
  "integrity": {
    "hash": "sha256-hash",
    "previousHash": "sha256-of-previous",
    "signature": "cryptographic-signature"
  }
}
```

## Event Types

### L1 - Entry Events

- `workflow_triggered`
- `branch_protection_evaluated`
- `permission_checked`

### L2 - Build Events

- `build_started`
- `dependencies_installed`
- `artifact_created`
- `build_completed`

### L3 - Test Events

- `tests_started`
- `test_suite_completed`
- `coverage_calculated`
- `quality_gate_evaluated`

### L4 - Policy Events

**Most Critical for Accountability**

- `policy_decision`
- `pdp_evaluation_started`
- `agent_proposal_received`
- `policy_rule_evaluated`
- `reason_code_generated`
- `obligation_assigned`

Example:
```json
{
  "eventType": "policy_decision",
  "layer": "L4",
  "service": "policy-pdp",
  "action": "evaluate_policy",
  "outcome": "conditional",
  "reasonCode": "REQUIRES_PARENT_APPROVAL",
  "context": {
    "policyVersion": "1.0.0",
    "policiesEvaluated": ["SAFE-001", "SEC-002"],
    "agentProposals": [
      {"agent": "behavior-agent", "riskScore": 0.75},
      {"agent": "anomaly-agent", "flags": ["age_restriction"]}
    ],
    "obligations": ["REQUIRE_APPROVAL", "NOTIFY_PARENT"]
  }
}
```

### L5 - Approval Events

- `approval_requested`
- `approval_notification_sent`
- `approval_granted`
- `approval_denied`
- `approval_expired`

### L6 - Deployment Events

- `deployment_started`
- `container_deployed`
- `policy_enforced`
- `deployment_completed`
- `rollback_initiated`

### L7 - Runtime Events

- `health_check_performed`
- `smoke_test_executed`
- `anomaly_detected`
- `service_degradation`

### L8 - Audit Events (Meta)

- `audit_log_written`
- `audit_query_executed`
- `evidence_exported`

### L9 - Monitoring Events

- `alert_triggered`
- `incident_created`
- `metric_threshold_exceeded`

## Correlation IDs

### Purpose

Link related events across services and time for complete trace.

### Format

- **Correlation ID**: `corr-{timestamp}-{uuid}`
- **Event ID**: `evt-{uuid}`

### Usage

All events related to a request share a correlation ID:
```
corr-1234567890-abc123
  ├─ evt-001: API request received
  ├─ evt-002: Agent proposal (behavior)
  ├─ evt-003: Agent proposal (anomaly)
  ├─ evt-004: PDP decision
  ├─ evt-005: Approval requested
  ├─ evt-006: Notification sent
  ├─ evt-007: Approval granted
  └─ evt-008: Action executed
```

## Tamper-Evidence

### Cryptographic Chain

Each audit entry includes:
- Hash of current event
- Hash of previous event
- Digital signature

This creates an immutable chain where any modification breaks the integrity.

### Verification

```bash
# Verify audit log integrity
npm run audit:verify --from=2026-05-01 --to=2026-05-21
```

## Retention Policy

| Event Category | Retention Period | Reason |
|---------------|------------------|---------|
| Policy Decisions | 7 years | Compliance |
| Approvals | 7 years | Legal |
| Security Events | 5 years | Compliance |
| Access Logs | 3 years | Compliance |
| System Events | 1 year | Operational |
| Debug Logs | 30 days | Troubleshooting |

## Query Capabilities

### Query by Correlation ID

```javascript
const events = await audit.query({
  correlationId: 'corr-1234567890-abc123'
});
```

### Query by Event Type

```javascript
const decisions = await audit.query({
  eventType: 'policy_decision',
  fromDate: '2026-05-01',
  toDate: '2026-05-21'
});
```

### Query by Actor

```javascript
const userEvents = await audit.query({
  actor: {
    type: 'user',
    id: 'user-123'
  },
  limit: 100
});
```

### Query by Outcome

```javascript
const denials = await audit.query({
  eventType: 'policy_decision',
  outcome: 'deny',
  fromDate: '2026-05-20'
});
```

## Compliance Reports

### Monthly Compliance Report

- Total policy decisions
- Decision breakdown (allow/deny/conditional)
- Top reason codes
- Approval response times
- Safety incidents
- Security events

### Quarterly Audit Review

- Comprehensive event analysis
- Compliance violations
- Incident trends
- Recommendations

### Annual Compliance Certification

- Full audit trail export
- Evidence collection
- External audit support
- Certification documentation

## Evidence Export

```bash
# Export audit evidence for date range
npm run audit:export \
  --from=2026-01-01 \
  --to=2026-12-31 \
  --format=json \
  --output=/evidence/2026-annual.json
```

## Privacy Considerations

### PII Handling

- **User IDs**: Pseudonymized
- **IP Addresses**: Anonymized
- **Location**: City-level only
- **Content**: Not logged (only metadata)

### Access Control

- **Compliance Team**: Full read access
- **Security Team**: Security events only
- **Operations**: System events only
- **Developers**: Development environment only

## Monitoring Audit Health

### Metrics

- Audit write latency
- Audit write failures
- Storage utilization
- Query performance
- Integrity check status

### Alerts

- Audit write failure
- Integrity check failed
- Storage capacity warning
- Unusual query volume

## Responsible AI Integration

- **Transparency**: Complete audit trail
- **Accountability**: All actions tracked to actors
- **Fairness**: Objective evidence collection

## API Reference

See `services/audit-service/README.md` for API documentation.

## Document Control

- **Version**: 1.0.0
- **Last Updated**: 2026-05-21
- **Owner**: Audit Team
