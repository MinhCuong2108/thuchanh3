# Áp dụng kiểm thử hộp đen cho 8 bài toán

Black-box testing (kiểm thử hộp đen) kiểm tra chương trình dựa trên **đặc tả đầu vào / đầu ra** mà không cần biết cấu trúc bên trong. Mình áp dụng **3 kỹ thuật** sau cho mỗi bài:

## 3 Kỹ thuật sử dụng

### 1. Phân lớp tương đương (Equivalence Partitioning)
Chia miền đầu vào thành các lớp mà trong mỗi lớp, chương trình được kỳ vọng xử lý giống nhau. Chỉ cần chọn **1 giá trị đại diện** cho mỗi lớp.

Ví dụ — `alternating_sum(n)`:
- Lớp hợp lệ: `n >= 0` → chia thành `n = 0` (rỗng), `n` lẻ, `n` chẵn dương.
- Lớp không hợp lệ: `n < 0`, `n` không phải số nguyên.

### 2. Phân tích giá trị biên (Boundary Value Analysis)
Kiểm thử tại các **điểm biên** (boundary) của miền hợp lệ và **lân cận ngay bên ngoài** (just-outside). Lỗi thường xuất hiện ở biên.

Ví dụ — `days_in_month(month, year)`:
- Biên dưới hợp lệ: `month = 1` ✓ (test tháng 1)
- Biên trên hợp lệ: `month = 12` ✓ (test tháng 12)
- Vừa ngoài biên dưới: `month = 0` ✗ (raise ValueError)
- Vừa ngoài biên trên: `month = 13` ✗ (raise ValueError)

### 3. Dữ liệu hợp lệ / không hợp lệ
- **Dữ liệu hợp lệ**: giá trị nằm trong miền kỳ vọng của input.
- **Dữ liệu không hợp lệ**: vi phạm đặc tả (sai kiểu, sai miền, ký tự không phải số…).

Mỗi bài có **ít nhất 1 test case dữ liệu không hợp lệ** (theo yêu cầu đề bài) để quan sát cách chương trình xử lý — raise `ValueError`, trả về giá trị đặc biệt, hoặc trả về kết quả ngầm định.

## Áp dụng cho từng bài

### Bài 1+2 — Hình chữ nhật (chu vi, diện tích)
- **Lớp tương đương**: số thực dương; số nguyên dương; số thực rất nhỏ / rất lớn; hình vuông (`L = W`).
- **Biên**: `sys.float_info.min` (nhỏ nhất), `1e9` (rất lớn).
- **Không hợp lệ**: `0`, số âm, `None`, chuỗi `"5"`, list `[5]`, `bool True`. Mỗi loại phải raise `ValueError`.

### Bài 3 — Phương trình bậc 2
- **Lớp hợp lệ**: `D > 0` (2 nghiệm phân biệt); `D == 0` (nghiệm kép); `D < 0` (nghiệm phức); `a = 0, b ≠ 0` (phương trình bậc 1).
- **Biên**: `D = 0` (x² − 4x + 4); hệ số phân số (1/2).
- **Không hợp lệ**: `a = b = 0` (vô định / vô nghiệm); hệ số không phải số (`"1"`, `None`, `[3]`, `bool`).

### Bài 4 — Số ngày của tháng
- **Lớp hợp lệ**: tháng 31 ngày {1, 3, 5, 7, 8, 10, 12}; tháng 30 ngày {4, 6, 9, 11}; tháng 2 năm thường (28); tháng 2 năm nhuận (29).
- **Biên**: tháng = 1, tháng = 12; năm = 1; năm nhuận thế kỷ (1900, 2000).
- **Không hợp lệ**: `month = 0`, `month = 13`, `month < 0`, `year = 0`, `year < 0`, `month`/`year` không phải số nguyên.

### Bài 5 — Số nguyên tố
- **Lớp hợp lệ**: nguyên tố {2, 3, 5, 7, 13, 7919}, hợp số {4, 9, 15, 100}.
- **Biên**: `n = 2` (nguyên tố nhỏ nhất); `n = 1` (KHÔNG nguyên tố); `n = 0`; `n < 0`.
- **Không hợp lệ**: `3.5` (float), chuỗi, `None`, `bool True`.

### Bài 6 — Tổng đan dấu S = 1 − 2 + 3 − 4 + … + n
- **Lớp hợp lệ**: `n = 0` (rỗng → 0); `n` lẻ (kết quả dương); `n` chẵn (kết quả âm).
- **Biên**: `n = 0`, `n = 1`, `n = 20` (lớn).
- **Không hợp lệ**: `n < 0`, `n` không nguyên.

### Bài 7 — UCLN(a, b)
- **Lớp hợp lệ**: nguyên tố cùng nhau; có ước chung lớn; một số chia hết số kia; một số = 0; cả hai = 0; một âm; cả hai âm; đảo thứ tự.
- **Biên**: `gcd(0, 0) = 0` (theo quy ước); `gcd(n, 0) = n`.
- **Không hợp lệ**: số thực, chuỗi, `None`, list, `bool`.

### Bài 8 — Tổng giai thừa S = 1! + 2! + … + n!
- **Lớp hợp lệ**: `n = 0` (rỗng → 0); `n = 1`; `n >= 2`.
- **Biên**: `n = 0`, `n = 1`; kiểm tra helper `factorial(0) = 1`, `factorial(5) = 120`.
- **Không hợp lệ**: `n < 0`, `n` không nguyên, `bool`.

## Cấu trúc test

| File | Issue | Số tests |
|---|---|---|
| `tests/test_valid.py` | #1 — dữ liệu hợp lệ | 62 |
| `tests/test_invalid.py` | #2 — không hợp lệ + biên + ngoại lệ | 53 |
| **Tổng** | | **115** |

## Chạy test

```bash
python3 -m unittest discover -s tests -v
```
