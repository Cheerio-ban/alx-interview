#!/usr/bin/python3
"""Unlock boxes"""


def canUnlockAll(boxes):
    """Function to open locked boxes"""
    keys = [0]
    key_clone = keys[:]
    for i, box in enumerate(boxes, start=0):
        if i in keys:
            key_clone.extend(box)
        else:
            j = len(boxes) - 1
            while (j > 0):
                if j == i:
                    return False
                if j != i:
                    if j in keys:
                        if i in boxes[j]:
                            key_clone.extend(boxes[i])
                            break
                j -= 1
        keys = key_clone
    return True
