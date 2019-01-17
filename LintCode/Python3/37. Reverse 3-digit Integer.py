# Description
# Reverse a 3-digit integer.
# Example 1:

# Input: number = 123
# Output: 321
# Example 2:

# Input: number = 900
# Output: 9

class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        # write your code here
        rnumber = 0
        while(number != 0):
            bit = number % 10
            number = number // 10
            rnumber = rnumber*10 + bit
        return rnumber