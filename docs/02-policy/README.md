# Layer 02: Policy (PDP Contract)

**Layer Purpose**: Centralized policy decisions with explainability

## Policy Decision Point (PDP)

The PDP is the single source of truth for all policy decisions in O.N.I.O.N.

### Core Principle

**Agents Propose, PDP Decides**

- Agents analyze and propose
- PDP evaluates policies and decides
- PEP enforces decisions
- Audit logs everything

## PDP Decision Contract

Every PDP decision MUST include:

```json
{
  "decision": "allow" | "deny" | "conditional",
  "reasonCode": "string",
  "obligations": ["string"],
  "policyVersion": "semver",
  "correlationId": "string",
  "timestamp": "ISO 8601",
  "context": {...}
}
```

### Decision Types

1. **allow**: Action permitted, proceed
2. **deny**: Action blocked, do not proceed
3. **conditional**: Action requires additional steps (e.g., approval)

### Reason Codes

Every decision MUST have a reason code for transparency.

#### Common Reason Codes

- `ALL_POLICIES_SATISFIED`: All checks passed
- `MISSING_REQUIRED_DOCS`: Documentation missing
- `HARDCODED_SECRETS`: Secrets detected in code
- `AGE_RESTRICTION`: User age below minimum
- `REQUIRES_PARENT_APPROVAL`: Parent oversight needed
- `CONTENT_VIOLATION`: Safety policy violated
- `UNKNOWN_ACTION`: Action not recognized (default deny)
- `SECURITY_VIOLATION`: Security policy violated
- `COMPLIANCE_VIOLATION`: Compliance requirement not met

#### Adding New Reason Codes

1. Document in `configs/policy-config.yaml`
2. Add explanation templates for child/parent
3. Update audit schema
4. Version the policy

### Obligations

Actions required before or after a decision:

- `REQUIRE_APPROVAL`: Human approval needed
- `LOG_TO_AUDIT`: Must log to audit service
- `NOTIFY_PARENT`: Parent notification required
- `VERIFY_AGE`: Age verification needed
- `FIX_VIOLATIONS`: Code must be corrected
- `ADDITIONAL_REVIEW`: Extra review required

## Policy Types

### 1. Security Policies

- Authentication requirements
- Authorization rules
- Secrets management
- Vulnerability thresholds

### 2. Child Safety Policies

- Age restrictions
- Content filtering
- Predatory behavior detection
- Default deny rules

### 3. Compliance Policies

- Required documentation
- Audit logging
- Data retention
- Regulatory requirements

### 4. Operational Policies

- Rate limiting
- Quota management
- Maintenance windows
- Deployment approval

## Policy Evaluation Process

1. **Receive Request**: From PEP with context
2. **Gather Signals**: From agents (proposals only)
3. **Evaluate Policies**: Apply policy rules
4. **Generate Decision**: With reason code and obligations
5. **Log Decision**: To audit service
6. **Return Decision**: To PEP for enforcement

## Policy Versioning

- Policies are versioned using semantic versioning
- All decisions include policy version
- Audit logs track policy version used
- Changes require approval and testing

## Integration Points

### Input: Agent Proposals

```json
{
  "agentId": "behavior-agent",
  "proposal": {
    "riskScore": 0.75,
    "confidence": 0.9,
    "flags": ["unusual_pattern"],
    "context": {...},
    "suggestedAction": "require_verification"
  }
}
```

### Output: PDP Decision

```json
{
  "decision": "conditional",
  "reasonCode": "REQUIRES_PARENT_APPROVAL",
  "obligations": ["REQUIRE_APPROVAL", "NOTIFY_PARENT"],
  "policyVersion": "1.0.0",
  "correlationId": "pdp-1234567890"
}
```

## Testing Policy Decisions

```bash
npm run test:policy-rules
npm run test:reason-codes
npm run test:edge-cases
```

## Responsible AI Integration

- **Fairness**: Consistent policy application
- **Transparency**: Reason codes for all decisions
- **Accountability**: All decisions logged with context
- **Explainability**: Decisions explainable at multiple levels

## Document Control

- **Version**: 1.0.0
- **Last Updated**: 2026-05-21
- **Owner**: Policy Team
