# Python Interview Questions for AI/ML Roles

## Core Python Foundations

### Data Structures

#### Basic
1. **What are the differences between lists and tuples in Python? Provide an example of each.**  
   Lists are mutable, allowing dynamic changes (e.g., feature lists in ML), while tuples are immutable, ideal for fixed data (e.g., model parameters).  
   ```python
   lst = [1, 2, 3]  # List
   lst[0] = 4
   tup = (1, 2, 3)  # Tuple
   ```

2. **How do you create and access elements in a dictionary? Give an example.**  
   Dictionaries store key-value pairs, useful for metadata or feature mappings.  
   ```python
   data = {"feature1": 10, "feature2": 20}
   print(data["feature1"])  # Access: 10
   ```

3. **What is a set in Python, and how does it differ from a list?**  
   A set contains unique, unordered elements, unlike lists which allow duplicates and maintain order. Sets are great for extracting unique categories in datasets.  
   ```python
   s = {1, 2, 2}  # Set: {1, 2}
   lst = [1, 2, 2]  # List: [1, 2, 2]
   ```

4. **Explain strings in Python and their immutability.**  
   Strings are immutable sequences of characters, used in AI/ML for text preprocessing (e.g., tokenization). You can’t modify them in place, requiring new strings for changes.  
   ```python
   s = "hello"
   s = s + " world"  # Creates a new string
   ```

#### Intermediate
5. **How do you use set operations (union, intersection) in Python? Provide an example.**  
   Set operations like union (`|`) and intersection (`&`) compare feature sets or filter unique data.  
   ```python
   set1 = {1, 2, 3}
   set2 = {2, 3, 4}
   print(set1 | set2)  # Union: {1, 2, 3, 4}
   print(set1 & set2)  # Intersection: {2, 3}
   ```

6. **Write a function to merge two dictionaries, handling duplicate keys.**  
   Merging dictionaries unifies metadata from different sources, with later values overriding duplicates.  
   ```python
   def merge_dicts(dict1, dict2):
       return {**dict1, **dict2}
   d1 = {"a": 1}
   d2 = {"a": 2, "b": 3}
   print(merge_dicts(d1, d2))  # {'a': 2, 'b': 3}
   ```

7. **How do you convert a list to a tuple and vice versa?**  
   Conversions enable flexibility between mutable and immutable data in ML workflows.  
   ```python
   lst = [1, 2, 3]
   tup = tuple(lst)  # List to tuple
   new_lst = list(tup)  # Tuple to list
   ```

#### Advanced
8. **What are frozen sets in Python? When would you use them in AI/ML?**  
   Frozen sets are immutable sets, useful for storing unchangeable unique features (e.g., fixed categories) to ensure data integrity.  
   ```python
   fs = frozenset([1, 2, 3])
   ```

9. **Write a function to find the most frequent element in a list using a dictionary.**  
   This identifies dominant categories or features in datasets.  
   ```python
   def most_frequent(lst):
       freq = {}
       for item in lst:
           freq[item] = freq.get(item, 0) + 1
       return max(freq, key=freq.get)
   print(most_frequent([1, 2, 2, 3]))  # 2
   ```

10. **Explain how to implement a custom hashable data structure for use in sets.**  
    Custom objects need `__hash__` and `__eq__` for set inclusion, enabling unique feature storage.  
    ```python
    class Feature:
        def __init__(self, id):
            self.id = id
        def __hash__(self):
            return hash(self.id)
        def __eq__(self, other):
            return self.id == other.id
    s = {Feature(1), Feature(1)}  # Only one Feature(1)
    ```

### Control Flow

#### Basic
11. **What is the difference between `break` and `continue` in Python loops? Provide an example.**  
    `break` exits the loop entirely, while `continue` skips to the next iteration—useful for skipping invalid data in ML.  
    ```python
    for i in range(5):
        if i == 2:
            break  # Stops at 2
        print(i)  # 0, 1
    ```

12. **How do you use `if-else` statements in Python? Give an example.**  
    Filters data based on conditions, e.g., selecting valid samples.  
    ```python
    value = 10
    if value > 0:
        print("Positive")
    else:
        print("Non-positive")
    ```

13. **What is the `pass` statement, and when is it used?**  
    `pass` is a no-op placeholder, used in ML prototyping when logic is TBD.  
    ```python
    def train_model():
        pass  # To be implemented
    ```

#### Intermediate
14. **Explain the use of `elif` statements with an example.**  
    Handles multiple conditions, e.g., categorizing data points.  
    ```python
    score = 85
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    else:
        print("C")
    ```

15. **Write a loop to iterate over a list and skip even numbers using `continue`.**  
    Filters data during preprocessing, e.g., skipping outliers.  
    ```python
    numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        if num % 2 == 0:
            continue
        print(num)  # 1, 3, 5
    ```

16. **How do you use nested conditionals in Python? Provide an example.**  
    Implements complex logic for data validation in ML.  
    ```python
    value = 10
    if value > 0:
        if value < 100:
            print("Valid range")
        else:
            print("Too large")
    ```

#### Advanced
17. **Write a function using `for-else` to check if a list contains a specific value.**  
    Verifies dataset properties like missing features.  
    ```python
    def has_value(lst, target):
        for item in lst:
            if item == target:
                return True
        else:
            return False  # Runs if loop completes without break
    print(has_value([1, 2, 3], 2))  # True
    ```

18. **Implement a while loop to simulate an iterative optimization process.**  
    Mimics gradient descent in ML.  
    ```python
    error = 1.0
    step = 0
    while error > 0.01:
        error *= 0.5  # Simulated convergence
        step += 1
    print(f"Converged in {step} steps")
    ```

19. **Explain how to handle infinite loops safely in Python.**  
    Use a counter or condition to exit, preventing crashes in iterative ML training.  
    ```python
    count = 0
    while True:
        if count > 10:
            break
        count += 1
    ```

