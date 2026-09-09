"""Black-box tests for INVALID data, BOUNDARY violations and EXCEPTIONS (Issue #2).

Strategy:
  - Boundary value analysis: test just-outside valid range
    (e.g. month = 0, month = 13, n = -1, year = 0).
  - Invalid data types: None, strings, lists, dicts, booleans (where type
    discipline matters).
  - Program-handling observation: assertRaises for expected errors, and
    direct assertions for functions that return a well-defined value for
    "edge" inputs (e.g. is_prime(-5) -> False).
"""

import math
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
# Exercises 1 & 2: Rectangle — invalid dimensions
# ---------------------------------------------------------------------------

class RectangleInvalidTests(unittest.TestCase):

    def test_zero_length_invalid(self):
        with self.assertRaises(ValueError):
            perimeter(0, 5)

    def test_zero_width_invalid(self):
        with self.assertRaises(ValueError):
            area(5, 0)

    def test_negative_length_invalid(self):
        with self.assertRaises(ValueError):
            perimeter(-1, 5)

    def test_negative_width_invalid(self):
        with self.assertRaises(ValueError):
            area(5, -3.5)

    def test_none_length_invalid(self):
        with self.assertRaises(ValueError):
            perimeter(None, 5)

    def test_string_length_invalid(self):
        with self.assertRaises(ValueError):
            perimeter("5", 3)

    def test_list_length_invalid(self):
        with self.assertRaises(ValueError):
            perimeter([5], 3)

    def test_bool_length_invalid(self):
        # bool is technically int subclass but is rejected explicitly
        with self.assertRaises(ValueError):
            perimeter(True, 3)

    def test_complex_number_invalid(self):
        with self.assertRaises(ValueError):
            perimeter(complex(1, 2), 3)


# ---------------------------------------------------------------------------
# Exercise 3: Quadratic — degenerate + invalid
# ---------------------------------------------------------------------------

class QuadraticInvalidTests(unittest.TestCase):

    def test_zero_zero_zero_raises(self):
        # 0*x^2 + 0*x + 0 = 0 -> degenerate, infinite solutions
        with self.assertRaises(ValueError):
            solve_quadratic(0, 0, 0)

    def test_zero_zero_nonzero_raises(self):
        # 0*x^2 + 0*x + 5 = 0 -> no solution
        with self.assertRaises(ValueError):
            solve_quadratic(0, 0, 5)

    def test_non_numeric_a_raises(self):
        with self.assertRaises(ValueError):
            solve_quadratic("1", 2, 3)

    def test_non_numeric_b_raises(self):
        with self.assertRaises(ValueError):
            solve_quadratic(1, None, 3)

    def test_non_numeric_c_raises(self):
        with self.assertRaises(ValueError):
            solve_quadratic(1, 2, [3])

    def test_negative_discriminant_returns_complex(self):
        # x^2 + x + 1 = 0 -> D = 1 - 4 = -3 < 0
        roots = solve_quadratic(1, 1, 1)
        self.assertEqual(len(roots), 2)
        # both roots must be complex (have non-zero imaginary part)
        self.assertTrue(any(isinstance(r, complex) and r.imag != 0 for r in roots))
        # x^2 + x + 1 = 0 -> x = (-1 ± i*sqrt(3))/2
        x1, x2 = roots
        expected_real = -0.5
        self.assertAlmostEqual(x1.real, expected_real)
        self.assertAlmostEqual(x2.real, expected_real)
        self.assertAlmostEqual(abs(x1.imag), math.sqrt(3) / 2, places=6)
        self.assertAlmostEqual(abs(x2.imag), math.sqrt(3) / 2, places=6)

    def test_bool_a_invalid(self):
        with self.assertRaises(ValueError):
            solve_quadratic(True, -5, 6)


# ---------------------------------------------------------------------------
# Exercise 4: Days in month — out-of-range month/year
# ---------------------------------------------------------------------------

