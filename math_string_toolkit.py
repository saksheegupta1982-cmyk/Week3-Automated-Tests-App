"""
math_string_toolkit.py
Mini library for Math & String operations
Designed for testability - pure functions, no external dependencies
TDD Aproach: Tests written first , then implementation
"""
# --------------- MATH FUNCTIONS ------------------

def add(a,b):
    """Add two numbers - basic unit test"""
    return a + b

def subtract(a,b):
    """ Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers - handles zero and negative edge cases"""
    return a * b

def divide(a, b):
    """Divide a by b 
    Edge case: b=   0 should raise ValueError(important for testing error conditions) 
    """
    if b == 0 : 
        raise ValueError("Cannot divide by zero" ) # Error conditions to test 
    return a/b 

def factorial(n):
    """ 
    Calculate factorial of n 
    Edge cases covered:
    - n =0, 1=> (base case) 
    - negative => ValueError
    """
    if not isinstance(n, int):
        raise TypeError("Factorial only for integers")  # Type validation
    if n< 0:
        raise ValueError("Factorial not defined for negative") # Error condition
    if n in (0,1):
        return 1  # Base case edge
    result = 1
    for i in range(2, n+1): 
        result *= i
    return result

def is_prime(n): 
    """
    Check if number is prime 
    Optimized with sqrt(n) - Refactored for performance
    Edge: 0,1=>False, 2=>True
    """
    if n<= 1:
        return False  
    if n <= 3:
        return True 
    if n % 2 == 0 or n % 3 == 0 :
        return False 
    # Refactored: 0(sqrt(n)) instead of 0(n) for performance
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0 :
            return False
        i +=6
    return True
# -----------------STRING FUNCTIONS--------------------
 
def reverse_string(s):
    """ Reverse a string - handles empty and single shar edge"""
    
    return s[::-1] # Pythonic slicing

def is_palindrome(s):
    """
    Check if string is palindrome
    Handles: case-insensitive, ignores spaces
    Example: "nurses run" => True, "Racecar" =>True
    """
    if not isinstance(s, str): 
        raise TypeError("Input must be string")
    # Cleaned for robust check - removesspaces and lowercases
    cleaned = ''.join(s.lower().split())
    return cleaned == cleaned[::-1]

def count_words(s):
    """Count words in string - edge: empty,multiple spaces"""
    if not isinstance(s, str):
        raise TypeError("Input must be string")
    if not s.strip():
        return 0 # caseEdge case: empty or only spaces
    return len(s.strip().split())

def parse_csv_line(line):
    """
    Parse a CSV line into list
    Example: "a, b, c" => ["a", "b", "c"]
    Edge: empty line => ValueErroe
    """
    if not isinstance(line, str):
        raise TypeError("CSV line must be string")
    if not line.strip():
        raise ValueError("Empty CSV line") # Error condition

    # Strip each part to handle " a , b "
    return [p.strip() for p in line.split(',')]

