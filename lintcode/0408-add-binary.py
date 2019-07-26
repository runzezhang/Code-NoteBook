# Description
# 中文
# English
# Given two binary strings, return their sum (also a binary string).

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input:
# a = "0", b = "0"
# Output:
# "0"
# Example 2:

# Input:
# a = "11", b = "1"
# Output:
# "100"

class Solution:
    """
    @param a: a number
    @param b: a number
    @return: the result
    """
    def addBinary(self, a, b):
        # write your code here
        indexa = len(a) - 1
        indexb = len(b) - 1 
        sum = ''
        carry = 0
        while indexa >= 0 or indexb >= 0:
            if indexa >= 0:
                bitA = int(a[indexa])
            else:
                bitA = 0
            if indexb >= 0:
                bitB = int(b[indexb])
            else:
                bitB = 0
            if (bitB + bitA + carry) % 2 == 0:
                sum =  '0' + sum
            else:
                sum = '1' + sum
            carry = (bitA + bitB + carry) // 2
            indexa, indexb = indexa - 1, indexb - 1 
        # important!!! last carry must be only 1 or 0
        if carry == 1:
            sum = '1' + sum
        return sum