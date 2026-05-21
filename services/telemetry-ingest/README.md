# Telemetry Ingest Service

**Layer**: L1 - Entry (Signal Collection)

## Purpose

The Telemetry Ingest Service collects and validates signals from agents and services. It:
- Ingests telemetry data from all sources
- Validates signal format and integrity
- Routes signals to appropriate services
- Provides buffering and backpressure handling

## Architecture Role

- **Collects** signals from agents
- **Validates** signal structure
- **Routes** to PDP, audit, monitoring
- **Buffers** during high load

## Signal Types

1. **Agent Signals**: Risk scores, flags, context from agents
2. **Service Telemetry**: Health, performance, errors
3. **User Events**: Actions, interactions (anonymized)
4. **System Events**: Deployments, configuration changes

## Signal Contract

```json
{
  "source": "behavior-agent",
  "timestamp": "2026-05-21T06:00:00Z",
  "correlationId": "signal-1234567890",
  "signalType": "risk_assessment",
  "data": {
    "riskScore": 0.75,
    "flags": ["unusual_pattern"],
    "context": {...},
    "confidence": 0.9
  }
}
```

## Key Principles

1. **Validation First**: All signals validated before processing
2. **Non-Blocking**: Async processing with buffering
3. **Audit Trail**: All signals logged
4. **Privacy**: No PII in telemetry

## Development

```bash
cd services/telemetry-ingest
npm install
npm run dev
```

## Responsible AI Integration

- **Privacy**: PII stripped from telemetry
- **Transparency**: Signal sources tracked
- **Reliability**: High-availability design
