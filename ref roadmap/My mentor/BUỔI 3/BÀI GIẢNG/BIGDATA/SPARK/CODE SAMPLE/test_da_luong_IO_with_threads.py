import threading
import logging
import time
import os

"""

"""

def get_matching_files(directory, keyword="citizens_data_spit"):
    """
    Lấy danh sách các file trong thư mục có chứa keyword trong tên.

    Args:
        directory (str): Đường dẫn thư mục.
        keyword (str): Cụm từ cần tìm trong tên file.

    Returns:
        list: Danh sách các file phù hợp.
    """
    try:
        # Kiểm tra thư mục có tồn tại
        if not os.path.exists(directory):
            print(f"Thư mục {directory} không tồn tại.")
            return []
        
        # Duyệt qua các file trong thư mục
        matching_files = [
            file for file in os.listdir(directory)
            if keyword in file and file.endswith('.txt')
        ]

        return matching_files
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
        return []

def read_file_in_chunks(filename,results,num_part_index,word, chunk_size=1024):
    """
    Hàm đọc file theo từng chunk và xử lý chunk đó.
    """
    total_count = 0
    logging.info(f"Bắt đầu đọc file: {filename}")
    with open(filename, 'r', encoding='utf-8') as f: # tác vụ cũng nhả CPU ra trả về cho main thread
        #thread gọi tới cpu và load data từ disk vào ram : đa luồng
        logging.info(f"Bắt đầu trả cho main thread")
        chunk = f.read() # thread waiting luồng đọc disk : nhả ra main
        logging.info(f"Bắt đầu đóng băng các thread khác để chạy thread thiện tại")
        total_count = chunk.count(word)  
    logging.info(f"Hoàn thành đọc file: {filename}")
    results[num_part_index] = total_count

def count_word(output_dir,list_files, word, num_threads=16):
    """Đếm số lần xuất hiện của từ trong file với việc chia nhỏ khối ngay khi đọc"""
    num_parts = len(list_files)
    results = [0] * num_parts
    threads = []
    # Kiểm tra số lượng thread đang chạy
    logging.info(f"Active threads count: {threading.active_count()}")
    
    # Danh sách thread
    threads = []

    # Tạo và bắt đầu thread
    for i, file in enumerate(list_files):
        input_file = os.path.join(output_dir, file)
        thread = threading.Thread(target=read_file_in_chunks, args=(input_file,results,i,word), name=f"Thread-{i+1}")
        threads.append(thread)
        thread.start()
        
        logging.info(f"Active threads count: {threading.active_count()}")
        # Đảm bảo chỉ chạy tối đa num_threads luồng cùng lúc
        if len(threads) == num_threads:
            #logging.info(f"Đủ số lượng {num_threads} threads tối đa : chờ hoàn thành hết để chạy tiếp")
            for t in threads:
               t.join()
            threads = []
            #logging.info(f"Hoàn thành 20 threads trong hàng đợi")
    # Chờ tất cả thread hoàn thành
    for thread in threads:
        thread.join()

    return sum(results)


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
    word = input("Nhập từ cần tìm: ").strip()
    
    
    output_dir = r"C:\Users\Admin\Desktop\output\splitfiles"
    output_prefix = "citizens_data_spit"
    # Đếm số lần xuất hiện của từ
    start_time = time.time()
    logging.info("Start time: %s", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time)))

    # Sử dụng hàm:
    # Lấy danh sách file
    matching_files = get_matching_files(output_dir,output_prefix)
    
    count = count_word(output_dir,matching_files, word)

    # In danh sách file
    #print("Các file phù hợp:")
    #for file in matching_files:
    #    print(file)
    

    print(f"Từ '{word}' xuất hiện {count} lần trong file.")
    end_time = time.time()
    logging.info("Start time: %s", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time)))

    # Tính tổng thời gian chạy
    elapsed_time = end_time - start_time
    logging.info("Elapsed time: %.2f seconds", elapsed_time)
