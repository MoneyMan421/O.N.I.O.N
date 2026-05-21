# Context Agent - Signal Enrichment

**Type**: Agent (Non-Authoritative)

## Purpose

The Context Agent enriches signals with additional context. It:
- Adds historical context to signals
- Correlates related events
- Provides user behavior history
- **Does NOT make decisions** (PDP decides)

## Agent Contract

### Outputs (Proposals Only)
```json
{
  "agentId": "context-agent",
  "timestamp": "2026-05-21T06:00:00Z",
  "correlationId": "signal-1234567890",
  "enrichment": {
    "userHistory": {
      "accountAge": "6 months",
      "previousViolations": 0,
      "trustScore": 0.85,
      "typicalBehavior": "low_activity"
    },
    "relatedEvents": [
      {"eventId": "evt-123", "type": "similar_request", "timestamp": "..."}
    ],
    "environmentalContext": {
      "timeOfDay": "unusual",
      "deviceType": "new",
      "location": "known"
    },
    "suggestedConsiderations": [
      "First time from this device",
      "Request during unusual hours"
    ]
  }
}
```

## Enrichment Types

1. **User Context**: History, trust score, patterns
2. **Temporal Context**: Time patterns, frequency
3. **Device Context**: Device fingerprinting, location
4. **Behavioral Context**: Typical vs current behavior

## Key Principle
**Context Without Judgment**

The agent provides:
- ✅ Historical data
- ✅ Correlations
- ✅ Environmental factors
- ✅ Patterns
- ❌ No risk scores
- ❌ No decisions
- ❌ No policy enforcement

## Privacy Considerations

- PII is anonymized
- Data retention follows policy
- User consent respected
- Minimal data collection

## Responsible AI Integration

- **Privacy**: Minimal necessary data only
- **Transparency**: Clear data sources
- **Fairness**: Unbiased context provision
- **Accountability**: Data usage tracked

## Development

```bash
cd agents/context-agent
npm install
npm run dev
```
