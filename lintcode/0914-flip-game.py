# Description
# 中文
# English
# You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

# Write a function to compute all possible states of the string after one valid move.

# Have you met this question in a real interview?  
# Example
# Example1

# Input:  s = "++++"
# Output: 
# [
#   "--++",
#   "+--+",
#   "++--"
# ]
# Example2

# Input: s = "---+++-+++-+"
# Output: 
# [
# 	"---+++-+---+",
# 	"---+++---+-+",
# 	"---+---+++-+",
# 	"-----+-+++-+"
# ]

class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """
    def generatePossibleNextMoves(self, s):
        # write your code here
        if s is None or len(s) == 0:
            return []
        result = []
        for i in range(len(s)-1):
            if s[i] == s[i+1] and s[i] == '+':
                tmp = s[:i] + '--' + s[i+2:]
                result.append(tmp)
        return result