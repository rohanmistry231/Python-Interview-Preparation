# Python File Handling: Writing Files

# Purpose: Writing files stores data in text files for persistence.
# Key Features: Write, append, create files if they don’t exist.

# 1. Writing to a New File
# Explanation: Use open() with 'w' mode to write content, overwriting existing files.
# Example:
try:
    with open("output.txt", "w") as file:
        file.write("Laptop,999.99\nSmartphone,699.99")
    print("Data written to output.txt")
except PermissionError:
    print("Error: Permission denied (simulated)")
# Output: Data written to output.txt
# File content: Laptop,999.99 Smartphone,699.99

# 2. Appending to a File
# Explanation: Use 'a' mode to append content without overwriting.
# Example:
try:
    with open("output.txt", "a") as file:
        file.write("\nCoffee Maker,49.99")
    print("Appended to output.txt")
except PermissionError:
    print("Error: Permission denied (simulated)")
# Output: Appended to output.txt
# File content (after append): Laptop,999.99 Smartphone,699.99 Coffee Maker,49.99

# 3. Retail Scenario with Writing Files
# Explanation: Write retail order data to a file.
# Example:
orders = [
    {"order_id": 101, "total": 1999.98},
    {"order_id": 102, "total": 49.99}
]
try:
    with open("orders.txt", "w") as file:
        for order in orders:
            file.write(f"Order {order['order_id']},${order['total']:.2f}\n")
    print("Orders written to orders.txt")
except PermissionError:
    print("Error: Permission denied (simulated)")
# Output: Orders written to orders.txt
# File content: Order 101,$1999.98 Order 102,$49.99

# Exercise 1: Write a list of products to products.txt.
# Solution:
# products = ["Mouse,29.99", "Keyboard,59.99"]
# try:
#     with open("products.txt", "w") as file:
#         for product in products:
#             file.write(product + "\n")
#     print("Exercise 1 - Products written to products.txt")
# except PermissionError:
#     print("Exercise 1 - Error: Permission denied (simulated)")
# # Output: Products written to products.txt

# Exercise 2: Append a new product to products.txt.
# Solution:
# try:
#     with open("products.txt", "a") as file:
#         file.write("Monitor,199.99\n")
#     print("Exercise 2 - Appended to products.txt")
# except PermissionError:
#     print("Exercise 2 - Error: Permission denied (simulated)")
# # Output: Appended to products.txt

# Exercise 3: Write customer data to customers.txt with name and email.
# Solution:
# customers = [{"name": "Alice", "email": "alice@example.com"}, {"name": "Bob", "email": "bob@example.com"}]
# try:
#     with open("customers.txt", "w") as file:
#         for customer in customers:
#             file.write(f"{customer['name']},{customer['email']}\n")
#     print("Exercise 3 - Customers written to customers.txt")
# except PermissionError:
#     print("Exercise 3 - Error: Permission denied (simulated)")
# # Output: Customers written to customers.txt

# Notes:
# - 'w' overwrites files; 'a' appends to existing content.
# - Use 'with' for safe file handling; handle PermissionError for restricted directories.
# - Useful in ML for saving model outputs or web apps for logging user actions.