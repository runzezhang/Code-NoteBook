# Description
# We are to write the letters of a given string S, from left to right into lines. Each line has maximum width 100 units, and if writing a letter would cause the width of the line to exceed 100 units, it is written on the next line. We are given an array widths, an array where widths[0] is the width of 'a', widths[1] is the width of 'b', ..., and widths[25] is the width of 'z'.

# Now answer two questions: how many lines have at least one character from S, and what is the width used by the last such line? Return your answer as an integer list of length 2.
# The length of S will be in the range [1, 1000].
# S will only contain lowercase letters.
# widths is an array of length 26.
# widths[i] will be in the range of [2, 10].
# Example1 :

# Input: 
# widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
# S = "abcdefghijklmnopqrstuvwxyz"
# Output: [3, 60]
# Explanation: 
# All letters have the same length of 10. To write all 26 letters,
# we need two full lines and one line with 60 units.

class Solution:
    """
    @param widths: an array
    @param S: a string
    @return: how many lines have at least one character from S, and what is the width used by the last such line
    """
    def numberOfLines(self, widths, S):
        # Write your code here
        line = 0
        width = 100
        for s in S:
            w = widths[ord(s)-ord('a')]
            if width + w <= 100:
                width = width + w 
            else:
                width = w 
                line += 1 
        return [line, width]