### Functions

#### Basic
20. **What are lambda functions in Python? Provide an example.**  
    Lambda functions are anonymous, single-line functions, great for quick data transformations in ML pipelines.  
    ```python
    scale = lambda x: x * 2
    print(scale(5))  # 10
    ```

21. **How do you define a function with default parameters? Give an example.**  
    Sets default hyperparameters for ML functions.  
    ```python
    def train(epochs=10):
        return f"Training for {epochs} epochs"
    print(train())  # Training for 10 epochs
    ```

22. **What are positional and keyword arguments?**  
    Positional args rely on order, while keyword args use names—flexible for model configs.  
    ```python
    def model(name, layers=2):
        print(f"{name}, {layers} layers")
    model("CNN", layers=3)  # CNN, 3 layers
    ```

#### Intermediate
23. **How do you use `*args` and `**kwargs` in Python functions? Provide an example.**  
    Handles variable inputs in ML pipelines.  
    ```python
    def process_data(*args, **kwargs):
        print(args, kwargs)
    process_data(1, 2, 3, scale=0.1)  # (1, 2, 3) {'scale': 0.1}
    ```

24. **Write a recursive function to calculate the factorial of a number.**  
    Useful in recursive algorithms like tree traversals.  
    ```python
    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n - 1)
    print(factorial(5))  # 120
    ```

25. **Explain function annotations in Python with an example.**  
    Documents inputs/outputs for clarity in ML code.  
    ```python
    def add(a: int, b: int) -> int:
        return a + b
    print(add(2, 3))  # 5
    ```

#### Advanced
26. **Write a lambda function to sort a list of dictionaries by a specific key.**  
    Sorts datasets by feature values.  
    ```python
    data = [{"id": 2}, {"id": 1}]
    sorted_data = sorted(data, key=lambda x: x["id"])
    print(sorted_data)  # [{'id': 1}, {'id': 2}]
    ```

27. **Implement a function to handle variable-length arguments for data aggregation.**  
    Aggregates multiple features for model input.  
    ```python
    def aggregate(*values):
        return sum(values)
    print(aggregate(1, 2, 3, 4))  # 10
    ```

28. **Explain how to optimize recursive functions using memoization.**  
    Caches results to speed up recursive feature computations.  
    ```python
    def memoize(func):
        cache = {}
        def wrapper(n):
            if n not in cache:
                cache[n] = func(n)
            return cache[n]
        return wrapper
    @memoize
    def fib(n):
        if n <= 1:
            return n
        return fib(n-1) + fib(n-2)
    ```

### Comprehensions

#### Basic
29. **What is a list comprehension? Provide an example.**  
    Efficiently filters or transforms data for preprocessing.  
    ```python
    squares = [x**2 for x in range(5)]
    print(squares)  # [0, 1, 4, 9, 16]
    ```

30. **How do you create a set comprehension? Give an example.**  
    Extracts unique values from datasets.  
    ```python
    uniques = {x for x in [1, 2, 2, 3]}
    print(uniques)  # {1, 2, 3}
    ```

31. **Explain dictionary comprehensions with an example.**  
    Maps features to values for quick lookups.  
    ```python
    squares_dict = {x: x**2 for x in range(3)}
    print(squares_dict)  # {0: 0, 1: 1, 2: 4}
    ```

#### Intermediate
32. **Write a list comprehension to filter numbers greater than a threshold.**  
    Filters outliers or specific data points.  
    ```python
    nums = [x for x in range(10) if x > 5]
    print(nums)  # [6, 7, 8, 9]
    ```

33. **Create a dictionary comprehension to map indices to values.**  
    Creates feature indices for model inputs.  
    ```python
    idx_map = {i: val for i, val in enumerate([10, 20, 30])}
    print(idx_map)  # {0: 10, 1: 20, 2: 30}
    ```

34. **Use a set comprehension to find unique words in a text.**  
    Preprocesses text data for NLP tasks.  
    ```python
    text = "hello hello world"
    uniques = {word for word in text.split()}
    print(uniques)  # {'hello', 'world'}
    ```

#### Advanced
35. **Explain generator expressions and their memory benefits.**  
    Generator expressions yield items one at a time, saving memory for large datasets in ML.  
    ```python
    gen = (x**2 for x in range(1000))  # No list in memory
    ```

36. **Write a nested list comprehension to create a matrix.**  
    Generates feature matrices for ML models.  
    ```python
    matrix = [[i + j for j in range(3)] for i in range(3)]
    print(matrix)  # [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
    ```

37. **Combine comprehensions with conditionals to process complex data.**  
    Filters and transforms data in one step.  
    ```python
    filtered = [x**2 for x in range(10) if x % 2 == 0]
    print(filtered)  # [0, 4, 16, 36, 64]
    ```

### Exception Handling

#### Basic
38. **How do you handle exceptions in Python using `try-except`? Provide an example.**  
    Handles errors in data loading or processing.  
    ```python
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Division by zero!")
    ```

39. **What is the `finally` block, and when is it used?**  
    Ensures cleanup (e.g., closing files) regardless of errors.  
    ```python
    try:
        x = 1 / 0
    finally:
        print("Cleanup done")
    ```

40. **Explain the `else` clause in exception handling.**  
    Runs if no exceptions occur, useful for post-processing.  
    ```python
    try:
        x = 5
    except ValueError:
        print("Error")
    else:
        print("Success")  # Success
    ```

#### Intermediate
41. **Write a function with multiple `except` blocks to handle different errors.**  
    Manages various data-related errors.  
    ```python
    def safe_div(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Zero division"
        except TypeError:
            return "Invalid type"
    print(safe_div(10, "2"))  # Invalid type
    ```

42. **How do you raise an exception in Python? Provide an example.**  
    Signals invalid data or inputs in ML.  
    ```python
    def check_positive(x):
        if x < 0:
            raise ValueError("Negative value")
        return x
    ```

