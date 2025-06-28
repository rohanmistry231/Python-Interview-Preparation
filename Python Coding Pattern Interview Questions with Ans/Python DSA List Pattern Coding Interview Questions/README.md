# Python List DSA Patterns Interview Questions

This README provides **100 Python list manipulation questions** designed for AI/ML students preparing for technical interviews. The questions focus on list-specific problems, emphasizing Data Structures and Algorithms (DSA) patterns such as two pointers, sliding windows, prefix sums, binary search, and Pythonic idioms like slicing and list comprehensions. They are categorized into **Basic**, **Intermediate**, and **Advanced** levels, covering operations like reversals, rotations, sublist sums, and complex algorithms tailored to Python's list features. Each question includes a problem statement, with the solution hidden in a `<details>` tag to encourage users to attempt the problem before viewing the answer. This format supports hands-on practice and aligns with interview preparation for AI/ML roles, focusing on list-specific DSA patterns.

## Basic List Questions

### 1. Reverse a List Using Slicing
**Problem**: Write a Python function to reverse a list using Python's slicing feature.  
Example:  
```
Input: [1, 2, 3, 4, 5]  
Output: [5, 4, 3, 2, 1]
```
<details>
<summary>Solution</summary>

```python
def reverse_list(lst):
    return lst[::-1]
```

</details>

### 2. Find Maximum Element with Index
**Problem**: Write a Python function to find the maximum element in a list and its index.  
Example:  
```
Input: [3, 7, 2, 9, 1]  
Output: (9, 3)
```
<details>
<summary>Solution</summary>

```python
def find_max_with_index(lst):
    if not lst:
        return None
    max_val = max(lst)
    return (max_val, lst.index(max_val))
```

</details>

### 3. Filter Even Numbers
**Problem**: Write a Python function to create a new list containing only even numbers using a list comprehension.  
Example:  
```
Input: [1, 2, 3, 4, 5, 6]  
Output: [2, 4, 6]
```
<details>
<summary>Solution</summary>

```python
def filter_evens(lst):
    return [x for x in lst if x % 2 == 0]
```

</details>

### 4. Sum of List Using Reduce
**Problem**: Write a Python function to calculate the sum of all elements in a list using `functools.reduce`.  
Example:  
```
Input: [1, 2, 3, 4]  
Output: 10
```
<details>
<summary>Solution</summary>

```python
from functools import reduce
def list_sum(lst):
    return reduce(lambda x, y: x + y, lst, 0)
```

</details>

### 5. Check if List is Sorted Ascending
**Problem**: Write a Python function to check if a list is sorted in ascending order using a single pass.  
Example:  
```
Input: [1, 2, 3, 4, 5]  
Output: True
```
<details>
<summary>Solution</summary>

```python
def is_sorted_ascending(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```

</details>

### 6. Rotate List Left by K
**Problem**: Write a Python function to rotate a list left by k positions using slicing.  
Example:  
```
Input: lst = [1, 2, 3, 4, 5], k = 2  
Output: [3, 4, 5, 1, 2]
```
<details>
<summary>Solution</summary>

```python
def rotate_left(lst, k):
    k = k % len(lst)
    return lst[k:] + lst[:k]
```

</details>

### 7. Rotate List Right by K
**Problem**: Write a Python function to rotate a list right by k positions using slicing.  
Example:  
```
Input: lst = [1, 2, 3, 4, 5], k = 2  
Output: [4, 5, 1, 2, 3]
```
<details>
<summary>Solution</summary>

```python
def rotate_right(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]
```

</details>

### 8. Find Second Smallest Element
**Problem**: Write a Python function to find the second smallest element in a list.  
Example:  
```
Input: [3, 7, 2, 9, 1]  
Output: 2
```
<details>
<summary>Solution</summary>

```python
def second_smallest(lst):
    if len(lst) < 2:
        return None
    min1 = min2 = float('inf')
    for num in lst:
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2 and num != min1:
            min2 = num
    return min2 if min2 != float('inf') else None
```

</details>

### 9. Remove Duplicates from Unsorted List
**Problem**: Write a Python function to remove duplicates from an unsorted list using a set.  
Example:  
```
Input: [1, 3, 3, 2, 1]  
Output: [1, 3, 2]
```
<details>
<summary>Solution</summary>

```python
def remove_duplicates_unsorted(lst):
    return list(dict.fromkeys(lst))
```

</details>

### 10. Move Non-Zero Elements to Front
**Problem**: Write a Python function to move all non-zero elements to the front of a list, maintaining their relative order.  
Example:  
```
Input: [0, 1, 0, 3, 12]  
Output: [1, 3, 12, 0, 0]
```
<details>
<summary>Solution</summary>

```python
def move_non_zeros(lst):
    non_zero_pos = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            lst[non_zero_pos], lst[i] = lst[i], lst[non_zero_pos]
            non_zero_pos += 1
    return lst
```

</details>

### 11. Find First Missing Positive Integer
**Problem**: Write a Python function to find the first missing positive integer in a list.  
Example:  
```
Input: [3, 4, -1, 1]  
Output: 2
```
<details>
<summary>Solution</summary>

```python
def first_missing_positive(lst):
    n = len(lst)
    for i in range(n):
        while 1 <= lst[i] <= n and lst[lst[i] - 1] != lst[i]:
            lst[lst[i] - 1], lst[i] = lst[i], lst[lst[i] - 1]
    for i in range(n):
        if lst[i] != i + 1:
            return i + 1
    return n + 1
```

</details>

### 12. Find Pair with Target Sum
**Problem**: Write a Python function to find indices of two numbers in a list that sum to a target using a dictionary.  
Example:  
```
Input: lst = [2, 7, 11, 15], target = 9  
Output: [0, 1]
```
<details>
<summary>Solution</summary>

```python
def two_sum(lst, target):
    seen = {}
    for i, num in enumerate(lst):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []
```

</details>

### 13. Check for Duplicates Using Set
**Problem**: Write a Python function to check if a list contains duplicates using a set.  
Example:  
```
Input: [1, 2, 3, 1]  
Output: True
```
<details>
<summary>Solution</summary>

```python
def has_duplicates(lst):
    return len(lst) != len(set(lst))
```

</details>

### 14. Find Range of Target in Sorted List
**Problem**: Write a Python function to find the starting and ending indices of a target value in a sorted list using binary search.  
Example:  
```
Input: lst = [5, 7, 7, 8, 8, 10], target = 8  
Output: [3, 4]
```
<details>
<summary>Solution</summary>

```python
def search_range(lst, target):
    def binary_search(lst, target, left_bias):
        left, right = 0, len(lst) - 1
        i = -1
        while left <= right:
            mid = (left + right) // 2
            if target < lst[mid]:
                right = mid - 1
            elif target > lst[mid]:
                left = mid + 1
            else:
                i = mid
                if left_bias:
                    right = mid - 1
                else:
                    left = mid + 1
        return i
    
    return [binary_search(lst, target, True), binary_search(lst, target, False)]
```

</details>

### 15. Merge Two Sorted Lists
**Problem**: Write a Python function to merge two sorted lists into a single sorted list.  
Example:  
```
Input: lst1 = [1, 3, 5], lst2 = [2, 4, 6]  
Output: [1, 2, 3, 4, 5, 6]
```
<details>
<summary>Solution</summary>

