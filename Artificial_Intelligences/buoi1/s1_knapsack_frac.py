"""
Ví dụ 1.1 — Bài toán cái túi phân số (Fractional Knapsack)
File: s1_knapsack_frac.py
Chiến lược tham lam: sắp xếp theo tỉ lệ giá trị / trọng lượng giảm dần.
"""

def greedy_knapsack(items, capacity):
    """
    items: list các tuple (ten, gia_tri, trong_luong)
    capacity: sức chứa túi
    """
    # Sắp theo tỉ lệ giá trị/trọng lượng giảm dần -> "nguyên lý thứ tự"
    items_sorted = sorted(items, key=lambda x: x[1] / x[2], reverse=True)
    
    total_value = 0.0
    total_weight = 0.0
    chosen = []
    
    for name, value, weight in items_sorted:
        if total_weight + weight <= capacity:
            chosen.append(name)
            total_weight += weight
            total_value += value
        else:
            # Cho phép lấy phần lẻ (fractional knapsack)
            remain = capacity - total_weight
            if remain > 0:
                fraction = remain / weight
                chosen.append(f"{name} ({fraction:.2f} phần)")
                total_value += value * fraction
                total_weight = capacity
            break
            
    return chosen, total_value, total_weight


if __name__ == "__main__":
    items = [
        ("Kim cương", 100, 2),
        ("Vàng", 60, 3),
        ("Bạc", 40, 5),
        ("Gạo", 10, 8),
    ]
    capacity = 7

    chosen, value, weight = greedy_knapsack(items, capacity)
    print("=== VÍ DỤ 1.1: BÀI TOÁN CÁI TÚI PHÂN SỐ (FRACTIONAL KNAPSACK) ===")
    print("Các món được chọn:", chosen)
    print("Tổng giá trị:", value)
    print("Tổng trọng lượng:", weight, "/", capacity)