43. **Handle a `KeyError` when accessing a dictionary.**  
    Manages missing keys in feature dictionaries.  
    ```python
    data = {"a": 1}
    try:
        print(data["b"])
    except KeyError:
        print("Key not found")
    ```

#### Advanced
44. **Create a custom exception class for invalid ML data.**  
    Defines specific errors for data validation.  
    ```python
    class InvalidDataError(Exception):
        pass
    def validate(data):
        if not data:
            raise InvalidDataError("Empty dataset")
    ```

45. **Write a function to retry a failed operation using exception handling.**  
    Retries failed API calls or data fetches.  
    ```python
    def retry_operation(max_attempts=3):
        for attempt in range(max_attempts):
            try:
                return 1 / 0  # Simulated failure
            except ZeroDivisionError:
                if attempt == max_attempts - 1:
                    raise
                print(f"Retry {attempt + 1}")
    ```

46. **Explain exception groups in Python and their use in AI/ML.**  
    Python 3.11+ allows grouping exceptions for complex workflows (e.g., multiple data errors), though not widely used yet in ML—typically handled individually.

### Object-Oriented Programming

#### Basic
47. **What are classes and objects in Python? Provide an example.**  
    Classes define blueprints; objects are instances—organizes reusable ML components.  
    ```python
    class Model:
        def __init__(self, name):
            self.name = name
    m = Model("Linear")  # Object
    ```

48. **How do you define methods in a class? Give an example.**  
    Implements model or preprocessing logic.  
    ```python
    class Model:
        def predict(self, x):
            return x * 2
    m = Model()
    print(m.predict(5))  # 10
    ```

49. **Explain attributes in Python classes.**  
    Attributes store data (e.g., model parameters).  
    ```python
    class Model:
        def __init__(self):
            self.weights = [1, 2]
    m = Model()
    print(m.weights)  # [1, 2]
    ```

#### Intermediate
50. **What is inheritance in Python? Provide an example.**  
    Creates specialized models from base classes.  
    ```python
    class BaseModel:
        def train(self):
            print("Training")
    class LinearModel(BaseModel):
        pass
    m = LinearModel()
    m.train()  # Training
    ```

51. **Explain encapsulation and how to implement it in Python.**  
    Protects internals using `_` or `__` prefixes.  
    ```python
    class Model:
        def __init__(self):
            self.__weights = [1, 2]  # Private
        def get_weights(self):
            return self.__weights
    ```

52. **What are static methods, and when are they used?**  
    Utility functions not tied to instances, e.g., data processing.  
    ```python
    class Utils:
        @staticmethod
        def scale(x):
            return x * 2
    print(Utils.scale(5))  # 10
    ```

#### Advanced
53. **Implement polymorphism in Python with an example.**  
    Allows flexible handling of different model types.  
    ```python
    class Model:
        def predict(self):
            pass
    class Linear(Model):
        def predict(self):
            return "Linear"
    class Tree(Model):
        def predict(self):
            return "Tree"
    for m in [Linear(), Tree()]:
        print(m.predict())
    ```

54. **Write an abstract base class for a machine learning model.**  
    Defines a template for ML implementations.  
    ```python
    from abc import ABC, abstractmethod
    class MLModel(ABC):
        @abstractmethod
        def fit(self, X, y):
            pass
        @abstractmethod
        def predict(self, X):
            pass
    ```

55. **Explain multiple inheritance and its challenges in Python.**  
    Combines features from multiple classes, but risks method resolution order (MRO) conflicts.  
    ```python
    class A:
        def method(self): return "A"
    class B:
        def method(self): return "B"
    class C(A, B):
        pass
    print(C().method())  # A (follows MRO)
    ```

### Modules and Packages

#### Basic
56. **How do you import modules in Python? Provide an example.**  
    Imports libraries like NumPy for data tasks.  
    ```python
    import numpy as np
    arr = np.array([1, 2, 3])
    ```

57. **What is the difference between a module and a package?**  
    A module is a single `.py` file; a package is a directory of modules with an `__init__.py`, organizing large ML projects.

58. **List three standard libraries and their uses in AI/ML.**  
    - `math`: Calculations (e.g., `sqrt`).  
    - `random`: Randomization (e.g., `shuffle`).  
    - `datetime`: Time handling (e.g., timestamps).

#### Intermediate
59. **How do you create a custom module in Python?**  
    Save functions in a `.py` file and import—encapsulates reusable ML code.  
    ```python
    # mymodule.py
    def process(x):
        return x * 2
    # main.py
    import mymodule
    print(mymodule.process(5))  # 10
    ```

60. **Use the `os` module to list files in a directory.**  
    Manages dataset files in a project.  
    ```python
    import os
    files = os.listdir("data/")
    print(files)
    ```

61. **Explain the `sys` module and its use in AI/ML.**  
    Handles system tasks, e.g., parsing command-line args for ML scripts.  
    ```python
    import sys
    print(sys.argv)  # Command-line arguments
    ```

#### Advanced
62. **Create a Python package for a data preprocessing pipeline.**  
    Organize preprocessing code in a package:  
    ```
    preprocessing/
    ├── __init__.py
    ├── scale.py (def scale(x): return x / 10)
    ├── filter.py (def filter_outliers(x): return [i for i in x if i < 100])
    ```
    ```python
    from preprocessing import scale, filter
    ```

63. **How do you handle module dependencies in a large ML project?**  
    Use `requirements.txt` or `pyproject.toml` with tools like `pip` or `poetry` to manage versions.

64. **Use the `time` module to measure function execution time.**  
    Benchmarks model training or preprocessing.  
    ```python
    import time
    start = time.time()
    sum(range(1000000))
    print(time.time() - start)  # Execution time
    ```

### File Handling

