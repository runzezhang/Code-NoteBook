# Description
# 中文
# English
# Given a digit string excluded '0' and '1', return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below.

# 1	2
# ABC	3
# DEF
# 4
# GHI	5
# JKL	6
# MNO
# 7
# PQRS	8
# TUV	9
# WXYZ
# Although the answer above is in lexicographical order, your answer could be in any order you want.

# Have you met this question in a real interview?
# Example
# Example 1:

# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
# Explanation:
# '2' could be 'a', 'b' or 'c'
# '3' could be 'd', 'e' or 'f'
# Example 2:

# Input: "5"
# Output: ["j", "k", "l"]

KEYBOARD = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}


class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """

    def letterCombinations(self, digits):
        # write your code here
        if not digits:
            return []
        result = []
        self.dfs(digits, 0, '', result)
        return result

    def dfs(self, digits, index, string, result):
        if index == len(digits):
            result.append(string)
            return
        for letter in KEYBOARD[digits[index]]:
            self.dfs(digits, index + 1, string + letter, result)
