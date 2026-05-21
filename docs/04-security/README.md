# 04 - Security

**O.N.I.O.N Layers:** All (focus on L1, L4, L6)  
**Purpose:** Authentication, authorization, secrets management, and security controls

---

## 📋 Overview

This folder documents security controls, authentication mechanisms, authorization policies, and secrets management for the O.N.I.O.N system.

---

## 🔐 Security Principles

### Core Principles
1. **Least Privilege** — Grant minimum necessary permissions
2. **Defense in Depth** — Multiple layered security controls
3. **Zero Trust** — Never trust, always verify
4. **Secure by Default** — Security enabled out of the box
5. **Transparency** — Security decisions are explainable

---

## 🔑 Authentication

### User Authentication
- **Primary:** OAuth 2.0 / OpenID Connect
- **Identity Providers:** Azure AD, Auth0, or similar
- **Session Management:** Secure, HTTP-only cookies
- **Token Lifecycle:** Short-lived access tokens, refresh tokens

### Service Authentication
- **Method:** Managed identities (Azure) or service accounts
- **Authentication:** Certificate-based or OIDC
- **Rotation:** Automatic credential rotation
- **Scope:** Minimally scoped to required resources

### GitHub Actions Authentication
- **Method:** OIDC (Passwordless)
- **Permissions:** Minimal required for each job
- **Secrets:** Stored in GitHub Secrets or Azure Key Vault
- **Audit:** All authentication attempts logged

---

## 🛡️ Authorization

### Role-Based Access Control (RBAC)

#### User Roles
| Role | Permissions | Use Case |
|------|-------------|----------|
| **Child** | Read child-appropriate content, limited actions | Users under 18 |
| **Parent** | Child role + approve child actions | Parents/guardians |
| **User** | Read/write own data, standard actions | Adult users |
| **Moderator** | Review flagged content, ban users | Content moderation |
| **Admin** | Full system access | System administration |

#### Service Roles
| Role | Permissions | Use Case |
|------|-------------|----------|
| **Reader** | Read-only access to non-sensitive data | Monitoring services |
| **Writer** | Write to specific resources | Application services |
| **Deployer** | Deploy to specific environments | CI/CD pipelines |
| **Admin** | Full access to infrastructure | Infrastructure management |

### Policy-Based Authorization
- **PDP Evaluation:** All authorization requests evaluated by PDP
- **Attributes:** User attributes, resource classification, context
- **Decision:** Allow/Deny with reason codes
- **Caching:** Policy decisions cached with TTL

---

## 🔒 Secrets Management

### Secrets Strategy
- **Storage:** Azure Key Vault or GitHub Secrets
- **Access:** Managed identities or OIDC
- **Rotation:** Automatic rotation where possible
- **Audit:** All secret access logged

### Secret Types
1. **API Keys** — Third-party service authentication
2. **Database Credentials** — Database access
3. **Encryption Keys** — Data encryption
4. **Signing Keys** — Token signing
5. **Certificates** — TLS/SSL certificates

### Best Practices
- ✅ Never commit secrets to code
- ✅ Use environment-specific secrets
- ✅ Rotate secrets regularly (90 days max)
- ✅ Audit secret access
- ✅ Use short-lived tokens when possible
- ❌ Never log secrets
- ❌ Never expose secrets in error messages
- ❌ Never share secrets between environments

---

## 🔐 Encryption

### Data at Rest
- **Method:** AES-256 encryption
- **Key Management:** Azure Key Vault
- **Scope:** All sensitive data (PII, child data)

### Data in Transit
- **Method:** TLS 1.3
- **Certificates:** Valid, properly signed certificates
- **HSTS:** Enabled for all web endpoints

### Application-Level Encryption
- **Use Cases:** Sensitive user data, child information
- **Method:** Field-level encryption
- **Keys:** Per-tenant or per-user encryption keys

---

## 🛡️ Network Security

### Network Segmentation
```
┌─────────────────────────────────────────┐
│  Public Zone (Internet-facing)           │
│  - Load Balancer                         │
│  - CDN                                   │
└──────────────┬──────────────────────────┘
               │ Firewall/WAF
               ▼
┌─────────────────────────────────────────┐
│  DMZ (Web Tier)                          │
│  - Web Servers                           │
│  - API Gateway                           │
└──────────────┬──────────────────────────┘
               │ Network Policy
               ▼
┌─────────────────────────────────────────┐
│  Application Zone (App Tier)             │
│  - Application Services                  │
│  - PDP/PEP                               │
└──────────────┬──────────────────────────┘
               │ Network Policy
               ▼
┌─────────────────────────────────────────┐
│  Data Zone (Data Tier)                   │
│  - Databases                             │
│  - Storage                               │
└─────────────────────────────────────────┘
```

### Firewall Rules
- **Default:** Deny all, allow by exception
- **Ingress:** Only necessary ports open
- **Egress:** Restricted to required destinations
- **Monitoring:** All network traffic logged

---

## 🔍 Security Monitoring

### Security Events to Monitor
- Failed login attempts
- Unauthorized access attempts
- Policy violations
- Secret access
- Configuration changes
- Anomalous behavior

### Alerting
- **Critical:** Immediate notification (SMS/phone)
- **High:** 5-minute notification (email/Slack)
- **Medium:** Hourly digest
- **Low:** Daily report

---

## 🚨 Incident Response

### Severity Levels
- **P0 - Critical:** Active breach, data exposure
- **P1 - High:** Vulnerability exploitation attempt
- **P2 - Medium:** Security misconfiguration
- **P3 - Low:** Minor security issue

### Response Process
1. **Detection** — Security event detected
2. **Analysis** — Assess severity and impact
3. **Containment** — Isolate affected systems
4. **Eradication** — Remove threat
5. **Recovery** — Restore normal operations
6. **Post-Mortem** — Learn and improve

---

## 🔧 Security Tools

### Static Analysis (SAST)
- CodeQL (GitHub)
- SonarQube
- Semgrep

### Dynamic Analysis (DAST)
- OWASP ZAP
- Burp Suite

### Dependency Scanning
- Dependabot (GitHub)
- npm audit / pip-audit
- Snyk

### Secret Scanning
- GitHub secret scanning
- git-secrets
- TruffleHog

### Container Scanning
- Trivy
- Grype
- Docker Scout

---

## ✅ Security Checklist

### Development
- [ ] Code review required for all changes
- [ ] Security testing in CI/CD
- [ ] Dependency vulnerability scanning
- [ ] Secret scanning enabled

### Deployment
- [ ] Least privilege service accounts
- [ ] Secrets from Key Vault
- [ ] TLS/HTTPS enforced
- [ ] Network policies configured

### Runtime
- [ ] Authentication required
- [ ] Authorization enforced by PEP
- [ ] All access logged
- [ ] Security monitoring active

---

## 📚 Related Documentation

- [Governance](../00-governance/) — Security governance
- [Risk Management](../01-risk/) — Security risks
- [Policy](../02-policy/) — Security policies
- [Architecture](../03-architecture/) — Security architecture
- [Audit](../08-audit/) — Security audit logging

---

## 📝 Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-05-21 | Initial | Initial security documentation |

---

**🧅 Security at every layer. Authentication verified. Authorization enforced. Secrets protected.**
