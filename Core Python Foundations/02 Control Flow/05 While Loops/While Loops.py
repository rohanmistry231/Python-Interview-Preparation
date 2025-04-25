# Python Control Flow: While Loops
# Purpose: Learn While Loops to execute a block as long as a condition is True.
# Key Features: Flexible for dynamic iteration, requires termination condition.

# %% 1. Basic While Loop
# Explanation: Continue looping until the condition becomes False.
# Useful for tasks with unknown iteration counts.
stock = 50
while stock > 0:
    print(f"1.1 Stock remaining: {stock}")
    stock -= 10
# Example with counter
count = 1
while count <= 3:
    print(f"1.2 Count: {count}")
    count += 1

# Mini-Exercise: Reduce a price by 20 until it’s below 100.
price = 150
while price >= 100:
    print("1.3 Mini-Exercise: Price:", price)
    price -= 20

# %% 2. While with Conditionals
# Explanation: Combine with if-else for conditional logic within the loop.
# Common in dynamic pricing or inventory adjustments.
price = 1000
discount = 0
while price > 500:
    discount += 0.05
    price -= 100
    print(f"2.1 Price: {price}, Discount: {discount * 100}%")
# Example with if
stock_level = 80
while stock_level > 20:
    if stock_level > 50:
        print(f"2.2 High stock: {stock_level}")
    else:
        print(f"2.2 Moderate stock: {stock_level}")
    stock_level -= 20

# Mini-Exercise: Count up from 1 to 5, printing only odd numbers.
num = 1
while num <= 5:
    if num % 2 == 1:
        print("2.3 Mini-Exercise: Odd number:", num)
    num += 1

# %% 3. Infinite Loop with Break
# Explanation: Use break to exit an infinite loop based on a condition.
# Useful for controlled termination.
count = 0
while True:
    count += 1
    if count > 3:
        print("3.1 Breaking at count:", count)
        break
    print(f"3.1 Count: {count}")
# Example with condition
total = 0
while True:
    total += 10
    if total >= 50:
        print(f"3.2 Total reached: {total}")
        break

# Mini-Exercise: Increment a counter until it reaches 4, then break.
counter = 0
while True:
    counter += 1
    if counter >= 4:
        print("3.3 Mini-Exercise: Stopped at:", counter)
        break
    print("3.3 Mini-Exercise: Counter:", counter)

# %% 4. Exercises for Practice
# Exercise 1: Use a while loop to reduce a product’s price by 50 until it’s below 200.
price = 500
while price >= 200:
    price -= 50
    print("4.1 Exercise 1 - Reduced price:", price)

# Exercise 2: Count down from 10 to 1 using a while loop.
num = 10
while num >= 1:
    print("4.2 Exercise 2 - Countdown:", num)
    num -= 1

# Exercise 3: Use a while loop to find the first stock level below 30, starting from 100.
stock = 100
while stock >= 30:
    stock -= 10
print("4.3 Exercise 3 - First stock below 30:", stock)

# Exercise 4: Double a value starting from 1 until it exceeds 100.
value = 1
while value <= 100:
    value *= 2
    print("4.4 Exercise 4 - Value:", value)

# %% 5. Notes for Further Learning
# - Ensure while loops have a clear termination condition to avoid infinite loops.
# - Use in ML for iterative algorithms (e.g., gradient descent) or web apps for polling.
# - Combine with break/continue for fine-grained control (see later subtopics).
# - Test loop conditions to ensure all cases are handled.
# - Try the projects below to apply these concepts!