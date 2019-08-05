# Description
# Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

# Have you met this question in a real interview?
# Example
# Example 1:

# Input:"abcdzdcab"
# Output:"cdzdc"
# Example 2:

# Input:"aba"
# Output:"aba"
# Challenge
# O(n2) time is acceptable. Can you do it in O(n) time.


class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """

    def longestPalindrome(self, s):
        # write your code here
        if s is None:
            return -1
        if len(s) == 0:
            return ''
        if len(s) > 1:
            for i in range(len(s)):
                for j in range(i+1):
                    if (i-j) == 0:
                        sCompare = s[j:]
                        if sCompare == sCompare[:: -1]:
                            return sCompare
                    else:
                        sCompare = s[j: -(i-j)]
                        if sCompare == sCompare[:: -1]:
                            return s[j: -(i-j)]
        elif len(s) == 1:
            return s

基于区间型动态规划的解法
class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        if not s:
            return ""
            
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]
        
        for i in range(n):
            is_palindrome[i][i] = True
        for i in range(1, n):
            is_palindrome[i][i - 1] = True
            
        longest, start, end = 1, 0, 0
        for length in range(1, n):
            for i in range(n - length):
                j = i + length
                is_palindrome[i][j] = s[i] == s[j] and is_palindrome[i + 1][j - 1]
                if is_palindrome[i][j] and length + 1 > longest:
                    longest = length + 1
                    start, end = i, j
                    
        return s[start:end + 1]

基于中心线枚举的方法
class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        if not s:
            return ""
            
        longest = ""
        for middle in range(len(s)):
            sub = self.find_palindrome_from(s, middle, middle)
            if len(sub) > len(longest):
                longest = sub
            sub = self.find_palindrome_from(s, middle, middle + 1)
            if len(sub) > len(longest):
                longest = sub

        return longest
        
    def find_palindrome_from(self, string, left, right):
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
            
        return string[left + 1:right]

使用 Manacher's Algorithm
可以在 O(n) 的时间内解决问题
参考资料：https://www.felix021.com/blog/read.php?2040
class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        if not s:
            return

        # Using manacher's algorithm
        # abba => #a#b#b#a#
        chars = []
        for c in s:
            chars.append('#')
            chars.append(c)
        chars.append('#')
        
        n = len(chars)
        palindrome = [0] * n
        palindrome[0] = 1
        
        mid, longest = 0, 1
        for i in range(1, n):
            length = 1
            if mid + longest > i:
                mirror = mid - (i - mid)
                length = min(palindrome[mirror], mid + longest - i)

            while i + length < len(chars) and i - length >= 0:
                if chars[i + length] != chars[i - length]:
                    break;
                length += 1
            
            if length > longest:
                longest = length
                mid = i
            
            palindrome[i] = length
        
        # remove the extra #
        longest = longest - 1
        start = (mid - 1) // 2 - (longest - 1) // 2
        return s[start:start + longest]