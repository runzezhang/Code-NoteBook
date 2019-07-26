# Description
# 中文
# English
# Implement an algorithm to determine if a string has all unique characters.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input: "abc_____"
# Output: false
# Example 2:

# Input:  "abc"
# Output: true	
# Challenge
# What if you can not use additional data structures?

class Solution:
    """
    @param: str: A string
    @return: a boolean
    """
    def isUnique(self, str):
        # write your code here
        # counts = set()
        # for char in str:
        #     if char not in counts:
        #         counts.add(char)
        #     else:
        #         return False
        # return True
        # Answer using ASCII Code arrary
        ch = range(129)
        ch = [0 for i in range(129)]
        
        for char in str:
            if ch[ord(char)]==0:
                ch[ord(char)] = 1
            else:
                return False
        return True