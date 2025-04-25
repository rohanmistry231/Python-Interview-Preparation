# CSV Files Projects
# Purpose: Apply CSV file handling through 5 retail-themed projects.
# Structure: Each project is separated by %% and includes description, tasks, and solution code.
# Note: Solutions use simulated inputs for reproducibility and match the updated base file outputs.

# %% Project 1: Read Customer Names
# Difficulty: Basic
# Description: Read customers.csv and print customer names.
# Objective: Practice basic CSV reading.
# Tasks:
# - Use csv.reader to read customers.csv and extract names.
# - Print names or simulate if missing.
# Expected Output: Customers: ['Alice', 'Bob']
import csv

file_path = "customers.csv"
try:
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        names = [row[0] for row in reader]
    print(f"Customers: {names}")
except FileNotFoundError:
    print("Customers: ['Alice', 'Bob']")

# %% Project 2: Write Product CSV
# Difficulty: Basic
# Description: Write a list of products to products.csv.
# Objective: Practice basic CSV writing.
# Tasks:
# - Use csv.writer to write products with headers to products.csv.
# - Print confirmation or handle errors.
# Expected Output: Products written to products.csv
import csv

products = [["Mouse", 29.99], ["Keyboard", 59.99]]
try:
    with open("products.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "price"])
        writer.writerows(products)
    print("Products written to products.csv")
except PermissionError:
    print("Error: Permission denied (simulated)")

# %% Project 3: Calculate Order Total
# Difficulty: Intermediate
# Description: Read orders.csv and calculate the total order value.
# Objective: Practice processing CSV data.
# Tasks:
# - Use csv.DictReader to read orders.csv and sum totals.
# - Print the total or simulate if missing.
# Expected Output: Total order value: $2049.97
import csv

file_path = "orders.csv"
try:
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        total = sum(float(row["total"]) for row in reader)
    print(f"Total order value: ${total:.2f}")
except FileNotFoundError:
    print("Total order value: $2049.97")

# %% Project 4: Filter High-Value Orders
# Difficulty: Intermediate
# Description: Read orders.csv and list orders with total > $500.
# Objective: Practice filtering CSV data.
# Tasks:
# - Use csv.DictReader to read orders.csv and filter by total.
# - Print order IDs or simulate if missing.
# Expected Output: High-value orders: [101]
import csv

file_path = "orders.csv"
high_value_orders = []
try:
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if float(row["total"]) > 500:
                high_value_orders.append(int(row["order_id"]))
    print(f"High-value orders: {high_value_orders}")
except FileNotFoundError:
    print("High-value orders: [101]")

# %% Project 5: Comprehensive CSV Processor
# Difficulty: Advanced
# Description: Read products.csv, add discounts, and write to discounted_products.csv.
# Objective: Practice reading and writing CSV with processing.
# Tasks:
# - Read products.csv, apply a 10% discount, and write to a new CSV.
# - Print confirmation or simulate if missing.
# Expected Output: Discounted products written to discounted_products.csv
import csv

input_file = "products.csv"
output_file = "discounted_products.csv"
try:
    with open(input_file, "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        products = [[row[0], float(row[1]) * 0.9] for row in reader]
    with open(output_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "price"])
        writer.writerows(products)
    print("Discounted products written to discounted_products.csv")
except FileNotFoundError:
    print("Discounted products written to discounted_products.csv (simulated)")
except PermissionError:
    print("Error: Permission denied (simulated)")