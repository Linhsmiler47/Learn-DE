import pandas as pd
import logging
import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Cấu hình logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)s] %(message)s",
    handlers=[
        logging.FileHandler("log_threadpool_pandas.log", mode="w", encoding="utf-8"),  # Ghi log vào file
        logging.StreamHandler()  # Hiển thị log ra màn hình (tùy chọn)
    ]
)

def read_chunk(start, end, file_path):
    # Đọc phần của file từ start đến end
    return pd.read_csv(file_path, skiprows=range(1, start), nrows=end-start)

# Đếm số lần xuất hiện của từ
start_time = time.time()
logging.info("Start time: %s", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time)))

file_path = r'C:\Users\Admin\Desktop\output\citizens_data.csv'
num_threads = 8  # Số luồng bạn muốn

# Lấy tổng số dòng trong file
total_lines = sum(1 for _ in open(file_path))

# Tính kích thước mỗi phần
chunk_size = total_lines // num_threads

# Sử dụng ThreadPoolExecutor để đọc song song
with ThreadPoolExecutor(max_workers=num_threads) as pool:
    futures = [pool.submit(read_chunk, i * chunk_size, (i + 1) * chunk_size if i != num_threads - 1 else total_lines, file_path) for i in range(num_threads)]
    chunks = [future.result() for future in futures]

# Gộp các phần lại thành một DataFrame
df = pd.concat(chunks, ignore_index=True)
search_word = "French"
filtered_df = df.filter(col('country').contains(search_word))

# Đếm số dòng tìm được
count = filtered_df.count()
logging.info(f"Found {count} rows containing '{search_word}'.")


end_time = time.time()
logging.info("End time: %s", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time)))

# Tính tổng thời gian chạy
elapsed_time = end_time - start_time
logging.info("Elapsed time: %.2f seconds", elapsed_time)