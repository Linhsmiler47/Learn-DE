import dask.dataframe as dd 
import logging
import time

# Cấu hình logging
logging.basicConfig(
    format="%(asctime)s [%(threadName)s] %(message)s",  # Định dạng log
    level=logging.INFO,   # Mức độ log: DEBUG, INFO, WARNING, ERROR, CRITICAL
    handlers=[
        logging.FileHandler("log_pydask.log", mode="w", encoding="utf-8"),  # Ghi log vào file
        logging.StreamHandler()  # Hiển thị log ra màn hình (tùy chọn)
    ]
)

total_memory = 4 * 1024**3  # 8GB in bytes
num_cores = 8
scaling_factor = 0.2  # Có thể điều chỉnh

blocksize = (total_memory / num_cores) * scaling_factor
print(blocksize)  # Kết quả khoảng 512MB


def count_word(file_path,word):
    column1 = "country"
    column2 = "name"
    # Đọc file CSV lớn bằng Dask 
    #begin_time = time.time()
    #logging.info("Start Read file: %s", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(begin_time)))
    #df = dd.read_csv(file_path,blocksize=25e6) : chỗ này mặc định dask đã tự tối ưu đối với máy tính local
    
    df = dd.read_csv(file_path) 
    #begin_time = time.time()
    #logging.info("End Read file: %s", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(begin_time)))
    # Thực hiện các thao tác tương tự Pandas 
    df_filtered = df[(df[column1].str.contains(word)) | (df[column2].str.contains(word))]
    # Lưu kết quả ra file 
    filtered_df_len = len(df_filtered.compute())
    print(filtered_df_len)
    return filtered_df_len


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



