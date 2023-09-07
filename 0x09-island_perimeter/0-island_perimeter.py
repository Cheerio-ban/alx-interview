#!/usr/bin/python3
"""ALX Interview Prep Module."""


def island_perimeter(grid):
    """Return the perimeter of an island."""
    visited = set()

    def dfs(i, j):
        if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0:
            return 1
        if grid[i][j] == 0:
            return 1
        if (i, j) in visited:
            return 0
        visited.add((i, j))
        perimeter = dfs(i + 1, j)
        perimeter += dfs(i, j + 1)
        perimeter += dfs(i, j - 1)
        perimeter += dfs(i - 1, j)
        return perimeter

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]:
                return dfs(i, j)
    return 0
