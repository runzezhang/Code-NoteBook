# Description
# 中文
# English
# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

# 1.Note that the row index starts from 0.
# 2.In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Have you met this question in a real interview?  
# Example
# Example1

# Input: 3
# Output: [1,3,3,1]
# Example2

# Input: 4
# Output: [1,4,6,4,1]
# Challenge
# Could you optimize your algorithm to use only O(k) extra space?

class Solution:
    """
    @param rowIndex: a non-negative index
    @return: the kth index row of the Pascal's triangle
    """
    def getRow(self, rowIndex):
        # write your code here
        r = 1
        last = []
        first = [1]
        while r < rowIndex+1:
            last = []
            for i in range(r+1):
                if i == 0:
                    last.append(1)
                else:
                    if i == r:
                        last.append(1)
                    else:
                        last.append(first[i-1]+first[i])
            first = last
            
            r += 1
            print (last)
        return last