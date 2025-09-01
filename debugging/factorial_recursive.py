#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Computes the factorial of a non-negative integer using recursion.
        The factorial of a number n (written n!) is the product of all positive integers less than or equal to n.
        Example: factorial(5) = 5 * 4 * 3 * 2 * 1 = 120

    Parameters:
        n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
        int: The factorial of the input integer n.
             Returns 1 if n is 0, as 0! is defined to be 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read the first command-line argument, convert it to an integer, and calculate its factorial
f = factorial(int(sys.argv[1]))

# Print the result to the console
print(f)
