# Python Test-Driven Development Constitution

## Core Principles

### 1. TDD Is Required
- Tests are written before production code: write a failing test (Red), implement until it passes (Green), then refactor (Refactor).

### 2. Tests First, Always
- Every new feature, bug fix, or behavior change must include one or more tests that reproduce the desired behavior (or the bug) before implementation.

### 3. Preferred Tools and Environment
- Use `pytest` as the default test runner; `unittest` allowed for legacy code.
- Use virtual environments (`venv`, `pipenv`, or `poetry`) and record dev dependencies in `requirements-dev.txt` or `pyproject.toml`.

### 4. Test Structure & Naming
- Place tests under a top-level `tests/` directory mirroring package/module structure.
- Test files should be named `test_*.py`; test classes and functions should clearly state behavior.

### 5. Test Types and Scope
- Unit tests: isolated, fast, deterministic—mock external dependencies.
- Integration tests: used when modules interact or when external systems are required; keep them separate and runnable in CI stages.
- Acceptance tests: cover end-to-end user-facing behavior where appropriate.

### 6. Quality & Coverage
- New modules should aim for high test coverage (nominal target: 90%); coverage reports must be produced in CI.
- Coverage targets are guidelines—tests must prioritize meaningful behavioral checks over metric gaming.

### 7. CI and Pull Requests
- All tests (unit + required integration stages) must run in CI on every pull request and must pass before merging.
- Flaky tests must be annotated, investigated, and either fixed or quarantined with an accompanying issue.

### 8. Fast Feedback Loop
- Keep unit tests fast to enable quick local iteration. Developers should be able to run relevant tests locally before pushing.
- Recommended local command: `pytest -q` or a narrowed `pytest tests/path/to:test_name`.

### 9. Test Data and Fixtures
- Use fixtures, factories, and minimal real data. Avoid brittle reliance on external services or on specific file paths.

### 10. Code Review and Acceptance
- Every PR must include tests demonstrating the behavior and reviewers must verify the tests are meaningful and sufficient.

### 11. Refactor Safely
- After making tests pass, refactor code and tests for clarity and maintainability while keeping all tests green.

### 12. Documentation
- Document how to run tests and the project's testing conventions in the project README or a `CONTRIBUTING.md`.

## Governance
- This constitution is the default testing policy for Python code in this repository. Amendments must be documented and agreed by maintainers.

**Version**: 1.0 | **Ratified**: [2026-02-03] | **Last Amended**: [2026-02-3]
