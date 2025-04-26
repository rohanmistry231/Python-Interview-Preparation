# Advanced Python Coding Exercises

This file contains 34 advanced Python coding exercises for interview preparation, covering complex algorithms, data structures, and advanced Python features like metaclasses and multiprocessing. Retail-themed examples are included where applicable. Each exercise includes a problem statement, example, and a solution hidden in a collapsible section.

## Exercise 1: Longest Substring Without Repeating Characters
**Description**: Write a function to find the length of the longest substring without repeating characters.
**Example**:
```
Input: "abcabcbb"
Output: 3
```
<details>
<summary>Click to expand solution</summary>

```python
def length_of_longest_substring(s):
    char_set = set()
    left = max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length

print(length_of_longest_substring("abcabcbb"))  # 3
```

**Explanation**: The function uses a sliding window with a set to track unique characters.
</details>

## Exercise 2: Merge Intervals
**Description**: Write a function to merge all overlapping intervals in a list of intervals.
**Example**:
```
Input: [[1,3], [2,6], [8,10], [15,18]]
Output: [[1,6], [8,10], [15,18]]
```
<details>
<summary>Click to expand solution</summary>

```python
def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    return merged

print(merge_intervals([[1,3], [2,6], [8,10], [15,18]]))  # [[1,6], [8,10], [15,18]]
```

**Explanation**: The function sorts intervals by start time and merges overlapping ones.
</details>

## Exercise 3: Implement LRU Cache
**Description**: Implement a Least Recently Used (LRU) cache with `get` and `put` operations.
**Example**:
```
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)  # 1
cache.put(3, 3)  # evicts key 2
cache.get(2)  # -1
```
<details>
<summary>Click to expand solution</summary>

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key):
        if key not in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value

cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # 1
cache.put(3, 3)
print(cache.get(2))  # -1
```

**Explanation**: The class uses an `OrderedDict` to maintain order and manage cache eviction.
</details>

## Exercise 4: Metaclass for Singleton
**Description**: Write a metaclass that enforces a singleton pattern for a class.
**Example**:
```
obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)  # True
```
<details>
<summary>Click to expand solution</summary>

```python
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self.value = None

obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)  # True
```

**Explanation**: The metaclass ensures only one instance of the class is created.
</details>

## Exercise 5: Multiprocessing Example
**Description**: Write a function to parallelize a task using the `multiprocessing` module.
**Example**:
```
Input: [1, 2, 3, 4]
Output: [1, 4, 9, 16]
```
<details>
<summary>Click to expand solution</summary>

```python
from multiprocessing import Pool

def square(n):
    return n * n

def parallel_square(numbers):
    with Pool() as pool:
        results = pool.map(square, numbers)
    return results

