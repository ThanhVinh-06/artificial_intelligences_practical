"""
Ví dụ 1.9 — Khung Greedy Best-First tổng quát
File: s1_greedy_common.py

Khung thuật toán dùng chung cho mọi bài toán tìm kiếm có thông tin (heuristic):
- dau: trạng thái bắt đầu
- la_dich(tt): hàm kiểm tra trạng thái tt có phải là đích không
- ke(tt): hàm sinh các trạng thái kề, trả về generator/list của các cặp (tên_toán_tử, trạng_thái_mới)
- h(tt): hàm heuristic ước lượng chi phí từ tt đến đích
"""

import heapq

def greedy_best_first(dau, la_dich, ke, h):
    """
    Tham lam theo hàm đánh giá h: luôn mở rộng nút có h nhỏ nhất.
    ke(tt) -> các cặp (tên_toán_tử, trạng_thái_mới).
    Trả về:
      - duong: list các bước [(toán tử, trạng thái), ...] dẫn từ 'dau' đến đích
      - so_mo: số nút đã mở rộng (thước đo chi phí tìm kiếm)
    """
    dem = 0  # biến đếm để "phá hoà" khi hai trạng thái có h bằng nhau
    bien = [(h(dau), dem, dau)]
    cha = {dau: None}  # ánh xạ: trạng thái -> (trạng thái cha, toán tử)
    so_mo = 0
    
    while bien:
        _, _, tt = heapq.heappop(bien)
        so_mo += 1
        
        if la_dich(tt):
            # Truy vết ngược đường đi từ đích về gốc
            duong = []
            while cha[tt] is not None:
                tt_cha, ten = cha[tt]
                duong.append((ten, tt))
                tt = tt_cha
            return duong[::-1], so_mo
            
        for ten, moi in ke(tt):
            if moi not in cha:
                cha[moi] = (tt, ten)
                dem += 1
                heapq.heappush(bien, (h(moi), dem, moi))
                
    return None, so_mo
