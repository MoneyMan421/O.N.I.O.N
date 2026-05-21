# Approval Service - Human Oversight

**Layer**: L5 - Control (Parent/Guardian Approval)

## Purpose

The Approval Service manages human-in-the-loop oversight for O.N.I.O.N. It:
- Handles parent/guardian approval requests
- Manages time-limited approval tokens
- Enforces approval workflows
- Sends notifications for approval requests

## Architecture Role

- **Gates** high-risk actions
- **Notifies** parents/guardians
- **Tracks** approval history
- **Enforces** consent requirements

## Approval Types

1. **Parent Approval**: Required for sensitive child actions
2. **Release Approval**: Required for production deployments
3. **Override Approval**: Emergency access with audit trail

## Approval Flow

1. Service receives conditional PDP decision
2. Approval request created with context
3. Parent/guardian notified
4. Approval granted or denied
5. Decision logged immutably
6. Token generated (if approved)
7. Action proceeds with token

## Key Principles

1. **Parent Authority**: Parents have final say
2. **Time-Limited**: Approvals expire
3. **Context-Rich**: Full information provided for informed consent
4. **Audit Trail**: All approvals tracked permanently

## API Endpoints

- `POST /approval/request` - Request approval
- `GET /approval/:id` - Check approval status
- `POST /approval/:id/grant` - Grant approval (parent only)
- `POST /approval/:id/deny` - Deny approval (parent only)

## Development

```bash
cd services/approval-service
npm install
npm run dev
```

## Responsible AI Integration

- **Human Oversight**: Parents control high-risk decisions
- **Transparency**: Full context provided for approval
- **Accountability**: Clear ownership of approval decisions
