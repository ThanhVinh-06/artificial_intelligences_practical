"""
Ví dụ 1.4 — Chọn hoạt động (Activity Selection)
File: s1_hoat_dong.py
Khảo sát 3 tiêu chí tham lam khác nhau để chọn số lượng hoạt động tối đa không chồng chéo.
"""

def chon_hoat_dong(ds, khoa):
    """
    ds: list các tuple (ten, bat_dau, ket_thuc). Chọn nhiều hoạt động nhất, không chồng lấn.
    khoa: hàm quy định THỨ TỰ xét các hoạt động.
    """
    chon = []
    ket_thuc_cuoi = 0
    for ten, bd, kt in sorted(ds, key=khoa):
        if bd >= ket_thuc_cuoi:
            chon.append(ten)
            ket_thuc_cuoi = kt
    return chon

if __name__ == "__main__":
    ds = [
        ("H1", 1, 4), ("H2", 3, 5), ("H3", 0, 6), ("H4", 5, 7), ("H5", 3, 9),
        ("H6", 5, 9), ("H7", 6, 10), ("H8", 8, 11), ("H9", 8, 12),
        ("H10", 2, 14), ("H11", 12, 16)
    ]

    tieu_chi = {
        "Kết thúc sớm nhất": lambda x: x[2],
        "Bắt đầu sớm nhất ": lambda x: x[1],
        "Thời lượng ngắn nhất": lambda x: x[2] - x[1],
    }

    print("=== VÍ DỤ 1.4: BÀI TOÁN CHỌN HOẠT ĐỘNG (ACTIVITY SELECTION) ===")
    for ten, khoa in tieu_chi.items():
        kq = chon_hoat_dong(ds, khoa)
        print(f"{ten:22s}: {len(kq)} hoạt động {kq}")

    print("\n[NHẬN XÉT]:")
    print("- 'Kết thúc sớm nhất' được chứng minh toán học luôn cho kết quả tối ưu toàn cục.")
    print("- 'Bắt đầu sớm nhất' cho kết quả kém (H3 bắt đầu từ 0 đến 6 làm mất cơ hội của nhiều việc khác).")
    print("- 'Thời lượng ngắn nhất' tình cờ đạt 4 hoạt động trên tập dữ liệu này nhưng KHÔNG đúng tổng quát (xem bt_1_6_hoat_dong.py).")
