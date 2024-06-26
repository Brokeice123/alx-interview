#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
  """
  Returns the perimeter of the island described in grid
  """
  rows = len(grid)
  cols = len(grid[0])
  perimeter = 0

  for r in range(rows):
      for c in range(cols):
          if grid[r][c] == 1:
              # Each land cell initially has 4 sides
              perimeter += 4
    
              # Check for adjacent land cells and subtract shared sides
              if r > 0 and grid[r - 1][c] == 1:  # Check cell above
                  perimeter -= 2
              if c > 0 and grid[r][c - 1] == 1:  # Check cell to the left
                  perimeter -= 2

  return perimeter