```python
def merge_sorted_lists(lst1, lst2):
    result = []
    i = j = 0
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
```

</details>

### 16. Find Element in Rotated Sorted List
**Problem**: Write a Python function to find an element in a rotated sorted list using binary search.  
Example:  
```
Input: lst = [4, 5, 6, 7, 0, 1, 2], target = 0  
Output: 4
```
<details>
<summary>Solution</summary>

```python
def search_rotated_list(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        if lst[left] <= lst[mid]:
            if lst[left] <= target < lst[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if lst[mid] < target <= lst[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
```

</details>

### 17. Find Peak Element
**Problem**: Write a Python function to find a peak element (greater than its neighbors) in a list using binary search.  
Example:  
```
Input: [1, 2, 3, 1]  
Output: 2
```
<details>
<summary>Solution</summary>

```python
def find_peak_element(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        mid = (left + right) // 2
        if lst[mid] > lst[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left
```

</details>

### 18. Remove All Instances of Value
**Problem**: Write a Python function to remove all instances of a value in a list in-place and return the new length.  
Example:  
```
Input: lst = [3, 2, 2, 3], val = 3  
Output: 2, lst = [2, 2, _, _]
```
<details>
<summary>Solution</summary>

```python
def remove_element(lst, val):
    write_index = 0
    for i in range(len(lst)):
        if lst[i] != val:
            lst[write_index] = lst[i]
            write_index += 1
    return write_index
```

</details>

### 19. Find Kth Largest Element
**Problem**: Write a Python function to find the kth largest element in a list using sorting.  
Example:  
```
Input: lst = [3, 2, 1, 5, 6, 4], k = 2  
Output: 5
```
<details>
<summary>Solution</summary>

```python
def find_kth_largest(lst, k):
    return sorted(lst, reverse=True)[k-1]
```

</details>

### 20. Find Common Elements in Two Lists
**Problem**: Write a Python function to find common elements in two lists using sets.  
Example:  
```
Input: lst1 = [1, 2, 3], lst2 = [2, 3, 4]  
Output: [2, 3]
```
<details>
<summary>Solution</summary>

```python
def find_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))
```

</details>

### 21. Find Majority Element
**Problem**: Write a Python function to find the majority element (appears more than n/2 times) using Boyer-Moore voting.  
Example:  
```
Input: [3, 2, 3]  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def majority_element(lst):
    candidate = lst[0]
    count = 1
    for num in lst[1:]:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate
```

</details>

### 22. Find First Missing Positive
**Problem**: Write a Python function to find the first missing positive integer in a list using in-place swapping.  
Example:  
```
Input: [1, 2, 0]  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def first_missing_positive(lst):
    n = len(lst)
    for i in range(n):
        while 1 <= lst[i] <= n and lst[lst[i] - 1] != lst[i]:
            lst[lst[i] - 1], lst[i] = lst[i], lst[lst[i] - 1]
    for i in range(n):
        if lst[i] != i + 1:
            return i + 1
    return n + 1
```

</details>

### 23. Merge Intervals in List
**Problem**: Write a Python function to merge overlapping intervals in a list of intervals.  
Example:  
```
Input: [[1,3], [2,6], [8,10], [15,18]]  
Output: [[1,6], [8,10], [15,18]]
```
<details>
<summary>Solution</summary>

```python
def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]
    for curr in intervals[1:]:
        if curr[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], curr[1])
        else:
            result.append(curr)
    return result
```

</details>

### 24. Product of List Except Self
**Problem**: Write a Python function to return a list where each element is the product of all other elements.  
Example:  
```
Input: [1, 2, 3, 4]  
Output: [24, 12, 8, 6]
```
<details>
<summary>Solution</summary>

```python
def product_except_self(lst):
    n = len(lst)
    result = [1] * n
    left_product = 1
    for i in range(n):
        result[i] *= left_product
        left_product *= lst[i]
    right_product = 1
    for i in range(n-1, -1, -1):
        result[i] *= right_product
        right_product *= lst[i]
    return result
```

</details>

### 25. Find Duplicate Number
**Problem**: Write a Python function to find the duplicate number in a list of n+1 integers from 1 to n using Floyd's cycle detection.  
Example:  
```
Input: [1, 3, 4, 2, 2]  
Output: 2
```
<details>
<summary>Solution</summary>

```python
def find_duplicate(lst):
    slow = fast = lst[0]
    while True:
        slow = lst[slow]
        fast = lst[lst[fast]]
        if slow == fast:
            break
    slow = lst[0]
    while slow != fast:
        slow = lst[slow]
        fast = lst[fast]
    return slow
```

</details>

### 26. Two Sum in Sorted List
**Problem**: Write a Python function to find two numbers in a sorted list that sum to a target, returning their 1-based indices using two pointers.  
Example:  
```
Input: numbers = [2, 7, 11, 15], target = 9  
Output: [1, 2]
```
<details>
<summary>Solution</summary>

```python
def two_sum_sorted(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        curr_sum = numbers[left] + numbers[right]
        if curr_sum == target:
            return [left + 1, right + 1]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []
```

</details>

### 27. Maximum Subarray Sum
**Problem**: Write a Python function to find the maximum sum of a contiguous subarray using Kadane's algorithm.  
Example:  
```
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]  
Output: 6
```
<details>
<summary>Solution</summary>

```python
def max_subarray_sum(lst):
    max_so_far = max_ending_here = lst[0]
    for num in lst[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
```

</details>

### 28. Find Minimum in Rotated Sorted List
**Problem**: Write a Python function to find the minimum element in a rotated sorted list using binary search.  
Example:  
```
Input: [4, 5, 6, 7, 0, 1, 2]  
Output: 0
```
<details>
<summary>Solution</summary>

```python
def find_min_rotated(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        mid = (left + right) // 2
        if lst[mid] > lst[right]:
            left = mid + 1
        else:
            right = mid
    return lst[left]
```

</details>

### 29. Sort List by Parity
**Problem**: Write a Python function to move all even numbers to the front of a list, followed by odd numbers using two pointers.  
Example:  
```
Input: [3, 1, 2, 4]  
Output: [2, 4, 3, 1]
```
<details>
<summary>Solution</summary>

```python
def sort_by_parity(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        while left < right and lst[left] % 2 == 0:
            left += 1
        while left < right and lst[right] % 2 == 1:
            right -= 1
        lst[left], lst[right] = lst[right], lst[left]
    return lst
```

</details>

### 30. Find K Closest Elements
**Problem**: Write a Python function to find k closest elements to a target value in a sorted list using binary search.  
Example:  
```
Input: lst = [1, 2, 3, 4, 5], k = 4, x = 3  
Output: [1, 2, 3, 4]
```
<details>
<summary>Solution</summary>

```python
def find_k_closest(lst, k, x):
    left, right = 0, len(lst) - k
    while left < right:
        mid = (left + right) // 2
        if x - lst[mid] > lst[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    return lst[left:left + k]
```

</details>

