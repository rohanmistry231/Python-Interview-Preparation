# math Projects
# Purpose: Apply math module through 10 retail-themed projects.
# Structure: Each project is separated by %% and includes description, tasks, and solution code.
# Note: Solutions use simulated inputs for reproducibility and match the updated base file outputs.

# %% Project 1: Price Ceiling Calculator
# Difficulty: Basic
# Description: Round up a product price to the nearest integer.
# Objective: Practice basic math functions.
# Tasks:
# - Import math and use ceil() on a price.
# - Print the ceiling price.
# Expected Output: Ceiling price: $30.00
import math

price = 29.99
ceiling_price = math.ceil(price)
print(f"Ceiling price: ${ceiling_price:.2f}")

# %% Project 2: Price Flooring Calculator
# Difficulty: Basic
# Description: Round down a product price to the nearest integer.
# Objective: Practice basic math functions.
# Tasks:
# - Import math and use floor() on a price.
# - Print the floored price.
# Expected Output: Floored price: $29.00
import math

price = 29.99
floored_price = math.floor(price)
print(f"Floored price: ${floored_price:.2f}")

# %% Project 3: Display Area Calculator
# Difficulty: Basic
# Description: Calculate the area of a circular product display.
# Objective: Practice using math constants.
# Tasks:
# - Import math and calculate the area using pi and radius 3.
# - Print the area.
# Expected Output: Display area: 28.27 square units
import math

radius = 3
area = math.pi * radius ** 2
print(f"Display area: {area:.2f} square units")

# %% Project 4: Logarithmic Stock Analysis
# Difficulty: Intermediate
# Description: Calculate the logarithm of a stock quantity.
# Objective: Practice logarithmic functions.
# Tasks:
# - Import math and use log() on a stock value.
# - Print the logarithm.
# Expected Output: Stock logarithm: 4.61
import math

stock = 100
log_stock = math.log(stock)
print(f"Stock logarithm: {log_stock:.2f}")

# %% Project 5: Power-Based Discount
# Difficulty: Intermediate
# Description: Apply a discount using a power function.
# Objective: Practice power calculations.
# Tasks:
# - Import math and use pow() to calculate a discounted price.
# - Print the discounted price.
# Expected Output: Discounted price: $90.00
import math

price = 100
discount_factor = 0.9
discounted_price = math.pow(price, 1) * discount_factor
print(f"Discounted price: ${discounted_price:.2f}")

# %% Project 6: Nearest Ten Rounder
# Difficulty: Intermediate
# Description: Round a price to the nearest 10.
# Objective: Practice combining math functions.
# Tasks:
# - Import math and round a price to the nearest 10 using ceil().
# - Print the rounded price.
# Expected Output: Rounded price: $100.00
import math

price = 95.99
rounded_price = math.ceil(price / 10) * 10
print(f"Rounded price: ${rounded_price:.2f}")

# %% Project 7: Factorial Quantity Calculator
# Difficulty: Intermediate
# Description: Calculate the factorial of a small order quantity.
# Objective: Practice factorial calculations.
# Tasks:
# - Import math and use factorial() on a quantity.
# - Print the factorial.
# Expected Output: Order factorial: 120
import math

quantity = 5
factorial = math.factorial(quantity)
print(f"Order factorial: {factorial}")

# %% Project 8: Trigonometric Display Angle
# Difficulty: Advanced
# Description: Calculate the sine of an angle for a product display.
# Objective: Practice trigonometric functions.
# Tasks:
# - Import math and calculate sin(30 degrees).
# - Print the sine value.
# Expected Output: Display sine: 0.50
import math

angle_degrees = 30
angle_radians = math.radians(angle_degrees)
sine_value = math.sin(angle_radians)
print(f"Display sine: {sine_value:.2f}")

# %% Project 9: Exponential Growth Forecast
# Difficulty: Advanced
# Description: Forecast sales growth using an exponential function.
# Objective: Practice exponential calculations.
# Tasks:
# - Import math and use exp() to model sales growth.
# - Print the forecasted sales.
# Expected Output: Forecasted sales: $271.83
import math

initial_sales = 100
growth_rate = 1
forecasted_sales = initial_sales * math.exp(growth_rate)
print(f"Forecasted sales: ${forecasted_sales:.2f}")

# %% Project 10: Comprehensive Pricing System
# Difficulty: Advanced
# Description: Combine multiple math functions for pricing calculations.
# Objective: Practice integrating math functions.
# Tasks:
# - Import math and calculate ceiling, square root, and rounded price.
# - Print all results.
# Expected Output: Ceiling: $100.00, Sqrt: 9.95, Rounded: $100.00
import math

price = 99.49
ceiling = math.ceil(price)
sqrt_price = math.sqrt(price)
rounded = math.ceil(price / 10) * 10
print(f"Ceiling: ${ceiling:.2f}, Sqrt: {sqrt_price:.2f}, Rounded: ${rounded:.2f}")