import logging
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import time
import psutil
from pyspark import TaskContext
import socket

# Cấu hình logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',  # Định dạng log
    level=logging.INFO,   # Mức độ log: DEBUG, INFO, WARNING, ERROR, CRITICAL
    handlers=[
        logging.FileHandler("log_pyspark.log", mode="w", encoding="utf-8"),  # Ghi log vào file
        logging.StreamHandler()  # Hiển thị log ra màn hình (tùy chọn)
    ]
)

# Tạo SparkSession và chỉ định master node
spark = SparkSession.builder \
    .appName("Submit Job to Master") \
    .master("spark://172.30.2.98:7077") \
    .config("spark.submit.deployMode", "cluster") \
    .getOrCreate()

def find_word_in_csv_pyspark(file_path, search_word, column_name):
    """
    Tìm kiếm một từ trong file CSV sử dụng PySpark và ghi log ra file.
    
    Args:
        file_path (str): Đường dẫn tới file CSV.
        search_word (str): Từ cần tìm.
        column_name (str): Tên cột cần tìm trong file CSV.
    
    Returns:
        DataFrame: DataFrame chứa các dòng khớp từ cần tìm.
    """
    try:
        
        logging.info("Spark session started successfully.")
        
        # Đường dẫn tới file
        header_file = "/root/data_sample/splitfiles/citizens_data_spit_1.csv"  # File chứa header
        data_files = "/root/data_sample/splitfiles/*.txt"  # Các file không có header (dùng ký tự đại diện)
        
        logging.info("Begin Read CSV Files.")
        # Đọc file header để lấy schema
        header_df = spark.read.csv(header_file, header=True, inferSchema=True)
        schema = header_df.schema  # Lấy schema từ file header

        # Đọc các file còn lại sử dụng schema
        data_df = spark.read.csv(data_files, header=False, schema=schema)
        
        logging.info("End Read CSV Files.")
        
        logging.info("Begin Find Word in Data.")
        # Ghép header vào dữ liệu
        full_df = header_df.union(data_df)
        
        # Kiểm tra số lượng partition trong DataFrame
        num_partitions = full_df.rdd.getNumPartitions()

        # In ra số partition
        logging.info(f"Số lượng partition: {num_partitions}")
               
        # Tìm kiếm từ khóa (không phân biệt hoa thường)
        logging.info(f"Searching for word '{search_word}' in column '{column_name}'...")
        filtered_df = full_df.filter(col(column_name).contains(search_word) | col('name').contains(search_word))

        # Đếm số dòng tìm được
        count = filtered_df.count()
        logging.info(f"Found {count} rows containing '{search_word}'.")
        logging.info("End Find Word in Data.")

        return filtered_df

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        raise
        
def log_task_info(partition):
    task_context = TaskContext.get()
    stage_id = task_context.stageId()  # Lấy Stage ID
    partition_id = task_context.partitionId()  # Lấy Partition ID
    attempt_id = task_context.attemptNumber()  # Lấy số lần thực hiện task
    worker_host = socket.gethostname()  # Lấy tên host của worker
    
    logging.info(f"Stage ID: {stage_id}, Partition ID: {partition_id}, Attempt: {attempt_id}, Worker Host: {worker_host}")
    return partition

# Ví dụ sử dụng
file_path = '/root/data_sample/citizens_data_spit_1.txt'  # Đường dẫn tới file CSV
search_word = "French"         # Từ cần tìm
column_name = "country"         # Tên cột cần tìm

# Đếm số lần xuất hiện của từ
start_time = time.time()
logging.info("Start time: %s", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time)))

try:
    filtered_df = find_word_in_csv_pyspark(file_path, search_word, column_name)
    #filtered_df.show(10)  # Hiển thị 10 dòng đầu tiên
    #filtered_df.write.csv("output_folder", header=True)  # Lưu kết quả vào file CSV
    #logging.info("Results written to 'output_folder'.")
except Exception as e:
    logging.critical(f"Critical failure: {str(e)}")

finally:
    # Đóng SparkSession
    spark.stop()

end_time = time.time()
logging.info("End time: %s", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time)))

# Tính tổng thời gian chạy
elapsed_time = end_time - start_time
logging.info("Elapsed time: %.2f seconds", elapsed_time)