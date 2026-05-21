# Anomaly Agent - Safety Detection

**Type**: Agent (Non-Authoritative)

## Purpose

The Anomaly Agent detects safety-related anomalies and proposes protective actions. It:
- Monitors for safety violations
- Detects content policy violations
- Identifies age-inappropriate content
- **Does NOT make decisions** (PDP decides)

## Agent Contract

### Outputs (Proposals Only)
```json
{
  "agentId": "anomaly-agent",
  "timestamp": "2026-05-21T06:00:00Z",
  "correlationId": "signal-1234567890",
  "proposal": {
    "anomalyType": "content_safety",
    "severity": "high",
    "confidence": 0.95,
    "flags": ["inappropriate_content", "age_restriction"],
    "context": {
      "detectedIssues": ["explicit_language", "violent_content"],
      "ageAppropriate": false,
      "reasoning": "Content violates child safety guidelines"
    },
    "suggestedAction": "deny_with_explanation"
  }
}
```

## Detection Categories

1. **Content Safety**: Inappropriate content detection
2. **Age Verification**: Age-appropriate checks
3. **Predatory Behavior**: Grooming pattern detection
4. **Privacy Violations**: PII exposure detection

## Child Safety Focus

This agent is specifically tuned for:
- Child safety first
- Age-appropriate content
- Predatory behavior detection
- Privacy protection

## Key Principle
**Default Deny on Safety Concerns**

When uncertain about safety:
- Flag for parent review
- Propose deny with explanation
- Escalate to human oversight

## Responsible AI Integration

- **Safety**: Primary focus on child protection
- **Fairness**: Consistent safety standards
- **Transparency**: Clear reasoning for flags
- **Accountability**: All detections logged

## Development

```bash
cd agents/anomaly-agent
npm install
npm run dev
```

## Testing

```bash
npm test
npm run test:safety-scenarios
```
