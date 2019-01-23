# Description
# Given an integer, return its base 7 string representation.
# Example
# Example 1:

# input: num = 100
# outut: 202
# Example 2:

# input: num = -7
# outut: -10

class Solution:
    """
    @param num: the given number
    @return: The base 7 string representation
    """
    def convertToBase7(self, num):
        # Write your code here
        if num == 0:
            return 0
        else:
            res = ''
            n = abs(num)
            while n:
                res = str(n%7) + res
                # print(res)
                n = n//7
        return res if num>0 else '-'+res