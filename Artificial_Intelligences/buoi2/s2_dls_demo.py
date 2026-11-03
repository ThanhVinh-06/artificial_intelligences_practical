"""
Ví dụ 2.7 — DLS và IDDFS (Chạy thử nghiệm)
Đoạn mã 23 — s2_dls_demo.py
"""

from s2_khung import BaiToan
from puzzle8_common import DICH, ke_8puzzle
from s2_dls_def import dls, iddfs

if __name__ == "__main__":
    DAU = (1, 2, 3, 5, 0, 6, 4, 7, 8)
    bt = BaiToan(DAU, lambda t: t == DICH, ke_8puzzle)

    print("DLS với giới hạn 3:", "cutoff" if dls(bt, DAU, 3, [], [0]) == "cutoff" else "tìm thấy")
    print("IDDFS:")
    duong, tong = iddfs(bt, in_log=True)
    print(f"Lời giải dài {len(duong)} bước: {[ten for ten, _ in duong]}")
    print(f"Tổng số nút đã thăm qua mọi vòng lặp: {tong}")
