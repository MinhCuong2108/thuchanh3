# Kết quả chạy kiểm thử

**Lệnh:** `python3 -m unittest discover -s tests -v`

**Kết quả:**

```
Ran 115 tests in 0.004s

OK
```

## Tóm tắt

| Metric | Value |
|---|---|
| Tổng số tests | 115 |
| Passed | 115 |
| Failed | 0 |
| Errors | 0 |
| Skipped | 0 |
| Thời gian chạy | 0.004s |

## Phân bố

| Nhóm | Số tests |
|---|---|
| Issue #1 — valid (test_valid.py) | 62 |
| Issue #2 — invalid + boundary (test_invalid.py) | 53 |
| **Tổng** | **115** |

## Phân bố theo bài

| Bài | Valid | Invalid | Tổng |
|---|---|---|---|
| 1+2 (rectangle) | 12 | 9 | 21 |
| 3 (quadratic) | 6 | 7 | 13 |
| 4 (days_in_month) | 9 | 8 | 17 |
| 5 (is_prime) | 10 | 8 | 18 |
| 6 (alternating_sum) | 9 | 6 | 15 |
| 7 (gcd) | 9 | 5 | 14 |
| 8 (factorial + factorial_sum) | 7 + 6 | 5 + 5 | 23 |

## Output chi tiết (tail)

```
test_perimeter_integer_dimensions (tests.test_valid.RectangleValidTests.test_perimeter_integer_dimensions) ... ok
test_perimeter_large_dimensions (tests.test_valid.RectangleValidTests.test_perimeter_large_dimensions) ... ok
test_perimeter_smallest_valid_boundary (tests.test_valid.RectangleValidTests.test_perimeter_smallest_valid_boundary) ... ok
test_perimeter_square_length_equals_width (tests.test_valid.RectangleValidTests.test_perimeter_square_length_equals_width) ... ok
test_perimeter_typical_positive (tests.test_valid.RectangleValidTests.test_perimeter_typical_positive) ... ok

----------------------------------------------------------------------
Ran 115 tests in 0.004s

OK
```
