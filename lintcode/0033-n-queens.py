# Description
# 中文
# English
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

# Example
# Example 1:

# Input:1
# Output:
#    [["Q"]]


# Example 2:

# Input:4
# Output:
# [
#   // Solution 1
#   [".Q..",
#    "...Q",
#    "Q...",
#    "..Q."
#   ],
#   // Solution 2
#   ["..Q.",
#    "Q...",
#    "...Q",
#    ".Q.."
#   ]
# ]

class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        results = []
        cols = []
        self.search(n, cols, results)
        return results
    def search(self, n, cols, results):
        row = len(cols)
        if row == n:
            results.append(self.draw_result(cols))
        for col in range(n):
            if self.is_valid(col, cols, row):
                cols.append(col)
                self.search(n, cols, results)
                cols.pop()
    def is_valid(self, col, cols, row):
        for x, y in enumerate(cols):
            if y == col:
                return False
            if x + y == col + row or x - y == row - col:
                return False
        return True
    def draw_result(self, cols):
        print(cols)
        new_result = []
        n = len(cols)
        for i in range(n):
            row = []
            for j in range(n):
                if cols[j] == i:
                    row.append('Q')
                else:
                    row.append('.')
            new_result.append(''.join(row))
        return new_result
