# Python File Handling: JSON Files

# Purpose: JSON (JavaScript Object Notation) files store structured data, ideal for APIs and configuration.
# Key Features: Serialize/deserialize Python objects using json module.

# 1. Reading a JSON File
# Explanation: Use json.load() to deserialize JSON into Python objects.
# Example:
import json

try:
    with open("products.json", "r") as file:
        products = json.load(file)
        for product in products:
            print(f"Product: {product['name']}, Price: ${product['price']:.2f}")
except FileNotFoundError:
    print("Simulated products.json:\nProduct: Laptop, Price: $999.99\nProduct: Smartphone, Price: $699.99")
# Output (if file exists): Product: (name), Price: $(price)
# Output (if file missing): Simulated products.json: Product: Laptop, Price: $999.99 Product: Smartphone, Price: $699.99
# Assumed file content: [{"name": "Laptop", "price": 999.99}, {"name": "Smartphone", "price": 699.99}]

# 2. Writing a JSON File
# Explanation: Use json.dump() to serialize Python objects to JSON.
# Example:
import json

products = [
    {"name": "Laptop", "price": 999.99},
    {"name": "Smartphone", "price": 699.99}
]
try:
    with open("products_output.json", "w") as file:
        json.dump(products, file, indent=2)
    print("Written to products_output.json")
except PermissionError:
    print("Error: Permission denied (simulated)")
# Output: Written to products_output.json
# File content: [
#   {"name": "Laptop", "price": 999.99},
#   {"name": "Smartphone", "price": 699.99}
# ]

# 3. Retail Scenario with JSON
# Explanation: Store and retrieve retail order data in JSON format.
# Example:
import json

orders = [
    {"order_id": 101, "total": 1999.98, "date": "2025-04-19"},
    {"order_id": 102, "total": 49.99, "date": "2025-04-20"}
]
try:
    # Write orders
    with open("orders.json", "w") as file:
        json.dump(orders, file, indent=2)
    print("Orders written to orders.json")
    # Read back for verification
    with open("orders.json", "r") as file:
        loaded_orders = json.load(file)
        for order in loaded_orders:
            print(f"Order {order['order_id']}: ${order['total']:.2f}")
except (FileNotFoundError, PermissionError):
    print("Simulated orders:\nOrder 101: $1999.98\nOrder 102: $49.99")
# Output: Orders written to orders.json
#         Order 101: $1999.98 Order 102: $49.99 (or simulated output)

# Exercise 1: Read a JSON file customers.json and print emails.
# Solution:
# import json
# try:
#     with open("customers.json", "r") as file:
#         customers = json.load(file)
#         for customer in customers:
#             print("Exercise 1 - Email:", customer["email"])
# except FileNotFoundError:
#     print("Exercise 1 - Simulated emails: alice@example.com, bob@example.com")
# # Output: Email: (email) or Simulated emails: alice@example.com, bob@example.com
# # Assumed file: [{"name": "Alice", "email": "alice@example.com"}, {"name": "Bob", "email": "bob@example.com"}]

# Exercise 2: Write a list of products to products.json.
# Solution:
# import json
# products = [{"name": "Mouse", "price": 29.99}, {"name": "Keyboard", "price": 59.99}]
# try:
#     with open("products.json", "w") as file:
#         json.dump(products, file, indent=2)
#     print("Exercise 2 - Written to products.json")
# except PermissionError:
#     print("Exercise 2 - Error: Permission denied (simulated)")
# # Output: Written to products.json

# Exercise 3: Read orders.json and calculate total order value.
# Solution:
# import json
# try:
#     with open("orders.json", "r") as file:
#         orders = json.load(file)
#         total = sum(order["total"] for order in orders)
#         print("Exercise 3 - Total order value:", total)
# except FileNotFoundError:
#     print("Exercise 3 - Simulated total: 2049.97")
# # Output: Total order value: (sum) or Simulated total: 2049.97

# Notes:
# - JSON supports lists, dicts, strings, numbers, booleans, and null; use json.loads()/dumps() for strings.
# - Critical in ML for saving model configs or web apps for API data exchange.
# - Use indent for readable JSON output; handle JSONDecodeError for invalid JSON.