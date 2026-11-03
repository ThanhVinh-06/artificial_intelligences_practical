"""
Ví dụ 1.6 — Sắp lịch công việc theo lợi nhuận và hạn chót (Job Sequencing with Deadlines)
File: s1_job.py
Áp dụng nguyên lý thứ tự: sắp xếp công việc theo lợi nhuận giảm dần,
rồi xếp mỗi việc vào khung giờ trống muộn nhất có thể trước hạn chót.
"""

def job_sequencing(jobs):
    """
    jobs: list các tuple (ten, han_chot, loi_nhuan)
    """
    # Nguyên lý thứ tự: ưu tiên xét công việc có lợi nhuận cao nhất trước
    jobs_sorted = sorted(jobs, key=lambda x: x[2], reverse=True)
    
    max_deadline = max(job[1] for job in jobs)
    slots = [None] * (max_deadline + 1)  # slots[0] không dùng
    total_profit = 0
    schedule = []
    skipped = []
    
    for name, deadline, profit in jobs_sorted:
        # Tìm khung giờ trống muộn nhất có thể, tính từ hạn chót lùi về
        for t in range(deadline, 0, -1):
            if slots[t] is None:
                slots[t] = name
                total_profit += profit
                schedule.append((t, name))
                break
        else:
            # Vòng for không break -> không còn chỗ trống hợp lệ
            skipped.append((name, profit))
            
    schedule.sort()  # Sắp xếp lại theo thứ tự thời gian khung giờ
    return schedule, total_profit, skipped

if __name__ == "__main__":
    jobs = [
        ("A", 2, 100),
        ("B", 1, 19),
        ("C", 2, 27),
        ("D", 1, 25),
        ("E", 3, 15)
    ]

    schedule, profit, skipped = job_sequencing(jobs)
    print("=== VÍ DỤ 1.6: SẮP LỊCH CÔNG VIỆC THEO LỢI NHUẬN VÀ HẠN CHÓT ===")
    print("Lịch thực hiện (khung giờ, công việc):", schedule)
    print("Tổng lợi nhuận:", profit)
    print("Bị bỏ qua:", skipped, "-> mất", sum(p for _, p in skipped))
