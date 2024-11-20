#!/usr/bin/python3
"""
This is a module for Minimum operations
"""


def minOperations(n):
    """
    Funtion for mini Operation
    """
    # all the output has to be 2 char at least
    if (n < 2):
        return 0
    operate, root = 0, 2
    while root <= n:
        # if n divids by root wothout a ramainder
        if n % root == 0:
            # Total quotient by root = total operations
            operate += root
            # set n to the remainder
            n = n / root
            # decrease the root to divide further and the smaller quotient
            root -= 1
        # increamet the root until the qoutient is an even num
        root += 1
    return operate
