# Description
# 中文
# English
# Given two sorted integer arrays A and B, merge B into A as one sorted array.

# You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input：[1, 2, 3] 3  [4,5]  2
# Output：[1,2,3,4,5]
# Explanation:
# After merge, A will be filled as [1, 2, 3, 4, 5]
# Example 2:

# Input：[1,2,5] 3 [3,4] 2
# Output：[1,2,3,4,5]
# Explanation:
# After merge, A will be filled as [1, 2, 3, 4, 5]

class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        A.reverse()
        B.reverse()
        pointer_A = n 
        pointer_B = 0
        index = 0
        while pointer_A < m + n and pointer_B < n:
            if A[pointer_A] < B[pointer_B]:
                A[index] = B[pointer_B]
                index += 1 
                pointer_B += 1
            else:
                A[index] = A[pointer_A]
                index += 1
                pointer_A += 1
        while pointer_A < m + n:
            A[index] = A[pointer_A]
            index += 1
            pointer_A += 1
        while pointer_B < n:
            A[index] = B[pointer_B]
            index += 1 
            pointer_B += 1
                
        A.reverse()
        return