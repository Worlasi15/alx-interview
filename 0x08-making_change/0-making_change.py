#!/usr/bin/python3
"""
Module for making change using the fewest number of coins
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total amount

    Args:
        coins (list): List of coin denominations
        total (int): Total amount

    Returns:
        int: Fewest number of coins needed to meet the total amount,
             or -1 if the total cannot be met by any number of coins
    """
    if total <= 0:
        return 0

    # Initialize memoization table with max value
    memo = [float('inf')] * (total + 1)
    memo[0] = 0

    # Iterate through each coin denomination
    for coin in coins:
        # Update memoization table for each amount from coin to total
        for amount in range(coin, total + 1):
            memo[amount] = min(memo[amount], memo[amount - coin] + 1)

    return memo[total] if memo[total] != float('inf') else -1


if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))  # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
