# %% Purpose
# Python File Handling: CSV Files
# Purpose: CSV (Comma-Separated Values) files store tabular data, ideal for retail datasets.
# Key Features: Read/write CSV files using csv module.

# %% 1. Reading a CSV File
# Explanation: Use csv.reader to read rows as lists.
# Example:
import csv

try:
    with open("products.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip header
        products = [(row[0], float(row[1])) for row in reader]
        for name, price in products:
            print(f"Product: {name}, Price: ${price:.2f}")
except FileNotFoundError:
    print("Simulated products.csv:\nProduct: Laptop, Price: $999.99\nProduct: Smartphone, Price: $699.99")
# Output (if file exists): Product: (name), Price: $(price)
# Output (if file missing): Simulated products.csv: Product: Laptop, Price: $999.99 Product: Smartphone, Price: $699.99
# Assumed file content: name,price Laptop,999.99 Smartphone,699.99

# %% 2. Writing a CSV File
# Explanation: Use csv.writer to write rows.
# Example:
import csv

products = [
    ["Laptop", 999.99],
    ["Smartphone", 699.99]
]
try:
    with open("products_output.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "price"])  # Write header
        writer.writerows(products)
    print("Written to products_output.csv")
except PermissionError:
    print("Error: Permission denied (simulated)")
# Output: Written to products_output.csv
# File content: name,price Laptop,999.99 Smartphone,699.99

# %% 3. Retail Scenario with CSV
# Explanation: Process retail orders in CSV format.
# Example:
import csv

orders = [
    {"order_id": 101, "total": 1999.98, "date": "2025-04-19"},
    {"order_id": 102, "total": 49.99, "date": "2025-04-20"}
]
try:
    with open("orders.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["order_id", "total", "date"])
        for order in orders:
            writer.writerow([order["order_id"], order["total"], order["date"]])
    print("Orders written to orders.csv")
    # Read back for verification
    with open("orders.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Order {row['order_id']}: ${float(row['total']):.2f}")
except (FileNotFoundError, PermissionError):
    print("Simulated orders:\nOrder 101: $1999.98\nOrder 102: $49.99")
# Output: Orders written to orders.csv
#         Order 101: $1999.98 Order 102: $49.99 (or simulated output)

# %% Notes
# Notes:
# - csv module handles delimiters, quotes, and escaping automatically.
# - Use DictReader/DictWriter for header-based access in ML (e.g., datasets) or web apps (e.g., reports).
# - Set newline="" in open() for consistent CSV writing across platforms.