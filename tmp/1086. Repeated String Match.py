# Description
# Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

# Example
# with A = "abcd" and B = "cdabcdab".

# Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

class Solution:
    """
    @param A: a string
    @param B: a string
    @return: return an integer
    """
    def repeatedStringMatch(self, A, B):
        # write your code here
        times = len(A) + len(B)
        for n in range(1,times):
            # print(A*n)
            if B in (A*n):
                return n
        return -1