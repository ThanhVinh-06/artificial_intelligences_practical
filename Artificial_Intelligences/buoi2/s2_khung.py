"""
Ví dụ 2.2 — Khung tìm kiếm cho mọi bài toán
Đoạn mã 17 — s2_khung.py
Đóng gói một BaiToan gồm trạng thái đầu, hàm kiểm tra đích và hàm sinh trạng thái kề.
Hàm tim_kiem chạy BFS hoặc DFS tuỳ tham số và thống kê số nút đã mở rộng cùng kích thước biên lớn nhất.
"""

from collections import deque

class BaiToan:
    """Bài toán tìm kiếm = (trạng thái đầu, kiểm tra đích, các toán tử)."""
    def __init__(self, dau, la_dich, ke):
        self.dau = dau
        self.la_dich = la_dich        # la_dich(tt) -> True/False
        self.ke = ke                  # ke(tt) -> các cặp (tên toán tử, tt mới)

def tim_kiem(bt, chien_luoc="bfs"):
    """Tìm kiếm mù tổng quát. Trả về (đường đi, số nút mở rộng, kích thước biên lớn nhất).
    Đường đi là list các cặp (toán tử, trạng thái)."""
    bien = deque([bt.dau])
    cha = {bt.dau: None}              # trạng thái -> (cha, toán tử); cũng là tập "đã thăm"
    so_mo, max_bien = 0, 1
    while bien:
        if chien_luoc == "bfs":
            tt = bien.popleft()       # FIFO -> BFS
        else:
            tt = bien.pop()           # LIFO -> DFS
        if bt.la_dich(tt):
            duong = []
            while cha[tt] is not None:  # lần ngược theo con trỏ cha
                tt_cha, ten = cha[tt]
                duong.append((ten, tt))
                tt = tt_cha
            return duong[::-1], so_mo, max_bien
        so_mo += 1
        for ten, moi in bt.ke(tt):
            if moi not in cha:
                cha[moi] = (tt, ten)
                bien.append(moi)
        max_bien = max(max_bien, len(bien))
    return None, so_mo, max_bien
