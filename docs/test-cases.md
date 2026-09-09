# Danh sách Test Cases

Tổng cộng **115 test cases** cho 8 bài toán, chia thành 2 nhóm theo 2 issues trên GitHub.

## Issue #1 — Dữ liệu hợp lệ (`tests/test_valid.py`)

### Bài 1+2: Chu vi & diện tích hình chữ nhật
| # | Test | Input | Expected |
|---|---|---|---|
| 1 | perimeter typical | (5, 3) | 16.0 |
| 2 | perimeter integer | (10, 4) | 28.0 |
| 3 | perimeter float | (2.5, 1.5) | 8.0 |
| 4 | perimeter smallest valid | (sys.float_info.min, sys.float_info.min) | 2 × min |
| 5 | perimeter large | (1e9, 1e9) | 4e9 |
| 6 | perimeter square | (7, 7) | 28.0 |
| 7 | area typical | (5, 3) | 15.0 |
| 8 | area integer | (12, 8) | 96.0 |
| 9 | area float | (2.5, 4.0) | 10.0 |
| 10 | area smallest valid | (sys.float_info.min, sys.float_info.min) | min² |
| 11 | area large | (1e6, 1e6) | 1e12 |
| 12 | area square | (9, 9) | 81.0 |

### Bài 3: Phương trình bậc 2
| # | Test | Input (a,b,c) | Expected |
|---|---|---|---|
| 13 | two distinct real roots | (1, -5, 6) | (2.0, 3.0) |
| 14 | one double real root | (1, -4, 4) | (2.0, 2.0) |
| 15 | linear root when a=0 | (0, 2, -6) | (3.0,) |
| 16 | negative coefficients | (-1, 4, -3) | (1.0, 3.0) |
| 17 | zero constant term | (1, -4, 0) | (0.0, 4.0) |
| 18 | fractional coefficients | (0.5, -1, 0.5) | (1.0, 1.0) |

### Bài 4: Số ngày của tháng
| # | Test | Input (m,y) | Expected |
|---|---|---|---|
| 19 | January (31) | (1, 2023) | 31 |
| 20 | December (31, biên trên) | (12, 2023) | 31 |
| 21 | April (30) | (4, 2023) | 30 |
| 22 | November (30) | (11, 2023) | 30 |
| 23 | February non-leap | (2, 2023) | 28 |
| 24 | February leap | (2, 2024) | 29 |
| 25 | February century non-leap | (2, 1900) | 28 |
| 26 | February quadricentennial leap | (2, 2000) | 29 |
| 27 | is_leap_year helper (4 cases) | — | boolean |

### Bài 5: Số nguyên tố
| # | Test | Input | Expected |
|---|---|---|---|
| 28 | smallest prime | 2 | True |
| 29 | prime | 3 | True |
| 30 | prime | 5 | True |
| 31 | prime | 7 | True |
| 32 | prime | 13 | True |
| 33 | prime large | 7919 | True |
| 34 | composite | 4 | False |
| 35 | composite | 9 | False |
| 36 | composite | 15 | False |
| 37 | composite | 100 | False |

### Bài 6: Tổng đan dấu
| # | Test | Input | Expected |
|---|---|---|---|
| 38 | empty sum | 0 | 0 |
| 39 | n=1 | 1 | 1 |
| 40 | n=2 | 2 | -1 |
| 41 | n=3 | 3 | 2 |
| 42 | n=4 | 4 | -2 |
| 43 | n=5 | 5 | 3 |
| 44 | n=6 | 6 | -3 |
| 45 | n=20 (lớn, chẵn) | 20 | -10 |
| 46 | n=21 (lớn, lẻ) | 21 | 11 |

### Bài 7: UCLN
| # | Test | Input (a,b) | Expected |
|---|---|---|---|
| 47 | coprime | (17, 13) | 1 |
| 48 | typical | (48, 18) | 6 |
| 49 | one divides other | (100, 25) | 25 |
| 50 | (0, n) | (0, 5) | 5 |
| 51 | (n, 0) | (7, 0) | 7 |
| 52 | (0, 0) | (0, 0) | 0 |
| 53 | negative a | (-12, 8) | 4 |
| 54 | both negative | (-12, -8) | 4 |
| 55 | swapped | (18, 48) | 6 |

### Bài 8: Tổng giai thừa
| # | Test | Input | Expected |
|---|---|---|---|
| 56 | factorial 0 | 0 | 1 |
| 57 | factorial 1 | 1 | 1 |
| 58 | factorial 2 | 2 | 2 |
| 59 | factorial 3 | 3 | 6 |
| 60 | factorial 4 | 4 | 24 |
| 61 | factorial 5 | 5 | 120 |
| 62 | factorial_sum n=0 | 0 | 0 |
| 63 | factorial_sum n=1 | 1 | 1 |
| 64 | factorial_sum n=2 | 2 | 3 |
| 65 | factorial_sum n=3 | 3 | 9 |
| 66 | factorial_sum n=4 | 4 | 33 |
| 67 | factorial_sum n=5 | 5 | 153 |

