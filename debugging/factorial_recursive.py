#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.
    
    The factorial of a non-negative integer n is the product of all positive
    integers less than or equal to n. It is denoted by n! and defined as:
    n! = n × (n-1) × (n-2) × ... × 3 × 2 × 1
    By definition, 0! = 1.
    
    Parameters:
    n (int): A non-negative integer for which to calculate the factorial
    
    Returns:
    int: The factorial of the input number n
    
    Example:
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    """
    if n == 0:
        # Base case: factorial of 0 is 1
        return 1
    else:
        # Recursive case: n! = n × (n-1)!
        return n * factorial(n-1)

# Get the factorial number from command line argument
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
