"""
Ví dụ 1.5 — Người bán hàng (TSP) bằng Nearest Neighbor
File: s1_tsp.py
So sánh thuật toán Tham lam Nearest Neighbor (láng giềng gần nhất) với Vét cạn tìm kiếm toàn cục.
"""

import math
from itertools import permutations

def khoang_cach(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def do_dai_chu_trinh(cities, path):
    return sum(khoang_cach(cities[path[i]], cities[path[i + 1]])
               for i in range(len(path) - 1))

def nearest_neighbor_tsp(cities, start=0):
    unvisited = set(range(len(cities)))
    unvisited.remove(start)
    path = [start]
    current = start
    while unvisited:
        # Nguyên lý tham lam: luôn chọn thành phố gần nhất tại bước hiện tại
        next_city = min(unvisited, key=lambda c: khoang_cach(cities[current], cities[c]))
        path.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    path.append(start)  # quay về điểm xuất phát
    return path, do_dai_chu_trinh(cities, path)

def tsp_vet_can(cities):
    """Thuật toán: thử mọi hoán vị (n-1)! -> chỉ dùng được khi n nhỏ."""
    tot = (float("inf"), None)
    for hoan_vi in permutations(range(1, len(cities))):
        path = [0, *hoan_vi, 0]
        d = do_dai_chu_trinh(cities, path)
        if d < tot[0]:
            tot = (d, path)
    return tot[1], tot[0]

if __name__ == "__main__":
    cities = [(0, 0), (2, 3), (5, 4), (1, 7), (6, 1), (3, 3)]

    print("=== VÍ DỤ 1.5: BÀI TOÁN NGƯỜI BÁN HÀNG (TSP) ===")
    print("Nearest Neighbor với từng điểm xuất phát:")
    tot_nhat = None
    for s in range(len(cities)):
        path, d = nearest_neighbor_tsp(cities, start=s)
        print(f"  start={s}: {path} dài {d:.2f}")
        if tot_nhat is None or d < tot_nhat[1]:
            tot_nhat = (path, d)
            
    print("Tốt nhất trong các lần chạy greedy:", tot_nhat[0], round(tot_nhat[1], 2))

    path_opt, d_opt = tsp_vet_can(cities)
    print("Tối ưu tuyệt đối (vét cạn)        :", path_opt, round(d_opt, 2))
    
    print("\n[NHẬN XÉT]:")
    print(f"- Greedy chạy rất nhanh với độ phức tạp O(n^2) so với O(n!) của vét cạn.")
    print(f"- Tuy nhiên kết quả phụ thuộc điểm xuất phát và không đảm bảo tối ưu toàn cục.")
    print(f"- Lời giải greedy tốt nhất ({round(tot_nhat[1], 2)}) dài hơn tối ưu ({round(d_opt, 2)}) khoảng 1.5%.")