#### Basic
65. **How do you read a text file in Python? Provide an example.**  
    Loads raw dataset files.  
    ```python
    with open("data.txt", "r") as f:
        content = f.read()
    ```

66. **Write a function to write data to a CSV file.**  
    Saves processed data for model input.  
    ```python
    import csv
    def write_csv(data, filename):
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(data)
    write_csv([[1, 2], [3, 4]], "output.csv")
    ```

67. **Explain the `with` statement in file handling.**  
    Automatically closes files, ensuring proper resource management in data pipelines.  
    ```python
    with open("file.txt", "r") as f:
        print(f.read())
    ```

#### Intermediate
68. **How do you read and write JSON files in Python?**  
    Handles model configs or metadata.  
    ```python
    import json
    data = {"param": 1}
    with open("config.json", "w") as f:
        json.dump(data, f)
    with open("config.json", "r") as f:
        print(json.load(f))  # {"param": 1}
    ```

69. **Write a function to append data to an existing file.**  
    Logs model outputs incrementally.  
    ```python
    def append_to_file(text, filename):
        with open(filename, "a") as f:
            f.write(text + "\n")
    append_to_file("Log entry", "log.txt")
    ```

70. **Process a CSV file to extract specific columns.**  
    Selects relevant features for training.  
    ```python
    import csv
    with open("data.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        cols = [row[1] for row in reader]  # Second column
    ```

#### Advanced
71. **Handle binary files in Python for model serialization.**  
    Saves trained models (e.g., `.pkl`).  
    ```python
    import pickle
    model = {"weights": [1, 2]}
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)
    ```

72. **Write a function to parse large CSV files efficiently.**  
    Processes big datasets without loading fully into memory.  
    ```python
    import csv
    def parse_large_csv(filename):
        with open(filename, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                yield row  # Generator for line-by-line processing
    ```

73. **Explain how to handle file encoding issues in Python.**  
    Specify encoding (e.g., `utf-8`) to handle diverse datasets.  
    ```python
    with open("data.txt", "r", encoding="utf-8") as f:
        content = f.read()
    ```

### Iterators and Generators

#### Basic
74. **What is an iterator in Python? How do you create one?**  
    An iterator yields items one at a time—useful for efficient dataset iteration.  
    ```python
    lst = [1, 2, 3]
    it = iter(lst)
    print(next(it))  # 1
    ```

75. **Explain the `yield` statement in Python.**  
    `yield` creates generators, pausing execution and resuming on demand—great for lazy data loading.  
    ```python
    def gen():
        yield 1
        yield 2
    ```

76. **How do generators differ from regular functions?**  
    Generators yield values lazily, saving memory vs. returning all at once—key for large datasets.  
    ```python
    def gen():
        yield 1
    ```

#### Intermediate
77. **Write a generator function to yield even numbers up to n.**  
    Generates filtered data for processing.  
    ```python
    def even_nums(n):
        for i in range(n):
            if i % 2 == 0:
                yield i
    print(list(even_nums(6)))  # [0, 2, 4]
    ```

78. **Create an iterator for a custom data structure.**  
    Iterates over custom feature sets.  
    ```python
    class FeatureSet:
        def __init__(self, data):
            self.data = data
        def __iter__(self):
            return iter(self.data)
    fs = FeatureSet([1, 2, 3])
    for x in fs:
        print(x)
    ```

79. **Use a generator to read a large file line by line.**  
    Processes big datasets incrementally.  
    ```python
    def read_lines(filename):
        with open(filename, "r") as f:
            for line in f:
                yield line.strip()
    ```

#### Advanced
80. **Explain the benefits of generators in memory-constrained ML tasks.**  
    Generators process data one item at a time, enabling real-time model training on large datasets without loading everything into memory.

81. **Write a generator pipeline for data preprocessing.**  
    Chains transformations efficiently.  
    ```python
    def scale(gen):
        for x in gen:
            yield x * 2
    def filter_gen(gen):
        for x in gen:
            if x > 5:
                yield x
    data = scale(filter_gen([1, 3, 4, 5]))
    print(list(data))  # [8, 10]
    ```

82. **Combine iterators and generators for complex data flows.**  
    Manages multi-step processing.  
    ```python
    def gen_data():
        yield from [1, 2, 3]
    it = iter(gen_data())
    doubled = (x * 2 for x in it)
    print(list(doubled))  # [2, 4, 6]
    ```

### Decorators

#### Basic
83. **What are decorators in Python? Provide a simple example.**  
    Decorators modify function behavior, e.g., adding logging to ML functions.  
    ```python
    def log(func):
        def wrapper(*args):
            print("Calling")
            return func(*args)
        return wrapper
    @log
    def add(a, b):
        return a + b
    print(add(2, 3))  # Calling, 5
    ```

84. **How do you create a function decorator?**  
    Wrap a function with another to extend its behavior.  
    ```python
    def deco(func):
        def wrapper():
            return func().upper()
        return wrapper
    @deco
    def text():
        return "hello"
    print(text())  # HELLO
    ```

85. **Explain the purpose of class decorators.**  
    Enhance class functionality, e.g., adding methods to models.  
    ```python
    def add_method(cls):
        cls.new_method = lambda self: "New"
        return cls
    ```

#### Intermediate
86. **Write a decorator to log function execution time.**  
    Benchmarks preprocessing or training steps.  
    ```python
    import time
    def timer(func):
        def wrapper(*args):
            start = time.time()
            result = func(*args)
            print(f"Time: {time.time() - start}")
            return result
        return wrapper
    @timer
    def slow():
        time.sleep(1)
    slow()
    ```

87. **Create a decorator to retry failed function calls.**  
    Handles transient errors in data fetching.  
    ```python
    def retry(func):
        def wrapper(*args, attempts=3):
            for _ in range(attempts):
                try:
                    return func(*args)
                except Exception:
                    pass
            raise Exception("All retries failed")
        return wrapper
    ```

