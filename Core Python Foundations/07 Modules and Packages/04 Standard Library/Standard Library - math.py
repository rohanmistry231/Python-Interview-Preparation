# Python Modules and Packages: Standard Library - math

# Purpose: The math module provides mathematical functions and constants.
# Key Features: Trigonometric, logarithmic, and arithmetic operations.

# 1. Basic math Functions
# Explanation: Use functions like ceil(), floor(), and sqrt().
# Example:
import math

price = 49.99
ceiling_price = math.ceil(price)
square_root = math.sqrt(price)
print(f"Ceiling price: ${ceiling_price:.2f}, Square root: {square_root:.2f}")
# Output: Ceiling price: $50.00, Square root: 7.07

# 2. Using Constants
# Explanation: Access constants like pi and e.
# Example:
import math

# Calculate area of a circular product display
radius = 5
area = math.pi * radius ** 2
print(f"Display area: {area:.2f} square units")
# Output: Display area: 78.54 square units

# 3. Retail Scenario with math
# Explanation: Apply math functions for pricing calculations.
# Example:
import math

items = [99.99, 149.99, 199.99]
# Round prices to nearest 10
rounded_prices = [math.ceil(price / 10) * 10 for price in items]
print(f"Rounded prices: {rounded_prices}")
# Output: Rounded prices: [100, 150, 200]

# Exercise 1: Use math.floor() to round down a product price.
# Solution:
# import math
# price = 29.99
# floored_price = math.floor(price)
# print("Exercise 1 - Floored price:", floored_price)
# # Output: Floored price: 29

# Exercise 2: Calculate the logarithm of a stock quantity using math.log().
# Solution:
# import math
# stock = 100
# log_stock = math.log(stock)
# print("Exercise 2 - Log of stock:", log_stock)
# # Output: Log of stock: 4.605170185988092

# Exercise 3: Use math.pow() to calculate the total cost for multiple units.
# Solution:
# import math
# price_per_unit = 19.99
# units = 3
# total = math.pow(price_per_unit, 1) * units  # Equivalent to price_per_unit * units
# print("Exercise 3 - Total cost:", total)
# # Output: Total cost: 59.97

# Notes:
# - math module is useful in ML for numerical computations (e.g., distance metrics) or web apps for pricing.
# - Functions expect numeric inputs; handle errors with try-except (e.g., math.sqrt(-1)).
# - Use math for precise floating-point calculations.