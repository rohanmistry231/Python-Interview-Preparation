# Python Tuple Pattern Coding Practice Questions

This file contains 100 practice questions for Python tuple patterns, ranging from beginner to advanced levels. Each task is designed to enhance your understanding of tuple operations and their applications in coding interviews.

## Beginner Level

1. **Create Tuple**  
   Create a tuple with 5 elements using: (a) parentheses, (b) `tuple()`, (c) without brackets.

2. **Access Element**  
   Given `deptnames = ('HR', 'ADMIN', 'ENGG', 'SECURITY', 'MANAGERS')`, access and print the element at index 2.

3. **Negative Indexing**  
   Using `deptnames` from Q2, print the last element using negative indexing.

4. **Slicing Tuple**  
   Given `t1 = (10, 30, 50, 30, 60, 45)`, print elements from index 1 to 3 using slicing.

5. **Slicing with Step**  
   Using `t1` from Q4, print every second element using slicing with a step of 2.

6. **Count Occurrences**  
   Given `t = (1, 2, 2, 3, 2)`, count occurrences of 2 using `count()`.

7. **Find Index**  
   Given `t = (10, 20, 30, 40)`, find the index of 30 using `index()`.

8. **Tuple Concatenation**  
   Concatenate two tuples `(1, 2)` and `(3, 4)` using `+`.

9. **Tuple Repetition**  
   Repeat the tuple `(1, 2)` three times using `*`.

10. **Membership Testing**  
    Check if 3 exists in `(1, 2, 3, 4)` using `in`.

11. **Tuple Length**  
    Find the length of `(10, 20, 30, 40, 50)` using `len()`.

12. **Maximum Value**  
    Find the maximum value in `(1, 5, 3, 2)` using `max()`.

13. **Minimum Value**  
    Find the minimum value in `(1, 5, 3, 2)` using `min()`.

14. **Sum of Tuple**  
    Calculate the sum of `(1, 2, 3, 4)` using `sum()`.

15. **Sorted Tuple**  
    Convert `(3, 1, 2)` to a sorted list using `sorted()`.

16. **Tuple Unpacking**  
    Unpack `(1, 2, 3)` into variables `a`, `b`, `c` and print them.

17. **Create Tuple from List**  
    Convert `[1, 2, 3]` to a tuple using `tuple()`.

18. **Create Tuple from Range**  
    Create a tuple of numbers 0 to 4 using `tuple(range(5))`.

19. **Tuple of Squares**  
    Create a tuple of squares for numbers 0 to 4 using a generator expression.

20. **Check Tuple Type**  
    Create a tuple without brackets (e.g., `1, 2, 3`) and verify its type using `type()`.

## Intermediate Level

21. **Modify Tuple**  
    Given `deptnames = ('HR', 'ADMIN', 'ENGG', 'SECURITY', 'MANAGERS')`, change 'HR' to 'HR ROSE' by converting to a list and back.

22. **Remove Element from Tuple**  
    Using `deptnames` from Q21, remove 'MANAGERS' by converting to a list and back.

23. **Tuple Slicing Reverse**  
    Given `t = (10, 20, 30, 40, 50)`, print elements in reverse order using slicing.

24. **Nested Tuple Access**  
    Given `t = ((1, 2), (3, 4), (5, 6))`, access the element 4.

25. **Count Duplicates**  
    Given `t = (1, 2, 2, 3, 2, 4)`, count duplicates of each element.

26. **Tuple to List Conversion**  
    Convert `(10, 20, 30)` to a list and append 40.

27. **List to Tuple Conversion**  
    Convert `[1, 2, 3, 4]` to a tuple.

28. **Tuple Concatenation with List**  
    Concatenate `(1, 2)` with a list `[3, 4]` after converting the list to a tuple.

29. **Tuple Unpacking with Star**  
    Unpack `(1, 2, 3, 4, 5)` into `a`, `b`, and a list of remaining elements using `*`.

