# Description
# 中文
# English
# Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position, find the shortest path to a destination position, return the length of the route.
# Return -1 if destination cannot be reached.

# source and destination must be empty.
# Knight can not enter the barrier.

# Have you met this question in a real interview?
# Clarification
# If the knight is at (x, y), he can get to the following positions in one step:

# (x + 1, y + 2)
# (x + 1, y - 2)
# (x - 1, y + 2)
# (x - 1, y - 2)
# (x + 2, y + 1)
# (x + 2, y - 1)
# (x - 2, y + 1)
# (x - 2, y - 1)
# Example
# Example 1:

# Input:
# [[0,0,0],
#  [0,0,0],
#  [0,0,0]]
# source = [2, 0] destination = [2, 2]
# Output: 2
# Explanation:
# [2,0]->[0,1]->[2,2]
# Example 2:

# Input:
# [[0,1,0],
#  [0,0,1],
#  [0,0,0]]
# source = [2, 0] destination = [2, 2]
# Output:-1

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

DIRECTIONS = [
    (-2, -1), (-2, 1), (-1, 2), (1, 2),
    (2, 1), (2, -1), (1, -2), (-1, -2),
]


class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """

    def shortestPath(self, grid, source, destination):
        # write your code here
        if grid is None or len(grid) == 0:
            return -1
        if source.x < 0 or source.x >= len(grid):
            return -1
        if source.y < 0 or source.y >= len(grid[0]):
            return -1
        if destination.x < 0 or destination.x >= len(grid):
            return -1
        if destination.y < 0 or destination.y >= len(grid[0]):
            return -1
        queue = collections.deque([(source.x, source.y)])
        level = {(source.x, source.y): 0}
        while queue:
            # x, y = queue.popleft()
            # for dx, dy in DIRECTIONS:
            #     next_x, next_y = x+dx, y+dy
            #     if self.is_valid(grid, next_x, next_y):
            #       queue.append((next_x, next_y))
            #       level[(next_x, next_y)] = level[(x, y)] + 1
            #       if next_x == destination.x and next_y == destination.y:
            #         return level[(next_x, next_y)]
            # 被注释掉的代码会超时，是因为除了子节点需要在图内这一限制条件，已经标记了距离出发点距离的点也需要排除在外，另外因为只需要判断终止点距离，所以在从队列中POP出来，就可以先行进行判断，节约时间。

            x, y = queue.popleft()
            if x == destination.x and y == destination.y:
                return level[(x, y)]
            for dx, dy in DIRECTIONS:
                next_x, next_y = x+dx, y+dy
                if (next_x, next_y) not in level and self.is_valid(grid, next_x, next_y):
                    queue.append((next_x, next_y))
                    level[(next_x, next_y)] = level[(x, y)] + 1
        return -1

    def is_valid(self, grid, next_x, next_y):
        if next_x < 0 or next_x >= len(grid):
            return False
        if next_y < 0 or next_y >= len(grid[0]):
            return False
        if grid[next_x][next_y] == 1:
            return False
        return True
