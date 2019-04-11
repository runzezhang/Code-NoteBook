# Implement int sqrt(int x).

# Compute and return the square root of x.


class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """

    def sqrt(self, x):
        # write your code here
        start = 0
        end = x
        while start + 1 < end:
            mid = start + (end - start)//2
            if mid**2 == x:
                start = mid
            else:
                if mid**2 < x:
                    start = mid
                else:
                    end = mid
        if end**2 <= x:
            return end
        if start**2 <= x:
            return start
        return -1
