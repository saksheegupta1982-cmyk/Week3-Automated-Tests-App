"""
test_toolkit.py - Comprehensive test suite using pytest
Run: pytest -v
Covers: unit, edge cases, error conditions, integration 
"""

import pytest 
from math_string_toolkit import *

# ------1-3:Unit Tests for Math -------

def test_add():
    # Normal and edge: negative, zero
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0 

def test_subtract():
    # Subtract normal and negative result 
    assert subtract(5, 3)==2
    assert subtract(0,5)== -5

def test_multiply():
    # Multiply normal and zero edge (zero is critical)
    assert multiply(2,3) ==6
    assert multiply(0,10)==0 

#--------4-6: Divide - Normal and Erroe ------
def test_divide():
    # Normal division 
    assert divide(10, 2) == 5
    
def test_divide_float():
    # Float result handling 
    assert divide (5,2) ==2.5

def test_divide_by_zero():
    # Error Condition - Important for evaluation criteria 
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0) 

#-------- 7-11: Factorial - Edge + Error ---------
def test_factorial_zero():
    # EDGE:0! = 1 base case    
    assert factorial(0) == 1 

def test_factorial_one():
    # EDGE: 1! = 1 base case 
    assert factorial(1) == 1 

def test_factorial_five():
    # Normal: 5! = 120
    assert factorial(5) == 120

def test_factorial_negative():
    # Error: negative not allowed
    with pytest.raises(ValueError):
        factorial(-1)

def test_factorial_type_error(): 
    # Erroe: only int allowed 
    with pytest.raises(TypeError):
        factorial(5.5)

# - -------12-13: Prime Check---------

def test_is_prime_true():
    # True cases :2 smallest prime, 17 prime
    assert is_prime(2) == True
    assert is_prime (17) == True

def test_is_prime_false():
    # False cases: 4 not prime, 1 not prime, 0not prime- edge cases
    assert is_prime(4) == False
    assert is_prime(1) == False
    assert is_prime(0) == False

# ------------14-18: String Unit Tests----------------

def test_reverse_string():
    # Normal, empty, single char
    assert reverse_string("hello") == "olleh"

def test_reverse_empty():
    assert reverse_string("") == "" # Edge: empty

def test_is_palindrome():
    # Normal palindrome and non-palindrome
    assert is_palindrome("madam") == True
    assert is_palindrome("hello") == False

def test_is_palindrome_case_space():
    #  Case-insensitive + space ignored logic - why this test chosen
    assert is_palindrome("Racecar") == True # Case-insensitive
    assert is_palindrome("nurses run") == True  # Ignores spaces

def test_count_words():
    # Edge: empty, multiple spaces
    assert count_words("hello world") == 2
    assert count_words("") == 0  # Edge: empty
    assert count_words("   ") == 0 #Edge: only spaces

# -------------19 - 20 : CSV  Parser -----------

def test_parse_csv_line():
    # Normal and stripping spaces robust check 
    assert parse_csv_line("a,b,c") == ["a", "b", "c"]
    assert parse_csv_line(" a , b ") == ["a", "b"] #Handles spaces

def test_parse_csv_empty():
    # Error: empty line should raise ValueError
    with pytest.raises(ValueError):
        parse_csv_line("")

#-----------------21: Integration Tests ----------------------

def test_integration_math_flow():
    # Integration: chaining math operations(5+3)*2/4 =4
    result = add(5, 3)
    result = multiply(result,2)
    result = divide(result, 4)
    assert result == 4 # Proves functions work together

def test_integration_string_flow():
    # Integration: count -> palindrome -> reverse 
    s = " Madam "
    assert count_words(s) == 1
    assert is_palindrome(s.strip()) == True
    assert reverse_string(s.strip().lower()) == "madam"
    














