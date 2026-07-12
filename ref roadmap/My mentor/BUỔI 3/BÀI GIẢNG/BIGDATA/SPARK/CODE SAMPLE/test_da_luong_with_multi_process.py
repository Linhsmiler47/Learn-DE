import multiprocessing
import logging
import time

"""
ĐA LUỒNG VỚI THREADS chưa bao gồm queue
"""






def count_word_in_chunk(chunk, word, result, index , line_offset ):
    """Đếm số lần xuất hiện của từ trong một khối dữ liệu"""
    total_count = 0
    for i, line in enumerate(chunk):
        if word in line:
            #line_number = line_offset + i + 1
            num_count = line.count("French")
            total_count = total_count + num_count
            #logging.info(f"Running on CPU core {cpu_core} - Found {num_count} '{word}' in line {line_number} : {line.strip()}")
    result[index] = total_count
    logging.info(f"Found {total_count} '{word}' at part_index : {index}")

def count_word(file_path, word, num_parts=40, num_processes=8):
    """Đếm số lần xuất hiện của từ trong file với việc chia nhỏ khối ngay khi đọc"""
    manager = multiprocessing.Manager()
    results = manager.list([0] * num_parts)  # Dùng list từ manager để chia sẻ kết quả giữa các process
    processes = []
    # Kiểm tra số lượng thread đang chạy
    logging.info(f"Active process count: {len(multiprocessing.active_children())}")
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

            # Tạo process cho từng phần dữ liệu
            process = multiprocessing.Process(target=count_word_in_chunk, args=(chunk, word, results, part_index,current_line))
            processes.append(process)
            process.start()
            
            # Cập nhật dòng bắt đầu cho khối tiếp theo
            current_line += len(chunk)
            
            # Kiểm tra số lượng thread đang chạy
            logging.info(f"Active process count: {len(multiprocessing.active_children())}")

            # Chờ cho process hoàn thành
            if len(processes) >= num_processes:
                for p in processes:
                    p.join()
                processes = []  # Reset lại list processes sau khi đã chờ hoàn thành

        # Đảm bảo chờ các process còn lại
        for p in processes:
            p.join()

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
