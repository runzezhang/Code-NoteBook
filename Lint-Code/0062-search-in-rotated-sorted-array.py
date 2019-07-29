# Description
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input: [4, 5, 1, 2, 3] and target=1, 
# Output: 2.
# Example 2:

# Input: [4, 5, 1, 2, 3] and target=0, 
# Output: -1.
# Challenge
# O(logN) time

# 此题难点在于如何判断目标值在二分点的左边还是右边，重点在于先确立一个判断条件判断二分点在拐点上半区还是下半区，再在对应区间判断目标点在二分点左边还是右边
class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if A is None or len(A) == 0:
            return -1
        if target is None:
            return -1
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] == target:
                return mid
            if A[mid] >= A[0]:
                if target >= A[0] and target < A[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if target < A[0] and target >= A[mid]:
                    start = mid
                else:
                    end = mid
        if A[start] == target:
            return start 
        if A[end] == target:
            return end 
        return -1
