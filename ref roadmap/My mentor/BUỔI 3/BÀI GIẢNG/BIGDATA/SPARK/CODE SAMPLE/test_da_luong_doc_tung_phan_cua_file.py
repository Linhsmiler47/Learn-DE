import logging
import threading
import time
import pickle

# Cấu hình logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)s] %(message)s",
    handlers=[
        logging.FileHandler("log_read_multi_io.log", mode="w", encoding="utf-8"),  # Ghi log vào file
        logging.StreamHandler()  # Hiển thị log ra màn hình (tùy chọn)
    ]
)

# Định nghĩa một hàm để đọc dữ liệu từ chunk
def count_word_manual(filename,word):
    total_count = 0
    with open(filename, 'r', encoding='utf-8') as file:
        pos = 0
        file.seek(pos)  # Di chuyển con trỏ file đến vị trí start
        while pos < 10000:
            line = file.readline()  # Đọc một dòng
            pos+=1
            #logging.info(line)
            if not line:  # Nếu đến cuối file, dừng lại
                break
            # Xử lý dữ liệu của dòng tại đây (chỉ in ra ví dụ)
            #logging.info(f"Processing line: {line.strip()}")
            # Kiểm tra xem từ "French" có trong dòng không
            if word in line:
                total_count += line.count(word)
    logging.info(f"found {total_count} word {word}") 

# Định nghĩa một hàm để đọc dữ liệu từ chunk
def process_chunk(start, end, filename,thread_id,part_sub_index,results,word,index):
    total_count = 0
    #if thread_id==0 and part_sub_index ==9:
    #    logging.info(f"part_sub_index: {part_sub_index} , Thread id: {thread_id} ,  start line : {start} , end line : {end}")
    with open(filename, 'r', encoding='utf-8') as file:
        pos = start
        #print(f"vị trí con trỏ : {index[start]}")
        file.seek(index[start])  # Di chuyển con trỏ file đến vị trí start
        
        while pos < end:
            line = file.readline()  # Đọc một dòng
            pos += 1
            #if thread_id==0 and part_sub_index ==9:
            #    logging.info(f"Dòng theo dõi : {line}")
            if not line:  # Nếu đến cuối file, dừng lại
                break
            # Xử lý dữ liệu của dòng tại đây (chỉ in ra ví dụ)
            # Kiểm tra xem từ "French" có trong dòng không
            if word in line:
                total_count += line.count(word)
    logging.info(f"Thread id : {thread_id} , part : {part_sub_index} , found {total_count} word {word}")
    results[thread_id].append(total_count)  # Gắn giá trị vào ma trận    
# Định nghĩa một hàm để xử lý từng phần
def process_part(start, end, filename, thread_id,results,word,index):
    chunk_size = (end - start) // 10  # Chia thành 10 phần nhỏ
    sub_threads = []
    # Tạo các thread con để xử lý từng chunk
    for i in range(10):
        chunk_start = start + i * chunk_size
        chunk_end = chunk_start + chunk_size if i < 10 else end  # Đảm bảo không vượt quá end
        logging.info(f"Thread id {thread_id} , part_sub_index: {i} , start line : {chunk_start} , end line : {chunk_end}")
        sub_thread = threading.Thread(target=process_chunk, args=(chunk_start, chunk_end, filename,thread_id,i,results,word,index))
        sub_threads.append(sub_thread)
        sub_thread.start()
    
    # Đợi tất cả các thread con hoàn thành
    for sub_thread in sub_threads:
        sub_thread.join()
    logging.info(f"Part {thread_id} processing completed.")

# Định nghĩa một hàm chính để chia file thành các phần cho 4 thread chính
def process_file(filename,word,index, num_threads=4):
    # Mở file và đo tổng số dòng
    with open(filename, 'r', encoding='utf-8') as file:
        total_lines = sum(1 for _ in file)  # Đếm tổng số dòng trong file

    # Chia đều số dòng cho 4 thread chính
    lines_per_thread = total_lines // num_threads
    threads = []
    results = [[] for _ in range(num_threads)]
    
    for i in range(num_threads):
        #print(i)
        start = i * lines_per_thread
        end = start + lines_per_thread if i < num_threads - 1 else total_lines
        logging.info(f"Thread id: {i} , start line : {start} , end line : {end}")
        thread = threading.Thread(target=process_part, args=(start, end, filename, i,results,word,index))
        threads.append(thread)
        thread.start()

    # Đợi tất cả các thread chính hoàn thành
    for thread in threads:
        thread.join()
    total_count = sum(sum(row) for row in results)
    logging.info(f"{results}")
    # In kết quả sau khi tất cả các thread hoàn thành
    logging.info(f"Total occurrences of '{word}': {total_count}")

word = input("Nhập từ cần tìm: ").strip()
# Đếm số lần xuất hiện của từ
start_time = time.time()
logging.info("Start time: %s", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time)))


# Gọi hàm chính
# nạp chỉ mục:
# Nạp chỉ mục từ Pickle
# Tạo chỉ mục và lưu với Pickle
index = {}
index_filename = "index_citizens_data_small.pkl"
with open(index_filename, 'rb') as f:
    index = pickle.load(f)

filename = r'C:\Users\Admin\Desktop\output\citizens_data_small.csv'  # Đường dẫn đến file text của bạn
process_file(filename,word,index)
#count_word_manual(filename,word)

end_time = time.time()
logging.info("End time: %s", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time)))

# Tính tổng thời gian chạy
elapsed_time = end_time - start_time
logging.info("Elapsed time: %.2f seconds", elapsed_time)