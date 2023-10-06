import os
import random
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import shutil

# Nhập đường dẫn đến thư mục input và output sau khi chạy code
input_folder = input("Nhập đường dẫn đến thư mục input: ")
output_folder = input("Nhập đường dẫn đến thư mục output: ")
error_folder = os.path.join(input_folder, "error")

# Tạo thư mục error nếu chưa tồn tại
os.makedirs(error_folder, exist_ok=True)

def process_videos(input_folder, output_folder, error_folder):
    # Lặp qua tất cả các tệp tin trong thư mục input
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp4"):
            input_path = os.path.join(input_folder, filename)
            
            # Tạo tên tệp tin đầu ra
            output_filename = f"output_{filename}"
            output_path = os.path.join(output_folder, output_filename)
            
            try:
                # Lấy một khoảng ngẫu nhiên từ video
                start_time = random.randint(0, 10)  # Chọn thời điểm bắt đầu ngẫu nhiên (0 - 10 giây)
                end_time = start_time + random.randint(3, 5)  # Kết thúc sau 3-5 giây
                
                # Trích xuất phần video và lưu vào thư mục output
                ffmpeg_extract_subclip(input_path, start_time, end_time, targetname=output_path)
            
            except Exception as e:
                print(f"Lỗi xảy ra với video {filename}: {e}")
                # Di chuyển video lỗi không cắt được vào thư mục error
                shutil.move(input_path, os.path.join(error_folder, filename))

# Thực hiện xử lý video
process_videos(input_folder, output_folder, error_folder)
