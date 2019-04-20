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

# Quick Sort
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

# Merge Sort 
class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        # This tmp should have len(A) value before, it is important!
        tmp = [0] * len(A)
        self.merge_sort(A, 0, len(A) - 1, tmp)
        
    def merge_sort(self, A, start, end, tmp):
        if start >= end:
            return
        
        left, right = start, end 
        mid = start + (end - start) // 2 
        
        self.merge_sort(A, start, mid, tmp)
        self.merge_sort(A, mid + 1, end, tmp)
        self.merge(A, start, mid, end, tmp)
        
    def merge(self, A, start, mid, end, tmp):
        left = start
        right = mid + 1 
        index = start 
        
        while left <= mid and right <= end:
            if A[left] < A[right]:
                tmp[index] = A[left]
                left += 1 
                index += 1 
            else:
                tmp[index] = A[right]
                right += 1 
                index += 1
        # print(index)
        # print(left)
        # print(right)
        # print(end)
        while left <= mid:
            tmp[index] = A[left]
            left += 1 
            index += 1
        while right <= end:
            tmp[index] = A[right]
            right += 1 
            index += 1
        
        for i in range(start, end + 1):
            A[i] = tmp[i]
        # print(A)