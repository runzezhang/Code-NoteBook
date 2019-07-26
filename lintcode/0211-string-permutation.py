# Description
# 中文
# English
# Given two strings, write a method to decide if one is a permutation of the other.

# Have you met this question in a real interview?  
# Example
# Example 1:
# 	Input:  "abcd", "bcad"
# 	Output:  True


# Example 2:
# 	Input: "aac", "abc"
# 	Output:  False

class Solution:
    """
    @param A: a string
    @param B: a string
    @return: a boolean
    """
    def Permutation(self, A, B):
        # write your code here
        A = ''.join(sorted(A))
        B = ''.join(sorted(B))
        
        return A == B