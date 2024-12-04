#!/usr/bin/python3
"""
Island Perimeter task
"""


def island_perimeter(grid):
    """
    This will calculate the perimeter of a grid
    Args:
        grid: list of the 2nd integer
    Return:
        the perimeter of the island
    """

    Perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):
                if (i <= 0 or grid[i - 1][j] == 0):
                    Perimeter += 1
                if (i >= len(grid) - 1 or grid[i + 1][j] == 0):
                    Perimeter += 1
                if (j <= 0 or grid[i][j - 1] == 0):
                    Perimeter += 1
                if (j >= len(grid[i]) - 1 or grid[i][j + 1] == 0):
                    Perimeter += 1
    return Perimeter
