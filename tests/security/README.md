# Security Tests

This directory contains security tests for O.N.I.O.N.

## Purpose

Verify security controls and identify vulnerabilities.

## Test Types

1. **Authentication Tests**: Login, MFA, session management
2. **Authorization Tests**: RBAC, PBAC, permission checks
3. **Input Validation**: SQL injection, XSS, command injection
4. **Secrets Tests**: No secrets in code/logs
5. **Encryption Tests**: Data protection at rest and in transit

## Running Tests

```bash
# Run security test suite
npm run test:security

# Run OWASP ZAP scan
npm run security:zap

# Run vulnerability scans
npm audit
npm run security:snyk
```

## Test Scenarios

- SQL injection attempts
- XSS attack vectors
- CSRF protection
- Authentication bypass attempts
- Authorization escalation
- Secret exposure
- Encryption validation

## Example

```typescript
describe('Security Tests', () => {
  it('should prevent SQL injection', async () => {
    const maliciousInput = "'; DROP TABLE users; --";
    
    const response = await api.post('/api/search', {
      query: maliciousInput
    });
    
    // Should sanitize input, not execute SQL
    expect(response.status).toBe(400);
    expect(response.body.error).toContain('invalid input');
    
    // Verify database tables still exist
    const tables = await db.listTables();
    expect(tables).toContain('users');
  });
  
  it('should not expose secrets in logs', async () => {
    // Trigger error that might log sensitive data
    await api.post('/api/login', {
      password: 'test-password-123'
    });
    
    // Check logs
    const logs = await getLogs();
    expect(logs).not.toContain('test-password-123');
    expect(logs).not.toContain('password');
  });
});
```
