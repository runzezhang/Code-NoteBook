# Description
# 中文
# English
# Given a non-negative number represented as an array of digits, plus one to the number.

# The digits are stored such that the most significant digit is at the head of the list.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input: [1,2,3]
# Output: [1,2,4]
# Example 2:

# Input: [9,9,9]
# Output: [1,0,0,0]

class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """
    def plusOne(self, digits):
        # write your code here
        digits.reverse()
        adv_value = 1
        digit = -1
        while adv_value:
            digit += 1
            if digit >= len(digits):
                digits.append(0)
            adv_value = (digits[digit] + 1) // 10
            digits[digit] = (digits[digit] + 1) % 10
        # result = digits[::-1]
        digits.reverse()
        return digits