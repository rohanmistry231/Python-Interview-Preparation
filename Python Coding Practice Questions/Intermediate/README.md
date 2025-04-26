# Intermediate Python Coding Exercises

This file contains 34 intermediate Python coding exercises for interview preparation, covering data structures, algorithms, and Python-specific features like decorators and generators. Retail-themed examples are included where applicable. Each exercise includes a problem statement, example, and a solution hidden in a collapsible section.

## Exercise 1: Merge Two Dictionaries
**Description**: Write a function to merge two dictionaries.
**Example**:
```
Input: {"a": 1}, {"b": 2}
Output: {"a": 1, "b": 2}
```
<details>
<summary>Click to expand solution</summary>

```python
def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

print(merge_dicts({"a": 1}, {"b": 2}))  # {"a": 1, "b": 2}
```

**Explanation**: The `**` operator unpacks both dictionaries into a new dictionary, merging their key-value pairs.
</details>

## Exercise 2: Find Common Elements in Two Lists
**Description**: Write a function to find common elements between two lists.
**Example**:
```
Input: [1, 2, 3], [2, 3, 4]
Output: [2, 3]
```
<details>
<summary>Click to expand solution</summary>

```python
def find_common(lst1, lst2):
    return list(set(lst1) & set(lst2))

print(find_common([1, 2, 3], [2, 3, 4]))  # [2, 3]
```

**Explanation**: The function converts lists to sets and uses the `&` operator to find the intersection.
</details>

## Exercise 3: Remove Duplicates from a List
**Description**: Write a function to remove duplicates from a list while preserving order.
**Example**:
```
Input: [1, 2, 2, 3, 3, 4]
Output: [1, 2, 3, 4]
```
<details>
<summary>Click to expand solution</summary>

```python
def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

print(remove_duplicates([1, 2, 2, 3, 3, 4]))  # [1, 2, 3, 4]
```

**Explanation**: The function uses a set to track seen items, adding only the first occurrence to the result list.
</details>

## Exercise 4: Find First Non-Repeating Character
**Description**: Write a function to find the first non-repeating character in a string.
**Example**:
```
Input: "swiss"
Output: "w"
```
<details>
<summary>Click to expand solution</summary>

```python
def first_non_repeating_char(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    for char in s:
        if freq[char] == 1:
            return char
    return None

print(first_non_repeating_char("swiss"))  # w
```

**Explanation**: The function counts character frequencies and returns the first character with a count of 1.
</details>

## Exercise 5: Merge Two Sorted Lists
**Description**: Write a function to merge two sorted lists into a single sorted list.
**Example**:
```
Input: [1, 3, 5], [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]
```
<details>
<summary>Click to expand solution</summary>

```python
def merge_sorted_lists(lst1, lst2):
    result = []
    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1
    result.extend(lst1[i:])
    result.extend(lst2[j:])
    return result

print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]
```

**Explanation**: The function uses two pointers to compare and merge elements in sorted order.
</details>

## Exercise 6: Rotate List
**Description**: Write a function to rotate a list by `k` positions to the right.
**Example**:
```
Input: [1, 2, 3, 4, 5], k=2
Output: [4, 5, 1, 2, 3]
```
<details>
<summary>Click to expand solution</summary>

```python
def rotate_list(lst, k):
    if not lst:
        return lst
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

print(rotate_list([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]
```

**Explanation**: The function normalizes `k` using modulo, then slices the list to rotate it.
</details>

## Exercise 7: Find Second Largest Number
**Description**: Write a function to find the second largest number in a list.
**Example**:
```
Input: [5, 2, 8, 1, 9]
Output: 8
```
<details>
<summary>Click to expand solution</summary>

```python
def second_largest(numbers):
    if len(numbers) < 2:
        return None
    first = second = float('-inf')
    for num in numbers:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None

print(second_largest([5, 2, 8, 1, 9]))  # 8
```

**Explanation**: The function tracks the largest and second-largest numbers in a single pass.
</details>

## Exercise 8: Fibonacci Series
**Description**: Write a function to generate the first `n` numbers in the Fibonacci series.
**Example**:
```
Input: 6
Output: [0, 1, 1, 2, 3, 5]
```
<details>
<summary>Click to expand solution</summary>

```python
def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

print(fibonacci(6))  # [0, 1, 1, 2, 3, 5]
```

**Explanation**: The function builds the series by appending the sum of the last two numbers.
</details>

