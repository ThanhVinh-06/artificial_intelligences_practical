# BÀI GIẢNG THỰC HÀNH - TRÍ TUỆ NHÂN TẠO (BUỔI 1)

Thư mục: `Artificial_Intelligences/buoi1/`  
Nội dung tài liệu: **Nguyên lý tham lam (Greedy) và Nguyên lý thứ tự (Ordering)**

---

## 1. Danh Sách Mã Nguồn & Bài Tập

| File | Nội dung | Thuật toán / Kỹ thuật |
| :--- | :--- | :--- |
| `s1_knapsack_frac.py` | Ví dụ 1.1: Bài toán cái túi phân số (Fractional Knapsack) | Tham lam theo tỉ lệ `giá trị / trọng lượng` giảm dần. |
| `s1_knapsack_01.py` | Ví dụ 1.2: Bài toán cái túi 0/1 (Knapsack 0/1) & Câu hỏi sinh viên | So sánh Tham lam vs Vét cạn ($2^n$ tổ hợp). |
| `s1_doi_tien.py` | Ví dụ 1.3: Bài toán đổi tiền | Tham lam vs Quy hoạch động (lời giải tối ưu). |
| `s1_hoat_dong.py` | Ví dụ 1.4: Lựa chọn hoạt động (Activity Selection) | So sánh 3 tiêu chí: Kết thúc sớm nhất, Bắt đầu sớm nhất, Thời lượng ngắn nhất. |
| `bt_1_6_hoat_dong.py` | **Bài tập 1.6**: Phản ví dụ tiêu chí "Thời lượng ngắn nhất" | Chứng minh heuristic thời lượng ngắn nhất không tối ưu tổng quát. |
| `s1_tsp.py` | Ví dụ 1.5: Người bán hàng (TSP) | Tham lam Nearest Neighbor so với Vét cạn $(n-1)!$. |
| `s1_job.py` | Ví dụ 1.6: Sắp lịch công việc (Job Sequencing with Deadlines) | Nguyên lý thứ tự: sắp theo lợi nhuận giảm dần và lùi hạn chót. |
| `s1_heapq_demo.py` | Ví dụ 1.7: Hàng đợi ưu tiên với thư viện `heapq` | Min-heap $O(\log n)$ và quy tắc phá hoà (tie-breaker). |
| `s1_pq.py` | Ví dụ 1.8: Best-First tối giản trên trục số 1D | Duyệt có thông tin với $h(state) = \|goal - state\|$. |
| `s1_greedy_common.py` | Ví dụ 1.9: Khung Greedy Best-First tổng quát | Cấu trúc dùng chung (gốc, kiểm tra đích, toán tử kế tiếp, $h$). |
| `maze_common.py` | Ví dụ 1.10: Định nghĩa dữ liệu và hàm mê cung 2D | Lưới mê cung, toán tử kề, khoảng cách Manhattan, vẽ đường đi. |
| `s1_maze_greedy.py` | Ví dụ 1.10: Tìm đường mê cung bằng Greedy Best-First | Heuristic Manhattan $h(o) = \|r - r_G\| + \|c - c_G\|$. |
| `bt_1_8_maze_trap.py` | **Bài tập 1.8**: Thiết kế mê cung bẫy chữ U | Chứng minh Greedy Best-First bị bẫy đi đường vòng so với BFS. |
| `puzzle8_common.py` | Ví dụ 1.11: Định nghĩa không gian trạng thái 8-puzzle | Biểu diễn trạng thái, toán tử trượt, kiểm tra tính giải được. |
| `s1_8puzzle.py` | Ví dụ 1.11: Giải 8-puzzle với 2 hàm heuristic ($h_1, h_2$) | So sánh $h_1$ (số ô sai chỗ) và $h_2$ (tổng khoảng cách Manhattan). |
| `main.py` | Trình điều khiển tổng hợp | Cho phép chạy kiểm tra từng bài hoặc toàn bộ bài tập cùng lúc. |

---

## 2. Giải Chi Tiết Các Câu Hỏi & Bài Tập Mở Rộng Trong PDF

### Câu hỏi cho sinh viên (Trang 8 PDF)
> *Nếu không cho phép lấy phần lẻ (bài toán Knapsack 0/1), kết quả tham lam trên có còn là tối ưu tuyệt đối không? Vì sao?*

