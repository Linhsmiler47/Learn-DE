import threading
import logging
import time

"""
ĐA LUỒNG VỚI THREADS chưa bao gồm queue

Lý do if __name__ == "__main__": là cần thiết:
Tránh việc file Python bị thực thi lại từ đầu mỗi lần tạo process con.
Bảo vệ mã khởi tạo process để chỉ thực thi khi file script được chạy trực tiếp (chứ không phải khi được process con gọi lại).
Đảm bảo chương trình chạy ổn định trên cả Windows, macOS và Linux.
Khi nào cần chú ý nhất đến điều này?
Windows/macOS: Luôn cần if __name__ == "__main__": vì không có cơ chế fork.
Linux: Không bắt buộc nhưng vẫn nên sử dụng để tránh lỗi khi triển khai đa nền tảng.

"""
def count_word_in_chunk(chunk, word, result, index , line_offset ):
    """Đếm số lần xuất hiện của từ trong một khối dữ liệu"""
    
    #logging.info(f"Thread current running : {threading.current_thread().ident}")
    logging.info(f"Thread current running : ")
    logging.info(f"Thread  vào ngủ đông, trả lại cho Main thread chạy")
    time.sleep(20)
    logging.info(f"Thread  đã hết ngủ đông bắt đầu xử lý tiếp ")
    #if index == 1:
    #    time.sleep(10)
    #if index == 2:
    #    time.sleep(15)
    #if index == 3:
    #    time.sleep(20)
    
    total_count = 0
    for i, line in enumerate(chunk):
        if word in line:
            #line_number = line_offset + i + 1
            num_count = line.count("French")
            total_count = total_count + num_count
            #logging.info(f"Running on CPU core {cpu_core} - Found {num_count} '{word}' in line {line_number} : {line.strip()}")
    result[index] = total_count
    logging.info(f"Found {total_count} '{word}' at part_index : {index}")

def count_word(file_path, word, num_parts=40, num_threads=8):
    """Đếm số lần xuất hiện của từ trong file với việc chia nhỏ khối ngay khi đọc"""
    results = [0] * num_parts
    threads = []
    # Kiểm tra số lượng thread đang chạy
    logging.info(f"Active threads count: {threading.active_count()}")
    with open(file_path, 'r', encoding='utf-8') as f:
        # Đọc tổng số dòng để tính kích thước mỗi phần
        total_lines = sum(1 for _ in f)
        f.seek(0)  # Quay lại đầu file

        chunk_size = total_lines // num_parts
        current_line = 0  # Đếm vị trí dòng hiện tại
        for part_index in range(num_parts):
            # Lấy khối dữ liệu
            chunk = [f.readline() for _ in range(chunk_size)]
            # Xử lý phần dư ở cuối file
            if part_index == num_parts - 1:
                chunk.extend(f.readlines())

            # Tạo luồng xử lý khối
            thread = threading.Thread(target=count_word_in_chunk, args=(chunk, word, results, part_index,current_line))
            threads.append(thread)
            thread.start()
            
            
            logging.info(f"Main thread được thread nhả CPU cho chạy tiếp")
            # Cập nhật dòng bắt đầu cho khối tiếp theo
            current_line += len(chunk)
            
            # Kiểm tra số lượng thread đang chạy
            logging.info(f"Active threads count: {threading.active_count()}")

            # Đảm bảo chỉ chạy tối đa num_threads luồng cùng lúc
            if len(threads) == num_threads:
                #logging.info(f"Đủ số lượng {num_threads} threads tối đa : chờ hoàn thành hết để chạy tiếp")
                logging.info(f"sinh ra đủ 8 thread , và main thread sẽ chờ 8 thread này chạy xong")
                for t in threads:
                   t.join()
                threads = []
                #logging.info(f"Hoàn thành 20 threads trong hàng đợi")

        # Join các luồng còn lại
        for t in threads:
            t.join()

    return sum(results)

if __name__ == "__main__":

    # Cấu hình logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(threadName)s] %(message)s",
        handlers=[
            logging.FileHandler("log_count.txt", mode="w", encoding="utf-8"),  # Ghi log vào file
            logging.StreamHandler()  # Hiển thị log ra màn hình (tùy chọn)
        ]
    )
    # Đường dẫn file và từ cần tìm
    file_path = r'C:\Users\Admin\Desktop\output\citizens_data.csv'
    word = input("Nhập từ cần tìm: ").strip()

    # Đếm số lần xuất hiện của từ
    start_time = time.time()
    logging.info("Start time: %s", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time)))

    count = count_word(file_path, word)
    print(f"Từ '{word}' xuất hiện {count} lần trong file.")

    end_time = time.time()
    logging.info("Start time: %s", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time)))

    # Tính tổng thời gian chạy
    elapsed_time = end_time - start_time
    logging.info("Elapsed time: %.2f seconds", elapsed_time)
