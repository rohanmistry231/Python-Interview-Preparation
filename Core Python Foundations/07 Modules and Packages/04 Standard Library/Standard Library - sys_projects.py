# sys Projects
# Purpose: Apply sys module through 10 retail-themed projects.
# Structure: Each project is separated by %% and includes description, tasks, and solution code.
# Note: Solutions use simulated sys.argv for reproducibility and match the updated base file outputs.

# %% Project 1: Python Version Display
# Difficulty: Basic
# Description: Display the Python version used.
# Objective: Practice accessing system information.
# Tasks:
# - Import sys and use version.
# - Print the Python version.
# Expected Output: Python version: (e.g., 3.11.4 ...)
import sys

print(f"Python version: {sys.version}")

# %% Project 2: Platform Checker
# Difficulty: Basic
# Description: Check the operating system platform.
# Objective: Practice accessing platform information.
# Tasks:
# - Import sys and use platform.
# - Print the platform.
# Expected Output: Platform: (e.g., win32)
import sys

print(f"Platform: {sys.platform}")

# %% Project 3: Script Name Printer
# Difficulty: Basic
# Description: Print the name of the running script.
# Objective: Practice accessing sys.argv[0].
# Tasks:
# - Import sys and use argv[0].
# - Print the script name.
# Expected Output: Script name: (e.g., script.py)
import sys

print(f"Script name: {sys.argv[0]}")

# %% Project 4: Product Argument Processor
# Difficulty: Intermediate
# Description: Process a product name from command-line arguments.
# Objective: Practice handling sys.argv.
# Tasks:
# - Import sys and check for a product name argument.
# - Print the product name or an error.
# Expected Output: Product: Laptop
import sys

# Simulate: python script.py Laptop
sys.argv = ["script.py", "Laptop"]
if len(sys.argv) >= 2:
    product_name = sys.argv[1]
    print(f"Product: {product_name}")
else:
    print("Error: Provide product name")

# %% Project 5: Price Validator
# Difficulty: Intermediate
# Description: Validate a product price from command-line arguments.
# Objective: Practice argument validation.
# Tasks:
# - Import sys and validate a price argument.
# - Print the price or an error.
# Expected Output: Price: $999.99
import sys

# Simulate: python script.py 999.99
sys.argv = ["script.py", "999.99"]
try:
    if len(sys.argv) >= 2:
        price = float(sys.argv[1])
        print(f"Price: ${price:.2f}")
    else:
        print("Error: Provide price")
except ValueError:
    print("Error: Invalid price format")

# %% Project 6: Exit on Invalid Stock
# Difficulty: Intermediate
# Description: Exit if a stock argument is negative.
# Objective: Practice using sys.exit().
# Tasks:
# - Import sys and check a stock argument.
# - Exit with an error if negative, else print the stock.
# Expected Output: Stock: 50
import sys

# Simulate: python script.py 50
sys.argv = ["script.py", "50"]
try:
    if len(sys.argv) >= 2:
        stock = int(sys.argv[1])
        if stock < 0:
            print("Error: Negative stock")
            sys.exit(1)
        print(f"Stock: {stock}")
    else:
        print("Error: Provide stock")
except ValueError:
    print("Error: Invalid stock format")

# %% Project 7: Module Path Viewer
# Difficulty: Intermediate
# Description: Display the Python module search paths.
# Objective: Practice accessing sys.path.
# Tasks:
# - Import sys and use path.
# - Print the module search paths.
# Expected Output: Module paths: (list of paths)
import sys

print(f"Module paths: {sys.path}")

# %% Project 8: Argument-Based Discount
# Difficulty: Advanced
# Description: Apply a discount based on command-line arguments.
# Objective: Practice complex argument processing.
# Tasks:
# - Import sys and process price and discount rate arguments.
# - Print the discounted price or an error.
# Expected Output: Discounted price: $899.99
import sys

# Simulate: python script.py 999.99 0.1
sys.argv = ["script.py", "999.99", "0.1"]
try:
    if len(sys.argv) >= 3:
        price = float(sys.argv[1])
        rate = float(sys.argv[2])
        if rate < 0 or rate > 1:
            print("Error: Invalid discount rate")
            sys.exit(1)
        discounted = price * (1 - rate)
        print(f"Discounted price: ${discounted:.2f}")
    else:
        print("Error: Provide price and discount rate")
except ValueError:
    print("Error: Invalid input format")

# %% Project 9: System Exit with Status
# Difficulty: Advanced
# Description: Exit with a custom status code for invalid arguments.
# Objective: Practice advanced sys.exit() usage.
# Tasks:
# - Import sys and check for valid product arguments.
# - Exit with a status code if invalid, else print the product.
# Expected Output: Product: Smartphone
import sys

# Simulate: python script.py Smartphone
sys.argv = ["script.py", "Smartphone"]
if len(sys.argv) >= 2:
    product = sys.argv[1]
    if not product.isalpha():
        print("Error: Invalid product name")
        sys.exit(2)
    print(f"Product: {product}")
else:
    print("Error: Provide product name")
    sys.exit(1)

# %% Project 10: Comprehensive Retail Config
# Difficulty: Advanced
# Description: Configure a retail script using system information and arguments.
# Objective: Practice integrating sys features.
# Tasks:
# - Import sys, display version, platform, and process a product argument.
# - Print all details.
# Expected Output: Version: 3.11.4, Platform: win32, Product: Laptop
import sys

# Simulate: python script.py Laptop
sys.argv = ["script.py", "Laptop"]
version = sys.version.split()[0]
platform = sys.platform
product = sys.argv[1] if len(sys.argv) >= 2 else "Unknown"
print(f"Version: {version}, Platform: {platform}, Product: {product}")