# Description
# 中文
# English
# Given a rotated sorted array, recover it to sorted array in-place.

# Have you met this question in a real interview?  
# Clarification
# What is rotated array?

# For example, the orginal array is [1,2,3,4], The rotated array of it can be [1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]
# Example
# Example1:
# [4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]
# Example2:
# [6,8,9,1,2] -> [1,2,6,8,9]

# Challenge
# In-place, O(1) extra space and O(n) time.

class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return []
        x_index = 0
        for index in range(len(nums)-2):
            if nums[index] > nums[index + 1]:
                x_index = index +1
                break
        if x_index:
            self.reverse(nums, 0, (len(nums) - 1))
            self.reverse(nums, 0, (len(nums) - x_index - 1))
            self.reverse(nums, (len(nums) - x_index), (len(nums) - 1))
        
    def reverse(self, nums, s, e):
        i = s; j = e
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1