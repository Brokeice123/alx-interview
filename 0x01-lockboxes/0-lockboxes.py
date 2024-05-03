#!/usr/bin/env python3
"""
This module contains a function that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    :param boxes: A list of lists representing the boxes
    :return: True if all boxes can be opened, else return False
    """
    keys = [0]
    """ list keys initialized with the first box (box 0) as unlocked.
    Keys stores indices of unlocked and accessible boxes """
    for key in keys:
        """ For each key, it accesses the corresponding box in boxes """
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    if len(keys) == len(boxes):
        """checking is numbe of keys equals number of boxes """
        return True
    return False
