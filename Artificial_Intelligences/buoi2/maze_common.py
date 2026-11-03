"""
Cấu trúc dữ liệu và hàm dùng chung cho bài toán Mê Cung (kế thừa từ Buổi 1)
File: maze_common.py

Mê cung trên lưới 2 chiều:
  'S': Điểm xuất phát (Start)
  'G': Điểm đích (Goal)
  '#': Tường cản, không đi qua được
  '.': Đường đi tự do
"""

MAZE = [
    "S.#.....",
    ".##.###.",
    "....#...",
    ".####.#.",
    "......#G",
]

def tim_o(ky_tu, maze=MAZE):
    """Tìm toạ độ (hàng, cột) của ký tự trong mê cung."""
    for r, hang in enumerate(maze):
        for c, ch in enumerate(hang):
            if ch == ky_tu:
                return (r, c)
    return None

START = tim_o("S", MAZE)
GOAL = tim_o("G", MAZE)

def ke_me_cung(o, maze=MAZE):
    """Toán tử: đi Lên/Xuống/Trái/Phải sang ô kề không phải tường '#'."""
    r, c = o
    cac_huong = [
        (-1, 0, "Lên"),
        (1, 0, "Xuống"),
        (0, -1, "Trái"),
        (0, 1, "Phải"),
    ]
    for dr, dc, ten in cac_huong:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and maze[nr][nc] != "#":
            yield ten, (nr, nc)

def manhattan(a, b):
    """Khoảng cách Manhattan giữa 2 toạ độ a=(r1, c1) và b=(r2, c2)."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def ve_duong_di(cac_o, maze=MAZE):
    """Vẽ đường đi bằng cách thay thế các ô '.' thành '*'."""
    luoi = [list(h) for h in maze]
    for r, c in cac_o:
        if luoi[r][c] == ".":
            luoi[r][c] = "*"
    return "\n".join("".join(h) for h in luoi)
