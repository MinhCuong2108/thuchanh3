"""Compute n! (factorial of n)."""

from numbers import Integral


def factorial(n: int) -> int:
    """Return n! for non-negative integer n.

    0! is defined as 1.

    Args:
        n: non-negative integer.

    Returns:
        n! as int.

    Raises:
        ValueError: if n < 0 or n is not an integer.
    """
    if not isinstance(n, Integral) or isinstance(n, bool):
        raise ValueError(f"n must be an integer, got {type(n).__name__}")
    n = int(n)
    if n < 0:
        raise ValueError(f"n must be >= 0, got {n}")
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result
