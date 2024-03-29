class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        perimeter = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4
                    # if cell on top is land 
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    # if cell to the left is land 
                    if j > 0 and grid[i][j-1]:
                        perimeter -= 2 
        return perimeter