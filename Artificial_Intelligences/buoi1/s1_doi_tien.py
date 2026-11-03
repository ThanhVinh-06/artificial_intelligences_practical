"""
Ví dụ 1.3 — Bài toán đổi tiền
File: s1_doi_tien.py
Đối chiếu giữa chiến lược Tham Lam và Quy Hoạch Động (DP - Lời giải tối ưu).
"""

def doi_tien_tham_lam(menh_gia, so_tien):
    """Tham lam: luôn lấy tờ mệnh giá lớn nhất còn dùng được."""
    ket_qua = []
    for m in sorted(menh_gia, reverse=True):  # mệnh giá lớn nhất trước
        while so_tien >= m:
            ket_qua.append(m)
            so_tien -= m
    return ket_qua if so_tien == 0 else None

def doi_tien_qhd(menh_gia, so_tien):
    """Quy hoạch động: số tờ ÍT NHẤT (lời giải tối ưu) để đối chiếu."""
    INF = float("inf")
    f = [0] + [INF] * so_tien
    for x in range(1, so_tien + 1):
        for m in menh_gia:
            if m <= x and f[x - m] + 1 < f[x]:
                f[x] = f[x - m] + 1
    return f[so_tien]

if __name__ == "__main__":
    print("=== VÍ DỤ 1.3: BÀI TOÁN ĐỔI TIỀN ===")
    
    # Trường hợp 1: Hệ tiền tệ Việt Nam (chuẩn bội số, tham lam tối ưu)
    he_vn = [500, 200, 100, 50, 20, 10]
    kq_vn = doi_tien_tham_lam(he_vn, 380)
    print("Hệ VN (nghìn đồng), đổi 380:", kq_vn, "->", len(kq_vn) if kq_vn else 0, "tờ")

    # Trường hợp 2: Hệ tiền tệ nhân tạo {4, 3, 1}, đổi 6
    he_la = [4, 3, 1]
    kq_la = doi_tien_tham_lam(he_la, 6)
    opt_la = doi_tien_qhd(he_la, 6)
    print("Hệ {4,3,1}, đổi 6 -> tham lam:", kq_la, "=", len(kq_la) if kq_la else 0, "tờ")
    print("Hệ {4,3,1}, đổi 6 -> tối ưu   :", opt_la, "tờ")
    
    print("\n[NHẬN XÉT]:")
    print("- Với hệ tiền chuẩn VN, tham lam cho lời giải tối ưu.")
    print("- Với hệ {4, 3, 1}, tham lam chọn 4 + 1 + 1 (3 tờ), trong khi tối ưu là 3 + 3 (2 tờ).")
    print("=> Kết luận: Tính đúng của tham lam phụ thuộc vào cấu trúc bài toán, không phải bản thân thuật giải.")
