# Description
# Given a set of candidtate numbers candidates and a target number target. Find all unique combinations in candidates where the numbers sums to target.

# The same repeated number may be chosen from candidates unlimited number of times.

# All numbers (including target) will be positive integers.
# Numbers in a combination a1, a2, … , ak must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak)
# Different combinations can be in any order.
# The solution set must not contain duplicate combinations.
# Have you met this question in a real interview?
# Example
# Example 1:

# Input: candidates = [2, 3, 6, 7], target = 7
# Output: [[7], [2, 2, 3]]
# Example 2:

# Input: candidates = [1], target = 3
# Output: [[1, 1, 1]]


class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """

    def combinationSum(self, candidates, target):
        # write your code here
        if not target or not candidates:
            return []
        result = []
        current_sum = 0
        candidates = sorted(candidates)
        combine = []
        self.dfs(candidates, 0, result, current_sum, target, combine)
        return result

    def dfs(self, candidates, index, result, current_sum, target, combine):
        if current_sum == target:
            if combine not in result:
                result.append(list(combine))
            return
        elif current_sum > target:
            return

        for i in range(index, len(candidates)):
            combine.append(candidates[i])
            self.dfs(candidates, i, result, current_sum +
                     candidates[i], target, combine)
            combine.pop()
