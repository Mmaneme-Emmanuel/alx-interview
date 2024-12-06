#!/usr/bin/python3
""" function def island_perimeter(grid): that returns the perimeter of the island described in grid:
"""

def island_perimeter(grid):
    perimeter = 0
    
    # Dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Land cell
                # Start with 4 edges
                perimeter += 4
                
                # Check top neighbor
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Shared edge
                
                # Check left neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Shared edge
    
    return perimeter
