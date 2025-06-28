# Python Set DSA Patterns Interview Questions

This README provides **100 Python set manipulation questions** designed for AI/ML students preparing for technical interviews. The questions focus on set-specific problems, leveraging Python's set data structure for efficient operations like union, intersection, difference, and membership testing, as well as DSA patterns such as union-find, hashing, and combinatorial problems. They are categorized into **Basic**, **Intermediate**, and **Advanced** levels, covering tasks like duplicate detection, subset checks, and complex set-based algorithms. Each question includes a problem statement, with the solution hidden in a `<details>` tag to encourage users to attempt the problem before viewing the answer. This format supports hands-on practice and aligns with interview preparation for AI/ML roles, complementing the list-focused DSA questions.

## Basic Set Questions

### 1. Check for Duplicates in a List
**Problem**: Write a Python function to check if a list contains duplicates using a set.  
Example:  
```
Input: [1, 2, 3, 1]  
Output: True
```
<details>
<summary>Solution</summary>

```python
def has_duplicates(nums):
    return len(nums) != len(set(nums))
```

</details>

### 2. Find Intersection of Two Lists
**Problem**: Write a Python function to find common elements between two lists using sets.  
Example:  
```
Input: nums1 = [1, 2, 3], nums2 = [2, 3, 4]  
Output: [2, 3]
```
<details>
<summary>Solution</summary>

```python
def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))
```

</details>

### 3. Find Union of Two Lists
**Problem**: Write a Python function to find the union of two lists using sets.  
Example:  
```
Input: nums1 = [1, 2, 3], nums2 = [2, 3, 4]  
Output: [1, 2, 3, 4]
```
<details>
<summary>Solution</summary>

```python
def union(nums1, nums2):
    return list(set(nums1) | set(nums2))
```

</details>

### 4. Find Difference of Two Lists
**Problem**: Write a Python function to find elements in the first list that are not in the second list using sets.  
Example:  
```
Input: nums1 = [1, 2, 3], nums2 = [2, 3, 4]  
Output: [1]
```
<details>
<summary>Solution</summary>

```python
def difference(nums1, nums2):
    return list(set(nums1) - set(nums2))
```

</details>

### 5. Check if Subset
**Problem**: Write a Python function to check if one list is a subset of another using sets.  
Example:  
```
Input: nums1 = [1, 2], nums2 = [1, 2, 3]  
Output: True
```
<details>
<summary>Solution</summary>

```python
def is_subset(nums1, nums2):
    return set(nums1).issubset(set(nums2))
```

</details>

### 6. Check if Superset
**Problem**: Write a Python function to check if one list is a superset of another using sets.  
Example:  
```
Input: nums1 = [1, 2, 3], nums2 = [1, 2]  
Output: True
```
<details>
<summary>Solution</summary>

```python
def is_superset(nums1, nums2):
    return set(nums1).issuperset(set(nums2))
```

</details>

### 7. Find Symmetric Difference
**Problem**: Write a Python function to find elements that are in either of two lists but not in both using sets.  
Example:  
```
Input: nums1 = [1, 2, 3], nums2 = [2, 3, 4]  
Output: [1, 4]
```
<details>
<summary>Solution</summary>

```python
def symmetric_difference(nums1, nums2):
    return list(set(nums1) ^ set(nums2))
```

</details>

### 8. Count Unique Elements
**Problem**: Write a Python function to count the number of unique elements in a list using a set.  
Example:  
```
Input: [1, 2, 2, 3, 3, 3]  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def count_unique(nums):
    return len(set(nums))
```

</details>

### 9. Remove Duplicates from List
**Problem**: Write a Python function to remove duplicates from a list while preserving order using a set.  
Example:  
```
Input: [1, 3, 3, 2, 1]  
Output: [1, 3, 2]
```
<details>
<summary>Solution</summary>

```python
def remove_duplicates(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
```

</details>

### 10. Check if Disjoint Sets
**Problem**: Write a Python function to check if two lists have no common elements using sets.  
Example:  
```
Input: nums1 = [1, 2, 3], nums2 = [4, 5, 6]  
Output: True
```
<details>
<summary>Solution</summary>

```python
def is_disjoint(nums1, nums2):
    return set(nums1).isdisjoint(set(nums2))
```

</details>

### 11. Find First Unique Element
**Problem**: Write a Python function to find the first element that appears exactly once in a list using a set.  
Example:  
```
Input: [1, 2, 1, 3, 3]  
Output: 2
```
<details>
<summary>Solution</summary>

```python
from collections import Counter
def first_unique(nums):
    count = Counter(nums)
    for num in nums:
        if count[num] == 1:
            return num
    return None
```

</details>

### 12. Find All Duplicates
**Problem**: Write a Python function to find all duplicate elements in a list using a set.  
Example:  
```
Input: [1, 2, 2, 3, 3, 4]  
Output: [2, 3]
```
<details>
<summary>Solution</summary>

```python
def find_duplicates(nums):
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)
```

</details>

### 13. Check if List Contains All Elements
**Problem**: Write a Python function to check if a list contains all elements from a target list using sets.  
Example:  
```
Input: nums = [1, 2, 3, 4], target = [1, 2]  
Output: True
```
<details>
<summary>Solution</summary>

```python
def contains_all(nums, target):
    return set(target).issubset(set(nums))
```

</details>

### 14. Find Unique Pairs with Sum K
**Problem**: Write a Python function to find all unique pairs in a list that sum to k using a set.  
Example:  
```
Input: nums = [1, 2, 3, 4], k = 5  
Output: [[1, 4], [2, 3]]
```
<details>
<summary>Solution</summary>

```python
def find_pairs(nums, k):
    seen = set()
    result = set()
    for num in nums:
        if k - num in seen:
            result.add(tuple(sorted([num, k - num])))
        seen.add(num)
    return list(result)
```

</details>

### 15. Check for Anagram Groups
**Problem**: Write a Python function to group anagrams in a list of numbers using a set for validation.  
Example:  
```
Input: nums = [[1, 2], [2, 1], [3, 4]]  
Output: [[[1, 2], [2, 1]], [[3, 4]]]
```
<details>
<summary>Solution</summary>

```python
def group_anagrams(nums):
    result = {}
    for arr in nums:
        key = tuple(sorted(arr))
        if key in result:
            result[key].append(arr)
        else:
            result[key] = [arr]
    return list(result.values())
```

</details>

### 16. Find Single Number
**Problem**: Write a Python function to find the number that appears exactly once in a list where all others appear twice using a set.  
Example:  
```
Input: [4, 1, 2, 1, 2]  
Output: 4
```
<details>
<summary>Solution</summary>

```python
def single_number(nums):
    return 2 * sum(set(nums)) - sum(nums)
```

</details>

### 17. Find Missing Number
**Problem**: Write a Python function to find the missing number in a list of n integers from 0 to n using a set.  
Example:  
```
Input: [3, 0, 1]  
Output: 2
```
<details>
<summary>Solution</summary>

```python
def missing_number(nums):
    return len(nums) * (len(nums) + 1) // 2 - sum(set(nums))
```

</details>

### 18. Find Common Elements in K Lists
**Problem**: Write a Python function to find common elements across k lists using sets.  
Example:  
```
Input: [[1, 2, 3], [2, 3, 4], [2, 3, 5]]  
Output: [2, 3]
```
<details>
<summary>Solution</summary>

```python
def common_elements(lists):
    if not lists:
        return []
    result = set(lists[0])
    for lst in lists[1:]:
        result &= set(lst)
    return list(result)
```

</details>

### 19. Find Unique Subsets
**Problem**: Write a Python function to find all unique subsets of a list using sets.  
Example:  
```
Input: [1, 2]  
Output: [[], [1], [2], [1, 2]]
```
<details>
<summary>Solution</summary>

