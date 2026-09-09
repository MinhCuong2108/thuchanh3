"""Black-box tests for VALID data (Issue #1).

Strategy: equivalence partitioning + boundary value analysis on VALID classes.
Each test exercises one equivalence class with representative values, including
boundary points at the lower and upper ends of valid input ranges.
"""

import math
import sys
import unittest

from src.alternating_sum import alternating_sum
from src.days_in_month import days_in_month, is_leap_year
from src.factorial import factorial
from src.factorial_sum import factorial_sum
from src.gcd import gcd
from src.is_prime import is_prime
from src.quadratic import solve_quadratic
from src.rectangle import area, perimeter


# ---------------------------------------------------------------------------
# Exercises 1 & 2: Rectangle — perimeter and area
# Valid equivalence classes:
#   - typical positive real (e.g. 5.0, 3.0)
#   - integer dimensions
#   - small positive floats near lower bound
#   - large positive floats near upper bound
#   - square (length == width)
#   - very large dimensions
# ---------------------------------------------------------------------------

class RectangleValidTests(unittest.TestCase):

    def test_perimeter_typical_positive(self):
        self.assertAlmostEqual(perimeter(5, 3), 16.0)

    def test_perimeter_integer_dimensions(self):
        self.assertAlmostEqual(perimeter(10, 4), 28.0)

    def test_perimeter_float_dimensions(self):
        self.assertAlmostEqual(perimeter(2.5, 1.5), 8.0)

    def test_perimeter_smallest_valid_boundary(self):
        # smallest representable positive float > 0
        tiny = sys_float_min()
        self.assertAlmostEqual(perimeter(tiny, tiny), 2 * tiny, places=20)

    def test_perimeter_large_dimensions(self):
        self.assertAlmostEqual(perimeter(1e9, 1e9), 4e9)

    def test_perimeter_square_length_equals_width(self):
        self.assertAlmostEqual(perimeter(7, 7), 28.0)

    def test_area_typical_positive(self):
        self.assertAlmostEqual(area(5, 3), 15.0)

    def test_area_integer_dimensions(self):
        self.assertAlmostEqual(area(12, 8), 96.0)

    def test_area_float_dimensions(self):
        self.assertAlmostEqual(area(2.5, 4.0), 10.0)

    def test_area_smallest_valid_boundary(self):
        tiny = sys_float_min()
        self.assertAlmostEqual(area(tiny, tiny), tiny * tiny, places=30)

    def test_area_large_dimensions(self):
        self.assertAlmostEqual(area(1e6, 1e6), 1e12)

    def test_area_square_length_equals_width(self):
        self.assertAlmostEqual(area(9, 9), 81.0)


def sys_float_min() -> float:
    return sys.float_info.min


# ---------------------------------------------------------------------------
# Exercise 3: Solve quadratic equation a*x^2 + b*x + c = 0
# Valid equivalence classes:
#   - a != 0, discriminant > 0 -> 2 distinct real roots
#   - a != 0, discriminant == 0 -> 1 real double root
#   - a == 0, b != 0 -> 1 linear root
# ---------------------------------------------------------------------------

class QuadraticValidTests(unittest.TestCase):

    def test_two_distinct_real_roots(self):
        # x^2 - 5x + 6 = 0 -> roots 2 and 3
        roots = solve_quadratic(1, -5, 6)
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0] + roots[1], 5.0)
        self.assertAlmostEqual(roots[0] * roots[1], 6.0)
        self.assertAlmostEqual(min(roots), 2.0)
        self.assertAlmostEqual(max(roots), 3.0)

    def test_one_double_real_root(self):
        # x^2 - 4x + 4 = (x-2)^2 -> root 2
        roots = solve_quadratic(1, -4, 4)
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], 2.0)
        self.assertAlmostEqual(roots[1], 2.0)

    def test_linear_root_when_a_zero(self):
        # 0*x^2 + 2x - 6 = 0 -> x = 3
        roots = solve_quadratic(0, 2, -6)
        self.assertEqual(len(roots), 1)
        self.assertAlmostEqual(roots[0], 3.0)

    def test_negative_coefficients(self):
        # -x^2 + 4x - 3 = 0 -> x^2 - 4x + 3 = 0 -> roots 1 and 3
        roots = solve_quadratic(-1, 4, -3)
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(min(roots), 1.0)
        self.assertAlmostEqual(max(roots), 3.0)

    def test_zero_constant_term(self):
        # x^2 - 4x = x(x-4) = 0 -> roots 0 and 4
        roots = solve_quadratic(1, -4, 0)
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(min(roots), 0.0)
        self.assertAlmostEqual(max(roots), 4.0)

    def test_fractional_coefficients(self):
        # (1/2)x^2 - x + 1/2 = 0 -> x^2 - 2x + 1 = (x-1)^2 -> root 1
        roots = solve_quadratic(0.5, -1, 0.5)
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], 1.0)
        self.assertAlmostEqual(roots[1], 1.0)


# ---------------------------------------------------------------------------
# Exercise 4: Days in month
# Valid equivalence classes:
#   - months with 31 days (1, 3, 5, 7, 8, 10, 12)
#   - months with 30 days (4, 6, 9, 11)
#   - February in a non-leap year (28)
#   - February in a leap year (29)
# Boundary: month = 1, month = 12.
# ---------------------------------------------------------------------------

