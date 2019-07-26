# Description
# 中文
# English
# Given a string containing uppercase alphabets and integer digits (from 0 to 9), write a function to return the alphabets in the order followed by the sum of digits.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input : str = "AC2BEW3"
# Output : "ABCEW5"
# Explanation : 
# Alphabets in the lexicographic order, followed by the sum of integers(2 and 3).

class Solution:
    """
    @param str: a string containing uppercase alphabets and integer digits
    @return: the alphabets in the order followed by the sum of digits
    """
    def rearrange(self, str):
        # Write your code here
        if str == '':
            return ''
        chars = []
        nums = []
        for char in str:
            if char.isupper():
                chars.append(char)
            else:
                nums.append(int(char))
        chars.sort()
        result = ''.join(chars)
        print(result)
        result = result + repr(sum(nums))
        return result