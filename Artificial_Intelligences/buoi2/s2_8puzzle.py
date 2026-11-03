"""
Ví dụ 2.6 — 8-puzzle: BFS và DFS
Đoạn mã 21 — s2_8puzzle.py
Dùng lại đoạn mã puzzle8_common của Buổi 1 (trạng thái, ke_8puzzle, DICH).
Trạng thái đầu dưới đây có lời giải ngắn nhất 6 bước.
"""

from s2_khung import BaiToan, tim_kiem
from puzzle8_common import DICH, ke_8puzzle

if __name__ == "__main__":
    DAU = (4, 1, 3, 7, 2, 6, 0, 5, 8)
    bt = BaiToan(DAU, lambda t: t == DICH, ke_8puzzle)

    for cl in ("bfs", "dfs"):
        duong, so_mo, max_bien = tim_kiem(bt, cl)
        print(f"{cl.upper()}: đường đi {len(duong):6d} bước | mở {so_mo:6d} nút | biên lớn nhất {max_bien:6d}")
