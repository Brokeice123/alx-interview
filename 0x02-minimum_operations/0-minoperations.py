#!/usr/bin/python3
"""
Python module that contains function minOperations
"""


def minOperations(n):
    """
    Function that calculates the fewest number of operations
    """

    min_ops = 0  # Initialize operations to 0

    if n <= 1:
        return 0

    # Iterate through numbers from 2 to n
    for i in range(2, n + 1):
        # While n is divisible by i,
        # keep dividing n by i and increment operations by i
        while n % i == 0:
            n = n / i  # Divide n by i

            # Increment operations by i, as i rep number of times 'i' is pasted
            min_ops += i
    return min_ops