### 31. Find Intersection of Two Lists with Duplicates
**Problem**: Write a Python function to find the intersection of two lists, including duplicates, using a dictionary.  
Example:  
```
Input: lst1 = [1, 2, 2, 1], lst2 = [2, 2]  
Output: [2, 2]
```
<details>
<summary>Solution</summary>

```python
def intersect_lists(lst1, lst2):
    count = {}
    for num in lst1:
        count[num] = count.get(num, 0) + 1
    result = []
    for num in lst2:
        if num in count and count[num] > 0:
            result.append(num)
            count[num] -= 1
    return result
```

</details>

### 32. Find Single Number
**Problem**: Write a Python function to find the number that appears exactly once in a list where every other number appears twice using XOR.  
Example:  
```
Input: [4, 1, 2, 1, 2]  
Output: 4
```
<details>
<summary>Solution</summary>

```python
def single_number(lst):
    result = 0
    for num in lst:
        result ^= num
    return result
```

</details>

### 33. Find Maximum Product Subarray
**Problem**: Write a Python function to find the maximum product of a contiguous subarray.  
Example:  
```
Input: [2, 3, -2, 4]  
Output: 6
```
<details>
<summary>Solution</summary>

```python
def max_product_subarray(lst):
    max_so_far = max_ending_here = min_ending_here = lst[0]
    for num in lst[1:]:
        temp = max_ending_here
        max_ending_here = max(num, max_ending_here * num, min_ending_here * num)
        min_ending_here = min(num, temp * num, min_ending_here * num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
```

</details>

### 34. Find Next Greater Element
**Problem**: Write a Python function to find the next greater element for each element in a list using a stack.  
Example:  
```
Input: [1, 3, 2, 4]  
Output: [3, 4, 4, -1]
```
<details>
<summary>Solution</summary>

```python
def next_greater_element(lst):
    stack = []
    result = [-1] * len(lst)
    for i in range(len(lst)):
        while stack and lst[stack[-1]] < lst[i]:
            result[stack.pop()] = lst[i]
        stack.append(i)
    return result
```

</details>

## Intermediate List Questions

### 35. Three Sum
**Problem**: Write a Python function to find all unique triplets in a list that sum to zero using two pointers.  
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
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            if curr_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif curr_sum < 0:
                left += 1
            else:
                right -= 1
    return result
```

</details>

### 36. Four Sum
**Problem**: Write a Python function to find all unique quadruplets in a list that sum to a target.  
Example:  
```
Input: nums = [1, 0, -1, 0, -2, 2], target = 0  
Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
```
<details>
<summary>Solution</summary>

```python
def four_sum(nums, target):
    nums.sort()
    result = []
    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            left, right = j + 1, len(nums) - 1
            while left < right:
                curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if curr_sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1
    return result
```

</details>

### 37. Subarray Sum Equals K
**Problem**: Write a Python function to find the total number of subarrays with sum equal to k using prefix sums.  
Example:  
```
Input: nums = [1, 1, 1], k = 2  
Output: 2
```
<details>
<summary>Solution</summary>

```python
def subarray_sum(nums, k):
    count = 0
    curr_sum = 0
    prefix_sums = {0: 1}
    for num in nums:
        curr_sum += num
        count += prefix_sums.get(curr_sum - k, 0)
        prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
    return count
```

</details>

### 38. Container With Most Water
**Problem**: Write a Python function to find two lines that form a container with the most water using two pointers.  
Example:  
```
Input: [1, 8, 6, 2, 5, 4, 8, 3, 7]  
Output: 49
```
<details>
<summary>Solution</summary>

```python
def max_area(height):
    max_water = 0
    left, right = 0, len(height) - 1
    while left < right:
        max_water = max(max_water, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water
```

</details>

### 39. Trapping Rain Water
**Problem**: Write a Python function to compute how much water can be trapped in a list of heights using two pointers.  
Example:  
```
Input: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]  
Output: 6
```
<details>
<summary>Solution</summary>

```python
def trap_rain_water(height):
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max = right_max = water = 0
    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            water += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            water += right_max - height[right]
            right -= 1
    return water
```

</details>

### 40. Merge K Sorted Lists
**Problem**: Write a Python function to merge k sorted lists into one sorted list using a min-heap.  
Example:  
```
Input: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]  
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
<details>
<summary>Solution</summary>

```python
from heapq import heappush, heappop
def merge_k_sorted_lists(lists):
    result = []
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heappush(heap, (lst[0], i, 0))
    while heap:
        val, lst_idx, idx = heappop(heap)
        result.append(val)
        if idx + 1 < len(lists[lst_idx]):
            heappush(heap, (lists[lst_idx][idx + 1], lst_idx, idx + 1))
    return result
```

</details>

### 41. Find Median of Two Sorted Lists
**Problem**: Write a Python function to find the median of two sorted lists using binary search.  
Example:  
```
Input: nums1 = [1, 3], nums2 = [2]  
Output: 2.0
```
<details>
<summary>Solution</summary>

```python
def find_median_sorted_lists(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    x, y = len(nums1), len(nums2)
    left, right = 0, x
    while left <= right:
        partition_x = (left + right) // 2
        partition_y = (x + y + 1) // 2 - partition_x
        max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
        min_right_x = float('inf') if partition_x == x else nums1[partition_x]
        max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
        min_right_y = float('inf') if partition_y == y else nums2[partition_y]
        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            if (x + y) % 2 == 0:
                return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
            else:
                return max(max_left_x, max_left_y)
        elif max_left_x > min_right_y:
            right = partition_x - 1
        else:
            left = partition_x + 1
```

</details>

### 42. Maximum Points on a Line
**Problem**: Write a Python function to find the maximum number of points that lie on the same straight line.  
Example:  
```
Input: [[1,1], [2,2], [3,3]]  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def max_points(points):
    if not points:
        return 0
    max_count = 1
    for i in range(len(points)):
        slopes = {}
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if x1 == x2:
                slope = float('inf')
            else:
                slope = (y2 - y1) / (x2 - x1)
            slopes[slope] = slopes.get(slope, 0) + 1
            max_count = max(max_count, slopes[slope] + 1)
    return max_count
```

</details>

### 43. Spiral Matrix
**Problem**: Write a Python function to print all elements of a matrix (list of lists) in spiral order.  
Example:  
```
Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
```
<details>
<summary>Solution</summary>

```python
def spiral_order(matrix):
    if not matrix:
        return []
    result = []
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    return result
```

</details>

### 44. Rotate Matrix
**Problem**: Write a Python function to rotate an n x n matrix (list of lists) by 90 degrees clockwise in-place.  
Example:  
```
Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  
Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```
<details>
<summary>Solution</summary>

```python
def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
    return matrix
```

</details>

### 45. Set Matrix Zeroes
**Problem**: Write a Python function to set entire row and column to zero in a matrix (list of lists) if an element is zero.  
Example:  
```
Input: [[1, 1, 1], [1, 0, 1], [1, 1, 1]]  
Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
```
<details>
<summary>Solution</summary>

```python
def set_zeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_zero = any(matrix[i][0] == 0 for i in range(m))
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0
    for i in range(1, m):
        if matrix[i][0] == 0:
            for j in range(1, n):
                matrix[i][j] = 0
    for j in range(1, n):
        if matrix[0][j] == 0:
            for i in range(1, m):
                matrix[i][j] = 0
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0
    return matrix
```

