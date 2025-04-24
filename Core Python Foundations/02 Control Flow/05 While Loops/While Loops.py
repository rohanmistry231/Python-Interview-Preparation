# Python Control Flow: While Loops

# Purpose: While loops execute a block as long as a condition is True.
# Key Features: Flexible for dynamic iteration.

# 1. Basic While Loop
# Explanation: Continue looping until condition is False.
# Example:
stock = 50
while stock > 0:
    print(f"Stock remaining: {stock}")
    stock -= 10
# Output: Stock remaining: 50, 40, 30, 20, 10

# 2. While with Conditionals
# Explanation: Combine with if-else for complex logic.
# Example:
price = 1000
discount = 0
while price > 500:
    discount += 0.05
    price -= 100
    print(f"Price: {price}, Discount: {discount * 100}%")
# Output: Price: 900, Discount: 5.0%, Price: 800, Discount: 10.0%, ...

# 3. Infinite Loop with Break
# Explanation: Use break to exit an infinite loop based on a condition.
# Example:
count = 0
while True:
    count += 1
    if count > 3:
        break
    print(f"Count: {count}")
# Output: Count: 1, Count: 2, Count: 3

# Exercise 1: Use a while loop to reduce a product’s price by 50 until it’s below 200.
# Solution:
# price = 500
# while price >= 200:
#     price -= 50
#     print("Exercise 1 - Reduced price:", price)
# # Output: 450, 400, ..., 150

# Exercise 2: Count down from 10 to 1 using a while loop.
# Solution:
# num = 10
# while num >= 1:
#     print("Exercise 2 - Countdown:", num)
#     num -= 1
# # Output: 10, 9, ..., 1

# Exercise 3: Use a while loop to find the first stock level below 30, starting from 100.
# Solution:
# stock = 100
# while stock >= 30:
#     stock -= 10
# print("Exercise 3 - First stock below 30:", stock)
# # Output: 20

# Notes:
# - Ensure while loops have a termination condition to avoid infinite loops.
# - Use in ML for iterative algorithms (e.g., gradient descent) or web apps for polling.
# - Combine with break/continue for advanced control (see later subtopics).