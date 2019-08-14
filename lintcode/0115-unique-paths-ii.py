# Description
# 中文
# English
# Follow up for "Unique Paths":

# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

# m and n will be at most 100.

# Have you met this question in a real interview?  
# Example
# Example 1:
# 	Input: [[0]]
# 	Output: 1


# Example 2:
# 	Input:  [[0,0,0],[0,1,0],[0,0,0]]
# 	Output: 2
	
# 	Explanation:
# 	Only 2 different path.

class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # if grid is empty return 0
        if not obstacleGrid or obstacleGrid == []:
            return 0
        # write your code here
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        count = {}
        # 1. init all sides to be 0
        # 2. then turn it to be 1 if can pass
        # 3. when hit break, stop and leave all point rest in this side as 0 case they can't be pass
        
        for i in range(m):
            count[(i, 0)] = 0
            
        for i in range(m):
            if obstacleGrid[i][0] != 1:
                count[(i, 0)] = 1
            else:
                break
            
        for j in range(n):
            count[(0, j)] = 0
            
        for j in range(n):
            if obstacleGrid[0][j] != 1:
                count[(0, j)] = 1
            else:
                break
        
        
        for x in range(m):
            for y in range(n):
                if x == 0 or y == 0:
                    continue
                if obstacleGrid[x][y] == 1:
                    count[(x, y)] = 0
                else:
                    count[(x, y)] = count[(x - 1, y)] + count[(x, y - 1)]
        return count[(m - 1, n - 1)]