</details>

### 46. Search 2D Matrix
**Problem**: Write a Python function to search for a value in an m x n matrix (list of lists) where rows and columns are sorted.  
Example:  
```
Input: matrix = [[1, 3, 5], [10, 11, 16], [23, 30, 34]], target = 3  
Output: True
```
<details>
<summary>Solution</summary>

```python
def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    while left <= right:
        mid = (left + right) // 2
        row, col = mid // n, mid % n
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
```

</details>

### 47. Find K Pairs with Smallest Sums
**Problem**: Write a Python function to find k pairs with smallest sums from two sorted lists using a min-heap.  
Example:  
```
Input: nums1 = [1, 7, 11], nums2 = [2, 4, 6], k = 3  
Output: [[1, 2], [1, 4], [1, 6]]
```
<details>
<summary>Solution</summary>

```python
from heapq import heappush, heappop
def k_smallest_pairs(nums1, nums2, k):
    if not nums1 or not nums2:
        return []
    heap = []
    result = []
    heappush(heap, (nums1[0] + nums2[0], 0, 0))
    seen = {(0, 0)}
    while k > 0 and heap:
        _, i, j = heappop(heap)
        result.append([nums1[i], nums2[j]])
        if i + 1 < len(nums1) and (i + 1, j) not in seen:
            heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
            seen.add((i + 1, j))
        if j + 1 < len(nums2) and (i, j + 1) not in seen:
            heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            seen.add((i, j + 1))
        k -= 1
    return result
```

</details>

### 48. Count Duplicate Sublists
**Problem**: Write a Python function to count the number of duplicate sublists of length k in a list.  
Example:  
```
Input: lst = [1, 2, 3, 2, 3], k = 2  
Output: 1
```
<details>
<summary>Solution</summary>

```python
def count_duplicate_sublists(lst, k):
    seen = {}
    count = 0
    for i in range(len(lst) - k + 1):
        sublist = tuple(lst[i:i+k])
        seen[sublist] = seen.get(sublist, 0) + 1
        if seen[sublist] == 2:
            count += 1
    return count
```

</details>

### 49. Longest Consecutive Sequence
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

### 50. Maximum Circular Subarray Sum
**Problem**: Write a Python function to find the maximum sum of a circular subarray using Kadane's algorithm.  
Example:  
```
Input: [1, -2, 3, -2]  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def max_circular_subarray_sum(lst):
    def kadane(lst):
        max_so_far = max_ending_here = lst[0]
        for num in lst[1:]:
            max_ending_here = max(num, max_ending_here + num)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
    
    max_linear = kadane(lst)
    if max_linear < 0:
        return max_linear
    array_sum = sum(lst)
    max_circular = array_sum + kadane([-x for x in lst])
    return max(max_linear, max_circular)
```

</details>

### 51. Kth Smallest in Two Sorted Lists
**Problem**: Write a Python function to find the kth smallest element in two sorted lists using binary search.  
Example:  
```
Input: nums1 = [1, 3], nums2 = [2], k = 2  
Output: 2
```
<details>
<summary>Solution</summary>

```python
def kth_smallest(nums1, nums2, k):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    x, y = len(nums1), len(nums2)
    left, right = 0, x
    while left <= right:
        partition_x = (left + right) // 2
        partition_y = k - partition_x
        max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
        min_right_x = float('inf') if partition_x == x else nums1[partition_x]
        max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
        min_right_y = float('inf') if partition_y == y else nums2[partition_y]
        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            return max(max_left_x, max_left_y)
        elif max_left_x > min_right_y:
            right = partition_x - 1
        else:
            left = partition_x + 1
```

</details>

### 52. Maximum Average Subarray
**Problem**: Write a Python function to find the maximum average of a subarray of size k using sliding window.  
Example:  
```
Input: nums = [1, 12, -5, -6, 50, 3], k = 4  
Output: 12.75
```
<details>
<summary>Solution</summary>

```python
def max_average_subarray(nums, k):
    curr_sum = sum(nums[:k])
    max_sum = curr_sum
    for i in range(k, len(nums)):
        curr_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, curr_sum)
    return max_sum / k
```

</details>

### 53. Subarray with Given Sum
**Problem**: Write a Python function to find a contiguous subarray with a given sum in a non-negative list using sliding window.  
Example:  
```
Input: nums = [1, 4, 20, 3, 10, 5], sum = 33  
Output: [2, 4]
```
<details>
<summary>Solution</summary>

```python
def subarray_with_sum(nums, target):
    curr_sum = 0
    left = 0
    for right in range(len(nums)):
        curr_sum += nums[right]
        while curr_sum > target and left <= right:
            curr_sum -= nums[left]
            left += 1
        if curr_sum == target:
            return [left, right]
    return []
```

</details>

### 54. Minimum Size Subarray Sum
**Problem**: Write a Python function to find the minimal length of a contiguous subarray with sum >= target using sliding window.  
Example:  
```
Input: nums = [2, 3, 1, 2, 4, 3], target = 7  
Output: 2
```
<details>
<summary>Solution</summary>

```python
def min_subarray_len(nums, target):
    if not nums:
        return 0
    min_len = float('inf')
    curr_sum = 0
    left = 0
    for right in range(len(nums)):
        curr_sum += nums[right]
        while curr_sum >= target:
            min_len = min(min_len, right - left + 1)
            curr_sum -= nums[left]
            left += 1
    return min_len if min_len != float('inf') else 0
```

</details>

### 55. Largest Sum of K Elements
**Problem**: Write a Python function to find the largest sum of k elements in a list using sorting.  
Example:  
```
Input: lst = [4, 2, 1, 7, 5], k = 3  
Output: 16
```
<details>
<summary>Solution</summary>

```python
def max_sum_k_elements(lst, k):
    return sum(sorted(lst, reverse=True)[:k])
```

</details>

### 56. Smallest Missing Positive Integer
**Problem**: Write a Python function to find the smallest missing positive integer in a list using in-place swapping.  
Example:  
```
Input: [3, 4, -1, 1]  
Output: 2
```
<details>
<summary>Solution</summary>

```python
def smallest_missing_positive(lst):
    n = len(lst)
    for i in range(n):
        while 1 <= lst[i] <= n and lst[lst[i] - 1] != lst[i]:
            lst[lst[i] - 1], lst[i] = lst[i], lst[lst[i] - 1]
    for i in range(n):
        if lst[i] != i + 1:
            return i + 1
    return n + 1
```

</details>

### 57. Maximum Difference
**Problem**: Write a Python function to find the maximum difference between any two elements where the larger element appears after the smaller one.  
Example:  
```
Input: [7, 1, 5, 4]  
Output: 4
```
<details>
<summary>Solution</summary>

```python
def max_difference(lst):
    min_element = lst[0]
    max_diff = 0
    for num in lst[1:]:
        if num < min_element:
            min_element = num
        else:
            max_diff = max(max_diff, num - min_element)
    return max_diff
```

</details>

### 58. Longest Increasing Subsequence
**Problem**: Write a Python function to find the length of the longest increasing subsequence in a list using dynamic programming.  
Example:  
```
Input: [10, 9, 2, 5, 3, 7, 101, 18]  
Output: 4
```
<details>
<summary>Solution</summary>

