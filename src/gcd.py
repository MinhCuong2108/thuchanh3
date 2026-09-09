"""Compute GCD (Greatest Common Divisor) via the Euclidean algorithm."""

from numbers import Integral


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of a and b.

    Always returns a non-negative integer. gcd(0, 0) is defined as 0.

    Args:
        a, b: integers.

    Returns:
        Non-negative int.

    Raises:
        ValueError: if a or b is not an integer.
    """
    if not isinstance(a, Integral) or isinstance(a, bool):
        raise ValueError(f"a must be an integer, got {type(a).__name__}")
    if not isinstance(b, Integral) or isinstance(b, bool):
        raise ValueError(f"b must be an integer, got {type(b).__name__}")
    a, b = abs(int(a)), abs(int(b))
    while b:
        a, b = b, a % b
    return a
