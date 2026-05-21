# End-to-End Tests

This directory contains E2E tests for O.N.I.O.N.

## Purpose

Test complete user workflows from end to end.

## Tools

- Playwright for browser automation
- Postman/Newman for API workflows
- Custom test harnesses

## Test Scenarios

### Child Safety Workflows

1. **Content Filtering**
   - Child attempts to access inappropriate content
   - Content is blocked
   - Age-appropriate explanation shown
   - Parent notification sent

2. **Approval Workflow**
   - Child requests age-restricted feature
   - Approval request created
   - Parent receives notification
   - Parent approves/denies
   - Action proceeds or blocked accordingly

3. **Privacy Protection**
   - Child attempts to share personal information
   - System detects PII
   - Request blocked
   - Parent notified

### Complete Request Flow

```
User → API Gateway → PDP → Agents → PDP Decision → 
Approval (if needed) → PEP Enforcement → Audit → Response
```

## Running Tests

```bash
# Install Playwright
npx playwright install

# Run E2E tests
npm run test:e2e

# Run specific test suite
npm run test:e2e -- --grep "approval"

# Run in headed mode (see browser)
npm run test:e2e -- --headed
```

## Example

```typescript
describe('E2E: Parent Approval Workflow', () => {
  test('should complete approval flow', async ({ page }) => {
    // 1. Child login
    await page.goto('http://localhost:8080/login');
    await page.fill('#username', 'child-user-8yo');
    await page.fill('#password', 'test-password');
    await page.click('button[type=submit]');
    
    // 2. Attempt age-restricted action
    await page.goto('http://localhost:8080/add-friend');
    await page.fill('#friendId', 'older-user-15yo');
    await page.click('#submit');
    
    // 3. Verify approval required message
    await expect(page.locator('.approval-message')).toContainText(
      'We need to ask your parent first!'
    );
    
    // 4. Switch to parent account
    await page.goto('http://localhost:8080/logout');
    await page.goto('http://localhost:8080/login');
    await page.fill('#username', 'parent-account');
    await page.fill('#password', 'parent-password');
    await page.click('button[type=submit]');
    
    // 5. Check approval requests
    await page.goto('http://localhost:8080/parent/approvals');
    await expect(page.locator('.approval-request')).toBeVisible();
    
    // 6. Approve request
    await page.click('.approve-button');
    
    // 7. Verify approval granted
    await expect(page.locator('.success-message')).toContainText(
      'Approval granted'
    );
    
    // 8. Switch back to child, verify action proceeds
    // ... etc
  });
});
```
