# Description
# 中文
# English
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

# If the last word does not exist, return 0.

# A word is defined as a character sequence consists of non-space characters only.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input: "Hello World"
# Output: 5
# Example 2:

# Input: "Hello LintCode"
# Output: 8

class Solution:
    """
    @param s: A string
    @return: the length of last word
    """
    def lengthOfLastWord(self, s):
        # write your code here
        if s is None: 
            return 0
        s = s.split()
        if len(s) == 0:
            return 0
        last = s[-1]
        return len(last)