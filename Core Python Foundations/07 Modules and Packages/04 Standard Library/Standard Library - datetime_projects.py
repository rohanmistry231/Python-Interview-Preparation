# datetime Projects
# Purpose: Apply datetime module through 10 retail-themed projects.
# Structure: Each project is separated by %% and includes description, tasks, and solution code.
# Note: Solutions use simulated inputs for reproducibility and match the updated base file outputs.

# %% Project 1: Current Order Date
# Difficulty: Basic
# Description: Record the current date for an order.
# Objective: Practice retrieving the current date.
# Tasks:
# - Import datetime and get the current date using datetime.date.today().
# - Print the current date.
# Expected Output: Order date: 2025-04-25
import datetime

current_date = datetime.date.today()
print(f"Order date: {current_date}")

# %% Project 2: Delivery Date Calculator
# Difficulty: Basic
# Description: Calculate the delivery date by adding 5 days to the order date.
# Objective: Practice basic date arithmetic.
# Tasks:
# - Import datetime and add 5 days to the current date.
# - Print the delivery date in YYYY-MM-DD format.
# Expected Output: Delivery date: 2025-04-30
import datetime

order_date = datetime.date.today()
delivery_date = order_date + datetime.timedelta(days=5)
print(f"Delivery date: {delivery_date}")

# %% Project 3: Return Period Checker
# Difficulty: Basic
# Description: Check if an order is within a 30-day return period.
# Objective: Practice calculating date differences.
# Tasks:
# - Import datetime and compare an order date (2025-03-26) with today.
# - Print whether the order is eligible for return.
# Expected Output: Return status: Eligible
import datetime

order_date = datetime.date(2025, 3, 26)
today = datetime.date.today()
days_since_order = (today - order_date).days
return_status = "Eligible" if days_since_order <= 30 else "Not eligible"
print(f"Return status: {return_status}")

# %% Project 4: Order Time Formatter
# Difficulty: Intermediate
# Description: Format the current order timestamp with hours and minutes.
# Objective: Practice datetime formatting.
# Tasks:
# - Import datetime and get the current timestamp.
# - Print the timestamp in YYYY-MM-DD HH:MM format.
# Expected Output: Order time: 2025-04-25 14:30
import datetime

order_time = datetime.datetime.now()
print(f"Order time: {order_time.strftime('%Y-%m-%d %H:%M')}")

# %% Project 5: Weekly Sales Period
# Difficulty: Intermediate
# Description: Define a one-week sales period starting today.
# Objective: Practice date arithmetic with timedelta.
# Tasks:
# - Import datetime and calculate the end date (7 days from today).
# - Print the start and end dates.
# Expected Output: Sales period: 2025-04-25 to 2025-05-02
import datetime

start_date = datetime.date.today()
end_date = start_date + datetime.timedelta(days=7)
print(f"Sales period: {start_date} to {end_date}")

# %% Project 6: Parse Order Date
# Difficulty: Intermediate
# Description: Parse a string order date into a datetime object.
# Objective: Practice parsing datetime strings.
# Tasks:
# - Import datetime and parse "2025-04-01" using strptime.
# - Print the parsed date.
# Expected Output: Parsed order date: 2025-04-01
import datetime

order_date_str = "2025-04-01"
parsed_date = datetime.datetime.strptime(order_date_str, '%Y-%m-%d').date()
print(f"Parsed order date: {parsed_date}")

# %% Project 7: Days Since Last Order
# Difficulty: Intermediate
# Description: Calculate days since a customer’s last order.
# Objective: Practice advanced date differences.
# Tasks:
# - Import datetime and calculate days between today and 2025-03-01.
# - Print the number of days.
# Expected Output: Days since last order: 55
import datetime

last_order = datetime.date(2025, 3, 1)
today = datetime.date.today()
days_since = (today - last_order).days
print(f"Days since last order: {days_since}")

# %% Project 8: Store Opening Hours
# Difficulty: Advanced
# Description: Check if the store is open based on the current time.
# Objective: Practice datetime comparisons.
# Tasks:
# - Import datetime and check if the current time is between 09:00 and 17:00.
# - Print whether the store is open.
# Expected Output: Store status: Open
import datetime

current_time = datetime.datetime.now().time()
open_time = datetime.time(9, 0)
close_time = datetime.time(17, 0)
status = "Open" if open_time <= current_time <= close_time else "Closed"
print(f"Store status: {status}")

# %% Project 9: Timezone-Aware Order
# Difficulty: Advanced
# Description: Record an order timestamp in a specific timezone.
# Objective: Practice timezone handling with pytz.
# Tasks:
# - Import datetime and pytz, and get the current time in America/New_York.
# - Print the timestamp in YYYY-MM-DD HH:MM:SS TZ format.
# Expected Output: Order time: 2025-04-25 14:30:00-04:00
import datetime
import pytz

tz = pytz.timezone("America/New_York")
order_time = datetime.datetime.now(tz)
print(f"Order time: {order_time.strftime('%Y-%m-%d %H:%M:%S%z')}")

# %% Project 10: Comprehensive Order Tracker
# Difficulty: Advanced
# Description: Track order details with timestamps and return eligibility.
# Objective: Practice combining datetime features.
# Tasks:
# - Import datetime and create an order with a timestamp (2025-04-01).
# - Check return eligibility and print order details.
# Expected Output: Order on 2025-04-01: Return Eligible
import datetime

order_date = datetime.datetime(2025, 4, 1)
today = datetime.datetime.now()
days_since = (today - order_date).days
return_status = "Eligible" if days_since <= 30 else "Not eligible"
print(f"Order on {order_date.strftime('%Y-%m-%d')}: Return {return_status}")