## Exercise 9: Bubble Sort
**Description**: Write a function to sort a list using the bubble sort algorithm.
**Example**:
```
Input: [5, 2, 8, 1, 9]
Output: [1, 2, 5, 8, 9]
```
<details>
<summary>Click to expand solution</summary>

```python
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

print(bubble_sort([5, 2, 8, 1, 9]))  # [1, 2, 5, 8, 9]
```

**Explanation**: The function repeatedly swaps adjacent elements if they are in the wrong order.
</details>

## Exercise 10: Binary Search
**Description**: Write a function to perform binary search on a sorted list.
**Example**:
```
Input: [1, 2, 3, 4, 5], target=3
Output: 2
```
<details>
<summary>Click to expand solution</summary>

```python
def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_search([1, 2, 3, 4, 5], 3))  # 2
```

**Explanation**: The function uses a divide-and-conquer approach to find the target in a sorted list.
</details>

## Exercise 11: Retail Order Processing
**Description**: Write a function to process retail orders, applying a discount if the total exceeds $100.
**Example**:
```
Input: [60.00, 50.00], discount_rate=0.1
Output: 99.00
```
<details>
<summary>Click to expand solution</summary>

```python
def process_order(items, discount_rate):
    total = sum(items)
    if total > 100:
        total *= (1 - discount_rate)
    return round(total, 2)

print(process_order([60.00, 50.00], 0.1))  # 99.00
```

**Explanation**: The function sums the items and applies a discount if the total exceeds $100.
</details>

## Exercise 12: Find Longest Word
**Description**: Write a function to find the longest word in a sentence.
**Example**:
```
Input: "The quick brown fox"
Output: "quick"
```
<details>
<summary>Click to expand solution</summary>

```python
def longest_word(sentence):
    return max(sentence.split(), key=len)

print(longest_word("The quick brown fox"))  # quick
```

**Explanation**: The function splits the sentence into words and uses `max()` with `key=len`.
</details>

## Exercise 13: Reverse Words in a String
**Description**: Write a function to reverse the order of words in a string.
**Example**:
```
Input: "Hello World"
Output: "World Hello"
```
<details>
<summary>Click to expand solution</summary>

```python
def reverse_words(s):
    return " ".join(s.split()[::-1])

print(reverse_words("Hello World"))  # World Hello
```

**Explanation**: The function splits the string into words, reverses the list, and joins with spaces.
</details>

## Exercise 14: Check Valid Parentheses
**Description**: Write a function to check if a string of parentheses is valid.
**Example**:
```
Input: "()"
Output: True
Input: "({)"
Output: False
```
<details>
<summary>Click to expand solution</summary>

```python
def is_valid_parentheses(s):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets:
            if not stack or stack.pop() != brackets[char]:
                return False
    return len(stack) == 0

print(is_valid_parentheses("()"))  # True
print(is_valid_parentheses("({}"))  # False
```

**Explanation**: The function uses a stack to match opening and closing brackets.
</details>

## Exercise 15: Find Factorial Iteratively
**Description**: Write a function to calculate the factorial of a number iteratively.
**Example**:
```
Input: 5
Output: 120
```
<details>
<summary>Click to expand solution</summary>

```python
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_iterative(5))  # 120
```

**Explanation**: The function multiplies numbers from 1 to `n` iteratively.
</details>

## Exercise 16: Find Missing Number in Array
**Description**: Write a function to find the missing number in an array of integers from 1 to `n`.
**Example**:
```
Input: [1, 2, 4, 5]
Output: 3
```
<details>
<summary>Click to expand solution</summary>

```python
def find_missing_number(nums):
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

print(find_missing_number([1, 2, 4, 5]))  # 3
```

**Explanation**: The function uses the sum formula to find the missing number.
</details>

## Exercise 17: Implement Stack
**Description**: Implement a stack with push, pop, and peek operations.
**Example**:
```
stack = Stack()
stack.push(1)
stack.push(2)
stack.pop()  # 2
stack.peek()  # 1
```
<details>
<summary>Click to expand solution</summary>

```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop() if self.items else None
    
    def peek(self):
        return self.items[-1] if self.items else None

stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # 2
print(stack.peek())  # 1
```

**Explanation**: The stack uses a list to store items, with `append` for push, `pop` for pop, and indexing for peek.
</details>