```python
def subsets(nums):
    result = [[]]
    for num in set(nums):
        result += [curr + [num] for curr in result]
    return result
```

</details>

### 20. Check for Unique Elements
**Problem**: Write a Python function to check if all elements in a list are unique using a set.  
Example:  
```
Input: [1, 2, 3, 4]  
Output: True
```
<details>
<summary>Solution</summary>

```python
def all_unique(nums):
    return len(nums) == len(set(nums))
```

</details>

## Intermediate Set Questions

### 21. Find Intersection with Duplicates
**Problem**: Write a Python function to find the intersection of two lists, including duplicates, using a set and counter.  
Example:  
```
Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]  
Output: [2, 2]
```
<details>
<summary>Solution</summary>

```python
from collections import Counter
def intersect_with_duplicates(nums1, nums2):
    count1 = Counter(nums1)
    result = []
    for num in nums2:
        if num in count1 and count1[num] > 0:
            result.append(num)
            count1[num] -= 1
    return result
```

</details>

### 22. Longest Consecutive Sequence
**Problem**: Write a Python function to find the length of the longest consecutive elements sequence using a set.  
Example:  
```
Input: [100, 4, 200, 1, 3, 2]  
Output: 4
```
<details>
<summary>Solution</summary>

```python
def longest_consecutive(nums):
    num_set = set(nums)
    max_len = 0
    for num in num_set:
        if num - 1 not in num_set:
            curr_num = num
            curr_len = 1
            while curr_num + 1 in num_set:
                curr_num += 1
                curr_len += 1
            max_len = max(max_len, curr_len)
    return max_len
```

</details>

### 23. Find All Numbers Disappeared
**Problem**: Write a Python function to find all numbers that disappeared in a list of integers from 1 to n using a set.  
Example:  
```
Input: [4, 3, 2, 7, 8, 2, 3, 1]  
Output: [5, 6]
```
<details>
<summary>Solution</summary>

```python
def find_disappeared_numbers(nums):
    return list(set(range(1, len(nums) + 1)) - set(nums))
```

</details>

### 24. Find Unique Triplets with Sum Zero
**Problem**: Write a Python function to find all unique triplets in a list that sum to zero using a set.  
Example:  
```
Input: [-1, 0, 1, 2, -1, -4]  
Output: [[-1, -1, 2], [-1, 0, 1]]
```
<details>
<summary>Solution</summary>

```python
def three_sum(nums):
    nums.sort()
    result = set()
    for i in range(len(nums) - 2):
        seen = set()
        target = -nums[i]
        for j in range(i + 1, len(nums)):
            if target - nums[j] in seen:
                result.add((nums[i], target - nums[j], nums[j]))
            seen.add(nums[j])
    return [list(t) for t in result]
```

</details>

### 25. Find Subarrays with Equal Sum
**Problem**: Write a Python function to check if there exist two subarrays with equal sum using a set.  
Example:  
```
Input: [4, 2, 4]  
Output: True
```
<details>
<summary>Solution</summary>

```python
def find_subarrays_equal_sum(nums):
    seen = set()
    curr_sum = 0
    seen.add(0)
    for num in nums:
        curr_sum += num
        if curr_sum in seen:
            return True
        seen.add(curr_sum)
    return False
```

</details>

### 26. Check if Array Can Be Partitioned into Two Subsets
**Problem**: Write a Python function to check if a list can be partitioned into two subsets with equal sum using a set.  
Example:  
```
Input: [1, 5, 11, 5]  
Output: True
```
<details>
<summary>Solution</summary>

```python
def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    sums = {0}
    for num in nums:
        new_sums = set()
        for s in sums:
            new_sums.add(s)
            new_sums.add(s + num)
        sums = new_sums
        if target in sums:
            return True
    return False
```

</details>

### 27. Find Maximum Number of Unique Elements
**Problem**: Write a Python function to find the maximum number of unique elements in any subarray of size k using a set.  
Example:  
```
Input: nums = [1, 2, 1, 3, 4], k = 3  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def max_unique_subarray(nums, k):
    max_unique = 0
    for i in range(len(nums) - k + 1):
        max_unique = max(max_unique, len(set(nums[i:i+k])))
    return max_unique
```

</details>

### 28. Find All Unique Pairs with Difference K
**Problem**: Write a Python function to find all unique pairs with difference k in a list using a set.  
Example:  
```
Input: nums = [3, 1, 4, 1, 5], k = 2  
Output: [[1, 3], [3, 5]]
```
<details>
<summary>Solution</summary>

```python
def pairs_with_difference(nums, k):
    num_set = set(nums)
    result = set()
    for num in nums:
        if num + k in num_set:
            result.add(tuple(sorted([num, num + k])))
        if num - k in num_set:
            result.add(tuple(sorted([num - k, num])))
    return [list(pair) for pair in result]
```

</details>

### 29. Check for Valid Sudoku
**Problem**: Write a Python function to check if a 9x9 Sudoku board (list of lists) is valid using sets.  
Example:  
```
Input: board = [["5","3",".",".","7",".",".",".","."], ...]  
Output: True
```
<details>
<summary>Solution</summary>

```python
def is_valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                continue
            num = board[i][j]
            if num in rows[i] or num in cols[j] or num in boxes[(i//3)*3 + j//3]:
                return False
            rows[i].add(num)
            cols[j].add(num)
            boxes[(i//3)*3 + j//3].add(num)
    return True
```

</details>

### 30. Find Longest Subarray with Distinct Elements
**Problem**: Write a Python function to find the length of the longest subarray with distinct elements using a set.  
Example:  
```
Input: [1, 2, 3, 1, 2]  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def longest_subarray_distinct(nums):
    seen = set()
    left = 0
    max_len = 0
    for right in range(len(nums)):
        while nums[right] in seen:
            seen.remove(nums[left])
            left += 1
        seen.add(nums[right])
        max_len = max(max_len, right - left + 1)
    return max_len
```

</details>

### 31. Find All Unique Subsets with Sum K
**Problem**: Write a Python function to find all unique subsets of a list that sum to k using a set.  
Example:  
```
Input: nums = [1, 2, 3], k = 3  
Output: [[1, 2], [3]]
```
<details>
<summary>Solution</summary>

```python
def subsets_with_sum(nums, k):
    result = []
    def backtrack(index, curr_sum, curr_set):
        if curr_sum == k:
            result.append(list(curr_set))
            return
        if curr_sum > k or index >= len(nums):
            return
        curr_set.add(nums[index])
        backtrack(index + 1, curr_sum + nums[index], curr_set)
        curr_set.remove(nums[index])
        backtrack(index + 1, curr_sum, curr_set)
    backtrack(0, 0, set())
    return result
```

</details>

### 32. Find Common Characters
**Problem**: Write a Python function to find all characters that appear in all strings of a list using sets.  
Example:  
```
Input: ["bella", "label", "roller"]  
Output: ["e", "l", "l"]
```
<details>
<summary>Solution</summary>

```python
from collections import Counter
def common_chars(words):
    result = Counter(words[0])
    for word in words[1:]:
        curr = Counter(word)
        for c in result:
            result[c] = min(result[c], curr[c])
    return [c for c, count in result.items() for _ in range(count)]
```

</details>

### 33. Find Unique Combinations
**Problem**: Write a Python function to find all unique combinations of a list that sum to a target using a set.  
Example:  
```
Input: nums = [2, 3, 6, 7], target = 7  
Output: [[2, 2, 3], [7]]
```
<details>
<summary>Solution</summary>

