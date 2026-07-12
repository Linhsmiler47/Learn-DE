import logging
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import time
import psutil

# Cấu hình logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',  # Định dạng log
    level=logging.INFO,   # Mức độ log: DEBUG, INFO, WARNING, ERROR, CRITICAL
    handlers=[
        logging.FileHandler("log_pyspark.log", mode="w", encoding="utf-8"),  # Ghi log vào file
        logging.StreamHandler()  # Hiển thị log ra màn hình (tùy chọn)
    ]
)

# Tạo SparkSession
spark = SparkSession.builder \
.appName("Find Word in CSV with Logging") \
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
        
            
        #spark = SparkSession.builder \
        #.appName("Find Word in CSV with Logging") \
        #.config("spark.executor.memory", "1g") \
        #.config("spark.driver.memory", "1g") \
        #.config("spark.local.dir", r"C:/Users/Admin/Desktop/output/") \
        #.getOrCreate()    
        logging.info("Spark session started successfully.")

        # Đọc file CSV
        logging.info(f"Reading CSV file from path: {file_path}")
        df = spark.read.csv(file_path, header=True, inferSchema=True)
        
        # Kiểm tra số lượng partition trong DataFrame
        #num_partitions = df.rdd.getNumPartitions()

        # In ra số partition
        #print(f"Số lượng partition: {num_partitions}")
        
        #df.filter(df['review_id'].isNull()).show(10)
        
        #logging.info(f"total has : {df.count()} records'.")
        
        # Tìm kiếm từ khóa (không phân biệt hoa thường)
        logging.info(f"Searching for word '{search_word}' in column '{column_name}'...")
        filtered_df = df.filter(col(column_name).contains(search_word) | col('name').contains(search_word))

        # Đếm số dòng tìm được
        count = filtered_df.count()
        logging.info(f"Found {count} rows containing '{search_word}'.")

        return filtered_df

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        raise

# Ví dụ sử dụng
file_path = r'C:\Users\Admin\Desktop\output\citizens_data_small.csv'  # Đường dẫn tới file CSV
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