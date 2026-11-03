"""
Ví dụ 1.2 — Cái túi 0/1: tham lam có thể sai
File: s1_knapsack_01.py
So sánh thuật toán Tham Lam với Vét Cạn (Brute-force duyệt 2^n tổ hợp).

Câu hỏi cho sinh viên (trang 8 PDF):
- Nếu không cho phép lấy phần lẻ (bài toán Knapsack 0/1), kết quả tham lam trên có còn là tối ưu tuyệt đối không? Vì sao?
=> Trả lời:
KHÔNG còn tối ưu tuyệt đối. Vì khi không chia nhỏ được, phần sức chứa còn thừa bị "bỏ phí"
(lãng phí dung tích). Thuật toán tham lam vội chọn món có tỉ lệ cao nhất nhưng kích thước
không lấp đầy khoảng trống tối ưu, làm mất cơ hội chọn các tổ hợp món đồ khác có tổng giá trị lớn hơn.
"""

from itertools import combinations

def knapsack01_tham_lam(items, capacity):
    """0/1: mỗi món lấy trọn hoặc bỏ. Tham lam theo tỉ lệ giá trị/trọng lượng."""
    tong_gt = 0
    tong_tl = 0
    chon = []
    for ten, gt, tl in sorted(items, key=lambda x: x[1] / x[2], reverse=True):
        if tong_tl + tl <= capacity:
            chon.append(ten)
            tong_tl += tl
            tong_gt += gt
    return chon, tong_gt

def knapsack01_vet_can(items, capacity):
    """Duyệt toàn bộ 2^n tổ hợp -> lời giải tối ưu tuyệt đối."""
    tot_nhat = (0, [])
    for k in range(len(items) + 1):
        for tap in combinations(items, k):
            tl = sum(x[2] for x in tap)
            gt = sum(x[1] for x in tap)
            if tl <= capacity and gt > tot_nhat[0]:
                tot_nhat = (gt, [x[0] for x in tap])
    return tot_nhat[1], tot_nhat[0]

if __name__ == "__main__":
    items = [("A", 60, 10), ("B", 100, 20), ("C", 120, 30)]
    capacity = 50

    print("=== VÍ DỤ 1.2: CÁI TÚI 0/1 (THAM LAM VS VÉT CẠN) ===")
    chon_tl, gt_tl = knapsack01_tham_lam(items, capacity)
    chon_vc, gt_vc = knapsack01_vet_can(items, capacity)
    
    print("Tham lam :", (chon_tl, gt_tl))
    print("Vét cạn  :", (chon_vc, gt_vc))
    
    print("\n[GIẢI THÍCH]:")
    print("- Tỉ lệ giá trị/trọng lượng của A, B, C lần lượt là 6.0, 5.0, 4.0.")
    print("- Tham lam chọn A rồi B (tổng TL = 30, còn thừa 20 không đủ cho C), tổng giá trị = 160.")
    print("- Vét cạn chọn B và C (tổng TL = 50 vừa khít), tổng giá trị = 220 > 160.")
    print("=> Kết luận: Thuật toán tham lam không đảm bảo tối ưu toàn cục cho bài toán Knapsack 0/1.")
