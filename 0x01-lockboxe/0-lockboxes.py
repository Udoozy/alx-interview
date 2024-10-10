#!/usr/bin/python3
"""
Module for n number of locked boxes
"""


def canUnlockAll(boxes):
    """
     A prototype that return true or false value
    """
    if not boxes or type(boxes) is not list:
        return False

    unlocked = [0]
    for i in unlocked:
        for key in boxes[i]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
