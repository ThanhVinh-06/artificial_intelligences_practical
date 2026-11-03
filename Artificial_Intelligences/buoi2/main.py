"""
Runner tổng hợp toàn bộ ví dụ & bài tập Buổi 2: Trí Tuệ Nhân Tạo
File: main.py
Thực hành: Tìm kiếm mù (Uninformed / Blind Search: BFS, DFS, DLS, IDDFS)
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

BUOI2_DIR = Path(__file__).parent

SCRIPTS = [
    ("Ví dụ 2.1: BFS và DFS trên đồ thị danh sách kề", "s2_do_thi.py"),
    ("Ví dụ 2.3: Bài toán đổ nước (Water Jugs)", "s2_binh_nuoc.py"),
    ("Bài tập 2.4: Khảo sát khi nào bài toán đổ nước vô nghiệm", "bt_2_4_binh_nuoc.py"),
    ("Ví dụ 2.4: Nông dân, sói, dê và bắp cải qua sông", "s2_nong_dan.py"),
    ("Ví dụ 2.5: Mê cung — So sánh BFS và DFS", "s2_me_cung.py"),
    ("Ví dụ 2.6: 8-Puzzle — So sánh BFS và DFS", "s2_8puzzle.py"),
    ("Ví dụ 2.7: Tìm kiếm sâu giới hạn (DLS) và sâu dần (IDDFS)", "s2_dls_demo.py"),
    ("Ví dụ 2.8: Bảng so sánh BFS, DFS, IDDFS trên 8-Puzzle", "s2_so_sanh.py"),
]

def run_script(script_name):
    script_path = BUOI2_DIR / script_name
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
        cwd=str(BUOI2_DIR),
        env=env,
    )
    if res.stdout:
        print(res.stdout)
    if res.stderr:
        print("[LỖI]:", res.stderr)
    print()

def main():
    print("*" * 75)
    print(" BÀI GIẢNG THỰC HÀNH TRÍ TUỆ NHÂN TẠO - BUỔI 2")
    print(" Chủ đề: Tìm kiếm mù (BFS, DFS, DLS, IDDFS)")
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
