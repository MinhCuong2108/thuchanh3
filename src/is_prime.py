"""Check whether an integer is prime."""

from numbers import Integral


def is_prime(n: int) -> bool:
    """Return True iff n is a prime number.

    Definition: a prime is an integer > 1 with no positive divisors other
    than 1 and itself. Negative numbers, 0, and 1 are NOT prime.

    Args:
        n: integer to test.

    Returns:
        bool.

    Raises:
        ValueError: if n is not an integer.
    """
    if not isinstance(n, Integral) or isinstance(n, bool):
        raise ValueError(f"n must be an integer, got {type(n).__name__}")
    n = int(n)
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    # trial division up to sqrt(n); only odd divisors
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