```python
def length_of_LIS(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

</details>

### 59. Largest Rectangle in Histogram
**Problem**: Write a Python function to find the largest rectangle area in a histogram (list of heights) using a stack.  
Example:  
```
Input: [2, 1, 5, 6, 2, 3]  
Output: 10
```
<details>
<summary>Solution</summary>

```python
def largest_rectangle_area(heights):
    stack = [-1]
    max_area = 0
    heights.append(0)
    for i in range(len(heights)):
        while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    return max_area
```

</details>

### 60. Maximum Square
**Problem**: Write a Python function to find the size of the largest square sub-matrix with all 1s in a matrix (list of lists).  
Example:  
```
Input: [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]  
Output: 4
```
<details>
<summary>Solution</summary>

```python
def maximal_square(matrix):
    if not matrix or not matrix[0]:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_side = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if matrix[i-1][j-1] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])
    return max_side * max_side
```

</details>

### 61. Kth Largest Element Using Heap
**Problem**: Write a Python function to find the kth largest element in a list using a min-heap.  
Example:  
```
Input: nums = [3, 2, 1, 5, 6, 4], k = 2  
Output: 5
```
<details>
<summary>Solution</summary>

```python
from heapq import heappush, heappop
def find_kth_largest_heap(nums, k):
    heap = []
    for num in nums:
        heappush(heap, num)
        if len(heap) > k:
            heappop(heap)
    return heappop(heap)
```

</details>

### 62. Smallest Range Covering Elements
**Problem**: Write a Python function to find the smallest range that includes at least one number from each of k sorted lists using a min-heap.  
Example:  
```
Input: nums = [[4, 10, 15], [1, 5, 9], [3, 12, 16]]  
Output: [4, 5]
```
<details>
<summary>Solution</summary>

```python
from heapq import heappush, heappop
def smallest_range(nums):
    heap = []
    max_val = float('-inf')
    for i, lst in enumerate(nums):
        heappush(heap, (lst[0], i, 0))
        max_val = max(max_val, lst[0])
    min_range = [heap[0][0], max_val]
    range_len = max_val - heap[0][0]
    while True:
        min_val, lst_idx, idx = heappop(heap)
        if idx + 1 == len(nums[lst_idx]):
            break
        next_val = nums[lst_idx][idx + 1]
        heappush(heap, (next_val, lst_idx, idx + 1))
        max_val = max(max_val, next_val)
        if max_val - heap[0][0] < range_len:
            min_range = [heap[0][0], max_val]
            range_len = max_val - heap[0][0]
    return min_range
```

</details>

### 63. Maximum Gap
**Problem**: Write a Python function to find the maximum gap between any two consecutive elements in a sorted list.  
Example:  
```
Input: [3, 6, 9, 1]  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def maximum_gap(nums):
    if len(nums) < 2:
        return 0
    nums.sort()
    max_gap = 0
    for i in range(1, len(nums)):
        max_gap = max(max_gap, nums[i] - nums[i-1])
    return max_gap
```

</details>

### 64. Find Missing Ranges
**Problem**: Write a Python function to find all missing ranges in a list of integers from lower to upper.  
Example:  
```
Input: nums = [0, 1, 3, 50, 75], lower = 0, upper = 99  
Output: [[2, 2], [4, 49], [51, 74], [76, 99]]
```
<details>
<summary>Solution</summary>

```python
def find_missing_ranges(nums, lower, upper):
    result = []
    prev = lower - 1
    for num in nums + [upper + 1]:
        if num - prev > 1:
            result.append([prev + 1, num - 1])
        prev = num
    return result
```

</details>

### 65. Kth Smallest Pair Distance
**Problem**: Write a Python function to find the kth smallest distance among all pairs in a list using binary search.  
Example:  
```
Input: nums = [1, 3, 1], k = 1  
Output: 0
```
<details>
<summary>Solution</summary>

```python
def smallest_distance_pair(nums, k):
    nums.sort()
    left, right = 0, nums[-1] - nums[0]
    while left < right:
        mid = (left + right) // 2
        count = 0
        j = 0
        for i in range(len(nums)):
            while j < len(nums) and nums[j] - nums[i] <= mid:
                j += 1
            count += j - i - 1
        if count < k:
            left = mid + 1
        else:
            right = mid
    return left
```

</details>

### 66. K Empty Slots
**Problem**: Write a Python function to find the day when there are k empty slots between two bloomed flowers.  
Example:  
```
Input: flowers = [1, 3, 2], k = 1  
Output: 2
```
<details>
<summary>Solution</summary>

```python
def k_empty_slots(flowers, k):
    days = [0] * len(flowers)
    for day, pos in enumerate(flowers, 1):
        days[pos - 1] = day
    left, right = 0, k + 1
    result = float('inf')
    for i in range(len(days) - k - 1):
        valid = True
        for j in range(left + 1, right):
            if days[j] < days[left] or days[j] < days[right]:
                valid = False
                break
        if valid:
            result = min(result, max(days[left], days[right]))
        left += 1
        right += 1
    return result if result != float('inf') else -1
```

</details>

## Advanced List Questions

### 67. Median in Data Stream
**Problem**: Write a Python class to find the median of a data stream using two heaps.  
Example:  
```
Input: addNum(1), addNum(2), findMedian()  
Output: 1.5
```
<details>
<summary>Solution</summary>

```python
from heapq import heappush, heappop
class MedianFinder:
    def __init__(self):
        self.small = []  # max heap
        self.large = []  # min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))
        if self.small and self.large and -self.small[0] > self.large[0]:
            heappush(self.large, -heappop(self.small))
            heappush(self.small, -heappop(self.large))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        return float(self.large[0])
```

</details>

### 68. K Closest Points to Origin
**Problem**: Write a Python function to find the k closest points to the origin (0, 0) in a 2D plane using a max-heap.  
Example:  
```
Input: points = [[1,3],[-2,2]], k = 1  
Output: [[-2,2]]
```
<details>
<summary>Solution</summary>

```python
from heapq import heappush, heappop
def k_closest_points(points, k):
    heap = []
    for x, y in points:
        dist = x*x + y*y
        heappush(heap, (-dist, x, y))
        if len(heap) > k:
            heappop(heap)
    return [[x, y] for _, x, y in heap]
```

</details>

### 69. Minimum Time to Finish Jobs
**Problem**: Write a Python function to find the minimum time to finish all jobs with k workers using backtracking.  
Example:  
```
Input: jobs = [3, 2, 3], k = 3  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def minimum_time(jobs, k):
    def can_finish(max_time, k, jobs, curr):
        if curr == len(jobs):
            return True
        for i in range(k):
            if workers[i] + jobs[curr] <= max_time:
                workers[i] += jobs[curr]
                if can_finish(max_time, k, jobs, curr + 1):
                    return True
                workers[i] -= jobs[curr]
            if workers[i] == 0:
                break
        return False

    left, right = max(jobs), sum(jobs)
    while left < right:
        mid = (left + right) // 2
        workers = [0] * k
        if can_finish(mid, k, sorted(jobs, reverse=True), 0):
            right = mid
        else:
            left = mid + 1
    return left
