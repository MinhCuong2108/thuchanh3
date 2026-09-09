"""Compute alternating sum S = 1 - 2 + 3 - 4 + ... + n."""

from numbers import Integral


def alternating_sum(n: int) -> int:
    """Return alternating sum 1 - 2 + 3 - 4 + ... + n.

    For n == 0 the sum is 0 (empty sum).
    For n >= 1, sign of term k is + when k is odd, - when k is even.

    Args:
        n: non-negative integer.

    Returns:
        The alternating sum as int.

    Raises:
        ValueError: if n < 0 or n is not an integer.
    """
    if not isinstance(n, Integral) or isinstance(n, bool):
        raise ValueError(f"n must be an integer, got {type(n).__name__}")
    n = int(n)
    if n < 0:
        raise ValueError(f"n must be >= 0, got {n}")
    # closed form: if n is even -> -n/2; if n is odd  -> (n+1)/2
    if n % 2 == 0:
        return -n // 2
    return (n + 1) // 2