```python
def combination_sum(nums, target):
    result = []
    nums.sort()
    def backtrack(start, target, curr):
        if target == 0:
            result.append(list(curr))
            return
        for i in range(start, len(nums)):
            if nums[i] > target:
                break
            curr_set = set(curr)
            curr_set.add(nums[i])
            backtrack(i, target - nums[i], curr_set)
    backtrack(0, target, set())
    return result
```

</details>

### 34. Check for Palindrome Permutation
**Problem**: Write a Python function to check if a list of numbers has a permutation that forms a palindrome using a set.  
Example:  
```
Input: [1, 2, 2, 1, 3]  
Output: True
```
<details>
<summary>Solution</summary>

```python
from collections import Counter
def can_form_palindrome(nums):
    count = Counter(nums)
    odd_count = sum(1 for c in count.values() if c % 2 != 0)
    return odd_count <= 1
```

</details>

### 35. Find All Unique Elements in Matrix
**Problem**: Write a Python function to find all unique elements in a matrix (list of lists) using a set.  
Example:  
```
Input: [[1, 2, 2], [3, 1, 4], [4, 5, 5]]  
Output: [1, 2, 3, 4, 5]
```
<details>
<summary>Solution</summary>

```python
def unique_elements_matrix(matrix):
    return list(set(num for row in matrix for num in row))
```

</details>

### 36. Find Missing Ranges
**Problem**: Write a Python function to find all missing ranges in a list from lower to upper using a set.  
Example:  
```
Input: nums = [0, 1, 3, 50, 75], lower = 0, upper = 99  
Output: [[2, 2], [4, 49], [51, 74], [76, 99]]
```
<details>
<summary>Solution</summary>

```python
def find_missing_ranges(nums, lower, upper):
    nums = set(nums)
    result = []
    start = lower
    for i in range(lower, upper + 1):
        if i not in nums and i > start:
            result.append([start, i - 1])
            start = i + 1
        elif i not in nums and i == start:
            start += 1
    if start <= upper:
        result.append([start, upper])
    return result
```

</details>

### 37. Find All Unique Subarrays
**Problem**: Write a Python function to find all unique subarrays of a list using a set to track seen subarrays.  
Example:  
```
Input: [1, 2, 3]  
Output: [[1], [2], [3], [1, 2], [2, 3], [1, 2, 3]]
```
<details>
<summary>Solution</summary>

```python
def unique_subarrays(nums):
    result = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            result.add(tuple(nums[i:j]))
    return [list(sub) for sub in result]
```

</details>

### 38. Find All Unique Pairs with Product K
**Problem**: Write a Python function to find all unique pairs in a list with product k using a set.  
Example:  
```
Input: nums = [1, 2, 3, 4], k = 8  
Output: [[2, 4]]
```
<details>
<summary>Solution</summary>

```python
def pairs_with_product(nums, k):
    seen = set()
    result = set()
    for num in nums:
        if k % num == 0 and k // num in seen:
            result.add(tuple(sorted([num, k // num])))
        seen.add(num)
    return [list(pair) for pair in result]
```

</details>

### 39. Find All Elements Appearing Exactly K Times
**Problem**: Write a Python function to find all elements that appear exactly k times in a list using a set.  
Example:  
```
Input: nums = [1, 2, 2, 3, 3, 3], k = 2  
Output: [2]
```
<details>
<summary>Solution</summary>

```python
from collections import Counter
def elements_k_times(nums, k):
    count = Counter(nums)
    return [num for num, freq in count.items() if freq == k]
```

</details>

### 40. Find Unique Elements in K Windows
**Problem**: Write a Python function to find the number of unique elements in each window of size k using a set.  
Example:  
```
Input: nums = [1, 2, 1, 3, 4], k = 3  
Output: [2, 3, 3]
```
<details>
<summary>Solution</summary>

```python
def unique_in_windows(nums, k):
    result = []
    for i in range(len(nums) - k + 1):
        result.append(len(set(nums[i:i+k])))
    return result
```

</details>

## Advanced Set Questions

### 41. Union-Find for Connected Components
**Problem**: Write a Python class to find the number of connected components in a graph using a union-find data structure with sets.  
Example:  
```
Input: n = 5, edges = [[0, 1], [1, 2], [3, 4]]  
Output: 2
```
<details>
<summary>Solution</summary>

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.count -= 1

def count_components(n, edges):
    uf = UnionFind(n)
    for x, y in edges:
        uf.union(x, y)
    return uf.count
```

</details>

### 42. Find Smallest Set of Vertices
**Problem**: Write a Python function to find the smallest set of vertices to reach all nodes in a directed graph using sets.  
Example:  
```
Input: n = 6, edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]  
Output: [0, 3]
```
<details>
<summary>Solution</summary>

```python
def find_smallest_set(n, edges):
    reachable = set()
    for _, v in edges:
        reachable.add(v)
    return [i for i in range(n) if i not in reachable]
```

</details>

### 43. Find All Possible Subsets with Duplicates
**Problem**: Write a Python function to find all unique subsets of a list with duplicates using a set.  
Example:  
```
Input: [1, 2, 2]  
Output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
```
<details>
<summary>Solution</summary>

```python
def subsets_with_duplicates(nums):
    nums.sort()
    result = set([()])
    for num in nums:
        new_subsets = set()
        for subset in result:
            new_subsets.add(subset + (num,))
        result |= new_subsets
    return [list(subset) for subset in result]
```

</details>

### 44. Maximum Size Subset with Given Difference
**Problem**: Write a Python function to find the maximum size subset with a given difference between any two elements using a set.  
Example:  
```
Input: nums = [1, 2, 3, 4, 5], diff = 2  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def max_size_subset_diff(nums, diff):
    nums.sort()
    max_size = 1
    for i in range(len(nums)):
        curr_set = {nums[i]}
        for j in range(i + 1, len(nums)):
            valid = True
            for num in curr_set:
                if abs(nums[j] - num) > diff:
                    valid = False
                    break
            if valid:
                curr_set.add(nums[j])
        max_size = max(max_size, len(curr_set))
    return max_size
