# Description
# Given an integer array with even length, where different numbers in this array represent different kinds of candies. Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to brother and sister. Return the maximum number of kinds of candies the sister could gain.
# Example
# Input: candies = [1,1,2,2,3,3]
# Output: 3
# Explanation:
# There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
# Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too.
# The sister has three different kinds of candies.

# Input: candies = [1,1,2,3]
# Output: 2
# Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1].
# The sister has two different kinds of candies, the brother has only one kind of candies.

class Solution:
    """
    @param candies: a list of integers
    @return: return a integer
    """
    def distributeCandies(self, candies):
        # write your code here
        return int(min(len(candies)/2,len(set(candies))))
