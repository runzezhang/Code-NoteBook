# Description
# Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
# Example 1:

# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

class Solution:
    """
    @param num: an integer
    @return: the complement number
    """
    def findComplement(self, num):
        # Write your code here
        return num ^ ((1 << (len(bin(num)) - 2)) - 1)
        
        
# flipper = 1 
#         while flipper <= num:
#             num ^= flipper
#             flipper <<= 1
#         return num