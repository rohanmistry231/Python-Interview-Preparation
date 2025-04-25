# random Projects
# Purpose: Apply random module through 10 retail-themed projects.
# Structure: Each project is separated by %% and includes description, tasks, and solution code.
# Note: Solutions use simulated inputs for reproducibility and match the updated base file outputs.

# %% Project 1: Random Order ID Generator
# Difficulty: Basic
# Description: Generate a random order ID.
# Objective: Practice generating random integers.
# Tasks:
# - Import random and use randint() to generate an ID.
# - Print the order ID.
# Expected Output: Order ID: (e.g., 5321)
import random

order_id = random.randint(1000, 9999)
print(f"Order ID: {order_id}")

# %% Project 2: Random Product Selector
# Difficulty: Basic
# Description: Select a random product for promotion.
# Objective: Practice random selection.
# Tasks:
# - Import random and use choice() on a product list.
# - Print the selected product.
# Expected Output: Featured product: (e.g., Smartphone)
import random

products = ["Laptop", "Smartphone", "Mouse"]
featured_product = random.choice(products)
print(f"Featured product: {featured_product}")

# %% Project 3: Random Discount Generator
# Difficulty: Basic
# Description: Generate a random discount percentage.
# Objective: Practice generating random floats.
# Tasks:
# - Import random and use uniform() for a discount rate.
# - Print the discount percentage.
# Expected Output: Discount: 15.23%
import random

discount = random.uniform(0.05, 0.2)
print(f"Discount: {discount:.2%}")

# %% Project 4: Random Stock Allocator
# Difficulty: Intermediate
# Description: Assign random stock levels to products.
# Objective: Practice random number generation for multiple items.
# Tasks:
# - Import random and use randint() for two products.
# - Print the stock levels.
# Expected Output: Stock: {'Laptop': 45, 'Mouse': 72}
import random

products = ["Laptop", "Mouse"]
stock_levels = {product: random.randint(10, 100) for product in products}
print(f"Stock: {stock_levels}")

# %% Project 5: Random Category Selector
# Difficulty: Intermediate
# Description: Select a random product category for a sale.
# Objective: Practice random selection with categories.
# Tasks:
# - Import random and use choice() on a category list.
# - Print the selected category.
# Expected Output: Sale category: Electronics
import random

categories = ["Electronics", "Appliances", "Clothing"]
selected_category = random.choice(categories)
print(f"Sale category: {selected_category}")

# %% Project 6: Random Product Sampler
# Difficulty: Intermediate
# Description: Select two random products for a bundle.
# Objective: Practice sampling multiple items.
# Tasks:
# - Import random and use sample() on a product list.
# - Print the selected products.
# Expected Output: Bundle: ['Laptop', 'Mouse']
import random

products = ["Laptop", "Smartphone", "Mouse", "Blender"]
selected_products = random.sample(products, 2)
print(f"Bundle: {selected_products}")

# %% Project 7: Shuffled Product Display
# Difficulty: Intermediate
# Description: Shuffle a list of products for display.
# Objective: Practice list shuffling.
# Tasks:
# - Import random and use shuffle() on a product list.
# - Print the shuffled list.
# Expected Output: Shuffled display: (e.g., ['Mouse', 'Laptop', 'Smartphone'])
import random

products = ["Laptop", "Smartphone", "Mouse"]
random.shuffle(products)
print(f"Shuffled display: {products}")

# %% Project 8: Seeded Random Discount
# Difficulty: Advanced
# Description: Generate reproducible random discounts.
# Objective: Practice using random.seed().
# Tasks:
# - Import random, set a seed, and use uniform() for a discount.
# - Print the discount percentage.
# Expected Output: Discount: 12.34%
import random

random.seed(42)
discount = random.uniform(0.05, 0.2)
print(f"Discount: {discount:.2%}")

# %% Project 9: Weighted Product Selector
# Difficulty: Advanced
# Description: Select a product with weighted probabilities.
# Objective: Practice weighted random choices.
# Tasks:
# - Import random and use choices() with weights.
# - Print the selected product.
# Expected Output: Featured product: (e.g., Laptop)
import random

products = ["Laptop", "Smartphone", "Mouse"]
weights = [0.5, 0.3, 0.2]
selected_product = random.choices(products, weights=weights, k=1)[0]
print(f"Featured product: {selected_product}")

# %% Project 10: Comprehensive Random Promotion
# Difficulty: Advanced
# Description: Create a random promotion with ID, product, and discount.
# Objective: Practice combining random functions.
# Tasks:
# - Import random, generate an ID, select a product, and set a discount.
# - Print the promotion details.
# Expected Output: Promotion: ID 4321, Product: Smartphone, Discount: 10.50%
import random

order_id = random.randint(1000, 9999)
products = ["Laptop", "Smartphone", "Mouse"]
product = random.choice(products)
discount = random.uniform(0.05, 0.15)
print(f"Promotion: ID {order_id}, Product: {product}, Discount: {discount:.2%}")