88. **Use a decorator to validate function inputs.**  
    Ensures valid data for ML functions.  
    ```python
    def validate(func):
        def wrapper(x):
            if x < 0:
                raise ValueError("Negative input")
            return func(x)
        return wrapper
    @validate
    def process(x):
        return x * 2
    ```

#### Advanced
89. **Write a decorator to cache function results for ML computations.**  
    Speeds up repeated calculations.  
    ```python
    def cache(func):
        memo = {}
        def wrapper(*args):
            if args not in memo:
                memo[args] = func(*args)
            return memo[args]
        return wrapper
    @cache
    def compute(x):
        return x * 2
    ```

90. **Explain how to chain multiple decorators in Python.**  
    Apply decorators from bottom to top for combined effects in ML pipelines.  
    ```python
    @timer
    @log
    def add(a, b):
        return a + b
    add(2, 3)  # Logs, then times
    ```

91. **Implement a class decorator to add functionality to an ML model.**  
    Enhances models with logging or metrics.  
    ```python
    def log_pred(cls):
        orig_predict = cls.predict
        def predict(self, x):
            print(f"Predicting {x}")
            return orig_predict(self, x)
        cls.predict = predict
        return cls
    @log_pred
    class Model:
        def predict(self, x):
            return x * 2
    ```

## Data Science Libraries

### NumPy

#### Basic
92. **What are the advantages of NumPy arrays over Python lists?**  
    NumPy arrays are faster, use less memory, and support vectorized operations—key for feature matrices in ML.

93. **How do you create a NumPy array? Provide an example.**  
    Initializes feature arrays for models.  
    ```python
    import numpy as np
    arr = np.array([1, 2, 3])
    ```

94. **Perform basic mathematical operations on NumPy arrays.**  
    Computes feature transformations.  
    ```python
    import numpy as np
    arr = np.array([1, 2, 3])
    print(arr * 2)  # [2 4 6]
    ```

#### Intermediate
95. **Explain indexing and slicing in NumPy with an example.**  
    Selects specific features or samples.  
    ```python
    import numpy as np
    arr = np.array([0, 1, 2, 3])
    print(arr[1:3])  # [1 2]
    ```

96. **How do you use NumPy for random number generation?**  
    Generates synthetic data or initializes weights.  
    ```python
    import numpy as np
    print(np.random.rand(3))  # Random array
    ```

97. **Write a function to reshape a NumPy array.**  
    Prepares data for model input shapes.  
    ```python
    import numpy as np
    def reshape_array(arr, rows, cols):
        return arr.reshape(rows, cols)
    arr = np.array([1, 2, 3, 4])
    print(reshape_array(arr, 2, 2))  # [[1 2] [3 4]]
    ```

#### Advanced
98. **Explain broadcasting in NumPy with an example.**  
    Simplifies operations on arrays of different shapes.  
    ```python
    import numpy as np
    a = np.array([1, 2, 3])
    b = 2
    print(a + b)  # [3 4 5]
    ```

99. **Perform linear algebra operations (e.g., matrix multiplication) in NumPy.**  
    Used in ML algorithms like regression.  
    ```python
    import numpy as np
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    print(np.dot(a, b))
    ```

100. **Write a function to compute the inverse of a matrix using NumPy.**  
     Solves systems in optimization problems.  
     ```python
     import numpy as np
     def matrix_inverse(matrix):
         return np.linalg.inv(matrix)
     m = np.array([[1, 2], [3, 4]])
     print(matrix_inverse(m))
     ```

### Pandas

#### Basic
101. **What is a Pandas DataFrame? How is it different from a Series?**  
     DataFrames are 2D tabular structures for datasets; Series are 1D, like single columns.  
     ```python
     import pandas as pd
     df = pd.DataFrame({"A": [1, 2]})
     s = pd.Series([1, 2])
     ```

102. **How do you read a CSV file into a Pandas DataFrame?**  
     Loads datasets for preprocessing.  
     ```python
     import pandas as pd
     df = pd.read_csv("data.csv")
     ```

103. **Filter rows in a DataFrame based on a condition.**  
     Selects relevant samples for training.  
     ```python
     import pandas as pd
     df = pd.DataFrame({"value": [1, 5, 10]})
     print(df[df["value"] > 5])  # Rows where value > 5
     ```

#### Intermediate
104. **How do you merge two DataFrames in Pandas? Provide an example.**  
     Combines datasets from multiple sources.  
     ```python
     import pandas as pd
     df1 = pd.DataFrame({"id": [1, 2], "val": [10, 20]})
     df2 = pd.DataFrame({"id": [1, 2], "cat": ["A", "B"]})
     merged = pd.merge(df1, df2, on="id")
     print(merged)
     ```

105. **Explain grouping in Pandas with an example.**  
     Aggregates data for feature engineering.  
     ```python
     import pandas as pd
     df = pd.DataFrame({"cat": ["A", "A", "B"], "val": [1, 2, 3]})
     print(df.groupby("cat").sum())
     ```

106. **Handle missing values in a DataFrame using Pandas.**  
     Cleans data for model training.  
     ```python
     import pandas as pd
     df = pd.DataFrame({"A": [1, None, 3]})
     df["A"] = df["A"].fillna(0)  # Replace NaN with 0
     ```

#### Advanced
107. **Write a function to pivot a DataFrame for analysis.**  
     Reshapes data for feature matrices.  
     ```python
     import pandas as pd
     def pivot_df(df, index, columns, values):
         return df.pivot(index=index, columns=columns, values=values)
     df = pd.DataFrame({"date": ["1", "1"], "type": ["A", "B"], "val": [10, 20]})
     print(pivot_df(df, "date", "type", "val"))
     ```

108. **Use Pandas to process time-series data.**  
     Prepares data for forecasting models.  
     ```python
     import pandas as pd
     dates = pd.date_range("2023-01-01", periods=3)
     df = pd.DataFrame({"value": [1, 2, 3]}, index=dates)
     print(df.resample("D").mean())
     ```