30. **Tuple from String**  
    Create a tuple of characters from a string (e.g., `'hello'`).

31. **Check Subtuple**  
    Check if `(2, 3)` is a subtuple of `(1, 2, 3, 4)`.

32. **Tuple Frequency**  
    Given `t = (1, 2, 2, 3, 1)`, create a dictionary of element frequencies.

33. **Tuple Comparison**  
    Compare two tuples `(1, 2, 3)` and `(1, 2, 4)` for equality.

34. **Tuple of Tuples**  
    Create a tuple of tuples to store student details (e.g., `(name, roll_no)`).

35. **Tuple Sorting**  
    Sort elements of `(5, 2, 8, 1)` into a new tuple.

36. **Tuple Intersection**  
    Find common elements between two tuples using sets.

37. **Tuple Union**  
    Find the union of two tuples using sets.

38. **Tuple Difference**  
    Find elements in one tuple not in another using sets.

39. **Tuple to String**  
    Convert `(1, 2, 3)` to a string like `"1,2,3"`.

40. **Tuple from Input**  
    Create a tuple from user-input numbers.

## Advanced Level

41. **Nested Tuple Flattening**  
    Flatten a nested tuple `((1, 2), (3, (4, 5)))` into `(1, 2, 3, 4, 5)`.

42. **Tuple to Dictionary**  
    Convert a tuple of pairs `(('a', 1), ('b', 2))` to a dictionary.

43. **Tuple Rotation**  
    Rotate a tuple `(1, 2, 3, 4)` by k positions to the right.

44. **Tuple Partition**  
    Partition a tuple into two based on a condition (e.g., even/odd numbers).

45. **Tuple to Set**  
    Convert a tuple `(1, 2, 2, 3)` to a set to remove duplicates.

46. **Tuple of Unique Elements**  
    Create a tuple of unique elements from `(1, 2, 2, 3, 3)`.

47. **Tuple Palindrome Check**  
    Check if a tuple `(1, 2, 2, 1)` is a palindrome.

48. **Tuple Subsequence**  
    Check if `(2, 3)` is a subsequence of `(1, 2, 3, 4)`.

49. **Tuple Pair Sum**  
    Find pairs in a tuple `(1, 2, 3, 4)` that sum to a target value.

50. **Tuple to Matrix**  
    Convert a tuple `(1, 2, 3, 4, 5, 6)` to a 2x3 matrix tuple `((1, 2, 3), (4, 5, 6))`.

51. **Tuple Comprehension Alternative**  
    Create a tuple of cubes for numbers 1 to 5 using a generator expression.

52. **Tuple Element Swap**  
    Swap two elements in a tuple by converting to a list and back.

53. **Tuple Grouping**  
    Group elements in a tuple by a condition (e.g., even/odd).

54. **Tuple to JSON**  
    Convert a tuple of tuples to a JSON string using the `json` module.

55. **Tuple Merging**  
    Merge two tuples, removing duplicates using sets.

56. **Tuple Element Frequency**  
    Create a tuple of (element, frequency) pairs from `(1, 2, 2, 3)`.

57. **Tuple to Binary**  
    Convert a tuple of numbers to their binary representations.

58. **Tuple Slicing with Dynamic Input**  
    Slice a tuple based on user-specified start, stop, and step.

59. **Tuple to CSV**  
    Convert a tuple of tuples to a CSV string.

60. **Tuple Validation**  
    Validate that all elements in a tuple are of a specific type (e.g., int).

## Expert Level

61. **Tuple to Permutations**  
    Generate all permutations of a tuple `(1, 2, 3)` as a tuple of tuples.

62. **Tuple to Combinations**  
    Generate all combinations of a tuple `(1, 2, 3)` of size k.

63. **Tuple Subset Sum**  
    Check if a subtuple sums to a target value.

64. **Tuple Longest Increasing Subsequence**  
    Find the length of the longest increasing subsequence in a tuple.

