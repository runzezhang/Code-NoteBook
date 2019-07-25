# Description
# Given an array and two indexes, swap the integers on the two indices.

# Example
# Given [1,2,3,4] and index1 = 2, index2 = 3. The array will change to [1,2,4,3] after swapping. You don't need return anything, just swap the integers in-place.

class Solution:
    """
    @param A: An integer array
    @param index1: the first index
    @param index2: the second index
    @return: nothing
    """
    def swapIntegers(self, A, index1, index2):
        # write your code here
        A[index1],A[index2] = A[index2],A[index1]