```

</details>

### 70. Maximum Profit with K Transactions
**Problem**: Write a Python function to find the maximum profit with at most k transactions in stock prices using dynamic programming.  
Example:  
```
Input: prices = [3, 2, 6, 5, 0, 3], k = 2  
Output: 7
```
<details>
<summary>Solution</summary>

```python
def max_profit_k_transactions(prices, k):
    if not prices or k == 0:
        return 0
    n = len(prices)
    if k >= n // 2:
        profit = 0
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
    dp = [[0] * n for _ in range(k + 1)]
    for i in range(1, k + 1):
        max_diff = -prices[0]
        for j in range(1, n):
            dp[i][j] = max(dp[i][j-1], prices[j] + max_diff)
            max_diff = max(max_diff, dp[i-1][j-1] - prices[j])
    return dp[k][n-1]
```

</details>

### 71. Maximum Sum Rectangle
**Problem**: Write a Python function to find the maximum sum rectangle in a 2D matrix (list of lists) using Kadane's algorithm.  
Example:  
```
Input: [[1, 2, -1], [-2, 3, -2], [4, -1, 2]]  
Output: 8
```
<details>
<summary>Solution</summary>

```python
def max_sum_rectangle(matrix):
    if not matrix or not matrix[0]:
        return 0
    m, n = len(matrix), len(matrix[0])
    max_sum = float('-inf')
    for left in range(n):
        temp = [0] * m
        for right in range(left, n):
            for i in range(m):
                temp[i] += matrix[i][right]
            curr_sum = max_ending_here = temp[0]
            for num in temp[1:]:
                max_ending_here = max(num, max_ending_here + num)
                curr_sum = max(curr_sum, max_ending_here)
            max_sum = max(max_sum, curr_sum)
    return max_sum
```

</details>

### 72. Kth Largest in Stream
**Problem**: Write a Python class to find the kth largest element in a stream of numbers using a min-heap.  
Example:  
```
Input: k = 3, nums = [4, 5, 8, 2], add(3), add(5), add(10)  
Output: [4, 5, 5]
```
<details>
<summary>Solution</summary>

```python
from heapq import heappush, heappop
class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = []
        for num in nums:
            heappush(self.heap, num)
            if len(self.heap) > k:
                heappop(self.heap)

    def add(self, val):
        heappush(self.heap, val)
        if len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]
```

</details>

### 73. Maximum Sum Path in Two Lists
**Problem**: Write a Python function to find the maximum sum path in two lists where you can switch lists at common elements.  
Example:  
```
Input: ar1 = [2, 3, 7, 10], ar2 = [3, 12, 15, 7]  
Output: 32
```
<details>
<summary>Solution</summary>

```python
def max_sum_path(ar1, ar2):
    i = j = 0
    sum1 = sum2 = result = 0
    while i < len(ar1) and j < len(ar2):
        if ar1[i] < ar2[j]:
            sum1 += ar1[i]
            i += 1
        elif ar1[i] > ar2[j]:
            sum2 += ar2[j]
            j += 1
        else:
            result += max(sum1, sum2) + ar1[i]
            sum1 = sum2 = 0
            i += 1
            j += 1
    while i < len(ar1):
        sum1 += ar1[i]
        i += 1
    while j < len(ar2):
        sum2 += ar2[j]
        j += 1
    return result + max(sum1, sum2)
```

</details>

### 74. Longest Valid Parentheses
**Problem**: Write a Python function to find the length of the longest valid parentheses sequence in a list of 1s and -1s using a stack.  
Example:  
```
Input: [1, -1, -1, 1]  
Output: 4
```
<details>
<summary>Solution</summary>

```python
def longest_valid_parentheses(lst):
    stack = [-1]
    max_len = 0
    for i, val in enumerate(lst):
        if val == 1:
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])
    return max_len
```

</details>

### 75. Maximum Profit with Cooldown
**Problem**: Write a Python function to find the maximum profit with a cooldown period after selling using dynamic programming.  
Example:  
```
Input: [1, 2, 3, 0, 2]  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def max_profit_cooldown(prices):
    if not prices:
        return 0
    hold = -float('inf')
    sold = 0
    rest = 0
    for price in prices:
        prev_hold = hold
        hold = max(hold, rest - price)
        rest = max(rest, sold)
        sold = prev_hold + price
    return max(sold, rest)
```

</details>

### 76. Maximum Sum with No Adjacent Elements
**Problem**: Write a Python function to find the maximum sum of a subarray with no adjacent elements using dynamic programming.  
Example:  
```
Input: [5, 5, 10, 100, 10, 5]  
Output: 110
```
<details>
<summary>Solution</summary>

```python
def max_sum_no_adjacent(nums):
    if not nums:
        return 0
    incl = nums[0]
    excl = 0
    for i in range(1, len(nums)):
        temp = incl
        incl = excl + nums[i]
        excl = max(excl, temp)
    return max(incl, excl)
```

</details>

### 77. Minimum Cost to Reach End
**Problem**: Write a Python function to find the minimum cost to reach the end of a list with jumps of at most k steps using dynamic programming.  
Example:  
```
Input: lst = [10, 20, 30, 10], k = 2  
Output: 20
```
<details>
<summary>Solution</summary>

```python
def min_cost_to_end(lst, k):
    n = len(lst)
    dp = [float('inf')] * n
    dp[0] = lst[0]
    for i in range(1, n):
        for j in range(max(0, i - k), i):
            dp[i] = min(dp[i], dp[j] + lst[i])
    return dp[n-1]
```

</details>

### 78. Maximum Sum of Two Non-Overlapping Subarrays
**Problem**: Write a Python function to find the maximum sum of two non-overlapping subarrays with lengths L and M.  
Example:  
```
Input: nums = [0, 6, 5, 2, 2, 5], L = 2, M = 1  
Output: 13
```
<details>
<summary>Solution</summary>

```python
def max_sum_two_no_overlap(nums, L, M):
    def kadane(arr):
        max_so_far = max_ending_here = arr[0]
        for num in arr[1:]:
            max_ending_here = max(num, max_ending_here + num)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
    
    max_sum = 0
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    
    for i in range(len(nums) - L - M + 1):
        l_sum = prefix[i + L] - prefix[i]
        for j in range(i + L, len(nums) - M + 1):
            m_sum = prefix[j + M] - prefix[j]
            max_sum = max(max_sum, l_sum + m_sum)
        for j in range(i - M, -1, -1):
            m_sum = prefix[j + M] - prefix[j]
            l_sum = prefix[i + L + M] - prefix[i + M]
            max_sum = max(max_sum, l_sum + m_sum)
    return max_sum
```

</details>

### 79. Maximum Sum of Subarray with At Least K Elements
**Problem**: Write a Python function to find the maximum sum of a subarray with at least k elements using Kadane's algorithm.  
Example:  
```
Input: nums = [1, -2, 3, -4, 5], k = 3  
Output: 4
```
<details>
<summary>Solution</summary>

```python
def max_sum_at_least_k(nums, k):
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = max(nums[i], dp[i-1] + nums[i])
    curr_sum = sum(nums[:k])
    max_sum = curr_sum
    for i in range(k, n):
        curr_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum, curr_sum, dp[i-1] + nums[i])
    return max_sum
