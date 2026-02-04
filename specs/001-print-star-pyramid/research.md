# Research: Print Star Pyramid

Decision: Use Python (current project language) and `pytest` for testing.

Rationale: The repository is already Python-based with `pytest` tests and a `requirements-dev.txt`. Implementing the CLI and library function in Python minimizes friction and leverages existing CI/test conventions from the project's constitution.

Alternatives considered:
- Implement in another language (Node/Rust) — rejected due to added toolchain and CI complexity.
- Add third-party formatting libraries — rejected because requirements are simple ASCII output.
