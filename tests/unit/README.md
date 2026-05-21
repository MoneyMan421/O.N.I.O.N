# Unit Tests

This directory contains unit tests for O.N.I.O.N components.

## Structure

- `services/` - Unit tests for services
- `agents/` - Unit tests for agents
- `packages/` - Unit tests for shared packages

## Running Tests

```bash
# Run all unit tests
npm run test:unit

# Run tests for specific service
cd services/api-gateway && npm test

# Run with coverage
npm run test:unit -- --coverage
```

## Test Standards

- Minimum 80% code coverage
- Test all public APIs
- Mock external dependencies
- Test edge cases and error conditions

## Example

```typescript
describe('PDP Service', () => {
  it('should return allow decision when all policies pass', async () => {
    const pdp = new PDPService();
    const decision = await pdp.evaluate({
      action: 'read_content',
      userId: 'user-123'
    });
    
    expect(decision.decision).toBe('allow');
    expect(decision.reasonCode).toBe('ALL_POLICIES_SATISFIED');
  });
});
```