print(parallel_square([1, 2, 3, 4]))  # [1, 4, 9, 16]
```

**Explanation**: The function uses `Pool` to parallelize the `square` function across multiple processes.
</details>

## Exercise 6: Find Median of Two Sorted Arrays
**Description**: Write a function to find the median of two sorted arrays.
**Example**:
```
Input: [1, 3], [2]
Output: 2.0
```
<details>
<summary>Click to expand solution</summary>

```python
def find_median_sorted_arrays(nums1, nums2):
    merged = sorted(nums1 + nums2)
    n = len(merged)
    if n % 2 == 0:
        return (merged[n//2 - 1] + merged[n//2]) / 2
    return float(merged[n//2])

print(find_median_sorted_arrays([1, 3], [2]))  # 2.0
```

**Explanation**: The function merges and sorts the arrays, then computes the median based on length parity.
</details>

## Exercise 7: Implement Trie
**Description**: Implement a trie (prefix tree) with insert and search operations.
**Example**:
```
trie = Trie()
trie.insert("apple")
trie.search("apple")  # True
trie.search("app")  # False
```
<details>
<summary>Click to expand solution</summary>

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  # True
print(trie.search("app"))  # False
```

**Explanation**: The trie uses nodes to store characters, with `is_end` marking word boundaries.
</details>

## Exercise 8: Word Ladder
**Description**: Write a function to find the shortest transformation sequence from beginWord to endWord.
**Example**:
```
Input: beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]
Output: ["hit", "hot", "dot", "dog", "cog"]
```
<details>
<summary>Click to expand solution</summary>

```python
from collections import deque

def word_ladder(beginWord, endWord, wordList):
    word_set = set(wordList)
    if endWord not in word_set:
        return []
    queue = deque([(beginWord, [beginWord])])
    while queue:
        word, path = queue.popleft()
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                new_word = word[:i] + c + word[i+1:]
                if new_word in word_set:
                    if new_word == endWord:
                        return path + [new_word]
                    word_set.remove(new_word)
                    queue.append((new_word, path + [new_word]))
    return []

print(word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # ["hit", "hot", "dot", "dog", "cog"]
```

**Explanation**: The function uses BFS to find the shortest transformation path.
</details>

## Exercise 9: Longest Valid Parentheses
**Description**: Write a function to find the length of the longest valid parentheses substring.
**Example**:
```
Input: "(()"
Output: 2
```
<details>
<summary>Click to expand solution</summary>

```python
def longest_valid_parentheses(s):
    stack = [-1]
    max_length = 0
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])
    return max_length

print(longest_valid_parentheses("(()"))  # 2
```

**Explanation**: The function uses a stack to track indices of parentheses and calculate valid lengths.
</details>

## Exercise 10: Minimum Window Substring
**Description**: Write a function to find the minimum window substring containing all characters of a pattern.
**Example**:
```
Input: s="ADOBECODEBANC", t="ABC"
Output: "BANC"
```
<details>
<summary>Click to expand solution</summary>

```python
from collections import Counter

def min_window(s, t):
    if not s or not t:
        return ""
    t_count = Counter(t)
    required = len(t_count)
    formed = 0
    window_counts = {}
    left = right = 0
    min_len = float('inf')
    min_window_sub = ""
    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        if char in t_count and window_counts[char] == t_count[char]:
            formed += 1
        while left <= right and formed == required:
            char = s[left]
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window_sub = s[left:right + 1]
            window_counts[char] -= 1
            if char in t_count and window_counts[char] < t_count[char]:
                formed -= 1
            left += 1
        right += 1
    return min_window_sub

print(min_window("ADOBECODEBANC", "ABC"))  # BANC
```

**Explanation**: The function uses a sliding window to find the smallest substring containing all characters of `t`.
</details>

## Exercise 11: Regular Expression Matching
**Description**: Write a function to implement regular expression matching with `.` and `*`.
**Example**:
```
Input: s="aa", p="a*"
Output: True
```
<details>
<summary>Click to expand solution</summary>

```python
def is_match(s, p):
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True
    for j in range(1, len(p) + 1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j-1] == '*':
                dp[i][j] = dp[i][j-2] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
            elif p[j-1] == '.' or s[i-1] == p[j-1]:
                dp[i][j] = dp[i-1][j-1]
    return dp[len(s)][len(p)]

print(is_match("aa", "a*"))  # True
```

**Explanation**: The function uses dynamic programming to match the string against the pattern.
</details>

## Exercise 12: Find All Permutations
**Description**: Write a function to find all permutations of a list.
**Example**:
```
Input: [1, 2, 3]
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```
<details>
<summary>Click to expand solution</summary>

```python
def permute(nums):
    if len(nums) <= 1:
        return [nums]
    result = []
    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)
        for perm in perms:
            perm.append(n)
        result.extend(perms)
        nums.append(n)
    return result

print(permute([1, 2, 3]))  # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

**Explanation**: The function recursively generates permutations by fixing each element.
</details>

## Exercise 13: Find Combination Sum
**Description**: Write a function to find all combinations of numbers that sum to a target.
**Example**:
```
Input: candidates=[2, 3, 6, 7], target=7
Output: [[7], [2, 2, 3]]
```
<details>
<summary>Click to expand solution</summary>

```python
def combination_sum(candidates, target):
    result = []
    def backtrack(remain, comb, start):
        if remain == 0:
            result.append(comb[:])
            return
        if remain < 0:
            return
        for i in range(start, len(candidates)):
            comb.append(candidates[i])
            backtrack(remain - candidates[i], comb, i)
            comb.pop()
    backtrack(target, [], 0)
    return result

print(combination_sum([2, 3, 6, 7], 7))  # [[7], [2, 2, 3]]
```

**Explanation**: The function uses backtracking to find all valid combinations.
</details>

## Exercise 14: Implement Graph BFS
**Description**: Write a function to perform breadth-first search on a graph.
**Example**:
```
Input: graph={0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}, start=2
Output: [2, 0, 3, 1]
```
<details>
<summary>Click to expand solution</summary>

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result

print(bfs({0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}, 2))  # [2, 0, 3, 1]
```

**Explanation**: The function uses a queue to explore nodes level by level.
</details>

## Exercise 15: Implement Graph DFS
**Description**: Write a function to perform depth-first search on a graph.
**Example**:
```
Input: graph={0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}, start=2
Output: [2, 0, 1, 3]
```
<details>
<summary>Click to expand solution</summary>

```python
def dfs(graph, start):
    visited = set()
    result = []
    def dfs_util(vertex):
        visited.add(vertex)
        result.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs_util(neighbor)
    dfs_util(start)
    return result

print(dfs({0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}, 2))  # [2, 0, 1, 3]
```

**Explanation**: The function uses recursion to explore as far as possible along each branch.
</details>

## Exercise 16: Find Shortest Path (Dijkstra’s)
**Description**: Write a function to find the shortest path in a weighted graph using Dijkstra’s algorithm.
**Example**:
```
Input: graph={0: {1: 4, 2: 8}, 1: {2: 2, 3: 5}, 2: {3: 5}, 3: {}}, start=0
Output: {0: 0, 1: 4, 2: 6, 3: 9}
```
<details>
<summary>Click to expand solution</summary>

```python
from heapq import heappush, heappop

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_dist, current_vertex = heappop(pq)
        if current_dist > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heappush(pq, (distance, neighbor))
    return distances

print(dijkstra({0: {1: 4, 2: 8}, 1: {2: 2, 3: 5}, 2: {3: 5}, 3: {}}, 0))  # {0: 0, 1: 4, 2: 6, 3: 9}
```

**Explanation**: The function uses a priority queue to find the shortest paths from the start vertex.
</details>

## Exercise 17: Longest Increasing Subsequence
**Description**: Write a function to find the length of the longest increasing subsequence.
**Example**:
```
Input: [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
```
<details>
<summary>Click to expand solution</summary>

```python
def length_of_lis(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
```

**Explanation**: The function uses dynamic programming to track the longest increasing subsequence ending at each index.
</details>

## Exercise 18: Edit Distance
**Description**: Write a function to find the minimum number of operations to transform one string into another.
**Example**:
```
Input: word1="horse", word2="ros"
Output: 3
```
<details>
<summary>Click to expand solution</summary>

```python
def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    return dp[m][n]

print(edit_distance("horse", "ros"))  # 3
```

**Explanation**: The function uses dynamic programming to compute the minimum edit operations.
</details>

## Exercise 19: Find Maximum Profit (Stock Prices)
**Description**: Write a function to find the maximum profit from buying and selling a stock once.
**Example**:
```
Input: [7, 1, 5, 3, 6, 4]
Output: 5
```
<details>
<summary>Click to expand solution</summary>

```python
def max_profit(prices):
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    return max_profit

print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
```

**Explanation**: The function tracks the minimum price and computes the maximum profit possible.
</details>

## Exercise 20: Knapsack Problem
**Description**: Write a function to solve the 0/1 knapsack problem given weights, values, and capacity.
**Example**:
```
Input: values=[60, 100, 120], weights=[10, 20, 30], capacity=50
Output: 220
```
<details>
<summary>Click to expand solution</summary>

```python
def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]

print(knapsack([60, 100, 120], [10, 20, 30], 50))  # 220
```

**Explanation**: The function uses dynamic programming to maximize the value within the weight capacity.
</details>

## Exercise 21: Find All Subsets with Sum
**Description**: Write a function to find all subsets of a list that sum to a target.
**Example**:
```
Input: nums=[1, 2, 3], target=5
Output: [[2, 3]]
```
<details>
<summary>Click to expand solution</summary>

```python
def find_subsets_with_sum(nums, target):
    result = []
    def backtrack(index, current_sum, subset):
        if current_sum == target:
            result.append(subset[:])
            return
        if current_sum > target or index >= len(nums):
            return
        subset.append(nums[index])
        backtrack(index + 1, current_sum + nums[index], subset)
        subset.pop()
        backtrack(index + 1, current_sum, subset)
    backtrack(0, 0, [])
    return result

print(find_subsets_with_sum([1, 2, 3], 5))  # [[2, 3]]
```

**Explanation**: The function uses backtracking to find all subsets summing to the target.
</details>

## Exercise 22: Implement Context Manager
**Description**: Write a custom context manager to measure execution time of a block.
**Example**:
```
with Timer():
    sum(range(1000000))
Output: Execution time: ~0.02 seconds
```
<details>
<summary>Click to expand solution</summary>

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, *args):
        self.end = time.time()
        print(f"Execution time: {self.end - self.start:.2f} seconds")

with Timer():
    sum(range(1000000))
```

**Explanation**: The context manager records the start and end times, printing the difference.
</details>

## Exercise 23: Implement Coroutine
**Description**: Write a coroutine to process data incrementally.
**Example**:
```
coro = accumulator()
coro.send(1)  # 1
coro.send(2)  # 3
```
<details>
<summary>Click to expand solution</summary>

```python
def accumulator():
    total = 0
    while True:
        value = yield total
        total += value

coro = accumulator()
next(coro)
print(coro.send(1))  # 1
print(coro.send(2))  # 3
```

**Explanation**: The coroutine maintains a running sum, yielding the current total after each input.
</details>

## Exercise 24: Find Cycle in Graph
**Description**: Write a function to detect a cycle in a directed graph.
**Example**:
```
Input: graph={0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
Output: True
```
<details>
<summary>Click to expand solution</summary>

```python
def has_cycle(graph):
    visited = set()
    rec_stack = set()
    def dfs(vertex):
        visited.add(vertex)
        rec_stack.add(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        rec_stack.remove(vertex)
        return False
    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex):
                return True
    return False

print(has_cycle({0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}))  # True
```

**Explanation**: The function uses DFS with a recursion stack to detect cycles.
</details>

## Exercise 25: Retail Order Scheduling
**Description**: Write a function to schedule retail orders based on priority and time.
**Example**:
```
Input: orders=[{"id": 1, "priority": 2, "time": 10}, {"id": 2, "priority": 1, "time": 5}]
Output: [2, 1]
```
<details>
<summary>Click to expand solution</summary>

```python
def schedule_orders(orders):
    return [order["id"] for order in sorted(orders, key=lambda x: (x["priority"], x["time"]))]

print(schedule_orders([{"id": 1, "priority": 2, "time": 10}, {"id": 2, "priority": 1, "time": 5}]))  # [2, 1]
```

**Explanation**: The function sorts orders by priority (ascending) and then by time.
</details>

## Exercise 26: Word Break
**Description**: Write a function to check if a string can be segmented into words from a dictionary.
**Example**:
```
Input: s="leetcode", wordDict=["leet", "code"]
Output: True
```
<details>
<summary>Click to expand solution</summary>

```python
def word_break(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for word in wordDict:
            if i >= len(word) and dp[i - len(word)]:
                if s[i - len(word):i] == word:
                    dp[i] = True
                    break
    return dp[len(s)]

print(word_break("leetcode", ["leet", "code"]))  # True
```

**Explanation**: The function uses dynamic programming to check if the string can be segmented.
</details>

## Exercise 27: Maximum Product Subarray
**Description**: Write a function to find the maximum product of a contiguous subarray.
**Example**:
```
Input: [2, 3, -2, 4]
Output: 6
```
<details>
<summary>Click to expand solution</summary>

```python
def max_product(nums):
    max_so_far = min_so_far = result = nums[0]
    for num in nums[1:]:
        temp_max = max(num, max_so_far * num, min_so_far * num)
        min_so_far = min(num, max_so_far * num, min_so_far * num)
        max_so_far = temp_max
        result = max(result, max_so_far)
    return result

print(max_product([2, 3, -2, 4]))  # 6
```

**Explanation**: The function tracks maximum and minimum products to handle negative numbers.
</details>

## Exercise 28: Find K Closest Points
**Description**: Write a function to find the k closest points to the origin.
**Example**:
```
Input: points=[[1,3], [-2,2]], k=1
Output: [[-2,2]]
```
<details>
<summary>Click to expand solution</summary>

```python
from heapq import heappush, heappop

def k_closest(points, k):
    heap = []
    for x, y in points:
        dist = -(x*x + y*y)
        heappush(heap, (dist, x, y))
        if len(heap) > k:
            heappop(heap)
    return [[x, y] for _, x, y in heap]

print(k_closest([[1,3], [-2,2]], 1))  # [[-2,2]]
```

**Explanation**: The function uses a max heap to keep the k closest points based on distance.
</details>

## Exercise 29: Implement Priority Queue
**Description**: Implement a priority queue with push and pop operations.
**Example**:
```
pq = PriorityQueue()
pq.push(3, 1)
pq.push(1, 3)
pq.pop()  # (3, 1)
```
<details>
<summary>Click to expand solution</summary>

```python
from heapq import heappush, heappop

class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def push(self, priority, item):
        heappush(self.heap, (-priority, item))
    
    def pop(self):
        if self.heap:
            priority, item = heappop(self.heap)
            return (-priority, item)
        return None

pq = PriorityQueue()
pq.push(3, 1)
pq.push(1, 3)
print(pq.pop())  # (3, 1)
```

**Explanation**: The class uses a max heap (negated priorities) to manage items by priority.
</details>

## Exercise 30: Find Minimum Spanning Tree (Kruskal’s)
**Description**: Write a function to find the minimum spanning tree using Kruskal’s algorithm.
**Example**:
```
Input: edges=[(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)], n=4
Output: [(2, 3, 4), (0, 3, 5), (0, 2, 6)]
```
<details>
<summary>Click to expand solution</summary>

```python
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def kruskal(edges, n):
    parent = list(range(n))
    rank = [0] * n
    mst = []
    edges.sort(key=lambda x: x[2])
    for u, v, weight in edges:
        pu, pv = find_parent(parent, u), find_parent(parent, v)
        if pu != pv:
            if rank[pu] < rank[pv]:
                pu, pv = pv, pu
            parent[pv] = pu
            if rank[pu] == rank[pv]:
                rank[pu] += 1
            mst.append((u, v, weight))
    return mst

print(kruskal([(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)], 4))  # [(2, 3, 4), (0, 3, 5), (0, 2, 6)]
```

**Explanation**: The function uses a union-find data structure to build the MST.
</details>

## Exercise 31: Find Longest Common Subsequence
**Description**: Write a function to find the length of the longest common subsequence of two strings.
**Example**:
```
Input: text1="abcde", text2="ace"
Output: 3
```
<details>
<summary>Click to expand solution</summary>

```python
def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

print(longest_common_subsequence("abcde", "ace"))  # 3
```

**Explanation**: The function uses dynamic programming to find the longest common subsequence.
</details>

## Exercise 32: Implement Bloom Filter
**Description**: Implement a Bloom filter for probabilistic membership testing.
**Example**:
```
bf = BloomFilter(100, 3)
bf.add("apple")
bf.contains("apple")  # True
bf.contains("banana")  # False
```
<details>
<summary>Click to expand solution</summary>

```python
import mmh3
from bitarray import bitarray

class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)
    
    def add(self, item):
        for i in range(self.hash_count):
            index = mmh3.hash(item, i) % self.size
            self.bit_array[index] = 1
    
    def contains(self, item):
        for i in range(self.hash_count):
            index = mmh3.hash(item, i) % self.size
            if not self.bit_array[index]:
                return False
        return True

bf = BloomFilter(100, 3)
bf.add("apple")
print(bf.contains("apple"))  # True
print(bf.contains("banana"))  # False
```

**Explanation**: The Bloom filter uses multiple hash functions and a bit array for probabilistic membership testing. Note: Requires `mmh3` and `bitarray` libraries.
</details>

## Exercise 33: Find Top K Frequent Elements
**Description**: Write a function to find the top k frequent elements in an array.
**Example**:
```
Input: nums=[1, 1, 1, 2, 2, 3], k=2
Output: [1, 2]
```
<details>
<summary>Click to expand solution</summary>

```python
from collections import Counter
from heapq import heappush, heappop

def top_k_frequent(nums, k):
    count = Counter(nums)
    heap = []
    for num, freq in count.items():
        heappush(heap, (-freq, num))
    return [heappop(heap)[1] for _ in range(k)]

print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
```

**Explanation**: The function uses a Counter and a max heap to find the k most frequent elements.
</details>

## Exercise 34: Find Minimum Cost Path
**Description**: Write a function to find the minimum cost path in a grid from top-left to bottom-right.
**Example**:
```
Input: grid=[[1,3,1], [1,5,1], [4,2,1]]
Output: 7
```
<details>
<summary>Click to expand solution</summary>

```python
def min_cost_path(grid):
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])
    dp = [[float('inf')] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(m):
        for j in range(n):
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j] + grid[i][j])
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1] + grid[i][j])
    return dp[m-1][n-1]

print(min_cost_path([[1,3,1], [1,5,1], [4,2,1]]))  # 7
```

**Explanation**: The function uses dynamic programming to find the minimum cost path, moving only right or down.
</details>