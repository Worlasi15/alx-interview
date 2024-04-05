#!/usr/bin/python3
"""
Module for making change problem
"""

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total
    """
    if total < 1:
        return 0

    # Initialize a list to store the fewest number of coins needed for each value from 0 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins needed for total of 0

    # Iterate through each coin value
    for coin in coins:
        # For each coin value, update the dp list to store the fewest number of coins needed
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still float('inf'), it means the total cannot be met by any number of coins
    return dp[total] if dp[total] != float('inf') else -1

if __name__ == "__main__":
    coins = [1, 2, 25]
    total = 37
    print(makeChange(coins, total))  # Output should be 7

    coins = [1256, 54, 48, 16, 102]
    total = 1453
    print(makeChange(coins, total))  # Output should be -1
