# Description
# 中文
# English
# Given a string containing n lowercase letters, the string needs to be divided into several continuous substrings, the letter in the substring should be same, and the number of letters in the substring does not exceed k, and output the minimal substring number meeting the requirement.

# n \leq 1e5n≤1e5
# Have you met this question in a real interview?  
# Example
# Example1

# Input: s = "aabbbc", k = 2
# Output: 4
# Explanation:
# we can get "aa", "bb", "b", "c" four substring.
# Example2

# input: s = "aabbbc", k = 3
# Output: 3
# we can get "aa", "bbb", "c" three substring.

class Solution:
    """
    @param s: the string s
    @param k: the maximum length of substring
    @return: return the least number of substring
    """
    def getAns(self, s, k):
        if not s or len(s) == 0 or k == 0:
            return 1
            
        # Write your code here
        count = 1
        max_continue = 1
        for i in range(1, len(s)):
            if max_continue >= k:
                count += 1
                max_continue = 1
                continue
            if s[i] == s[i - 1]:
                max_continue += 1
            else:
                max_continue = 1
                count += 1
        return count

# 本参考程序来自九章算法，由 @九章算法助教团队 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param s: the string s
    @param k: the maximum length of substring
    @return: return the least number of substring
    """
    def getAns(self, s, k):
        # Write your code here
        n = len(s)
        ans = 1
        cnt = 1;
        for i in range (1,n):
            if (s[i] == s[i-1] and cnt < k) :
                cnt += 1
            else :
                ans += 1
                cnt = 1
        return ans;