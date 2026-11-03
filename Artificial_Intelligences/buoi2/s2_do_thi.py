"""
Ví dụ 2.1 — BFS và DFS trên đồ thị
Đoạn mã 16 — s2_do_thi.py
Cài đặt BFS (hàng đợi deque), DFS dùng ngăn xếp, và DFS đệ quy trên đồ thị danh sách kề.
"""

from collections import deque

DO_THI = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": ["H"],
    "F": ["H"],
    "G": [],
    "H": [],
}

def bfs(do_thi, dau, dich):
    bien = deque([dau])              # hàng đợi FIFO
    cha = {dau: None}
    thu_tu = []
    while bien:
        u = bien.popleft()           # lấy từ ĐẦU hàng đợi
        thu_tu.append(u)
        if u == dich:
            break
        for v in do_thi[u]:
            if v not in cha:
                cha[v] = u
                bien.append(v)       # thêm vào CUỐI hàng đợi
    return thu_tu, cha

def dfs(do_thi, dau, dich):
    bien = [dau]                     # ngăn xếp LIFO
    cha = {dau: None}
    thu_tu = []
    while bien:
        u = bien.pop()               # lấy từ ĐỈNH ngăn xếp
        thu_tu.append(u)
        if u == dich:
            break
        for v in reversed(do_thi[u]):  # đảo để nút con ĐẦU TIÊN được xét trước
            if v not in cha:
                cha[v] = u
                bien.append(v)
    return thu_tu, cha

def dung_duong(cha, dich):
    duong = []
    while dich is not None:
        duong.append(dich)
        dich = cha.get(dich)
    return duong[::-1]

def dfs_de_quy(do_thi, u, da_tham=None):
    if da_tham is None:
        da_tham = []
    da_tham.append(u)
    for v in do_thi[u]:
        if v not in da_tham:
            dfs_de_quy(do_thi, v, da_tham)
    return da_tham

if __name__ == "__main__":
    for ten, ham in [("BFS", bfs), ("DFS", dfs)]:
        thu_tu, cha = ham(DO_THI, "A", "H")
        print(f"{ten}: thứ tự xét {thu_tu}")
        print(f"    đường đi tới H: {dung_duong(cha, 'H')}")

    print("DFS đệ quy (duyệt toàn đồ thị):", dfs_de_quy(DO_THI, "A"))
