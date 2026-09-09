"""Return the number of days in a month, accounting for leap years.

Leap year rule (Gregorian):
  - divisible by 400, OR
  - divisible by 4 AND NOT divisible by 100.
"""

from numbers import Integral


def is_leap_year(year: int) -> bool:
    """Return True if `year` is a Gregorian leap year."""
    if not isinstance(year, Integral) or isinstance(year, bool):
        raise ValueError(f"year must be an integer, got {type(year).__name__}")
    year = int(year)
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def days_in_month(month: int, year: int) -> int:
    """Return number of days in `month` of `year`.

    Args:
        month: 1..12
        year:  any positive integer (year 0 and below raise ValueError)

    Returns:
        28, 29, 30 or 31.

    Raises:
        ValueError: if month is not 1..12 or year is not a positive integer.
    """
    if not isinstance(month, Integral) or isinstance(month, bool):
        raise ValueError(f"month must be an integer, got {type(month).__name__}")
    if not isinstance(year, Integral) or isinstance(year, bool):
        raise ValueError(f"year must be an integer, got {type(year).__name__}")
    month = int(month)
    year = int(year)
    if not (1 <= month <= 12):
        raise ValueError(f"month must be in 1..12, got {month}")
    if year < 1:
        raise ValueError(f"year must be >= 1, got {year}")

    days_per_month = {
        1: 31, 2: 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31,
        9: 30, 10: 31, 11: 30, 12: 31,
    }
    if month == 2 and is_leap_year(year):
        return 29
    return days_per_month[month]
