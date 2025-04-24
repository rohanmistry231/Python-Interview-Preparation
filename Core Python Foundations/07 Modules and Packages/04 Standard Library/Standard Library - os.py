# Python Modules and Packages: Standard Library - os

# Purpose: The os module interacts with the operating system (e.g., file handling, directories).
# Key Features: File operations, path management, environment variables.

# 1. Working with Directories
# Explanation: Use os.getcwd() and os.listdir() for directory operations.
# Example:
import os

current_dir = os.getcwd()
print(f"Current directory: {current_dir}")
files = os.listdir(current_dir)
print(f"Files in directory: {files}")
# Output: Current directory: (current path)
#         Files in directory: (list of files, e.g., ['script.py'])

# 2. File Path Handling
# Explanation: Use os.path for cross-platform path manipulation.
# Example:
import os

# Create a path for a retail database file
db_file = os.path.join("data", "retail.db")
print(f"Database file path: {db_file}")
exists = os.path.exists(db_file)
print(f"File exists: {exists}")
# Output: Database file path: data/retail.db
#         File exists: False (unless file exists)

# 3. Retail Scenario with os
# Explanation: Manage retail data files (e.g., product CSVs).
# Example:
import os

# Check for product data directory and create if missing
data_dir = "product_data"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
    print(f"Created directory: {data_dir}")
else:
    print(f"Directory exists: {data_dir}")
# Output: Created directory: product_data (if not exists)

# Exercise 1: Get the current working directory using os.getcwd().
# Solution:
# import os
# cwd = os.getcwd()
# print("Exercise 1 - Current directory:", cwd)
# # Output: Current directory: (current path)

# Exercise 2: Check if a file 'orders.csv' exists using os.path.exists().
# Solution:
# import os
# file_path = "orders.csv"
# exists = os.path.exists(file_path)
# print("Exercise 2 - File exists:", exists)
# # Output: File exists: False (unless file exists)

# Exercise 3: Create a directory 'logs' if it doesn’t exist.
# Solution:
# import os
# log_dir = "logs"
# if not os.path.exists(log_dir):
#     os.makedirs(log_dir)
#     print("Exercise 3 - Created directory:", log_dir)
# else:
#     print("Exercise 3 - Directory exists:", log_dir)
# # Output: Created directory: logs (if not exists)

# Notes:
# - os is essential in ML for file handling (e.g., datasets) or web apps for managing static files.
# - Use os.path for platform-independent paths (e.g., Windows vs. Linux).
# - Handle exceptions (e.g., PermissionError) for robust file operations.