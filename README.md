# CI/CD Practice — Skills Showcase

[![Python application](https://github.com/JonasBlx/ci-cd-practice/actions/workflows/python-app.yml/badge.svg)](https://github.com/JonasBlx/ci-cd-practice/actions/workflows/python-app.yml)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Tests](https://img.shields.io/badge/tests-pytest-green)

This repository demonstrates CI/CD skills using a simple Python project.  
It includes source code (`src/`), tests (`tests/`), and GitHub Actions workflows (`.github/workflows/`) to automate quality checks.

---

## Features

- Python application code in `src/`
- Unit tests with `pytest` in `tests/`
- Workflow automation under `.github/workflows/`
- Dependency management via `requirements.txt`

---

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows

pip install -r requirements.txt
pytest -q```

---

flowchart LR
  A[Push / PR] --> B[Setup Python]
  B --> C[Install requirements]
  C --> D[Run pytest]
  D --> E{Checks pass?}
  E -- Yes --> F[Success]
  E -- No --> G[Fail]

---

ci-cd-practice/
├─ .github/workflows/   # GitHub Actions workflows
├─ src/                 # Application code
├─ tests/               # Unit tests
├─ conftest.py          # Pytest configuration
├─ requirements.txt     # Dependencies
└─ README.md
