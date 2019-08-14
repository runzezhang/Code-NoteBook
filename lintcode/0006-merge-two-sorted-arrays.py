# Description
# 中文
# English
# Merge two given sorted ascending integer array A and B into a new sorted integer array.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input:  A=[1], B=[1]
# Output: [1,1]	
# Explanation:  return array merged.
# Example 2:

# Input:  A=[1,2,3,4], B=[2,4,5,6]
# Output: [1,2,2,3,4,4,5,6]	
# Explanation: return array merged.
# Challenge
# How can you optimize your algorithm if one array is very large and the other is very small?

class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        if not A and not B:
            return []
        if not A and B:
            return B
        if not B and A:
            return A
        
        pointer_A = 0
        pointer_B = 0
        result = []
        
        while pointer_A < len(A) and pointer_B < len(B):
            if A[pointer_A] <= B[pointer_B]:
                result.append(A[pointer_A])
                pointer_A += 1
            else:
                result.append(B[pointer_B])
                pointer_B += 1
        while pointer_A < len(A):
            result.append(A[pointer_A])
            pointer_A += 1
        while pointer_B < len(B):
            result.append(B[pointer_B])
            pointer_B += 1
        
        return result