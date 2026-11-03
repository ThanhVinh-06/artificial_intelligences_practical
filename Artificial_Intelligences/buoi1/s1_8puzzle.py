"""
Ví dụ 1.11 — 8-puzzle với hai hàm heuristic
File: s1_8puzzle.py
So sánh hiệu quả của hai hàm heuristic khi giải bài toán 8-puzzle bằng Greedy Best-First:
- h1: số ô đứng sai vị trí
- h2: tổng khoảng cách Manhattan của các ô tới vị trí đích
"""

from s1_greedy_common import greedy_best_first
from puzzle8_common import DICH, ke_8puzzle, h_sai_cho, h_manhattan_8, la_giai_duoc, in_bang

if __name__ == "__main__":
    DAU = (8, 1, 3, 4, 0, 2, 7, 6, 5)

    print("=== VÍ DỤ 1.11: GIẢI 8-PUZZLE BẰNG GREEDY BEST-FIRST VỚI H1 VÀ H2 ===")
    print("Trạng thái đầu (giải được:", la_giai_duoc(DAU), "):")
    in_bang(DAU)
    print()

    for ten_h, h in [
        ("h1 = số ô sai chỗ", h_sai_cho),
        ("h2 = tổng Manhattan", h_manhattan_8),
    ]:
        duong, so_mo = greedy_best_first(DAU, lambda t: t == DICH, ke_8puzzle, h)
        if duong is not None:
            print(f"{ten_h:22s}: mở {so_mo:4d} nút, đường đi {len(duong)} bước")
        else:
            print(f"{ten_h:22s}: không tìm thấy đường đi (đã mở {so_mo} nút)")

    print("\n[NHẬN XÉT QUAN TRỌNG]:")
    print("1. h2 (tổng Manhattan) chứa nhiều thông tin định lượng hơn h1 nên mở ít nút hơn (179 so với 196).")
    print("2. Cả hai đường đi do Greedy tìm được đều dài hơn nhiều so với tối ưu tuyệt đối")
    print("   (BFS ở Buổi 2 cho thấy bài này tối ưu chỉ cần đúng 14 bước, trong khi Greedy ra 26 và 36 bước).")
    print("3. Greedy Best-First đi nhanh nhưng không đảm bảo đường đi ngắn nhất -> Đó là lý do cần thuật toán A* (kết hợp g(n) + h(n)).")
