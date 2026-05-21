# API Gateway - Policy Enforcement Point (PEP)

**Layer**: L6 - Deploy (Policy Enforcement)

## Purpose

The API Gateway serves as the Policy Enforcement Point (PEP) for the O.N.I.O.N system. It:
- Enforces policy decisions from the PDP
- Validates all incoming requests
- Provides rate limiting and DDoS protection
- Routes requests to appropriate services

## Architecture Role

- **Enforces** policies (does not decide)
- **Validates** authentication and authorization
- **Logs** all requests for audit
- **Integrates** with PDP for decision evaluation

## Key Principles

1. **No Autonomous Decisions**: All policy decisions come from PDP
2. **Default Deny**: Unknown requests are rejected
3. **Audit Everything**: All requests and responses are logged
4. **Fail Secure**: On error, deny access

## API Endpoints

- `GET /health` - Health check
- `GET /ready` - Readiness check
- `POST /api/*` - Protected API endpoints (PDP evaluation required)

## Configuration

See `configs/` for environment-specific configuration.

## Development

```bash
cd services/api-gateway
npm install
npm run dev
```

## Testing

```bash
npm test
npm run test:integration
npm run test:security
```

## Responsible AI Integration

- **Privacy & Security**: TLS encryption, no PII logging
- **Accountability**: All requests tied to correlation IDs
- **Transparency**: Decision reasons included in responses
