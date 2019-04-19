# Description
# 中文
# English
# Given an integer array, sort it in ascending order. Use quick sort, merge sort, heap sort or any O(nlogn) algorithm.

# Have you met this question in a real interview?  
# Example
# Example1:

# Input: [3, 2, 1, 4, 5], 
# Output: [1, 2, 3, 4, 5].
# Example2:

# Input: [2, 3, 1], 
# Output: [1, 2, 3].

class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
         # write your code here
        if A is None or len(A) == 0:
            return -1
        self.quick_sort(A, 0, len(A) - 1)
        return A 
        
    def quick_sort(self, A, start, end):
        if start >= end:
            return
        left = start
        right = end
        pivot = A[start + (end - start) // 2]
        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1 
            while left <= right and A[right] > pivot:
                right -= 1 
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1 
                right -= 1 
        self.quick_sort(A, start, right)
        self.quick_sort(A, left, end)