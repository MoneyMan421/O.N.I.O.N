# O.N.I.O.N Automation Task Runner
.PHONY: setup dev test lint format clean help

help:
	@echo "🧅 O.N.I.O.N Developer Automation Suite"
	@echo "========================================"
	@echo "make setup   - Initialize virtual environment, install packages, and activate hooks"
	@echo "make dev     - Boot standard local API development server instance"
	@echo "make test    - Execute localized Crucible test verification runner with coverage report"
	@echo "make lint    - Run code quality validation tools (Black, Flake8, Mypy)"
	@echo "make format  - Auto-format code scripts utilizing strict Black guidelines"
	@echo "make clean   - Clean runtime caching artifacts and cache matrices safely"

setup:
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -e ".[dev]"
	.venv/bin/pre-commit install
	@echo "✅ Environment successfully initialized. Run 'source .venv/bin/activate' to begin."

dev:
	.venv/bin/uvicorn src.main:app --reload --host 127.0.0.1 --port 8000

test:
	.venv/bin/pytest tests/ --cov=src --cov-report=term-missing --cov-report=xml

lint:
	.venv/bin/black --check src/ tests/
	.venv/bin/flake8 src/ tests/ --max-line-length=88 --extend-ignore=E203
	.venv/bin/mypy src/ || true
	.venv/bin/bandit -r src/ -ll

format:
	.venv/bin/black src/ tests/

clean:
	rm -rf .pytest_cache .coverage coverage.xml htmlcov .mypy_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.py[cod]" -delete
