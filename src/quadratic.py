"""Solve quadratic equation a*x^2 + b*x + c = 0.

Handles three regimes:
  1. a == 0  -> linear equation b*x + c = 0.
  2. a != 0, discriminant >  0 -> two distinct real roots.
  3. a != 0, discriminant == 0 -> one real root (double).
  4. a != 0, discriminant <  0 -> two complex conjugate roots.

Raises ValueError for degenerate equations (a == b == 0).
"""

import cmath
import math
from numbers import Real


def _validate_coef(name: str, value: Real) -> float:
    if not isinstance(value, Real) or isinstance(value, bool):
        raise ValueError(f"{name} must be a real number, got {type(value).__name__}")
    return float(value)


def solve_quadratic(a: Real, b: Real, c: Real) -> tuple:
    """Return roots of a*x^2 + b*x + c = 0.

    Returns:
        Tuple of two complex numbers (real roots when discriminant >= 0).
        When discriminant == 0, both entries of the tuple are equal (real).
        When a == 0 and b != 0, returns tuple (x,) with single real root.

    Raises:
        ValueError: if a == 0 and b == 0 (degenerate equation).
    """
    a = _validate_coef("a", a)
    b = _validate_coef("b", b)
    c = _validate_coef("c", c)

    if a == 0:
        if b == 0:
            if c == 0:
                raise ValueError("Degenerate equation 0=0, infinite solutions")
            raise ValueError(f"Inconsistent equation {c}=0, no solution")
        # Linear case
        return (-c / b,)

    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        sd = cmath.sqrt(discriminant)
        x1 = (-b + sd) / (2 * a)
        x2 = (-b - sd) / (2 * a)
        return (x1, x2)
    if discriminant == 0:
        x = -b / (2.0 * a)
        return (x, x)
    sd = math.sqrt(discriminant)
    x1 = (-b + sd) / (2.0 * a)
    x2 = (-b - sd) / (2.0 * a)
    return (x1, x2)
