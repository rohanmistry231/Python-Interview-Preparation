# Importing Modules Projects
# Purpose: Apply Importing Modules through 10 retail-themed projects.
# Structure: Each project is separated by %% and includes description, tasks, and solution code.
# Note: Solutions use simulated inputs for reproducibility and match the updated base file outputs.

# %% Project 1: Price Rounding with Math
# Difficulty: Basic
# Description: Use the math module to round up a product price.
# Objective: Practice basic module imports.
# Tasks:
# - Import the math module.
# - Use math.ceil to round up a price.
# - Print the rounded price.
# Expected Output: Rounded price: $30.00
import math

price = 29.99
rounded_price = math.ceil(price)
print(f"Rounded price: ${rounded_price:.2f}")

# %% Project 2: Random Product Selector
# Difficulty: Basic
# Description: Select a random product from a list using the random module.
# Objective: Practice importing specific module functions.
# Tasks:
# - Import the choice function from the random module.
# - Define a list of products and select one randomly.
# - Print the selected product.
# Expected Output: Selected product: (e.g., Laptop)
from random import choice

products = ["Laptop", "Smartphone", "Coffee Maker"]
selected_product = choice(products)
print(f"Selected product: {selected_product}")

# %% Project 3: Order Timestamp Recorder
# Difficulty: Basic
# Description: Record the current timestamp for an order using datetime.
# Objective: Practice using aliases with imports.
# Tasks:
# - Import datetime as dt.
# - Get the current timestamp and format it as YYYY-MM-DD.
# - Print the formatted timestamp.
# Expected Output: Order date: 2025-04-25
import datetime as dt

order_time = dt.datetime.now()
print(f"Order date: {order_time.strftime('%Y-%m-%d')}")

# %% Project 4: UUID Order ID Generator
# Difficulty: Intermediate
# Description: Generate a unique order ID using the uuid module.
# Objective: Practice importing and using unique identifiers.
# Tasks:
# - Import the uuid module.
# - Generate a UUID4 and use its first 8 characters as an order ID.
# - Print the order ID.
# Expected Output: Order ID: (e.g., 123e4567)
import uuid

order_id = str(uuid.uuid4())[:8]
print(f"Order ID: {order_id}")

# %% Project 5: JSON Order Formatter
# Difficulty: Intermediate
# Description: Format order data as JSON using the json module.
# Objective: Practice working with data serialization.
# Tasks:
# - Import the json module.
# - Create a dictionary with order details and convert it to a JSON string.
# - Print the JSON string.
# Expected Output: Order JSON: {"order_id": 101, "total": 999.99}
import json

order = {"order_id": 101, "total": 999.99}
order_json = json.dumps(order)
print(f"Order JSON: {order_json}")

# %% Project 6: File Path Validator
# Difficulty: Intermediate
# Description: Validate a file path for retail data using the os module.
# Objective: Practice module imports for file system operations.
# Tasks:
# - Import the os module.
# - Check if a given path (e.g., "data/orders.csv") exists.
# - Print whether the path exists.
# Expected Output: Path exists: False
import os

path = "data/orders.csv"
exists = os.path.exists(path)
print(f"Path exists: {exists}")

# %% Project 7: Statistical Price Analysis
# Difficulty: Intermediate
# Description: Calculate the average price of products using the statistics module.
# Objective: Practice statistical computations with modules.
# Tasks:
# - Import the statistics module.
# - Define a list of product prices and compute the mean.
# - Print the average price.
# Expected Output: Average price: $349.99
import statistics

prices = [999.99, 49.99, 0.01]
average_price = statistics.mean(prices)
print(f"Average price: ${average_price:.2f}")

# %% Project 8: Secure Password Generator
# Difficulty: Advanced
# Description: Generate a secure password for a retail account using secrets.
# Objective: Practice secure random generation.
# Tasks:
# - Import the secrets module.
# - Generate a 12-character password using letters, digits, and symbols.
# - Print the generated password.
# Expected Output: Password: (e.g., X7#kP9mZ2qL5)
import secrets
import string

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(characters) for _ in range(12))
print(f"Password: {password}")

# %% Project 9: CSV Data Reader
# Difficulty: Advanced
# Description: Read product data from a CSV string using the csv module.
# Objective: Practice data parsing with modules.
# Tasks:
# - Import the csv module.
# - Parse a CSV string with product names and prices.
# - Print the first product’s details.
# Expected Output: Product: Laptop, Price: $999.99
import csv
import io

csv_data = "name,price\nLaptop,999.99\nSmartphone,699.99"
csv_file = io.StringIO(csv_data)
reader = csv.DictReader(csv_file)
first_product = next(reader)
print(f"Product: {first_product['name']}, Price: ${float(first_product['price']):.2f}")

# %% Project 10: Timezone Order Tracker
# Difficulty: Advanced
# Description: Track order timestamps in a specific timezone using zoneinfo.
# Objective: Practice advanced datetime handling.
# Tasks:
# - Import the zoneinfo module.
# - Get the current time in the America/New_York timezone.
# - Print the formatted timestamp.
# Expected Output: Order time: 2025-04-25 14:30:45-04:00
from datetime import datetime
from zoneinfo import ZoneInfo

order_time = datetime.now(tz=ZoneInfo("America/New_York"))
print(f"Order time: {order_time.strftime('%Y-%m-%d %H:%M:%S%z')}")