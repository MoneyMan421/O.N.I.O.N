# Changelog

All notable changes to the O.N.I.O.N Guardian Agent project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project structure and documentation
- Complete README with O.N.I.O.N architecture overview
- 9-layer verification architecture documentation structure
- Core service scaffolding (API Gateway, PDP, Approval, Telemetry, Notification, Audit)
- Agent layer structure (Behavior, Anomaly, Context, Explanation agents)
- Infrastructure as Code templates (Terraform, Kubernetes)
- CI/CD pipeline configurations
- Security scanning workflows
- Policy validation workflow
- Contribution guidelines
- Security policy
- Code of conduct

### Architecture
- Established "Agents Propose, PDP Decides" principle
- Defined Policy Decision Point (PDP) contract
- Implemented child safety principles (Default Deny, Parent Authority, Explainability)
- Created audit trail requirements
- Defined agent output contracts

### Documentation
- Created docs/00-governance/ for mission and Responsible AI
- Created docs/01-risk/ for threat modeling
- Created docs/02-policy/ for PDP contracts
- Created docs/03-architecture/ for system diagrams
- Created docs/04-security/ for security controls
- Created docs/05-safety/ for child safety guidelines
- Created docs/06-compliance/ for compliance checklists
- Created docs/07-verification/ for testing strategies
- Created docs/08-audit/ for audit requirements
- Created docs/09-agents/ for agent contracts

## [0.1.0] - 2026-05-21

### Added
- Initial repository setup
- Project foundation and architecture planning

---

## Version History Guide

### Version Number Format: MAJOR.MINOR.PATCH

- **MAJOR**: Breaking changes, incompatible API changes
- **MINOR**: New features, backward-compatible additions
- **PATCH**: Bug fixes, backward-compatible fixes

### Categories

- **Added**: New features
- **Changed**: Changes in existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security vulnerability fixes
- **Architecture**: Architectural changes or decisions
- **Documentation**: Documentation updates

### Child Safety Notice

All changes that impact child safety mechanisms are marked with ⚠️ and require additional review and testing before release.
