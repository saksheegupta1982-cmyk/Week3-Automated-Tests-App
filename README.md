# Week 3 - Automated Tests for Python Applications

## Objective
Create a testable Python module + comprehensive test suite demonstrating TDD principles, unit tests, integration tests and documentation.

## Module Developed 
*File: 'math_string_toolkit.py'*
A mini library with 10 functions designed for easy testability (pure functions, no external deps).

*Math Functions (6):*
- 'add(a,b)', 'subtract(a,b)', 'multiply(a,b)' - basic ops
- 'divide(a,b)' - raises 'ValueError: Cannot divide by zero' if b = 0
- 'factorial(n)' - handles 0 =>1, negative => ValueError, float => TypeError
- 'is_prime(n)' - optimized with sqrt(n) logic

*String Functios (4):
- 'reverse_string(s)' - handles empty string edge
- 'is_palondrome(s)' - case - insensitive, ignores spaces. Eg: "nurses run" => True
- 'count_words(s)' - handles multiple spaces, empty => 0
- 'parse_csv_line(line)' - "a, b, c" => ["a", "b", "c"],empty => ValueError

##Testing Methodology - TDD 
*Approach Used: Test-Driven Development (TDD) - Red - Green- Refactor*
1. *Red:* wrote failing tests first in 'test_toolkit.py'(22 tests)
2. *Green:* Implemented 'math_string_toolkit.py' to pass tests
3. *Refactor:* Optimized 'is_prime()'from 0(n) to 0(sqrt(n)) and used 'strip()'/'lower()' for robust string checks. VErified no tests broke.

Framework: **pytest** chosen for clear assert syntax and verbose output.

## Test Documentation
|Test File | what it Covers| Why Chosen|
|---|---|---|
|test_add, test_subtract, test_multiply | Normal, negative, zero |Core functionality |
|test_divide | 10/2 =>5, 5/2=>2.5 |Normal flow|
|test_divide_by_zero |divide(10,0) raises ValueError | Criticial error condition |
|test_factorial | 0=>1,5=>120 | Base case edge |
|test_factorial_negative | -1 raises ValueError | Error handling |
 test_factorial_type_error | 5.5 raises TypeError | Type validation |
| test_is_primr | 2 => True, 4 =>False, 1=>False | Prime logic + edge|
| test_reverse_string | "hello" => "olleh", ""| Empty edge |
| test_is palindrome | "madam" => True, "Racecar" =>True | Case - insensitive logic |
| test_count_words | "hello world" =>2, ""=>0, "  "=>0 | Multiple spaces edge |
| test_parse_csv_line | "a,b,v" =>[a,b,c], " a , b "=>[a,b]|Stripping logic |
| test_parse_csv_empty | "" raises ValueError |  Empty input error |
| test_integration_math_flow | (5+3)*2/4 =>4 | Proves functions work together ( integration) |
| test_integration_string_flow | count-> palindrome ->reverse | String integration | 

Total:22 tests - 100% logic coverage of module.

## How to Run tests
'''bash 
# Install pytest
pip install pytest

# Run all tests with verbose output 
pytest -v

# Expected Output:
# 22 passed 

# Run with coverage
pytest --cov=math_string_toolkit

