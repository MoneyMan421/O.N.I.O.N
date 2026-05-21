# Behavior Agent - Risk Pattern Detection

**Type**: Agent (Non-Authoritative)

## Purpose

The Behavior Agent analyzes patterns and proposes risk assessments. It:
- Detects unusual behavior patterns
- Calculates risk scores
- Proposes flags and context
- **Does NOT make decisions** (PDP decides)

## Agent Contract

### Outputs (Proposals Only)
```json
{
  "agentId": "behavior-agent",
  "timestamp": "2026-05-21T06:00:00Z",
  "correlationId": "signal-1234567890",
  "proposal": {
    "riskScore": 0.75,
    "confidence": 0.9,
    "flags": ["unusual_pattern", "high_velocity"],
    "context": {
      "patterns": ["rapid_requests", "geographic_anomaly"],
      "reasoning": "User made 100 requests in 5 seconds from new location"
    },
    "suggestedAction": "require_additional_verification"
  }
}
```

### Key Principle
**Agents Propose, PDP Decides**

The agent:
- ✅ Analyzes data
- ✅ Calculates scores
- ✅ Provides context
- ✅ Suggests actions
- ❌ Never makes final decisions
- ❌ Never enforces policies
- ❌ Never blocks requests

## Detection Patterns

1. **Velocity Anomalies**: Unusual request rates
2. **Geographic Anomalies**: Unexpected locations
3. **Temporal Anomalies**: Unusual timing patterns
4. **Content Anomalies**: Suspicious content patterns

## Responsible AI Integration

- **Fairness**: No bias in pattern detection
- **Transparency**: Reasoning included in proposals
- **Reliability**: Confidence scores provided
- **Accountability**: All proposals logged

## Development

```bash
cd agents/behavior-agent
npm install
npm run dev
```

## Testing

```bash
npm test
npm run test:patterns
```
