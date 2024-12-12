#!/usr/bin/python3
"""
This is game bw Maria and Ben and determine the winner
"""


def primes(n):
    """
    Assuming Maria always goes first and
    both players play optimally,
    determine who the winner of each game is.
    """
    prime = []
    sieve = [True] * (n + 1)
    for i in range(2, n + 1):
        if (sieve[i]):
            prime.append(i)
            for m in range(i, n + 1, i):
                sieve[m] = False
    return prime


def isWinner(x, nums):
    """
    This is played x times and the winner is determined
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for k in range(x):
        prime = primes(nums[k])
        if len(prime) % 2 == 0:
            Ben = Ben + 1
        else:
            Maria = Maria + 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
