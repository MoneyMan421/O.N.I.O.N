# Contributing to O.N.I.O.N Guardian Agent

Thank you for your interest in contributing to O.N.I.O.N! This document provides guidelines for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Process](#development-process)
- [Architecture Principles](#architecture-principles)
- [Pull Request Process](#pull-request-process)
- [Testing Requirements](#testing-requirements)
- [Documentation](#documentation)

## Code of Conduct

This project adheres to the Contributor Covenant [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## Getting Started

1. **Fork the repository** and clone it locally
2. **Set up your development environment**:
   ```bash
   # Install dependencies
   npm install
   
   # Copy environment configuration
   cp configs/dev.env.example configs/dev.env
   
   # Start local services
   docker-compose up -d
   ```

3. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Process

### Architecture Principles

O.N.I.O.N follows strict architectural principles:

1. **Agents Propose, PDP Decides**: Agents cannot make autonomous decisions. All proposals must go through the Policy Decision Point (PDP).

2. **Default Deny**: When in doubt, deny. Child safety always comes first.

3. **Parent Authority**: High-risk actions require explicit parent approval.

4. **Explainability Required**: Every decision must be explainable in both child-friendly and technical terms.

5. **Immutable Audit**: All decisions and actions must be logged immutably.

### Coding Standards

- **TypeScript/JavaScript**: Follow ESLint configuration
- **Python**: Follow PEP 8 and use type hints
- **Documentation**: All public APIs must have comprehensive documentation
- **Testing**: Minimum 80% code coverage required
- **Security**: No secrets in code, all inputs validated

### Branch Naming Convention

- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation updates
- `refactor/` - Code refactoring
- `test/` - Test additions or modifications
- `security/` - Security improvements

## Pull Request Process

1. **Before submitting**:
   - Ensure all tests pass: `npm test`
   - Run linters: `npm run lint`
   - Update documentation if needed
   - Add entries to CHANGELOG.md

2. **PR Description must include**:
   - Summary of changes
   - Link to related issue(s)
   - Testing performed
   - Security considerations
   - Impact on child safety (if applicable)

3. **Review Process**:
   - At least one maintainer approval required
   - All CI checks must pass (build, test, security scans, policy validation)
   - Security-sensitive changes require additional review
   - Changes affecting child safety require extra scrutiny

4. **Merge Requirements**:
   - All conversations resolved
   - Branch up to date with main
   - No merge conflicts
   - Documentation updated

## Testing Requirements

### Unit Tests
- Cover all new functions and methods
- Test edge cases and error conditions
- Mock external dependencies

### Integration Tests
- Test service interactions
- Verify PDP integration
- Test approval workflows

### Security Tests
- Test authentication and authorization
- Validate input sanitization
- Test for common vulnerabilities (OWASP Top 10)

### Policy Tests
- Verify policy decisions
- Test reason code generation
- Validate audit log entries

## Documentation

### Code Documentation
- All public APIs must have JSDoc/docstrings
- Include examples in documentation
- Document security considerations

### Architecture Documentation
Documentation is organized by the 9-layer architecture in `/docs`:

- `00-governance/` - Mission, roles, Responsible AI
- `01-risk/` - Threat models, risk register
- `02-policy/` - PDP contracts, reason codes
- `03-architecture/` - System diagrams, ONION model
- `04-security/` - Authentication, secrets, CI/CD security
- `05-safety/` - Child safety, guardrails, approval flows
- `06-compliance/` - Checklists, audit requirements
- `07-verification/` - Test strategy, runtime validation
- `08-audit/` - Audit schema, evidence collection
- `09-agents/` - Agent contracts, safety rules

Update relevant documentation when making changes.

## Security Issues

**DO NOT** open public issues for security vulnerabilities. Instead, please refer to our [Security Policy](SECURITY.md) for responsible disclosure procedures.

## Questions?

- Open a discussion in GitHub Discussions
- Check existing issues and documentation
- Contact maintainers via the channels listed in README.md

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
