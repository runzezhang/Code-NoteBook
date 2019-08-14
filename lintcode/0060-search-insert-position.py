# Description
# 中文
# English
# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume NO duplicates in the array.

# Have you met this question in a real interview?  
# Example
# [1,3,5,6], 5 → 2

# [1,3,5,6], 2 → 1

# [1,3,5,6], 7 → 4

# [1,3,5,6], 0 → 0

# Challenge
# O(log(n)) time

class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if A == []:
            return 0
        for index in range(len(A)):
            if target <= A[index]:
                return index
        return len(A)