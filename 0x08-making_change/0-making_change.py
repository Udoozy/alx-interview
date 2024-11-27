#!/usr/bin/python3

""" This module to makeChange"""


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
        The value of a coin will always be an integer greater than 0
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    others = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            others += 1
        if (total == 0):
            return others
    return -1
