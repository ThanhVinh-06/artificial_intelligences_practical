"""
Ví dụ 1.11 — Cấu trúc dữ liệu và hàm dùng chung cho bài toán 8-Puzzle
File: puzzle8_common.py

Trạng thái đích quy ước: (1, 2, 3, 4, 5, 6, 7, 8, 0) với 0 là ô trống.
Biểu diễn bảng 3x3 dưới dạng tuple 9 phần tử.
"""

DICH = (1, 2, 3, 4, 5, 6, 7, 8, 0)  # 0 là ô trống

def ke_8puzzle(tt):
    """Toán tử: dịch ô trống Lên/Xuống/Trái/Phải (nếu không ra ngoài lưới 3x3)."""
    i = tt.index(0)
    r, c = divmod(i, 3)
    cac_phep_dich = [
        (-1, 0, "Lên"),
        (1, 0, "Xuống"),
        (0, -1, "Trái"),
        (0, 1, "Phải"),
    ]
    for dr, dc, ten in cac_phep_dich:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            j = nr * 3 + nc
            moi = list(tt)
            moi[i], moi[j] = moi[j], moi[i]
            yield ten, tuple(moi)

def h_sai_cho(tt):
    """h1: số ô (khác ô trống) đang đứng sai vị trí."""
    return sum(1 for i in range(9) if tt[i] != 0 and tt[i] != DICH[i])

def h_manhattan_8(tt):
    """h2: tổng khoảng cách Manhattan của từng ô tới vị trí đúng."""
    tong = 0
    for i, v in enumerate(tt):
        if v != 0:
            j = DICH.index(v)
            tong += abs(i // 3 - j // 3) + abs(i % 3 - j % 3)
    return tong

def la_giai_duoc(tt):
    """8-puzzle giải được khi số nghịch thế của dãy (bỏ ô trống) là số chẵn."""
    day = [x for x in tt if x != 0]
    nghich_the = sum(1 for i in range(8) for j in range(i + 1, 8) if day[i] > day[j])
    return nghich_the % 2 == 0

def in_bang(tt):
    """In cấu hình bảng 3x3 ra màn hình trực quan."""
    for i in range(0, 9, 3):
        print(" ".join(str(x) if x else "_" for x in tt[i:i + 3]))
