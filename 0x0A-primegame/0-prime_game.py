#!/usr/bin/python3
"""
Prime game
"""


def is_prime(n):
    """function Checking if a number is prime
    Args:
        n (int): upper boundary of range. lower boundary is always 1
    """

    primeNums = []

    # List to track if each number is prime or not
    filtered = [True] * (n + 1)
    # Loop over numbers from 2 to n
    for prime in range(2, n + 1):
        if (filtered[prime]):
            primeNums.append(prime)

            # Mark all multiples of the current prime as not prime
            for i in range(prime, n + 1, prime):
                filtered[i] = False
    return primeNums


def isWinner(x, nums):
    """Determines the winner of each round
    Args:
        x (num) = The number of rounds
        nums (list)= array of n for each round
    Returns:
        str: name of player that won the most rounds or None"""

    if x is None or nums is None or x == 0 or nums == []:
        return None

    maria_wins = 0
    ben_wins = 0

    for i in range(x):
        primeNums = is_prime(nums[i])

        # Determine the winner of the round based on count of prime numbers
        if len(primeNums) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
