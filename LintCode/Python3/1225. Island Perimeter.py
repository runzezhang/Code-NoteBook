# Description
# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

# Example
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]

# Answer: 16

class Solution:
    """
    @param grid: a 2D array
    @return: the perimeter of the island
    """
    def islandPerimeter(self, grid):
        # Write your code here
        count = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x]:
                    if x == 0:
                        count = count + 1 
                    elif grid[y][x-1] == 0:
                        count = count + 1
                    
                    if y == 0:
                        count = count + 1
                    elif grid[y-1][x] == 0:
                        count = count + 1
                    
                    if x == len(grid[0])-1:
                        count = count + 1
                    elif grid[y][x+1] == 0:
                        count = count + 1
                    
                    if y == len(grid)-1:
                        count = count + 1
                    elif grid[y+1][x] == 0:
                        count = count + 1
        return count