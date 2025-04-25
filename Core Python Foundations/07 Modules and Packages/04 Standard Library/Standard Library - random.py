# %% Purpose
# Python Modules and Packages: Standard Library - random
# Purpose: The random module generates pseudo-random numbers and selections.
# Key Features: Random numbers, choices, shuffling.

# %% 1. Generating Random Numbers
# Explanation: Use randint() for integers, uniform() for floats.
# Example:
import random

# Simulate random discount percentage
discount = random.uniform(0.05, 0.2)
price = 999.99
discounted_price = price * (1 - discount)
print(f"Random discount: {discount:.2%}, Discounted price: ${discounted_price:.2f}")
# Output: Random discount: (e.g., 12.34%), Discounted price: (e.g., $876.65)

# %% 2. Random Selection
# Explanation: Use choice() or sample() for selecting items.
# Example:
import random

products = ["Laptop", "Smartphone", "Coffee Maker"]
featured_product = random.choice(products)
print(f"Featured product: {featured_product}")
# Output: Featured product: (random product)

# %% 3. Retail Scenario with random
# Explanation: Simulate random stock or promotional offers.
# Example:
import random

# Simulate random stock levels for multiple products
stock_levels = {product: random.randint(10, 100) for product in ["Mouse", "Keyboard"]}
print(f"Random stock levels: {stock_levels}")
# Output: Random stock levels: {'Mouse': (random), 'Keyboard': (random)}

# %% Notes
# Notes:
# - random is pseudo-random; use random.seed() for reproducibility in ML (e.g., data splitting).
# - Useful in web apps for random promotions or A/B testing.
# - Avoid in cryptographic applications (use secrets module instead).