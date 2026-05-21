# 09 - Agents

**O.N.I.O.N Layers:** All (Cross-cutting)  
**Purpose:** Agent architecture and contracts - "Agents Propose, PDP Decides"

---

## 📋 Overview

This folder documents the agent architecture for the O.N.I.O.N system, implementing the principle: **"Agents Propose, PDP Decides"**.

---

## 🎯 Agent Philosophy

**Agents are Helpers, Not Deciders**

Key principles:
- **Agents propose actions** — They suggest what to do
- **PDP decides** — Policy Decision Point makes final decisions
- **Always explainable** — Every agent action has a reason
- **Always accountable** — Every agent action is logged
- **Safety first** — Agents cannot bypass safety controls

---

## 🤖 Agent Types

### 1. GitHub Copilot Agent
**Purpose:** AI-powered coding assistance

**Capabilities:**
- Code generation
- Code review suggestions
- Documentation generation
- Test generation
- Security vulnerability detection

**Constraints:**
- Cannot commit code directly
- Cannot bypass code review
- Cannot access secrets
- All suggestions logged

**Integration Points:**
- L1: Code generation in PRs
- L3: Test generation suggestions
- L4: Security recommendations

---

### 2. Content Moderation Agent
**Purpose:** Automated content safety checking

**Capabilities:**
- Detect inappropriate content
- Flag content for review
- Suggest content classification
- Detect patterns of abuse

**Constraints:**
- Cannot automatically ban users
- Cannot delete content without human review (except illegal content)
- Must provide reason codes
- All decisions appealable

**Integration Points:**
- L4: Policy evaluation for content
- L5: Escalation to human moderators
- L8: Content moderation audit trail

---

### 3. Deployment Agent
**Purpose:** Automated deployment orchestration

**Capabilities:**
- Build artifacts
- Run tests
- Deploy to environments
- Verify deployments

**Constraints:**
- Cannot deploy to production without approval
- Cannot bypass quality gates
- Must log all actions
- Must verify before proceeding

**Integration Points:**
- L2: Build orchestration
- L3: Test execution
- L6: Deployment execution
- L7: Post-deployment verification

---

### 4. Monitoring Agent
**Purpose:** Anomaly detection and alerting

**Capabilities:**
- Detect anomalies
- Trigger alerts
- Suggest remediation
- Correlate events

**Constraints:**
- Cannot take automated remediation without policy approval
- Must provide confidence scores
- Must explain anomaly detection
- All alerts logged

**Integration Points:**
- L7: Runtime monitoring
- L9: Feedback loops
- L8: Alert audit trail

---

## 📜 Agent Contract

### Request Format (Agent → PDP)

```json
{
  "request_id": "uuid",
  "correlation_id": "workflow-id",
  "timestamp": "ISO-8601",
  "agent": {
    "id": "agent-identifier",
    "type": "copilot|moderation|deployment|monitoring",
    "version": "1.0.0"
  },
  "proposal": {
    "action": "deploy|moderate|alert|execute",
    "resource": "resource identifier",
    "confidence": 0.95,
    "reasoning": "Why this action is proposed",
    "alternatives_considered": ["alt1", "alt2"]
  },
  "context": {
    "triggering_event": "what triggered this proposal",
    "environment": "dev|staging|prod",
    "risk_assessment": "low|medium|high|critical"
  },
  "supporting_evidence": {
    "test_results": "...",
    "scan_results": "...",
    "monitoring_data": "..."
  }
}
```

### Response Format (PDP → Agent)

```json
{
  "request_id": "uuid",
  "correlation_id": "workflow-id",
  "timestamp": "ISO-8601",
  "decision": "allow|deny|conditional",
  "reason_codes": ["REASON_1", "REASON_2"],
  "reason_text": {
    "technical": "Technical explanation",
    "user_friendly": "Simple explanation"
  },
  "obligations": [
    {
      "type": "log|notify|approval|verify",
      "description": "What must be done",
      "deadline": "when it must be done"
    }
  ],
  "policy": {
    "version": "1.0.0",
    "applicable_rules": ["rule-1", "rule-2"]
  },
  "instructions": {
    "proceed": true,
    "modifications_required": ["change1", "change2"],
    "verification_required": true
  }
}
```

---

## 🔄 Agent Workflow

### Standard Agent Flow

