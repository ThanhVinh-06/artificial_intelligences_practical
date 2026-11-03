# BÀI GIẢNG THỰC HÀNH - TRÍ TUỆ NHÂN TẠO (BUỔI 2)

Thư mục: `Artificial_Intelligences/buoi2/`  
Nội dung tài liệu: **Mục 2.4. Thực hành: Tìm kiếm mù (BFS, DFS, DLS, IDDFS)** (Trang 27–34 PDF)

---

## 1. Danh Sách Mã Nguồn & Bài Tập

| File | Nội dung | Thuật toán / Kỹ thuật |
| :--- | :--- | :--- |
| `s2_do_thi.py` | **Đoạn mã 16** (Ví dụ 2.1): BFS và DFS trên đồ thị | Hàng đợi `deque` (BFS), ngăn xếp LIFO (DFS), và DFS đệ quy. |
| `s2_khung.py` | **Đoạn mã 17** (Ví dụ 2.2): Khung tìm kiếm cho mọi bài toán | Lớp `BaiToan(dau, la_dich, ke)` và hàm `tim_kiem(bt, chien_luoc)`. |
| `s2_binh_nuoc.py` | **Đoạn mã 18** (Ví dụ 2.3): Bài toán đổ nước | Mô hình hoá trạng thái `(a, b)` với 6 toán tử đong nước, giải bằng BFS. |
| `bt_2_4_binh_nuoc.py` | **Bài tập 2.4** (Trang 30): Khảo sát bài toán đổ nước vô nghiệm | Kiểm chứng điều kiện có nghiệm theo Định lý Bézout: `MUC_TIEU % gcd(CA, CB) == 0`. |
| `s2_nong_dan.py` | **Đoạn mã 19** (Ví dụ 2.4): Nông dân, sói, dê và bắp cải | Trạng thái bộ bốn `(n, s, d, b)`, lọc trạng thái không an toàn ngay trong hàm sinh kề. |
| `maze_common.py` | Thư viện dùng chung cho bài toán Mê cung (từ Ví dụ 1.10) | Lưới `MAZE`, `START`, `GOAL`, `ke_me_cung`, `ve_duong_di`. |
| `s2_me_cung.py` | **Đoạn mã 20** (Ví dụ 2.5): Mê cung — BFS và DFS | So sánh đường đi, số nút mở rộng và kích thước biên lớn nhất trên mê cung. |
| `puzzle8_common.py` | Thư viện dùng chung cho bài toán 8-puzzle (từ Ví dụ 1.11) | Trạng thái `DICH`, toán tử trượt ô trống `ke_8puzzle`. |
| `s2_8puzzle.py` | **Đoạn mã 21** (Ví dụ 2.6): 8-puzzle — BFS và DFS | Minh hoạ sự khác biệt giữa BFS (6 bước) và DFS (4096 bước). |
| `s2_dls_def.py` | **Đoạn mã 22** (Ví dụ 2.7): Cài đặt DLS và IDDFS | Đệ quy `dls` chống vòng lặp trên đường đi hiện tại (bộ nhớ $O(bd)$) và `iddfs`. |
| `s2_dls_demo.py` | **Đoạn mã 23** (Ví dụ 2.7): Minh hoạ DLS và IDDFS trên 8-puzzle | Kiểm tra ngưỡng cắt `cutoff` và quá trình tăng dần giới hạn sâu $0, 1, 2, \dots$ |
| `s2_so_sanh.py` | **Đoạn mã 24** (Ví dụ 2.8): So sánh BFS, DFS, IDDFS trên 8-puzzle | Thực nghiệm trên 4 cấu hình xuất phát có độ khó tăng dần. |
| `main.py` | Trình điều khiển tổng hợp | Cho phép chọn chạy từng ví dụ/bài tập hoặc chạy toàn bộ cùng lúc. |

---

## 2. Giải Thích & Nhận Xét Lý Thuyết Trong Tài Liệu

### 2.1. Cây tìm kiếm BFS và DFS trên đồ thị (Ví dụ 2.1 - Trang 28)
- **BFS** duyệt theo từng tầng (FIFO): `['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']` và đảm bảo tìm được đường đi ít cạnh nhất `A -> B -> E -> H`.
- **DFS** dùng ngăn xếp (LIFO), nhờ đảo danh sách kề `reversed(do_thi[u])` nên ưu tiên xét nhánh trái trước: đi sâu vào `A -> B -> D` (ngõ cụt), quay lui sang `E -> H`. Thứ tự xét là `['A', 'B', 'D', 'E', 'H']`.

### 2.2. Khi nào Bài toán đổ nước vô nghiệm? (BT2.4 - Trang 30)
- Với hai bình dung tích $C_A, C_B$ (không có vạch chia), mọi thao tác (đổ đầy, đổ cạn, rót qua lại) chỉ tạo ra lượng nước là tổ hợp tuyến tính nguyên của $C_A$ và $C_B$.
- Theo **Định lý Bézout**, bài toán đong được đúng $M$ lít ($0 \le M \le \max(C_A, C_B)$) **khi và chỉ khi** $M$ chia hết cho $\gcd(C_A, C_B)$.
- Ví dụ: Nếu $C_A = 4, C_B = 2$ ($\gcd = 2$) và $M = 3$ (lẻ), cả hai bình chỉ có thể chứa số lít chẵn nên bài toán **vô nghiệm**.

### 2.3. So sánh BFS, DFS và IDDFS (Ví dụ 2.8 - Trang 34)
- **Tính tối ưu (Optimality):** Khi chi phí mỗi bước bằng nhau, **BFS** và **IDDFS** luôn tìm ra lời giải ngắn nhất (cùng số bước). **DFS** không đảm bảo tối ưu và cho lời giải rất dài, thất thường (ví dụ bài chỉ cần 2 bước nhưng DFS đi tới 49.284 bước).
- **Bộ nhớ & Số nút xét:**
  - **BFS** lưu tập đã thăm (`cha`) trên toàn đồ thị nên không mở rộng trùng trạng thái, nhưng tốn bộ nhớ $O(b^d)$ để lưu toàn bộ biên và tập đã thăm.
  - **IDDFS** thực chất là tìm kiếm trên cây (chỉ kiểm tra trùng tổ tiên trên nhánh hiện tại `tren_duong`), do đó số nút thăm lớn hơn BFS (vì xét lặp lại các trạng thái trùng qua nhiều nhánh/vòng lặp), nhưng đổi lại chỉ tốn bộ nhớ tuyến tính $O(b \cdot d)$.

---

## 3. Hướng Dẫn Chạy Chương Trình

Mở Terminal tại thư mục `D:\python\Artificial_Intelligences\buoi2`:

### Cách 1: Chạy qua menu tổng hợp
```bash
python main.py
```

### Cách 2: Chạy trực tiếp từng tệp theo đúng tên trong giáo trình
```bash
python s2_do_thi.py
python s2_binh_nuoc.py
python bt_2_4_binh_nuoc.py
python s2_nong_dan.py
python s2_me_cung.py
python s2_8puzzle.py
python s2_dls_demo.py
python s2_so_sanh.py
```