```

</details>

### 80. Maximum Length of Repeated Subarray
**Problem**: Write a Python function to find the length of the longest common subarray between two lists using dynamic programming.  
Example:  
```
Input: A = [1, 2, 3, 2, 1], B = [3, 2, 1, 4, 7]  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def find_length(A, B):
    m, n = len(A), len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_len = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                max_len = max(max_len, dp[i][j])
    return max_len
```

</details>

### 81. Maximum Average of Subarray of Size K
**Problem**: Write a Python function to find the maximum average of a subarray of size k using sliding window.  
Example:  
```
Input: nums = [1, 12, -5, -6, 50, 3], k = 4  
Output: 12.75
```
<details>
<summary>Solution</summary>

```python
def find_max_average(nums, k):
    curr_sum = sum(nums[:k])
    max_sum = curr_sum
    for i in range(k, len(nums)):
        curr_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum, curr_sum)
    return max_sum / k
```

</details>

### 82. Maximum Product of Three Numbers
**Problem**: Write a Python function to find the maximum product of three numbers in a list.  
Example:  
```
Input: [-4, -3, -2, 1, 60]  
Output: 720
```
<details>
<summary>Solution</summary>

```python
def maximum_product(nums):
    nums.sort()
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
```

</details>

### 83. Maximum Sum of Two Lists
**Problem**: Write a Python function to find the maximum sum of two non-overlapping subarrays from two lists using Kadane's algorithm.  
Example:  
```
Input: nums1 = [1, 2, 3], nums2 = [4, 5, 6]  
Output: 21
```
<details>
<summary>Solution</summary>

```python
def max_sum_two_lists(nums1, nums2):
    def kadane(arr):
        max_so_far = max_ending_here = arr[0]
        for num in arr[1:]:
            max_ending_here = max(num, max_ending_here + num)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
    
    return kadane(nums1) + kadane(nums2)
```

</details>

### 84. Maximum Length of Subarray with Equal 0s and 1s
**Problem**: Write a Python function to find the maximum length of a subarray with equal number of 0s and 1s using prefix sums.  
Example:  
```
Input: [0, 1]  
Output: 2
```
<details>
<summary>Solution</summary>

```python
def find_max_length(nums):
    count = 0
    max_len = 0
    seen = {0: -1}
    for i, num in enumerate(nums):
        count += 1 if num == 1 else -1
        if count in seen:
            max_len = max(max_len, i - seen[count])
        else:
            seen[count] = i
    return max_len
```

</details>

### 85. Maximum Sum with At Most K Elements
**Problem**: Write a Python function to find the maximum sum of a subarray with at most k elements using a sliding window.  
Example:  
```
Input: nums = [1, -2, 3, -4, 5], k = 3  
Output: 5
```
<details>
<summary>Solution</summary>

```python
def max_sum_at_most_k(nums, k):
    curr_sum = 0
    max_sum = float('-inf')
    for i in range(len(nums)):
        curr_sum += nums[i]
        if i >= k:
            curr_sum -= nums[i - k]
        max_sum = max(max_sum, curr_sum)
        if i < k:
            max_sum = max(max_sum, sum(nums[:i+1]))
    return max_sum if max_sum != float('-inf') else 0
```

</details>

### 86. Longest Subarray with Sum Divisible by K
**Problem**: Write a Python function to find the length of the longest subarray with a sum divisible by k using prefix sums.  
Example:  
```
Input: nums = [4, 5, 0, -2, -3, 1], k = 5  
Output: 6
```
<details>
<summary>Solution</summary>

```python
def longest_subarray_divisible(nums, k):
    prefix_sum = 0
    max_len = 0
    remainders = {0: -1}
    for i, num in enumerate(nums):
        prefix_sum += num
        rem = ((prefix_sum % k) + k) % k
        if rem in remainders:
            max_len = max(max_len, i - remainders[rem])
        else:
            remainders[rem] = i
    return max_len
```

</details>

### 87. Minimum Window Subarray
**Problem**: Write a Python function to find the minimum window subarray that contains all elements of a target list using a sliding window.  
Example:  
```
Input: nums = [1, 2, 3, 2, 1], target = [1, 2]  
Output: [1, 2]
```
<details>
<summary>Solution</summary>

```python
from collections import Counter
def min_window_subarray(nums, target):
    target_count = Counter(target)
    required = len(target_count)
    formed = 0
    window_counts = {}
    left = right = 0
    min_len = float('inf')
    min_window = []
    while right < len(nums):
        window_counts[nums[right]] = window_counts.get(nums[right], 0) + 1
        if nums[right] in target_count and window_counts[nums[right]] == target_count[nums[right]]:
            formed += 1
        while left <= right and formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = nums[left:right + 1]
            window_counts[nums[left]] -= 1
            if nums[left] in target_count and window_counts[nums[left]] < target_count[nums[left]]:
                formed -= 1
            left += 1
        right += 1
    return min_window
```

</details>

### 88. Longest Subarray with Absolute Difference Less Than or Equal to Limit
**Problem**: Write a Python function to find the longest subarray where the absolute difference between any two elements is at most a limit using deques.  
Example:  
```
Input: nums = [8, 2, 4, 7], limit = 4  
Output: 2
```
<details>
<summary>Solution</summary>

```python
from collections import deque
def longest_subarray_with_limit(nums, limit):
    max_deque = deque()
    min_deque = deque()
    left = 0
    max_len = 0
    for right in range(len(nums)):
        while max_deque and nums[max_deque[-1]] <= nums[right]:
            max_deque.pop()
        while min_deque and nums[min_deque[-1]] >= nums[right]:
            min_deque.pop()
        max_deque.append(right)
        min_deque.append(right)
        while max_deque and min_deque and nums[max_deque[0]] - nums[min_deque[0]] > limit:
            if max_deque[0] < min_deque[0]:
                left = max_deque.popleft() + 1
            else:
                left = min_deque.popleft() + 1
        max_len = max(max_len, right - left + 1)
    return max_len
