import pickle
import logging
import threading
import time

filename = r'C:\Users\Admin\Desktop\output\citizens_data.csv'
index_filename = "index_citizens_data.pkl"

# Tạo chỉ mục và lưu với Pickle
index = {}
with open(filename, 'r', encoding='utf-8') as file:
    line_number = 0
    last_position = 0
    index[line_number] = last_position
    for line in file:
        line_number+=1
        last_position += len(line.encode('utf-8'))  # Tính vị trí cho dòng kế tiếp
        index[line_number] = last_position
        # Định kỳ ghi chỉ mục để giảm tải bộ nhớ (mỗi 1 triệu dòng)
        if line_number % 1_000_000 == 0:
            print(f"Đã xử lý {line_number // 1_000_000} triệu dòng...")

# Ghi chỉ mục vào file
with open(index_filename, 'wb') as f:
    pickle.dump(index, f)
print(f"Đã lưu chỉ mục {line_number - 1} dòng vào {index_filename}.")