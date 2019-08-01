# Description
# 中文
# English
# For a given source string and a target string, you should output the first index(from 0) of target string in source string.

# If target does not exist in source, just return -1.

# Have you met this question in a real interview?
# Clarification
# Do I need to implement KMP Algorithm in a real interview?

# Not necessary. When you meet this problem in a real interview, the interviewer may just want to test your basic implementation ability. But make sure you confirm with the interviewer first.
# Example
# Example 1:
# 	Input: source = "source" ，target = "target"
# 	Output: -1

# 	Explanation:
# 	If the source does not contain the target content, return - 1.

# Example 2:
# 	Input:source = "abcdabcdefg" ，target = "bcd"
# 	Output: 1

# 	Explanation:
# 	If the source contains the target content, return the location where the target first appeared in the source.

# Challenge
# O(n2) is acceptable. Can you implement an O(n) algorithm? (hint: KMP)


class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """

    def strStr(self, source, target):
        # Write your code here
        if source is None:
            return -1
        if target is None:
            return -1
        return source.find(target)

# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    def strStr(self, source, target):
        if source is None or target is None:
            return -1
        len_s = len(source)
        len_t = len(target)
        for i in range(len_s - len_t + 1):
            j = 0
            while (j < len_t):
                if source[i + j] != target[j]:
                    break
                j += 1
            if j == len_t:
                return i
        return -1
