# Notification Service

**Layer**: L9 - Monitor (Alerts & Communications)

## Purpose

The Notification Service handles all communication with stakeholders. It:
- Sends alerts to parents/guardians
- Notifies staff of system events
- Provides child-friendly explanations
- Manages notification preferences

## Architecture Role

- **Alerts** on policy violations
- **Notifies** on approval requests
- **Explains** decisions in appropriate language
- **Tracks** notification delivery

## Notification Types

1. **Parent Alerts**: Approval requests, safety concerns
2. **Child Notifications**: Age-appropriate explanations
3. **Staff Alerts**: System issues, security events
4. **Audit Notifications**: Compliance reports

## Notification Channels

- Email
- SMS
- In-app notifications
- Webhooks (for integrations)

## Key Principles

1. **Age-Appropriate**: Messages tailored to audience
2. **Explainable**: Clear, simple language
3. **Timely**: Critical alerts sent immediately
4. **Preferences**: Users control notification settings

## API Endpoints

- `POST /notify/parent` - Send parent notification
- `POST /notify/child` - Send child notification
- `POST /notify/staff` - Send staff alert
- `GET /preferences/:userId` - Get notification preferences

## Development

```bash
cd services/notification-service
npm install
npm run dev
```

## Responsible AI Integration

- **Inclusiveness**: Accessible notification formats
- **Transparency**: Clear, honest communication
- **Privacy**: Secure message delivery
