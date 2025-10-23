"""
Challenges Database

This module stores the dictionary of challenges that acts as the database.
Each category has at least one challenge per difficulty level (easy, medium, hard).
Challenges are available in English (CHALLENGES_DB_EN) and Spanish (CHALLENGES_DB_ES).
"""

# English Challenges Database
CHALLENGES_DB_EN = [
    # MATHEMATICS - 15 challenges (5 easy, 5 medium, 5 hard)
    {
        "id": 1,
        "title": "Sum of Two Numbers",
        "description": "Create a function that takes two numbers and returns their sum.",
        "difficulty": "easy",
        "category": "mathematics",
        "points": 10,
        "example_input": "[2, 3]",
        "example_output": "5",
        "hints": ["Use the + operator", "Don't forget the return statement"]
    },
    {
        "id": 34,
        "title": "Multiplication Table",
        "description": "Generate a multiplication table for a given number up to 10.",
        "difficulty": "easy",
        "category": "mathematics",
        "points": 10,
        "example_input": "5",
        "example_output": "[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]",
        "hints": ["Use a loop or list comprehension", "Multiply number by 1 to 10", "Return as list"]
    },
    {
        "id": 35,
        "title": "Average Calculator",
        "description": "Calculate the average (mean) of a list of numbers.",
        "difficulty": "easy",
        "category": "mathematics",
        "points": 10,
        "example_input": "[10, 20, 30, 40, 50]",
        "example_output": "30.0",
        "hints": ["Sum all numbers", "Divide by the count", "Use len() for count"]
    },
    {
        "id": 36,
        "title": "Even or Odd",
        "description": "Determine if a number is even or odd.",
        "difficulty": "easy",
        "category": "mathematics",
        "points": 10,
        "example_input": "7",
        "example_output": "'odd'",
        "hints": ["Use modulo operator %", "If n % 2 == 0, it's even", "Return string 'even' or 'odd'"]
    },
    {
        "id": 37,
        "title": "Maximum of Three Numbers",
        "description": "Find the maximum value among three numbers without using max() function.",
        "difficulty": "easy",
        "category": "mathematics",
        "points": 10,
        "example_input": "(15, 42, 28)",
        "example_output": "42",
        "hints": ["Use if-elif-else statements", "Compare pairs of numbers", "Return the largest"]
    },
    {
        "id": 2,
        "title": "Prime Numbers",
        "description": "Create a function that determines if a number is prime.",
        "difficulty": "medium",
        "category": "mathematics",
        "points": 25,
        "example_input": "17",
        "example_output": "True",
        "hints": ["A prime number is only divisible by 1 and itself", "Use the % operator", "Optimize by checking only up to the square root"]
    },
    {
        "id": 38,
        "title": "Fibonacci Sequence",
        "description": "Generate the first n numbers of the Fibonacci sequence.",
        "difficulty": "medium",
        "category": "mathematics",
        "points": 25,
        "example_input": "7",
        "example_output": "[0, 1, 1, 2, 3, 5, 8]",
        "hints": ["Start with [0, 1]", "Each number is sum of previous two", "Use loop to generate n numbers"]
    },
    {
        "id": 39,
        "title": "GCD Calculator",
        "description": "Calculate the Greatest Common Divisor (GCD) of two numbers using Euclidean algorithm.",
        "difficulty": "medium",
        "category": "mathematics",
        "points": 25,
        "example_input": "(48, 18)",
        "example_output": "6",
        "hints": ["Use Euclidean algorithm", "Apply modulo operation repeatedly", "Can use recursion or loop"]
    },
    {
        "id": 40,
        "title": "Perfect Number Checker",
        "description": "Determine if a number is perfect (equals sum of its proper divisors).",
        "difficulty": "medium",
        "category": "mathematics",
        "points": 25,
        "example_input": "28",
        "example_output": "True",
        "hints": ["Find all divisors less than the number", "Sum the divisors", "Compare sum with original number"]
    },
    {
        "id": 41,
        "title": "Number to Roman Numerals",
        "description": "Convert an integer to Roman numerals (1-3999).",
        "difficulty": "medium",
        "category": "mathematics",
        "points": 25,
        "example_input": "1994",
        "example_output": "'MCMXCIV'",
        "hints": ["Use mapping of values to symbols", "Process from largest to smallest", "Handle special cases like 4, 9, 40, 90, etc."]
    },
    {
        "id": 3,
        "title": "Complex Number Operations",
        "description": "Implement complex mathematical operations including factorial, power, and modular arithmetic.",
        "difficulty": "hard",
        "category": "mathematics",
        "points": 40,
        "example_input": "(5, 3, 7)",
        "example_output": "{'factorial': 120, 'power': 125, 'mod': 6}",
        "hints": ["Use recursion for factorial", "Handle large numbers", "Implement modular exponentiation"]
    },
    {
        "id": 42,
        "title": "Matrix Operations",
        "description": "Implement matrix addition, multiplication, and transpose operations.",
        "difficulty": "hard",
        "category": "mathematics",
        "points": 40,
        "example_input": "([[1, 2], [3, 4]], [[5, 6], [7, 8]])",
        "example_output": "{'add': [[6, 8], [10, 12]], 'multiply': [[19, 22], [43, 50]], 'transpose': [[1, 3], [2, 4]]}",
        "hints": ["Use nested loops for matrix operations", "Check dimensions for multiplication", "Transpose swaps rows and columns"]
    },
    {
        "id": 43,
        "title": "Sieve of Eratosthenes",
        "description": "Find all prime numbers up to n using the Sieve of Eratosthenes algorithm.",
        "difficulty": "hard",
        "category": "mathematics",
        "points": 40,
        "example_input": "30",
        "example_output": "[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]",
        "hints": ["Create boolean array of size n+1", "Mark multiples of each prime as composite", "Return indices that remain marked as prime"]
    },
    {
        "id": 44,
        "title": "Polynomial Evaluator",
        "description": "Evaluate a polynomial given coefficients and x value, and find its derivative.",
        "difficulty": "hard",
        "category": "mathematics",
        "points": 40,
        "example_input": "([3, 0, 2, -1], 2)",
        "example_output": "{'value': 17, 'derivative': [0, 4, -3]}",
        "hints": ["Use Horner's method for efficiency", "Derivative reduces power by 1", "Multiply coefficient by original power"]
    },
    {
        "id": 45,
        "title": "Number Theory Challenge",
        "description": "Implement functions to find LCM, check for coprime numbers, and calculate Euler's totient function.",
        "difficulty": "hard",
        "category": "mathematics",
        "points": 40,
        "example_input": "(12, 18)",
        "example_output": "{'lcm': 36, 'coprime': False, 'totient_12': 4, 'totient_18': 6}",
        "hints": ["LCM = (a*b) / GCD(a,b)", "Coprime means GCD = 1", "Totient counts numbers < n that are coprime to n"]
    },
    
    # STRINGS - 15 challenges (5 easy, 5 medium, 5 hard)
    {
        "id": 4,
        "title": "Character Counter",
        "description": "Count the frequency of each character in a text string.",
        "difficulty": "easy",
        "category": "strings",
        "points": 15,
        "example_input": "'hello'",
        "example_output": "{'h': 1, 'e': 1, 'l': 2, 'o': 1}",
        "hints": ["Use a dictionary", "Iterate over each character", "Increment the counter"]
    },
    {
        "id": 46,
        "title": "String Reverser",
        "description": "Reverse a string without using built-in reverse functions.",
        "difficulty": "easy",
        "category": "strings",
        "points": 15,
        "example_input": "'Python'",
        "example_output": "'nohtyP'",
        "hints": ["Use slicing [::-1]", "Or iterate backwards", "Or use a loop to build reversed string"]
    },
    {
        "id": 47,
        "title": "Vowel Counter",
        "description": "Count the number of vowels in a given string.",
        "difficulty": "easy",
        "category": "strings",
        "points": 15,
        "example_input": "'Programming'",
        "example_output": "3",
        "hints": ["Define vowels: a, e, i, o, u", "Convert to lowercase", "Count occurrences"]
    },
    {
        "id": 48,
        "title": "First Letter Capitalizer",
        "description": "Capitalize the first letter of each word in a sentence.",
        "difficulty": "easy",
        "category": "strings",
        "points": 15,
        "example_input": "'hello world python'",
        "example_output": "'Hello World Python'",
        "hints": ["Use title() method", "Or split, capitalize each, and join", "Handle multiple spaces"]
    },
    {
        "id": 49,
        "title": "Remove Whitespace",
        "description": "Remove all whitespace characters from a string.",
        "difficulty": "easy",
        "category": "strings",
        "points": 15,
        "example_input": "'  Hello   World  '",
        "example_output": "'HelloWorld'",
        "hints": ["Use replace(' ', '')", "Or filter out whitespace", "Or join split parts"]
    },
    {
        "id": 5,
        "title": "Palindrome",
        "description": "Determine if a word or phrase is a palindrome (reads the same from left to right as from right to left).",
        "difficulty": "medium",
        "category": "strings",
        "points": 20,
        "example_input": "'radar'",
        "example_output": "True",
        "hints": ["Use slicing [::-1]", "Consider uppercase and spaces", "Compare the string with its reverse"]
    },
    {
        "id": 50,
        "title": "Anagram Checker",
        "description": "Check if two strings are anagrams of each other.",
        "difficulty": "medium",
        "category": "strings",
        "points": 20,
        "example_input": "('listen', 'silent')",
        "example_output": "True",
        "hints": ["Sort both strings and compare", "Or count character frequencies", "Ignore case and spaces"]
    },
    {
        "id": 51,
        "title": "String Compression",
        "description": "Compress a string by replacing consecutive characters with character and count.",
        "difficulty": "medium",
        "category": "strings",
        "points": 20,
        "example_input": "'aaabbcccc'",
        "example_output": "'a3b2c4'",
        "hints": ["Iterate through string", "Count consecutive characters", "Build compressed string"]
    },
    {
        "id": 52,
        "title": "Longest Word Finder",
        "description": "Find the longest word in a sentence.",
        "difficulty": "medium",
        "category": "strings",
        "points": 20,
        "example_input": "'The quick brown fox jumps'",
        "example_output": "'quick'",
        "hints": ["Split sentence into words", "Compare lengths", "Return longest word"]
    },
    {
        "id": 53,
        "title": "Caesar Cipher",
        "description": "Implement a Caesar cipher encryption with configurable shift.",
        "difficulty": "medium",
        "category": "strings",
        "points": 20,
        "example_input": "('hello', 3)",
        "example_output": "'khoor'",
        "hints": ["Shift each letter by n positions", "Use ord() and chr()", "Handle wrap-around from z to a"]
    },
    {
        "id": 6,
        "title": "Advanced String Manipulation",
        "description": "Implement multiple string operations: reverse words, capitalize alternating characters, and remove duplicates.",
        "difficulty": "hard",
        "category": "strings",
        "points": 35,
        "example_input": "'hello world hello'",
        "example_output": "{'reversed': 'olleh dlrow olleh', 'alternating': 'HeLlO WoRlD HeLlO', 'no_duplicates': 'helo wrd'}",
        "hints": ["Split and join for word reversal", "Use enumerate for alternating", "Use set or tracking for duplicates"]
    },
    {
        "id": 54,
        "title": "Substring Pattern Finder",
        "description": "Find all occurrences of a pattern in a string and return their positions.",
        "difficulty": "hard",
        "category": "strings",
        "points": 35,
        "example_input": "('ababcababa', 'aba')",
        "example_output": "[0, 5, 7]",
        "hints": ["Search for overlapping patterns", "Use string slicing", "Return list of starting indices"]
    },
    {
        "id": 55,
        "title": "Text Justification",
        "description": "Justify text to a given width by distributing spaces evenly.",
        "difficulty": "hard",
        "category": "strings",
        "points": 35,
        "example_input": "(['This', 'is', 'an', 'example'], 16)",
        "example_output": "['This    is    an', 'example         ']",
        "hints": ["Calculate spaces needed", "Distribute spaces evenly", "Handle last line differently"]
    },
    {
        "id": 56,
        "title": "Longest Palindromic Substring",
        "description": "Find the longest palindromic substring in a given string.",
        "difficulty": "hard",
        "category": "strings",
        "points": 35,
        "example_input": "'babad'",
        "example_output": "'bab'",
        "hints": ["Check each possible substring", "Expand around center", "Track longest found"]
    },
    {
        "id": 57,
        "title": "Word Frequency Analyzer",
        "description": "Analyze text to find word frequencies, most common words, and generate statistics.",
        "difficulty": "hard",
        "category": "strings",
        "points": 35,
        "example_input": "'the quick brown fox jumps over the lazy dog the fox'",
        "example_output": "{'most_common': [('the', 3), ('fox', 2)], 'unique_words': 9, 'total_words': 11}",
        "hints": ["Use Counter from collections", "Clean and normalize text", "Sort by frequency"]
    },

    # ALGORITHMS - 15 challenges (5 easy, 5 medium, 5 hard)
    {
        "id": 7,
        "title": "Linear Search",
        "description": "Implement a simple linear search algorithm to find an element in a list.",
        "difficulty": "easy",
        "category": "algorithms",
        "points": 15,
        "example_input": "([1, 3, 5, 7, 9], 5)",
        "example_output": "2",
        "hints": ["Iterate through the list", "Compare each element", "Return the index when found"]
    },
    {
        "id": 58,
        "title": "Find Maximum",
        "description": "Find the maximum element in a list without using max() function.",
        "difficulty": "easy",
        "category": "algorithms",
        "points": 15,
        "example_input": "[3, 7, 2, 9, 1]",
        "example_output": "9",
        "hints": ["Initialize with first element", "Compare with each element", "Update if larger found"]
    },
    {
        "id": 59,
        "title": "Count Occurrences",
        "description": "Count how many times an element appears in a list.",
        "difficulty": "easy",
        "category": "algorithms",
        "points": 15,
        "example_input": "([1, 2, 3, 2, 4, 2], 2)",
        "example_output": "3",
        "hints": ["Use counter variable", "Iterate and compare", "Increment when match found"]
    },
    {
        "id": 60,
        "title": "List Reversal",
        "description": "Reverse a list without using built-in reverse() or [::-1].",
        "difficulty": "easy",
        "category": "algorithms",
        "points": 15,
        "example_input": "[1, 2, 3, 4, 5]",
        "example_output": "[5, 4, 3, 2, 1]",
        "hints": ["Use two pointers approach", "Swap elements from ends", "Move pointers toward center"]
    },
    {
        "id": 61,
        "title": "Remove Duplicates",
        "description": "Remove duplicate elements from a list while preserving order.",
        "difficulty": "easy",
        "category": "algorithms",
        "points": 15,
        "example_input": "[1, 2, 2, 3, 4, 3, 5]",
        "example_output": "[1, 2, 3, 4, 5]",
        "hints": ["Use set to track seen elements", "Build new list", "Only add if not seen before"]
    },
    {
        "id": 8,
        "title": "Merge Two Sorted Lists",
        "description": "Merge two sorted lists into one sorted list without using built-in sort functions.",
        "difficulty": "medium",
        "category": "algorithms",
        "points": 25,
        "example_input": "([1, 3, 5], [2, 4, 6])",
        "example_output": "[1, 2, 3, 4, 5, 6]",
        "hints": ["Use two pointers", "Compare elements from both lists", "Handle remaining elements"]
    },
    {
        "id": 62,
        "title": "Binary Search",
        "description": "Implement binary search algorithm on a sorted list.",
        "difficulty": "medium",
        "category": "algorithms",
        "points": 25,
        "example_input": "([1, 3, 5, 7, 9, 11, 13], 7)",
        "example_output": "3",
        "hints": ["Use two pointers: left and right", "Check middle element", "Adjust pointers based on comparison"]
    },
    {
        "id": 63,
        "title": "Two Sum Problem",
        "description": "Find two numbers in an array that add up to a target sum.",
        "difficulty": "medium",
        "category": "algorithms",
        "points": 25,
        "example_input": "([2, 7, 11, 15], 9)",
        "example_output": "[0, 1]",
        "hints": ["Use hash map for O(n) solution", "Store complements", "Return indices when found"]
    },
    {
        "id": 64,
        "title": "Rotate Array",
        "description": "Rotate an array to the right by k positions.",
        "difficulty": "medium",
        "category": "algorithms",
        "points": 25,
        "example_input": "([1, 2, 3, 4, 5], 2)",
        "example_output": "[4, 5, 1, 2, 3]",
        "hints": ["Use slicing", "Handle k larger than array length", "k = k % len(arr)"]
    },
    {
        "id": 65,
        "title": "Find Missing Number",
        "description": "Find the missing number in an array containing n-1 numbers from 1 to n.",
        "difficulty": "medium",
        "category": "algorithms",
        "points": 25,
        "example_input": "[1, 2, 4, 5, 6]",
        "example_output": "3",
        "hints": ["Use sum formula n*(n+1)/2", "Subtract sum of array", "Or use XOR approach"]
    },
    {
        "id": 9,
        "title": "Bubble Sort",
        "description": "Implement the bubble sort algorithm to sort a list of numbers.",
        "difficulty": "hard",
        "category": "algorithms",
        "points": 35,
        "example_input": "[64, 34, 25, 12, 22, 11, 90]",
        "example_output": "[11, 12, 22, 25, 34, 64, 90]",
        "hints": ["Compare adjacent elements", "Swap if they are in wrong order", "Repeat the process"]
    },
    {
        "id": 66,
        "title": "Quick Sort",
        "description": "Implement the quicksort algorithm with pivot selection.",
        "difficulty": "hard",
        "category": "algorithms",
        "points": 35,
        "example_input": "[3, 6, 8, 10, 1, 2, 1]",
        "example_output": "[1, 1, 2, 3, 6, 8, 10]",
        "hints": ["Choose pivot element", "Partition around pivot", "Recursively sort partitions"]
    },
    {
        "id": 67,
        "title": "Longest Common Subsequence",
        "description": "Find the longest common subsequence between two strings.",
        "difficulty": "hard",
        "category": "algorithms",
        "points": 35,
        "example_input": "('ABCDGH', 'AEDFHR')",
        "example_output": "'ADH'",
        "hints": ["Use dynamic programming", "Build 2D table", "Backtrack to find sequence"]
    },
    {
        "id": 68,
        "title": "Dijkstra's Shortest Path",
        "description": "Implement Dijkstra's algorithm to find shortest path in a weighted graph.",
        "difficulty": "hard",
        "category": "algorithms",
        "points": 35,
        "example_input": "({'A': {'B': 4, 'C': 2}, 'B': {'D': 3}, 'C': {'D': 1}, 'D': {}}, 'A', 'D')",
        "example_output": "{'path': ['A', 'C', 'D'], 'distance': 3}",
        "hints": ["Use priority queue", "Track distances and visited nodes", "Update distances when shorter path found"]
    },
    {
        "id": 69,
        "title": "Dynamic Programming - Knapsack",
        "description": "Solve the 0/1 knapsack problem using dynamic programming.",
        "difficulty": "hard",
        "category": "algorithms",
        "points": 35,
        "example_input": "([60, 100, 120], [10, 20, 30], 50)",
        "example_output": "{'max_value': 220, 'items': [1, 2]}",
        "hints": ["Build 2D DP table", "dp[i][w] = max value with i items and weight w", "Backtrack to find selected items"]
    },

    # LIST COMPREHENSION - 15 challenges (5 easy, 5 medium, 5 hard)
    {
        "id": 10,
        "title": "List Comprehension Filter",
        "description": "Use list comprehension to filter even numbers from a list and square them.",
        "difficulty": "easy",
        "category": "list comprehension",
        "points": 15,
        "example_input": "[1, 2, 3, 4, 5, 6]",
        "example_output": "[4, 16, 36]",
        "hints": ["Use list comprehension syntax [expr for item in list if condition]", "Check if number % 2 == 0", "Square with ** 2"]
    },
    {
        "id": 70,
        "title": "Extract Positive Numbers",
        "description": "Use list comprehension to extract only positive numbers from a list.",
        "difficulty": "easy",
        "category": "list comprehension",
        "points": 15,
        "example_input": "[-3, -1, 0, 2, 5, -7, 8]",
        "example_output": "[2, 5, 8]",
        "hints": ["Use condition x > 0", "Syntax: [x for x in list if x > 0]", "Filter while iterating"]
    },
    {
        "id": 71,
        "title": "String Lengths",
        "description": "Create a list of string lengths using list comprehension.",
        "difficulty": "easy",
        "category": "list comprehension",
        "points": 15,
        "example_input": "['hello', 'world', 'python']",
        "example_output": "[5, 5, 6]",
        "hints": ["Use len() function", "Syntax: [len(s) for s in strings]", "Apply function to each element"]
    },
    {
        "id": 72,
        "title": "Uppercase Conversion",
        "description": "Convert all strings in a list to uppercase using list comprehension.",
        "difficulty": "easy",
        "category": "list comprehension",
        "points": 15,
        "example_input": "['apple', 'banana', 'cherry']",
        "example_output": "['APPLE', 'BANANA', 'CHERRY']",
        "hints": ["Use .upper() method", "Syntax: [s.upper() for s in strings]", "Transform each element"]
    },
    {
        "id": 73,
        "title": "Range with Multiplication",
        "description": "Create a list of first 10 multiples of a number using list comprehension.",
        "difficulty": "easy",
        "category": "list comprehension",
        "points": 15,
        "example_input": "7",
        "example_output": "[7, 14, 21, 28, 35, 42, 49, 56, 63, 70]",
        "hints": ["Use range(1, 11)", "Multiply by the number", "Syntax: [n * i for i in range(1, 11)]"]
    },
    {
        "id": 11,
        "title": "Nested List Comprehension",
        "description": "Create a matrix (2D list) using nested list comprehensions.",
        "difficulty": "medium",
        "category": "list comprehension",
        "points": 25,
        "example_input": "(3, 3)",
        "example_output": "[[0, 1, 2], [1, 2, 3], [2, 3, 4]]",
        "hints": ["Use nested list comprehension [[expr for j in range] for i in range]", "Each element should be i + j", "Return rows x cols matrix"]
    },
    {
        "id": 74,
        "title": "Conditional Transformation",
        "description": "Use list comprehension with if-else to transform numbers.",
        "difficulty": "medium",
        "category": "list comprehension",
        "points": 25,
        "example_input": "[1, 2, 3, 4, 5]",
        "example_output": "['odd', 'even', 'odd', 'even', 'odd']",
        "hints": ["Use ternary operator in comprehension", "Syntax: [expr1 if cond else expr2 for x in list]", "Check if x % 2 == 0"]
    },
    {
        "id": 75,
        "title": "Flatten 2D List",
        "description": "Flatten a 2D list into a 1D list using list comprehension.",
        "difficulty": "medium",
        "category": "list comprehension",
        "points": 25,
        "example_input": "[[1, 2], [3, 4], [5, 6]]",
        "example_output": "[1, 2, 3, 4, 5, 6]",
        "hints": ["Use nested comprehension", "Syntax: [item for sublist in matrix for item in sublist]", "Iterate outer then inner"]
    },
    {
        "id": 76,
        "title": "Dictionary from Lists",
        "description": "Create a dictionary from two lists using dict comprehension.",
        "difficulty": "medium",
        "category": "list comprehension",
        "points": 25,
        "example_input": "(['a', 'b', 'c'], [1, 2, 3])",
        "example_output": "{'a': 1, 'b': 2, 'c': 3}",
        "hints": ["Use dict comprehension", "Syntax: {k: v for k, v in zip(keys, values)}", "Combine with zip()"]
    },
    {
        "id": 77,
        "title": "Filter and Transform",
        "description": "Filter strings by length and convert to uppercase using list comprehension.",
        "difficulty": "medium",
        "category": "list comprehension",
        "points": 25,
        "example_input": "(['hi', 'hello', 'world', 'python', 'is', 'great'], 5)",
        "example_output": "['HELLO', 'WORLD', 'GREAT']",
        "hints": ["Combine filter and transform", "Check len(s) >= min_length", "Apply .upper() in same comprehension"]
    },
    {
        "id": 12,
        "title": "Complex List Transformations",
        "description": "Use list comprehension to create a dictionary from two lists, filter by conditions, and flatten nested structures.",
        "difficulty": "hard",
        "category": "list comprehension",
        "points": 40,
        "example_input": "(['a', 'b', 'c'], [1, 2, 3], [[1, 2], [3, 4], [5]])",
        "example_output": "{'dict': {'a': 1, 'b': 2, 'c': 3}, 'flattened': [1, 2, 3, 4, 5]}",
        "hints": ["Use dict comprehension {k:v for k,v in zip()}", "Use nested comprehension for flattening", "Combine multiple comprehensions"]
    },
    {
        "id": 78,
        "title": "Cartesian Product",
        "description": "Generate cartesian product of two lists using nested list comprehension.",
        "difficulty": "hard",
        "category": "list comprehension",
        "points": 40,
        "example_input": "([1, 2, 3], ['a', 'b'])",
        "example_output": "[(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]",
        "hints": ["Nested comprehension for pairs", "Syntax: [(x, y) for x in list1 for y in list2]", "Outer loop first, inner loop second"]
    },
    {
        "id": 79,
        "title": "Prime Numbers with Comprehension",
        "description": "Generate list of prime numbers up to n using list comprehension.",
        "difficulty": "hard",
        "category": "list comprehension",
        "points": 40,
        "example_input": "20",
        "example_output": "[2, 3, 5, 7, 11, 13, 17, 19]",
        "hints": ["Use nested comprehension for prime check", "Filter with all() function", "Check divisibility for each number"]
    },
    {
        "id": 80,
        "title": "Matrix Transpose",
        "description": "Transpose a matrix using list comprehension.",
        "difficulty": "hard",
        "category": "list comprehension",
        "points": 40,
        "example_input": "[[1, 2, 3], [4, 5, 6], [7, 8, 9]]",
        "example_output": "[[1, 4, 7], [2, 5, 8], [3, 6, 9]]",
        "hints": ["Use zip with unpacking", "Syntax: [[row[i] for row in matrix] for i in range(len(matrix[0]))]", "Or use list(map(list, zip(*matrix)))"]
    },
    {
        "id": 81,
        "title": "Complex Nested Filtering",
        "description": "Apply multiple filters and transformations in nested comprehensions.",
        "difficulty": "hard",
        "category": "list comprehension",
        "points": 40,
        "example_input": "[[1, 2, 3], [4, 5], [6, 7, 8, 9]]",
        "example_output": "{'evens': [2, 4, 6, 8], 'odds_squared': [1, 9, 25, 49, 81], 'sum_per_list': [6, 9, 30]}",
        "hints": ["Multiple comprehensions for different operations", "Filter evens and odds separately", "Use sum() with comprehension"]
    },

    # LAMBDAS - 15 challenges (5 easy, 5 medium, 5 hard)
    {
        "id": 13,
        "title": "Simple Lambda Operations",
        "description": "Create lambda functions for basic mathematical operations and use them with a list.",
        "difficulty": "easy",
        "category": "lambdas",
        "points": 15,
        "example_input": "[1, 2, 3, 4, 5]",
        "example_output": "[2, 4, 6, 8, 10]",
        "hints": ["Create lambda x: x * 2", "Use map() function", "Convert result to list"]
    },
    {
        "id": 82,
        "title": "Lambda with Filter",
        "description": "Use lambda with filter() to get numbers greater than a value.",
        "difficulty": "easy",
        "category": "lambdas",
        "points": 15,
        "example_input": "([1, 5, 8, 3, 10, 7], 5)",
        "example_output": "[8, 10, 7]",
        "hints": ["Use filter(lambda x: x > value, list)", "Convert to list", "Lambda returns boolean"]
    },
    {
        "id": 83,
        "title": "Lambda Sorting",
        "description": "Sort a list of tuples by second element using lambda.",
        "difficulty": "easy",
        "category": "lambdas",
        "points": 15,
        "example_input": "[('a', 3), ('b', 1), ('c', 2)]",
        "example_output": "[('b', 1), ('c', 2), ('a', 3)]",
        "hints": ["Use sorted() with key parameter", "key=lambda x: x[1]", "Returns sorted list"]
    },
    {
        "id": 84,
        "title": "Lambda Addition",
        "description": "Create a lambda function that adds a constant to each number.",
        "difficulty": "easy",
        "category": "lambdas",
        "points": 15,
        "example_input": "([1, 2, 3, 4], 10)",
        "example_output": "[11, 12, 13, 14]",
        "hints": ["Use map with lambda", "Lambda captures the constant", "Syntax: map(lambda x: x + n, list)"]
    },
    {
        "id": 85,
        "title": "Lambda String Operations",
        "description": "Use lambda to extract first character of each string.",
        "difficulty": "easy",
        "category": "lambdas",
        "points": 15,
        "example_input": "['apple', 'banana', 'cherry']",
        "example_output": "['a', 'b', 'c']",
        "hints": ["Use map with lambda", "Lambda: lambda s: s[0]", "Access first character"]
    },
    {
        "id": 14,
        "title": "Lambda Functions with Map",
        "description": "Use lambda functions with map() to convert temperatures from Celsius to Fahrenheit.",
        "difficulty": "medium",
        "category": "lambdas",
        "points": 20,
        "example_input": "[0, 20, 30, 40]",
        "example_output": "[32.0, 68.0, 86.0, 104.0]",
        "hints": ["Formula: F = C * 9/5 + 32", "Use lambda with map()", "Convert result to list"]
    },
    {
        "id": 86,
        "title": "Multiple Lambda Operations",
        "description": "Apply different lambda operations based on conditions.",
        "difficulty": "medium",
        "category": "lambdas",
        "points": 20,
        "example_input": "[1, 2, 3, 4, 5, 6]",
        "example_output": "[1, 4, 3, 8, 5, 12]",
        "hints": ["Use lambda with conditional", "Double evens, keep odds", "Syntax: lambda x: x*2 if x%2==0 else x"]
    },
    {
        "id": 87,
        "title": "Lambda with Reduce",
        "description": "Use lambda with reduce to find product of all numbers.",
        "difficulty": "medium",
        "category": "lambdas",
        "points": 20,
        "example_input": "[1, 2, 3, 4, 5]",
        "example_output": "120",
        "hints": ["Import reduce from functools", "Lambda: lambda x, y: x * y", "reduce(lambda, list)"]
    },
    {
        "id": 88,
        "title": "Nested Lambda Functions",
        "description": "Create lambda functions that return other lambda functions.",
        "difficulty": "medium",
        "category": "lambdas",
        "points": 20,
        "example_input": "5",
        "example_output": "[5, 10, 15, 20, 25]",
        "hints": ["Lambda returning lambda", "multiplier = lambda n: lambda x: x * n", "Apply to range"]
    },
    {
        "id": 89,
        "title": "Lambda Dictionary Operations",
        "description": "Use lambda to sort dictionary by values.",
        "difficulty": "medium",
        "category": "lambdas",
        "points": 20,
        "example_input": "{'a': 5, 'b': 2, 'c': 8, 'd': 1}",
        "example_output": "[('d', 1), ('b', 2), ('a', 5), ('c', 8)]",
        "hints": ["Use sorted with items()", "key=lambda x: x[1]", "Returns list of tuples"]
    },
    {
        "id": 15,
        "title": "Advanced Lambda Combinations",
        "description": "Combine lambda functions with filter, map, and reduce to process complex data transformations.",
        "difficulty": "hard",
        "category": "lambdas",
        "points": 35,
        "example_input": "[{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 17}, {'name': 'Carol', 'age': 30}]",
        "example_output": "{'adults': ['Alice', 'Carol'], 'total_age': 55}",
        "hints": ["Filter adults (age >= 18)", "Use lambda with filter and map", "Import functools for reduce"]
    },
    {
        "id": 90,
        "title": "Lambda Function Pipeline",
        "description": "Create a pipeline of lambda functions for data transformation.",
        "difficulty": "hard",
        "category": "lambdas",
        "points": 35,
        "example_input": "[1, 2, 3, 4, 5]",
        "example_output": "{'squared': [1, 4, 9, 16, 25], 'filtered': [4, 16], 'sum': 20}",
        "hints": ["Chain multiple operations", "Square, filter evens, sum", "Use map, filter, reduce in sequence"]
    },
    {
        "id": 91,
        "title": "Lambda with Custom Sorting",
        "description": "Sort complex data structures using multiple lambda criteria.",
        "difficulty": "hard",
        "category": "lambdas",
        "points": 35,
        "example_input": "[{'name': 'John', 'age': 25, 'grade': 85}, {'name': 'Alice', 'age': 25, 'grade': 90}, {'name': 'Bob', 'age': 30, 'grade': 85}]",
        "example_output": "[{'name': 'Alice', 'age': 25, 'grade': 90}, {'name': 'John', 'age': 25, 'grade': 85}, {'name': 'Bob', 'age': 30, 'grade': 85}]",
        "hints": ["Sort by multiple keys", "Use lambda with tuple", "key=lambda x: (x['age'], -x['grade'])"]
    },
    {
        "id": 92,
        "title": "Lambda Currying",
        "description": "Implement currying using lambda functions for partial application.",
        "difficulty": "hard",
        "category": "lambdas",
        "points": 35,
        "example_input": "(2, 3, 4)",
        "example_output": "24",
        "hints": ["Nested lambdas", "lambda a: lambda b: lambda c: a*b*c", "Partial function application"]
    },
    {
        "id": 93,
        "title": "Advanced Lambda Reducers",
        "description": "Use lambda with reduce for complex aggregations.",
        "difficulty": "hard",
        "category": "lambdas",
        "points": 35,
        "example_input": "['hello', 'world', 'python', 'programming']",
        "example_output": "{'longest': 'programming', 'total_chars': 27, 'concatenated': 'helloworldpythonprogramming'}",
        "hints": ["Multiple reduce operations", "Find longest with lambda", "Concatenate strings with reduce"]
    },

    # REGULAR EXPRESSIONS - 15 challenges (5 easy, 5 medium, 5 hard)
    {
        "id": 16,
        "title": "Basic Pattern Matching",
        "description": "Use regex to find all words that start with a specific letter in a text.",
        "difficulty": "easy",
        "category": "regular expressions",
        "points": 15,
        "example_input": "('The quick brown fox', 'T')",
        "example_output": "['The']",
        "hints": ["Import re module", "Use r'\\bT\\w*' pattern", "Use re.findall()"]
    },
    {
        "id": 94,
        "title": "Digit Extraction",
        "description": "Extract all digits from a string using regex.",
        "difficulty": "easy",
        "category": "regular expressions",
        "points": 15,
        "example_input": "'abc123def456'",
        "example_output": "['123', '456']",
        "hints": ["Use \\d+ pattern", "re.findall(r'\\d+', text)", "\\d matches digits"]
    },
    {
        "id": 95,
        "title": "Word Counter with Regex",
        "description": "Count total number of words in a text using regex.",
        "difficulty": "easy",
        "category": "regular expressions",
        "points": 15,
        "example_input": "'Hello world, how are you?'",
        "example_output": "5",
        "hints": ["Use \\w+ pattern", "Use re.findall()", "Count results with len()"]
    },
    {
        "id": 96,
        "title": "Replace Spaces",
        "description": "Replace all spaces with underscores using regex.",
        "difficulty": "easy",
        "category": "regular expressions",
        "points": 15,
        "example_input": "'hello world python'",
        "example_output": "'hello_world_python'",
        "hints": ["Use re.sub()", "Pattern: r' '", "Replace with '_'"]
    },
    {
        "id": 97,
        "title": "Find URLs",
        "description": "Find all URLs in a text using simple regex pattern.",
        "difficulty": "easy",
        "category": "regular expressions",
        "points": 15,
        "example_input": "'Visit https://example.com or http://test.org'",
        "example_output": "['https://example.com', 'http://test.org']",
        "hints": ["Pattern: r'https?://\\S+'", "Use re.findall()", "\\S+ matches non-whitespace"]
    },
    {
        "id": 17,
        "title": "Phone Number Extractor",
        "description": "Extract all phone numbers from a text using regular expressions.",
        "difficulty": "medium",
        "category": "regular expressions",
        "points": 30,
        "example_input": "'Call me at 123-456-7890 or 987.654.3210'",
        "example_output": "['123-456-7890', '987.654.3210']",
        "hints": ["Use re.findall()", "Pattern for digits with separators", "Handle both - and . separators"]
    },
    {
        "id": 98,
        "title": "Date Format Validator",
        "description": "Validate and extract dates in DD/MM/YYYY format.",
        "difficulty": "medium",
        "category": "regular expressions",
        "points": 30,
        "example_input": "'Today is 25/12/2023 and tomorrow is 26/12/2023'",
        "example_output": "['25/12/2023', '26/12/2023']",
        "hints": ["Pattern: r'\\d{2}/\\d{2}/\\d{4}'", "Use re.findall()", "\\d{n} matches exactly n digits"]
    },
    {
        "id": 99,
        "title": "Password Strength Checker",
        "description": "Check password strength using regex (min 8 chars, 1 upper, 1 lower, 1 digit).",
        "difficulty": "medium",
        "category": "regular expressions",
        "points": 30,
        "example_input": "'Passw0rd'",
        "example_output": "True",
        "hints": ["Use multiple patterns", "(?=.*[A-Z]) for uppercase", "Combine with re.match()"]
    },
    {
        "id": 100,
        "title": "HTML Tag Remover",
        "description": "Remove all HTML tags from text using regex.",
        "difficulty": "medium",
        "category": "regular expressions",
        "points": 30,
        "example_input": "'<p>Hello <b>world</b></p>'",
        "example_output": "'Hello world'",
        "hints": ["Pattern: r'<[^>]+>'", "Use re.sub()", "Replace with empty string"]
    },
    {
        "id": 101,
        "title": "Extract Hashtags",
        "description": "Extract all hashtags from social media text.",
        "difficulty": "medium",
        "category": "regular expressions",
        "points": 30,
        "example_input": "'Learning #python and #regex is fun! #coding'",
        "example_output": "['#python', '#regex', '#coding']",
        "hints": ["Pattern: r'#\\w+'", "Use re.findall()", "# followed by word characters"]
    },
    {
        "id": 18,
        "title": "Email Validation with Regex",
        "description": "Create a comprehensive email validator that handles various email formats and provides detailed validation results.",
        "difficulty": "hard",
        "category": "regular expressions",
        "points": 35,
        "example_input": "['user@example.com', 'invalid.email', 'test@domain.co.uk']",
        "example_output": "{'valid': ['user@example.com', 'test@domain.co.uk'], 'invalid': ['invalid.email']}",
        "hints": ["Complex email pattern with groups", "Validate domain extensions", "Handle multiple emails"]
    },
    {
        "id": 102,
        "title": "Log Parser",
        "description": "Parse log entries to extract timestamp, level, and message using regex groups.",
        "difficulty": "hard",
        "category": "regular expressions",
        "points": 35,
        "example_input": "'[2023-10-22 10:30:45] ERROR: Connection failed'",
        "example_output": "{'timestamp': '2023-10-22 10:30:45', 'level': 'ERROR', 'message': 'Connection failed'}",
        "hints": ["Use named groups (?P<name>...)", "Pattern for each component", "Use re.match() with groups()"]
    },
    {
        "id": 103,
        "title": "Advanced Text Substitution",
        "description": "Perform complex text replacements using regex with backreferences.",
        "difficulty": "hard",
        "category": "regular expressions",
        "points": 35,
        "example_input": "'John Smith, Jane Doe, Bob Johnson'",
        "example_output": "'Smith, John; Doe, Jane; Johnson, Bob'",
        "hints": ["Capture groups for names", "Use backreferences \\1, \\2", "re.sub() with replacement pattern"]
    },
    {
        "id": 104,
        "title": "SQL Injection Detector",
        "description": "Detect potential SQL injection patterns in user input.",
        "difficulty": "hard",
        "category": "regular expressions",
        "points": 35,
        "example_input": "\"SELECT * FROM users WHERE id = 1 OR '1'='1'\"",
        "example_output": "{'dangerous': True, 'patterns': ['OR', 'quotes'], 'risk_level': 'high'}",
        "hints": ["Multiple patterns for SQL keywords", "Check for quote manipulation", "Detect UNION, DROP, etc."]
    },
    {
        "id": 105,
        "title": "Regex-based Tokenizer",
        "description": "Create a tokenizer that splits code into tokens using regex.",
        "difficulty": "hard",
        "category": "regular expressions",
        "points": 35,
        "example_input": "'x = 10 + y * 2'",
        "example_output": "['x', '=', '10', '+', 'y', '*', '2']",
        "hints": ["Pattern for identifiers, numbers, operators", "Use re.findall() with multiple patterns", "Handle different token types"]
    },

    # FILE HANDLING - 15 challenges (5 easy, 5 medium, 5 hard)
    {
        "id": 19,
        "title": "Simple File Reader",
        "description": "Read the content of a text file and return it as a string.",
        "difficulty": "easy",
        "category": "file handling",
        "points": 15,
        "example_input": "'sample.txt'",
        "example_output": "'Hello World\\nThis is a test file.'",
        "hints": ["Use open() with 'r' mode", "Use read() method", "Handle FileNotFoundError"]
    },
    {
        "id": 106,
        "title": "File Line Counter",
        "description": "Count the number of lines in a text file.",
        "difficulty": "easy",
        "category": "file handling",
        "points": 15,
        "example_input": "'data.txt'",
        "example_output": "42",
        "hints": ["Use open() and readlines()", "Use len() on lines list", "Or iterate and count"]
    },
    {
        "id": 107,
        "title": "File Writer",
        "description": "Write a list of strings to a file, one per line.",
        "difficulty": "easy",
        "category": "file handling",
        "points": 15,
        "example_input": "(['Line 1', 'Line 2', 'Line 3'], 'output.txt')",
        "example_output": "'File written successfully'",
        "hints": ["Use open() with 'w' mode", "Use write() or writelines()", "Add newlines with '\\n'"]
    },
    {
        "id": 108,
        "title": "File Append",
        "description": "Append text to an existing file without overwriting.",
        "difficulty": "easy",
        "category": "file handling",
        "points": 15,
        "example_input": "('New line\\n', 'log.txt')",
        "example_output": "'Text appended successfully'",
        "hints": ["Use open() with 'a' mode", "Use write() method", "Mode 'a' appends to file"]
    },
    {
        "id": 109,
        "title": "File Existence Checker",
        "description": "Check if a file exists and return file size if it does.",
        "difficulty": "easy",
        "category": "file handling",
        "points": 15,
        "example_input": "'data.txt'",
        "example_output": "{'exists': True, 'size': 1024}",
        "hints": ["Use os.path.exists()", "Use os.path.getsize()", "Return dictionary with info"]
    },
    {
        "id": 20,
        "title": "File Word Counter",
        "description": "Read a text file and count the number of words, lines, and characters in it.",
        "difficulty": "medium",
        "category": "file handling",
        "points": 25,
        "example_input": "'sample.txt'",
        "example_output": "{'words': 42, 'lines': 5, 'characters': 235}",
        "hints": ["Use open() with 'r' mode", "Use split() for words", "Count newlines for lines"]
    },
    {
        "id": 110,
        "title": "CSV File Reader",
        "description": "Read a CSV file and return data as list of dictionaries.",
        "difficulty": "medium",
        "category": "file handling",
        "points": 25,
        "example_input": "'data.csv'",
        "example_output": "[{'name': 'John', 'age': '25'}, {'name': 'Jane', 'age': '30'}]",
        "hints": ["Import csv module", "Use csv.DictReader()", "Return list of rows"]
    },
    {
        "id": 111,
        "title": "File Search and Replace",
        "description": "Search for a pattern in file and replace it with new text.",
        "difficulty": "medium",
        "category": "file handling",
        "points": 25,
        "example_input": "('old_text', 'new_text', 'file.txt')",
        "example_output": "'Replaced 3 occurrences'",
        "hints": ["Read entire file", "Use string replace()", "Write back to file"]
    },
    {
        "id": 112,
        "title": "Directory File Lister",
        "description": "List all files in a directory with their sizes.",
        "difficulty": "medium",
        "category": "file handling",
        "points": 25,
        "example_input": "'./data'",
        "example_output": "[{'name': 'file1.txt', 'size': 1024}, {'name': 'file2.txt', 'size': 2048}]",
        "hints": ["Use os.listdir()", "Use os.path.getsize()", "Filter directories"]
    },
    {
        "id": 113,
        "title": "File Copy with Progress",
        "description": "Copy a file and report progress percentage.",
        "difficulty": "medium",
        "category": "file handling",
        "points": 25,
        "example_input": "('source.txt', 'dest.txt')",
        "example_output": "{'success': True, 'bytes_copied': 1024}",
        "hints": ["Read in chunks", "Track bytes copied", "Use shutil or manual copy"]
    },
    {
        "id": 21,
        "title": "JSON File Manager",
        "description": "Read a JSON file, modify its content based on conditions, and write it back with proper error handling.",
        "difficulty": "hard",
        "category": "file handling",
        "points": 40,
        "example_input": "('data.json', {'operation': 'update', 'key': 'age', 'value': 26})",
        "example_output": "'File updated successfully. Modified 1 record.'",
        "hints": ["Use json.load() and json.dump()", "Handle JSON decode errors", "Implement backup functionality"]
    },
    {
        "id": 114,
        "title": "Log File Analyzer",
        "description": "Analyze log file to extract errors, warnings, and statistics.",
        "difficulty": "hard",
        "category": "file handling",
        "points": 40,
        "example_input": "'app.log'",
        "example_output": "{'errors': 5, 'warnings': 12, 'info': 150, 'time_range': '2023-10-22 08:00 to 18:00'}",
        "hints": ["Parse log format", "Count by severity", "Extract timestamps"]
    },
    {
        "id": 115,
        "title": "File Merger",
        "description": "Merge multiple files into one, removing duplicates and sorting.",
        "difficulty": "hard",
        "category": "file handling",
        "points": 40,
        "example_input": "(['file1.txt', 'file2.txt', 'file3.txt'], 'merged.txt')",
        "example_output": "{'lines_merged': 150, 'duplicates_removed': 25}",
        "hints": ["Read all files", "Use set for duplicates", "Sort and write"]
    },
    {
        "id": 116,
        "title": "Binary File Handler",
        "description": "Read and write binary files, implement file encryption/decryption.",
        "difficulty": "hard",
        "category": "file handling",
        "points": 40,
        "example_input": "('image.png', 'rb')",
        "example_output": "{'size': 15360, 'type': 'binary', 'readable': True}",
        "hints": ["Use 'rb' and 'wb' modes", "Read bytes", "Handle binary data"]
    },
    {
        "id": 117,
        "title": "Configuration File Manager",
        "description": "Read, update, and validate configuration files in multiple formats (JSON, INI, YAML).",
        "difficulty": "hard",
        "category": "file handling",
        "points": 40,
        "example_input": "('config.ini', {'database': {'host': 'localhost'}})",
        "example_output": "{'updated': True, 'format': 'ini', 'sections': ['database', 'server']}",
        "hints": ["Use configparser for INI", "Handle different formats", "Validate structure"]
    },

    # PACKAGE MANAGEMENT - 15 challenges (5 easy, 5 medium, 5 hard)
    {
        "id": 22,
        "title": "Basic Package Usage",
        "description": "Import and use basic Python modules (math, random, datetime) in a single function.",
        "difficulty": "easy",
        "category": "package management",
        "points": 15,
        "example_input": "5",
        "example_output": "{'sqrt': 2.236, 'random': 0.753, 'now': '2023-10-22 10:30:45'}",
        "hints": ["Import math, random, datetime", "Use math.sqrt()", "Use random.random() and datetime.now()"]
    },
    {
        "id": 118,
        "title": "Random Number Generator",
        "description": "Use random module to generate different types of random values.",
        "difficulty": "easy",
        "category": "package management",
        "points": 15,
        "example_input": "(1, 100, 5)",
        "example_output": "[23, 67, 12, 89, 45]",
        "hints": ["Import random", "Use random.randint()", "Generate n random numbers"]
    },
    {
        "id": 119,
        "title": "Math Operations",
        "description": "Use math module for trigonometric and logarithmic operations.",
        "difficulty": "easy",
        "category": "package management",
        "points": 15,
        "example_input": "45",
        "example_output": "{'sin': 0.707, 'cos': 0.707, 'log': 3.807}",
        "hints": ["Import math", "Use math.sin(), math.cos()", "Convert degrees to radians"]
    },
    {
        "id": 120,
        "title": "Time Module Usage",
        "description": "Use time module to measure execution time and create delays.",
        "difficulty": "easy",
        "category": "package management",
        "points": 15,
        "example_input": "0.5",
        "example_output": "{'elapsed': 0.501, 'timestamp': 1698062400.0}",
        "hints": ["Import time", "Use time.time()", "Use time.sleep() for delay"]
    },
    {
        "id": 121,
        "title": "Collections Module",
        "description": "Use Counter from collections to count element frequencies.",
        "difficulty": "easy",
        "category": "package management",
        "points": 15,
        "example_input": "['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']",
        "example_output": "{'apple': 3, 'banana': 2, 'cherry': 1}",
        "hints": ["Import Counter from collections", "Pass list to Counter()", "Convert to dict if needed"]
    },
    {
        "id": 23,
        "title": "Package Import Challenge",
        "description": "Create a function that imports and uses multiple Python packages (json, os, sys) to gather system information.",
        "difficulty": "medium",
        "category": "package management",
        "points": 25,
        "example_input": "{'name': 'test'}",
        "example_output": "{'current_dir': '/path', 'python_version': '3.9.0', 'json_data': '{\"name\": \"test\"}'}",
        "hints": ["Import json, os, sys", "Use os.getcwd()", "Use sys.version and json.dumps()"]
    },
    {
        "id": 122,
        "title": "Statistics Module",
        "description": "Use statistics module to calculate mean, median, and standard deviation.",
        "difficulty": "medium",
        "category": "package management",
        "points": 25,
        "example_input": "[10, 20, 30, 40, 50]",
        "example_output": "{'mean': 30.0, 'median': 30, 'stdev': 15.811}",
        "hints": ["Import statistics", "Use statistics.mean()", "Use statistics.median() and stdev()"]
    },
    {
        "id": 123,
        "title": "Regular Expression Module",
        "description": "Use re module for pattern matching and text processing.",
        "difficulty": "medium",
        "category": "package management",
        "points": 25,
        "example_input": "'Contact: email@example.com or phone 123-456-7890'",
        "example_output": "{'emails': ['email@example.com'], 'phones': ['123-456-7890']}",
        "hints": ["Import re", "Use re.findall()", "Create patterns for email and phone"]
    },
    {
        "id": 124,
        "title": "UUID Generator",
        "description": "Use uuid module to generate different types of unique identifiers.",
        "difficulty": "medium",
        "category": "package management",
        "points": 25,
        "example_input": "3",
        "example_output": "['550e8400-e29b-41d4-a716-446655440000', '6ba7b810-9dad-11d1-80b4-00c04fd430c8', '7c9e6679-7425-40de-944b-e07fc1f90ae7']",
        "hints": ["Import uuid", "Use uuid.uuid4()", "Generate n unique ids"]
    },
    {
        "id": 125,
        "title": "Itertools Module",
        "description": "Use itertools for combinations, permutations, and product operations.",
        "difficulty": "medium",
        "category": "package management",
        "points": 25,
        "example_input": "[1, 2, 3]",
        "example_output": "{'combinations': [(1, 2), (1, 3), (2, 3)], 'permutations': 6}",
        "hints": ["Import itertools", "Use itertools.combinations()", "Use itertools.permutations()"]
    },
    {
        "id": 24,
        "title": "Advanced Package Integration",
        "description": "Create a utility that combines multiple packages (pathlib, collections, itertools) for advanced file and data operations.",
        "difficulty": "hard",
        "category": "package management",
        "points": 40,
        "example_input": "['/path/file1.txt', '/path/file2.txt', '/other/file3.txt']",
        "example_output": "{'grouped_by_dir': {'/path': 2, '/other': 1}, 'extensions': {'txt': 3}, 'combinations': [('file1.txt', 'file2.txt')]}",
        "hints": ["Use pathlib for path operations", "Use collections.Counter", "Use itertools.combinations"]
    },
    {
        "id": 126,
        "title": "Logging System",
        "description": "Implement a logging system using the logging module with multiple handlers.",
        "difficulty": "hard",
        "category": "package management",
        "points": 40,
        "example_input": "('app.log', 'INFO')",
        "example_output": "{'logger_configured': True, 'handlers': ['file', 'console'], 'level': 'INFO'}",
        "hints": ["Import logging", "Configure logger", "Add file and stream handlers"]
    },
    {
        "id": 127,
        "title": "Pickle Serialization",
        "description": "Use pickle to serialize and deserialize complex Python objects.",
        "difficulty": "hard",
        "category": "package management",
        "points": 40,
        "example_input": "{'name': 'John', 'scores': [85, 90, 78], 'metadata': {'id': 123}}",
        "example_output": "{'serialized': True, 'deserialized': True, 'data_match': True}",
        "hints": ["Import pickle", "Use pickle.dumps() and pickle.loads()", "Handle complex structures"]
    },
    {
        "id": 128,
        "title": "Multi-module Data Pipeline",
        "description": "Create a data processing pipeline using csv, json, pickle, and collections.",
        "difficulty": "hard",
        "category": "package management",
        "points": 40,
        "example_input": "'data.csv'",
        "example_output": "{'csv_rows': 100, 'json_export': True, 'pickle_cache': True, 'statistics': {...}}",
        "hints": ["Chain multiple modules", "Convert between formats", "Use collections for stats"]
    },
    {
        "id": 129,
        "title": "Threading and Multiprocessing",
        "description": "Use threading and multiprocessing modules for parallel execution.",
        "difficulty": "hard",
        "category": "package management",
        "points": 40,
        "example_input": "[1, 2, 3, 4, 5]",
        "example_output": "{'threaded_time': 1.23, 'multiprocess_time': 0.45, 'results': [1, 4, 9, 16, 25]}",
        "hints": ["Import threading and multiprocessing", "Compare execution times", "Use Pool for multiprocessing"]
    },

    # DATES - 15 challenges (5 easy, 5 medium, 5 hard)
    {
        "id": 25,
        "title": "Simple Date Operations",
        "description": "Calculate age in years given a birth date.",
        "difficulty": "easy",
        "category": "dates",
        "points": 15,
        "example_input": "'1990-05-15'",
        "example_output": "33",
        "hints": ["Import datetime", "Use datetime.strptime()", "Calculate difference with today"]
    },
    {
        "id": 130,
        "title": "Current Date and Time",
        "description": "Get current date and time in different formats.",
        "difficulty": "easy",
        "category": "dates",
        "points": 15,
        "example_input": "None",
        "example_output": "{'iso': '2023-10-22T10:30:45', 'formatted': '22/10/2023 10:30:45', 'timestamp': 1698062445}",
        "hints": ["Import datetime", "Use datetime.now()", "Use strftime() for formatting"]
    },
    {
        "id": 131,
        "title": "Days Until Event",
        "description": "Calculate days remaining until a future date.",
        "difficulty": "easy",
        "category": "dates",
        "points": 15,
        "example_input": "'2024-12-31'",
        "example_output": "435",
        "hints": ["Parse future date", "Subtract from today", "Access .days attribute"]
    },
    {
        "id": 132,
        "title": "Day of Week",
        "description": "Find the day of week for a given date.",
        "difficulty": "easy",
        "category": "dates",
        "points": 15,
        "example_input": "'2023-10-22'",
        "example_output": "'Sunday'",
        "hints": ["Use datetime.strptime()", "Use .strftime('%A')", "Or use .weekday() with mapping"]
    },
    {
        "id": 133,
        "title": "Add Days to Date",
        "description": "Add a specified number of days to a date.",
        "difficulty": "easy",
        "category": "dates",
        "points": 15,
        "example_input": "('2023-10-22', 7)",
        "example_output": "'2023-10-29'",
        "hints": ["Import timedelta", "Parse date", "Add timedelta(days=n)"]
    },
    {
        "id": 26,
        "title": "Date Calculator",
        "description": "Calculate the number of days, weeks, and months between two dates.",
        "difficulty": "medium",
        "category": "dates",
        "points": 30,
        "example_input": "('2023-01-01', '2023-12-31')",
        "example_output": "{'days': 364, 'weeks': 52, 'months': 12}",
        "hints": ["Import datetime", "Use datetime.strptime()", "Calculate different time units"]
    },
    {
        "id": 134,
        "title": "Date Range Generator",
        "description": "Generate all dates in a range with specified interval.",
        "difficulty": "medium",
        "category": "dates",
        "points": 30,
        "example_input": "('2023-10-01', '2023-10-07', 1)",
        "example_output": "['2023-10-01', '2023-10-02', '2023-10-03', '2023-10-04', '2023-10-05', '2023-10-06', '2023-10-07']",
        "hints": ["Use timedelta for increment", "Loop from start to end", "Yield or append each date"]
    },
    {
        "id": 135,
        "title": "Working Days Calculator",
        "description": "Calculate number of working days (Monday-Friday) between two dates.",
        "difficulty": "medium",
        "category": "dates",
        "points": 30,
        "example_input": "('2023-10-16', '2023-10-27')",
        "example_output": "9",
        "hints": ["Use .weekday() method", "0-4 are Monday-Friday", "Count days excluding weekends"]
    },
    {
        "id": 136,
        "title": "Time Until Deadline",
        "description": "Calculate time remaining until deadline in days, hours, minutes.",
        "difficulty": "medium",
        "category": "dates",
        "points": 30,
        "example_input": "'2023-12-31 23:59:59'",
        "example_output": "{'days': 70, 'hours': 13, 'minutes': 29, 'seconds': 14}",
        "hints": ["Parse datetime with time", "Calculate timedelta", "Extract components"]
    },
    {
        "id": 137,
        "title": "Month Name Converter",
        "description": "Convert between month numbers and names, handle different locales.",
        "difficulty": "medium",
        "category": "dates",
        "points": 30,
        "example_input": "10",
        "example_output": "{'english': 'October', 'spanish': 'Octubre', 'abbr': 'Oct'}",
        "hints": ["Use calendar module", "Use strftime('%B') for name", "Handle localization"]
    },
    {
        "id": 27,
        "title": "Advanced Date Processing",
        "description": "Process a list of dates to find patterns, calculate business days, and handle different timezones.",
        "difficulty": "hard",
        "category": "dates",
        "points": 40,
        "example_input": "['2023-01-01', '2023-01-07', '2023-01-15']",
        "example_output": "{'weekends': 1, 'business_days': 10, 'average_gap': 7.0}",
        "hints": ["Use datetime.weekday()", "Handle weekend detection", "Calculate business days excluding weekends"]
    },
    {
        "id": 138,
        "title": "Timezone Converter",
        "description": "Convert times between different timezones.",
        "difficulty": "hard",
        "category": "dates",
        "points": 40,
        "example_input": "('2023-10-22 10:00:00', 'UTC', 'America/New_York')",
        "example_output": "'2023-10-22 06:00:00'",
        "hints": ["Use pytz or zoneinfo", "Create timezone-aware datetime", "Convert using astimezone()"]
    },
    {
        "id": 139,
        "title": "Recurring Date Generator",
        "description": "Generate recurring dates based on pattern (daily, weekly, monthly).",
        "difficulty": "hard",
        "category": "dates",
        "points": 40,
        "example_input": "('2023-10-01', 'weekly', 5)",
        "example_output": "['2023-10-01', '2023-10-08', '2023-10-15', '2023-10-22', '2023-10-29']",
        "hints": ["Use timedelta with different intervals", "Handle monthly differently", "Support multiple patterns"]
    },
    {
        "id": 140,
        "title": "Holiday Calculator",
        "description": "Calculate holidays and check if date is a holiday for a given country.",
        "difficulty": "hard",
        "category": "dates",
        "points": 40,
        "example_input": "('2023-12-25', 'US')",
        "example_output": "{'is_holiday': True, 'name': 'Christmas Day', 'observed': '2023-12-25'}",
        "hints": ["Define holiday rules", "Handle movable holidays", "Support different countries"]
    },
    {
        "id": 141,
        "title": "Age Calculator with Precision",
        "description": "Calculate age with years, months, and days precision.",
        "difficulty": "hard",
        "category": "dates",
        "points": 40,
        "example_input": "'1990-05-15'",
        "example_output": "{'years': 33, 'months': 5, 'days': 7, 'total_days': 12234}",
        "hints": ["Calculate year difference", "Handle month and day differences", "Account for leap years"]
    },

    # ERROR TYPES - 15 challenges (5 easy, 5 medium, 5 hard)
    {
        "id": 28,
        "title": "Basic Exception Handling",
        "description": "Handle a simple division by zero error and return a user-friendly message.",
        "difficulty": "easy",
        "category": "error types",
        "points": 15,
        "example_input": "(10, 0)",
        "example_output": "'Error: Cannot divide by zero'",
        "hints": ["Use try/except", "Catch ZeroDivisionError", "Return descriptive message"]
    },
    {
        "id": 142,
        "title": "File Not Found Handler",
        "description": "Handle FileNotFoundError when trying to read a non-existent file.",
        "difficulty": "easy",
        "category": "error types",
        "points": 15,
        "example_input": "'nonexistent.txt'",
        "example_output": "'Error: File not found'",
        "hints": ["Use try/except", "Catch FileNotFoundError", "Return error message"]
    },
    {
        "id": 143,
        "title": "Type Error Catcher",
        "description": "Handle TypeError when performing invalid operations.",
        "difficulty": "easy",
        "category": "error types",
        "points": 15,
        "example_input": "('5', 3)",
        "example_output": "'Error: Invalid type for operation'",
        "hints": ["Catch TypeError", "Try to add string and int", "Return friendly message"]
    },
    {
        "id": 144,
        "title": "Value Error Handler",
        "description": "Handle ValueError when converting invalid string to number.",
        "difficulty": "easy",
        "category": "error types",
        "points": 15,
        "example_input": "'abc'",
        "example_output": "'Error: Cannot convert to number'",
        "hints": ["Try int() conversion", "Catch ValueError", "Return error message"]
    },
    {
        "id": 145,
        "title": "Index Error Handler",
        "description": "Handle IndexError when accessing list with invalid index.",
        "difficulty": "easy",
        "category": "error types",
        "points": 15,
        "example_input": "([1, 2, 3], 10)",
        "example_output": "'Error: Index out of range'",
        "hints": ["Try to access list[index]", "Catch IndexError", "Return error message"]
    },
    {
        "id": 29,
        "title": "Multiple Exception Types",
        "description": "Handle different types of errors (ValueError, TypeError, ZeroDivisionError) in a calculator function.",
        "difficulty": "medium",
        "category": "error types",
        "points": 25,
        "example_input": "('abc', '5', '+')",
        "example_output": "'ValueError: Invalid number format'",
        "hints": ["Use multiple except blocks", "Handle string to number conversion", "Identify specific error types"]
    },
    {
        "id": 146,
        "title": "JSON Parse Error Handler",
        "description": "Handle JSONDecodeError when parsing invalid JSON.",
        "difficulty": "medium",
        "category": "error types",
        "points": 25,
        "example_input": "'{invalid json}'",
        "example_output": "{'success': False, 'error': 'Invalid JSON format', 'type': 'JSONDecodeError'}",
        "hints": ["Import json", "Try json.loads()", "Catch json.JSONDecodeError"]
    },
    {
        "id": 147,
        "title": "Key Error Handler",
        "description": "Handle KeyError when accessing missing dictionary keys.",
        "difficulty": "medium",
        "category": "error types",
        "points": 25,
        "example_input": "({'name': 'John'}, 'age')",
        "example_output": "'Error: Key not found, using default value: 0'",
        "hints": ["Try to access dict key", "Catch KeyError", "Provide default value"]
    },
    {
        "id": 148,
        "title": "Import Error Handler",
        "description": "Handle ImportError when module is not available.",
        "difficulty": "medium",
        "category": "error types",
        "points": 25,
        "example_input": "'nonexistent_module'",
        "example_output": "{'imported': False, 'error': 'Module not found', 'fallback': True}",
        "hints": ["Try to import module", "Catch ImportError", "Provide fallback"]
    },
    {
        "id": 149,
        "title": "Attribute Error Handler",
        "description": "Handle AttributeError when accessing non-existent attributes.",
        "difficulty": "medium",
        "category": "error types",
        "points": 25,
        "example_input": "('hello', 'nonexistent_method')",
        "example_output": "'Error: Attribute does not exist'",
        "hints": ["Try getattr()", "Catch AttributeError", "Check with hasattr()"]
    },
    {
        "id": 30,
        "title": "Exception Handler",
        "description": "Create a robust error handling system that logs errors, provides user feedback, and implements retry mechanisms.",
        "difficulty": "hard",
        "category": "error types",
        "points": 40,
        "example_input": "{'operation': 'divide', 'a': '10', 'b': '0', 'retries': 3}",
        "example_output": "{'success': False, 'error': 'ZeroDivisionError', 'attempts': 3, 'message': 'Operation failed after 3 attempts'}",
        "hints": ["Implement retry logic", "Log error details", "Create custom exceptions"]
    },
    {
        "id": 150,
        "title": "Custom Exception Class",
        "description": "Create custom exception classes with detailed error information.",
        "difficulty": "hard",
        "category": "error types",
        "points": 40,
        "example_input": "{'value': -5, 'operation': 'sqrt'}",
        "example_output": "{'error': 'NegativeValueError', 'message': 'Cannot calculate sqrt of negative number', 'value': -5}",
        "hints": ["Define custom exception class", "Inherit from Exception", "Add custom attributes"]
    },
    {
        "id": 151,
        "title": "Context Manager Error Handling",
        "description": "Implement context manager with proper error handling and cleanup.",
        "difficulty": "hard",
        "category": "error types",
        "points": 40,
        "example_input": "'resource.txt'",
        "example_output": "{'opened': True, 'processed': True, 'closed': True, 'errors': []}",
        "hints": ["Use __enter__ and __exit__", "Handle errors in __exit__", "Ensure cleanup"]
    },
    {
        "id": 152,
        "title": "Error Recovery System",
        "description": "Build error recovery system with fallback strategies.",
        "difficulty": "hard",
        "category": "error types",
        "points": 40,
        "example_input": "['primary.db', 'backup.db', 'fallback.db']",
        "example_output": "{'connected': 'backup.db', 'attempts': 2, 'fallbacks_used': 1}",
        "hints": ["Try multiple sources", "Implement fallback chain", "Track attempts"]
    },
    {
        "id": 153,
        "title": "Exception Chaining",
        "description": "Implement exception chaining to preserve error context.",
        "difficulty": "hard",
        "category": "error types",
        "points": 40,
        "example_input": "{'data': 'invalid', 'strict': True}",
        "example_output": "{'error_chain': ['ValueError', 'DataProcessingError'], 'original': 'invalid literal', 'context': 'preserved'}",
        "hints": ["Use 'raise ... from ...'", "Preserve original exception", "Chain multiple errors"]
    },

    # HIGHER ORDER FUNCTIONS - 15 challenges (5 easy, 5 medium, 5 hard)
    {
        "id": 31,
        "title": "Simple Higher Order Function",
        "description": "Create a function that takes another function as parameter and applies it to a number.",
        "difficulty": "easy",
        "category": "higher order functions",
        "points": 15,
        "example_input": "(lambda x: x * 2, 5)",
        "example_output": "10",
        "hints": ["Function should accept function parameter", "Call the passed function", "Return the result"]
    },
    {
        "id": 154,
        "title": "Map Function Implementation",
        "description": "Implement a custom map function that applies a function to each element.",
        "difficulty": "easy",
        "category": "higher order functions",
        "points": 15,
        "example_input": "(lambda x: x ** 2, [1, 2, 3, 4])",
        "example_output": "[1, 4, 9, 16]",
        "hints": ["Create custom_map function", "Iterate through list", "Apply function to each element"]
    },
    {
        "id": 155,
        "title": "Filter Implementation",
        "description": "Implement a custom filter function.",
        "difficulty": "easy",
        "category": "higher order functions",
        "points": 15,
        "example_input": "(lambda x: x > 5, [1, 6, 3, 8, 2, 9])",
        "example_output": "[6, 8, 9]",
        "hints": ["Create custom_filter function", "Check condition for each element", "Include only if condition is True"]
    },
    {
        "id": 156,
        "title": "Function Multiplier",
        "description": "Create a function that returns a multiplier function.",
        "difficulty": "easy",
        "category": "higher order functions",
        "points": 15,
        "example_input": "3",
        "example_output": "15",
        "hints": ["Return a function from function", "Closure captures multiplier", "Apply to value"]
    },
    {
        "id": 157,
        "title": "Reduce Implementation",
        "description": "Implement a custom reduce function.",
        "difficulty": "easy",
        "category": "higher order functions",
        "points": 15,
        "example_input": "(lambda x, y: x + y, [1, 2, 3, 4], 0)",
        "example_output": "10",
        "hints": ["Start with initial value", "Apply function cumulatively", "Return final result"]
    },
    {
        "id": 32,
        "title": "Function Composition",
        "description": "Create a higher-order function that composes two functions and applies them to a list.",
        "difficulty": "medium",
        "category": "higher order functions",
        "points": 25,
        "example_input": "(lambda x: x + 1, lambda x: x * 2, [1, 2, 3])",
        "example_output": "[4, 6, 8]",
        "hints": ["Compose functions f(g(x))", "Apply to each list element", "Return transformed list"]
    },
    {
        "id": 158,
        "title": "Partial Function Application",
        "description": "Implement partial function application (currying).",
        "difficulty": "medium",
        "category": "higher order functions",
        "points": 25,
        "example_input": "(lambda x, y, z: x + y + z, 10)",
        "example_output": "60",
        "hints": ["Fix first argument", "Return function accepting remaining args", "Apply partial application"]
    },
    {
        "id": 159,
        "title": "Memoization Decorator",
        "description": "Create a memoization decorator for caching function results.",
        "difficulty": "medium",
        "category": "higher order functions",
        "points": 25,
        "example_input": "fibonacci(35)",
        "example_output": "{'result': 9227465, 'cache_hits': 33, 'cache_size': 36}",
        "hints": ["Use decorator pattern", "Cache results in dict", "Check cache before computing"]
    },
    {
        "id": 160,
        "title": "Retry Decorator",
        "description": "Create a decorator that retries a function on failure.",
        "difficulty": "medium",
        "category": "higher order functions",
        "points": 25,
        "example_input": "(unstable_function, 3)",
        "example_output": "{'success': True, 'attempts': 2, 'result': 'Success'}",
        "hints": ["Wrap function with try/except", "Implement retry loop", "Track attempts"]
    },
    {
        "id": 161,
        "title": "Timing Decorator",
        "description": "Create a decorator to measure function execution time.",
        "difficulty": "medium",
        "category": "higher order functions",
        "points": 25,
        "example_input": "slow_function()",
        "example_output": "{'result': 42, 'execution_time': 1.234, 'function': 'slow_function'}",
        "hints": ["Import time", "Record start and end time", "Return result with timing"]
    },
    {
        "id": 33,
        "title": "Higher Order Functions",
        "description": "Implement a decorator factory and function pipeline that can transform, filter, and reduce data with configurable operations.",
        "difficulty": "hard",
        "category": "higher order functions",
        "points": 35,
        "example_input": "([1, 2, 3, 4, 5], [lambda x: x*2, lambda x: x > 5, sum])",
        "example_output": "{'transformed': [2, 4, 6, 8, 10], 'filtered': [6, 8, 10], 'reduced': 24}",
        "hints": ["Chain multiple function operations", "Implement pipeline pattern", "Use *args for variable functions"]
    },
    {
        "id": 162,
        "title": "Function Pipeline Builder",
        "description": "Build a composable function pipeline with multiple operations.",
        "difficulty": "hard",
        "category": "higher order functions",
        "points": 35,
        "example_input": "[lambda x: x * 2, lambda x: x + 1, lambda x: x ** 2]",
        "example_output": "121",
        "hints": ["Chain functions left to right", "Apply each function to previous result", "Support variable number of functions"]
    },
    {
        "id": 163,
        "title": "Decorator with Arguments",
        "description": "Create a decorator factory that accepts arguments.",
        "difficulty": "hard",
        "category": "higher order functions",
        "points": 35,
        "example_input": "(@repeat(3), hello)",
        "example_output": "['Hello!', 'Hello!', 'Hello!']",
        "hints": ["Decorator returns decorator", "Three levels of nesting", "Outer function accepts arguments"]
    },
    {
        "id": 164,
        "title": "Function Dispatcher",
        "description": "Create a dispatcher that routes to different functions based on type.",
        "difficulty": "hard",
        "category": "higher order functions",
        "points": 35,
        "example_input": "{'int': process_int, 'str': process_str, 'list': process_list}",
        "example_output": "{'dispatched': True, 'handler': 'process_int', 'result': 42}",
        "hints": ["Map types to handlers", "Detect input type", "Call appropriate function"]
    },
    {
        "id": 165,
        "title": "Lazy Evaluation Pipeline",
        "description": "Implement lazy evaluation with generators in function pipeline.",
        "difficulty": "hard",
        "category": "higher order functions",
        "points": 35,
        "example_input": "range(1000000)",
        "example_output": "{'memory_efficient': True, 'first_10_results': [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]}",
        "hints": ["Use generators", "Yield instead of return", "Chain generator functions"]
    }
]

