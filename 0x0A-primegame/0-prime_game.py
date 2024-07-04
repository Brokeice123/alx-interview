#!/usr/bin/python3
"""
Prime game
"""


def isWinner(x, nums):
    def sieve(n):
        """ Generate list of primes up to n using the Sieve of
        Eratosthenes 
        """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if is_prime[p] == True:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def play_game(n):
        """ Simulate the game and return the winner 
        (True if Maria wins, False if Ben wins)
        """
        primes = sieve(n)
        primes_set = set(primes)
        turn = 0  # 0 for Maria, 1 for Ben
        while primes_set:
            # Current player picks the smallest prime number
            current_prime = min(primes_set)
            # Remove current_prime and its multiples
            primes_set -= {i for i in range(
                current_prime, n + 1, current_prime)
                }
            turn = 1 - turn  # Switch turns
        return turn == 1  # Maria wins if turn is 1 (meaning Ben had no moves)

    maria_wins = 0
    ben_wins = 0

    for num in nums:
        if num == 1:
            ben_wins += 1  # Ben wins automatically if num is 1
        else:
            if play_game(num):
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
