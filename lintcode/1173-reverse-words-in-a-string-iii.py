# Description
# 中文
# English
# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# In the string, each word is separated by single space and there will not be any extra space in the string.

# Have you met this question in a real interview?  
# Example
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

class Solution:
    """
    @param s: a string
    @return: reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order
    """
    def reverseWords(self, s):
        # Write your code here
        words = s.split(' ')
        result = ''
        for word in words:
            word = word[-1: :-1]
            if result == '':
                result = word
            else:
                result = result + ' ' + word
        return  result