109. **Optimize Pandas operations for large datasets.**  
     Use `chunksize` in `read_csv`, vectorized operations, and avoid loops for efficiency.

### Matplotlib

#### Basic
110. **How do you create a line plot using Matplotlib? Provide an example.**  
     Visualizes trends in time-series data.  
     ```python
     import matplotlib.pyplot as plt
     plt.plot([1, 2, 3], [4, 5, 6])
     plt.savefig("line.png")
     ```

111. **Create a scatter plot using Matplotlib.**  
     Shows relationships between features.  
     ```python
     import matplotlib.pyplot as plt
     plt.scatter([1, 2, 3], [4, 5, 6])
     plt.savefig("scatter.png")
     ```

112. **Explain how to add labels and titles to a Matplotlib plot.**  
     Enhances interpretability.  
     ```python
     import matplotlib.pyplot as plt
     plt.plot([1, 2], [3, 4])
     plt.xlabel("X-axis")
     plt.ylabel("Y-axis")
     plt.title("Plot")
     plt.savefig("labeled.png")
     ```

#### Intermediate
113. **What are subplots in Matplotlib? Provide an example.**  
     Compares multiple metrics (e.g., training vs. validation loss).  
     ```python
     import matplotlib.pyplot as plt
     fig, (ax1, ax2) = plt.subplots(1, 2)
     ax1.plot([1, 2], [3, 4])
     ax2.plot([1, 2], [4, 3])
     plt.savefig("subplots.png")
     ```

114. **Create a histogram using Matplotlib.**  
     Analyzes feature distributions.  
     ```python
     import matplotlib.pyplot as plt
     plt.hist([1, 1, 2, 3, 3, 3])
     plt.savefig("hist.png")
     ```

115. **How do you customize plot styles in Matplotlib?**  
     Improves clarity with colors, styles, etc.  
     ```python
     import matplotlib.pyplot as plt
     plt.plot([1, 2], [3, 4], "r--", linewidth=2)
     plt.savefig("styled.png")
     ```

#### Advanced
116. **Create a bar chart to compare model performance metrics.**  
     Visualizes evaluation results.  
     ```python
     import matplotlib.pyplot as plt
     plt.bar(["Model1", "Model2"], [0.8, 0.9])
     plt.savefig("bar.png")
     ```

117. **Write a function to save Matplotlib plots to a file.**  
     Stores visualizations for documentation.  
     ```python
     import matplotlib.pyplot as plt
     def save_plot(x, y, filename):
         plt.plot(x, y)
         plt.savefig(filename)
         plt.close()
     save_plot([1, 2], [3, 4], "plot.png")
     ```

118. **Combine multiple plot types in a single Matplotlib figure.**  
     Presents complex insights.  
     ```python
     import matplotlib.pyplot as plt
     plt.plot([1, 2], [3, 4])
     plt.scatter([1.5], [3.5], color="red")
     plt.savefig("combined.png")
     ```

### Seaborn

#### Basic
119. **What is Seaborn, and how does it differ from Matplotlib?**  
     Seaborn is a high-level library built on Matplotlib, offering statistical visualizations with less code.  
     ```python
     import seaborn as sns
     ```

120. **Create a box plot using Seaborn.**  
     Analyzes feature distributions and outliers.  
     ```python
     import seaborn as sns
     import matplotlib.pyplot as plt
     sns.boxplot(x=[1, 2, 2, 3, 5])
     plt.savefig("box.png")
     ```

121. **How do you create a heatmap in Seaborn?**  
     Visualizes correlation matrices.  
     ```python
     import seaborn as sns
     import matplotlib.pyplot as plt
     sns.heatmap([[1, 0.5], [0.5, 1]])
     plt.savefig("heatmap.png")
     ```

#### Intermediate
122. **Create a pair plot using Seaborn to explore feature relationships.**  
     Identifies correlations for feature selection.  
     ```python
     import seaborn as sns
     import pandas as pd
     import matplotlib.pyplot as plt
     df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
     sns.pairplot(df)
     plt.savefig("pair.png")
     ```

123. **Use Seaborn to create a violin plot.**  
     Shows data distribution with density.  
     ```python
     import seaborn as sns
     import matplotlib.pyplot as plt
     sns.violinplot(x=[1, 1, 2, 3, 3])
     plt.savefig("violin.png")
     ```

124. **Explain how to customize Seaborn plots.**  
     Use parameters like `palette` or Matplotlib tweaks for aesthetics.  
     ```python
     import seaborn as sns
     import matplotlib.pyplot as plt
     sns.boxplot(x=[1, 2, 3], palette="Blues")
     plt.savefig("custom.png")
     ```

#### Advanced
125. **Write a function to combine Seaborn and Matplotlib for advanced visualizations.**  
     Creates complex plots for analysis.  
     ```python
     import seaborn as sns
     import matplotlib.pyplot as plt
     def combined_plot(data):
         sns.scatterplot(x=data["x"], y=data["y"])
         plt.title("Custom Plot")
         plt.savefig("combined.png")
     ```

126. **Use Seaborn to visualize regression results.**  
     Interprets model predictions.  
     ```python
     import seaborn as sns
     import matplotlib.pyplot as plt
     sns.regplot(x=[1, 2, 3], y=[2, 4, 5])
     plt.savefig("reg.png")
     ```

127. **Optimize Seaborn plots for large datasets.**  
     Subsample data or use `sns.catplot` with aggregation for performance.

### Scikit-learn

#### Basic
128. **What is Scikit-learn, and what are its main uses in AI/ML?**  
     Scikit-learn is a library for ML, offering tools for classification, regression, clustering, etc.

129. **How do you split a dataset into training and testing sets in Scikit-learn?**  
     Prepares data for evaluation.  
     ```python
     from sklearn.model_selection import train_test_split
     X, y = [1, 2, 3], [0, 1, 0]
     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
     ```

