import threading
import logging
import time
import os

"""

"""
def split_file(input_file, num_parts, output_dir,output_prefix):
    
    # Tạo thư mục đích nếu chưa tồn tại
    os.makedirs(output_dir, exist_ok=True)
    
    with open(input_file, 'r',encoding='utf-8') as file:
        lines = file.readlines()
    
    total_lines = len(lines)
    lines_per_part = total_lines // num_parts
    remainder = total_lines % num_parts

    start = 0
    for i in range(num_parts):
        end = start + lines_per_part + (1 if i < remainder else 0)
        output_path = os.path.join(output_dir, f"{output_prefix}_{i+1}.txt")
        with open(output_path, 'w',encoding='utf-8') as output_file:
            output_file.writelines(lines[start:end])
        start = end



if __name__ == "__main__":

    # Cấu hình logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(threadName)s] %(message)s",
        handlers=[
            logging.FileHandler("log_{__name__}.txt", mode="w", encoding="utf-8"),  # Ghi log vào file
            logging.StreamHandler()  # Hiển thị log ra màn hình (tùy chọn)
        ]
    )
    # Đường dẫn file và từ cần tìm
    file_path = r'C:\Users\Admin\Desktop\output\citizens_data.csv'
    #word = input("Nhập từ cần tìm: ").strip()
    
    output_dir = r"C:\Users\Admin\Desktop\output\splitfiles"
    output_prefix = "citizens_data_spit"
    # Đếm số lần xuất hiện của từ
    start_time = time.time()
    logging.info("Start time: %s", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time)))

    # Sử dụng hàm:
    split_file(file_path, 51, output_dir, output_prefix)

    end_time = time.time()
    logging.info("Start time: %s", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time)))

    # Tính tổng thời gian chạy
    elapsed_time = end_time - start_time
    logging.info("Elapsed time: %.2f seconds", elapsed_time)
