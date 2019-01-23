# Description
# Given a column title as appear in an Excel sheet, return its corresponding column number.

# Example
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28

class Solution:
    """
    @param s: a string
    @return: return a integer
    """
    def titleToNumber(self, s):
        return sum((ord(s[-1 - i]) - ord("@")) * (26 ** i) for i in range(len(s)))