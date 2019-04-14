# Description
# Calculate the an % b where a, b and n are all 32bit positive integers.

# Have you met this question in a real interview?  
# Example
# For 231 % 3 = 2

# For 1001000 % 1000 = 0

# Challenge
# O(logn)

# Related Problems

class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        # return (a**n) % b
        ans = 1 
        while n > 0:
            if n % 2 == 1:
                ans = ans * a % b 
            a = a * a % b 
            n = n // 2 
        return ans % b


# 本参考程序来自九章算法，由 @令狐冲 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        if n == 0:
            return 1 % b
            
        if n == 1:
            return a % b
            
        # a^n = (a^n/2) ^ 2
        power = self.fastPower(a, b, n // 2)
        power = (power * power) % b
        
        # 如果 n 是奇数，还需要多乘以一个 a，因为 n // 2 是整除
        if n % 2 == 1:
            power = (power * a) % b
            
        return power
# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # a ^ n % b
        # 比如 n=5,可以看做 a^(101)2 % b （5的二进制是101）
        # 拆开也就是 [a^(100)2 * a&(1)2] % b
        # 因此相当于我们把 n 做二进制转换，碰到 1 的时候，称一下对应的 a 的幂次
        # 而 a 的幂次我们只需要知道 a^1, a^(10)2, a^(100)2 ... 也就是 a^1, a^2, a^4 ...
        # 因此不断的把 a = a * a 就可以了
        # 中间计算的时候，随时可以 % b 避免 overflow 其不影响结果，这是 % 运算的特性。
        ans = 1
        while n > 0:
            if n % 2 == 1:
                ans = (ans * a) % b
            a = a * a % b
            n = n // 2
        return ans % b