# Description
# There is an integer array which has the following features:

# The numbers in adjacent positions are different.
# A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
# We define a position P is a peak if:

# A[P] > A[P-1] && A[P] > A[P+1]

class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return -1
        start = 0
        end = len(A) - 1
        # On Answer start = 1
        # end = len(A) - 2
        # It should smaller but I think border as original is fine as well, just pay attention to the If Else function
        while start + 1 < end:
            mid = start + (end -start) // 2
            if A[mid]  < A[mid+1]:
                start = mid
            elif A[mid-1] > A[mid]:
                end = mid
            else:
                # end = mid is Ok as well ??
                start = mid
        if A[start] < A[end]:
            return end
        else:
            return start