# %% Purpose
# Python Modules and Packages: Standard Library - time
# Purpose: The time module provides time-related functions (e.g., delays, timestamps).
# Key Features: Measure execution time, add delays, format time.

# %% 1. Getting Current Time
# Explanation: Use time.time() for Unix timestamp, time.ctime() for readable time.
# Example:
import time

current_time = time.ctime()
print(f"Current time: {current_time}")
# Output: Current time: Fri Apr 25 HH:MM:SS 2025 (current time)

# %% 2. Adding Delays
# Explanation: Use time.sleep() to pause execution.
# Example:
import time

print("Processing order...")
time.sleep(2)  # Simulate processing delay
print("Order processed")
# Output: Processing order...
#         (2-second pause)
#         Order processed

# %% 3. Retail Scenario with time
# Explanation: Measure time for retail operations (e.g., batch processing).
# Example:
import time

# Simulate processing multiple orders
orders = ["Order 101", "Order 102", "Order 103"]
start_time = time.time()
for order in orders:
    print(f"Processing {order}")
    time.sleep(1)  # Simulate work
end_time = time.time()
print(f"Total processing time: {end_time - start_time:.2f} seconds")
# Output: Processing Order 101
#         Processing Order 102
#         Processing Order 103
#         Total processing time: 3.01 seconds (approx)

# %% Notes
# Notes:
# - time is useful in ML for profiling code or web apps for scheduling tasks.
# - time.time() returns seconds since epoch (Jan 1, 1970); use for timing.
# - For date handling, prefer datetime module.