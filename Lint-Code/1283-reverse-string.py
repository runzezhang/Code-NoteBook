# Description
# 中文
# English
# Write a function that takes a string as input and returns the string reversed.

# Have you met this question in a real interview?  
# Example
# Example 1：

# Input："hello"
# Output："olleh"
# Example 2：

# Input："hello world"
# Output："dlrow olleh"

class Solution:
    """
    @param s: a string
    @return: return a string
    """
    def reverseString(self, s):
        # write your code here
        # reverse_string = ''
        # for i in range(len(s) - 1, -1, -1):
        #     reverse_string += s[i]
        # return reverse_string
        
        return s[::-1]