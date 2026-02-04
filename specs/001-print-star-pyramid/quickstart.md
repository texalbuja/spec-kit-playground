# Quickstart: Print Star Pyramid

Run locally (use project's Python environment):

```bash
# run tests
PYTHONPATH=. pytest -q

# run program with default 5 rows
python -m src.pyramid

# run program with 3 rows
python -m src.pyramid --rows 3
```

Notes:
- Tests call `build_pyramid(rows)` for exact-output assertions and the CLI module for integration checks.
