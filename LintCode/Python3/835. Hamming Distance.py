# Description
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

# Example
# Input: x = 1, y = 4

# Output: 2

class Solution:
    """
    @param x: an integer
    @param y: an integer
    @return: return an integer, denote the Hamming Distance between two integers
    """
    def hammingDistance(self, x, y):
        # write your code here
        count = 0
        while x or y:
            if x&1 != y&1:
                count = count + 1 
            x = x >> 1 
            y = y >> 1 
            
        return count