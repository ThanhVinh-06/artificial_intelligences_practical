"""
Ví dụ 2.7 — DLS và IDDFS (Định nghĩa thuật toán)
Đoạn mã 22 — s2_dls_def.py
DLS và IDDFS viết bằng đệ quy để chỉ lưu đường đi hiện tại (bộ nhớ O(bd)).
Tránh vòng lặp bằng cách không quay lại các tổ tiên của nút hiện tại.
"""

def dls(bt, tt, gioi_han, duong, dem):
    """Tìm kiếm sâu có giới hạn (đệ quy).
    Trả về: đường đi | "cutoff" (bị cắt do hết giới hạn) | None (vô nghiệm trong nhánh)."""
    dem[0] += 1
    if bt.la_dich(tt):
        return duong
    if gioi_han == 0:
        return "cutoff"
    bi_cat = False
    tren_duong = {bt.dau} | {x[1] for x in duong}     # tránh quay lại tổ tiên (chống vòng lặp)
    for ten, moi in bt.ke(tt):
        if moi in tren_duong:
            continue
        kq = dls(bt, moi, gioi_han - 1, duong + [(ten, moi)], dem)
        if kq == "cutoff":
            bi_cat = True
        elif kq is not None:
            return kq
    return "cutoff" if bi_cat else None

def iddfs(bt, gh_toi_da=30, in_log=False):
    """Tìm kiếm sâu dần: DLS với giới hạn 0, 1, 2, ... cho tới khi gặp lời giải."""
    tong_nut = 0
    for gh in range(gh_toi_da + 1):
        dem = [0]
        kq = dls(bt, bt.dau, gh, [], dem)
        tong_nut += dem[0]
        if in_log:
            print(f"  giới hạn {gh:2d}: thăm {dem[0]:6d} nút -> {'cutoff' if kq == 'cutoff' else 'xong'}")
        if kq != "cutoff":
            return kq, tong_nut
    return None, tong_nut
