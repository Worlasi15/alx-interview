#!/usr/bin/python3
"""
Determines the winner of the prime game for multiple rounds.
"""

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def isWinner(x, nums):
    """Determines the winner of each round."""
    maria_wins = 0
    for n in nums:
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        if len(primes) % 2 == 0:
            maria_wins += 1
    if maria_wins > x // 2:
        return "Maria"
    elif maria_wins < x // 2:
        return "Ben"
    else:
        return None
