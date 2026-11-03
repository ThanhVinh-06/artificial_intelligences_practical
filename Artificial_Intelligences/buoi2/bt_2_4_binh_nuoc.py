"""
Bài tập 2.4 — Khảo sát điều kiện có nghiệm của Bài toán đổ nước (trang 30 PDF)
File: bt_2_4_binh_nuoc.py
Yêu cầu: "Hãy thử đổi MUC_TIEU hay dung tích hai bình (BT2.4) để xem khi nào bài toán vô nghiệm."

Định lý Bézout: Bài toán đong nước với 2 bình dung tích CA, CB để đạt lượng nước MUC_TIEU (0 <= MUC_TIEU <= max(CA, CB))
có nghiệm khi và chỉ khi MUC_TIEU chia hết cho Ước chung lớn nhất gcd(CA, CB).
"""

import math
from s2_khung import BaiToan, tim_kiem

def tao_ke_binh(ca, cb):
    def ke_binh(tt):
        a, b = tt
        yield "Đổ đầy A", (ca, b)
        yield "Đổ đầy B", (a, cb)
        yield "Đổ cạn A", (0, b)
        yield "Đổ cạn B", (a, 0)
        t = min(a, cb - b)
        yield "Rót A sang B", (a - t, b + t)
        t = min(b, ca - a)
        yield "Rót B sang A", (a + t, b - t)
    return ke_binh

if __name__ == "__main__":
    CAC_TRUONG_HOP = [
        (4, 3, 2),   # gcd(4, 3) = 1 -> 2 chia hết cho 1 -> Có nghiệm (6 bước)
        (4, 2, 2),   # gcd(4, 2) = 2 -> 2 chia hết cho 2 -> Có nghiệm (2 bước)
        (4, 2, 3),   # gcd(4, 2) = 2 -> 3 KHÔNG chia hết cho 2 -> Vô nghiệm
        (6, 4, 3),   # gcd(6, 4) = 2 -> 3 KHÔNG chia hết cho 2 -> Vô nghiệm
        (6, 4, 5),   # gcd(6, 4) = 2 -> 5 KHÔNG chia hết cho 2 -> Vô nghiệm
        (5, 3, 4),   # gcd(5, 3) = 1 -> 4 chia hết cho 1 -> Có nghiệm (6 bước)
    ]

    print(f"{'CA':>3s} {'CB':>3s} {'Mục tiêu':>9s} | {'gcd(CA,CB)':>10s} | {'Kết quả BFS':<22s} | {'Số nút mở':>9s}")
    print("-" * 70)
    for ca, cb, mt in CAC_TRUONG_HOP:
        g = math.gcd(ca, cb)
        bt = BaiToan((0, 0), lambda tt, m=mt: tt[0] == m, tao_ke_binh(ca, cb))
        duong, so_mo, _ = tim_kiem(bt, "bfs")
        if duong is not None:
            kq = f"Có nghiệm ({len(duong)} bước)"
        else:
            kq = "VÔ NGHIỆM (None)"
        print(f"{ca:3d} {cb:3d} {mt:9d} | {g:10d} | {kq:<22s} | {so_mo:9d}")

    print("\nKết luận (Định lý Bézout):")
    print("- Với 0 <= MUC_TIEU <= CA, bài toán có nghiệm khi và chỉ khi MUC_TIEU % gcd(CA, CB) == 0.")
    print("- Khi vô nghiệm, BFS duyệt hết toàn bộ không gian trạng thái khả dĩ rồi dừng và trả về None.")
