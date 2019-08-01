# Description
# 中文
# English
# Given an input string, reverse the string word by word.

# Have you met this question in a real interview?
# Clarification
# What constitutes a word?
# A sequence of non-space characters constitutes a word and some words have punctuation at the end.
# Could the input string contain leading or trailing spaces?
# Yes. However, your reversed string should not contain leading or trailing spaces.
# How about multiple spaces between two words?
# Reduce them to a single space in the reversed string.
# Example
# Example 1:
# 	Input:  "the sky is blue"
# 	Output:  "blue is sky the"

# 	Explanation:
# 	return a reverse the string word by word.

# Example 2:
# 	Input:  "hello world"
# 	Output:  "world hello"

# 	Explanation:
# 	return a reverse the string word by word.


class Solution:
    """
    @param: s: A string
    @return: A string
    """

    def reverseWords(self, s):
        # write your code here
        list_s = s.split()
        list_s.reverse()
        result = ' '.join(list_s)
        return result

# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        # strip()去掉s头尾的空格，split()按照空格分割字符串，reversed翻转，''.join按照空格连接字符串
        return ' '.join(reversed(s.strip().split()))
