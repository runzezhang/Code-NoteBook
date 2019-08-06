Description
中文
English
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

the string does not contain any non-printable characters.

Have you met this question in a real interview?  
Example
Example:

Input: "Hello, my name is John"
Output: 5
Explanation：There are five string "Hello"、"my"、"name"、"is"、"John"

class Solution:
    """
    @param s: a string
    @return: the number of segments in a string
    """
    def countSegments(self, s):
        # write yout code here
        return len(s.split())

# 本参考程序来自九章算法，由 @九章算法助教团队 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param s: a string
    @return: the number of segments in a string
    """
    def countSegments(self, s):
        # write yout code here
        res = 0
        for i in range(len(s)):
            if s[i] != ' ' and (i == 0 or s[i - 1] == ' '):
                res += 1 
        return res