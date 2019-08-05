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

# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution(object):
    '''
    题意：判断数字是否为回文数
    翻转数字比较相等即可
    注意负数不是回文数    
    '''
    def isPalindrome(self, x):
        if x < 0 :
            return False
        tmp = x
        rev = 0
        while tmp :
            rev = rev * 10 + tmp % 10
            tmp /= 10
        return rev == x