# Description
# 中文
# English
# Write a method anagram(s,t) to decide if two strings are anagrams or not.

# Have you met this question in a real interview?  
# Clarification
# What is Anagram?

# Two strings are anagram if they can be the same after change the order of characters.
# Example
# Example 1:

# Input: s = "ab", t = "ab"
# Output: true
# Example 2:

# Input:  s = "abcd", t = "dcba"
# Output: true
# Example 3:

# Input:  s = "ac", t = "ab"
# Output: false
# Challenge
# O(n) time, O(1) extra space

class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """
    def anagram(self, s, t):
        # write your code here
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        
        return s == t

# 本参考程序来自九章算法，由 @九章算法助教团队 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """
    def anagram(self, s, t):
        # write your code here
        # write your code here
        set_s = [0] * 256
        set_t = [0] * 256
        for i in range(0, len(s)):
            set_s[ord(s[i])] += 1
        for i in range(0, len(t)):
            set_t[ord(t[i])] += 1
        for i in range(0, 256):
            if set_s[i] != set_t[i]:
                return False
        return True