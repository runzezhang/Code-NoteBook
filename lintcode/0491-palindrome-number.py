# Description
# 中文
# English
# Check a positive number is a palindrome or not.

# A palindrome number is that if you reverse the whole number you will get exactly the same number.

# It's guaranteed the input number is a 32-bit integer, but after reversion, the number may exceed the 32-bit integer.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input:11
# Output:true

# Example 2:

# Input:1232
# Output:false
# Explanation:
# 1232!=2321

class Solution:
    """
    @param num: a positive number
    @return: true if it's a palindrome or false
    """
    def isPalindrome(self, num):
        # write your code here
        if num is None:
            return -1
        num = str(num)
        if num[ : : -1] == num:
            return True 
        else:
            return False