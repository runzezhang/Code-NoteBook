# Description
# 中文
# English
# Two strings are given and you have to modify 1st string such that all the common characters of the 2nd strings have to be removed and the uncommon characters of the 2nd string have to be concatenated with uncommon characters of the 1st string.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input : s1 = "aacdb", s2 = "gafd"
# Output : "cbgf"
# Example 2:

# Input : s1 = "abcs", s2 = "cxzca"
# Output : "bsxz"

class Solution:
    """
    @param s1: the 1st string
    @param s2: the 2nd string
    @return: uncommon characters of given strings
    """
    def concatenetedString(self, s1, s2):
        # write your code here
        set1 = set(s1)
        set2 = set(s2)
        join_set = set1 & set2
        print(join_set)
        i = 0
        while i < len(s1):
        # for i in range(0, len(s1)):
            if s1[i] in join_set:
                s1 = s1[0:i]+s1[i+1:]
                # !!!index has changed here 
                i -= 1
            i += 1
            
        for j in range(0, len(s2)):
            if s2[j] not in join_set:
                s1 += s2[j]
        return s1

# 本参考程序来自九章算法，由 @九章算法助教团队 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param s1: the 1st string
    @param s2: the 2nd string
    @return: uncommon characters of given strings
    """
    def concatenetedString(self, s1, s2):
        # write your code here
        ans = []
        for c in s1:
            if c not in s2:
                ans.append(c)
        for c in s2:
            if c not in s1:
                ans.append(c)
        return "".join(ans)