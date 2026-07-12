from hdfs import InsecureClient

# Kết nối đến NameNode
namenode_url = 'http://172.30.2.159:9870'  # Địa chỉ NameNode
client = InsecureClient(namenode_url, user='hadoop')  # 'hadoop' là tên user

# Đường dẫn file cục bộ trên máy bàn và đích HDFS
local_file_path = r'C:\Users\Admin\Desktop\output\citizens_data.csv'  # Đường dẫn file trên máy bàn
hdfs_destination_path = '/user/hadoop/input/citizens_data.csv'  # Đích HDFS

# Upload file
client.upload(hdfs_destination_path, local_file_path)

print(f"File {local_file_path} đã được tải lên HDFS tại {hdfs_destination_path}")