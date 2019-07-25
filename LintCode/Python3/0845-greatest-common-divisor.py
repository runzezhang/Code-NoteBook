# Description
# Given two numbers, number a and number b. Find the greatest common divisor of the given two numbers.
# Example
# Given a = 10, b = 15, return 5.
# Given a = 15, b = 30, return 15.

class Solution:
    """
    @param a: the given number
    @param b: another number
    @return: the greatest common divisor of two numbers
    """
    def gcd(self, a, b):
        # write your code here
        a, b = (a, b) if a >=b else (b, a)
        while b:
            a, b = b, a % b 
        return a

# #ç­ä»·äºï¼
# def gcd(a,b):  
#     a, b = (a, b) if a >=b else (b, a)
#     if a%b == 0:  
#         return b  
#     else :  
#         return gcd(b,a%b)