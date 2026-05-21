# Policy Decision Point (PDP)

**Layer**: L4 - Policy (Decision Engine)

## Purpose

The PDP is the centralized decision-making service for all policy evaluations in O.N.I.O.N. It:
- Evaluates policy rules against requests
- Generates structured decisions (allow/deny/conditional)
- Provides reason codes for transparency
- Defines obligations for enforcement

## Architecture Role

- **Decides** policy outcomes (does not enforce)
- **Centralizes** all policy logic
- **Generates** explainable decisions
- **Versions** policy rules for auditability

## Decision Contract

Every PDP decision includes:
- `decision`: "allow" | "deny" | "conditional"
- `reasonCode`: Explanation code (e.g., "ALL_POLICIES_SATISFIED")
- `obligations`: Actions required (e.g., "REQUIRE_PARENT_APPROVAL")
- `policyVersion`: Version of policy evaluated
- `correlationId`: For audit trail

## Policy Types

1. **Security Policies**: Authentication, authorization, secrets
2. **Compliance Policies**: Required documentation, standards
3. **Safety Policies**: Child safety, content filtering, age-appropriate
4. **Operational Policies**: Rate limits, quotas, maintenance windows

## Example Decision

```json
{
  "decision": "conditional",
  "reasonCode": "REQUIRES_PARENT_APPROVAL",
  "obligations": ["REQUIRE_APPROVAL"],
  "policyVersion": "1.0.0",
  "correlationId": "pdp-1234567890",
  "timestamp": "2026-05-21T06:00:00Z"
}
```

## Key Principles

1. **Agents Propose, PDP Decides**: Agents provide signals, PDP makes final call
2. **Explainability Required**: Every decision must have a reason code
3. **Immutable Audit**: All decisions logged permanently
4. **Version Control**: Policy changes are tracked

## Development

```bash
cd services/policy-pdp
npm install
npm run dev
```

## Testing

```bash
npm test
npm run test:policy-rules
```

## Responsible AI Integration

- **Fairness**: Consistent policy application across all users
- **Transparency**: Explicit reason codes for all decisions
- **Accountability**: Decisions tracked with full context
