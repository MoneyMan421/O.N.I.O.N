# 🧅 O.N.I.O.N — Observe, Notice, Infer, Operate, Narrate

**Verified • Responsible • Safety-First AI System (Child-Centered)**

[![Crucible-CI Workflow](https://github.com/MoneyMan421/O.N.I.O.N/actions/workflows/crucible-ci.yml/badge.svg)](https://github.com/MoneyMan421/O.N.I.O.N/actions)
[![codecov](https://codecov.io/gh/MoneyMan421/O.N.I.O.N/branch/main/graph/badge.svg)](https://codecov.io/gh/MoneyMan421/O.N.I.O.N)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Pre-Commit: Enabled](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Contributors](https://img.shields.io/github/contributors/MoneyMan421/O.N.I.O.N.svg)](https://github.com/MoneyMan421/O.N.I.O.N/graphs/contributors)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)

> O.N.I.O.N is a zero-trust, policy-driven AI architecture designed to protect children through verification-first workflows, explainable decisions, parent-aware controls, and accountable systems.

---

## ⚡ 60-Second Quickstart & Usage

```python
# example_usage.py
import asyncio
from src.main import app
import structlog

logger = structlog.get_logger()

async def pipeline_simulation():
    # L1: Observe (Input Validation)
    user_input = {"user_id": "kid_user_42", "prompt": "Hello world!"}
    logger.info("L1_observe", input=user_input)
    
    # L3: Infer (Policy Decision Point)
    is_safe = True 
    if is_safe:
        # L4: Operate (Execution Block)
        logger.info("L4_operate", action="allow_execution")
        # L5: Narrate (Audit Log Notification)
        print("🧅 O.N.I.O.N Lineage Verified: Message permitted safely.")

if __name__ == "__main__":
    asyncio.run(pipeline_simulation())
```

```shell
make setup
source .venv/bin/activate
make test  # Run all tests
make dev   # Start the API server (localhost:8000)
```

---

## ![O.N.I.O.N Pipeline Diagram](docs/assets/architecture.png)
*Replace with your actual SVG/PNG architecture diagram for full clarity.*

---

## 🧠 Responsible AI, COPPA & NIST Compliance

O.N.I.O.N explicitly implements architectural patterns targeting compliance with the Children's Online Privacy Protection Act (COPPA) and NIST AI Risk Management Framework:

- **Data Minimization:** No operator records memory states or persists identifying user tokens unless all verification constraints pass every layer.
- **Explainability:** Every decision is logged and auditable. Layer 5 provides audit logging before output.

See: [docs/why-zero-trust-ai.md](docs/why-zero-trust-ai.md) for a detailed rationale.

---

## ⚙️ Environment Variables

Before running O.N.I.O.N locally or in CI/CD, create a `.env` file at `AZ123ONI/.env` with the following structure:

```env
# Azure configuration for AI services
AZURE_EXISTING_AGENT_ID=...
AZURE_ENV_NAME=...
AZURE_LOCATION=...
AZURE_SUBSCRIPTION_ID=...
AZURE_EXISTING_AIPROJECT_ENDPOINT=...
AZURE_EXISTING_AIPROJECT_RESOURCE_ID=...
AZURE_EXISTING_RESOURCE_ID=...
AZD_ALLOW_NON_EMPTY_FOLDER=...
```

- NEVER commit secrets or production credentials.
- Use sample or dummy values in any example `.env` you share.

> See [`AZ123ONI/.env`](AZ123ONI/.env) for the template or required settings.

---

<!-- Keep your layered architecture, mission, acronym, and security/compliance docs as is after this section. -->
