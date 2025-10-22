"""
Challenges Database

This module stores the dictionary of challenges that acts as the database.
Each category has at least one challenge per difficulty level (easy, medium, hard).
"""

CHALLENGES_DB = [
    # MATHEMATICS - 3 challenges
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
    
    # STRINGS - 3 challenges
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

    # ALGORITHMS - 3 challenges
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

    # COMPRENSION DE LISTAS - 3 challenges
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

    # LAMBDAS - 3 challenges
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

    # EXPRESIONES REGULARES - 3 challenges
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

    # MANEJO DE FICHEROS - 3 challenges
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

    # MANEJO DE PAQUETES - 3 challenges
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

    # FECHAS - 3 challenges
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

    # TIPOS DE ERROR - 3 challenges
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

    # FUNCIONES DE ORDEN SUPERIOR - 3 challenges
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
        "id": 33,
        "title": "Higher Order Functions",
        "description": "Implement a decorator factory and function pipeline that can transform, filter, and reduce data with configurable operations.",
        "difficulty": "hard",
        "category": "funciones de orden superior",
        "points": 35,
        "example_input": "([1, 2, 3, 4, 5], [lambda x: x*2, lambda x: x > 5, sum])",
        "example_output": "{'transformed': [2, 4, 6, 8, 10], 'filtered': [6, 8, 10], 'reduced': 24}",
        "hints": ["Chain multiple function operations", "Implement pipeline pattern", "Use *args for variable functions"]
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