130. **Explain data preprocessing in Scikit-learn.**  
     Scales and encodes features (e.g., `StandardScaler`, `LabelEncoder`) for models.

#### Intermediate
131. **Write a function to fit a linear regression model using Scikit-learn.**  
     Trains a predictive model.  
     ```python
     from sklearn.linear_model import LinearRegression
     def fit_linear(X, y):
         model = LinearRegression()
         model.fit(X, y)
         return model
     ```

132. **How do you evaluate a model’s performance in Scikit-learn?**  
     Use metrics like accuracy or RMSE.  
     ```python
     from sklearn.metrics import accuracy_score
     y_true, y_pred = [0, 1], [0, 1]
     print(accuracy_score(y_true, y_pred))  # 1.0
     ```

133. **Use Scikit-learn to perform k-means clustering.**  
     Segments data for unsupervised learning.  
     ```python
     from sklearn.cluster import KMeans
     X = [[1, 2], [2, 3], [5, 6]]
     kmeans = KMeans(n_clusters=2).fit(X)
     print(kmeans.labels_)
     ```

#### Advanced
134. **Implement a pipeline in Scikit-learn for preprocessing and modeling.**  
     Streamlines workflows.  
     ```python
     from sklearn.pipeline import Pipeline
     from sklearn.preprocessing import StandardScaler
     from sklearn.linear_model import LinearRegression
     pipeline = Pipeline([("scaler", StandardScaler()), ("model", LinearRegression())])
     ```

135. **Explain hyperparameter tuning in Scikit-learn with GridSearchCV.**  
     Optimizes model performance by testing parameter combinations.  
     ```python
     from sklearn.model_selection import GridSearchCV
     from sklearn.svm import SVC
     param_grid = {"C": [1, 10]}
     grid = GridSearchCV(SVC(), param_grid)
     ```

136. **Write a function to implement a random forest classifier.**  
     Builds robust classification models.  
     ```python
     from sklearn.ensemble import RandomForestClassifier
     def fit_rf(X, y):
         rf = RandomForestClassifier()
         rf.fit(X, y)
         return rf
     ```

### Collections

#### Basic
137. **What is the Counter class in the collections module? Provide an example.**  
     Counts feature frequencies for analysis.  
     ```python
     from collections import Counter
     c = Counter([1, 1, 2])
     print(c)  # Counter({1: 2, 2: 1})
     ```

138. **How do you use `defaultdict` in Python?**  
     Simplifies handling missing keys in aggregation.  
     ```python
     from collections import defaultdict
     d = defaultdict(int)
     d["key"] += 1
     print(d["key"])  # 1
     ```

139. **Explain `namedtuple` and its use cases.**  
     Structures data for clarity in ML code.  
     ```python
     from collections import namedtuple
     Point = namedtuple("Point", ["x", "y"])
     p = Point(1, 2)
     print(p.x)  # 1
     ```

#### Intermediate
140. **Use `OrderedDict` to maintain insertion order in a dictionary.**  
     Preserves feature order for consistency.  
     ```python
     from collections import OrderedDict
     od = OrderedDict([("a", 1), ("b", 2)])
     print(od)  # OrderedDict([('a', 1), ('b', 2)])
     ```

141. **Write a function using Counter to find the most common elements.**  
     Identifies dominant categories.  
     ```python
     from collections import Counter
     def most_common(lst):
         return Counter(lst).most_common(1)[0][0]
     print(most_common([1, 1, 2]))  # 1
     ```

142. **Combine `defaultdict` and `Counter` for data processing.**  
     Aggregates and counts efficiently.  
     ```python
     from collections import defaultdict, Counter
     d = defaultdict(Counter)
     d["group"]["item"] += 1
     print(d)  # defaultdict(<class 'Counter'>, {'group': Counter({'item': 1})})
     ```

#### Advanced
143. **Use `deque` for efficient queue operations in Python.**  
     Manages sliding windows in time-series data.  
     ```python
     from collections import deque
     d = deque([1, 2, 3], maxlen=2)
     d.append(4)
     print(d)  # deque([3, 4], maxlen=2)
     ```

144. **Explain how collections improve performance in ML tasks.**  
     Specialized structures like `Counter` and `deque` optimize counting and queue operations over basic types.

145. **Write a function to process large datasets using `deque`.**  
     Handles streaming data efficiently.  
     ```python
     from collections import deque
     def sliding_window(data, size):
         d = deque(maxlen=size)
         for item in data:
             d.append(item)
             if len(d) == size:
                 yield list(d)
     ```

### Itertools

#### Basic
146. **What are `combinations` and `permutations` in itertools? Provide an example.**  
     Generates feature combinations for analysis.  
     ```python
     from itertools import combinations, permutations
     print(list(combinations([1, 2, 3], 2)))  # [(1, 2), (1, 3), (2, 3)]
     print(list(permutations([1, 2], 2)))  # [(1, 2), (2, 1)]
     ```

147. **How do you use the `chain` function in itertools?**  
     Concatenates datasets for processing.  
     ```python
     from itertools import chain
     print(list(chain([1, 2], [3, 4])))  # [1, 2, 3, 4]
     ```

148. **Explain the `product` function in itertools.**  
     Creates Cartesian products for parameter testing.  
     ```python
     from itertools import product
     print(list(product([1, 2], [3])))  # [(1, 3), (2, 3)]
     ```

#### Intermediate
149. **Write a function using `combinations` to generate feature pairs.**  
     Explores feature interactions for modeling.  
     ```python
     from itertools import combinations
     def feature_pairs(features):
         return list(combinations(features, 2))
     print(feature_pairs(["A", "B", "C"]))  # [('A', 'B'), ('A', 'C'), ('B', 'C')]
     ```

