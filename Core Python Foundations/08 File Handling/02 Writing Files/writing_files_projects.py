# Writing Files Projects
# Purpose: Apply file writing through 5 retail-themed projects.
# Structure: Each project is separated by %% and includes description, tasks, and solution code.
# Note: Solutions use simulated inputs for reproducibility and match the updated base file outputs.

# %% Project 1: Write Product Catalog
# Difficulty: Basic
# Description: Write a list of products to catalog.txt.
# Objective: Practice basic file writing.
# Tasks:
# - Write two products to catalog.txt using 'w' mode.
# - Print confirmation or handle errors.
# Expected Output: Catalog written to catalog.txt
products = ["Mouse,29.99", "Keyboard,59.99"]
try:
    with open("catalog.txt", "w") as file:
        for product in products:
            file.write(f"{product}\n")
    print("Catalog written to catalog.txt")
except PermissionError:
    print("Error: Permission denied (simulated)")

# %% Project 2: Append Order Log
# Difficulty: Basic
# Description: Append a new order to orders_log.txt.
# Objective: Practice file appending.
# Tasks:
# - Append one order to orders_log.txt using 'a' mode.
# - Print confirmation or handle errors.
# Expected Output: Order appended to orders_log.txt
order = "Order 103,99.99"
try:
    with open("orders_log.txt", "a") as file:
        file.write(f"{order}\n")
    print("Order appended to orders_log.txt")
except PermissionError:
    print("Error: Permission denied (simulated)")

# %% Project 3: Save Customer Data
# Difficulty: Intermediate
# Description: Write customer data with names and emails to customers.txt.
# Objective: Practice structured file writing.
# Tasks:
# - Write a list of dictionaries to customers.txt.
# - Print confirmation or handle errors.
# Expected Output: Customers written to customers.txt
customers = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"}
]
try:
    with open("customers.txt", "w") as file:
        for customer in customers:
            file.write(f"{customer['name']},{customer['email']}\n")
    print("Customers written to customers.txt")
except PermissionError:
    print("Error: Permission denied (simulated)")

# %% Project 4: Log Sales Summary
# Difficulty: Intermediate
# Description: Write a sales summary with total and count to sales.txt.
# Objective: Practice formatted file writing.
# Tasks:
# - Calculate total and count from sales data and write to sales.txt.
# - Print confirmation or handle errors.
# Expected Output: Sales summary written to sales.txt
sales = [1999.98, 49.99]
total = sum(sales)
count = len(sales)
try:
    with open("sales.txt", "w") as file:
        file.write(f"Sales Summary\nTotal: ${total:.2f}\nCount: {count}\n")
    print("Sales summary written to sales.txt")
except PermissionError:
    print("Error: Permission denied (simulated)")

# %% Project 5: Conditional Order Backup
# Difficulty: Advanced
# Description: Write high-value orders (> $500) to backup.txt.
# Objective: Practice conditional file writing.
# Tasks:
# - Filter orders by value and write to backup.txt.
# - Print confirmation or handle errors.
# Expected Output: High-value orders written to backup.txt
orders = [
    {"order_id": 101, "total": 1999.98},
    {"order_id": 102, "total": 49.99}
]
try:
    with open("backup.txt", "w") as file:
        for order in orders:
            if order["total"] > 500:
                file.write(f"Order {order['order_id']},${order['total']:.2f}\n")
    print("High-value orders written to backup.txt")
except PermissionError:
    print("Error: Permission denied (simulated)")