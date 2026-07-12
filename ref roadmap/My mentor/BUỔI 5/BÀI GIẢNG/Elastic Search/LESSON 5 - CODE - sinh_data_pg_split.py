import csv
from faker import Faker
import random
import os

fake = Faker()

categories = ["laptop", "điện thoại", "tai nghe", "thiết bị IoT", "phụ kiện"]
brands = ["Asus", "Dell", "HP", "Samsung", "Apple", "Xiaomi", "Anker", "Sony"]
ram_options = ["4GB", "8GB", "16GB"]
cpu_options = ["Intel Core i3", "Intel Core i5", "Intel Core i7", "M1", "Snapdragon 8 Gen 1"]

def generate_product(i):
    category = random.choice(categories)
    brand = random.choice(brands)
    name = f"{brand} {category.title()} {fake.word().capitalize()} {random.randint(1, 9999)}"
    price = round(random.uniform(500_000, 50_000_000), 2)
    cpu = random.choice(cpu_options)
    ram = random.choice(ram_options)
    desc = fake.sentence(nb_words=12)

    return {
        "id": f"p{i}",
        "name": name,
        "brand": brand,
        "category": category,
        "price": price,
        "ram": ram,
        "cpu": cpu,
        "description": desc,
        "tags": [category, brand, cpu, ram]
    }

# ==== Chia file ====
TOTAL = 10_000_000              # Tổng số record
BATCH_SIZE = 500_000           # Mỗi file chứa tối đa bao nhiêu record
NUM_FILES = TOTAL // BATCH_SIZE + (1 if TOTAL % BATCH_SIZE else 0)

for file_index in range(NUM_FILES):
    filename = f"products_{file_index+1}_pg.csv"
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name", "brand", "category", "price", "ram", "cpu", "description", "tags"])
        
        start = file_index * BATCH_SIZE + 1
        end = min((file_index + 1) * BATCH_SIZE + 1, TOTAL + 1)

        for i in range(start, end):
            product = generate_product(i)
            writer.writerow([
                product["id"],
                product["name"],
                product["brand"],
                product["category"],
                product["price"],
                product["ram"],
                product["cpu"],
                product["description"],
                "{" + ",".join(f'"{tag}"' for tag in product["tags"]) + "}"
            ])
    
    print(f"✅ Wrote file: {filename} with records {start} to {end - 1}")

