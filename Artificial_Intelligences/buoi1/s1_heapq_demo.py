"""
Ví dụ 1.7 — Hàng đợi ưu tiên với heapq
File: s1_heapq_demo.py
Demo cấu trúc Min-Heap trong thư viện chuẩn của Python:
- heapq luôn lấy phần tử có độ ưu tiên nhỏ nhất trước trong O(log n).
- Nếu độ ưu tiên bằng nhau, Python tiếp tục so sánh trường dữ liệu tiếp theo.
"""

import heapq

def demo_heapq():
    hang_doi = []
    viec = [
        (3, "Viết báo cáo"),
        (1, "Nộp học phí"),
        (2, "Họp khoa"),
        (1, "Chấm bài")
    ]
    
    for do_uu_tien, cong_viec in viec:
        heapq.heappush(hang_doi, (do_uu_tien, cong_viec))

    print("=== VÍ DỤ 1.7: HÀNG ĐỢI ƯU TIÊN VỚI HEAPQ ===")
    print("Thứ tự công việc được lấy ra (ưu tiên nhỏ nhất trước):")
    while hang_doi:
        item = heapq.heappop(hang_doi)
        print(f"  Ưu tiên {item[0]}: {item[1]}")

    print("\n[LƯU Ý]:")
    print("- 'Chấm bài' được lấy trước 'Nộp học phí' vì cùng ưu tiên 1, Python so sánh tiếp chuỗi ký tự.")
    print("- Nếu đối tượng không so sánh được (như dict, object), cần dùng thêm biến đếm làm khoá phá hoà (tie-breaker).")

if __name__ == "__main__":
    demo_heapq()
