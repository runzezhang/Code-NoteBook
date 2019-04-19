# Description
# 中文
# English
# The count-and-say sequence is the sequence of integers beginning as follows:

# 1, 11, 21, 1211, 111221, ...

# 1 is read off as "one 1" or 11.

# 11 is read off as "two 1s" or 21.

# 21 is read off as "one 2, then one 1" or 1211.

# Given an integer n, generate the nth sequence.

# The sequence of integers will be represented as a string.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input: 1
# Output: "1"
# Example 2:

# Input: 5
# Output: "111221"

# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    # @return a string
    def count(self,s):
        t=''; count=0; curr='#'
        for i in s:
            if i!=curr:
                if curr!='#':
                    t+=str(count)+curr
                curr=i
                count=1
            else:
                count+=1
        t+=str(count)+curr
        return t
    def countAndSay(self, n):
        s='1'
        for i in range(2,n+1):
            s=self.count(s)
        return s


class Solution:
    """
    @param n: the nth
    @return: the nth sequence
    """
    def countAndSay(self, n):
        # write your code here
        if n is None or n == 0:
            return ""
        result = '1'
        tmp = ''
        loop = 1
        while loop < n:
            for i in range(len(result)):
                if i == 0:
                    num = result[0]
                    count = 1 
                elif result[i] == num:
                    count += 1 
                elif result[i] != num:
                    tmp = tmp + str(count) + str(num)
                    num = result[i]
                    count = 1
                i += 1
                if i == len(result):
                    tmp = tmp + str(count) + str(num)    
            result = tmp
            print(result)
            tmp = ''
            loop += 1 
        return result