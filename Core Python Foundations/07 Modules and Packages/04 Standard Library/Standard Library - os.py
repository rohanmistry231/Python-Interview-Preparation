# %% Purpose
# Python Modules and Packages: Standard Library - os
# Purpose: The os module interacts with the operating system (e.g., file handling, directories).
# Key Features: File operations, path management, environment variables.

# %% 1. Working with Directories
# Explanation: Use os.getcwd() and os.listdir() for directory operations.
# Example:
import os

current_dir = os.getcwd()
print(f"Current directory: {current_dir}")
files = os.listdir(current_dir)
print(f"Files in directory: {files}")
# Output: Current directory: (current path)
#         Files in directory: (list of files, e.g., ['script.py'])

# %% 2. File Path Handling
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

# %% 3. Retail Scenario with os
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

# %% Notes
# Notes:
# - os is essential in ML for file handling (e.g., datasets) or web apps for managing static files.
# - Use os.path for platform-independent paths (e.g., Windows vs. Linux).
# - Handle exceptions (e.g., PermissionError) for robust file operations.