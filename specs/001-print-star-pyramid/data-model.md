# Data Model: Print Star Pyramid

Entities:

- Rows
  - type: integer
  - constraints: positive (> 0)
  - source: CLI argument `--rows` or default value (5)

- Pyramid Output
  - type: multiline string
  - content: rows lines with centered `*` characters
  - representation: returned by `build_pyramid(rows)` and printed by CLI

Validation rules:
- `rows` must be an integer and > 0; non-integer or non-positive values produce an error.

State transitions: N/A — deterministic pure function mapping `rows` -> `output`.
