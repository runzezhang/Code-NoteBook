# Description
# Implement pow(x, n). (n is an integer.)

# You don't need to care about the precision of your answer, it's acceptable if the expected answer and your answer 's difference is smaller than 1e-3.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input: x = 9.88023, n = 3
# Output: 964.498
# Example 2:

# Input: x = 2.1, n = 3
# Output: 9.261
# Example 3:

# Input: x = 1, n = 0
# Output: 1
# Challenge
# O(logn) time

class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        # write your code here
        return x ** n


# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


#Python2 版本
class Solution:
    # @param {double} x the base number
    # @param {int} n the power number
    # @return {double} the result
    def myPow(self, x, n):   #Note:在Python3中整除需使用"//"
        if n < 0 :
            x = 1 / x  
            n = -n

        ans = 1
        tmp = x

        while n != 0:
            if n % 2 == 1:
                ans *= tmp
            tmp *= tmp
            n /= 2
        return ans