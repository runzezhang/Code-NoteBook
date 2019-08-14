# Description
# 中文
# English
# A robot is located at the top-left corner of a m x n grid.

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.

# How many possible unique paths are there?

# m and n will be at most 100.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input: n = 1, m = 3
# Output: 1	
# Explanation: Only one path to target position.
# Example 2:

# Input:  n = 3, m = 3
# Output: 6	
# Explanation:
# 	D : Down
# 	R : Right
# 	1) DDRR
# 	2) DRDR
# 	3) DRRD
# 	4) RRDD
# 	5) RDRD
# 	6) RDDR

class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        # æ­¤å¤æä»¬çæ°ç»éè¦è®°å½çæ¯æ¯ä¸ªä½ç½®çå¯è½èµ°æ³ï¼æä»¥ç¨å­å¸æ¥è¯¢åªéè¦Oï¼1ï¼ï¼å¹¶ä¸ä¸éè¦æå¿æ°ç»çæµæ·è´ç­äºç»´æ°ç»é®é¢
        result = {}
        for i in range(m):
            for j in range(n):
                # if the point is in corner side, casue it only allow down/right, so they would only have one choice, they need to define as 1 straightly so that we can avoid corner overflow problem.
                if i == 0 or j == 0:
                     result[(i, j)] = 1
                     continue
                result[(i, j)] = result[(i - 1, j)] + result[(i, j - 1)]
        return result[(m - 1, n - 1)]