# Integration Tests

This directory contains integration tests for O.N.I.O.N.

## Purpose

Test interactions between services and components.

## Structure

- `api/` - API integration tests
- `services/` - Service-to-service tests
- `workflows/` - End-to-end workflow tests

## Running Tests

```bash
# Start test environment
docker-compose -f docker-compose.test.yml up -d

# Run integration tests
npm run test:integration

# Stop test environment
docker-compose -f docker-compose.test.yml down
```

## Test Scenarios

- API Gateway → PDP → Audit flow
- Approval workflow
- Agent signal processing
- Policy decision with multiple agents

## Example

```typescript
describe('Approval Workflow Integration', () => {
  it('should complete parent approval flow', async () => {
    // 1. Request requiring approval
    const response = await api.post('/api/action', {
      childId: 'child-123',
      action: 'add_friend'
    });
    
    expect(response.body.decision).toBe('conditional');
    expect(response.body.approvalId).toBeDefined();
    
    // 2. Verify approval request created
    const approval = await approvalService.get(response.body.approvalId);
    expect(approval.status).toBe('pending');
    
    // 3. Grant approval
    await approvalService.grant(response.body.approvalId, 'parent-456');
    
    // 4. Verify action proceeds
    const finalResponse = await api.post('/api/action', {
      childId: 'child-123',
      action: 'add_friend',
      approvalToken: approval.token
    });
    
    expect(finalResponse.body.decision).toBe('allow');
  });
});
```
