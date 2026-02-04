"""Simple Fibonacci implementation.

fib(n) returns the n-th Fibonacci number with the sequence starting at:
    fib(0) == 0
    fib(1) == 1

Behavior: raises ValueError for negative integers and TypeError for non-integers.
"""

def fib(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    import sys

    try:
        n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    except ValueError:
        print("Please provide an integer")
        sys.exit(2)
    print(fib(n))
