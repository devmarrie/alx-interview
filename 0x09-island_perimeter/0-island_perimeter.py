#!/usr/bin/python3
"""
Island perimeter
"""


def island_perimeter(grid):
    """
    Takes in square cells and uses them
    to create an island
    Returns:
           the preimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    island_count = 0
    perimeter = 0
    if rows > 100 or cols > 100:
        raise ValueError("Rows or columns exceeds the expected value")
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                # Minus 2 horizontally
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
                # Minus 2 vertically
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
    return perimeter
