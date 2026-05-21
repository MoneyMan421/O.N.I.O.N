# Explanation Agent - Decision Explanations

**Type**: Agent (Non-Authoritative)

## Purpose

The Explanation Agent generates human-readable explanations of decisions. It:
- Translates PDP decisions into plain language
- Creates child-friendly explanations
- Generates parent-level technical details
- **Does NOT make decisions** (PDP decides)

## Agent Contract

### Outputs (Explanations Only)
```json
{
  "agentId": "explanation-agent",
  "timestamp": "2026-05-21T06:00:00Z",
  "correlationId": "pdp-1234567890",
  "explanations": {
    "child": {
      "simple": "We need to check with your parent before you can do this.",
      "friendly": "This action needs grown-up permission. We've sent a message to your parent. They'll let us know if it's okay!"
    },
    "parent": {
      "summary": "Action requires parental approval due to age restrictions.",
      "technical": "Policy PDP-123 triggered: User age (8) below minimum (13) for requested action. Parent approval workflow initiated per child safety guidelines.",
      "nextSteps": [
        "Review the approval request in your parent portal",
        "Approve or deny within 24 hours",
        "Contact support if you have questions"
      ]
    },
    "staff": {
      "details": "PDP Decision: CONDITIONAL | Reason: AGE_RESTRICTION | Policy: v1.0.0 | Correlation ID: pdp-1234567890"
    }
  }
}
```

## Explanation Levels

1. **Child (Ages 5-12)**: Simple, friendly, reassuring
2. **Teen (Ages 13-17)**: Clear, respectful, informative
3. **Parent**: Detailed, actionable, technical when needed
4. **Staff**: Full technical details, correlation IDs

## Key Principles

1. **Age-Appropriate Language**: Tailored to audience
2. **Honesty**: Clear, truthful explanations
3. **Empowerment**: Next steps provided
4. **No Jargon**: Plain language (except staff level)

## Explanation Templates

- Approval required
- Policy violation
- Safety concern
- Technical error
- Success confirmation

## Responsible AI Integration

- **Transparency**: All decisions explained
- **Inclusiveness**: Multiple reading levels
- **Accountability**: Clear reasoning provided
- **Safety**: Child-appropriate messaging

## Development

```bash
cd agents/explanation-agent
npm install
npm run dev
```

## Testing

```bash
npm test
npm run test:readability
```
