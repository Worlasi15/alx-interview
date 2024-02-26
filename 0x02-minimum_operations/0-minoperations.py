#!/usr/bin/python3
def minOperations(n):
    if n <= 1:
        return 0

    # Initialize an array to store the minimum operations required for each number
    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        # Check if i is prime
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                # If i is divisible by j, update dp[i] with the minimum operations
                dp[i] = min(dp[i], dp[j] + i // j)
                break

        # If i is prime, update dp[i] with the minimum operations
        dp[i] = min(dp[i], i)

    return dp[n] if dp[n] != float('inf') else 0

# Test cases
n1 = 4
n2 = 12

print("Min # of operations to reach {} char: {}".format(n1, minOperations(n1)))
print("Min # of operations to reach {} char: {}".format(n2, minOperations(n2)))