class DaysInMonthInvalidTests(unittest.TestCase):

    def test_month_zero_below_boundary(self):
        with self.assertRaises(ValueError):
            days_in_month(0, 2023)

    def test_month_thirteen_above_boundary(self):
        with self.assertRaises(ValueError):
            days_in_month(13, 2023)

    def test_month_negative_invalid(self):
        with self.assertRaises(ValueError):
            days_in_month(-1, 2023)

    def test_year_zero_below_boundary(self):
        with self.assertRaises(ValueError):
            days_in_month(2, 0)

    def test_year_negative_invalid(self):
        with self.assertRaises(ValueError):
            days_in_month(2, -100)

    def test_non_int_month_invalid(self):
        with self.assertRaises(ValueError):
            days_in_month(2.5, 2023)

    def test_non_int_year_invalid(self):
        with self.assertRaises(ValueError):
            days_in_month(2, "2023")

    def test_is_leap_year_bool_invalid(self):
        with self.assertRaises(ValueError):
            is_leap_year(True)


# ---------------------------------------------------------------------------
# Exercise 5: is_prime — invalid + boundary
# ---------------------------------------------------------------------------

class IsPrimeInvalidTests(unittest.TestCase):

    def test_zero_below_boundary(self):
        self.assertFalse(is_prime(0))

    def test_one_below_boundary(self):
        self.assertFalse(is_prime(1))

    def test_negative_one(self):
        self.assertFalse(is_prime(-1))

    def test_large_negative(self):
        self.assertFalse(is_prime(-100))

    def test_non_int_invalid(self):
        with self.assertRaises(ValueError):
            is_prime(3.5)

    def test_string_invalid(self):
        with self.assertRaises(ValueError):
            is_prime("7")

    def test_none_invalid(self):
        with self.assertRaises(ValueError):
            is_prime(None)

    def test_bool_invalid(self):
        with self.assertRaises(ValueError):
            is_prime(True)


# ---------------------------------------------------------------------------
# Exercise 6: alternating_sum — invalid + boundary
# ---------------------------------------------------------------------------

class AlternatingSumInvalidTests(unittest.TestCase):

    def test_negative_n_below_boundary(self):
        with self.assertRaises(ValueError):
            alternating_sum(-1)

    def test_large_negative_n(self):
        with self.assertRaises(ValueError):
            alternating_sum(-1000)

    def test_non_int_invalid(self):
        with self.assertRaises(ValueError):
            alternating_sum(5.5)

    def test_string_invalid(self):
        with self.assertRaises(ValueError):
            alternating_sum("3")

    def test_none_invalid(self):
        with self.assertRaises(ValueError):
            alternating_sum(None)

    def test_bool_invalid(self):
        with self.assertRaises(ValueError):
            alternating_sum(True)


# ---------------------------------------------------------------------------
# Exercise 7: gcd — invalid types
# ---------------------------------------------------------------------------

class GcdInvalidTests(unittest.TestCase):

    def test_non_int_a_invalid(self):
        with self.assertRaises(ValueError):
            gcd(1.5, 2)

    def test_non_int_b_invalid(self):
        with self.assertRaises(ValueError):
            gcd(1, "2")

    def test_none_a_invalid(self):
        with self.assertRaises(ValueError):
            gcd(None, 2)

    def test_list_a_invalid(self):
        with self.assertRaises(ValueError):
            gcd([1, 2], 2)

    def test_bool_a_invalid(self):
        with self.assertRaises(ValueError):
            gcd(True, 2)


# ---------------------------------------------------------------------------
# Exercise 8: factorial / factorial_sum — invalid + boundary
# ---------------------------------------------------------------------------

class FactorialInvalidTests(unittest.TestCase):

    def test_factorial_negative_invalid(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_factorial_non_int_invalid(self):
        with self.assertRaises(ValueError):
            factorial(3.5)

    def test_factorial_string_invalid(self):
        with self.assertRaises(ValueError):
            factorial("5")

    def test_factorial_none_invalid(self):
        with self.assertRaises(ValueError):
            factorial(None)

    def test_factorial_bool_invalid(self):
        with self.assertRaises(ValueError):
            factorial(True)


class FactorialSumInvalidTests(unittest.TestCase):

    def test_factorial_sum_negative_invalid(self):
        with self.assertRaises(ValueError):
            factorial_sum(-1)

    def test_factorial_sum_non_int_invalid(self):
        with self.assertRaises(ValueError):
            factorial_sum(2.0)

    def test_factorial_sum_string_invalid(self):
        with self.assertRaises(ValueError):
            factorial_sum("3")

    def test_factorial_sum_none_invalid(self):
        with self.assertRaises(ValueError):
            factorial_sum(None)

    def test_factorial_sum_bool_invalid(self):
        with self.assertRaises(ValueError):
            factorial_sum(False)


if __name__ == "__main__":
    unittest.main(verbosity=2)
