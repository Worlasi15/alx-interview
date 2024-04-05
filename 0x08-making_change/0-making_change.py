#!/usr/bin/python3
"""A function to determine the fewest number of coins needed
   to meet a given amount total"""


def make_change(coins, total):
    """This function calculates the fewest number of coins needed
       to meet the given total amount"""
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            num_coins += 1
    if total == 0:
        return num_coins
    return -1


