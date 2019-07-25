# Description
# Given a list funds representing the investor's investment each time. There are three companies A, B, C, and their initial funds are a, b, and c. Investors will invest in the company with the fewest funds each time (when multiple companies have the same funds, the investor will invest in the company with the smallest id). Output the final funds of A, B, C.
# Example
# Given funds=[1,2,1,3,1,1], a=1, b=2, c=1, return [4,5,4]

# Explanation:
# In the first round of investment, the funds of A and C are the same, and A is selected. At this time, a=2, b=2, c=1
# In the second round of investment, C has the minimal funds, and invest in C, at this time a=2, b=2, c=3
# In the third round of investment, the funds of A and B are the same, and A is selected. At this time, a=3, b=2, c=3
# In the fourth round of investment, B has the minimal funds, and invest in B, at this time a=3, b=5, c=3
# In the fifth round of investment, the funds of A and C are the same, and A is selected. At this time, a=4, b=5, c=3
# In the sixth round of investment, C has the minimal funds, and invest in C, at this time a=4, b=5, c=4
# Given funds=[2,1,1,1], a=1, b=2, c=2, return [4,3,3]

# Explanation:
# In the first round of investment, A has the minimal funds, and invest in A, at this time a=3, b=2, c=2
# In the second round of investment, the funds of B and C are the same, and B is selected. At this time, a=3, b=3, c=2
# In the third round of investment, C has the minimal funds, and invest in C, at this time a=3, b=3, c=3
# In the fourth round of investment, the funds of A, B and C are the same, and A is selected. At this time, a=4, b=3, c=3

class Solution:
    """
    @param funds: The investment each time
    @param a: The initial funds of A
    @param b: The initial funds of B
    @param c: The initial funds of C
    @return: The final funds
    """
    def getAns(self, funds, a, b, c):
        # Write your code here
        list = [a, b, c]
        for f in funds:
            list[list.index(min(list))] = list[list.index(min(list))] + f 
        return list