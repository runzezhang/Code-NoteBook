# Given n pieces of wood with length L[i] (integer array). 
# Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length.
#  What is the longest length you can get from the n pieces of wood? 
# Given L & k, return the maximum length of the small pieces.

class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if L is None or len(L) == 0:
            return 0
        
        maxium = max(L)
        start = 1 
        end = maxium
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.count(mid,L) >= k:
                start = mid
            else:
                end = mid
        if self.count(end, L) >= k:
            return end
        if  self.count(start, L) >= k:
            return start
        return 0    
            
            
    
    def count(self, length, L):
        sum = 0
        for i in L:
            sum = sum + i // length
        return sum