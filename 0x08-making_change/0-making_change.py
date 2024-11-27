#!/usr/bin/python3
"""Module for Making Change.
"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    
    # Initialize dp array where dp[x] represents the minimum coins needed to make amount x
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0

    # Populate the dp array
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be formed
    return dp[total] if dp[total] != float('inf') else -1