class DaysInMonthValidTests(unittest.TestCase):

    def test_31_day_month_january(self):
        self.assertEqual(days_in_month(1, 2023), 31)

    def test_31_day_month_december_boundary(self):
        self.assertEqual(days_in_month(12, 2023), 31)

    def test_30_day_month_april(self):
        self.assertEqual(days_in_month(4, 2023), 30)

    def test_30_day_month_november(self):
        self.assertEqual(days_in_month(11, 2023), 30)

    def test_february_non_leap_year(self):
        self.assertEqual(days_in_month(2, 2023), 28)

    def test_february_leap_year_divisible_by_4(self):
        self.assertEqual(days_in_month(2, 2024), 29)

    def test_february_century_non_leap(self):
        # 1900 is divisible by 100 but not 400 -> not a leap year
        self.assertEqual(days_in_month(2, 1900), 28)

    def test_february_quadricentennial_leap(self):
        # 2000 is divisible by 400 -> leap year
        self.assertEqual(days_in_month(2, 2000), 29)

    def test_is_leap_year_helper(self):
        self.assertTrue(is_leap_year(2024))
        self.assertFalse(is_leap_year(2023))
        self.assertTrue(is_leap_year(2000))
        self.assertFalse(is_leap_year(1900))


# ---------------------------------------------------------------------------
# Exercise 5: is_prime(n)
# Valid equivalence classes:
#   - prime numbers
#   - composite numbers (> 1, not prime)
# Boundary values: 2 (smallest prime), 1 (not prime by definition).
# ---------------------------------------------------------------------------

class IsPrimeValidTests(unittest.TestCase):

    def test_smallest_prime_2(self):
        self.assertTrue(is_prime(2))

    def test_prime_3(self):
        self.assertTrue(is_prime(3))

    def test_prime_5(self):
        self.assertTrue(is_prime(5))

    def test_prime_7(self):
        self.assertTrue(is_prime(7))

    def test_prime_13(self):
        self.assertTrue(is_prime(13))

    def test_prime_large(self):
        self.assertTrue(is_prime(7919))  # known prime

    def test_composite_4(self):
        self.assertFalse(is_prime(4))

    def test_composite_9(self):
        self.assertFalse(is_prime(9))

    def test_composite_15(self):
        self.assertFalse(is_prime(15))

    def test_composite_100(self):
        self.assertFalse(is_prime(100))


# ---------------------------------------------------------------------------
# Exercise 6: alternating_sum(n) = 1 - 2 + 3 - 4 + ... + n
# Valid equivalence classes:
#   - n odd
#   - n even
# Boundary values: n = 0, n = 1.
# ---------------------------------------------------------------------------

class AlternatingSumValidTests(unittest.TestCase):

    def test_n_zero_empty_sum(self):
        self.assertEqual(alternating_sum(0), 0)

    def test_n_one_smallest_odd(self):
        self.assertEqual(alternating_sum(1), 1)

    def test_n_two_smallest_even(self):
        self.assertEqual(alternating_sum(2), -1)

    def test_n_three(self):
        self.assertEqual(alternating_sum(3), 2)

    def test_n_four(self):
        self.assertEqual(alternating_sum(4), -2)

    def test_n_five(self):
        self.assertEqual(alternating_sum(5), 3)

    def test_n_six(self):
        self.assertEqual(alternating_sum(6), -3)

    def test_n_twenty(self):
        # even, sum = -20/2 = -10
        self.assertEqual(alternating_sum(20), -10)

    def test_n_twenty_one(self):
        # odd, sum = (21+1)/2 = 11
        self.assertEqual(alternating_sum(21), 11)


# ---------------------------------------------------------------------------
# Exercise 7: gcd(a, b)
# Valid equivalence classes:
#   - both positive
#   - one zero, other non-zero (gcd = |other|)
#   - both zero (gcd = 0 by definition)
#   - one negative (function should return positive result)
#   - relatively prime
#   - one divides the other
# ---------------------------------------------------------------------------

class GcdValidTests(unittest.TestCase):

    def test_coprime(self):
        self.assertEqual(gcd(17, 13), 1)

    def test_typical(self):
        self.assertEqual(gcd(48, 18), 6)

    def test_one_divides_other(self):
        self.assertEqual(gcd(100, 25), 25)

    def test_zero_and_positive(self):
        self.assertEqual(gcd(0, 5), 5)

    def test_positive_and_zero(self):
        self.assertEqual(gcd(7, 0), 7)

    def test_both_zero(self):
        # by convention gcd(0, 0) = 0
        self.assertEqual(gcd(0, 0), 0)

    def test_negative_inputs(self):
        self.assertEqual(gcd(-12, 8), 4)

    def test_both_negative(self):
        self.assertEqual(gcd(-12, -8), 4)

    def test_swapped_arguments(self):
        self.assertEqual(gcd(18, 48), gcd(48, 18))


# ---------------------------------------------------------------------------
# Exercise 8: factorial_sum(n) = 1! + 2! + ... + n!  (uses factorial)
# Valid equivalence classes:
#   - n = 0 (empty sum)
#   - n = 1
#   - n >= 2
# ---------------------------------------------------------------------------

class FactorialSumValidTests(unittest.TestCase):

    def test_factorial_helper(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)

    def test_factorial_sum_n_zero_empty(self):
        self.assertEqual(factorial_sum(0), 0)

    def test_factorial_sum_n_one(self):
        self.assertEqual(factorial_sum(1), 1)

    def test_factorial_sum_n_two(self):
        # 1! + 2! = 1 + 2 = 3
        self.assertEqual(factorial_sum(2), 3)

    def test_factorial_sum_n_three(self):
        # 1! + 2! + 3! = 1 + 2 + 6 = 9
        self.assertEqual(factorial_sum(3), 9)

    def test_factorial_sum_n_four(self):
        # 1 + 2 + 6 + 24 = 33
        self.assertEqual(factorial_sum(4), 33)

    def test_factorial_sum_n_five(self):
        # 33 + 120 = 153
        self.assertEqual(factorial_sum(5), 153)


if __name__ == "__main__":
    unittest.main(verbosity=2)
