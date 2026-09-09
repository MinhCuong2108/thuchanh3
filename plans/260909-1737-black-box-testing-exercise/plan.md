# Plan: Bài thực hành Kiểm thử hộp đen

## Overview
- **Priority**: High (academic submission)
- **Stack**: Python 3.12 + `unittest` (built-in, no install needed)
- **Repo**: `https://github.com/MinhCuong2108/thuchanh3.git`
- **Branch**: `main`

## Exercises (8 functions)
| # | Function | Module |
|---|---|---|
| 1 + 2 | perimeter + area of rectangle | `src/rectangle.py` |
| 3 | Solve quadratic equation ax² + bx + c = 0 | `src/quadratic.py` |
| 4 | Days in month (leap year handling) | `src/days_in_month.py` |
| 5 | Check if n is prime | `src/is_prime.py` |
| 6 | Alternating sum S = 1 - 2 + 3 - 4 + ... + n | `src/alternating_sum.py` |
| 7 | GCD of a and b (Euclid) | `src/gcd.py` |
| 8 | Sum of factorials S = 1! + 2! + ... + n! | `src/factorial_sum.py` + `src/factorial.py` |

## Structure
```
thuchanh3/
├── src/
│   ├── rectangle.py
│   ├── quadratic.py
│   ├── days_in_month.py
│   ├── is_prime.py
│   ├── alternating_sum.py
│   ├── gcd.py
│   ├── factorial.py            # helper for #8
│   └── factorial_sum.py
├── tests/
│   ├── test_valid.py            # Issue #1: valid equivalence classes
│   └── test_invalid.py          # Issue #2: invalid + boundary
├── docs/
│   ├── black-box-approach.md    # mô tả áp dụng
│   ├── test-cases.md            # danh sách test cases
│   └── test-results.md          # output unittest
├── README.md
└── .gitignore
```

## Black-box Testing Coverage per Exercise
For each function:
- **Equivalence partitioning**: identify input classes (valid/invalid)
- **Boundary value analysis**: test min/max/at-boundary values
- **Invalid data**: at least 1 invalid case per exercise

## GitHub Workflow
1. **Issue #1**: "Thiết kế và viết các ca kiểm thử hộp đen cho các trường hợp dữ liệu hợp lệ"
2. **Issue #2**: "Thiết kế và viết các ca kiểm thử hộp đen cho dữ liệu không hợp lệ, biên và ngoại lệ"
3. **Commit #1** closes Issue #1: source + valid tests + docs
4. **Commit #2** closes Issue #2: adds invalid tests

## Status
- [x] Environment check (Python 3.12 OK, unittest available)
- [x] Plan file created
- [ ] Implement source code (8 modules)
- [ ] Write valid tests (Issue #1)
- [ ] Write invalid + boundary tests (Issue #2)
- [ ] Run unittest, capture output
- [ ] Write README + docs
- [ ] Create GitHub issues
- [ ] Commit #1 (closes Issue #1)
- [ ] Commit #2 (closes Issue #2)
- [ ] Push to remote
