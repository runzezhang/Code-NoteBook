# Description
# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

# This is case sensitive, for example "Aa" is not considered a palindrome here.

# Example
# Example 1:

# Input : s = "abccccdd"
# Output : 7
# Explanation :
# One longest palindrome that can be built is "dccaccd", whose length is `7`.


class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """

    def longestPalindrome(self, s):
        # write your code here
        if s is None or len(s) == 0:
            return 0
        setS = {a: s.count(a) for a in set(s)}
        hasOdd = False
        palindromeLen = 0
        for i in setS.values():
            if i % 2 != 0 and hasOdd is not True:
                hasOdd = True
            palindromeLen = palindromeLen + i/2*2
        if hasOdd:
            palindromeLen = palindromeLen + 1
        return palindromeLen