## Exercise 18: Implement Queue
**Description**: Implement a queue with enqueue, dequeue, and peek operations.
**Example**:
```
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.dequeue()  # 1
queue.peek()  # 2
```
<details>
<summary>Click to expand solution</summary>

```python
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0) if self.items else None
    
    def peek(self):
        return self.items[0] if self.items else None

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  # 1
print(queue.peek())  # 2
```

**Explanation**: The queue uses a list, with `append` for enqueue and `pop(0)` for dequeue.
</details>

## Exercise 19: Find Longest Common Prefix
**Description**: Write a function to find the longest common prefix among a list of strings.
**Example**:
```
Input: ["flower", "flow", "flight"]
Output: "fl"
```
<details>
<summary>Click to expand solution</summary>

```python
def longest_common_prefix(strs):
    if not strs:
        return ""
    for i, char in enumerate(strs[0]):
        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return strs[0][:i]
    return strs[0]

print(longest_common_prefix(["flower", "flow", "flight"]))  # fl
```

**Explanation**: The function compares characters of the first string with others, returning the common prefix.
</details>

## Exercise 20: Find Duplicate Number
**Description**: Write a function to find the duplicate number in an array of integers from 1 to `n`.
**Example**:
```
Input: [1, 3, 4, 2, 2]
Output: 2
```
<details>
<summary>Click to expand solution</summary>

```python
def find_duplicate(nums):
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

print(find_duplicate([1, 3, 4, 2, 2]))  # 2
```

**Explanation**: The function uses Floyd’s Tortoise and Hare algorithm to detect the duplicate.
</details>

## Exercise 21: Retail Inventory Update
**Description**: Write a function to update retail inventory based on sales.
**Example**:
```
Input: {"item1": 50, "item2": 20}, sales={"item1": 10, "item2": 5}
Output: {"item1": 40, "item2": 15}
```
<details>
<summary>Click to expand solution</summary>

```python
def update_inventory(inventory, sales):
    return {item: inventory[item] - sales.get(item, 0) for item in inventory}

print(update_inventory({"item1": 50, "item2": 20}, {"item1": 10, "item2": 5}))  # {"item1": 40, "item2": 15}
```

**Explanation**: The function subtracts sales quantities from inventory using a dictionary comprehension.
</details>

## Exercise 22: Find Majority Element
**Description**: Write a function to find the majority element (appears more than n/2 times) in an array.
**Example**:
```
Input: [2, 2, 1, 1, 1, 2, 2]
Output: 2
```
<details>
<summary>Click to expand solution</summary>

```python
def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate

print(majority_element([2, 2, 1, 1, 1, 2, 2]))  # 2
```

**Explanation**: The function uses Boyer-Moore Voting Algorithm to find the majority element.
</details>

## Exercise 23: Find All Anagrams
**Description**: Write a function to find all anagrams of a string in a list of strings.
**Example**:
```
Input: ["cat", "dog", "act", "god"], pattern="act"
Output: ["cat", "act"]
```
<details>
<summary>Click to expand solution</summary>

```python
def find_anagrams(words, pattern):
    pattern_count = {}
    for char in pattern:
        pattern_count[char] = pattern_count.get(char, 0) + 1
    return [word for word in words if len(word) == len(pattern) and pattern_count == {char: word.count(char) for char in word}]

print(find_anagrams(["cat", "dog", "act", "god"], "act"))  # ["cat", "act"]
```

**Explanation**: The function compares character counts of each word with the pattern.
</details>

## Exercise 24: Generate Subsets
**Description**: Write a function to generate all subsets of a list.
**Example**:
```
Input: [1, 2]
Output: [[], [1], [2], [1, 2]]
```
<details>
<summary>Click to expand solution</summary>

```python
def subsets(nums):
    result = [[]]
    for num in nums:
        result += [curr + [num] for curr in result]
    return result

print(subsets([1, 2]))  # [[], [1], [2], [1, 2]]
```

**Explanation**: The function iteratively builds subsets by adding each element to existing subsets.
</details>

## Exercise 25: Find Peak Element
**Description**: Write a function to find a peak element (greater than its neighbors) in an array.
**Example**:
```
Input: [1, 2, 3, 1]
Output: 2
```
<details>
<summary>Click to expand solution</summary>

```python
def find_peak_element(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left

print(find_peak_element([1, 2, 3, 1]))  # 2
```

**Explanation**: The function uses binary search to find a peak by comparing midpoints.
</details>