**Trả lời:**
- **Không.** Trong bài toán Knapsack 0/1, chiến lược tham lam theo tỉ lệ `giá trị / trọng lượng` không đảm bảo tìm được nghiệm tối ưu toàn cục.
- **Nguyên nhân:** Khi không cho phép lấy phần lẻ của một vật thể, việc tham lam chọn các món có tỉ lệ đơn vị cao nhất có thể làm lãng phí dung tích túi còn lại (phần sức chứa dư thừa không thể chứa thêm món nào khác). Một tập hợp các món đồ có tỉ lệ đơn vị thấp hơn một chút nhưng phối hợp vừa khít với dung tích túi sẽ mang lại tổng giá trị cao hơn.
- **Minh chứng (Ví dụ 1.2):**
  - Món hàng: $A(60, 10)$, $B(100, 20)$, $C(120, 30)$, dung tích túi = $50$.
  - Tỉ lệ: $A=6.0$, $B=5.0$, $C=4.0$.
  - Tham lam chọn $A$ rồi $B \Rightarrow$ Tổng trọng lượng $30$, còn thừa $20$ (không đủ chứa $C$). Giá trị đạt được $= 160$.
  - Lời giải tối ưu (Vét cạn / QHD): Chọn $B$ và $C \Rightarrow$ Trọng lượng $50$ vừa khít túi. Tổng giá trị $= 220 > 160$.

---

### Bài tập 1.6 (Trang 10 PDF)
> *Xây dựng bộ dữ liệu chứng minh tiêu chí "Thời lượng ngắn nhất" không đúng tổng quát.*

**Trả lời & Cài đặt (`bt_1_6_hoat_dong.py`):**
- Giả sử có 3 hoạt động:
  - $H_1 = [1, 5]$ (thời lượng = $4$)
  - $H_2 = [4, 6]$ (thời lượng = $2$ — ngắn nhất)
  - $H_3 = [5, 9]$ (thời lượng = $4$)
- Nếu theo tiêu chí **Thời lượng ngắn nhất**:
  - $H_2$ được chọn đầu tiên vì thời lượng ngắn nhất ($2$).
  - $H_1$ bị loại vì chồng lấn $[4, 5]$ với $H_2$.
  - $H_3$ bị loại vì chồng lấn $[5, 6]$ với $H_2$.
  - Kết quả: chỉ chọn được duy nhất **1 hoạt động** ($[H_2]$).
- Nếu theo tiêu chí **Kết thúc sớm nhất** (Thuật toán tối ưu đã được chứng minh):
  - Chọn $H_1$ (kết thúc ở $t=5$).
  - $H_2$ bắt đầu lúc $4 < 5 \Rightarrow$ bỏ qua.
  - Chọn $H_3$ (bắt đầu $5 \ge 5$, kết thúc ở $t=9$).
  - Kết quả: chọn được **2 hoạt động** ($[H_1, H_3]$).
- **Kết luận:** Tiêu chí "Thời lượng ngắn nhất" có thể bị bẫy bởi hoạt động nằm ở vị trí giao cắt giữa hai hoạt động khác.

---

### Bài tập 1.8 (Trang 12 PDF)
> *Tự tạo mê cung khiến Greedy Best-First đi vòng / kém tối ưu.*

**Trả lời & Cài đặt (`bt_1_8_maze_trap.py`):**
- **Cơ chế bẫy:** Greedy Best-First chỉ quan sát hàm heuristic $h(n)$ (khoảng cách đường chim bay Manhattan tới đích $G$) mà không tính chi phí tích luỹ $g(n)$. Khi ta tạo một bức tường lõm hình chữ U chắn phía trước đích, thuật toán sẽ liên tục chọn đi sâu vào đáy túi lõm (nơi có toạ độ gần $G$ nhất theo Manhattan).
- Khi tới bước đường cùng (ngõ cụt bên trong chữ U), thuật toán mới buộc phải quay lui và vòng qua miệng túi, dẫn đến:
  1. Phải mở rộng thêm rất nhiều trạng thái vô ích bên trong túi lõm.
  2. Đường đi tìm được bị dài hơn đáng kể so với đường đi tối ưu (tìm bởi BFS).
- **Ý nghĩa:** Đây là tiền đề chứng minh sự cần thiết của thuật toán **A\*** kết hợp $f(n) = g(n) + h(n)$.

---

## 3. Hướng Dẫn Chạy Chương Trình

Mở Terminal tại thư mục `D:\python\Artificial_Intelligences\buoi1` và thực hiện:

### Chạy qua Runner tương tác (Khuyến nghị):
```bash
python main.py
```
Nhập số thứ tự của bài muốn kiểm tra (hoặc ấn `0` để chạy toàn bộ các bài).

### Chạy từng bài riêng lẻ:
```bash
python s1_knapsack_frac.py
python s1_knapsack_01.py
python s1_doi_tien.py
python s1_hoat_dong.py
python bt_1_6_hoat_dong.py
python s1_tsp.py
python s1_job.py
python s1_heapq_demo.py
python s1_pq.py
python s1_maze_greedy.py
python bt_1_8_maze_trap.py
python s1_8puzzle.py
```
