# %% Purpose
# Python Modules and Packages: Standard Library - sys
# Purpose: The sys module provides system-specific parameters and functions.
# Key Features: Command-line arguments, Python version, exit program.

# %% 1. Accessing System Information
# Explanation: Use sys.version and sys.platform for system details.
# Example:
import sys

print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")
# Output: Python version: (e.g., 3.11.4 ...)
#         Platform: (e.g., win32 or linux)

# %% 2. Command-Line Arguments
# Explanation: sys.argv contains command-line arguments.
# Example:
import sys

# Simulate running: python script.py Laptop 999.99
# sys.argv = ["script.py", "Laptop", "999.99"]  # Simulated for demo
try:
    if len(sys.argv) >= 3:
        product_name = sys.argv[1]
        price = float(sys.argv[2])
        print(f"Product: {product_name}, Price: ${price:.2f}")
    else:
        print("Provide product name and price as arguments")
except ValueError:
    print("Invalid price format")
# Output: Product: Laptop, Price: $999.99 (if args provided)
# Note: Run as 'python script.py Laptop 999.99' in practice

# %% 3. Retail Scenario with sys
# Explanation: Exit program if invalid retail data is provided.
# Example:
import sys

# Simulate checking retail script arguments
# sys.argv = ["script.py", "Smartphone", "-10"]  # Simulated
try:
    if len(sys.argv) >= 3:
        name = sys.argv[1]
        price = float(sys.argv[2])
        if price < 0:
            print("Error: Negative price")
            sys.exit(1)  # Exit with error code
        print(f"Valid product: {name}, Price: ${price:.2f}")
    else:
        print("Error: Missing arguments")
except ValueError:
    print("Error: Invalid price format")
# Output: Error: Negative price (exits if price < 0)
# Note: Run as 'python script.py Smartphone -10' in practice

# %% Notes
# Notes:
# - sys is useful in ML for script configuration or web apps for runtime info.
# - Use sys.exit() for controlled program termination.
# - sys.argv[0] is the script name; arguments start at sys.argv[1].