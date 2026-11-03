"""
Bài tập 1.8 — Tự tạo mê cung khiến Greedy Best-First đi đường vòng / rơi vào bẫy
File: bt_1_8_maze_trap.py

Mục tiêu:
Thiết kế một mê cung có chướng ngại vật dạng túi lõm (chữ U) quay lưng về phía xuất phát
và hứng về phía đích, hoặc chắn ngay hướng đi thẳng đến đích G.
Do hàm heuristic Manhattan h(o) = |r - rG| + |c - cG| chỉ đo khoảng cách đường chim bay,
Greedy Best-First sẽ bị "lừa" đâm đầu vào đáy bẫy (nơi h nhỏ nhất) trước khi buộc phải
quay đầu đi vòng, dẫn tới mở rộng nhiều nút dư thừa và tìm đường kém tối ưu so với BFS.
"""

from collections import deque
from s1_greedy_common import greedy_best_first
from maze_common import manhattan, ve_duong_di

# Mê cung có bẫy chữ U chắn giữa S và G:
# Đường đi thẳng dẫn vào ngõ cụt hình chữ U; đường vòng phía trên thoáng hơn.
MAZE_TRAP = [
    "S.......",
    "..#####.",
    "..#...#.",
    "..#.#.#.",
    "....#..G",
]

def tim_o_trong(ky_tu, maze):
    for r, hang in enumerate(maze):
        for c, ch in enumerate(hang):
            if ch == ky_tu:
                return (r, c)
    return None

def ke_maze_trap(o, maze=MAZE_TRAP):
    r, c = o
    for dr, dc, ten in [(-1, 0, "Lên"), (1, 0, "Xuống"), (0, -1, "Trái"), (0, 1, "Phải")]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and maze[nr][nc] != "#":
            yield ten, (nr, nc)

def bfs_maze(start, goal, ke_fn):
    """BFS để tìm đường đi ngắn nhất tuyệt đối làm chuẩn đối chiếu."""
    hang_doi = deque([(start, [])])
    visited = {start}
    so_mo = 0
    while hang_doi:
        curr, duong = hang_doi.popleft()
        so_mo += 1
        if curr == goal:
            return duong, so_mo
        for ten, moi in ke_fn(curr):
            if moi not in visited:
                visited.add(moi)
                hang_doi.append((moi, duong + [(ten, moi)]))
    return None, so_mo

if __name__ == "__main__":
    start = tim_o_trong("S", MAZE_TRAP)
    goal = tim_o_trong("G", MAZE_TRAP)

    print("=== BÀI TẬP 1.8: THIẾT KẾ MÊ CUNG KHIẾN GREEDY ĐI VÒNG / BỊ BẪY ===")
    print("Mê cung bẫy:")
    print("\n".join(MAZE_TRAP))
    print(f"\nXuất phát S: {start}, Đích G: {goal}\n")

    # 1. Chạy Greedy Best-First
    duong_greedy, mo_greedy = greedy_best_first(
        start,
        lambda o: o == goal,
        lambda o: ke_maze_trap(o, MAZE_TRAP),
        lambda o: manhattan(o, goal)
    )

    # 2. Chạy BFS (Tối ưu)
    duong_bfs, mo_bfs = bfs_maze(start, goal, lambda o: ke_maze_trap(o, MAZE_TRAP))

    print(f"[GREEDY BEST-FIRST]: Mở {mo_greedy} nút, Đường đi: {len(duong_greedy)} bước")
    print(ve_duong_di([o for _, o in duong_greedy], MAZE_TRAP))
    print()

    print(f"[BFS - TỐI ƯU TOÀN CỤC]: Mở {mo_bfs} nút, Đường đi: {len(duong_bfs)} bước")
    print(ve_duong_di([o for _, o in duong_bfs], MAZE_TRAP))

    print("\n[NHẬN XÉT BT 1.8]:")
    print("- Heuristic Manhattan chỉ nhìn khoảng cách thẳng tới G, nên kéo Greedy Best-First")
    print("  chạy sâu vào lòng chướng ngại vật trước khi phát hiện ngõ cụt và phải quay lui.")
    print("- Điều này chứng minh Greedy Best-First không đảm bảo tìm ra đường đi ngắn nhất,")
    print("  đặt nền tảng cho việc cần bổ sung hàm chi phí g(n) trong thuật toán A* (sẽ học ở các bài sau).")
