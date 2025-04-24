# Python String Projects
# Purpose: Apply Python String knowledge through 10 optimized projects (Basic to Advanced).
# Structure: Each project is separated by %% and includes description, tasks, and best solution.
# Note: Solutions are designed for clarity, efficiency, and beginner learning.

# %% Project 1: Product Name Formatter
# Difficulty: Basic
# Description: Format a product name for display.
# Objective: Practice string methods and slicing.
# Tasks:
# - Create a string for a product name.
# - Convert to uppercase and slice the first 5 characters.
# - Check if a substring is present.
# - Print the results.
product_name = "Smartphone X"
upper_name = product_name.upper()
first_five = product_name[:5]
has_phone = "phone" in product_name.lower()
print("Uppercase:", upper_name)
print("First 5 chars:", first_five)
print("Is 'phone' in name?:", has_phone)

# %% Project 2: Category Concatenator
# Difficulty: Basic
# Description: Combine product categories into a single string.
# Objective: Practice concatenation and repetition.
# Tasks:
# - Create two strings for categories.
# - Concatenate them with a separator.
# - Repeat the result twice.
# - Print the concatenated and repeated strings.
cat1 = "Electronics"
cat2 = "Appliances"
combined = cat1 + " | " + cat2
repeated = combined * 2
print("Concatenated:", combined)
print("Repeated:", repeated)

# %% Project 3: Order Description Generator
# Difficulty: Basic
# Description: Generate a description for an order using string formatting.
# Objective: Practice f-strings.
# Tasks:
# - Create a string for a product and a price.
# - Format a description using an f-string.
# - Print the description.
product = "Laptop"
price = 999.99
description = f"Order: {product}, Price: ${price:.2f}"
print(description)

# %% Project 4: Text Cleaner
# Difficulty: Intermediate
# Description: Clean a messy string for processing.
# Objective: Use strip(), replace(), and lower().
# Tasks:
# - Create a string with extra spaces and mixed case.
# - Strip spaces, convert to lowercase, and replace a word.
# - Print the cleaned string.
messy_text = "  LAPTOP Pro  "
cleaned = messy_text.strip().lower().replace("pro", "elite")
print("Cleaned:", cleaned)

# %% Project 5: Word Splitter
# Difficulty: Intermediate
# Description: Split a sentence into words and process them.
# Objective: Use split() and join().
# Tasks:
# - Create a sentence string.
# - Split into words and convert each to title case.
# - Join back into a string.
# - Print the result.
sentence = "the quick brown fox"
words = sentence.split()
title_words = [word.title() for word in words]
title_sentence = " ".join(title_words)
print("Title case:", title_sentence)

# %% Project 6: Tag Extractor
# Difficulty: Intermediate
# Description: Extract and format tags from a string.
# Objective: Use split(), strip(), and join().
# Tasks:
# - Create a string of comma-separated tags with extra spaces.
# - Split into tags, strip spaces, and convert to lowercase.
# - Join into a clean string with a different separator.
# - Print the result.
tags = " Python , Coding ,  Tech "
clean_tags = [tag.strip().lower() for tag in tags.split(",")]
formatted_tags = "|".join(clean_tags)
print("Clean tags:", formatted_tags)

# %% Project 7: Email Formatter
# Difficulty: Advanced
# Description: Format user names into email addresses.
# Objective: Use string methods and formatting.
# Tasks:
# - Create a string with a full name.
# - Extract first and last names, convert to lowercase, and format as an email.
# - Print the email address.
full_name = "John Doe"
first, last = full_name.split()
email = f"{first.lower()}.{last.lower()}@example.com"
print("Email:", email)

# %% Project 8: Log Parser
# Difficulty: Advanced
# Description: Parse a log entry to extract key information.
# Objective: Use split(), strip(), and indexing.
# Tasks:
# - Create a log string with timestamp and message.
# - Split and extract the timestamp and message.
# - Print both parts.
log = "2023-10-01 10:00 | User logged in"
timestamp, message = [part.strip() for part in log.split("|")]
print("Timestamp:", timestamp)
print("Message:", message)

# %% Project 9: URL Builder
# Difficulty: Advanced
# Description: Build a URL from components.
# Objective: Use join() and string formatting.
# Tasks:
# - Create strings for protocol, domain, and path.
# - Combine using join() and add query parameters with f-strings.
# - Print the full URL.
protocol = "https"
domain = "example.com"
path = "api"
user = "john"
url = f"{protocol}://{domain}/{path}?user={user}"
print("URL:", url)

# %% Project 10: Text Analyzer
# Difficulty: Advanced
# Description: Analyze a text for word count and unique words.
# Objective: Use split(), sets, and string methods.
# Tasks:
# - Create a sentence string.
# - Split into words, count total words, and find unique words using a set.
# - Print the word count and unique words.
text = "the cat and the dog and cat"
words = text.split()
word_count = len(words)
unique_words = set(words)
print("Word count:", word_count)
print("Unique words:", unique_words)