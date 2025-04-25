# %% Purpose
# Python File Handling: Reading Files
# Purpose: Reading files allows accessing data stored in text files.
# Key Features: Read entire files, read lines, handle file paths.

# Note: Examples assume files exist or simulate file content for demonstration.

# %% 1. Reading Entire File
# Explanation: Use open() with 'r' mode to read file content.
# Example:
try:
    with open("products.txt", "r") as file:
        content = file.read()
        print("Products:\n", content)
except FileNotFoundError:
    print("Simulated products.txt content:\nLaptop,999.99\nSmartphone,699.99")
# Output (if file exists): Products: (file content)
# Output (if file missing): Simulated products.txt content: Laptop,999.99 Smartphone,699.99

# %% 2. Reading Line by Line
# Explanation: Use readlines() or iterate over file object for line-by-line reading.
# Example:
try:
    with open("products.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print("Product line:", line.strip())
except FileNotFoundError:
    print("Simulated line-by-line:\nProduct line: Laptop,999.99\nProduct line: Smartphone,699.99")
# Output (if file exists): Product line: (each line)
# Output (if file missing): Simulated line-by-line: Product line: Laptop,999.99 Product line: Smartphone,699.99

# %% 3. Retail Scenario with Reading Files
# Explanation: Read product data for retail processing.
# Example:
try:
    with open("products.txt", "r") as file:
        products = [line.strip().split(",") for line in file]
        for name, price in products:
            print(f"Product: {name}, Price: ${float(price):.2f}")
except FileNotFoundError:
    print("Simulated retail data:\nProduct: Laptop, Price: $999.99\nProduct: Smartphone, Price: $699.99")
except ValueError:
    print("Error: Invalid price format in file")
# Output (if file exists): Product: Laptop, Price: $999.99 (etc.)
# Output (if file missing): Simulated retail data: Product: Laptop, Price: $999.99 Product: Smartphone, Price: $699.99

# %% Notes
# Notes:
# - Use 'with' statement to automatically close files, reducing resource leaks.
# - Handle FileNotFoundError and other exceptions for robust file reading.
# - Useful in ML for reading datasets or web apps for loading configurations.