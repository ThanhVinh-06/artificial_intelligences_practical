"""
Ví dụ 1.10 — Mê cung trên lưới với heuristic Manhattan
File: s1_maze_greedy.py
Sử dụng thuật toán Greedy Best-First với hàm heuristic Manhattan để tìm đường trong mê cung.
"""

from s1_greedy_common import greedy_best_first
from maze_common import MAZE, START, GOAL, ke_me_cung, manhattan, ve_duong_di

if __name__ == "__main__":
    print("=== VÍ DỤ 1.10: TÌM ĐƯỜNG TRONG MÊ CUNG BẰNG GREEDY BEST-FIRST ===")
    print("Mê cung gốc:")
    print("\n".join(MAZE))
    print(f"\nĐiểm bắt đầu S: {START}, Đích G: {GOAL}")

    duong, so_mo = greedy_best_first(
        START,
        lambda o: o == GOAL,
        ke_me_cung,
        lambda o: manhattan(o, GOAL)
    )

    print("\n[KẾT QUẢ TÌM KIẾM]:")
    print("Số nút đã mở rộng:", so_mo)
    print("Độ dài đường đi  :", len(duong), "bước")
    print("Đường đi tìm được trên mê cung:")
    print(ve_duong_di([o for _, o in duong]))
