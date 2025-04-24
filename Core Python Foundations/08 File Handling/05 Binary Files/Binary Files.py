# Python File Handling: Binary Files

# Purpose: Binary files store non-text data (e.g., images, serialized objects) in bytes.
# Key Features: Read/write bytes using 'rb' or 'wb' modes.

# 1. Reading a Binary File
# Explanation: Use open() with 'rb' mode to read bytes.
# Example:
try:
    with open("logo.png", "rb") as file:
        data = file.read(10)  # Read first 10 bytes
        print("First 10 bytes:", data)
except FileNotFoundError:
    print("Simulated binary data: b'\\x89PNG\\r\\n\\x1a\\n'")
# Output (if file exists): First 10 bytes: (byte sequence)
# Output (if file missing): Simulated binary data: b'\x89PNG\r\n\x1a\n'
# Note: logo.png assumed to be a PNG image for demo

# 2. Writing a Binary File
# Explanation: Use 'wb' mode to write bytes, overwriting existing files.
# Example:
try:
    binary_data = b"RETAIL_DATA"
    with open("data.bin", "wb") as file:
        file.write(binary_data)
    print("Written to data.bin")
except PermissionError:
    print("Error: Permission denied (simulated)")
# Output: Written to data.bin
# File content: RETAIL_DATA (as bytes)

# 3. Retail Scenario with Binary Files
# Explanation: Serialize and deserialize retail product data using pickle (binary serialization).
# Example:
import pickle

products = [
    {"name": "Laptop", "price": 999.99},
    {"name": "Smartphone", "price": 699.99}
]
try:
    # Write to binary file
    with open("products.bin", "wb") as file:
        pickle.dump(products, file)
    print("Products written to products.bin")
    # Read back for verification
    with open("products.bin", "rb") as file:
        loaded_products = pickle.load(file)
        for product in loaded_products:
            print(f"Product: {product['name']}, Price: ${product['price']:.2f}")
except (FileNotFoundError, PermissionError):
    print("Simulated products:\nProduct: Laptop, Price: $999.99\nProduct: Smartphone, Price: $699.99")
# Output: Products written to products.bin
#         Product: Laptop, Price: $999.99 Product: Smartphone, Price: $699.99 (or simulated output)

# Exercise 1: Read the first 5 bytes of a binary file data.bin.
# Solution:
# try:
#     with open("data.bin", "rb") as file:
#         data = file.read(5)
#         print("Exercise 1 - First 5 bytes:", data)
# except FileNotFoundError:
#     print("Exercise 1 - Simulated bytes: b'RETAI'")
# # Output: First 5 bytes: (bytes) or Simulated bytes: b'RETAI'

# Exercise 2: Write a string as bytes to a binary file output.bin.
# Solution:
# try:
#     data = b"ORDER_101"
#     with open("output.bin", "wb") as file:
#         file.write(data)
#     print("Exercise 2 - Written to output.bin")
# except PermissionError:
#     print("Exercise 2 - Error: Permission denied (simulated)")
# # Output: Written to output.bin

# Exercise 3: Serialize a list of orders to orders.bin using pickle.
# Solution:
# import pickle
# orders = [{"order_id": 101, "total": 1999.98}, {"order_id": 102, "total": 49.99}]
# try:
#     with open("orders.bin", "wb") as file:
#         pickle.dump(orders, file)
#     print("Exercise 3 - Orders written to orders.bin")
# except PermissionError:
#     print("Exercise 3 - Error: Permission denied (simulated)")
# # Output: Orders written to orders.bin

# Notes:
# - Binary files are used in ML for model serialization (e.g., pickle) or web apps for image handling.
# - Use 'rb'/'wb' modes; handle EOFError or PickleError for corrupted data.
# - pickle is not secure for untrusted sources; validate data before deserialization.