```

</details>

### 45. Find All Unique Triplets with Product K
**Problem**: Write a Python function to find all unique triplets with product k using a set.  
Example:  
```
Input: nums = [1, 2, 3, 4], k = 24  
Output: [[1, 2, 12], [1, 3, 8], [2, 3, 4]]
```
<details>
<summary>Solution</summary>

```python
def triplets_with_product(nums, k):
    num_set = set(nums)
    result = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            prod = nums[i] * nums[j]
            if k % prod == 0 and k // prod in num_set:
                result.add(tuple(sorted([nums[i], nums[j], k // prod])))
    return [list(t) for t in result]
```

</details>

### 46. Find Maximum XOR of Two Numbers
**Problem**: Write a Python function to find the maximum XOR of any two numbers in a list using a set.  
Example:  
```
Input: [3, 10, 5, 25, 2, 8]  
Output: 28
```
<details>
<summary>Solution</summary>

```python
def find_maximum_xor(nums):
    max_xor = 0
    mask = 0
    for i in range(31, -1, -1):
        mask |= (1 << i)
        prefixes = set()
        for num in nums:
            prefixes.add(num & mask)
        temp = max_xor | (1 << i)
        for prefix in prefixes:
            if (temp ^ prefix) in prefixes:
                max_xor = temp
                break
    return max_xor
```

</details>

### 47. Find All Unique Subarrays with K Distinct Elements
**Problem**: Write a Python function to find all subarrays with exactly k distinct elements using a set.  
Example:  
```
Input: nums = [1, 2, 1, 2, 3], k = 2  
Output: [[1, 2], [2, 1], [1, 2, 1], [2, 1, 2], [1, 2, 3]]
```
<details>
<summary>Solution</summary>

```python
def subarrays_with_k_distinct(nums, k):
    result = []
    for i in range(len(nums)):
        curr_set = set()
        for j in range(i, len(nums)):
            curr_set.add(nums[j])
            if len(curr_set) == k:
                result.append(nums[i:j+1])
            elif len(curr_set) > k:
                break
    return result
```

</details>

### 48. Find All Unique Elements in Sliding Window
**Problem**: Write a Python function to find the number of unique elements in each sliding window of size k using a set.  
Example:  
```
Input: nums = [1, 2, 1, 3, 4], k = 3  
Output: [2, 3, 3]
```
<details>
<summary>Solution</summary>

```python
def unique_in_sliding_window(nums, k):
    result = []
    curr_set = set()
    for i in range(len(nums)):
        curr_set.add(nums[i])
        if i >= k:
            curr_set.discard(nums[i - k])
        if i >= k - 1:
            result.append(len(curr_set))
    return result
```

</details>

### 49. Check for Valid Graph Coloring
**Problem**: Write a Python function to check if a graph can be colored with k colors using sets.  
Example:  
```
Input: n = 4, edges = [[0, 1], [1, 2], [2, 3], [3, 0]], k = 2  
Output: True
```
<details>
<summary>Solution</summary>

```python
def valid_graph_coloring(n, edges, k):
    from collections import defaultdict
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    colors = [-1] * n
    def can_color(node, color):
        colors[node] = color
        for neighbor in graph[node]:
            neighbor_colors = {colors[n] for n in graph[neighbor] if colors[n] != -1}
            for c in range(k):
                if c not in neighbor_colors:
                    if colors[neighbor] == -1 and not can_color(neighbor, c):
                        return False
            if colors[neighbor] == -1:
                return False
        return True
    for i in range(n):
        if colors[i] == -1:
            if not can_color(i, 0):
                return False
    return True
```

</details>

### 50. Find All Unique Subsets with Target Sum
**Problem**: Write a Python function to find all unique subsets with a target sum using a set to avoid duplicates.  
Example:  
```
Input: nums = [1, 2, 2], target = 4  
Output: [[2, 2]]
```
<details>
<summary>Solution</summary>

```python
def subsets_with_target_sum(nums, target):
    result = set()
    def backtrack(index, curr_sum, curr):
        if curr_sum == target:
            result.add(tuple(sorted(curr)))
            return
        if curr_sum > target or index >= len(nums):
            return
        backtrack(index + 1, curr_sum + nums[index], curr + [nums[index]])
        backtrack(index + 1, curr_sum, curr)
    backtrack(0, 0, [])
    return [list(subset) for subset in result]
```

</details>

### 51. Find Maximum Subset with No Pair Sum Divisible by K
**Problem**: Write a Python function to find the size of the maximum subset where no pair sum is divisible by k using a set.  
Example:  
```
Input: nums = [1, 7, 2, 4], k = 3  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def max_subset_no_pair_divisible(nums, k):
    remainders = [0] * k
    for num in nums:
        remainders[num % k] += 1
    max_size = min(remainders[0], 1)
    for i in range(1, (k + 1) // 2):
        max_size += max(remainders[i], remainders[k - i])
    if k % 2 == 0:
        max_size += min(remainders[k // 2], 1)
    return max_size
```

</details>

### 52. Find All Unique Subarrays with Sum Zero
**Problem**: Write a Python function to find all unique subarrays with sum zero using a set for prefix sums.  
Example:  
```
Input: [4, 2, -2, 1, -1]  
Output: [[2, -2], [2, -2, 1, -1]]
```
<details>
<summary>Solution</summary>

```python
def subarrays_with_sum_zero(nums):
    result = []
    curr_sum = 0
    sums = {0: [-1]}
    for i, num in enumerate(nums):
        curr_sum += num
        if curr_sum in sums:
            for start in sums[curr_sum]:
                result.append(nums[start + 1:i + 1])
        sums[curr_sum] = sums.get(curr_sum, []) + [i]
    return result
```

</details>

### 53. Find Maximum Length of Subarray with K Distinct Elements
**Problem**: Write a Python function to find the maximum length of a subarray with at most k distinct elements using a set.  
Example:  
```
Input: nums = [1, 2, 1, 2, 3], k = 2  
Output: 4
```
<details>
<summary>Solution</summary>

```python
def max_subarray_k_distinct(nums, k):
    seen = {}
    left = 0
    max_len = 0
    for right in range(len(nums)):
        seen[nums[right]] = seen.get(nums[right], 0) + 1
        while len(seen) > k:
            seen[nums[left]] -= 1
            if seen[nums[left]] == 0:
                del seen[nums[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len
```

</details>

### 54. Find All Unique Pairs with Same XOR
**Problem**: Write a Python function to find all unique pairs with the same XOR value using a set.  
Example:  
```
Input: nums = [1, 2, 3, 4]  
Output: [[1, 3], [2, 4]]
```
<details>
<summary>Solution</summary>

```python
def pairs_with_same_xor(nums):
    result = []
    xor_map = {}
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            xor_val = nums[i] ^ nums[j]
            xor_map[xor_val] = xor_map.get(xor_val, []) + [[nums[i], nums[j]]]
    for pairs in xor_map.values():
        result.extend(pairs)
    return result
```

</details>

### 55. Find All Unique Subsets with Product K
**Problem**: Write a Python function to find all unique subsets with product k using a set.  
Example:  
```
Input: nums = [1, 2, 3, 4], k = 6  
Output: [[1, 2, 3], [2, 3]]
```
<details>
<summary>Solution</summary>

```python
def subsets_with_product(nums, k):
    result = set()
    def backtrack(index, curr_prod, curr):
        if curr_prod == k:
            result.add(tuple(sorted(curr)))
            return
        if curr_prod > k or index >= len(nums):
            return
        backtrack(index + 1, curr_prod * nums[index], curr + [nums[index]])
        backtrack(index + 1, curr_prod, curr)
    backtrack(0, 1, [])
    return [list(subset) for subset in result]
```

</details>

### 56. Find Maximum Subset with GCD K
**Problem**: Write a Python function to find the maximum size subset where the GCD of all elements is k using a set.  
Example:  
```
Input: nums = [2, 4, 6, 8], k = 2  
Output: 4
```
<details>
<summary>Solution</summary>

```python
from math import gcd
def max_subset_gcd(nums, k):
    valid = [num for num in nums if num % k == 0]
    return len(valid)
```

</details>

### 57. Find All Unique Subarrays with Target Sum
**Problem**: Write a Python function to find all unique subarrays with a target sum using a set for prefix sums.  
Example:  
```
Input: nums = [1, 2, 3, 2], target = 5  
Output: [[2, 3], [3, 2]]
```
<details>
<summary>Solution</summary>

```python
def subarrays_with_target_sum(nums, target):
    result = []
    curr_sum = 0
    sums = {0: [-1]}
    for i, num in enumerate(nums):
        curr_sum += num
        if curr_sum - target in sums:
            for start in sums[curr_sum - target]:
                result.append(nums[start + 1:i + 1])
        sums[curr_sum] = sums.get(curr_sum, []) + [i]
    return result
```

</details>

### 58. Find Maximum Subset with No Pair Product K
**Problem**: Write a Python function to find the maximum size subset where no pair has product k using a set.  
Example:  
```
Input: nums = [1, 2, 3, 4], k = 6  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def max_subset_no_pair_product(nums, k):
    max_size = 0
    for mask in range(1 << len(nums)):
        curr_set = set()
        valid = True
        for i in range(len(nums)):
            if mask & (1 << i):
                for num in curr_set:
                    if num * nums[i] == k:
                        valid = False
                        break
                if not valid:
                    break
                curr_set.add(nums[i])
        if valid:
            max_size = max(max_size, len(curr_set))
    return max_size
```

</details>

### 59. Find All Unique Subarrays with K Elements
**Problem**: Write a Python function to find all unique subarrays with exactly k elements using a set.  
Example:  
```
Input: nums = [1, 2, 3, 4], k = 2  
Output: [[1, 2], [2, 3], [3, 4]]
```
<details>
<summary>Solution</summary>

```python
def unique_subarrays_k(nums, k):
    result = set()
    for i in range(len(nums) - k + 1):
        result.add(tuple(nums[i:i+k]))
    return [list(sub) for sub in result]
```

</details>

### 60. Find Minimum Set Cover
**Problem**: Write a Python function to find the minimum number of sets needed to cover all elements in a universe using a greedy approach.  
Example:  
```
Input: universe = [1, 2, 3, 4], subsets = [[1, 2], [2, 3], [3, 4]]  
Output: 2
```
<details>
<summary>Solution</summary>

```python
def min_set_cover(universe, subsets):
    universe = set(universe)
    covered = set()
    count = 0
    while covered != universe:
        max_cover = set()
        best_subset = None
        for subset in subsets:
            curr = set(subset) - covered
            if len(curr) > len(max_cover):
                max_cover = curr
                best_subset = subset
        if best_subset:
            covered |= set(best_subset)
            count += 1
        else:
            break
    return count
```

</details>

### 61. Find All Unique Subsets with No Duplicates
**Problem**: Write a Python function to find all unique subsets of a list without duplicates using a set.  
Example:  
```
Input: [1, 2, 3]  
Output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
```
<details>
<summary>Solution</summary>

```python
def unique_subsets(nums):
    result = set([()])
    for num in nums:
        new_subsets = set()
        for subset in result:
            new_subsets.add(subset + (num,))
        result |= new_subsets
    return [list(subset) for subset in result]
```

</details>

### 62. Find Maximum Subset with Sum Less Than K
**Problem**: Write a Python function to find the maximum size subset with sum less than k using a set.  
Example:  
```
Input: nums = [1, 2, 3], k = 5  
Output: 2
```
<details>
<summary>Solution</summary>

```python
def max_subset_sum_less_than_k(nums, k):
    max_size = 0
    for mask in range(1 << len(nums)):
        curr_sum = 0
        curr_set = set()
        for i in range(len(nums)):
            if mask & (1 << i):
                curr_sum += nums[i]
                curr_set.add(nums[i])
        if curr_sum < k:
            max_size = max(max_size, len(curr_set))
    return max_size
```

</details>

### 63. Find All Unique Pairs with Sum in Range
**Problem**: Write a Python function to find all unique pairs with sum in a given range using a set.  
Example:  
```
Input: nums = [1, 2, 3, 4], low = 3, high = 5  
Output: [[1, 2], [1, 3], [1, 4], [2, 3]]
```
<details>
<summary>Solution</summary>

```python
def pairs_with_sum_in_range(nums, low, high):
    num_set = set(nums)
    result = set()
    for num in nums:
        for target in range(low - num, high - num + 1):
            if target in num_set and target != num:
                result.add(tuple(sorted([num, target])))
    return [list(pair) for pair in result]
```

</details>

### 64. Find Maximum Subset with No Pair Difference K
**Problem**: Write a Python function to find the maximum size subset where no pair has difference k using a set.  
Example:  
```
Input: nums = [1, 2, 3, 4], k = 1  
Output: 2
```
<details>
<summary>Solution</summary>

```python
def max_subset_no_pair_diff(nums, k):
    max_size = 0
    for mask in range(1 << len(nums)):
        curr_set = set()
        valid = True
        for i in range(len(nums)):
            if mask & (1 << i):
                for num in curr_set:
                    if abs(nums[i] - num) == k:
                        valid = False
                        break
                if not valid:
                    break
                curr_set.add(nums[i])
        if valid:
            max_size = max(max_size, len(curr_set))
    return max_size
```

</details>

### 65. Find All Unique Subarrays with Product Less Than K
**Problem**: Write a Python function to find all unique subarrays with product less than k using a set.  
Example:  
```
Input: nums = [1, 2, 3], k = 6  
Output: [[1], [2], [3], [1, 2], [1, 3]]
```
<details>
<summary>Solution</summary>

```python
def subarrays_with_product_less_than_k(nums, k):
    result = set()
    for i in range(len(nums)):
        curr_prod = 1
        for j in range(i, len(nums)):
            curr_prod *= nums[j]
            if curr_prod < k:
                result.add(tuple(nums[i:j+1]))
            else:
                break
    return [list(sub) for sub in result]
```

</details>

### 66. Find All Unique Subsets with GCD K
**Problem**: Write a Python function to find all unique subsets with GCD k using a set.  
Example:  
```
Input: nums = [2, 4, 6, 8], k = 2  
Output: [[2], [4], [6], [8], [2, 4], [2, 6], [2, 8], [4, 6], [4, 8], [6, 8], [2, 4, 6], [2, 4, 8], [2, 6, 8], [4, 6, 8], [2, 4, 6, 8]]
```
<details>
<summary>Solution</summary>

```python
from math import gcd
from functools import reduce
def subsets_with_gcd(nums, k):
    result = set()
    for mask in range(1, 1 << len(nums)):
        curr = []
        for i in range(len(nums)):
            if mask & (1 << i):
                curr.append(nums[i])
        if curr and reduce(gcd, curr) == k:
            result.add(tuple(sorted(curr)))
    return [list(subset) for subset in result]
```

</details>

### 67. Find Maximum Length Subarray with Unique Elements
**Problem**: Write a Python function to find the maximum length subarray with unique elements using a set and sliding window.  
Example:  
```
Input: [1, 2, 3, 1, 2]  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def max_length_unique_subarray(nums):
    seen = set()
    left = 0
    max_len = 0
    for right in range(len(nums)):
        while nums[right] in seen:
            seen.remove(nums[left])
            left += 1
        seen.add(nums[right])
        max_len = max(max_len, right - left + 1)
    return max_len
```

</details>

### 68. Find All Unique Subarrays with Sum in Range
**Problem**: Write a Python function to find all unique subarrays with sum in a given range using a set.  
Example:  
```
Input: nums = [1, 2, 3], low = 3, high = 5  
Output: [[1, 2], [2, 3], [1, 2, 3]]
```
<details>
<summary>Solution</summary>

```python
def subarrays_with_sum_in_range(nums, low, high):
    result = set()
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            if low <= curr_sum <= high:
                result.add(tuple(nums[i:j+1]))
    return [list(sub) for sub in result]
```

</details>

### 69. Find Maximum Subset with No Pair Sum in Set
**Problem**: Write a Python function to find the maximum size subset where no pair’s sum exists in a given set.  
Example:  
```
Input: nums = [1, 2, 3, 4], forbidden = [5, 7]  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def max_subset_no_pair_sum(nums, forbidden):
    forbidden = set(forbidden)
    max_size = 0
    for mask in range(1 << len(nums)):
        curr_set = set()
        valid = True
        for i in range(len(nums)):
            if mask & (1 << i):
                for num in curr_set:
                    if num + nums[i] in forbidden:
                        valid = False
                        break
                if not valid:
                    break
                curr_set.add(nums[i])
        if valid:
            max_size = max(max_size, len(curr_set))
    return max_size
```

</details>

### 70. Find All Unique Subarrays with Distinct Elements
**Problem**: Write a Python function to find all unique subarrays with distinct elements using a set.  
Example:  
```
Input: [1, 2, 3, 1]  
Output: [[1], [2], [3], [1, 2], [2, 3], [1, 2, 3]]
```
<details>
<summary>Solution</summary>

```python
def unique_subarrays_distinct(nums):
    result = set()
    for i in range(len(nums)):
        curr_set = set()
        for j in range(i, len(nums)):
            if nums[j] in curr_set:
                break
            curr_set.add(nums[j])
            result.add(tuple(nums[i:j+1]))
    return [list(sub) for sub in result]
```

</details>

### 71. Find Maximum Subset with No Pair Product in Set
**Problem**: Write a Python function to find the maximum size subset where no pair’s product exists in a given set.  
Example:  
```
Input: nums = [1, 2, 3, 4], forbidden = [6, 8]  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def max_subset_no_pair_product(nums, forbidden):
    forbidden = set(forbidden)
    max_size = 0
    for mask in range(1 << len(nums)):
        curr_set = set()
        valid = True
        for i in range(len(nums)):
            if mask & (1 << i):
                for num in curr_set:
                    if num * nums[i] in forbidden:
                        valid = False
                        break
                if not valid:
                    break
                curr_set.add(nums[i])
        if valid:
            max_size = max(max_size, len(curr_set))
    return max_size
```

</details>

### 72. Find All Unique Subsets with Even Sum
**Problem**: Write a Python function to find all unique subsets with an even sum using a set.  
Example:  
```
Input: [1, 2, 3]  
Output: [[2], [1, 3]]
```
<details>
<summary>Solution</summary>

```python
def subsets_with_even_sum(nums):
    result = set()
    def backtrack(index, curr_sum, curr):
        if curr_sum % 2 == 0 and curr:
            result.add(tuple(sorted(curr)))
        if index >= len(nums):
            return
        backtrack(index + 1, curr_sum + nums[index], curr + [nums[index]])
        backtrack(index + 1, curr_sum, curr)
    backtrack(0, 0, [])
    return [list(subset) for subset in result]
```

</details>

### 73. Find Maximum Subset with No Pair XOR K
**Problem**: Write a Python function to find the maximum size subset where no pair’s XOR equals k using a set.  
Example:  
```
Input: nums = [1, 2, 3, 4], k = 7  
Output: 4
```
<details>
<summary>Solution</summary>

```python
def max_subset_no_pair_xor(nums, k):
    max_size = 0
    for mask in range(1 << len(nums)):
        curr_set = set()
        valid = True
        for i in range(len(nums)):
            if mask & (1 << i):
                for num in curr_set:
                    if num ^ nums[i] == k:
                        valid = False
                        break
                if not valid:
                    break
                curr_set.add(nums[i])
        if valid:
            max_size = max(max_size, len(curr_set))
    return max_size
```

</details>

### 74. Find All Unique Subarrays with Odd Sum
**Problem**: Write a Python function to find all unique subarrays with an odd sum using a set.  
Example:  
```
Input: [1, 2, 3]  
Output: [[1], [3], [1, 2, 3]]
```
<details>
<summary>Solution</summary>

```python
def subarrays_with_odd_sum(nums):
    result = set()
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            if curr_sum % 2 == 1:
                result.add(tuple(nums[i:j+1]))
    return [list(sub) for sub in result]
```

</details>

### 75. Find Maximum Subset with No Pair Sum Equal to Target
**Problem**: Write a Python function to find the maximum size subset where no pair sums to a target value using a set.  
Example:  
```
Input: nums = [1, 2, 3, 4], target = 7  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def max_subset_no_pair_sum(nums, target):
    max_size = 0
    for mask in range(1 << len(nums)):
        curr_set = set()
        valid = True
        for i in range(len(nums)):
            if mask & (1 << i):
                for num in curr_set:
                    if num + nums[i] == target:
                        valid = False
                        break
                if not valid:
                    break
                curr_set.add(nums[i])
        if valid:
            max_size = max(max_size, len(curr_set))
    return max_size
```

</details>

### 76. Find All Unique Subsets with Sum Divisible by K
**Problem**: Write a Python function to find all unique subsets with sum divisible by k using a set.  
Example:  
```
Input: nums = [4, 3, 2, 7], k = 5  
Output: [[3, 2], [4, 3, 2, 7]]
```
<details>
<summary>Solution</summary>

```python
def subsets_sum_divisible_k(nums, k):
    result = set()
    def backtrack(index, curr_sum, curr):
        if curr_sum % k == 0 and curr:
            result.add(tuple(sorted(curr)))
        if index >= len(nums):
            return
        backtrack(index + 1, curr_sum + nums[index], curr + [nums[index]])
        backtrack(index + 1, curr_sum, curr)
    backtrack(0, 0, [])
    return [list(subset) for subset in result]
```

</details>

### 77. Find Maximum Subset with No Pair Difference in Set
**Problem**: Write a Python function to find the maximum size subset where no pair’s difference exists in a given set.  
Example:  
```
Input: nums = [1, 2, 3, 4], forbidden = [1, 2]  
Output: 2
```
<details>
<summary>Solution</summary>

```python
def max_subset_no_pair_diff(nums, forbidden):
    forbidden = set(forbidden)
    max_size = 0
    for mask in range(1 << len(nums)):
        curr_set = set()
        valid = True
        for i in range(len(nums)):
            if mask & (1 << i):
                for num in curr_set:
                    if abs(num - nums[i]) in forbidden:
                        valid = False
                        break
                if not valid:
                    break
                curr_set.add(nums[i])
        if valid:
            max_size = max(max_size, len(curr_set))
    return max_size
```

</details>

### 78. Find All Unique Subarrays with No Duplicates
**Problem**: Write a Python function to find all unique subarrays with no duplicate elements using a set.  
Example:  
```
Input: [1, 2, 3, 1]  
Output: [[1], [2], [3], [1, 2], [2, 3], [1, 2, 3]]
```
<details>
<summary>Solution</summary>

```python
def unique_subarrays_no_duplicates(nums):
    result = set()
    for i in range(len(nums)):
        curr_set = set()
        for j in range(i, len(nums)):
            if nums[j] in curr_set:
                break
            curr_set.add(nums[j])
            result.add(tuple(nums[i:j+1]))
    return [list(sub) for sub in result]
```

</details>

### 79. Find Maximum Subset with Minimum Difference
**Problem**: Write a Python function to find the maximum size subset with a minimum difference between any two elements using a set.  
Example:  
```
Input: nums = [1, 2, 3, 4], min_diff = 2  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def max_subset_min_diff(nums, min_diff):
    max_size = 0
    for mask in range(1 << len(nums)):
        curr_set = set()
        valid = True
        for i in range(len(nums)):
            if mask & (1 << i):
                for num in curr_set:
                    if abs(nums[i] - num) < min_diff:
                        valid = False
                        break
                if not valid:
                    break
                curr_set.add(nums[i])
        if valid:
            max_size = max(max_size, len(curr_set))
    return max_size
```

</details>

### 80. Find All Unique Subsets with Product in Range
**Problem**: Write a Python function to find all unique subsets with product in a given range using a set.  
Example:  
```
Input: nums = [1, 2, 3], low = 2, high = 6  
Output: [[1, 2], [1, 3], [2], [3]]
```
<details>
<summary>Solution</summary>

```python
def subsets_with_product_in_range(nums, low, high):
    result = set()
    def backtrack(index, curr_prod, curr):
        if low <= curr_prod <= high and curr:
            result.add(tuple(sorted(curr)))
        if curr_prod > high or index >= len(nums):
            return
        backtrack(index + 1, curr_prod * nums[index], curr + [nums[index]])
        backtrack(index + 1, curr_prod, curr)
    backtrack(0, 1, [])
    return [list(subset) for subset in result]
```

</details>

### 81. Find Maximum Subset with No Pair Sum Divisible by K
**Problem**: Write a Python function to find the maximum size subset where no pair’s sum is divisible by k using a set.  
Example:  
```
Input: nums = [1, 2, 3, 4], k = 5  
Output: 4
```
<details>
<summary>Solution</summary>

```python
def max_subset_no_pair_sum_divisible(nums, k):
    remainders = [0] * k
    for num in nums:
        remainders[num % k] += 1
    max_size = min(remainders[0], 1)
    for i in range(1, (k + 1) // 2):
        max_size += max(remainders[i], remainders[k - i])
    if k % 2 == 0:
        max_size += min(remainders[k // 2], 1)
    return max_size
```

</details>

### 82. Find All Unique Subarrays with Sum Less Than K
**Problem**: Write a Python function to find all unique subarrays with sum less than k using a set.  
Example:  
```
Input: nums = [1, 2, 3], k = 5  
Output: [[1], [2], [3], [1, 2], [1, 3]]
```
<details>
<summary>Solution</summary>

```python
def subarrays_with_sum_less_than_k(nums, k):
    result = set()
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            if curr_sum < k:
                result.add(tuple(nums[i:j+1]))
            else:
                break
    return [list(sub) for sub in result]
```

</details>

### 83. Find Maximum Subset with No Pair XOR in Set
**Problem**: Write a Python function to find the maximum size subset where no pair’s XOR exists in a given set.  
Example:  
```
Input: nums = [1, 2, 3, 4], forbidden = [3, 7]  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def max_subset_no_pair_xor(nums, forbidden):
    forbidden = set(forbidden)
    max_size = 0
    for mask in range(1 << len(nums)):
        curr_set = set()
        valid = True
        for i in range(len(nums)):
            if mask & (1 << i):
                for num in curr_set:
                    if (num ^ nums[i]) in forbidden:
                        valid = False
                        break
                if not valid:
                    break
                curr_set.add(nums[i])
        if valid:
            max_size = max(max_size, len(curr_set))
    return max_size
```

</details>

### 84. Find All Unique Subsets with No Duplicates in Sliding Window
**Problem**: Write a Python function to find all unique subarrays of size k with no duplicates using a set.  
Example:  
```
Input: nums = [1, 2, 3, 1], k = 3  
Output: [[1, 2, 3]]
```
<details>
<summary>Solution</summary>

```python
def unique_subarrays_no_duplicates_k(nums, k):
    result = set()
    for i in range(len(nums) - k + 1):
        if len(set(nums[i:i+k])) == k:
            result.add(tuple(nums[i:i+k]))
    return [list(sub) for sub in result]
```

</details>

### 85. Find Maximum Subset with Sum in Range
**Problem**: Write a Python function to find the maximum size subset with sum in a given range using a set.  
Example:  
```
Input: nums = [1, 2, 3, 4], low = 3, high = 5  
Output: 2
```
<details>
<summary>Solution</summary>

```python
def max_subset_sum_in_range(nums, low, high):
    max_size = 0
    for mask in range(1 << len(nums)):
        curr_sum = 0
        curr_set = set()
        for i in range(len(nums)):
            if mask & (1 << i):
                curr_sum += nums[i]
                curr_set.add(nums[i])
        if low <= curr_sum <= high:
            max_size = max(max_size, len(curr_set))
    return max_size
```

</details>

### 86. Find All Unique Subsets with No Pair Sum Equal to Target
**Problem**: Write a Python function to find all unique subsets where no pair sums to a target value using a set.  
Example:  
```
Input: nums = [1, 2, 3], target = 5  
Output: [[1], [2], [3], [1, 2], [1, 3]]
```
<details>
<summary>Solution</summary>

```python
def subsets_no_pair_sum(nums, target):
    result = set()
    for mask in range(1 << len(nums)):
        curr = []
        valid = True
        for i in range(len(nums)):
            if mask & (1 << i):
                for num in curr:
                    if num + nums[i] == target:
                        valid = False
                        break
                if not valid:
                    break
                curr.append(nums[i])
        if valid:
            result.add(tuple(sorted(curr)))
    return [list(subset) for subset in result if subset]
```

</details>

### 87. Find Maximum Subset with No Pair Product Equal to Target
**Problem**: Write a Python function to find the maximum size subset where no pair’s product equals a target value using a set.  
Example:  
```
Input: nums = [1, 2, 3, 4], target = 6  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def max_subset_no_pair_product(nums, target):
    max_size = 0
    for mask in range(1 << len(nums)):
        curr_set = set()
        valid = True
        for i in range(len(nums)):
            if mask & (1 << i):
                for num in curr_set:
                    if num * nums[i] == target:
                        valid = False
                        break
                if not valid:
                    break
                curr_set.add(nums[i])
        if valid:
            max_size = max(max_size, len(curr_set))
    return max_size
```

</details>

### 88. Find All Unique Subarrays with Product in Range
**Problem**: Write a Python function to find all unique subarrays with product in a given range using a set.  
Example:  
```
Input: nums = [1, 2, 3], low = 2, high = 6  
Output: [[1, 2], [1, 3], [2], [3]]
```
<details>
<summary>Solution</summary>

```python
def subarrays_with_product_in_range(nums, low, high):
    result = set()
    for i in range(len(nums)):
        curr_prod = 1
        for j in range(i, len(nums)):
            curr_prod *= nums[j]
            if low <= curr_prod <= high:
                result.add(tuple(nums[i:j+1]))
            if curr_prod > high:
                break
    return [list(sub) for sub in result]
```

</details>

### 89. Find Maximum Subset with No Pair Difference Equal to Target
**Problem**: Write a Python function to find the maximum size subset where no pair’s difference equals a target value using a set.  
Example:  
```
Input: nums = [1, 2, 3, 4], target = 1  
Output: 2
```
<details>
<summary>Solution</summary>

```python
def max_subset_no_pair_diff_target(nums, target):
    max_size = 0
    for mask in range(1 << len(nums)):
        curr_set = set()
        valid = True
        for i in range(len(nums)):
            if mask & (1 << i):
                for num in curr_set:
                    if abs(num - nums[i]) == target:
                        valid = False
                        break
                if not valid:
                    break
                curr_set.add(nums[i])
        if valid:
            max_size = max(max_size, len(curr_set))
    return max_size
```

</details>

### 90. Find All Unique Subsets with No Pair XOR Equal to Target
**Problem**: Write a Python function to find all unique subsets where no pair’s XOR equals a target value using a set.  
Example:  
```
Input: nums = [1, 2, 3], target = 3  
Output: [[1], [2], [3], [1, 2]]
```
<details>
<summary>Solution</summary>

```python
def subsets_no_pair_xor(nums, target):
    result = set()
    for mask in range(1 << len(nums)):
        curr = []
        valid = True
        for i in range(len(nums)):
            if mask & (1 << i):
                for num in curr:
                    if (num ^ nums[i]) == target:
                        valid = False
                        break
                if not valid:
                    break
                curr.append(nums[i])
        if valid:
            result.add(tuple(sorted(curr)))
    return [list(subset) for subset in result if subset]
```

</details>

### 91. Find Maximum Subset with Sum Divisible by K
**Problem**: Write a Python function to find the maximum size subset with sum divisible by k using a set.  
Example:  
```
Input: nums = [4, 3, 2, 7], k = 5  
Output: 4
```
<details>
<summary>Solution</summary>

```python
def max_subset_sum_divisible_k(nums, k):
    remainders = [[] for _ in range(k)]
    for num in nums:
        remainders[num % k].append(num)
    max_size = min(len(remainders[0]), 1)
    for i in range(1, (k + 1) // 2):
        max_size += max(len(remainders[i]), len(remainders[k - i]))
    if k % 2 == 0:
        max_size += min(len(remainders[k // 2]), 1)
    return max_size
```

</details>

### 92. Find All Unique Subarrays with No Pair Sum in Range
**Problem**: Write a Python function to find all unique subarrays where no pair’s sum is in a given range using a set.  
Example:  
```
Input: nums = [1, 2, 3], low = 5, high = 7  
Output: [[1], [2], [3], [1, 2], [2, 3], [1, 2, 3]]
```
<details>
<summary>Solution</summary>

```python
def subarrays_no_pair_sum_in_range(nums, low, high):
    result = set()
    for i in range(len(nums)):
        curr = []
        valid = True
        for j in range(i, len(nums)):
            for num in curr:
                if low <= num + nums[j] <= high:
                    valid = False
                    break
            if not valid:
                break
            curr.append(nums[j])
            result.add(tuple(curr))
    return [list(sub) for sub in result]
```

</details>

### 93. Find Maximum Subset with No Pair Product Divisible by K
**Problem**: Write a Python function to find the maximum size subset where no pair’s product is divisible by k using a set.  
Example:  
```
Input: nums = [1, 2, 3, 4], k = 6  
Output: 4
```
<details>
<summary>Solution</summary>

```python
def max_subset_no_pair_product_divisible(nums, k):
    max_size = 0
    for mask in range(1 << len(nums)):
        curr_set = set()
        valid = True
        for i in range(len(nums)):
            if mask & (1 << i):
                for num in curr_set:
                    if (num * nums[i]) % k == 0:
                        valid = False
                        break
                if not valid:
                    break
                curr_set.add(nums[i])
        if valid:
            max_size = max(max_size, len(curr_set))
    return max_size
```

</details>

### 94. Find All Unique Subsets with No Pair Difference in Range
**Problem**: Write a Python function to find all unique subsets where no pair’s absolute difference is within a given range [low, high] using a set.  
Example:  
```
Input: nums = [1, 2, 3], low = 2, high = 3  
Output: [[1], [2], [3]]
```
<details>
<summary>Solution</summary>

```python
def subsets_no_pair_diff_in_range(nums, low, high):
    result = set()
    for mask in range(1 << len(nums)):
        curr = []
        valid = True
        for i in range(len(nums)):
            if mask & (1 << i):
                for num in curr:
                    diff = abs(nums[i] - num)
                    if low <= diff <= high:
                        valid = False
                        break
                if not valid:
                    break
                curr.append(nums[i])
        if valid and curr:
            result.add(tuple(sorted(curr)))
    return [list(subset) for subset in result]
```

</details>

### 95. Find Maximum Subset with No Pair Sum in Forbidden Set
**Problem**: Write a Python function to find the maximum size subset where no pair’s sum exists in a given forbidden set using a set.  
Example:  
```
Input: nums = [1, 2, 3, 4], forbidden = [5, 7]  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def max_subset_no_pair_sum_forbidden(nums, forbidden):
    forbidden = set(forbidden)
    max_size = 0
    for mask in range(1 << len(nums)):
        curr_set = set()
        valid = True
        for i in range(len(nums)):
            if mask & (1 << i):
                for num in curr_set:
                    if num + nums[i] in forbidden:
                        valid = False
                        break
                if not valid:
                    break
                curr_set.add(nums[i])
        if valid:
            max_size = max(max_size, len(curr_set))
    return max_size
```

</details>

### 96. Find All Unique Subsets with No Pair Product in Forbidden Set
**Problem**: Write a Python function to find all unique subsets where no pair’s product exists in a given forbidden set using a set.  
Example:  
```
Input: nums = [1, 2, 3, 4], forbidden = [6, 8]  
Output: [[1], [2], [3], [4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
```
<details>
<summary>Solution</summary>

```python
def subsets_no_pair_product_forbidden(nums, forbidden):
    forbidden = set(forbidden)
    result = set()
    for mask in range(1 << len(nums)):
        curr = []
        valid = True
        for i in range(len(nums)):
            if mask & (1 << i):
                for num in curr:
                    if num * nums[i] in forbidden:
                        valid = False
                        break
                if not valid:
                    break
                curr.append(nums[i])
        if valid and curr:
            result.add(tuple(sorted(curr)))
    return [list(subset) for subset in result]
```

</details>

### 97. Find Maximum Subset with No Pair XOR in Forbidden Set
**Problem**: Write a Python function to find the maximum size subset where no pair’s XOR exists in a given forbidden set using a set.  
Example:  
```
Input: nums = [1, 2, 3, 4], forbidden = [3, 7]  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def max_subset_no_pair_xor_forbidden(nums, forbidden):
    forbidden = set(forbidden)
    max_size = 0
    for mask in range(1 << len(nums)):
        curr_set = set()
        valid = True
        for i in range(len(nums)):
            if mask & (1 << i):
                for num in curr_set:
                    if (num ^ nums[i]) in forbidden:
                        valid = False
                        break
                if not valid:
                    break
                curr_set.add(nums[i])
        if valid:
            max_size = max(max_size, len(curr_set))
    return max_size
```

</details>

### 98. Find All Unique Subarrays with Exactly K Distinct Elements
**Problem**: Write a Python function to find all unique subarrays with exactly k distinct elements using a sliding window and a set.  
Example:  
```
Input: nums = [1, 2, 1, 2, 3], k = 2  
Output: [[1, 2], [2, 1], [1, 2, 1], [2, 1, 2], [2, 3]]
```
<details>
<summary>Solution</summary>

```python
from collections import Counter
def subarrays_with_k_distinct(nums, k):
    result = set()
    for i in range(len(nums)):
        count = Counter()
        distinct = 0
        for j in range(i, len(nums)):
            if count[nums[j]] == 0:
                distinct += 1
            count[nums[j]] += 1
            if distinct == k:
                result.add(tuple(nums[i:j+1]))
            elif distinct > k:
                break
    return [list(sub) for sub in result]
```

</details>

### 99. Find Maximum Subset with No Pair Difference Divisible by K
**Problem**: Write a Python function to find the maximum size subset where no pair’s absolute difference is divisible by k using a set.  
Example:  
```
Input: nums = [1, 2, 3, 4], k = 2  
Output: 2
```
<details>
<summary>Solution</summary>

```python
def max_subset_no_pair_diff_divisible(nums, k):
    max_size = 0
    for mask in range(1 << len(nums)):
        curr_set = set()
        valid = True
        for i in range(len(nums)):
            if mask & (1 << i):
                for num in curr_set:
                    if abs(num - nums[i]) % k == 0:
                        valid = False
                        break
                if not valid:
                    break
                curr_set.add(nums[i])
        if valid:
            max_size = max(max_size, len(curr_set))
    return max_size
```

</details>

### 100. Find All Unique Subsets with No Pair Sum Divisible by K
**Problem**: Write a Python function to find all unique subsets where no pair’s sum is divisible by k using a set.  
Example:  
```
Input: nums = [1, 2, 3], k = 5  
Output: [[1], [2], [3], [1, 2], [1, 3], [2, 3]]
```
<details>
<summary>Solution</summary>

```python
def subsets_no_pair_sum_divisible(nums, k):
    result = set()
    for mask in range(1 << len(nums)):
        curr = []
        valid = True
        for i in range(len(nums)):
            if mask & (1 << i):
                for num in curr:
                    if (num + nums[i]) % k == 0:
                        valid = False
                        break
                if not valid:
                    break
                curr.append(nums[i])
        if valid and curr:
            result.add(tuple(sorted(curr)))
    return [list(subset) for subset in result]
```

</details>