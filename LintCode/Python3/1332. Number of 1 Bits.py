# Description
# Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).
# Example
# For example, the 32-bit integer 11 has binary representation 00000000000000000000000000001011, so the function should return 3.

class Solution:
    """
    @param n: an unsigned integer
    @return: the number of Ã¢ÂÂ1' bits
    """
    def hammingWeight(self, n):
        # write your code here
        count = 0
        while n != 0:
            count = count + ( n & 1 )
            n >>= 1 
        return count
