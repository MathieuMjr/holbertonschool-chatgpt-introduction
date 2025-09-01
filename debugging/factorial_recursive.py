#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
        Compute the factorial of a non-negative integer n using recursion.

    Parameters:
        n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
        int: The factorial of n (i.e., n! = n * (n-1) * ... * 1). Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the input from command line arguments, convert to integer
f = factorial(int(sys.argv[1]))

# Print the result
print(f)