```

</details>

### 89. Maximum Sum of Non-Overlapping Subarrays
**Problem**: Write a Python function to find the maximum sum of k non-overlapping subarrays using dynamic programming.  
Example:  
```
Input: nums = [1, 2, 1, 2, 6, 7, 5, 1], k = 2  
Output: 16
```
<details>
<summary>Solution</summary>

```python
def max_sum_k_non_overlapping(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        curr_sum = 0
        for j in range(i, -1, -1):
            curr_sum += nums[j] if j < i else 0
            for m in range(1, k + 1):
                if j == i:
                    dp[i][m] = dp[i-1][m]
                else:
                    dp[i][m] = max(dp[i][m], dp[j][m-1] + curr_sum)
        dp[i][0] = dp[i-1][0]
    return dp[n][k]
```

</details>

### 90. Find All Duplicates in List
**Problem**: Write a Python function to find all duplicates in a list of integers from 1 to n using in-place marking.  
Example:  
```
Input: [4, 3, 2, 7, 8, 2, 3, 1]  
Output: [2, 3]
```
<details>
<summary>Solution</summary>

```python
def find_all_duplicates(nums):
    result = []
    for num in nums:
        index = abs(num) - 1
        if nums[index] > 0:
            nums[index] = -nums[index]
        else:
            result.append(abs(num))
    return result
```

</details>

### 91. Maximum Length of Pair Chain
**Problem**: Write a Python function to find the longest chain of pairs where each pair’s second element is less than the next pair’s first element.  
Example:  
```
Input: pairs = [[1,2], [2,3], [3,4]]  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def find_longest_chain(pairs):
    pairs.sort(key=lambda x: x[1])
    curr_end = float('-inf')
    count = 0
    for start, end in pairs:
        if start > curr_end:
            count += 1
            curr_end = end
    return count
```

</details>

### 92. Maximum Profit with Two Transactions
**Problem**: Write a Python function to find the maximum profit with at most two transactions in stock prices using dynamic programming.  
Example:  
```
Input: prices = [3, 3, 5, 0, 0, 3, 1, 4]  
Output: 6
```
<details>
<summary>Solution</summary>

```python
def max_profit_two_transactions(prices):
    if not prices:
        return 0
    n = len(prices)
    first = [0] * n
    min_price = prices[0]
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        first[i] = max(first[i-1], prices[i] - min_price)
    max_profit = 0
    max_price = prices[-1]
    second = [0] * n
    for i in range(n-2, -1, -1):
        max_price = max(max_price, prices[i])
        second[i] = max(second[i+1], max_price - prices[i])
        max_profit = max(max_profit, first[i] + second[i])
    return max_profit
```

</details>

### 93. Maximum Sum Circular Subarray with At Most K Elements
**Problem**: Write a Python function to find the maximum sum of a circular subarray with at most k elements using a deque.  
Example:  
```
Input: nums = [1, -2, 3, -2], k = 3  
Output: 3
```
<details>
<summary>Solution</summary>

```python
from collections import deque
def max_sum_circular_k(nums, k):
    n = len(nums)
    nums = nums + nums
    max_sum = float('-inf')
    deq = deque()
    curr_sum = 0
    for i in range(len(nums)):
        while deq and i - deq[0] > k:
            deq.popleft()
        curr_sum += nums[i]
        while deq and curr_sum < nums[i]:
            curr_sum -= nums[deq.popleft()]
        deq.append(i)
        max_sum = max(max_sum, curr_sum)
        if i >= k:
            curr_sum -= nums[i - k]
    return max_sum if max_sum != float('-inf') else 0
```

</details>

### 94. Maximum Length of Subarray with Positive Product
**Problem**: Write a Python function to find the maximum length of a subarray with a positive product.  
Example:  
```
Input: nums = [1, -2, -3, 4]  
Output: 4
```
<details>
<summary>Solution</summary>

```python
def max_len_positive_product(nums):
    pos_len = neg_len = max_len = 0
    for num in nums:
        if num == 0:
            pos_len = neg_len = 0
        elif num > 0:
            pos_len += 1
            neg_len = neg_len + 1 if neg_len > 0 else 0
        else:
            pos_len, neg_len = neg_len + 1 if neg_len > 0 else 0, pos_len + 1
        max_len = max(max_len, pos_len)
    return max_len
```

</details>

### 95. Find All Anagrams in a List
**Problem**: Write a Python function to find all starting indices of anagrams of a pattern in a list using a sliding window.  
Example:  
```
Input: nums = [1, 2, 3, 1, 2, 3, 4], pattern = [1, 2, 3]  
Output: [0, 3]
```
<details>
<summary>Solution</summary>

```python
from collections import Counter
def find_anagrams(nums, pattern):
    target = Counter(pattern)
    window = Counter()
    result = []
    required = len(target)
    formed = 0
    k = len(pattern)
    for i in range(len(nums)):
        window[nums[i]] += 1
        if nums[i] in target and window[nums[i]] == target[nums[i]]:
            formed += 1
        if i >= k:
            left_num = nums[i - k]
            if left_num in target and window[left_num] == target[left_num]:
                formed -= 1
            window[left_num] -= 1
            if window[left_num] == 0:
                del window[left_num]
        if formed == required and len(window) == len(target):
            result.append(i - k + 1)
    return result
```

</details>

### 96. Maximum Sum of Distinct Subarrays with Length K
**Problem**: Write a Python function to find the maximum sum of a subarray of length k with distinct elements using a sliding window.  
Example:  
```
Input: nums = [1, 5, 4, 2, 9, 9, 9], k = 3  
Output: 15
```
<details>
<summary>Solution</summary>

```python
def max_sum_distinct_k(nums, k):
    max_sum = 0
    for i in range(len(nums) - k + 1):
        window = nums[i:i+k]
        if len(set(window)) == k:
            max_sum = max(max_sum, sum(window))
    return max_sum
```

</details>

### 97. Minimum Number of Operations to Sort
**Problem**: Write a Python function to find the minimum number of operations to sort a list by swapping adjacent elements.  
Example:  
```
Input: nums = [4, 2, 1, 3]  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def min_operations_to_sort(nums):
    n = len(nums)
    pos = {num: i for i, num in enumerate(nums)}
    target = sorted(nums)
    swaps = 0
    for i in range(n):
        while pos[target[i]] != i:
            j = pos[target[i]]
            nums[i], nums[j] = nums[j], nums[i]
            pos[nums[i]], pos[nums[j]] = i, j
            swaps += 1
    return swaps
```

</details>

### 98. Maximum Number of Pairs in Array
**Problem**: Write a Python function to find the maximum number of pairs that can be formed in a list and the remaining elements.  
Example:  
```
Input: nums = [1, 3, 2, 1, 3, 2, 2]  
Output: [3, 1]
```
<details>
<summary>Solution</summary>

```python
from collections import Counter
def number_of_pairs(nums):
    count = Counter(nums)
    pairs = sum(c // 2 for c in count.values())
    remaining = sum(c % 2 for c in count.values())
    return [pairs, remaining]
```

</details>

### 99. Maximum Number of Events That Can Be Attended
**Problem**: Write a Python function to find the maximum number of non-overlapping events that can be attended from a list of intervals.  
Example:  
```
Input: events = [[1,2], [2,3], [3,4]]  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def max_events(events):
    events.sort(key=lambda x: x[1])
    count = 0
    prev_end = 0
    for start, end in events:
        if start > prev_end:
            count += 1
            prev_end = end
    return count
```

</details>

### 100. Maximum Sum of K Non-Overlapping Intervals
**Problem**: Write a Python function to find the maximum sum of k non-overlapping intervals from a list of intervals with weights.  
Example:  
```
Input: intervals = [[1,3,10], [2,4,15], [3,5,20]], k = 2  
Output: 35
```
<details>
<summary>Solution</summary>

```python
def max_sum_k_non_overlapping_intervals(intervals, k):
    intervals.sort(key=lambda x: x[1])
    n = len(intervals)
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        j = i - 1
        while j >= 0 and intervals[j][1] > intervals[i-1][0]:
            j -= 1
        for m in range(k + 1):
            dp[i][m] = dp[i-1][m]
            if m > 0 and j >= 0:
                dp[i][m] = max(dp[i][m], dp[j+1][m-1] + intervals[i-1][2])
            elif m > 0:
                dp[i][m] = max(dp[i][m], intervals[i-1][2])
    return dp[n][k]
```

</details>