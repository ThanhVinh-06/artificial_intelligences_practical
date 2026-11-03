"""
Ví dụ 2.4 — Nông dân, sói, dê và bắp cải
Đoạn mã 19 — s2_nong_dan.py
Nông dân phải đưa sói, dê, bắp cải qua sông trên một chiếc thuyền chỉ chở được nông dân
cùng nhiều nhất một vật. Khi nông dân vắng mặt, sói không được ở cùng dê, dê không được
ở cùng bắp cải. Trạng thái là bộ bốn (n, s, d, b) với 0 là bờ trái, 1 là bờ phải.
"""

from s2_khung import BaiToan, tim_kiem

# Trạng thái: (nông dân, sói, dê, bắp cải); 0 = bờ trái, 1 = bờ phải
TEN = ["Nông dân", "Sói", "Dê", "Bắp cải"]

def an_toan(tt):
    n, s, d, b = tt
    soi_an_de = (s == d and s != n)
    de_an_bap = (d == b and d != n)
    return not soi_an_de and not de_an_bap

def ke_nong_dan(tt):
    n = tt[0]
    huong = "sang bờ phải" if n == 0 else "về bờ trái"
    moi = (1 - n,) + tt[1:]           # nông dân đi một mình
    if an_toan(moi):
        yield f"Nông dân đi một mình {huong}", moi
    for i in (1, 2, 3):               # hoặc chở theo một thứ cùng bờ
        if tt[i] == n:
            l = list(tt)
            l[0] = l[i] = 1 - n
            moi = tuple(l)
            if an_toan(moi):
                yield f"Nông dân chở {TEN[i]} {huong}", moi

if __name__ == "__main__":
    bt = BaiToan((0, 0, 0, 0), lambda tt: tt == (1, 1, 1, 1), ke_nong_dan)
    duong, so_mo, _ = tim_kiem(bt, "bfs")

    print("Đầu:", (0, 0, 0, 0))
    for i, (ten, tt) in enumerate(duong, 1):
        print(f"{i}. {ten:34s} -> {tt}")
    print(f"Tổng {len(duong)} lần qua sông, đã mở rộng {so_mo} nút")
