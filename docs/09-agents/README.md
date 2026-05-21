# Layer 09: Agents

**Layer Purpose**: Agent architecture and contracts

## Agent Philosophy

**Agents Propose, PDP Decides**

Agents in O.N.I.O.N are **non-authoritative**:
- ✅ Analyze data
- ✅ Calculate scores
- ✅ Detect patterns
- ✅ Provide context
- ✅ Propose actions
- ❌ Never make final decisions
- ❌ Never enforce policies
- ❌ Never block requests directly

## Agent Contract

Every agent MUST:
1. Output proposals, not decisions
2. Include confidence scores
3. Provide reasoning/context
4. Never enforce actions
5. Log all proposals to audit

### Standard Agent Output

```json
{
  "agentId": "string",
  "agentVersion": "semver",
  "timestamp": "ISO 8601",
  "correlationId": "string",
  "proposal": {
    "type": "risk_assessment | anomaly_detection | context_enrichment | explanation",
    "confidence": 0.0 to 1.0,
    "data": {
      // Agent-specific data
    },
    "reasoning": "string",
    "suggestedAction": "string (optional)"
  }
}
```

## Agent Types

### 1. Assessment Agents

**Purpose**: Analyze and assign scores

**Examples**:
- Behavior Agent: Risk score calculation
- Sentiment Agent: Emotional tone analysis
- Quality Agent: Content quality scoring

**Output**:
```json
{
  "proposal": {
    "type": "risk_assessment",
    "score": 0.75,
    "confidence": 0.9,
    "factors": ["unusual_velocity", "new_location"],
    "reasoning": "Request rate 5x normal from new geographic location"
  }
}
```

### 2. Detection Agents

**Purpose**: Identify patterns and anomalies

**Examples**:
- Anomaly Agent: Safety violations
- Fraud Agent: Suspicious activity
- Intrusion Agent: Security threats

**Output**:
```json
{
  "proposal": {
    "type": "anomaly_detection",
    "anomalyType": "content_safety",
    "severity": "high",
    "confidence": 0.95,
    "flags": ["inappropriate_content"],
    "reasoning": "Content matches prohibited patterns"
  }
}
```

### 3. Enrichment Agents

**Purpose**: Add context and correlations

**Examples**:
- Context Agent: Historical data
- Relationship Agent: Connection mapping
- Environment Agent: Device/location context

**Output**:
```json
{
  "proposal": {
    "type": "context_enrichment",
    "userHistory": {
      "accountAge": "6 months",
      "trustScore": 0.85,
      "previousViolations": 0
    },
    "environmentContext": {
      "deviceType": "new",
      "location": "known_city"
    },
    "confidence": 0.8
  }
}
```

### 4. Explanation Agents

**Purpose**: Generate human-readable explanations

**Examples**:
- Explanation Agent: Multi-level explanations
- Translation Agent: Language conversion
- Simplification Agent: Reading level adaptation

**Output**:
```json
{
  "proposal": {
    "type": "explanation",
    "child": "We need to ask your parent first!",
    "parent": "Action requires parental approval per child safety policy.",
    "technical": "PDP decision: CONDITIONAL | Reason: AGE_RESTRICTION | Policy: v1.0.0"
  }
}
```

## Agent Safety Rules

### Rule 1: No Autonomous Actions

Agents MUST NOT:
- Block requests directly
- Modify data
- Send notifications
- Change configuration
- Execute commands

### Rule 2: Proposals Only

Agents MUST:
- Output proposals to be evaluated by PDP
- Include confidence scores
- Provide clear reasoning
- Suggest (not enforce) actions

### Rule 3: Fail Safe

On error, agents MUST:
- Log the error
- Return low-confidence proposal
- Not crash the system
- Allow PDP to apply default deny

### Rule 4: Privacy Respect

Agents MUST:
- Not log PII
- Anonymize data
- Minimize data collection
- Respect privacy policies

### Rule 5: Audit Everything

Agents MUST:
- Log all proposals
- Include correlation IDs
- Track confidence scores
- Record reasoning

## Agent Development

### Creating a New Agent

1. **Define Purpose**: What does this agent detect/analyze?
2. **Design Output**: What proposals will it make?
3. **Implement Logic**: Build detection/analysis logic
4. **Add Safety Checks**: Ensure no autonomous actions
5. **Write Tests**: Unit + integration + safety tests
6. **Document**: README with examples
7. **Register**: Add to agent registry

### Agent Template

```typescript
interface AgentProposal {
  agentId: string;
  agentVersion: string;
  timestamp: string;
  correlationId: string;
  proposal: {
    type: string;
    confidence: number;
    data: any;
    reasoning: string;
    suggestedAction?: string;
  };
}

class BaseAgent {
  async propose(input: any, correlationId: string): Promise<AgentProposal> {
    // 1. Validate input
    // 2. Perform analysis
    // 3. Calculate confidence
    // 4. Generate reasoning
    // 5. Return proposal (NOT decision)
    // 6. Log to audit
  }
}
```

## Agent Integration

### Agent → Telemetry → PDP Flow

```
1. Agent analyzes data
2. Agent generates proposal
3. Agent sends to Telemetry Ingest
4. Telemetry validates and routes
5. PDP receives proposals
6. PDP evaluates with policy
7. PDP makes decision
8. PEP enforces decision
```

### Multiple Agent Proposals

PDP can receive proposals from multiple agents:

```json
{
  "correlationId": "corr-123",
  "proposals": [
    {
      "agentId": "behavior-agent",
      "proposal": {"riskScore": 0.75, "confidence": 0.9}
    },
    {
      "agentId": "anomaly-agent",
      "proposal": {"flags": ["age_restriction"], "confidence": 0.95}
    },
    {
      "agentId": "context-agent",
      "proposal": {"trustScore": 0.85, "confidence": 0.8}
    }
  ]
}
```

PDP weighs all proposals and makes final decision.

## Agent Monitoring

### Metrics

- Proposal count
- Average confidence
- Processing latency
- Error rate
- Proposal acceptance rate (by PDP)

### Health Checks

- Agent responsiveness
- Data pipeline health
- Model performance (if ML-based)
- Resource utilization

### Alerts

- Agent unavailable
- Low confidence trend
- High error rate
- Processing delays

## Agent Testing

### Required Tests

1. **Unit Tests**: Core logic
2. **Integration Tests**: Data flow
3. **Safety Tests**: No autonomous actions
4. **Performance Tests**: Latency targets
5. **Edge Case Tests**: Unusual inputs
6. **Privacy Tests**: No PII logging

### Safety Test Example

```javascript
describe('Agent Safety Rules', () => {
  it('should not block requests directly', async () => {
    const agent = new BehaviorAgent();
    const result = await agent.propose(highRiskInput);
    
    // Agent should propose, not decide
    expect(result.proposal).toBeDefined();
    expect(result.proposal.type).toBe('risk_assessment');
    expect(result.proposal.confidence).toBeGreaterThan(0);
    
    // Agent should not have blocked anything
    expect(mockAPI.blockRequest).not.toHaveBeenCalled();
  });
});
```

## Existing Agents

See individual READMEs:
- `agents/behavior-agent/README.md`
- `agents/anomaly-agent/README.md`
- `agents/context-agent/README.md`
- `agents/explanation-agent/README.md`

## Responsible AI Integration

- **Fairness**: Agents must not introduce bias
- **Transparency**: Reasoning must be provided
- **Accountability**: All proposals logged
- **Reliability**: Confidence scores required

## Document Control

- **Version**: 1.0.0
- **Last Updated**: 2026-05-21
- **Owner**: Agent Team
