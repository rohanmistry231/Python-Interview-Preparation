# Python Control Flow: Pass Statement

# Purpose: Pass statement is a placeholder that does nothing, used for syntactical completeness.
# Key Features: Enables empty blocks during development.

# 1. Pass in Conditionals
# Explanation: Use pass when a block is required but no action is needed.
# Example:
price = 999.99
if price > 1000:
    print("Luxury product")
else:
    pass  # Placeholder for future logic
# Output: (No output, as price <= 1000)

# 2. Pass in Loops
# Explanation: Use pass in loops to skip implementation temporarily.
# Example:
products = ["Laptop", "Smartphone", "Coffee Maker"]
for product in products:
    if product == "Smartphone":
        pass  # Will add logic later
    else:
        print(f"Processing {product}")
# Output: Processing Laptop, Processing Coffee Maker

# 3. Pass in Functions or Classes
# Explanation: Use pass for unimplemented functions or class methods.
# Example:
def calculate_discount(price):
    pass  # To be implemented later
class Product:
    def update_stock(self):
        pass  # Placeholder for method
product = Product()
print("Created Product object (no action)")
# Output: Created Product object (no action)

# Exercise 1: Use pass in an if-else block to skip budget products (< 100).
# Solution:
# price = 50
# if price < 100:
#     pass
# else:
#     print("Exercise 1 - Non-budget price:", price)
# # Output: (No output, as price < 100)

# Exercise 2: Use pass in a for loop to skip a specific product.
# Solution:
# items = ["Mouse", "Keyboard", "Monitor"]
# for item in items:
#     if item == "Keyboard":
#         pass
#     else:
#         print("Exercise 2 - Processing:", item)
# # Output: Processing: Mouse, Processing: Monitor

# Exercise 3: Define a placeholder function for stock checking with pass.
# Solution:
# def check_stock(stock):
#     pass
# print("Exercise 3 - Placeholder function defined")
# # Output: Placeholder function defined

# Notes:
# - Pass is a no-op, used during development to avoid syntax errors.
# - Common in ML for placeholder model training functions or web apps for API stubs.
# - Replace pass with actual logic as development progresses.