## Issue #2 — Dữ liệu không hợp lệ + biên + ngoại lệ (`tests/test_invalid.py`)

### Bài 1+2: Hình chữ nhật — invalid
| # | Test | Input | Expected behavior |
|---|---|---|---|
| 68 | length = 0 | perimeter(0, 5) | raises ValueError |
| 69 | width = 0 | area(5, 0) | raises ValueError |
| 70 | length < 0 | perimeter(-1, 5) | raises ValueError |
| 71 | width < 0 | area(5, -3.5) | raises ValueError |
| 72 | length = None | perimeter(None, 5) | raises ValueError |
| 73 | length = string | perimeter("5", 3) | raises ValueError |
| 74 | length = list | perimeter([5], 3) | raises ValueError |
| 75 | length = bool | perimeter(True, 3) | raises ValueError |
| 76 | length = complex | perimeter(complex(1,2), 3) | raises ValueError |

### Bài 3: Phương trình bậc 2 — invalid
| # | Test | Input | Expected behavior |
|---|---|---|---|
| 77 | a=b=c=0 (degenerate) | (0, 0, 0) | raises ValueError |
| 78 | a=b=0, c≠0 (no solution) | (0, 0, 5) | raises ValueError |
| 79 | non-numeric a | ("1", 2, 3) | raises ValueError |
| 80 | non-numeric b | (1, None, 3) | raises ValueError |
| 81 | non-numeric c | (1, 2, [3]) | raises ValueError |
| 82 | bool a | (True, -5, 6) | raises ValueError |
| 83 | negative discriminant | (1, 1, 1) | complex roots (-0.5 ± i·√3/2) |

### Bài 4: Số ngày — invalid
| # | Test | Input | Expected behavior |
|---|---|---|---|
| 84 | month = 0 (dưới biên) | (0, 2023) | raises ValueError |
| 85 | month = 13 (trên biên) | (13, 2023) | raises ValueError |
| 86 | month < 0 | (-1, 2023) | raises ValueError |
| 87 | year = 0 | (2, 0) | raises ValueError |
| 88 | year < 0 | (2, -100) | raises ValueError |
| 89 | month là float | (2.5, 2023) | raises ValueError |
| 90 | year là string | (2, "2023") | raises ValueError |
| 91 | is_leap_year với bool | True | raises ValueError |

### Bài 5: is_prime — invalid
| # | Test | Input | Expected behavior |
|---|---|---|---|
| 92 | n = 0 (dưới biên) | 0 | False (không phải nguyên tố) |
| 93 | n = 1 (dưới biên) | 1 | False |
| 94 | n = -1 | -1 | False |
| 95 | n = -100 | -100 | False |
| 96 | n là float | 3.5 | raises ValueError |
| 97 | n là string | "7" | raises ValueError |
| 98 | n = None | None | raises ValueError |
| 99 | n là bool | True | raises ValueError |

### Bài 6: alternating_sum — invalid
| # | Test | Input | Expected behavior |
|---|---|---|---|
| 100 | n = -1 | -1 | raises ValueError |
| 101 | n = -1000 | -1000 | raises ValueError |
| 102 | n là float | 5.5 | raises ValueError |
| 103 | n là string | "3" | raises ValueError |
| 104 | n = None | None | raises ValueError |
| 105 | n là bool | True | raises ValueError |

### Bài 7: gcd — invalid
| # | Test | Input | Expected behavior |
|---|---|---|---|
| 106 | a là float | (1.5, 2) | raises ValueError |
| 107 | b là string | (1, "2") | raises ValueError |
| 108 | a = None | (None, 2) | raises ValueError |
| 109 | a là list | ([1, 2], 2) | raises ValueError |
| 110 | a là bool | (True, 2) | raises ValueError |

### Bài 8: factorial / factorial_sum — invalid
| # | Test | Input | Expected behavior |
|---|---|---|---|
| 111 | factorial(-1) | -1 | raises ValueError |
| 112 | factorial(3.5) | 3.5 | raises ValueError |
| 113 | factorial("5") | "5" | raises ValueError |
| 114 | factorial(None) | None | raises ValueError |
| 115 | factorial(True) | True | raises ValueError |
| (bonus) | factorial_sum(-1) | -1 | raises ValueError |
| (bonus) | factorial_sum(2.0) | 2.0 | raises ValueError |
| (bonus) | factorial_sum("3") | "3" | raises ValueError |
| (bonus) | factorial_sum(None) | None | raises ValueError |
| (bonus) | factorial_sum(False) | False | raises ValueError |
