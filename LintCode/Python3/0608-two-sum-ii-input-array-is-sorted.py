# Description
# 中文
# English
# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

# You may assume that each input would have exactly one solution.

# Have you met this question in a real interview?
# Example
# Example 1:

# Input: nums = [2, 7, 11, 15], target = 9
# Output: [1, 2]
# Example 2:

# Input: nums = [2,3], target = 5
# Output: [1, 2]


class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, nums, target):
        # write your code here
        if nums is None or len(nums) == 0:
            return -1
        if target is None:
            return -1
        start = 0
        end = len(nums) - 1
        while start < end:
            if nums[start] + nums[end] == target:
                return [start + 1, end + 1]
            elif nums[start] + nums[end] < target:
                start += 1
            else:
                end -= 1
        return -1
