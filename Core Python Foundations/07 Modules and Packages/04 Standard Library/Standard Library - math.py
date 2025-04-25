# %% Purpose
# Python Modules and Packages: Standard Library - math
# Purpose: The math module provides mathematical functions and constants.
# Key Features: Trigonometric, logarithmic, and arithmetic operations.

# %% 1. Basic math Functions
# Explanation: Use functions like ceil(), floor(), and sqrt().
# Example:
import math

price = 49.99
ceiling_price = math.ceil(price)
square_root = math.sqrt(price)
print(f"Ceiling price: ${ceiling_price:.2f}, Square root: {square_root:.2f}")
# Output: Ceiling price: $50.00, Square root: 7.07

# %% 2. Using Constants
# Explanation: Access constants like pi and e.
# Example:
import math

# Calculate area of a circular product display
radius = 5
area = math.pi * radius ** 2
print(f"Display area: {area:.2f} square units")
# Output: Display area: 78.54 square units

# %% 3. Retail Scenario with math
# Explanation: Apply math functions for pricing calculations.
# Example:
import math

items = [99.99, 149.99, 199.99]
# Round prices to nearest 10
rounded_prices = [math.ceil(price / 10) * 10 for price in items]
print(f"Rounded prices: {rounded_prices}")
# Output: Rounded prices: [100, 150, 200]

# %% Notes
# Notes:
# - math module is useful in ML for numerical computations (e.g., distance metrics) or web apps for pricing.
# - Functions expect numeric inputs; handle errors with try-except (e.g., math.sqrt(-1)).
# - Use math for precise floating-point calculations.