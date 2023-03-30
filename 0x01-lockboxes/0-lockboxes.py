#!/usr/bin/python3
"""Check if boxes can be opened or not"""
def canUnlockAll(boxes):
    """determines if all the boxes can be opened or not
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    """
    n = len(boxes)
    visited = set()
    stacked = [0]
    while stacked:
        box = stacked.pop()
        if box not in visited:
            visited.add(box)
            keys = boxes[box]
            for key in keys:
                if key < n:
                  stacked.append(key)
    return len(visited) == n