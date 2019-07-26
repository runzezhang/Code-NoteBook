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