150. **Use `itertools` to iterate over multiple lists simultaneously.**  
     Combines data sources for analysis.  
     ```python
     from itertools import zip_longest
     print(list(zip_longest([1, 2], [3])))  # [(1, 3), (2, None)]
     ```

151. **Create a function using `product` for hyperparameter tuning.**  
     Tests parameter combinations efficiently.  
     ```python
     from itertools import product
     def param_grid(params):
         return list(product(*params.values()))
     print(param_grid({"C": [1, 10], "kernel": ["linear"]}))
     ```

#### Advanced
152. **Combine `itertools` functions for complex data transformations.**  
     Builds advanced feature engineering pipelines.  
     ```python
     from itertools import chain, combinations
     data = chain(combinations([1, 2, 3], 2))
     print(list(data))  # [(1, 2), (1, 3), (2, 3)]
     ```

153. **Explain how `itertools` optimizes memory usage in ML.**  
     Functions like `product` generate items lazily, reducing memory needs for large datasets.

154. **Write a function to generate all possible feature subsets using `itertools`.**  
     Supports feature selection in ML.  
     ```python
     from itertools import chain, combinations
     def subsets(features):
         return chain.from_iterable(combinations(features, r) for r in range(len(features) + 1))
     print(list(subsets([1, 2])))  # [(), (1,), (2,), (1, 2)]
     ```

### Functools

#### Basic
155. **What is the `partial` function in functools? Provide an example.**  
     Fixes arguments for reusable ML functions.  
     ```python
     from functools import partial
     def scale(x, factor): return x * factor
     double = partial(scale, factor=2)
     print(double(5))  # 10
     ```

156. **How do you use the `reduce` function in Python?**  
     Aggregates data (e.g., summing features).  
     ```python
     from functools import reduce
     print(reduce(lambda x, y: x + y, [1, 2, 3]))  # 6
     ```

157. **Explain the `lru_cache` decorator in functools.**  
     Caches results for faster computations.  
     ```python
     from functools import lru_cache
     @lru_cache
     def expensive(x):
         return x * 2
     ```

#### Intermediate
158. **Write a function using `partial` to create a specialized ML function.**  
     Simplifies model configuration.  
     ```python
     from functools import partial
     def predict(model, x, scale):
         return model(x) * scale
     linear = partial(predict, lambda x: x, scale=2)
     print(linear(5))  # 10
     ```

159. **Use `reduce` to compute a cumulative product of a list.**  
     Aggregates feature values.  
     ```python
     from functools import reduce
     print(reduce(lambda x, y: x * y, [1, 2, 3]))  # 6
     ```

160. **Apply `lru_cache` to a recursive function for optimization.**  
     Speeds up recursive ML algorithms.  
     ```python
     from functools import lru_cache
     @lru_cache
     def fib(n):
         if n <= 1:
             return n
         return fib(n-1) + fib(n-2)
     ```

#### Advanced
161. **Combine `functools` and `itertools` for advanced data processing.**  
     Builds efficient pipelines.  
     ```python
     from functools import reduce
     from itertools import product
     params = list(product([1, 2], [3]))
     print(reduce(lambda x, y: x + y[0], params, 0))  # Sum of first elements
     ```

162. **Write a function using `partial` for dynamic model evaluation.**  
     Adapts evaluation metrics dynamically.  
     ```python
     from functools import partial
     def evaluate(metric, y_true, y_pred):
         return metric(y_true, y_pred)
     accuracy = partial(evaluate, lambda x, y: sum(a == b for a, b in zip(x, y)) / len(x))
     ```

163. **Explain how `lru_cache` improves performance in ML experiments.**  
     Reduces computation time for repeated expensive calls, like hyperparameter testing.

## Additional Coding Questions

164. **Write a function to replace spaces in a string with underscores.**  
    Preprocesses text data for NLP tasks.  
    ```python
    def replace_spaces(text):
        return text.replace(" ", "_")
    print(replace_spaces("hello world"))  # hello_world
    ```

165. **Implement a function to check if a number is a perfect square.**  
    Validates numerical data properties.  
    ```python
    def is_perfect_square(n):
        root = int(n ** 0.5)
        return root * root == n
    print(is_perfect_square(16))  # True
    ```

166. **Write a function to find the first recurring character in a string.**  
    Analyzes text patterns for feature extraction.  
    ```python
    def first_recurring(s):
        seen = set()
        for char in s:
            if char in seen:
                return char
            seen.add(char)
        return None
    print(first_recurring("hello"))  # l
    ```

167. **Create a function to compute the maximum stock profit from a price list.**  
    Applies to financial time-series analysis.  
    ```python
    def max_profit(prices):
        min_price, max_profit = float("inf"), 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
    print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
    ```

168. **Implement K-means clustering from scratch using NumPy.**  
    Demonstrates ML algorithm understanding.  
    ```python
    import numpy as np
    def kmeans(X, k, max_iters=100):
        centroids = X[np.random.choice(len(X), k, replace=False)]
        for _ in range(max_iters):
            labels = np.argmin(np.linalg.norm(X[:, np.newaxis] - centroids, axis=2), axis=1)
            new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])
            if np.all(centroids == new_centroids):
                break
            centroids = new_centroids
        return labels, centroids
    X = np.array([[1, 2], [2, 3], [5, 6]])
    print(kmeans(X, 2))
    ```

169. **Write a function to generate bigrams from a sentence.**  
    Creates features for NLP models.  
    ```python
    def bigrams(sentence):
        words = sentence.split()
        return list(zip(words, words[1:]))
    print(bigrams("this is a test"))  # [('this', 'is'), ('is', 'a'), ('a', 'test')]
    ```

170. **Compute the standard deviation of a dataset using NumPy.**  
    Analyzes data variability for preprocessing.  
    ```python
    import numpy as np
    def std_dev(data):
        return np.std(data)
    print(std_dev([1, 2, 3, 4, 5]))  # ~1.414
    ```