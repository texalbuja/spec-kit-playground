"""Pyramid printer utility.

Provides `build_pyramid(rows)` that returns a string and a CLI entrypoint.
"""

from __future__ import annotations

def build_pyramid(rows: int) -> str:
    if not isinstance(rows, int):
        raise TypeError("rows must be an integer")
    if rows <= 0:
        raise ValueError("rows must be a positive integer")
    lines = []
    for i in range(1, rows + 1):
        stars = "*" * (2 * i - 1)
        spaces = " " * (rows - i)
        lines.append(f"{spaces}{stars}{spaces}")
    return "\n".join(lines)


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description="Print a pyramid of stars to the console")
    parser.add_argument("-n", "--rows", type=int, default=5, help="Number of pyramid rows (positive integer)")
    args = parser.parse_args()
    try:
        output = build_pyramid(args.rows)
    except (TypeError, ValueError) as e:
        parser.error(str(e))
    print(output)


if __name__ == "__main__":
    main()
