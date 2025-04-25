# %% Purpose
# Python Modules and Packages: Standard Library - datetime
# Purpose: The datetime module handles dates, times, and time intervals.
# Key Features: Date arithmetic, formatting, time zones.

# %% 1. Working with Current Date and Time
# Explanation: Use datetime.now() to get current timestamp.
# Example:
import datetime

order_time = datetime.datetime.now()
print(f"Order placed at: {order_time.strftime('%Y-%m-%d %H:%M:%S')}")
# Output: Order placed at: 2025-04-25 HH:MM:SS (current time)

# %% 2. Date Arithmetic
# Explanation: Perform operations like adding days or calculating differences.
# Example:
import datetime

# Calculate delivery date (3 days from now)
order_date = datetime.datetime.now()
delivery_date = order_date + datetime.timedelta(days=3)
print(f"Expected delivery: {delivery_date.strftime('%Y-%m-%d')}")
# Output: Expected delivery: 2025-04-28 (3 days from now)

# %% 3. Retail Scenario with datetime
# Explanation: Track order timestamps and deadlines.
# Example:
import datetime

# Check if order is within return period (30 days)
order_date = datetime.datetime(2025, 3, 15)
today = datetime.datetime.now()
days_since_order = (today - order_date).days
return_status = "Eligible" if days_since_order <= 30 else "Not eligible"
print(f"Order from {order_date.strftime('%Y-%m-%d')}: Return {return_status}")
# Output: Order from 2025-03-15: Return Eligible (if within 30 days)

# %% Notes
# Notes:
# - datetime is critical in ML for time-series data or web apps for logging (e.g., order timestamps).
# - Use strftime() for formatting, strptime() for parsing strings.
# - Handle timezone-aware datetimes with pytz for production apps.