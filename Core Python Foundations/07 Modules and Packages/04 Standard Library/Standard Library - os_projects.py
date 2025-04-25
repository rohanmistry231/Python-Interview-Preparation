# os Projects
# Purpose: Apply os module through 10 retail-themed projects.
# Structure: Each project is separated by %% and includes description, tasks, and solution code.
# Note: Solutions use simulated inputs for reproducibility and match the updated base file outputs.

# %% Project 1: Current Directory Viewer
# Difficulty: Basic
# Description: Display the current working directory.
# Objective: Practice basic directory operations.
# Tasks:
# - Import os and use getcwd().
# - Print the current directory.
# Expected Output: Current directory: (current path)
import os

current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# %% Project 2: File List Viewer
# Difficulty: Basic
# Description: List files in the current directory.
# Objective: Practice directory listing.
# Tasks:
# - Import os and use listdir().
# - Print the list of files.
# Expected Output: Files: (list of files)
import os

files = os.listdir()
print(f"Files: {files}")

# %% Project 3: Path Constructor
# Difficulty: Basic
# Description: Construct a file path for a retail database.
# Objective: Practice path manipulation.
# Tasks:
# - Import os and use path.join() to create a path.
# - Print the file path.
# Expected Output: File path: data/products.csv
import os

file_path = os.path.join("data", "products.csv")
print(f"File path: {file_path}")

# %% Project 4: Directory Creator
# Difficulty: Intermediate
# Description: Create a directory for retail logs if it doesn’t exist.
# Objective: Practice directory creation.
# Tasks:
# - Import os and use makedirs() to create a logs directory.
# - Print the creation status.
# Expected Output: Created directory: logs
import os

log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
    print(f"Created directory: {log_dir}")
else:
    print(f"Directory exists: {log_dir}")

# %% Project 5: File Existence Checker
# Difficulty: Intermediate
# Description: Check if a product data file exists.
# Objective: Practice file existence checks.
# Tasks:
# - Import os and use path.exists() on a file path.
# - Print whether the file exists.
# Expected Output: File exists: False
import os

file_path = "products.csv"
exists = os.path.exists(file_path)
print(f"File exists: {exists}")

# %% Project 6: File Size Checker
# Difficulty: Intermediate
# Description: Check the size of a retail data file.
# Objective: Practice file attribute access.
# Tasks:
# - Import os and use path.getsize() on a file path.
# - Print the file size or an error if it doesn’t exist.
# Expected Output: File size: (size in bytes or error)
import os

file_path = "products.csv"
try:
    size = os.path.getsize(file_path)
    print(f"File size: {size} bytes")
except FileNotFoundError:
    print(f"File size: File not found")

# %% Project 7: Environment Variable Reader
# Difficulty: Intermediate
# Description: Read a retail configuration from an environment variable.
# Objective: Practice accessing environment variables.
# Tasks:
# - Import os and use getenv() to read an environment variable.
# - Print the variable value or a default.
# Expected Output: Store name: RetailWorld
import os

store_name = os.getenv("STORE_NAME", "RetailWorld")
print(f"Store name: {store_name}")

# %% Project 8: Recursive Directory Creator
# Difficulty: Advanced
# Description: Create a nested directory structure for retail data.
# Objective: Practice advanced directory operations.
# Tasks:
# - Import os and use makedirs() with exist_ok for a nested path.
# - Print the creation status.
# Expected Output: Created directory: data/2025/sales
import os

nested_dir = os.path.join("data", "2025", "sales")
os.makedirs(nested_dir, exist_ok=True)
print(f"Created directory: {nested_dir}")

# %% Project 9: File Modification Time
# Difficulty: Advanced
# Description: Check the last modification time of a retail file.
# Objective: Practice file metadata access.
# Tasks:
# - Import os and use path.getmtime() on a file path.
# - Print the modification time or an error.
# Expected Output: Last modified: (timestamp or error)
import os
import time

file_path = "products.csv"
try:
    mtime = os.path.getmtime(file_path)
    print(f"Last modified: {time.ctime(mtime)}")
except FileNotFoundError:
    print(f"Last modified: File not found")

# %% Project 10: Comprehensive File Manager
# Difficulty: Advanced
# Description: Manage retail data files with directory and file operations.
# Objective: Practice integrating os functions.
# Tasks:
# - Import os, create a directory, construct a file path, and check existence.
# - Print the results.
# Expected Output: Directory created: data, Path: data/sales.csv, Exists: False
import os

data_dir = "data"
file_path = os.path.join(data_dir, "sales.csv")
os.makedirs(data_dir, exist_ok=True)
exists = os.path.exists(file_path)
print(f"Directory created: {data_dir}, Path: {file_path}, Exists: {exists}")