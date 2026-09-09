"""Rectangle utilities: perimeter and area.

Both functions accept length and width as numbers (int or float).
They raise ValueError for non-positive dimensions or non-numeric inputs.
"""

from numbers import Real


def _validate_side(name: str, value: Real) -> float:
    """Internal helper: ensure value is a positive real number."""
    if not isinstance(value, Real) or isinstance(value, bool):
        raise ValueError(f"{name} must be a real number, got {type(value).__name__}")
    value = float(value)
    if value <= 0:
        raise ValueError(f"{name} must be > 0, got {value}")
    return value


def perimeter(length: Real, width: Real) -> float:
    """Compute perimeter of a rectangle: P = 2 * (length + width).

    Args:
        length: length of rectangle (> 0).
        width:  width of rectangle (> 0).

    Returns:
        Perimeter as float.

    Raises:
        ValueError: when length or width is non-positive or non-numeric.
    """
    L = _validate_side("length", length)
    W = _validate_side("width", width)
    return 2.0 * (L + W)


def area(length: Real, width: Real) -> float:
    """Compute area of a rectangle: A = length * width.

    Args:
        length: length of rectangle (> 0).
        width:  width of rectangle (> 0).

    Returns:
        Area as float.

    Raises:
        ValueError: when length or width is non-positive or non-numeric.
    """
    L = _validate_side("length", length)
    W = _validate_side("width", width)
    return L * W
