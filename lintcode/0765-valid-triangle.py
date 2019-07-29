# Description
# Given three integers a, b, c, return true if they can form a triangle.
# Example
# Given a = 2, b = 3, c = 4
# return true
# Given a = 1, b = 2, c = 3
# return false

class Solution:
    """
    @param a: a integer represent the length of one edge
    @param b: a integer represent the length of one edge
    @param c: a integer represent the length of one edge
    @return: whether three edges can form a triangle
    """
    def isValidTriangle(self, a, b, c):
        # write your code here
        x = [a, b, c]
        
        x.sort()
        # return x
        
        if (x[0] + x[1]) > x[2]:
            return True
        return False