# Python Dictionary Projects
# Purpose: Apply Python Dictionary knowledge through 10 optimized projects (Basic to Advanced).
# Structure: Each project is separated by %% and includes description, tasks, and best solution.
# Note: Solutions are designed for clarity, efficiency, and beginner learning.

# %% Project 1: Product Catalog Manager
# Difficulty: Basic
# Description: Create a program to manage a product catalog using a dictionary.
# Objective: Practice creating, adding, and accessing key-value pairs.
# Tasks:
# - Initialize a dictionary with 3 product details (id, name, price).
# - Add a new key-value pair for stock.
# - Update the price.
# - Print the dictionary and the product name.
product = {"id": 1, "name": "Laptop", "price": 999.99}
product["stock"] = 50  # Add stock
product["price"] = 899.99  # Update price
print("Product:", product)
print("Product name:", product["name"])

# %% Project 2: Student Profile
# Difficulty: Basic
# Description: Store and update a student's profile in a dictionary.
# Objective: Practice updating and accessing dictionary values.
# Tasks:
# - Create a dictionary with student details (name, age, grade).
# - Update the grade to a new value.
# - Add a subject key with a default value.
# - Print all keys and the student’s age.
student = {"name": "Alice", "age": 20, "grade": "B"}
student["grade"] = "A"  # Update grade
student["subject"] = "Math"  # Add subject
print("Keys:", list(student.keys()))
print("Age:", student["age"])

# %% Project 3: Book Inventory
# Difficulty: Basic
# Description: Manage a book inventory with title and quantity.
# Objective: Practice dictionary methods like pop() and setdefault().
# Tasks:
# - Create a dictionary with 2 books (title: quantity).
# - Use setdefault() to add a new book with quantity 0 if it doesn’t exist.
# - Remove a book using pop().
# - Print the updated dictionary.
books = {"1984": 10, "The Great Gatsby": 5}
books.setdefault("Moby Dick", 0)  # Add book with default quantity
books.pop("The Great Gatsby")  # Remove book
print("Book inventory:", books)

# %% Project 4: Employee Database
# Difficulty: Intermediate
# Description: Store employee details in a dictionary with nested information.
# Objective: Work with nested dictionaries and iteration.
# Tasks:
# - Create a dictionary with 3 employees (id: {name, department}).
# - Add a new employee.
# - Print all employee names and their departments.
# - Count the number of employees.
employees = {
    "E001": {"name": "Alice", "department": "HR"},
    "E002": {"name": "Bob", "department": "IT"},
    "E003": {"name": "Charlie", "department": "Sales"}
}
employees["E004"] = {"name": "Dana", "department": "Marketing"}  # Add employee
for emp_id, details in employees.items():
    print(f"Employee {emp_id}: {details['name']}, {details['department']}")
print("Total employees:", len(employees))

# %% Project 5: Word Frequency Counter
# Difficulty: Intermediate
# Description: Count the frequency of words in a sentence using a dictionary.
# Objective: Practice dictionary creation and updating with loops.
# Tasks:
# - Take a sentence and split it into words.
# - Create a dictionary mapping words to their frequency.
# - Print the dictionary and the most frequent word.
sentence = "the cat and the dog and cat"
word_freq = {}
for word in sentence.split():
    word_freq[word] = word_freq.get(word, 0) + 1  # Increment count
most_frequent = max(word_freq, key=word_freq.get)  # Get word with max frequency
print("Word frequencies:", word_freq)
print("Most frequent word:", most_frequent)

# %% Project 6: Shopping Cart
# Difficulty: Intermediate
# Description: Simulate a shopping cart with items and quantities.
# Objective: Use dictionary methods and calculate totals.
# Tasks:
# - Create a dictionary with 3 items (item: quantity).
# - Update quantities using update().
# - Calculate the total number of items.
# - Print the cart and total.
cart = {"Laptop": 1, "Phone": 2, "Charger": 3}
cart.update({"Laptop": 2, "Charger": 5})  # Update quantities
total_items = sum(cart.values())  # Sum quantities
print("Cart:", cart)
print("Total items:", total_items)

# %% Project 7: Movie Rating System
# Difficulty: Advanced
# Description: Store movies with ratings and filter based on criteria.
# Objective: Filter and sort dictionaries.
# Tasks:
# - Create a dictionary with 5 movies (title: {genre, rating}).
# - Filter movies with rating > 8.0.
# - Sort filtered movies by rating (highest first).
# - Print filtered movies.
movies = {
    "The Shawshank Redemption": {"genre": "Drama", "rating": 9.3},
    "Inception": {"genre": "Sci-Fi", "rating": 8.8},
    "The Dark Knight": {"genre": "Action", "rating": 9.0},
    "La La Land": {"genre": "Romance", "rating": 8.0},
    "Joker": {"genre": "Thriller", "rating": 8.4}
}
high_rated = {k: v for k, v in sorted(movies.items(), key=lambda x: x[1]["rating"], reverse=True) if v["rating"] > 8.0}
print("High-rated movies:", high_rated)

# %% Project 8: Inventory Price Tracker
# Difficulty: Advanced
# Description: Track inventory with prices and discounts.
# Objective: Manipulate nested dictionaries and perform calculations.
# Tasks:
# - Create a dictionary with 3 items (item: {price, discount%}).
# - Calculate final prices after discounts.
# - Print items with final prices and total cost.
inventory = {
    "Laptop": {"price": 1000, "discount": 10},
    "Phone": {"price": 500, "discount": 5},
    "Tablet": {"price": 400, "discount": 10}
}
final_prices = {item: details["price"] * (1 - details["discount"] / 100) for item, details in inventory.items()}
total_cost = sum(final_prices.values())
print("Final prices:", final_prices)
print("Total cost:", total_cost)

# %% Project 9: Configuration Manager
# Difficulty: Advanced
# Description: Manage application settings with defaults and updates.
# Objective: Use setdefault() and deep copying.
# Tasks:
# - Create a config dictionary with 3 settings.
# - Use setdefault() to add defaults for missing keys.
# - Create a copy and update one setting.
# - Print original and updated configs.
import copy
config = {"theme": "dark", "font_size": 12, "language": "English"}
config.setdefault("notifications", "on")  # Add default
updated_config = copy.deepcopy(config)  # Deep copy
updated_config["theme"] = "light"  # Update copy
print("Original config:", config)
print("Updated config:", updated_config)

# %% Project 10: Task Manager
# Difficulty: Advanced
# Description: Manage tasks with priorities and statuses.
# Objective: Analyze and filter dictionaries.
# Tasks:
# - Create a dictionary with 4 tasks (task: {priority, status}).
# - Filter tasks with high priority (> 5).
# - Sort by priority (highest first).
# - Print high-priority tasks.
tasks = {
    "Task1": {"priority": 8, "status": "Pending"},
    "Task2": {"priority": 6, "status": "In Progress"},
    "Task3": {"priority": 3, "status": "Done"},
    "Task4": {"priority": 4, "status": "Pending"}
}
high_priority = {k: v for k, v in sorted(tasks.items(), key=lambda x: x[1]["priority"], reverse=True) if v["priority"] > 5}
print("High-priority tasks:", high_priority)