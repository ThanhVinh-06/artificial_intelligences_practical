"""
Runner tổng hợp toàn bộ bài tập & ví dụ Buổi 1: Trí Tuệ Nhân Tạo
File: main.py
Thực hành: Nguyên lý tham lam (Greedy) & Nguyên lý thứ tự (Ordering)
"""

import sys
import os
import subprocess
from pathlib import Path

# Đảm bảo mã hoá đầu ra luôn hỗ trợ tốt tiếng Việt trên Windows terminal
if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

BUOI1_DIR = Path(__file__).parent

SCRIPTS = [
    ("Ví dụ 1.1: Cái túi phân số (Fractional Knapsack)", "s1_knapsack_frac.py"),
    ("Ví dụ 1.2: Cái túi 0/1 (Tham lam vs Vét cạn)", "s1_knapsack_01.py"),
    ("Ví dụ 1.3: Bài toán đổi tiền", "s1_doi_tien.py"),
    ("Ví dụ 1.4: Chọn hoạt động (Activity Selection)", "s1_hoat_dong.py"),
    ("Bài tập 1.6: Phản ví dụ tiêu chí Thời lượng ngắn nhất", "bt_1_6_hoat_dong.py"),
    ("Ví dụ 1.5: Người bán hàng TSP (Nearest Neighbor vs Vét cạn)", "s1_tsp.py"),
    ("Ví dụ 1.6: Sắp lịch công việc (Job Sequencing)", "s1_job.py"),
    ("Ví dụ 1.7: Hàng đợi ưu tiên với heapq", "s1_heapq_demo.py"),
    ("Ví dụ 1.8: Best-First tối giản trên trục số", "s1_pq.py"),
    ("Ví dụ 1.10: Tìm đường trong mê cung với Manhattan Heuristic", "s1_maze_greedy.py"),
    ("Bài tập 1.8: Mê cung bẫy khiến Greedy đi đường vòng", "bt_1_8_maze_trap.py"),
    ("Ví dụ 1.11: 8-Puzzle với hai hàm Heuristic (h1 và h2)", "s1_8puzzle.py"),
]

def run_script(script_name):
    script_path = BUOI1_DIR / script_name
    print("=" * 75)
    print(f" Đang thực thi: {script_name}")
    print("=" * 75)
    
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    
    res = subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        cwd=str(BUOI1_DIR),
        env=env
    )
    if res.stdout:
        print(res.stdout)
    if res.stderr:
        print("[LỖI]:", res.stderr)
    print()

def main():
    print("*" * 75)
    print(" BÀI GIẢNG THỰC HÀNH TRÍ TUỆ NHÂN TẠO - BUỔI 1")
    print(" Chủ đề: Nguyên lý tham lam (Greedy) & Nguyên lý thứ tự (Ordering)")
    print("*" * 75)
    print("\nDanh sách chức năng:")
    print(" 0. Chạy TẤT CẢ các ví dụ và bài tập")
    for idx, (title, fname) in enumerate(SCRIPTS, start=1):
        print(f"{idx:2d}. {title} ({fname})")
    print(" Q. Thoát")

    choice = input("\nNhập lựa chọn của bạn [0 để chạy tất cả]: ").strip()
    if choice.lower() in ["q", "exit", "quit"]:
        return

    if choice == "0" or choice == "":
        for _, fname in SCRIPTS:
            run_script(fname)
    else:
        try:
            val = int(choice)
            if 1 <= val <= len(SCRIPTS):
                run_script(SCRIPTS[val - 1][1])
            else:
                print("Lựa chọn không hợp lệ!")
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")

if __name__ == "__main__":
    main()