```
┌─────────────┐
│   Agent     │  1. Detects event or receives request
└──────┬──────┘
       │
       │  2. Analyzes situation
       │     Considers options
       │     Assesses risks
       ▼
┌─────────────┐
│   Agent     │  3. Prepares proposal with:
│  Proposal   │     - Recommended action
│             │     - Reasoning
│             │     - Evidence
│             │     - Confidence score
└──────┬──────┘
       │
       │  4. Submits to PDP
       ▼
┌─────────────┐
│     PDP     │  5. Evaluates against policies
│  Evaluation │     - Checks rules
│             │     - Assesses risk
│             │     - Considers context
└──────┬──────┘
       │
       │  6. Returns decision with:
       │     - Allow/Deny/Conditional
       │     - Reason codes
       │     - Obligations
       ▼
┌─────────────┐
│   Agent     │  7. Executes decision:
│  Execution  │     - If Allow: proceed
│             │     - If Deny: stop and log
│             │     - If Conditional: await obligations
└──────┬──────┘
       │
       │  8. Reports results
       ▼
┌─────────────┐
│  Audit Log  │  9. Everything logged with correlation ID
└─────────────┘
```

---

## 🛡️ Safety Constraints for Agents

### Hard Constraints (Never Allow)
- **Cannot bypass authentication**
- **Cannot bypass authorization**
- **Cannot access secrets directly**
- **Cannot delete audit logs**
- **Cannot disable safety features**
- **Cannot impersonate users**
- **Cannot bypass parent approval for children**

### Soft Constraints (Require PDP Approval)
- Deploying to production
- Deleting user data
- Banning users
- Changing security policies
- Accessing sensitive data
- Automated remediation actions

---

## 📊 Agent Monitoring

### Agent Performance Metrics
- **Accuracy:** % of proposals approved by PDP
- **Precision:** True positives / (True positives + False positives)
- **Recall:** True positives / (True positives + False negatives)
- **Latency:** Time to generate proposal
- **Confidence Calibration:** Actual vs. stated confidence

### Agent Audit Trail
Every agent action logged:
```json
{
  "event_type": "agent_proposal",
  "agent_id": "copilot-agent-1",
  "proposal": { "action": "deploy", "resource": "prod" },
  "pdp_decision": "conditional",
  "reason_codes": ["DEPLOY_APPROVAL_PENDING"],
  "outcome": "awaiting_approval"
}
```

---

## 🧪 Agent Testing

### Required Tests for New Agents

1. **Functional Tests**
   - Agent correctly identifies situations
   - Proposals are well-formed
   - Agent handles PDP responses correctly

2. **Safety Tests**
   - Cannot bypass safety constraints
   - Handles edge cases safely
   - Fails safely (fail-closed, not fail-open)

3. **Performance Tests**
   - Meets latency requirements
   - Handles load appropriately
   - Resource usage acceptable

4. **Integration Tests**
   - Integrates with PDP correctly
   - Logs to audit system properly
   - Handles errors gracefully

---

## 📋 Agent Development Checklist

### New Agent Requirements
- [ ] Agent contract implemented (request/response)
- [ ] PDP integration tested
- [ ] Safety constraints enforced
- [ ] All actions logged with correlation IDs
- [ ] Confidence scores provided
- [ ] Reasoning included in proposals
- [ ] Error handling implemented
- [ ] Documentation complete
- [ ] Security review passed
- [ ] Safety review passed (if user-facing)

---

## 🎓 Agent Best Practices

### DO
✅ Always consult PDP before acting  
✅ Provide clear reasoning for proposals  
✅ Include confidence scores  
✅ Log all actions  
✅ Handle errors gracefully  
✅ Fail safely (deny when uncertain)  
✅ Respect timeouts  
✅ Consider alternatives  
✅ Explain decisions to users  

### DON'T
❌ Act without PDP approval  
❌ Bypass safety controls  
❌ Make irreversible actions without human approval  
❌ Access secrets directly  
❌ Modify audit logs  
❌ Impersonate users  
❌ Assume high-confidence = correct  
❌ Ignore PDP instructions  

---

## 🔮 Future Agent Types

### Planned Agents
1. **Accessibility Agent** — Ensure accessibility compliance
2. **Performance Agent** — Detect and suggest performance improvements
3. **Cost Optimization Agent** — Suggest cost-saving measures
4. **Documentation Agent** — Auto-generate and update docs
5. **Test Coverage Agent** — Identify gaps in test coverage

---

## 📚 Related Documentation

- [Governance](../00-governance/) — Agent governance
- [Policy](../02-policy/) — PDP contracts and reason codes
- [Architecture](../03-architecture/) — System architecture
- [Security](../04-security/) — Agent security controls
- [Audit](../08-audit/) — Agent audit logging

---

## 📝 Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-05-21 | Initial | Initial agent documentation |

---

**🧅 Agents propose. PDP decides. Every action explained. Every decision logged. Always accountable.**
