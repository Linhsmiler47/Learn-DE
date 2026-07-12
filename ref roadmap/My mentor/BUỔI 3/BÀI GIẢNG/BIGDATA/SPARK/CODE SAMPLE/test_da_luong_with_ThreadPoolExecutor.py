import logging
import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Cấu hình logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)s] %(message)s",
    handlers=[
        logging.FileHandler("log_count.txt", mode="w", encoding="utf-8"),  # Ghi log vào file
        logging.StreamHandler()  # Hiển thị log ra màn hình (tùy chọn)
    ]
)

def count_word_in_chunk(chunk, word, result, index , line_offset ):
    """Đếm số lần xuất hiện của từ trong một khối dữ liệu"""
    logging.info(f"Start found {word} in part_index {index}")
    total_count = 0
    for i, line in enumerate(chunk):
        if word in line:
            num_count = line.count(word)
            total_count += num_count
    result[index] = total_count
    logging.info(f"Found {total_count} '{word}' at part_index : {index}")

def count_word(file_path, word, num_parts=8, num_threads=4):
    """Đếm số lần xuất hiện của từ trong file với việc chia nhỏ khối ngay khi đọc"""
    results = [0] * num_parts
    with open(file_path, 'r', encoding='utf-8') as f:
        # Đọc tổng số dòng để tính kích thước mỗi phần
        # begin_time
        begin_time = time.time()
        logging.info("Bắt đầu đọc file: %s", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(begin_time)))
        total_lines = sum(1 for _ in f)
        
        end_time = time.time()
        logging.info("Kết thức đọc file: %s", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time)))
        print(total_lines)
        return
        f.seek(0)  # Quay lại đầu file

        chunk_size = total_lines // num_parts
        current_line = 0  # Đếm vị trí dòng hiện tại

        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = []
            for part_index in range(num_parts):
                # Lấy khối dữ liệu
                chunk = [f.readline() for _ in range(chunk_size)]
                # Xử lý phần dư ở cuối file
                if part_index == num_parts - 1:
                    chunk.extend(f.readlines())

                # Tạo luồng xử lý khối
                futures.append(executor.submit(count_word_in_chunk, chunk, word, results, part_index, current_line))
                # Cập nhật dòng bắt đầu cho khối tiếp theo
                current_line += len(chunk)
                print(part_index)
            # Đảm bảo rằng tất cả các luồng hoàn thành
            for future in futures:
                future.result()

    return sum(results)

# Đường dẫn file và từ cần tìm
file_path = r'C:\Users\Admin\Desktop\output\citizens_data.csv'
word = input("Nhập từ cần tìm: ").strip()

# Đếm số lần xuất hiện của từ
start_time = time.time()
logging.info("Start time: %s", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time)))

count = count_word(file_path, word)
print(f"Từ '{word}' xuất hiện {count} lần trong file.")

end_time = time.time()
logging.info("End time: %s", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time)))

# Tính tổng thời gian chạy
elapsed_time = end_time - start_time
logging.info("Elapsed time: %.2f seconds", elapsed_time)
