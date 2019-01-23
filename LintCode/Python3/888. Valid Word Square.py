# Description
# Given a sequence of words, check whether it forms a valid word square.

# A sequence of words forms a valid word square if the k^th row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

# Example
# Example1

# Input:  
# [
#   "abcd",
#   "bnrt",
#   "crmy",
#   "dtye"
# ]
# Output: true
# Explanation:
# The first row and first column both read "abcd".
# The second row and second column both read "bnrt".
# The third row and third column both read "crmy".
# The fourth row and fourth column both read "dtye".

# Therefore, it is a valid word square.

class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """
    def validWordSquare(self, words):
        if words is None or len(words) == 0:
            return True
        for i in range(len(words)):
            for j in range(len(words[i])):
                if j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
        return True