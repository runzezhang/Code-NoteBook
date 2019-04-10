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
