# Description
# 中文
# English
# Given an array of integers, find two numbers that their difference equals to a target value.
# where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are NOT zero-based.

# It's guaranteed there is only one available solution

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input: nums = [2, 7, 15, 24], target = 5 
# Output: [1, 2] 
# Explanation:
# (7 - 2 = 5)
# Example 2:

# Input: nums = [1, 1], target = 0
# Output: [1, 2] 
# Explanation:
# (1 - 1 = 0)


class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, nums, target):
        # write your code here
        if nums is None or len(nums) == 0:
            return -1
        if target is None:
            return -1
        nums = [(num, i) for i, num in enumerate(nums)]
        target = abs(target)
        nums = sorted(nums, key = lambda x: x[0])
        print(nums)
        left = 0
        right = 1 
        result = []
        while right < len(nums) or left < len(nums):
            if left == right:
                right += 1 
            if right < len(nums) and nums[right][0] - nums[left][0] > target:
                left += 1 
            elif right < len(nums) and  nums[right][0] - nums[left][0] < target:
                right += 1 
            elif nums[right][0] - nums[left][0] == target:
                result = [nums[left][1]+1, nums[right][1]+1]
                break
        if result[1] < result[0]:
            result[0], result[1] = result[1], result[0]
        return result
            