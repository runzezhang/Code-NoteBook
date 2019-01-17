# Description
# Given 2*n + 1 numbers, every numbers occurs twice except one, find it.
# Example
# Given [1,2,2,1,3,4,3], return 4

class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        # write your code here
        count2 = 0
        count1 = 0
        for n in set(A):
            count2 = count2 + n 
        for x in A:
            count1 = count1 +x 
        return count2*2-count1