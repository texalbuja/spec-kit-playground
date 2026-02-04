```markdown
# Feature Specification: Print Star Pyramid

**Feature Branch**: `001-print-star-pyramid`  
**Created**: 2026-02-03  
**Status**: Draft  
**Input**: User description: "Build an application that prints in the console a pyramid with stars"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Print pyramid to console (Priority: P1)

An end user wants a small command-line utility that prints a visually centered pyramid made of `*` characters to the console for a given number of rows.

**Why this priority**: This is the core feature requested and provides immediate visible value.

**Independent Test**: Run the program with `--rows 3` and verify the console output matches the expected pyramid shape.

**Acceptance Scenarios**:

1. **Given** the program is run without arguments, **When** it runs, **Then** it prints a pyramid with a sensible default number of rows (assumed 5).
2. **Given** the program is run with `--rows N`, **When** it runs, **Then** it prints a pyramid with exactly `N` rows, centered horizontally.
3. **Given** an invalid `--rows` value (e.g., zero or negative), **When** it runs, **Then** it prints a helpful error and exits non-zero.

---

### Edge Cases

- If `N` is 1, output is a single `*` with no surrounding spaces.
- If `N` is large (e.g., > 200), behavior should still be correct; performance should be reasonable for typical CLI usage.
- Non-integer inputs result in a parse error with clear message.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The program MUST print a centered pyramid of `*` characters with a configurable number of rows.
- **FR-002**: The program MUST accept a command-line argument `--rows` (or `-n`) to set the number of rows; default is 5.
- **FR-003**: The program MUST validate `--rows` is a positive integer and exit with an error for invalid values.
- **FR-004**: The program MUST produce deterministic output (no trailing extra blank lines beyond the pyramid block).
- **FR-005**: The program MUST expose a programmatic function (e.g., `build_pyramid(rows)`) that returns the pyramid as a string to enable unit testing.

### Key Entities

- **Rows**: Integer input controlling pyramid height.
- **Pyramid output**: Text block composed of spaces and `*` characters arranged in centered rows.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can run the program and see a correctly centered pyramid for `N=3` that matches the expected ASCII layout (testable in unit tests).
- **SC-002**: Default run (no args) prints a pyramid of 5 rows within 1 second on a typical developer machine.
- **SC-003**: Input validation prevents non-positive integers; error exit code present and an explanatory message is shown.

## Assumptions

- Default number of rows is 5 unless the user supplies `--rows`.
- The pyramid is printed using ASCII `*` and space characters only.

## Testing

- Unit tests will call the `build_pyramid(rows)` function and assert exact output for small values (e.g., 1, 3, 5).
- Integration test will run the CLI entrypoint and capture stdout to verify printed output matches the unit-tested string.

## Deliverables

- `src/pyramid.py` implementing `build_pyramid(rows)` and a CLI entrypoint.
- `tests/test_pyramid.py` with unit and CLI tests.

```
