"""Compute S = 1! + 2! + 3! + ... + n! using factorial(n)."""

from numbers import Integral

from src.factorial import factorial


def factorial_sum(n: int) -> int:
    """Return S = 1! + 2! + 3! + ... + n!.

    For n == 0 the sum is 0 (empty sum).
    For n == 1 the sum is 1.

    Args:
        n: non-negative integer.

    Returns:
        The sum as int.

    Raises:
        ValueError: if n < 0 or n is not an integer.
    """
    if not isinstance(n, Integral) or isinstance(n, bool):
        raise ValueError(f"n must be an integer, got {type(n).__name__}")
    n = int(n)
    if n < 0:
        raise ValueError(f"n must be >= 0, got {n}")
    return sum(factorial(k) for k in range(1, n + 1))
