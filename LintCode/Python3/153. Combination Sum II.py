# Description
# Given an array num and a number target. Find all unique combinations in num where the numbers sum to target.

# Each number in num can only be used once in one combination.
# All numbers (including target) will be positive integers.
# Numbers in a combination a1, a2, … , ak must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak)
# Different combinations can be in any order.
# The solution set must not contain duplicate combinations.
# Have you met this question in a real interview?
# Example
# Example 1:

# Input: num = [7,1,2,5,1,6,10], target = 8
# Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
# Example 2:

# Input: num = [1,1,1], target = 2
# Output: [[1,1]]
# Explanation: The solution set must not contain duplicate combinations.


class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """

    def combinationSum2(self, num, target):
        # write your code here
        # write your code here
        if not target or not num:
            return []
        result = []
        current_sum = 0
        num = sorted(num)
        combine = []
        self.dfs(num, 0, result, current_sum, target, combine)
        return result

    def dfs(self, num, index, result, current_sum, target, combine):
        if current_sum == target:
            if combine not in result:
                result.append(list(combine))
            return
        elif current_sum > target:
            return

        for i in range(index, len(num)):
            combine.append(num[i])
            self.dfs(num, i + 1, result, current_sum +
                     num[i], target, combine)
            combine.pop()
