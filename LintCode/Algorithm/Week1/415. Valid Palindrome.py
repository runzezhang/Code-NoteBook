# Description
# 中文
# English
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Have you consider that the string might be empty? This is a good question to ask during an interview.

# For the purpose of this problem, we define empty string as valid palindrome.

# Have you met this question in a real interview?
# Example
# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama"
# Example 2:

# Input: "race a car"
# Output: false
# Explanation: "raceacar"
# Challenge
# O(n) time without extra memory.


class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """

    def isPalindrome(self, s):
        # write your code here
        if s is None:
            return False
        if len(s) == 0:
            return True
        s = s.lower()
        pureS = ''
        for i in s:
            if i.isalnum():
                pureS = pureS + str(i)
        if pureS == pureS[::-1]:
            return True
        return False
