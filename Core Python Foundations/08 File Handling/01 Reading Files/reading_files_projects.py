# Reading Files Projects
# Purpose: Apply file reading through 5 retail-themed projects.
# Structure: Each project is separated by %% and includes description, tasks, and solution code.
# Note: Solutions use simulated inputs for reproducibility and match the updated base file outputs.

# %% Project 1: Read Inventory File
# Difficulty: Basic
# Description: Read the entire content of an inventory.txt file.
# Objective: Practice reading entire file content.
# Tasks:
# - Import os for path handling and read inventory.txt using read().
# - Print the file content or simulate if missing.
# Expected Output: Inventory: Laptop,999.99 Smartphone,699.99
import os

file_path = "inventory.txt"
try:
    with open(file_path, "r") as file:
        content = file.read()
        print(f"Inventory: {content.strip()}")
except FileNotFoundError:
    print("Inventory: Laptop,999.99 Smartphone,699.99")

# %% Project 2: List Orders Line by Line
# Difficulty: Basic
# Description: Read orders.txt and print each order line.
# Objective: Practice line-by-line reading.
# Tasks:
# - Read orders.txt using a file iterator.
# - Print each line or simulate if missing.
# Expected Output: Order: Order 101,1999.98
#                 Order: Order 102,49.99
file_path = "orders.txt"
try:
    with open(file_path, "r") as file:
        for line in file:
            print(f"Order: {line.strip()}")
except FileNotFoundError:
    print("Order: Order 101,1999.98")
    print("Order: Order 102,49.99")

# %% Project 3: Extract Expensive Products
# Difficulty: Intermediate
# Description: Read products.txt and list products with price > 500.
# Objective: Practice processing file data.
# Tasks:
# - Read products.txt, split lines, and filter products by price.
# - Print product names or simulate if missing.
# Expected Output: Expensive products: ['Laptop', 'Smartphone']
file_path = "products.txt"
expensive_products = []
try:
    with open(file_path, "r") as file:
        for line in file:
            name, price = line.strip().split(",")
            if float(price) > 500:
                expensive_products.append(name)
    print(f"Expensive products: {expensive_products}")
except FileNotFoundError:
    print("Expensive products: ['Laptop', 'Smartphone']")
except ValueError:
    print("Error: Invalid price format")

# %% Project 4: Count Customer Records
# Difficulty: Intermediate
# Description: Count the number of customer records in customers.txt.
# Objective: Practice file iteration and counting.
# Tasks:
# - Read customers.txt and count non-empty lines.
# - Print the count or simulate if missing.
# Expected Output: Customer count: 2
file_path = "customers.txt"
count = 0
try:
    with open(file_path, "r") as file:
        for line in file:
            if line.strip():
                count += 1
    print(f"Customer count: {count}")
except FileNotFoundError:
    print("Customer count: 2")

# %% Project 5: Validate Product Data
# Difficulty: Advanced
# Description: Read products.txt and validate price formats.
# Objective: Practice robust file reading with error handling.
# Tasks:
# - Read products.txt, check for valid float prices, and report invalid entries.
# - Print valid products or simulate if missing.
# Expected Output: Valid products: ['Laptop', 'Smartphone']
#                 Invalid entries: []
file_path = "products.txt"
valid_products = []
invalid_entries = []
try:
    with open(file_path, "r") as file:
        for line in file:
            try:
                name, price = line.strip().split(",")
                float(price)
                valid_products.append(name)
            except ValueError:
                invalid_entries.append(line.strip())
    print(f"Valid products: {valid_products}")
    print(f"Invalid entries: {invalid_entries}")
except FileNotFoundError:
    print("Valid products: ['Laptop', 'Smartphone']")
    print("Invalid entries: []")