65. **Tuple to Graph Edges**  
    Convert a tuple of pairs `(('a', 'b'), ('b', 'c'))` to a graph adjacency list.

66. **Tuple Anagram Groups**  
    Group elements in a tuple of strings by their anagrams.

67. **Tuple to Balanced BST**  
    Convert a sorted tuple to a balanced binary search tree tuple.

68. **Tuple Longest Common Subsequence**  
    Find the longest common subsequence between two tuples.

69. **Tuple to Spiral Matrix**  
    Convert a tuple to a 2D matrix tuple in spiral order.

70. **Tuple Cycle Detection**  
    Detect if a tuple representing a linked list has a cycle.

71. **Tuple to Minimum Spanning Tree**  
    Find the minimum spanning tree from a tuple of weighted edges.

72. **Tuple to Shortest Path**  
    Find the shortest path in a graph represented as a tuple of edges.

73. **Tuple to Topological Sort**  
    Perform a topological sort on a directed acyclic graph from a tuple of edges.

74. **Tuple to Bipartite Check**  
    Check if a graph from a tuple of edges is bipartite.

75. **Tuple to Maximum Flow**  
    Compute the maximum flow in a flow network from a tuple of edges.

76. **Tuple to Hamiltonian Cycle**  
    Check if a graph from a tuple of edges has a Hamiltonian cycle.

77. **Tuple to Clique Detection**  
    Detect if a tuple of edges forms a clique.

78. **Tuple to Knapsack Problem**  
    Solve the 0/1 knapsack problem using a tuple of items with weights and values.

79. **Tuple to Longest Palindromic Subsequence**  
    Find the length of the longest palindromic subsequence in a tuple.

80. **Tuple to Word Ladder**  
    Find the shortest transformation sequence from one word to another using a tuple of words.

81. **Tuple to Matrix Rotation**  
    Rotate a 2D matrix tuple 90 degrees clockwise.

82. **Tuple to Skyline Problem**  
    Compute the skyline from a tuple of building coordinates and heights.

83. **Tuple to Subarray Sum**  
    Find the number of subtuple sums equal to a target value.

84. **Tuple to Maximum Subarray Sum**  
    Find the maximum sum of a contiguous subtuple.

85. **Tuple to Graph Coloring**  
    Assign colors to vertices in a graph from a tuple of edges.

86. **Tuple to Strongly Connected Components**  
    Find strongly connected components in a graph from a tuple of edges.

87. **Tuple to Minimum Vertex Cover**  
    Find the minimum vertex cover in a graph from a tuple of edges.

88. **Tuple to Eulerian Path**  
    Find an Eulerian path in a graph from a tuple of edges.

89. **Tuple to Longest Valid Parentheses**  
    Find the longest valid parentheses sequence in a tuple of parentheses.

90. **Tuple to Maximum Matching**  
    Find the maximum matching in a bipartite graph from a tuple of edges.

91. **Tuple to Median of Two Tuples**  
    Find the median of two sorted tuples.

92. **Tuple to Merge Intervals**  
    Merge overlapping intervals in a tuple of intervals.

93. **Tuple to Longest Consecutive Sequence**  
    Find the length of the longest consecutive sequence in a tuple.

94. **Tuple to Maximum XOR**  
    Find the maximum XOR of any two elements in a tuple.

95. **Tuple to Course Schedule**  
    Determine if all courses can be completed from a tuple of prerequisites.

96. **Tuple to Minimum Cut**  
    Find the minimum cut in a graph from a tuple of edges.

97. **Tuple to Traveling Salesman**  
    Solve the traveling salesman problem for a graph from a tuple of weighted edges.

98. **Tuple to Alien Dictionary**  
    Derive the order of characters from a tuple of words in an alien language.

99. **Tuple to Balanced Partition**  
    Partition a tuple into two subtubles with minimum difference in sums.

100. **Tuple to Graph Isomorphism**  
     Check if two graphs from tuples of edges are isomorphic.