## Exercise 26: Implement Decorator
**Description**: Write a decorator to log function calls.
**Example**:
```
@log
def add(a, b):
    return a + b
Output: Calling add with args (2, 3)
```
<details>
<summary>Click to expand solution</summary>

```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args {args}")
        return func(*args, **kwargs)
    return wrapper

@log
def add(a, b):
    return a + b

print(add(2, 3))  # Calling add with args (2, 3)
```

**Explanation**: The decorator wraps the function to log its name and arguments before execution.
</details>

## Exercise 27: Find Longest Palindromic Substring
**Description**: Write a function to find the longest palindromic substring in a string.
**Example**:
```
Input: "babad"
Output: "bab"
```
<details>
<summary>Click to expand solution</summary>

```python
def longest_palindromic_substring(s):
    n = len(s)
    start = length = 0
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j + 1]
            if substring == substring[::-1] and j - i + 1 > length:
                start = i
                length = j - i + 1
    return s[start:start + length]

print(longest_palindromic_substring("babad"))  # bab
```

**Explanation**: The function checks all substrings to find the longest palindrome.
</details>

## Exercise 28: Find Maximum Subarray Sum
**Description**: Write a function to find the maximum sum of a contiguous subarray.
**Example**:
```
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
```
<details>
<summary>Click to expand solution</summary>

```python
def max_subarray_sum(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
```

**Explanation**: The function uses Kadane’s algorithm to track the maximum subarray sum.
</details>

## Exercise 29: Find Two Sum
**Description**: Write a function to find two numbers in a list that sum to a target.
**Example**:
```
Input: [2, 7, 11, 15], target=9
Output: [0, 1]
```
<details>
<summary>Click to expand solution</summary>

```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
```

**Explanation**: The function uses a hash map to store numbers and find the complement.
</details>

## Exercise 30: Implement Generator for Fibonacci
**Description**: Write a generator function for the Fibonacci sequence.
**Example**:
```
gen = fibonacci_generator(5)
Output: [0, 1, 1, 2, 3]
```
<details>
<summary>Click to expand solution</summary>

```python
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci_generator(5)))  # [0, 1, 1, 2, 3]
```

**Explanation**: The generator yields Fibonacci numbers one at a time, updating `a` and `b`.
</details>

## Exercise 31: Find Anagram Groups
**Description**: Write a function to group anagrams in a list of strings.
**Example**:
```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```
<details>
<summary>Click to expand solution</summary>

```python
def group_anagrams(strs):
    anagrams = {}
    for s in strs:
        sorted_s = "".join(sorted(s))
        if sorted_s not in anagrams:
            anagrams[sorted_s] = []
        anagrams[sorted_s].append(s)
    return list(anagrams.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

**Explanation**: The function groups strings by their sorted characters using a dictionary.
</details>

## Exercise 32: Find First Missing Positive
**Description**: Write a function to find the first missing positive integer in an array.
**Example**:
```
Input: [3, 4, -1, 1]
Output: 2
```
<details>
<summary>Click to expand solution</summary>

```python
def first_missing_positive(nums):
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1

print(first_missing_positive([3, 4, -1, 1]))  # 2
```

**Explanation**: The function places each number in its correct index and finds the first mismatch.
</details>

## Exercise 33: Retail Price Sorting
**Description**: Write a function to sort retail products by price in ascending order.
**Example**:
```
Input: [{"name": "item1", "price": 50}, {"name": "item2", "price": 30}]
Output: [{"name": "item2", "price": 30}, {"name": "item1", "price": 50}]
```
<details>
<summary>Click to expand solution</summary>

```python
def sort_products(products):
    return sorted(products, key=lambda x: x["price"])

print(sort_products([{"name": "item1", "price": 50}, {"name": "item2", "price": 30}]))  # [{"name": "item2", "price": 30}, {"name": "item1", "price": 50}]
```

**Explanation**: The function uses `sorted()` with a `key` function to sort by price.
</details>

## Exercise 34: Find Kth Largest Element
**Description**: Write a function to find the kth largest element in an array.
**Example**:
```
Input: [3, 2, 1, 5, 6, 4], k=2
Output: 5
```
<details>
<summary>Click to expand solution</summary>

```python
def find_kth_largest(nums, k):
    return sorted(nums, reverse=True)[k-1]

print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))  # 5
```

**Explanation**: The function sorts the array in descending order and returns the kth element.
</details>