# Python List Projects
# Purpose: Apply Python List knowledge through 10 optimized projects (Basic to Advanced).
# Structure: Each project is separated by %% and includes description, tasks, and best solution.
# Note: Solutions are designed for clarity, efficiency, and beginner learning.

# %% Project 1: Grocery List Manager
# Difficulty: Basic
# Description: Build a simple program to manage a grocery shopping list.
# Objective: Practice creating lists, appending, removing, and displaying items.
# Tasks:
# - Initialize a list with 3 grocery items.
# - Append 2 new items.
# - Remove 1 item.
# - Print the final list and its length.
grocery_list = ["Milk", "Bread", "Eggs"]
grocery_list.extend(["Butter", "Sugar"])  # Efficiently add multiple items
grocery_list.remove("Bread")  # Remove specific item
print("Final grocery list:", grocery_list)
print("Length:", len(grocery_list))

# %% Project 2: Student Grades Tracker
# Difficulty: Basic
# Description: Store and manipulate a list of student grades.
# Objective: Practice indexing, updating, and sorting lists.
# Tasks:
# - Create a list of 5 grades.
# - Update the second grade to 90.
# - Sort the grades in descending order.
# - Print the sorted grades and the highest grade.
grades = [85, 92, 78, 95, 88]
grades[1] = 90  # Update second grade (index 1)
grades.sort(reverse=True)  # Sort descending
print("Sorted grades:", grades)
print("Highest grade:", grades[0])

# %% Project 3: Favorite Books List
# Difficulty: Basic
# Description: Create a list of favorite books and perform basic operations.
# Objective: Reinforce list creation, concatenation, and repetition.
# Tasks:
# - Create a list of 3 book titles.
# - Create another list with 2 more books.
# - Concatenate the two lists.
# - Repeat the concatenated list twice.
# - Print the final list.
books = ["1984", "To Kill a Mockingbird", "Pride and Prejudice"]
more_books = ["The Great Gatsby", "Moby Dick"]
combined_books = books + more_books  # Concatenate lists
repeated_books = combined_books * 2  # Repeat list
print("Repeated book list:", repeated_books)

# %% Project 4: Inventory System
# Difficulty: Intermediate
# Description: Simulate a store inventory with products and quantities.
# Objective: Use list methods like extend(), index(), and calculate totals.
# Tasks:
# - Create a list of 4 products with quantities.
# - Extend with 2 more products and quantities.
# - Find the index of "Pencil".
# - Calculate total quantity.
# - Print inventory and total quantity.
inventory = ["Pen", 10, "Notebook", 5, "Pencil", 8, "Eraser", 3]
inventory.extend(["Marker", 6, "Ruler", 4])  # Add multiple items
pencil_index = inventory.index("Pencil")  # Find index
total_quantity = sum(inventory[i] for i in range(1, len(inventory), 2))  # Sum quantities
print("Inventory:", inventory)
print("Index of Pencil:", pencil_index)
print("Total quantity:", total_quantity)

# %% Project 5: Unique Words Counter
# Difficulty: Intermediate
# Description: Analyze a sentence by extracting unique words into a list.
# Objective: Practice string-to-list conversion and removing duplicates.
# Tasks:
# - Take a sentence.
# - Split into words.
# - Create a list of unique words.
# - Print unique words and count.
sentence = "the cat and the dog and cat"
words = sentence.split()  # Split into words
unique_words = sorted(list(set(words)))  # Remove duplicates, sort for consistency
print("Unique words:", unique_words)
print("Count:", len(unique_words))

# %% Project 6: Playlist Organizer
# Difficulty: Intermediate
# Description: Manage a music playlist with song names and durations.
# Objective: Work with nested lists, sorting, and calculations.
# Tasks:
# - Create a list of 3 songs as [song, duration] pairs.
# - Sort by duration (shortest to longest).
# - Calculate total duration.
# - Print sorted playlist and total duration.
playlist = [["Bohemian Rhapsody", 360], ["Imagine", 183], ["Billie Jean", 294]]
playlist.sort(key=lambda x: x[1])  # Sort by duration
total_duration = sum(song[1] for song in playlist)  # Sum durations
print("Sorted Playlist:", playlist)
print("Total duration:", total_duration, "seconds")

# %% Project 7: Shopping Cart with Discounts
# Difficulty: Advanced
# Description: Simulate a shopping cart with products, prices, and discounts.
# Objective: Manipulate nested lists and perform calculations.
# Tasks:
# - Create a cart as [product, price, discount%].
# - Calculate final price for each product.
# - Create a new list with [product, final_price].
# - Print final prices and total cost.
cart = [["Laptop", 1000, 10], ["Phone", 500, 5]]
final_prices = [[item[0], item[1] * (1 - item[2] / 100)] for item in cart]  # Calculate discounts
total_cost = sum(price for _, price in final_prices)  # Sum final prices
print("Cart with final prices:", final_prices)
print("Total cost:", total_cost)

# %% Project 8: Movie Recommendation System
# Difficulty: Advanced
# Description: Store movies with genres and ratings, recommend based on criteria.
# Objective: Filter and sort nested lists.
# Tasks:
# - Create a list of 5 movies as [title, genre, rating].
# - Filter movies with rating > 8.0.
# - Sort filtered movies by rating (highest first).
# - Print recommended movies.
movies = [
    ["The Shawshank Redemption", "Drama", 9.3],
    ["Inception", "Sci-Fi", 8.8],
    ["The Dark Knight", "Action", 9.0],
    ["La La Land", "Romance", 8.0],
    ["Joker", "Thriller", 8.4]
]
recommended = sorted([movie for movie in movies if movie[2] > 8.0], key=lambda x: x[2], reverse=True)
print("Recommended movies:", recommended)

# %% Project 9: Data Cleaning Tool
# Difficulty: Advanced
# Description: Clean a list of data by removing duplicates and invalid entries.
# Objective: Practice advanced list manipulation and validation.
# Tasks:
# - Create a list with mixed data.
# - Remove duplicates, None, and empty strings.
# - Sort remaining data (convert to strings).
# - Print cleaned list.
mixed_data = [1, "data", None, 1, "data", "", 5, None]
cleaned = sorted(str(item) for item in set(mixed_data) if item not in (None, ""))
print("Cleaned list:", cleaned)

# %% Project 10: Task Scheduler
# Difficulty: Advanced
# Description: Simulate a task scheduler with tasks, start times, and durations.
# Objective: Analyze nested lists for scheduling and detect conflicts.
# Tasks:
# - Create a list of 4 tasks as [task, start_time, duration].
# - Sort by start time.
# - Check for overlapping tasks.
# - Print sorted schedule and overlaps.
tasks = [["Meeting", 9, 2], ["Email", 10, 1], ["Report", 12, 1], ["Call", 13, 2]]
tasks.sort(key=lambda x: x[1])  # Sort by start time
overlaps = []
for i in range(1, len(tasks)):
    if tasks[i][1] < tasks[i-1][1] + tasks[i-1][2]:  # Check overlap
        overlaps.extend([tasks[i-1][0], tasks[i][0]])
overlaps = sorted(list(set(overlaps)))  # Remove duplicates, sort
print("Sorted schedule:", tasks)
print("Overlapping tasks:", overlaps)