# Spanish challenges database
CHALLENGES_DB_ES = [
    # MATEMÁTICAS - Fácil
    {
        "id": 1,
        "title": "Suma de Dos Números",
        "description": "Escribe una función que sume dos números y devuelva el resultado.",
        "difficulty": "easy",
        "category": "matemáticas",
        "points": 10,
        "example_input": "3, 5",
        "example_output": "8",
        "hints": ["Usa el operador +", "Los parámetros son números enteros"]
    },
    {
        "id": 2,
        "title": "Número Par o Impar",
        "description": "Determina si un número dado es par o impar.",
        "difficulty": "easy",
        "category": "matemáticas",
        "points": 10,
        "example_input": "4",
        "example_output": "True (es par)",
        "hints": ["Usa el operador módulo %", "Un número par es divisible por 2"]
    },
    {
        "id": 3,
        "title": "Factorial Simple",
        "description": "Calcula el factorial de un número usando un bucle.",
        "difficulty": "easy",
        "category": "matemáticas",
        "points": 10,
        "example_input": "5",
        "example_output": "120",
        "hints": ["Factorial de n = n * (n-1) * (n-2) * ... * 1", "Usa un bucle for o while"]
    },
    {
        "id": 4,
        "title": "Máximo de Tres",
        "description": "Encuentra el máximo de tres números dados.",
        "difficulty": "easy",
        "category": "matemáticas",
        "points": 10,
        "example_input": "3, 7, 5",
        "example_output": "7",
        "hints": ["Usa la función max() incorporada", "O compara usando if-else"]
    },
    {
        "id": 5,
        "title": "Valor Absoluto",
        "description": "Devuelve el valor absoluto de un número sin usar abs().",
        "difficulty": "easy",
        "category": "matemáticas",
        "points": 10,
        "example_input": "-5",
        "example_output": "5",
        "hints": ["Si el número es negativo, multiplícalo por -1", "Usa una declaración if"]
    },
    
    # MATEMÁTICAS - Medio
    {
        "id": 6,
        "title": "Verificador de Números Primos",
        "description": "Verifica si un número es primo.",
        "difficulty": "medium",
        "category": "matemáticas",
        "points": 20,
        "example_input": "17",
        "example_output": "True",
        "hints": ["Un primo solo es divisible por 1 y por sí mismo", "Verifica divisibilidad hasta la raíz cuadrada"]
    },
    {
        "id": 7,
        "title": "Secuencia de Fibonacci",
        "description": "Genera los primeros n números de Fibonacci.",
        "difficulty": "medium",
        "category": "matemáticas",
        "points": 20,
        "example_input": "7",
        "example_output": "[0, 1, 1, 2, 3, 5, 8]",
        "hints": ["Cada número es la suma de los dos anteriores", "Comienza con 0, 1"]
    },
    {
        "id": 8,
        "title": "Máximo Común Divisor",
        "description": "Encuentra el MCD de dos números usando el algoritmo de Euclides.",
        "difficulty": "medium",
        "category": "matemáticas",
        "points": 20,
        "example_input": "48, 18",
        "example_output": "6",
        "hints": ["Usa el algoritmo de Euclides", "MCD(a,b) = MCD(b, a%b)"]
    },
    {
        "id": 9,
        "title": "Exponenciación Rápida",
        "description": "Implementa exponenciación eficiente usando recursión.",
        "difficulty": "medium",
        "category": "matemáticas",
        "points": 20,
        "example_input": "2, 10",
        "example_output": "1024",
        "hints": ["Usa exponenciación por cuadratura", "Si el exponente es par, eleva al cuadrado el resultado"]
    },
    {
        "id": 10,
        "title": "Dígitos Perfectos",
        "description": "Verifica si un número es igual a la suma de sus dígitos elevados a la potencia del número de dígitos.",
        "difficulty": "medium",
        "category": "matemáticas",
        "points": 20,
        "example_input": "153",
        "example_output": "True (1^3 + 5^3 + 3^3 = 153)",
        "hints": ["Convierte el número a cadena para obtener dígitos", "153 es un número de Armstrong"]
    },
    
    # MATEMÁTICAS - Difícil
    {
        "id": 11,
        "title": "Criba de Eratóstenes",
        "description": "Implementa la Criba de Eratóstenes para encontrar todos los primos hasta n.",
        "difficulty": "hard",
        "category": "matemáticas",
        "points": 30,
        "example_input": "30",
        "example_output": "[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]",
        "hints": ["Crea un array booleano de tamaño n", "Marca múltiplos como no primos"]
    },
    {
        "id": 12,
        "title": "Descomposición en Factores Primos",
        "description": "Encuentra la descomposición en factores primos de un número.",
        "difficulty": "hard",
        "category": "matemáticas",
        "points": 30,
        "example_input": "84",
        "example_output": "[2, 2, 3, 7]",
        "hints": ["Divide por números comenzando desde 2", "Continúa hasta que el número sea 1"]
    },
    {
        "id": 13,
        "title": "Coeficientes Binomiales",
        "description": "Calcula el coeficiente binomial C(n, k) usando programación dinámica.",
        "difficulty": "hard",
        "category": "matemáticas",
        "points": 30,
        "example_input": "5, 2",
        "example_output": "10",
        "hints": ["Usa el triángulo de Pascal", "C(n,k) = C(n-1,k-1) + C(n-1,k)"]
    },
    {
        "id": 14,
        "title": "Raíz Cuadrada Entera",
        "description": "Implementa raíz cuadrada entera usando búsqueda binaria sin usar sqrt().",
        "difficulty": "hard",
        "category": "matemáticas",
        "points": 30,
        "example_input": "16",
        "example_output": "4",
        "hints": ["Usa búsqueda binaria entre 0 y n", "Encuentra el mayor entero cuyo cuadrado sea <= n"]
    },
    {
        "id": 15,
        "title": "Módulo de Potencia",
        "description": "Calcula (base^exponente) % mod eficientemente.",
        "difficulty": "hard",
        "category": "matemáticas",
        "points": 30,
        "example_input": "2, 10, 1000",
        "example_output": "24",
        "hints": ["Usa exponenciación modular", "Evita el desbordamiento usando módulo en cada paso"]
    },
    
    # CADENAS - Fácil
    {
        "id": 16,
        "title": "Invertir una Cadena",
        "description": "Invierte una cadena dada.",
        "difficulty": "easy",
        "category": "cadenas",
        "points": 10,
        "example_input": "'hola'",
        "example_output": "'aloh'",
        "hints": ["Usa slicing [::-1]", "O recorre la cadena en reversa"]
    },
    {
        "id": 17,
        "title": "Contador de Vocales",
        "description": "Cuenta el número de vocales en una cadena.",
        "difficulty": "easy",
        "category": "cadenas",
        "points": 10,
        "example_input": "'hola mundo'",
        "example_output": "4",
        "hints": ["Define un conjunto de vocales", "Itera y cuenta coincidencias"]
    },
    {
        "id": 18,
        "title": "Verificador de Palíndromos",
        "description": "Verifica si una cadena es un palíndromo.",
        "difficulty": "easy",
        "category": "cadenas",
        "points": 10,
        "example_input": "'radar'",
        "example_output": "True",
        "hints": ["Compara la cadena con su reverso", "Ignora mayúsculas/minúsculas"]
    },
    {
        "id": 19,
        "title": "Capitalizar Primera Letra",
        "description": "Capitaliza la primera letra de cada palabra.",
        "difficulty": "easy",
        "category": "cadenas",
        "points": 10,
        "example_input": "'hola mundo'",
        "example_output": "'Hola Mundo'",
        "hints": ["Usa el método title()", "O split, capitaliza y join"]
    },
    {
        "id": 20,
        "title": "Contar Palabras",
        "description": "Cuenta el número de palabras en una cadena.",
        "difficulty": "easy",
        "category": "cadenas",
        "points": 10,
        "example_input": "'Hola mundo desde Python'",
        "example_output": "4",
        "hints": ["Usa el método split()", "Cuenta los elementos de la lista"]
    },
    
    # CADENAS - Medio
    {
        "id": 21,
        "title": "Anagramas",
        "description": "Verifica si dos cadenas son anagramas.",
        "difficulty": "medium",
        "category": "cadenas",
        "points": 20,
        "example_input": "'listen', 'silent'",
        "example_output": "True",
        "hints": ["Ordena ambas cadenas y compara", "O usa un contador de caracteres"]
    },
    {
        "id": 22,
        "title": "Subcadena Más Larga Sin Repetir",
        "description": "Encuentra la longitud de la subcadena más larga sin caracteres repetidos.",
        "difficulty": "medium",
        "category": "cadenas",
        "points": 20,
        "example_input": "'abcabcbb'",
        "example_output": "3",
        "hints": ["Usa ventana deslizante", "Mantén un conjunto de caracteres vistos"]
    },
    {
        "id": 23,
        "title": "Compresión de Cadenas",
        "description": "Comprime una cadena usando conteos de caracteres repetidos.",
        "difficulty": "medium",
        "category": "cadenas",
        "points": 20,
        "example_input": "'aabcccccaaa'",
        "example_output": "'a2b1c5a3'",
        "hints": ["Cuenta caracteres consecutivos", "Construye cadena resultado"]
    },
    {
        "id": 24,
        "title": "Subcadena Palindrómica Más Larga",
        "description": "Encuentra la subcadena palindrómica más larga en una cadena.",
        "difficulty": "medium",
        "category": "cadenas",
        "points": 20,
        "example_input": "'babad'",
        "example_output": "'bab' o 'aba'",
        "hints": ["Expande alrededor del centro", "Considera palíndromos pares e impares"]
    },
    {
        "id": 25,
        "title": "Rotación de Cadenas",
        "description": "Verifica si una cadena es una rotación de otra.",
        "difficulty": "medium",
        "category": "cadenas",
        "points": 20,
        "example_input": "'waterbottle', 'erbottlewat'",
        "example_output": "True",
        "hints": ["Concatena s1 consigo misma", "Verifica si s2 es subcadena"]
    },
    
    # CADENAS - Difícil
    {
        "id": 26,
        "title": "Coincidencia de Patrón Comodín",
        "description": "Implementa coincidencia de patrones con '?' y '*'.",
        "difficulty": "hard",
        "category": "cadenas",
        "points": 30,
        "example_input": "'aa', 'a*'",
        "example_output": "True",
        "hints": ["Usa programación dinámica", "'?' coincide con un carácter, '*' con cualquier secuencia"]
    },
    {
        "id": 27,
        "title": "Editar Distancia",
        "description": "Calcula la distancia de Levenshtein entre dos cadenas.",
        "difficulty": "hard",
        "category": "cadenas",
        "points": 30,
        "example_input": "'kitten', 'sitting'",
        "example_output": "3",
        "hints": ["Usa programación dinámica", "Considera insertar, eliminar, reemplazar"]
    },
    {
        "id": 28,
        "title": "Decodificador de Cadenas",
        "description": "Decodifica una cadena codificada como '3[a]2[bc]'.",
        "difficulty": "hard",
        "category": "cadenas",
        "points": 30,
        "example_input": "'3[a]2[bc]'",
        "example_output": "'aaabcbc'",
        "hints": ["Usa una pila", "Procesa números y corchetes"]
    },
    {
        "id": 29,
        "title": "Paréntesis Válidos",
        "description": "Genera todas las combinaciones de n pares de paréntesis válidos.",
        "difficulty": "hard",
        "category": "cadenas",
        "points": 30,
        "example_input": "3",
        "example_output": "['((()))', '(()())', '(())()', '()(())', '()()()']",
        "hints": ["Usa backtracking", "Rastrea paréntesis abiertos y cerrados"]
    },
    {
        "id": 30,
        "title": "Búsqueda de Subcadena KMP",
        "description": "Implementa el algoritmo Knuth-Morris-Pratt para búsqueda de patrones.",
        "difficulty": "hard",
        "category": "cadenas",
        "points": 30,
        "example_input": "'ababcababa', 'ababa'",
        "example_output": "5",
        "hints": ["Construye array LPS", "Usa prefijos propios más largos"]
    },
    
    # ALGORITMOS - Fácil
    {
        "id": 31,
        "title": "Búsqueda Lineal",
        "description": "Implementa búsqueda lineal para encontrar un elemento en una lista.",
        "difficulty": "easy",
        "category": "algoritmos",
        "points": 10,
        "example_input": "[1, 2, 3, 4, 5], 3",
        "example_output": "2 (índice)",
        "hints": ["Itera por la lista", "Devuelve índice cuando se encuentre"]
    },
    {
        "id": 32,
        "title": "Ordenamiento Burbuja",
        "description": "Implementa el algoritmo de ordenamiento burbuja.",
        "difficulty": "easy",
        "category": "algoritmos",
        "points": 10,
        "example_input": "[64, 34, 25, 12, 22]",
        "example_output": "[12, 22, 25, 34, 64]",
        "hints": ["Compara elementos adyacentes", "Intercambia si están en orden incorrecto"]
    },
    {
        "id": 33,
        "title": "Encontrar Mínimo",
        "description": "Encuentra el elemento mínimo en una lista no ordenada.",
        "difficulty": "easy",
        "category": "algoritmos",
        "points": 10,
        "example_input": "[3, 1, 4, 1, 5, 9]",
        "example_output": "1",
        "hints": ["Itera y rastrea el mínimo", "O usa la función min() incorporada"]
    },
    {
        "id": 34,
        "title": "Inversión de Lista",
        "description": "Invierte una lista en su lugar.",
        "difficulty": "easy",
        "category": "algoritmos",
        "points": 10,
        "example_input": "[1, 2, 3, 4, 5]",
        "example_output": "[5, 4, 3, 2, 1]",
        "hints": ["Usa dos punteros", "Intercambia elementos desde los extremos"]
    },
    {
        "id": 35,
        "title": "Duplicados en Lista",
        "description": "Encuentra duplicados en una lista.",
        "difficulty": "easy",
        "category": "algoritmos",
        "points": 10,
        "example_input": "[1, 2, 3, 2, 4, 3]",
        "example_output": "[2, 3]",
        "hints": ["Usa un conjunto para rastrear vistos", "Agrega a resultado si ya se vio"]
    },
    
    # ALGORITMOS - Medio
    {
        "id": 36,
        "title": "Búsqueda Binaria",
        "description": "Implementa búsqueda binaria en una lista ordenada.",
        "difficulty": "medium",
        "category": "algoritmos",
        "points": 20,
        "example_input": "[1, 2, 3, 4, 5, 6, 7], 4",
        "example_output": "3 (índice)",
        "hints": ["Divide y conquista", "Compara con el elemento medio"]
    },
    {
        "id": 37,
        "title": "Merge Sort",
        "description": "Implementa el algoritmo merge sort.",
        "difficulty": "medium",
        "category": "algoritmos",
        "points": 20,
        "example_input": "[38, 27, 43, 3, 9, 82, 10]",
        "example_output": "[3, 9, 10, 27, 38, 43, 82]",
        "hints": ["Divide la lista por la mitad", "Mezcla listas ordenadas"]
    },
    {
        "id": 38,
        "title": "Quick Sort",
        "description": "Implementa el algoritmo quick sort.",
        "difficulty": "medium",
        "category": "algoritmos",
        "points": 20,
        "example_input": "[10, 7, 8, 9, 1, 5]",
        "example_output": "[1, 5, 7, 8, 9, 10]",
        "hints": ["Elige un pivote", "Particiona alrededor del pivote"]
    },
    {
        "id": 39,
        "title": "Problema de las Dos Sumas",
        "description": "Encuentra dos números que sumen un objetivo.",
        "difficulty": "medium",
        "category": "algoritmos",
        "points": 20,
        "example_input": "[2, 7, 11, 15], objetivo=9",
        "example_output": "[0, 1]",
        "hints": ["Usa un diccionario para rastrear valores vistos", "Busca complemento"]
    },
    {
        "id": 40,
        "title": "Subarray de Suma Máxima",
        "description": "Encuentra el subarray contiguo con la suma más grande (algoritmo de Kadane).",
        "difficulty": "medium",
        "category": "algoritmos",
        "points": 20,
        "example_input": "[-2, 1, -3, 4, -1, 2, 1, -5, 4]",
        "example_output": "6",
        "hints": ["Algoritmo de Kadane", "Rastrea suma máxima hasta ahora y suma actual"]
    },
    
    # ALGORITMOS - Difícil
    {
        "id": 41,
        "title": "Problema de la Mochila 0/1",
        "description": "Resuelve el problema de la mochila usando programación dinámica.",
        "difficulty": "hard",
        "category": "algoritmos",
        "points": 30,
        "example_input": "pesos=[1,2,3], valores=[6,10,12], capacidad=5",
        "example_output": "22",
        "hints": ["Usa tabla 2D DP", "Considera incluir/excluir cada artículo"]
    },
    {
        "id": 42,
        "title": "Subsecuencia Común Más Larga",
        "description": "Encuentra la LCS de dos secuencias.",
        "difficulty": "hard",
        "category": "algoritmos",
        "points": 30,
        "example_input": "'AGGTAB', 'GXTXAYB'",
        "example_output": "4 (GTAB)",
        "hints": ["Usa programación dinámica", "Construye tabla de subsecuencias"]
    },
    {
        "id": 43,
        "title": "Problema del Viajante (TSP)",
        "description": "Encuentra el camino más corto visitando todas las ciudades.",
        "difficulty": "hard",
        "category": "algoritmos",
        "points": 30,
        "example_input": "matriz de distancias 4x4",
        "example_output": "Distancia mínima del recorrido",
        "hints": ["Usa programación dinámica con máscaras de bits", "O backtracking para casos pequeños"]
    },
    {
        "id": 44,
        "title": "N-Reinas",
        "description": "Coloca N reinas en un tablero NxN sin ataques.",
        "difficulty": "hard",
        "category": "algoritmos",
        "points": 30,
        "example_input": "4",
        "example_output": "2 soluciones posibles",
        "hints": ["Usa backtracking", "Verifica diagonal y fila/columna"]
    },
    {
        "id": 45,
        "title": "Camino Más Corto de Dijkstra",
        "description": "Implementa el algoritmo de Dijkstra para caminos más cortos.",
        "difficulty": "hard",
        "category": "algoritmos",
        "points": 30,
        "example_input": "grafo con pesos, nodo inicial",
        "example_output": "distancias más cortas a todos los nodos",
        "hints": ["Usa cola de prioridad", "Actualiza distancias greedily"]
    },
    
    # COMPRENSIÓN DE LISTAS - Fácil
    {
        "id": 46,
        "title": "Cuadrados de Números",
        "description": "Crea una lista de cuadrados de números del 1 al n.",
        "difficulty": "easy",
        "category": "comprension de listas",
        "points": 10,
        "example_input": "5",
        "example_output": "[1, 4, 9, 16, 25]",
        "hints": ["Usa comprensión de listas", "[x**2 for x in range()]"]
    },
    {
        "id": 47,
        "title": "Filtrar Pares",
        "description": "Filtra solo números pares de una lista.",
        "difficulty": "easy",
        "category": "comprension de listas",
        "points": 10,
        "example_input": "[1, 2, 3, 4, 5, 6]",
        "example_output": "[2, 4, 6]",
        "hints": ["Usa comprensión con condición", "[x for x in lista if x % 2 == 0]"]
    },
    {
        "id": 48,
        "title": "Mayúsculas a Lista",
        "description": "Convierte todos los strings en una lista a mayúsculas.",
        "difficulty": "easy",
        "category": "comprension de listas",
        "points": 10,
        "example_input": "['hola', 'mundo']",
        "example_output": "['HOLA', 'MUNDO']",
        "hints": ["Usa comprensión de listas", "[s.upper() for s in lista]"]
    },
    {
        "id": 49,
        "title": "Aplanar Lista Anidada",
        "description": "Aplana una lista de listas en una sola lista.",
        "difficulty": "easy",
        "category": "comprension de listas",
        "points": 10,
        "example_input": "[[1, 2], [3, 4], [5]]",
        "example_output": "[1, 2, 3, 4, 5]",
        "hints": ["Usa comprensión anidada", "[item for sublist in lista for item in sublist]"]
    },
    {
        "id": 50,
        "title": "Longitud de Palabras",
        "description": "Crea una lista de longitudes de palabras.",
        "difficulty": "easy",
        "category": "comprension de listas",
        "points": 10,
        "example_input": "['hola', 'mundo', 'python']",
        "example_output": "[4, 5, 6]",
        "hints": ["Aplica len() a cada palabra", "[len(w) for w in palabras]"]
    },
    
    # COMPRENSIÓN DE LISTAS - Medio
    {
        "id": 51,
        "title": "Producto Cartesiano",
        "description": "Genera producto cartesiano de dos listas.",
        "difficulty": "medium",
        "category": "comprension de listas",
        "points": 20,
        "example_input": "[1, 2], ['a', 'b']",
        "example_output": "[(1,'a'), (1,'b'), (2,'a'), (2,'b')]",
        "hints": ["Usa comprensión anidada", "[(x,y) for x in lista1 for y in lista2]"]
    },
    {
        "id": 52,
        "title": "Transponer Matriz",
        "description": "Transpone una matriz usando comprensión de listas.",
        "difficulty": "medium",
        "category": "comprension de listas",
        "points": 20,
        "example_input": "[[1,2,3], [4,5,6]]",
        "example_output": "[[1,4], [2,5], [3,6]]",
        "hints": ["Usa zip con comprensión", "[list(x) for x in zip(*matriz)]"]
    },
    {
        "id": 53,
        "title": "Comprensión Condicional Compleja",
        "description": "Aplica diferentes transformaciones basadas en condiciones.",
        "difficulty": "medium",
        "category": "comprension de listas",
        "points": 20,
        "example_input": "[1, 2, 3, 4, 5]",
        "example_output": "[1, 4, 3, 16, 5] (cuadrado si es par)",
        "hints": ["Usa expresión ternaria en comprensión", "[x**2 if x%2==0 else x for x in lista]"]
    },
    {
        "id": 54,
        "title": "Generador de Diccionarios",
        "description": "Crea diccionario desde dos listas usando comprensión.",
        "difficulty": "medium",
        "category": "comprension de listas",
        "points": 20,
        "example_input": "claves=['a','b'], valores=[1,2]",
        "example_output": "{'a': 1, 'b': 2}",
        "hints": ["Usa comprensión de diccionarios", "{k:v for k,v in zip(claves, valores)}"]
    },
    {
        "id": 55,
        "title": "Filtrar y Transformar",
        "description": "Filtra números pares y devuelve sus raíces cuadradas.",
        "difficulty": "medium",
        "category": "comprension de listas",
        "points": 20,
        "example_input": "[1, 4, 9, 16, 25]",
        "example_output": "[2.0, 4.0]",
        "hints": ["Combina filtro y map", "[x**0.5 for x in lista if x%2==0]"]
    },
    
    # COMPRENSIÓN DE LISTAS - Difícil
    {
        "id": 56,
        "title": "Comprensión Anidada Multinivel",
        "description": "Aplana una estructura profundamente anidada.",
        "difficulty": "hard",
        "category": "comprension de listas",
        "points": 30,
        "example_input": "[[[1,2]], [[3,4]], [[5]]]",
        "example_output": "[1, 2, 3, 4, 5]",
        "hints": ["Usa múltiples niveles de comprensión", "Itera recursivamente"]
    },
    {
        "id": 57,
        "title": "Comprensión con Walrus",
        "description": "Usa el operador walrus (:=) en comprensión de listas.",
        "difficulty": "hard",
        "category": "comprension de listas",
        "points": 30,
        "example_input": "[1, 2, 3, 4, 5]",
        "example_output": "[(1,1), (2,4), (3,9), (4,16), (5,25)]",
        "hints": ["Usa := para asignar y usar", "[(x, y:=x**2) for x in lista]"]
    },
    {
        "id": 58,
        "title": "Set Comprehension con Lógica Compleja",
        "description": "Crea un conjunto con comprensión y lógica compleja.",
        "difficulty": "hard",
        "category": "comprension de listas",
        "points": 30,
        "example_input": "range(1, 20)",
        "example_output": "{números que son primos y divisibles por suma de dígitos}",
        "hints": ["Usa set comprehension", "Combina múltiples condiciones"]
    },
    {
        "id": 59,
        "title": "Comprensión de Generadores Encadenados",
        "description": "Encadena múltiples expresiones generadoras.",
        "difficulty": "hard",
        "category": "comprension de listas",
        "points": 30,
        "example_input": "[[1,2,3], [4,5], [6,7,8,9]]",
        "example_output": "Suma de todos los cuadrados de números pares",
        "hints": ["Usa expresiones generadoras anidadas", "sum(x**2 for sub in lista for x in sub if x%2==0)"]
    },
    {
        "id": 60,
        "title": "Matriz Generada Dinámicamente",
        "description": "Genera matriz basada en función de posición.",
        "difficulty": "hard",
        "category": "comprension de listas",
        "points": 30,
        "example_input": "n=3 (matriz 3x3)",
        "example_output": "[[0,1,2], [1,2,3], [2,3,4]] (i+j)",
        "hints": ["Usa comprensión 2D", "[[i+j for j in range(n)] for i in range(n)]"]
    },
    
    # LAMBDAS - Fácil
    {
        "id": 61,
        "title": "Lambda Simple",
        "description": "Crea una función lambda que duplique un número.",
        "difficulty": "easy",
        "category": "lambdas",
        "points": 10,
        "example_input": "5",
        "example_output": "10",
        "hints": ["lambda x: x * 2", "Las lambdas son funciones anónimas"]
    },
    {
        "id": 62,
        "title": "Lambda con Map",
        "description": "Usa lambda con map para elevar al cuadrado una lista.",
        "difficulty": "easy",
        "category": "lambdas",
        "points": 10,
        "example_input": "[1, 2, 3, 4]",
        "example_output": "[1, 4, 9, 16]",
        "hints": ["map(lambda x: x**2, lista)", "Convierte el resultado a lista"]
    },
    {
        "id": 63,
        "title": "Lambda con Filter",
        "description": "Usa lambda con filter para obtener números mayores que 5.",
        "difficulty": "easy",
        "category": "lambdas",
        "points": 10,
        "example_input": "[1, 6, 3, 8, 2, 9]",
        "example_output": "[6, 8, 9]",
        "hints": ["filter(lambda x: x > 5, lista)", "Filter devuelve un iterador"]
    },
    {
        "id": 64,
        "title": "Lambda de Ordenamiento",
        "description": "Ordena una lista de tuplas por el segundo elemento.",
        "difficulty": "easy",
        "category": "lambdas",
        "points": 10,
        "example_input": "[(1, 3), (3, 1), (2, 2)]",
        "example_output": "[(3, 1), (2, 2), (1, 3)]",
        "hints": ["sorted(lista, key=lambda x: x[1])", "El parámetro key especifica la función de ordenamiento"]
    },
    {
        "id": 65,
        "title": "Lambda Condicional",
        "description": "Crea lambda que devuelva 'par' o 'impar'.",
        "difficulty": "easy",
        "category": "lambdas",
        "points": 10,
        "example_input": "4",
        "example_output": "'par'",
        "hints": ["lambda x: 'par' if x%2==0 else 'impar'", "Usa expresión ternaria"]
    },
    
    # LAMBDAS - Medio
    {
        "id": 66,
        "title": "Lambda con Reduce",
        "description": "Usa lambda con reduce para multiplicar todos los elementos.",
        "difficulty": "medium",
        "category": "lambdas",
        "points": 20,
        "example_input": "[1, 2, 3, 4]",
        "example_output": "24",
        "hints": ["from functools import reduce", "reduce(lambda x, y: x*y, lista)"]
    },
    {
        "id": 67,
        "title": "Lambda Anidada",
        "description": "Crea lambda que devuelva otra lambda.",
        "difficulty": "medium",
        "category": "lambdas",
        "points": 20,
        "example_input": "2 (multiplicador)",
        "example_output": "función que multiplica por 2",
        "hints": ["lambda x: lambda y: x * y", "Closure con lambdas"]
    },
    {
        "id": 68,
        "title": "Lambda Multi-argumento",
        "description": "Ordena diccionarios por múltiples claves usando lambdas.",
        "difficulty": "medium",
        "category": "lambdas",
        "points": 20,
        "example_input": "[{'nombre': 'Juan', 'edad': 25}, {'nombre': 'Ana', 'edad': 25}]",
        "example_output": "Ordenado por edad, luego nombre",
        "hints": ["key=lambda x: (x['edad'], x['nombre'])", "Las tuplas se ordenan elemento por elemento"]
    },
    {
        "id": 69,
        "title": "Lambda con Zip",
        "description": "Combina dos listas usando lambda y zip.",
        "difficulty": "medium",
        "category": "lambdas",
        "points": 20,
        "example_input": "[1, 2, 3], [4, 5, 6]",
        "example_output": "[5, 7, 9]",
        "hints": ["map(lambda x, y: x+y, lista1, lista2)", "Zip empareja elementos"]
    },
    {
        "id": 70,
        "title": "Lambda para Agrupar",
        "description": "Agrupa elementos usando lambda como función clave.",
        "difficulty": "medium",
        "category": "lambdas",
        "points": 20,
        "example_input": "['uno', 'dos', 'tres', 'cuatro']",
        "example_output": "Agrupado por longitud",
        "hints": ["from itertools import groupby", "groupby(lista, key=lambda x: len(x))"]
    },
    
    # LAMBDAS - Difícil
    {
        "id": 71,
        "title": "Lambda Recursiva con Y-Combinator",
        "description": "Implementa recursión en lambda usando Y-combinator.",
        "difficulty": "hard",
        "category": "lambdas",
        "points": 30,
        "example_input": "5 (factorial)",
        "example_output": "120",
        "hints": ["Y = lambda f: (lambda x: f(lambda y: x(x)(y)))(lambda x: f(lambda y: x(x)(y)))", "Permite recursión sin nombre"]
    },
    {
        "id": 72,
        "title": "Lambda Chain Complex",
        "description": "Encadena múltiples lambdas para pipeline de transformación.",
        "difficulty": "hard",
        "category": "lambdas",
        "points": 30,
        "example_input": "[1, 2, 3, 4, 5]",
        "example_output": "Pipeline: filtrar pares -> cuadrado -> suma",
        "hints": ["Compone funciones lambda", "reduce para aplicar secuencialmente"]
    },
    {
        "id": 73,
        "title": "Lambda Currying",
        "description": "Implementa currying completo con lambdas.",
        "difficulty": "hard",
        "category": "lambdas",
        "points": 30,
        "example_input": "función de 3 argumentos",
        "example_output": "función curried que toma argumentos uno a uno",
        "hints": ["lambda a: lambda b: lambda c: a + b + c", "Cada lambda devuelve otra lambda"]
    },
    {
        "id": 74,
        "title": "Lambda Memoization",
        "description": "Implementa memoización usando lambdas y diccionarios.",
        "difficulty": "hard",
        "category": "lambdas",
        "points": 30,
        "example_input": "fibonacci(10)",
        "example_output": "Resultado cacheado",
        "hints": ["Usa diccionario para cache", "Lambda con estado mutable"]
    },
    {
        "id": 75,
        "title": "Lambda Decorator Pattern",
        "description": "Implementa patrón decorador usando solo lambdas.",
        "difficulty": "hard",
        "category": "lambdas",
        "points": 30,
        "example_input": "función a decorar",
        "example_output": "función decorada con logging",
        "hints": ["lambda f: lambda *args: (print('llamada'), f(*args))", "Envuelve funciones"]
    },
    
    # EXPRESIONES REGULARES - Fácil
    {
        "id": 76,
        "title": "Validar Email Simple",
        "description": "Valida un email básico con regex.",
        "difficulty": "easy",
        "category": "expresiones regulares",
        "points": 10,
        "example_input": "'usuario@ejemplo.com'",
        "example_output": "True",
        "hints": ["import re", "Patrón: r'^\\w+@\\w+\\.\\w+$'"]
    },
    {
        "id": 77,
        "title": "Encontrar Dígitos",
        "description": "Encuentra todos los dígitos en una cadena.",
        "difficulty": "easy",
        "category": "expresiones regulares",
        "points": 10,
        "example_input": "'abc123def456'",
        "example_output": "['123', '456']",
        "hints": ["re.findall(r'\\d+', texto)", "\\d coincide con dígitos"]
    },
    {
        "id": 78,
        "title": "Reemplazar Espacios",
        "description": "Reemplaza múltiples espacios con uno solo.",
        "difficulty": "easy",
        "category": "expresiones regulares",
        "points": 10,
        "example_input": "'hola    mundo'",
        "example_output": "'hola mundo'",
        "hints": ["re.sub(r'\\s+', ' ', texto)", "\\s+ coincide con uno o más espacios"]
    },
    {
        "id": 79,
        "title": "Validar Teléfono",
        "description": "Valida formato de número telefónico.",
        "difficulty": "easy",
        "category": "expresiones regulares",
        "points": 10,
        "example_input": "'123-456-7890'",
        "example_output": "True",
        "hints": ["Patrón: r'^\\d{3}-\\d{3}-\\d{4}$'", "\\d{n} coincide exactamente n dígitos"]
    },
    {
        "id": 80,
        "title": "Extraer Palabras",
        "description": "Extrae todas las palabras de un texto.",
        "difficulty": "easy",
        "category": "expresiones regulares",
        "points": 10,
        "example_input": "'Hola, mundo! ¿Cómo estás?'",
        "example_output": "['Hola', 'mundo', 'Cómo', 'estás']",
        "hints": ["re.findall(r'\\w+', texto)", "\\w coincide con caracteres de palabra"]
    },
    
    # EXPRESIONES REGULARES - Medio
    {
        "id": 81,
        "title": "Validar Contraseña",
        "description": "Valida contraseña con requisitos: 8+ caracteres, mayúscula, minúscula, número.",
        "difficulty": "medium",
        "category": "expresiones regulares",
        "points": 20,
        "example_input": "'Pass1234'",
        "example_output": "True",
        "hints": ["Usa lookahead: (?=.*[A-Z])", "Combina múltiples condiciones"]
    },
    {
        "id": 82,
        "title": "Extraer URLs",
        "description": "Extrae todas las URLs de un texto.",
        "difficulty": "medium",
        "category": "expresiones regulares",
        "points": 20,
        "example_input": "'Visita https://ejemplo.com y http://test.org'",
        "example_output": "['https://ejemplo.com', 'http://test.org']",
        "hints": ["Patrón: r'https?://[^\\s]+'", "? hace opcional la 's'"]
    },
    {
        "id": 83,
        "title": "Validar Fecha",
        "description": "Valida formato de fecha DD/MM/YYYY.",
        "difficulty": "medium",
        "category": "expresiones regulares",
        "points": 20,
        "example_input": "'25/12/2023'",
        "example_output": "True",
        "hints": ["Patrón: r'^\\d{2}/\\d{2}/\\d{4}$'", "Considera rangos válidos"]
    },
    {
        "id": 84,
        "title": "Grupos de Captura",
        "description": "Extrae nombre y dominio de emails usando grupos.",
        "difficulty": "medium",
        "category": "expresiones regulares",
        "points": 20,
        "example_input": "'usuario@ejemplo.com'",
        "example_output": "('usuario', 'ejemplo.com')",
        "hints": ["r'(\\w+)@([\\w.]+)'", "Usa () para grupos de captura"]
    },
    {
        "id": 85,
        "title": "Reemplazar con Función",
        "description": "Usa re.sub con función para transformación compleja.",
        "difficulty": "medium",
        "category": "expresiones regulares",
        "points": 20,
        "example_input": "'precio: 10 euros'",
        "example_output": "'precio: 20 euros' (duplicar números)",
        "hints": ["re.sub(r'\\d+', lambda m: str(int(m.group())*2), texto)", "Lambda recibe objeto Match"]
    },
    
    # EXPRESIONES REGULARES - Difícil
    {
        "id": 86,
        "title": "Validar HTML Tags",
        "description": "Valida que las etiquetas HTML estén balanceadas.",
        "difficulty": "hard",
        "category": "expresiones regulares",
        "points": 30,
        "example_input": "'<div><p>texto</p></div>'",
        "example_output": "True",
        "hints": ["Usa backreferences", "Patrón recursivo complejo"]
    },
    {
        "id": 87,
        "title": "Parser de Expresiones Matemáticas",
        "description": "Parsea y valida expresiones matemáticas.",
        "difficulty": "hard",
        "category": "expresiones regulares",
        "points": 30,
        "example_input": "'(2 + 3) * 4'",
        "example_output": "{'válido': True, 'tokens': [...]}}",
        "hints": ["Tokeniza números, operadores, paréntesis", "Usa grupos nombrados"]
    },
    {
        "id": 88,
        "title": "Lookahead y Lookbehind",
        "description": "Usa assertions para extraer patrones contextuales.",
        "difficulty": "hard",
        "category": "expresiones regulares",
        "points": 30,
        "example_input": "'precio123dolares'",
        "example_output": "Extrae número solo si precede 'dolares'",
        "hints": ["(?<=precio)\\d+(?=dolares)", "Lookbehind (?<=...) y lookahead (?=...)"]
    },
    {
        "id": 89,
        "title": "Validar IPv4",
        "description": "Valida dirección IPv4 completa con rangos correctos.",
        "difficulty": "hard",
        "category": "expresiones regulares",
        "points": 30,
        "example_input": "'192.168.1.1'",
        "example_output": "True",
        "hints": ["Cada octeto: 0-255", "Patrón complejo con alternación"]
    },
    {
        "id": 90,
        "title": "Extractor de Comentarios de Código",
        "description": "Extrae comentarios de código Python/JavaScript.",
        "difficulty": "hard",
        "category": "expresiones regulares",
        "points": 30,
        "example_input": "código con // y /* */ y #",
        "example_output": "Lista de todos los comentarios",
        "hints": ["Maneja múltiples estilos", "Usa flags re.MULTILINE y re.DOTALL"]
    },
    
    # MANEJO DE FICHEROS - Fácil
    {
        "id": 91,
        "title": "Leer Archivo de Texto",
        "description": "Lee el contenido completo de un archivo de texto.",
        "difficulty": "easy",
        "category": "manejo de ficheros",
        "points": 10,
        "example_input": "'archivo.txt'",
        "example_output": "contenido del archivo",
        "hints": ["with open('archivo.txt', 'r') as f:", "usa f.read()"]
    },
    {
        "id": 92,
        "title": "Escribir en Archivo",
        "description": "Escribe texto en un archivo.",
        "difficulty": "easy",
        "category": "manejo de ficheros",
        "points": 10,
        "example_input": "'Hola mundo'",
        "example_output": "archivo creado con texto",
        "hints": ["modo 'w' para escribir", "with open garantiza cierre"]
    },
    {
        "id": 93,
        "title": "Contar Líneas",
        "description": "Cuenta el número de líneas en un archivo.",
        "difficulty": "easy",
        "category": "manejo de ficheros",
        "points": 10,
        "example_input": "'archivo.txt'",
        "example_output": "15",
        "hints": ["Itera sobre f.readlines()", "O usa sum(1 for line in f)"]
    },
    {
        "id": 94,
        "title": "Verificar Existencia",
        "description": "Verifica si un archivo existe.",
        "difficulty": "easy",
        "category": "manejo de ficheros",
        "points": 10,
        "example_input": "'archivo.txt'",
        "example_output": "True/False",
        "hints": ["import os.path", "os.path.exists('archivo.txt')"]
    },
    {
        "id": 95,
        "title": "Añadir a Archivo",
        "description": "Añade texto al final de un archivo existente.",
        "difficulty": "easy",
        "category": "manejo de ficheros",
        "points": 10,
        "example_input": "'nueva línea'",
        "example_output": "texto añadido",
        "hints": ["modo 'a' para append", "No sobrescribe contenido existente"]
    },
    
    # MANEJO DE FICHEROS - Medio
    {
        "id": 96,
        "title": "Procesar CSV",
        "description": "Lee y procesa archivo CSV.",
        "difficulty": "medium",
        "category": "manejo de ficheros",
        "points": 20,
        "example_input": "'datos.csv'",
        "example_output": "lista de diccionarios",
        "hints": ["import csv", "csv.DictReader para leer con encabezados"]
    },
    {
        "id": 97,
        "title": "Copiar Archivo",
        "description": "Copia un archivo a otra ubicación.",
        "difficulty": "medium",
        "category": "manejo de ficheros",
        "points": 20,
        "example_input": "'origen.txt', 'destino.txt'",
        "example_output": "archivo copiado",
        "hints": ["import shutil", "shutil.copy2() preserva metadata"]
    },
    {
        "id": 98,
        "title": "Buscar en Archivos",
        "description": "Busca una palabra en todos los archivos de un directorio.",
        "difficulty": "medium",
        "category": "manejo de ficheros",
        "points": 20,
        "example_input": "directorio, 'palabra'",
        "example_output": "lista de archivos que contienen la palabra",
        "hints": ["os.walk() para recorrer directorio", "Lee cada archivo y busca"]
    },
    {
        "id": 99,
        "title": "Leer JSON",
        "description": "Lee y parsea archivo JSON.",
        "difficulty": "medium",
        "category": "manejo de ficheros",
        "points": 20,
        "example_input": "'datos.json'",
        "example_output": "diccionario/lista Python",
        "hints": ["import json", "json.load(f) para leer desde archivo"]
    },
    {
        "id": 100,
        "title": "Escribir JSON",
        "description": "Escribe estructura Python a archivo JSON.",
        "difficulty": "medium",
        "category": "manejo de ficheros",
        "points": 20,
        "example_input": "{'nombre': 'Juan', 'edad': 30}",
        "example_output": "archivo JSON creado",
        "hints": ["json.dump(data, f, indent=4)", "indent para formato legible"]
    },
    
    # MANEJO DE FICHEROS - Difícil
    {
        "id": 101,
        "title": "Monitor de Cambios",
        "description": "Monitorea cambios en un archivo en tiempo real.",
        "difficulty": "hard",
        "category": "manejo de ficheros",
        "points": 30,
        "example_input": "'archivo.log'",
        "example_output": "notifica cuando cambia",
        "hints": ["Compara timestamp o tamaño", "Usa bucle con time.sleep()"]
    },
    {
        "id": 102,
        "title": "Procesador de Logs",
        "description": "Procesa archivos de log grandes eficientemente.",
        "difficulty": "hard",
        "category": "manejo de ficheros",
        "points": 30,
        "example_input": "'app.log' (100MB)",
        "example_output": "estadísticas de errores",
        "hints": ["Lee línea por línea, no todo el archivo", "Usa generadores para eficiencia"]
    },
    {
        "id": 103,
        "title": "Merge de Archivos Ordenados",
        "description": "Mezcla múltiples archivos ordenados en uno solo ordenado.",
        "difficulty": "hard",
        "category": "manejo de ficheros",
        "points": 30,
        "example_input": "['file1.txt', 'file2.txt', 'file3.txt']",
        "example_output": "'merged.txt' ordenado",
        "hints": ["heapq.merge() para merge eficiente", "Lee archivos como generadores"]
    },
    {
        "id": 104,
        "title": "Archivo Binario Custom",
        "description": "Lee/escribe formato binario personalizado.",
        "difficulty": "hard",
        "category": "manejo de ficheros",
        "points": 30,
        "example_input": "estructura de datos compleja",
        "example_output": "archivo binario",
        "hints": ["import struct", "struct.pack/unpack para binario"]
    },
    {
        "id": 105,
        "title": "Sistema de Cache de Archivos",
        "description": "Implementa sistema de cache para lecturas frecuentes.",
        "difficulty": "hard",
        "category": "manejo de ficheros",
        "points": 30,
        "example_input": "archivos accedidos frecuentemente",
        "example_output": "cache LRU de contenidos",
        "hints": ["functools.lru_cache", "Considera timestamp de modificación"]
    },
    
    # MANEJO DE PAQUETES - Fácil
    {
        "id": 106,
        "title": "Importar Módulo Estándar",
        "description": "Importa y usa módulo de biblioteca estándar.",
        "difficulty": "easy",
        "category": "manejo de paquetes",
        "points": 10,
        "example_input": "módulo math",
        "example_output": "uso de math.sqrt()",
        "hints": ["import math", "math.sqrt(16) devuelve 4.0"]
    },
    {
        "id": 107,
        "title": "Import con Alias",
        "description": "Importa módulos con alias.",
        "difficulty": "easy",
        "category": "manejo de paquetes",
        "points": 10,
        "example_input": "numpy como np",
        "example_output": "np.array([1,2,3])",
        "hints": ["import numpy as np", "Alias hace código más conciso"]
    },
    {
        "id": 108,
        "title": "From Import",
        "description": "Importa funciones específicas de un módulo.",
        "difficulty": "easy",
        "category": "manejo de paquetes",
        "points": 10,
        "example_input": "datetime",
        "example_output": "from datetime import datetime",
        "hints": ["from modulo import funcion", "Solo importa lo necesario"]
    },
    {
        "id": 109,
        "title": "Verificar Módulo Instalado",
        "description": "Verifica si un módulo está instalado.",
        "difficulty": "easy",
        "category": "manejo de paquetes",
        "points": 10,
        "example_input": "'requests'",
        "example_output": "True/False",
        "hints": ["try: import requests", "except ImportError: return False"]
    },
    {
        "id": 110,
        "title": "Listar Atributos de Módulo",
        "description": "Lista todos los atributos disponibles en un módulo.",
        "difficulty": "easy",
        "category": "manejo de paquetes",
        "points": 10,
        "example_input": "math",
        "example_output": "['sqrt', 'pi', 'sin', ...]",
        "hints": ["dir(math)", "Filtra atributos privados con _"]
    },
    
    # MANEJO DE PAQUETES - Medio
    {
        "id": 111,
        "title": "Import Dinámico",
        "description": "Importa módulos dinámicamente en tiempo de ejecución.",
        "difficulty": "medium",
        "category": "manejo de paquetes",
        "points": 20,
        "example_input": "'math' (como string)",
        "example_output": "módulo math importado",
        "hints": ["importlib.import_module('math')", "Útil para plugins"]
    },
    {
        "id": 112,
        "title": "Crear Paquete Simple",
        "description": "Crea estructura de paquete Python con __init__.py.",
        "difficulty": "medium",
        "category": "manejo de paquetes",
        "points": 20,
        "example_input": "mi_paquete/",
        "example_output": "paquete importable",
        "hints": ["__init__.py marca directorio como paquete", "Define __all__ para control de imports"]
    },
    {
        "id": 113,
        "title": "Reload de Módulo",
        "description": "Recarga un módulo ya importado.",
        "difficulty": "medium",
        "category": "manejo de paquetes",
        "points": 20,
        "example_input": "módulo modificado",
        "example_output": "cambios reflejados",
        "hints": ["from importlib import reload", "reload(modulo)"]
    },
    {
        "id": 114,
        "title": "Import Relativo",
        "description": "Usa imports relativos en paquetes.",
        "difficulty": "medium",
        "category": "manejo de paquetes",
        "points": 20,
        "example_input": "from . import modulo",
        "example_output": "import desde mismo paquete",
        "hints": [". para mismo nivel", ".. para nivel superior"]
    },
    {
        "id": 115,
        "title": "Namespace Package",
        "description": "Crea y usa namespace packages.",
        "difficulty": "medium",
        "category": "manejo de paquetes",
        "points": 20,
        "example_input": "múltiples directorios mismo namespace",
        "example_output": "paquete distribuido",
        "hints": ["Sin __init__.py", "Python 3.3+ soporta PEP 420"]
    },
    
    # MANEJO DE PAQUETES - Difícil
    {
        "id": 116,
        "title": "Sistema de Plugins",
        "description": "Implementa sistema de plugins con carga dinámica.",
        "difficulty": "hard",
        "category": "manejo de paquetes",
        "points": 30,
        "example_input": "directorio plugins/",
        "example_output": "todos los plugins cargados",
        "hints": ["Escanea directorio", "Importa dinámicamente", "Usa inspección"]
    },
    {
        "id": 117,
        "title": "Import Hook Personalizado",
        "description": "Crea import hook personalizado con sys.meta_path.",
        "difficulty": "hard",
        "category": "manejo de paquetes",
        "points": 30,
        "example_input": "custom import logic",
        "example_output": "imports interceptados",
        "hints": ["Implementa MetaPathFinder", "Override find_module/find_spec"]
    },
    {
        "id": 118,
        "title": "Lazy Import",
        "description": "Implementa lazy loading de módulos pesados.",
        "difficulty": "hard",
        "category": "manejo de paquetes",
        "points": 30,
        "example_input": "módulo grande",
        "example_output": "importado solo cuando se usa",
        "hints": ["__getattr__ en módulo", "importlib.util.LazyLoader"]
    },
    {
        "id": 119,
        "title": "Versionado de Paquetes",
        "description": "Maneja múltiples versiones del mismo paquete.",
        "difficulty": "hard",
        "category": "manejo de paquetes",
        "points": 30,
        "example_input": "pkg v1.0 y v2.0",
        "example_output": "ambas versiones usables",
        "hints": ["Manipula sys.path", "Usa entornos virtuales"]
    },
    {
        "id": 120,
        "title": "Auto-discovery de Módulos",
        "description": "Descubre y carga automáticamente todos los módulos en un paquete.",
        "difficulty": "hard",
        "category": "manejo de paquetes",
        "points": 30,
        "example_input": "paquete con submódulos",
        "example_output": "todos importados automáticamente",
        "hints": ["pkgutil.walk_packages", "Itera sobre módulos del paquete"]
    },
    
    # FECHAS - Fácil
    {
        "id": 121,
        "title": "Fecha Actual",
        "description": "Obtén la fecha y hora actual.",
        "difficulty": "easy",
        "category": "fechas",
        "points": 10,
        "example_input": "N/A",
        "example_output": "2023-12-25 10:30:00",
        "hints": ["from datetime import datetime", "datetime.now()"]
    },
    {
        "id": 122,
        "title": "Formatear Fecha",
        "description": "Formatea una fecha como string.",
        "difficulty": "easy",
        "category": "fechas",
        "points": 10,
        "example_input": "datetime object",
        "example_output": "'25/12/2023'",
        "hints": ["strftime('%d/%m/%Y')", "%d día, %m mes, %Y año"]
    },
    {
        "id": 123,
        "title": "Parsear Fecha",
        "description": "Convierte string a objeto datetime.",
        "difficulty": "easy",
        "category": "fechas",
        "points": 10,
        "example_input": "'2023-12-25'",
        "example_output": "datetime object",
        "hints": ["datetime.strptime('2023-12-25', '%Y-%m-%d')", "strptime parsea strings"]
    },
    {
        "id": 124,
        "title": "Diferencia de Días",
        "description": "Calcula días entre dos fechas.",
        "difficulty": "easy",
        "category": "fechas",
        "points": 10,
        "example_input": "fecha1, fecha2",
        "example_output": "10 días",
        "hints": ["Resta dos datetime objects", "(fecha2 - fecha1).days"]
    },
    {
        "id": 125,
        "title": "Añadir Días",
        "description": "Añade días a una fecha.",
        "difficulty": "easy",
        "category": "fechas",
        "points": 10,
        "example_input": "fecha, 7 días",
        "example_output": "nueva fecha",
        "hints": ["from datetime import timedelta", "fecha + timedelta(days=7)"]
    },
    
    # FECHAS - Medio
    {
        "id": 126,
        "title": "Día de la Semana",
        "description": "Obtén el día de la semana de una fecha.",
        "difficulty": "medium",
        "category": "fechas",
        "points": 20,
        "example_input": "2023-12-25",
        "example_output": "'Lunes'",
        "hints": ["fecha.strftime('%A')", "O usa fecha.weekday() (0=Lunes)"]
    },
    {
        "id": 127,
        "title": "Timezone Conversion",
        "description": "Convierte entre zonas horarias.",
        "difficulty": "medium",
        "category": "fechas",
        "points": 20,
        "example_input": "UTC a EST",
        "example_output": "hora convertida",
        "hints": ["import pytz", "datetime.astimezone()"]
    },
    {
        "id": 128,
        "title": "Último Día del Mes",
        "description": "Encuentra el último día de un mes.",
        "difficulty": "medium",
        "category": "fechas",
        "points": 20,
        "example_input": "febrero 2024",
        "example_output": "29 (año bisiesto)",
        "hints": ["import calendar", "calendar.monthrange(year, month)"]
    },
    {
        "id": 129,
        "title": "Edad desde Fecha de Nacimiento",
        "description": "Calcula edad exacta desde fecha de nacimiento.",
        "difficulty": "medium",
        "category": "fechas",
        "points": 20,
        "example_input": "'1990-05-15'",
        "example_output": "33 años",
        "hints": ["Considera año, mes y día", "Compara con fecha actual"]
    },
    {
        "id": 130,
        "title": "Generar Rango de Fechas",
        "description": "Genera lista de fechas entre dos fechas.",
        "difficulty": "medium",
        "category": "fechas",
        "points": 20,
        "example_input": "inicio, fin",
        "example_output": "lista de fechas",
        "hints": ["Usa timedelta en bucle", "O pandas.date_range()"]
    },
    
    # FECHAS - Difícil
    {
        "id": 131,
        "title": "Calcular Días Laborables",
        "description": "Calcula días laborables entre dos fechas excluyendo festivos.",
        "difficulty": "hard",
        "category": "fechas",
        "points": 30,
        "example_input": "inicio, fin, lista_festivos",
        "example_output": "número de días laborables",
        "hints": ["Excluye sábados, domingos y festivos", "Itera día por día"]
    },
    {
        "id": 132,
        "title": "Parser de Fecha Natural",
        "description": "Parsea fechas en lenguaje natural.",
        "difficulty": "hard",
        "category": "fechas",
        "points": 30,
        "example_input": "'hace 3 días'",
        "example_output": "datetime object",
        "hints": ["Maneja múltiples formatos", "Considera 'ayer', 'mañana', etc."]
    },
    {
        "id": 133,
        "title": "Cron Expression Evaluator",
        "description": "Evalúa si una fecha coincide con expresión cron.",
        "difficulty": "hard",
        "category": "fechas",
        "points": 30,
        "example_input": "'0 9 * * 1' (cada lunes 9am)",
        "example_output": "True si fecha coincide",
        "hints": ["Parsea campos cron", "Verifica minuto, hora, día, mes, día semana"]
    },
    {
        "id": 134,
        "title": "Calendario Perpetuo",
        "description": "Genera calendario para cualquier mes/año.",
        "difficulty": "hard",
        "category": "fechas",
        "points": 30,
        "example_input": "12, 2023",
        "example_output": "calendario diciembre 2023 formateado",
        "hints": ["calendar.monthcalendar()", "Formatea con semanas"]
    },
    {
        "id": 135,
        "title": "Calcular Siguiente Fecha Específica",
        "description": "Encuentra la próxima ocurrencia de 'tercer martes del mes'.",
        "difficulty": "hard",
        "category": "fechas",
        "points": 30,
        "example_input": "'tercer martes'",
        "example_output": "próxima fecha",
        "hints": ["Itera días del mes", "Cuenta ocurrencias del día de semana"]
    },
    
    # TIPOS DE ERROR - Fácil
    {
        "id": 136,
        "title": "Try-Except Básico",
        "description": "Maneja excepción de división por cero.",
        "difficulty": "easy",
        "category": "tipos de error",
        "points": 10,
        "example_input": "10 / 0",
        "example_output": "Error capturado",
        "hints": ["try: ... except ZeroDivisionError:", "Previene crash"]
    },
    {
        "id": 137,
        "title": "Múltiples Excepciones",
        "description": "Maneja diferentes tipos de excepciones.",
        "difficulty": "easy",
        "category": "tipos de error",
        "points": 10,
        "example_input": "varios tipos de errores",
        "example_output": "mensaje específico por tipo",
        "hints": ["except ValueError:", "except TypeError:", "Bloques separados"]
    },
    {
        "id": 138,
        "title": "Finally Block",
        "description": "Usa bloque finally para limpieza.",
        "difficulty": "easy",
        "category": "tipos de error",
        "points": 10,
        "example_input": "archivo abierto",
        "example_output": "siempre se cierra",
        "hints": ["finally: siempre se ejecuta", "Útil para liberar recursos"]
    },
    {
        "id": 139,
        "title": "Raise Exception",
        "description": "Lanza una excepción personalizada.",
        "difficulty": "easy",
        "category": "tipos de error",
        "points": 10,
        "example_input": "condición inválida",
        "example_output": "ValueError lanzado",
        "hints": ["raise ValueError('mensaje')", "Lanza cuando detectas error"]
    },
    {
        "id": 140,
        "title": "Exception con Mensaje",
        "description": "Captura y muestra mensaje de error.",
        "difficulty": "easy",
        "category": "tipos de error",
        "points": 10,
        "example_input": "error",
        "example_output": "muestra str(e)",
        "hints": ["except Exception as e:", "print(str(e))"]
    },
    
    # TIPOS DE ERROR - Medio
    {
        "id": 141,
        "title": "Custom Exception Class",
        "description": "Crea clase de excepción personalizada.",
        "difficulty": "medium",
        "category": "tipos de error",
        "points": 20,
        "example_input": "error de validación",
        "example_output": "ValidationError",
        "hints": ["class ValidationError(Exception):", "Hereda de Exception"]
    },
    {
        "id": 142,
        "title": "Exception Chaining",
        "description": "Encadena excepciones con contexto.",
        "difficulty": "medium",
        "category": "tipos de error",
        "points": 20,
        "example_input": "error anidado",
        "example_output": "raise ... from ...",
        "hints": ["raise NewError() from original_error", "Preserva contexto"]
    },
    {
        "id": 143,
        "title": "Context Manager para Errores",
        "description": "Crea context manager con manejo de errores.",
        "difficulty": "medium",
        "category": "tipos de error",
        "points": 20,
        "example_input": "with mi_context():",
        "example_output": "limpieza automática",
        "hints": ["__enter__ y __exit__", "__exit__ recibe info de excepción"]
    },
    {
        "id": 144,
        "title": "Retry Decorator",
        "description": "Implementa decorador que reintenta en caso de error.",
        "difficulty": "medium",
        "category": "tipos de error",
        "points": 20,
        "example_input": "función que puede fallar",
        "example_output": "reintenta 3 veces",
        "hints": ["Usa decorador", "Captura excepción y reintenta"]
    },
    {
        "id": 145,
        "title": "Logging de Errores",
        "description": "Registra errores con módulo logging.",
        "difficulty": "medium",
        "category": "tipos de error",
        "points": 20,
        "example_input": "excepción",
        "example_output": "logged con traceback",
        "hints": ["import logging", "logging.exception('mensaje')"]
    },
    
    # TIPOS DE ERROR - Difícil
    {
        "id": 146,
        "title": "Exception Hierarchy",
        "description": "Crea jerarquía de excepciones personalizadas.",
        "difficulty": "hard",
        "category": "tipos de error",
        "points": 30,
        "example_input": "sistema de errores",
        "example_output": "BaseError -> SubErrors",
        "hints": ["Herencia múltiple", "Captura desde más específica a general"]
    },
    {
        "id": 147,
        "title": "Exception con Contexto Rico",
        "description": "Excepción con información de contexto detallada.",
        "difficulty": "hard",
        "category": "tipos de error",
        "points": 30,
        "example_input": "error complejo",
        "example_output": "excepción con metadata",
        "hints": ["Agrega atributos personalizados", "Override __str__"]
    },
    {
        "id": 148,
        "title": "Global Exception Handler",
        "description": "Implementa manejador global de excepciones no capturadas.",
        "difficulty": "hard",
        "category": "tipos de error",
        "points": 30,
        "example_input": "sys.excepthook",
        "example_output": "captura todos los errores",
        "hints": ["sys.excepthook = custom_handler", "Procesa excepciones no manejadas"]
    },
    {
        "id": 149,
        "title": "Async Exception Handling",
        "description": "Maneja excepciones en código asíncrono.",
        "difficulty": "hard",
        "category": "tipos de error",
        "points": 30,
        "example_input": "async/await con errores",
        "example_output": "excepciones async manejadas",
        "hints": ["try/except en funciones async", "asyncio.gather con return_exceptions"]
    },
    {
        "id": 150,
        "title": "Exception Suppression",
        "description": "Implementa supresión condicional de excepciones.",
        "difficulty": "hard",
        "category": "tipos de error",
        "points": 30,
        "example_input": "contextlib.suppress",
        "example_output": "errores ignorados selectivamente",
        "hints": ["from contextlib import suppress", "with suppress(TypeError, ValueError):"]
    },
    
    # FUNCIONES DE ORDEN SUPERIOR - Fácil
    {
        "id": 151,
        "title": "Map Simple",
        "description": "Usa map para aplicar función a lista.",
        "difficulty": "easy",
        "category": "funciones de orden superior",
        "points": 15,
        "example_input": "[1, 2, 3, 4]",
        "example_output": "[2, 4, 6, 8]",
        "hints": ["map(funcion, lista)", "Convierte resultado a lista"]
    },
    {
        "id": 152,
        "title": "Filter Simple",
        "description": "Filtra elementos con filter.",
        "difficulty": "easy",
        "category": "funciones de orden superior",
        "points": 15,
        "example_input": "[1, 2, 3, 4, 5, 6]",
        "example_output": "[2, 4, 6]",
        "hints": ["filter(funcion_predicado, lista)", "Función retorna True/False"]
    },
    {
        "id": 153,
        "title": "Reduce Simple",
        "description": "Reduce lista a un valor con reduce.",
        "difficulty": "easy",
        "category": "funciones de orden superior",
        "points": 15,
        "example_input": "[1, 2, 3, 4]",
        "example_output": "10 (suma)",
        "hints": ["from functools import reduce", "reduce(lambda x,y: x+y, lista)"]
    },
    {
        "id": 154,
        "title": "Sorted con Key",
        "description": "Ordena usando función key.",
        "difficulty": "easy",
        "category": "funciones de orden superior",
        "points": 15,
        "example_input": "['a', 'bb', 'ccc']",
        "example_output": "['ccc', 'bb', 'a'] (por longitud desc)",
        "hints": ["sorted(lista, key=len, reverse=True)", "key especifica criterio"]
    },
    {
        "id": 155,
        "title": "Any y All",
        "description": "Usa any/all para validar condiciones.",
        "difficulty": "easy",
        "category": "funciones de orden superior",
        "points": 15,
        "example_input": "[True, False, True]",
        "example_output": "any=True, all=False",
        "hints": ["any() retorna True si alguno es True", "all() retorna True si todos son True"]
    },
    
    # FUNCIONES DE ORDEN SUPERIOR - Medio
    {
        "id": 156,
        "title": "Compose Functions",
        "description": "Compone múltiples funciones.",
        "difficulty": "medium",
        "category": "funciones de orden superior",
        "points": 25,
        "example_input": "f, g, h",
        "example_output": "f(g(h(x)))",
        "hints": ["Usa reduce para composición", "lambda x: f(g(x))"]
    },
    {
        "id": 157,
        "title": "Partial Application",
        "description": "Usa functools.partial para aplicación parcial.",
        "difficulty": "medium",
        "category": "funciones de orden superior",
        "points": 25,
        "example_input": "función multiparámetro",
        "example_output": "función con parámetros prefijados",
        "hints": ["from functools import partial", "partial(funcion, arg1, arg2)"]
    },
    {
        "id": 158,
        "title": "Decorador Parametrizado",
        "description": "Crea decorador que acepta parámetros.",
        "difficulty": "medium",
        "category": "funciones de orden superior",
        "points": 25,
        "example_input": "@repeat(3)",
        "example_output": "función ejecutada 3 veces",
        "hints": ["Tres niveles de funciones anidadas", "decorador(params)(funcion)"]
    },
    {
        "id": 159,
        "title": "MapReduce Pattern",
        "description": "Implementa patrón MapReduce simple.",
        "difficulty": "medium",
        "category": "funciones de orden superior",
        "points": 25,
        "example_input": "datos, map_func, reduce_func",
        "example_output": "resultado agregado",
        "hints": ["Primero map, luego reduce", "Procesa en paralelo si es posible"]
    },
    {
        "id": 160,
        "title": "Memoization Decorator",
        "description": "Implementa decorador de memoización.",
        "difficulty": "medium",
        "category": "funciones de orden superior",
        "points": 25,
        "example_input": "función costosa",
        "example_output": "resultados cacheados",
        "hints": ["Usa diccionario para cache", "Verifica argumentos como key"]
    },
    
    # FUNCIONES DE ORDEN SUPERIOR - Difícil
    {
        "id": 161,
        "title": "Transducer Pattern",
        "description": "Implementa transducers para composición eficiente.",
        "difficulty": "hard",
        "category": "funciones de orden superior",
        "points": 35,
        "example_input": "pipeline de transformaciones",
        "example_output": "ejecución optimizada",
        "hints": ["Evita iteraciones intermedias", "Compone transformaciones antes de aplicar"]
    },
    {
        "id": 162,
        "title": "Monadic Pipeline",
        "description": "Implementa pipeline monádico para manejo de errores.",
        "difficulty": "hard",
        "category": "funciones de orden superior",
        "points": 35,
        "example_input": "operaciones que pueden fallar",
        "example_output": "Maybe/Either monad",
        "hints": ["Encadena operaciones con bind", "Maneja None/Error automáticamente"]
    },
    {
        "id": 163,
        "title": "Function Builder Pattern",
        "description": "Crea DSL con funciones de orden superior.",
        "difficulty": "hard",
        "category": "funciones de orden superior",
        "points": 35,
        "example_input": "query builder",
        "example_output": "query.where().select().limit()",
        "hints": ["Encadena llamadas", "Cada método retorna self o nuevo builder"]
    },
    {
        "id": 164,
        "title": "Type Dispatcher",
        "description": "Implementa despacho basado en tipos con funciones.",
        "difficulty": "hard",
        "category": "funciones de orden superior",
        "points": 35,
        "example_input": "valor de cualquier tipo",
        "example_output": "función apropiada llamada",
        "hints": ["Diccionario tipo -> función", "isinstance para detección"]
    },
    {
        "id": 165,
        "title": "Pipeline de Evaluación Perezosa",
        "description": "Implementa evaluación perezosa con generadores en pipeline de funciones.",
        "difficulty": "hard",
        "category": "funciones de orden superior",
        "points": 35,
        "example_input": "range(1000000)",
        "example_output": "{'eficiente_en_memoria': True, 'primeros_10_resultados': [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]}",
        "hints": ["Usa generadores", "Yield en lugar de return", "Encadena funciones generadoras"]
    }
]


def get_challenges_db(language: str = 'en') -> list:
    """
    Get the appropriate challenges database based on language.
    
    Args:
        language (str): Language code ('en' for English, 'es' for Spanish).
        
    Returns:
        list: The challenges database for the specified language.
    """
    if language == 'es':
        return CHALLENGES_DB_ES
    return CHALLENGES_DB_EN


def get_categories(language: str = 'en') -> list:
    """
    Get a list of all available categories.
    
    Args:
        language (str): Language code ('en' or 'es').
    
    Returns:
        list: List of unique categories.
    """
    categories = set()
    challenges_db = get_challenges_db(language)
    for challenge in challenges_db:
        categories.add(challenge.get('category', ''))
    return sorted(list(categories))


def get_difficulties(language: str = 'en') -> list:
    """
    Get a list of all available difficulty levels.
    
    Args:
        language (str): Language code ('en' or 'es').
    
    Returns:
        list: List of unique difficulties.
    """
    difficulties = set()
    challenges_db = get_challenges_db(language)
    for challenge in challenges_db:
        difficulties.add(challenge.get('difficulty', ''))
    return sorted(list(difficulties))