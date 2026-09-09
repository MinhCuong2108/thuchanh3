# Bài thực hành: Kiểm thử hộp đen (Black-box Testing)

Repo thực hành kiểm thử hộp đen cho 8 bài toán. Mỗi bài áp dụng 3 kỹ thuật:
**phân lớp tương đương**, **phân tích giá trị biên**, và kiểm thử với **dữ liệu hợp lệ / không hợp lệ**.

## Nội dung

| # | Bài | Module |
|---|---|---|
| 1 | Tính chu vi hình chữ nhật | `src/rectangle.py` |
| 2 | Tính diện tích hình chữ nhật | `src/rectangle.py` |
| 3 | Giải phương trình bậc 2 | `src/quadratic.py` |
| 4 | Tính số ngày của một tháng (năm nhuận) | `src/days_in_month.py` |
| 5 | Kiểm tra n có phải số nguyên tố | `src/is_prime.py` |
| 6 | Tính tổng S = 1 − 2 + 3 − 4 + … + n | `src/alternating_sum.py` |
| 7 | Tìm UCLN của a và b | `src/gcd.py` |
| 8 | Tính tổng S = 1! + 2! + … + n! | `src/factorial_sum.py` + `src/factorial.py` |

## Cấu trúc

```
thuchanh3/
├── src/                      # mã nguồn
│   ├── rectangle.py
│   ├── quadratic.py
│   ├── days_in_month.py
│   ├── is_prime.py
│   ├── alternating_sum.py
│   ├── gcd.py
│   ├── factorial.py          # helper cho bài 8
│   └── factorial_sum.py
├── tests/                    # test cases
│   ├── test_valid.py         # Issue #1: dữ liệu hợp lệ
│   └── test_invalid.py       # Issue #2: dữ liệu không hợp lệ + biên
├── docs/
│   ├── black-box-approach.md # mô tả áp dụng black-box
│   ├── test-cases.md         # danh sách 115 test cases
│   └── test-results.md       # kết quả chạy test
└── README.md
```

## Chạy chương trình

```bash
python3 -c "
from src.rectangle import perimeter, area
from src.quadratic import solve_quadratic
from src.days_in_month import days_in_month
from src.is_prime import is_prime
from src.alternating_sum import alternating_sum
from src.gcd import gcd
from src.factorial_sum import factorial_sum

print('perimeter(3,4) =', perimeter(3, 4))           # 14.0
print('area(3,4) =', area(3, 4))                       # 12.0
print('roots of x^2-5x+6 =', solve_quadratic(1, -5, 6))  # (3.0, 2.0)
print('days in Feb 2024 =', days_in_month(2, 2024))   # 29
print('is_prime(7) =', is_prime(7))                   # True
print('alternating_sum(5) =', alternating_sum(5))     # 3
print('gcd(48,18) =', gcd(48, 18))                    # 6
print('factorial_sum(3) =', factorial_sum(3))         # 9
"
```

## Chạy test

```bash
python3 -m unittest discover -s tests -v
```

**Kết quả:** 115/115 tests pass.

## Tài liệu

- [`docs/black-box-approach.md`](docs/black-box-approach.md) — mô tả cách áp dụng 3 kỹ thuật black-box cho từng bài
- [`docs/test-cases.md`](docs/test-cases.md) — danh sách đầy đủ 115 test cases
- [`docs/test-results.md`](docs/test-results.md) — kết quả chạy unittest

## GitHub Workflow

- **Issue #1**: Thiết kế test cho dữ liệu hợp lệ → resolved bởi Commit #1
- **Issue #2**: Thiết kế test cho dữ liệu không hợp lệ + biên + ngoại lệ → resolved bởi Commit #2

## Tech stack

- Python 3.12
- `unittest` (built-in, không cần cài thêm)
- Không dùng ChatGPT — code viết thủ công
