# Description
# 中文
# English
# Write a method to replace all spaces in a string with %20. The string is given in a characters array, you can assume it has enough space for replacement and you are given the true length of the string.

# You code should also return the new length of the string after replacement.

# If you are using Java or Python，please use characters array instead of string.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input: string[] = "Mr John Smith" and length = 13
# Output: string[] = "Mr%20John%20Smith" and return 17
# Explanation:
# The string after replacement should be "Mr%20John%20Smith", you need to change the string in-place and return the new length 17.
# Example 2:

# Input: string[] = "LintCode and Jiuzhang" and length = 21
# Output: string[] = "LintCode%20and%20Jiuzhang" and return 25
# Explanation:
# The string after replacement should be "LintCode%20and%20Jiuzhang", you need to change the string in-place and return the new length 25.
# Challenge
# Do it in-place.

class Solution:
    """
    @param: string: An array of Char
    @param: length: The true length of the string
    @return: The true length of new string
    """
    def replaceBlank(self, string, length):
        # write your code here
        if not string:
            return 0
        
        add_len = 0
        for i in range(len(string)):
            if string[i] == ' ':
                string[i] = '%20'
                add_len += 2
        return len(string) + add_len

# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        if string is None:
            return length
            
        spaces = 0
        for c in string:
            if c == ' ':
                spaces += 1
        
        L = length + spaces * 2
        index = L - 1
        for i in range(length - 1, -1, -1):
            if string[i] == ' ':
                string[index] = '0'
                string[index - 1] = '2'
                string[index - 2] = '%'
                index -= 3
            else:
                string[index] = string[i]
                index -= 1
        return L