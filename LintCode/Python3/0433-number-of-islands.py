# Description
# 中文
# English
# Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

# Find the number of islands.

# Have you met this question in a real interview?
# Example
# Example 1:

# Input:
# [
#   [1,1,0,0,0],
#   [0,1,0,0,1],
#   [0,0,0,1,1],
#   [0,0,0,0,0],
#   [0,0,0,0,1]
# ]
# Output:
# 3
# Example 2:

# Input:
# [
#   [1,1]
# ]
# Output:
# 1

# [[1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,1],[0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0],[1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,0,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1],[0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1],[1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1],[1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,0,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]


class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        # write your code here
        if grid is None:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    self.bfs(grid, i, j)
                    count += 1
        return count

    def bfs(self, grid, i, j):
        queue = collections.deque([(i, j)])
        while queue:
            current_x, current_y = queue.popleft()
            check_list = [(current_x - 1, current_y), (current_x + 1, current_y),
                          (current_x, current_y - 1), (current_x, current_y + 1)]
            for neighbor in check_list:
                if self.check_valid(neighbor[0], neighbor[1], grid):
                    queue.append((neighbor[0], neighbor[1]))
            grid[current_x][current_y] = 0
            print(queue)

    def check_valid(self, x, y, grid):
        if x >= len(grid) or x < 0:
            return False
        elif y >= len(grid[0]) or y < 0:
            return False
        elif not grid[x][y]:
            return False
        return True



# 上一个方法会在测试数据的大列表中溢出，是因为我每次都仅仅把POP出来的数据改为0，这种情况没有充分直接使用已经检查出来的1点，应当在找到任何一个“1”点的时候，在存入队列后，立即将该点重制为0，防止重复判断
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if grid is None or len(grid) == 0:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    self.bfs(grid, i, j)
                    count += 1 
        return count
    
    def bfs(self, grid, i, j):
        queue = collections.deque([(i, j)])
        grid[i][j] = 0
        while queue:
            current_x, current_y = queue.popleft()
            # print(current_x, current_y)
            check_list = [(current_x - 1, current_y), (current_x + 1, current_y), (current_x, current_y - 1), (current_x, current_y + 1)]
            for neighbor in check_list:
                if self.check_valid(neighbor[0], neighbor[1], grid):
                    queue.append((neighbor[0],neighbor[1]))
                    grid[neighbor[0]][neighbor[1]] = 0
            # print(queue)
    
    def check_valid(self, x, y, grid):
        if x >= len(grid) or x < 0:
            return False
        elif y >= len(grid[0]) or y < 0:
            return False
        elif not grid[x][y]:
            return False
        return True
    
    # def bfs(self, grid, x, y):
    #     queue = collections.deque([(x, y)])
    #     grid[x][y] = False
    #     while queue:
    #         x, y = queue.popleft()
    #         for delta_x, delta_y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
    #             next_x = x + delta_x
    #             next_y = y + delta_y
    #             if not self.is_valid(grid, next_x, next_y):
    #                 continue
    #             queue.append((next_x, next_y))
    #             grid[next_x][next_y] = False
                
    # def is_valid(self, grid, x, y):
    #     n, m = len(grid), len(grid[0])
    #     return 0 <= x < n and 0 <= y < m and grid[x][y]
                    
                    