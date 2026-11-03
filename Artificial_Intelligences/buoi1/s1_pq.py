"""
Ví dụ 1.8 — Best-First tối giản trên trục số
File: s1_pq.py
Minh hoạ trực tiếp nguyên lý thứ tự: duyệt các trạng thái theo thứ tự heuristic tốt dần.
Bài toán: đi từ start=0 đến goal=10 trên trục số nguyên 1 chiều.
Heuristic h(state) = |goal - state|.
"""

import heapq

def best_first_demo(start, goal, get_neighbors, heuristic):
    """
    start, goal: trạng thái bắt đầu / đích
    get_neighbors(state): trả về danh sách trạng thái kề
    heuristic(state, goal): ước lượng 'khoảng cách' tới đích, càng nhỏ càng tốt
    """
    visited = set()
    # Hàng đợi ưu tiên: (heuristic, state) -> heapq luôn lấy phần tử nhỏ nhất trước
    frontier = [(heuristic(start, goal), start)]
    
    while frontier:
        h, current = heapq.heappop(frontier)
        if current == goal:
            return current, h
        if current in visited:
            continue
        visited.add(current)
        print(f"Đang xét trạng thái: {current} (heuristic = {h})")
        
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                heapq.heappush(frontier, (heuristic(neighbor, goal), neighbor))
                
    return None, None

# Các hàm phụ trợ cho trục số 1D
def get_neighbors(state):
    return [state - 1, state + 1]

def heuristic(state, goal):
    return abs(goal - state)

if __name__ == "__main__":
    print("=== VÍ DỤ 1.8: BEST-FIRST TỐI GIẢN TRÊN TRỤC SỐ ===")
    result, h = best_first_demo(0, 10, get_neighbors, heuristic)
    print("Đến đích:", result)
