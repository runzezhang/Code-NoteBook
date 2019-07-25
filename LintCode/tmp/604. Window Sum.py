# Description
# 中文
# English
# Given an array of n integers, and a moving window(size k), move the window at each iteration from the start of the array, find the sum of the element inside the window at each moving.

# Have you met this question in a real interview?  
# Example
# Example 1

# Input：array = [1,2,7,8,5], k = 3
# Output：[10,17,20]
# Explanation：
# 1 + 2 + 7 = 10
# 2 + 7 + 8 = 17
# 7 + 8 + 5 = 20

class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        if nums is None or len(nums) == 0:
            return []
        if k == 0:
            return []
        if len(nums) - k < 0:
            return -1
        sum = 0 
        for i in range(k):
            sum += nums[i]
        result = []
        result.append(sum)
        for i in range(1, len(nums) - k + 1):
            sum = sum - nums[i-1] + nums[k+i-1]
            result.append(sum)
        return result