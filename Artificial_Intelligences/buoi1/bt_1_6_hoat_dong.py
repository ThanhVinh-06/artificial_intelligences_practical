"""
Bài tập 1.6 — Phản ví dụ tiêu chí 'Thời lượng ngắn nhất' (Activity Selection)
File: bt_1_6_hoat_dong.py

Mục tiêu:
Xây dựng một bộ dữ liệu hoạt động phản ví dụ để chứng minh rằng chiến lược tham lam
theo tiêu chí 'Thời lượng ngắn nhất' (Shortest Interval / Duration First) KHÔNG LUÔN TỐI ƯU.

Ví dụ kinh điển:
- Hoạt động H1: từ 1 đến 5 (thời lượng = 4)
- Hoạt động H2: từ 4 đến 6 (thời lượng = 2, ngắn nhất!)
- Hoạt động H3: từ 5 đến 9 (thời lượng = 4)

Khi áp dụng:
1. Tiêu chí 'Thời lượng ngắn nhất':
   - H2 được chọn đầu tiên vì có thời lượng 2.
   - H1 [1, 5] chồng chéo với H2 [4, 6] -> Bị loại.
   - H3 [5, 9] chồng chéo với H2 [4, 6] -> Bị loại.
   => Kết quả: chỉ chọn được 1 hoạt động [H2].

2. Tiêu chí 'Kết thúc sớm nhất' (Tối ưu chuẩn):
   - H1 kết thúc sớm nhất ở t=5 -> Chọn H1.
   - H2 bắt đầu lúc 4 < 5 -> Bỏ qua.
   - H3 bắt đầu lúc 5 >= 5 -> Chọn H3.
   => Kết quả: chọn được 2 hoạt động [H1, H3]!
"""

from s1_hoat_dong import chon_hoat_dong

if __name__ == "__main__":
    # Bộ dữ liệu phản ví dụ
    ds_phan_vi_du = [
        ("H1 (Trái)", 1, 5),     # Thời lượng = 4
        ("H2 (Giữa)", 4, 6),     # Thời lượng = 2 (ngắn nhất)
        ("H3 (Phải)", 5, 9),     # Thời lượng = 4
    ]

    tieu_chi = {
        "Kết thúc sớm nhất (Tối ưu)": lambda x: x[2],
        "Thời lượng ngắn nhất      ": lambda x: x[2] - x[1],
        "Bắt đầu sớm nhất          ": lambda x: x[1],
    }

    print("=== BÀI TẬP 1.6: PHẢN VÍ DỤ TIÊU CHÍ THỜI LƯỢNG NGẮN NHẤT ===")
    print("Danh sách hoạt động:")
    for ten, bd, kt in ds_phan_vi_du:
        print(f"  {ten}: [{bd}, {kt}] (thời lượng = {kt - bd})")
    print()

    for ten, khoa in tieu_chi.items():
        kq = chon_hoat_dong(ds_phan_vi_du, khoa)
        print(f"{ten}: {len(kq)} hoạt động -> {kq}")

    print("\n[KẾT LUẬN BT 1.6]:")
    print("- Tiêu chí 'Thời lượng ngắn nhất' chọn H2 ở giữa vì nó ngắn nhất,")
    print("  nhưng vô tình chặn cả H1 và H3 ở hai đầu, dẫn đến chỉ đạt được 1 hoạt động.")
    print("- Trong khi đó, tiêu chí 'Kết thúc sớm nhất' chọn được 2 hoạt động (H1, H3).")
    print("=> Chứng minh 'Thời lượng ngắn nhất' chỉ là heuristic cục bộ, không tối ưu tổng quát.")
