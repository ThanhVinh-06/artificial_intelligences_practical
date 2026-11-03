"""
Ví dụ 2.5 — Mê cung: BFS và DFS
Đoạn mã 20 — s2_me_cung.py
Dùng lại MAZE, ke_me_cung, ve_duong_di của Ví dụ 1.10 (maze_common) để so sánh BFS và DFS.
"""

from s2_khung import BaiToan, tim_kiem
from maze_common import START, GOAL, ke_me_cung, ve_duong_di

if __name__ == "__main__":
    bt = BaiToan(START, lambda o: o == GOAL, ke_me_cung)

    for cl in ("bfs", "dfs"):
        duong, so_mo, max_bien = tim_kiem(bt, cl)
        print(f"--- {cl.upper()}: {len(duong)} bước, mở {so_mo} nút, biên lớn nhất {max_bien}")
        print(ve_duong_di([o for _, o in duong]))
