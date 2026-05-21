# Audit Service - Immutable Logging

**Layer**: L8 - Audit (Evidence & Traceability)

## Purpose

The Audit Service provides immutable, tamper-evident logging for O.N.I.O.N. It:
- Logs all decisions and actions
- Provides correlation ID tracking
- Enables compliance reporting
- Supports forensic investigation

## Architecture Role

- **Records** all significant events
- **Ensures** immutability
- **Provides** audit trail
- **Enables** compliance reports

## Event Types

1. **Policy Decisions**: PDP evaluations with full context
2. **Approvals**: Parent/guardian approval events
3. **Access Events**: Authentication, authorization
4. **System Events**: Deployments, configuration changes
5. **Agent Signals**: Risk assessments, anomalies

## Audit Log Schema

```json
{
  "eventId": "evt-1234567890",
  "correlationId": "corr-1234567890",
  "timestamp": "2026-05-21T06:00:00Z",
  "eventType": "policy_decision",
  "actor": "user@example.com",
  "action": "evaluate_policy",
  "outcome": "allow",
  "reasonCode": "ALL_POLICIES_SATISFIED",
  "context": {...},
  "policyVersion": "1.0.0"
}
```

## Key Principles

1. **Immutability**: Logs cannot be modified
2. **Tamper-Evidence**: Cryptographic integrity
3. **Correlation**: All related events linked
4. **Retention**: Logs retained per compliance requirements

## Query Capabilities

- Search by correlation ID
- Filter by event type
- Time-range queries
- Actor-based queries
- Compliance reports

## API Endpoints

- `POST /audit/log` - Log an event
- `GET /audit/query` - Query audit logs
- `GET /audit/correlation/:id` - Get correlated events
- `GET /audit/compliance-report` - Generate compliance report

## Development

```bash
cd services/audit-service
npm install
npm run dev
```

## Responsible AI Integration

- **Transparency**: Complete audit trail
- **Accountability**: All actions tracked to actors
- **Compliance**: Meets regulatory requirements
