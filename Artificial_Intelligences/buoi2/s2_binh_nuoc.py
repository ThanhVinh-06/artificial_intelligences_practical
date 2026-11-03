"""
Ví dụ 2.3 — Bài toán đổ nước
Đoạn mã 18 — s2_binh_nuoc.py
Có bình A (4 lít) và bình B (3 lít), không có vạch chia. Làm sao để bình A có đúng 2 lít?
Trạng thái là cặp (a, b); có sáu toán tử.
"""

from s2_khung import BaiToan, tim_kiem

CA, CB, MUC_TIEU = 4, 3, 2            # bình A 4 lít, bình B 3 lít, cần 2 lít ở A

def ke_binh(tt):
    a, b = tt
    yield "Đổ đầy A", (CA, b)
    yield "Đổ đầy B", (a, CB)
    yield "Đổ cạn A", (0, b)
    yield "Đổ cạn B", (a, 0)
    t = min(a, CB - b)
    yield "Rót A sang B", (a - t, b + t)
    t = min(b, CA - a)
    yield "Rót B sang A", (a + t, b - t)

if __name__ == "__main__":
    bt = BaiToan((0, 0), lambda tt: tt[0] == MUC_TIEU, ke_binh)
    duong, so_mo, max_bien = tim_kiem(bt, "bfs")

    print("Trạng thái đầu: (0, 0)")
    for i, (ten, tt) in enumerate(duong, 1):
        print(f"Bước {i}: {ten:14s} -> {tt}")
    print(f"Số bước: {len(duong)} | nút đã mở rộng: {so_mo} | biên lớn nhất: {max_bien}")
