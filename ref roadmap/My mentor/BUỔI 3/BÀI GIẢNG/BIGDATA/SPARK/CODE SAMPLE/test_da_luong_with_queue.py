import threading
import time
import logging
from queue import Queue

"""
ĐA LUỒNG VỚI THREADS kết hợp với queue để chạy không cần wait
"""


# Cấu hình logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)s] %(message)s",
    handlers=[
        logging.FileHandler("log_count_with_queue.log", mode="w", encoding="utf-8"),  # Ghi log vào file
        logging.StreamHandler()  # Hiển thị log ra màn hình (tùy chọn)
    ]
)

def count_word_in_chunk(chunk, word):
    """Đếm số lần xuất hiện của từ trong một khối dữ liệu"""
    total_count = 0
    for line in chunk:
        total_count += line.count(word)
    return total_count

def worker(queue, word, results, lock, current_line_ref, file_path, chunk_size_input, file_lock):
    """Luồng xử lý: Lấy dữ liệu từ hàng đợi và xử lý"""
    while True:
        try:
            part_index = queue.get_nowait()  # Lấy chỉ mục phần từ hàng đợi
        except:
            break

        # Đọc dữ liệu từ file khi có luồng rảnh
        with file_lock:
            with open(file_path, 'r', encoding='utf-8') as f:
                f.seek(current_line_ref[0])  # Đọc từ vị trí dòng hiện tại
                chunk = [f.readline() for _ in range(chunk_size_input)]
                # Cập nhật vị trí dòng hiện tại
                current_line_ref[0] = f.tell()

        # Xử lý khối
        count = count_word_in_chunk(chunk, word)
        with lock:
            results[part_index] = count  # Lưu kết quả

        logging.info(f"Thread finished part_index {part_index}, Found {count} '{word}'")
        queue.task_done()  # Đánh dấu công việc hoàn thành

def count_word(file_path, word, num_parts=40, num_threads=8):
    """Đếm số lần xuất hiện của từ trong file"""
    results = [0] * num_parts
    task_queue = Queue()
    lock = threading.Lock()  # Để bảo vệ vùng ghi dữ liệu
    file_lock = threading.Lock()  # Để bảo vệ việc đọc tuần tự từ file
    current_line_ref = [0]  # Tham chiếu vị trí đọc hiện tại trong file

    # Tính tổng số dòng và kích thước mỗi phần
    with open(file_path, 'r', encoding='utf-8') as f:
        total_lines = sum(1 for _ in f)
        chunk_size = total_lines // num_parts

    # Đưa chỉ mục công việc vào hàng đợi
    for part_index in range(num_parts):
        task_queue.put(part_index)

    # Tạo các luồng
    threads = []
    for i in range(num_threads):
        #chunk_size_input = chunk_size
        #if i % 2 == 0:
        #   chunk_size_input = chunk_size_input * 2
        t = threading.Thread(target=worker, args=(task_queue, word, results, lock, current_line_ref, file_path, chunk_size_input, file_lock))
        t.start()
        threads.append(t)

    # Chờ tất cả các luồng hoàn thành
    for t in threads:
        t.join()

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