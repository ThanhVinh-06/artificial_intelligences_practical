"""
Ví dụ 2.8 — So sánh BFS, DFS, IDDFS trên 8-puzzle
Đoạn mã 24 — s2_so_sanh.py
Chạy ba thuật toán trên bốn trạng thái đầu khó dần. Ghi lại số bước của lời giải và số nút phải xét.
"""

from s2_khung import BaiToan, tim_kiem
from puzzle8_common import DICH, ke_8puzzle
from s2_dls_def import iddfs

if __name__ == "__main__":
    DS_DAU = [
        (1, 2, 3, 4, 0, 6, 7, 5, 8),
        (1, 2, 3, 5, 0, 6, 4, 7, 8),
        (4, 1, 3, 7, 2, 6, 0, 5, 8),
        (8, 1, 3, 4, 0, 2, 7, 6, 5),
    ]
    print(f"{'':3s}| {'BFS':^21s}| {'DFS':^21s}| {'IDDFS':^21s}")
    print(f"{'#':3s}| {'bước':>6s} {'nút mở':>7s}   | {'bước':>6s} {'nút mở':>7s}   | {'bước':>6s} {'nút thăm':>9s}")
    for k, dau in enumerate(DS_DAU, 1):
        bt = BaiToan(dau, lambda t: t == DICH, ke_8puzzle)
        d1, n1, _ = tim_kiem(bt, "bfs")
        d2, n2, _ = tim_kiem(bt, "dfs")
        d3, n3 = iddfs(bt)
        print(f"{k:<3d}| {len(d1):6d} {n1:7d}   | {len(d2):6d} {n2:7d}   | {len(d3):6d} {n3:9d}")
