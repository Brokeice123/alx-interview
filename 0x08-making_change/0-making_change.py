#!/usr/bin/python3
"""
Python module for giving change
"""


def makeChange(coins, total):
    """
    Python function
    """
    if total <= 0:
        return 0

    # Create an array to store the minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate over each coin
    for coin in coins:
        # Update the dp array for each amount from coin to total
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still inf, it means we can't make the total with the given coins
    return dp[total] if dp[total] != float('inf') else -1
