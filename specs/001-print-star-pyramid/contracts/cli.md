# CLI Contract: Print Star Pyramid

Usage:

`python -m src.pyramid [--rows N]`

Arguments:

- `-n`, `--rows` (optional): positive integer. Default: 5.

Behavior:

- On valid input, exit code 0 and print the pyramid text to stdout.
- On invalid input (non-integer, zero, negative), exit non-zero and print an error message to stderr via argparse.

Integration points:

- None external — pure CLI utility. Tests may invoke as module (`-m src.pyramid`) or call `build_pyramid(rows)` directly.
