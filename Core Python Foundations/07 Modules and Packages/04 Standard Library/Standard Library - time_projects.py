# time Projects
# Purpose: Apply time module through 10 retail-themed projects.
# Structure: Each project is separated by %% and includes description, tasks, and solution code.
# Note: Solutions use simulated inputs for reproducibility and match the updated base file outputs.

# %% Project 1: Current Timestamp
# Difficulty: Basic
# Description: Display the current Unix timestamp.
# Objective: Practice retrieving timestamps.
# Tasks:
# - Import time and use time().
# - Print the timestamp.
# Expected Output: Timestamp: (e.g., 1745102400.123)
import time

timestamp = time.time()
print(f"Timestamp: {timestamp}")

# %% Project 2: Readable Time Display
# Difficulty: Basic
# Description: Display the current time in a readable format.
# Objective: Practice formatting time.
# Tasks:
# - Import time and use ctime().
# - Print the current time.
# Expected Output: Current time: Fri Apr 25 14:30:45 2025
import time

current_time = time.ctime()
print(f"Current time: {current_time}")

# %% Project 3: Order Processing Delay
# Difficulty: Basic
# Description: Simulate a 2-second order processing delay.
# Objective: Practice using time.sleep().
# Tasks:
# - Import time and use sleep() for a 2-second delay.
# - Print processing messages.
# Expected Output: Processing...
#                 Done
import time

print("Processing...")
time.sleep(2)
print("Done")

# %% Project 4: Single Order Timer
# Difficulty: Intermediate
# Description: Measure the time to process a single order.
# Objective: Practice timing operations.
# Tasks:
# - Import time and measure a 1-second simulated task.
# - Print the processing time.
# Expected Output: Processing time: 1.00 seconds
import time

start = time.time()
time.sleep(1)
end = time.time()
print(f"Processing time: {end - start:.2f} seconds")

# %% Project 5: Batch Order Timer
# Difficulty: Intermediate
# Description: Measure the time to process multiple orders.
# Objective: Practice batch timing.
# Tasks:
# - Import time and measure a 2-second task for two orders.
# - Print the total time.
# Expected Output: Total time: 2.00 seconds
import time

start = time.time()
for order in ["Order 1", "Order 2"]:
    time.sleep(1)
end = time.time()
print(f"Total time: {end - start:.2f} seconds")

# %% Project 6: Time-Based Discount
# Difficulty: Intermediate
# Description: Offer a discount if processed within 3 seconds.
# Objective: Practice time-based logic.
# Tasks:
# - Import time and check if a task completes within 3 seconds.
# - Print the discount status.
# Expected Output: Discount applied: True
import time

start = time.time()
time.sleep(2)
end = time.time()
discount = (end - start) <= 3
print(f"Discount applied: {discount}")

# %% Project 7: Simulated Checkout Process
# Difficulty: Intermediate
# Description: Simulate a checkout with multiple delays.
# Objective: Practice combining delays.
# Tasks:
# - Import time and simulate a 3-step checkout with 1-second delays.
# - Print each step and total time.
# Expected Output: Step 1 done
#                 Step 2 done
#                 Step 3 done
#                 Total time: 3.00 seconds
import time

start = time.time()
for step in range(1, 4):
    time.sleep(1)
    print(f"Step {step} done")
end = time.time()
print(f"Total time: {end - start:.2f} seconds")

# %% Project 8: Performance Benchmark
# Difficulty: Advanced
# Description: Benchmark a retail calculation loop.
# Objective: Practice performance timing.
# Tasks:
# - Import time and measure a loop calculating 1000 prices.
# - Print the execution time.
# Expected Output: Benchmark time: (e.g., 0.01 seconds)
import time

start = time.time()
for _ in range(1000):
    price = 99.99 * 1.1
end = time.time()
print(f"Benchmark time: {end - start:.2f} seconds")

# %% Project 9: Scheduled Task Simulator
# Difficulty: Advanced
# Description: Simulate a scheduled retail task with delays.
# Objective: Practice advanced time management.
# Tasks:
# - Import time and simulate a task running every 2 seconds (3 runs).
# - Print each run’s timestamp.
# Expected Output: Task at (timestamp)
#                 Task at (timestamp)
#                 Task at (timestamp)
import time

for i in range(3):
    print(f"Task at {time.ctime()}")
    time.sleep(2)

# %% Project 10: Comprehensive Retail Timer
# Difficulty: Advanced
# Description: Time a retail operation with delays and timestamps.
# Objective: Practice integrating time functions.
# Tasks:
# - Import time, process orders with delays, and record timestamps.
# - Print timestamps and total time.
# Expected Output: Order 1 at (timestamp)
#                 Order 2 at (timestamp)
#                 Total time: 2.00 seconds
import time

start = time.time()
for i, order in enumerate(["Order 1", "Order 2"], 1):
    print(f"Order {i} at {time.ctime()}")
    time.sleep(1)
end = time.time()
print(f"Total time: {end - start:.2f} seconds")