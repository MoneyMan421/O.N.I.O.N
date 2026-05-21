# Contributing to O.N.I.O.N

Thank you for your interest in contributing to O.N.I.O.N! This guide will help you understand our contribution process and requirements.

## 🎯 Before You Start

### Understand the Mission

O.N.I.O.N is built around:
- **Safety-first approach** — especially for children and vulnerable users
- **Defense-in-depth** — verification at every layer (L1-L9)
- **Accountability** — every decision must be explainable and auditable
- **Responsible AI principles** — fairness, safety, privacy, inclusiveness, transparency, accountability

### Read the Documentation

Before contributing, please review:
- [README.md](README.md) — Architecture overview
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) — Community standards
- [SECURITY.md](SECURITY.md) — Security policies
- [`docs/`](docs/) — Detailed technical documentation

## 🚀 Getting Started

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR-USERNAME/O.N.I.O.N.git
cd O.N.I.O.N
git remote add upstream https://github.com/Big-Orga/O.N.I.O.N.git
```

### 2. Create a Branch

Use descriptive branch names that reflect the change:

```bash
git checkout -b feature/add-policy-verification
git checkout -b fix/audit-log-format
git checkout -b docs/update-architecture-diagram
```

### 3. Make Your Changes

Follow these principles:
- **Small, focused changes** — One logical change per PR
- **Maintain all 9 layers** — Don't bypass verification steps
- **Document your changes** — Update docs if you change behavior
- **Test thoroughly** — Add tests for new functionality

## 📋 Contribution Guidelines

### Code Standards

- **Security First:** Never compromise security for convenience
- **Safety Checks:** All user-facing changes must consider child safety
- **Explainability:** Add reason codes for decisions and policy evaluations
- **Auditability:** Ensure all actions are logged with correlation IDs

### Testing Requirements

All contributions must include appropriate tests:

- **Unit Tests:** For individual components and functions
- **Integration Tests:** For component interactions
- **Security Tests:** For security-relevant changes
- **Safety Tests:** For child-safety features

Run tests before submitting:

```bash
# Run unit tests
npm test  # or appropriate test command for your language

# Run linters
npm run lint

# Run security scans (if applicable)
npm run security-scan
```

### Documentation Requirements

Update documentation for:
- New features or capabilities
- Changes to existing behavior
- New configuration options
- Architecture changes

Documentation locations:
- `README.md` — High-level overview updates
- `docs/` — Detailed technical documentation
- Code comments — For complex logic
- `CHANGELOG.md` — User-facing changes

### Commit Message Format

Use clear, descriptive commit messages:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Test additions or changes
- `refactor`: Code refactoring
- `security`: Security improvements
- `chore`: Maintenance tasks

**Example:**
```
feat(policy): Add reason codes for content filtering decisions

- Implement structured reason code system
- Add parent-friendly explanations
- Update audit logging to include reason codes
- Add unit tests for reason code generation

Relates to: #123
```

## 🔄 Pull Request Process

### 1. Prepare Your PR

Before submitting:
- [ ] All tests pass locally
- [ ] Code follows project standards
- [ ] Documentation is updated
- [ ] Commits are clean and descriptive
- [ ] No merge conflicts with `main`

### 2. Submit PR

Use the provided PR template (`.github/PULL_REQUEST_TEMPLATE.md`):

- **Clear title** — Describe what the PR does
- **Description** — Explain why and how
- **Layer impact** — Which of the 9 layers are affected
- **Testing** — How you tested the changes
- **Screenshots** — If UI changes are involved

### 3. Code Review

Your PR will be reviewed for:
- **Correctness** — Does it work as intended?
- **Security** — Are there security implications?
- **Safety** — Does it maintain child-safety guarantees?
- **Architecture** — Does it fit the 9-layer model?
- **Tests** — Is it adequately tested?
- **Documentation** — Is it well-documented?

### 4. Address Feedback

- Respond to all review comments
- Make requested changes
- Push updates to your branch
- Request re-review when ready

### 5. Merge

Once approved:
- Maintainers will merge your PR
- Your changes will go through the full L1-L9 verification pipeline
- You'll be credited in [CHANGELOG.md](CHANGELOG.md)

## 🛡️ Security Contributions

### Reporting Vulnerabilities

**DO NOT** open public issues for security vulnerabilities. See [SECURITY.md](SECURITY.md) for reporting procedures.

### Security-Related PRs

Security improvements are always welcome:
- Dependency updates
- Security test additions
- Vulnerability fixes
- Security documentation improvements

## 📚 Documentation Contributions

Documentation improvements are highly valued:

- **Fix typos** — Small fixes are always welcome
- **Clarify instructions** — Help make docs more accessible
- **Add examples** — Real-world examples help users
- **Update diagrams** — Keep architecture diagrams current

## 🎨 Types of Contributions

### Code Contributions
- Bug fixes
- Feature implementations
- Performance improvements
- Test coverage improvements

### Documentation Contributions
- Tutorial creation
- Example projects
- Architecture documentation
- API documentation

### Community Contributions
- Answering questions in issues
- Helping new contributors
- Improving issue templates
- Community event organization

## ❓ Questions?

- **General questions:** Open a GitHub Discussion
- **Bug reports:** Use the [bug report template](.github/ISSUE_TEMPLATE/bug_report.md)
- **Feature requests:** Use the [feature request template](.github/ISSUE_TEMPLATE/feature_request.md)
- **Security issues:** See [SECURITY.md](SECURITY.md)

## 🙏 Recognition

We value all contributions! Contributors will be:
- Listed in [CHANGELOG.md](CHANGELOG.md) for their contributions
- Credited in release notes
- Recognized in our community

## 📜 License

By contributing to O.N.I.O.N, you agree that your contributions will be licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

**Thank you for helping make O.N.I.O.N safer, more secure, and more accountable!**

🧅 Every layer verified. Every decision explained. Every action accountable.
