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
    if not boxes:
        return False

    # Start with the first box unlocked
    unlocked_boxes = [0]
    boxes_to_check = [box for box in boxes if box]

    while boxes_to_check:
        current_box = boxes_to_check.pop(0)
        current_keys = current_box
        for key in current_keys:
            if key < len(boxes) and key not in unlocked_boxes:
                unlocked_boxes.append(key)
                boxes_to_check.append(boxes[key])

    return len(unlocked_boxes) == len(boxes)

if __name__ == "__main__:
    canUnlockAll(boxes)