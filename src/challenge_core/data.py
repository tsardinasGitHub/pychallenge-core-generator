"""
Challenges Database

This module stores the dictionary of challenges that acts as the database.
Each category has at least one challenge per difficulty level (easy, medium, hard).
"""

CHALLENGES_DB = [
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

    # COMPRENSION DE LISTAS - 15 challenges (5 easy, 5 medium, 5 hard)
    {
        "id": 10,
        "title": "List Comprehension Filter",
        "description": "Use list comprehension to filter even numbers from a list and square them.",
        "difficulty": "easy",
        "category": "comprension de listas",
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
        "category": "comprension de listas",
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
        "category": "comprension de listas",
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
        "category": "comprension de listas",
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
        "category": "comprension de listas",
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
        "category": "comprension de listas",
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
        "category": "comprension de listas",
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
        "category": "comprension de listas",
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
        "category": "comprension de listas",
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
        "category": "comprension de listas",
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
        "category": "comprension de listas",
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
        "category": "comprension de listas",
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
        "category": "comprension de listas",
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
        "category": "comprension de listas",
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
        "category": "comprension de listas",
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

    # EXPRESIONES REGULARES - 15 challenges (5 easy, 5 medium, 5 hard)
    {
        "id": 16,
        "title": "Basic Pattern Matching",
        "description": "Use regex to find all words that start with a specific letter in a text.",
        "difficulty": "easy",
        "category": "expresiones regulares",
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
        "category": "expresiones regulares",
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
        "category": "expresiones regulares",
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
        "category": "expresiones regulares",
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
        "category": "expresiones regulares",
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
        "category": "expresiones regulares",
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
        "category": "expresiones regulares",
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
        "category": "expresiones regulares",
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
        "category": "expresiones regulares",
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
        "category": "expresiones regulares",
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
        "category": "expresiones regulares",
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
        "category": "expresiones regulares",
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
        "category": "expresiones regulares",
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
        "category": "expresiones regulares",
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
        "category": "expresiones regulares",
        "points": 35,
        "example_input": "'x = 10 + y * 2'",
        "example_output": "['x', '=', '10', '+', 'y', '*', '2']",
        "hints": ["Pattern for identifiers, numbers, operators", "Use re.findall() with multiple patterns", "Handle different token types"]
    },

    # MANEJO DE FICHEROS - 15 challenges (5 easy, 5 medium, 5 hard)
    {
        "id": 19,
        "title": "Simple File Reader",
        "description": "Read the content of a text file and return it as a string.",
        "difficulty": "easy",
        "category": "manejo de ficheros",
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
        "category": "manejo de ficheros",
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
        "category": "manejo de ficheros",
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
        "category": "manejo de ficheros",
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
        "category": "manejo de ficheros",
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
        "category": "manejo de ficheros",
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
        "category": "manejo de ficheros",
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
        "category": "manejo de ficheros",
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
        "category": "manejo de ficheros",
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
        "category": "manejo de ficheros",
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
        "category": "manejo de ficheros",
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
        "category": "manejo de ficheros",
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
        "category": "manejo de ficheros",
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
        "category": "manejo de ficheros",
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
        "category": "manejo de ficheros",
        "points": 40,
        "example_input": "('config.ini', {'database': {'host': 'localhost'}})",
        "example_output": "{'updated': True, 'format': 'ini', 'sections': ['database', 'server']}",
        "hints": ["Use configparser for INI", "Handle different formats", "Validate structure"]
    },

    # MANEJO DE PAQUETES - 15 challenges (5 easy, 5 medium, 5 hard)
    {
        "id": 22,
        "title": "Basic Package Usage",
        "description": "Import and use basic Python modules (math, random, datetime) in a single function.",
        "difficulty": "easy",
        "category": "manejo de paquetes",
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
        "category": "manejo de paquetes",
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
        "category": "manejo de paquetes",
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
        "category": "manejo de paquetes",
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
        "category": "manejo de paquetes",
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
        "category": "manejo de paquetes",
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
        "category": "manejo de paquetes",
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
        "category": "manejo de paquetes",
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
        "category": "manejo de paquetes",
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
        "category": "manejo de paquetes",
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
        "category": "manejo de paquetes",
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
        "category": "manejo de paquetes",
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
        "category": "manejo de paquetes",
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
        "category": "manejo de paquetes",
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
        "category": "manejo de paquetes",
        "points": 40,
        "example_input": "[1, 2, 3, 4, 5]",
        "example_output": "{'threaded_time': 1.23, 'multiprocess_time': 0.45, 'results': [1, 4, 9, 16, 25]}",
        "hints": ["Import threading and multiprocessing", "Compare execution times", "Use Pool for multiprocessing"]
    },

    # FECHAS - 15 challenges (5 easy, 5 medium, 5 hard)
    {
        "id": 25,
        "title": "Simple Date Operations",
        "description": "Calculate age in years given a birth date.",
        "difficulty": "easy",
        "category": "fechas",
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
        "category": "fechas",
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
        "category": "fechas",
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
        "category": "fechas",
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
        "category": "fechas",
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
        "category": "fechas",
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
        "category": "fechas",
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
        "category": "fechas",
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
        "category": "fechas",
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
        "category": "fechas",
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
        "category": "fechas",
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
        "category": "fechas",
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
        "category": "fechas",
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
        "category": "fechas",
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
        "category": "fechas",
        "points": 40,
        "example_input": "'1990-05-15'",
        "example_output": "{'years': 33, 'months': 5, 'days': 7, 'total_days': 12234}",
        "hints": ["Calculate year difference", "Handle month and day differences", "Account for leap years"]
    },

    # TIPOS DE ERROR - 15 challenges (5 easy, 5 medium, 5 hard)
    {
        "id": 28,
        "title": "Basic Exception Handling",
        "description": "Handle a simple division by zero error and return a user-friendly message.",
        "difficulty": "easy",
        "category": "tipos de error",
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
        "category": "tipos de error",
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
        "category": "tipos de error",
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
        "category": "tipos de error",
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
        "category": "tipos de error",
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
        "category": "tipos de error",
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
        "category": "tipos de error",
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
        "category": "tipos de error",
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
        "category": "tipos de error",
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
        "category": "tipos de error",
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
        "category": "tipos de error",
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
        "category": "tipos de error",
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
        "category": "tipos de error",
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
        "category": "tipos de error",
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
        "category": "tipos de error",
        "points": 40,
        "example_input": "{'data': 'invalid', 'strict': True}",
        "example_output": "{'error_chain': ['ValueError', 'DataProcessingError'], 'original': 'invalid literal', 'context': 'preserved'}",
        "hints": ["Use 'raise ... from ...'", "Preserve original exception", "Chain multiple errors"]
    },

    # FUNCIONES DE ORDEN SUPERIOR - 15 challenges (5 easy, 5 medium, 5 hard)
    {
        "id": 31,
        "title": "Simple Higher Order Function",
        "description": "Create a function that takes another function as parameter and applies it to a number.",
        "difficulty": "easy",
        "category": "funciones de orden superior",
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
        "category": "funciones de orden superior",
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
        "category": "funciones de orden superior",
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
        "category": "funciones de orden superior",
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
        "category": "funciones de orden superior",
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
        "category": "funciones de orden superior",
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
        "category": "funciones de orden superior",
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
        "category": "funciones de orden superior",
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
        "category": "funciones de orden superior",
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
        "category": "funciones de orden superior",
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
        "category": "funciones de orden superior",
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
        "category": "funciones de orden superior",
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
        "category": "funciones de orden superior",
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
        "category": "funciones de orden superior",
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
        "category": "funciones de orden superior",
        "points": 35,
        "example_input": "range(1000000)",
        "example_output": "{'memory_efficient': True, 'first_10_results': [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]}",
        "hints": ["Use generators", "Yield instead of return", "Chain generator functions"]
    }
]


def get_categories() -> list:
    """
    Get a list of all available categories.
    
    Returns:
        list: List of unique categories.
    """
    categories = set()
    for challenge in CHALLENGES_DB:
        categories.add(challenge.get('category', ''))
    return sorted(list(categories))


def get_difficulties() -> list:
    """
    Get a list of all available difficulty levels.
    
    Returns:
        list: List of unique difficulties.
    """
    difficulties = set()
    for challenge in CHALLENGES_DB:
        difficulties.add(challenge.get('difficulty', ''))
    return sorted(list(difficulties))