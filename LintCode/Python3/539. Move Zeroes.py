# Description
# 中文
# English
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# Have you met this question in a real interview?
# Example
# Example 1:

# Input: nums = [0, 1, 0, 3, 12],
# Output: [1, 3, 12, 0, 0].
# Example 2:

# Input: nums = [0, 0, 0, 3, 1],
# Output: [3, 1, 0, 0, 0].
WRONG ANSWER !!
# class Solution:
#     """
#     @param nums: an integer array
#     @return: nothing
#     """
#     def moveZeroes(self, nums):
#         # write your code here
#         if nums is None:
#             return
#         slow, fast = 0, 0
#         lenth = len(nums)
#         while fast <= lenth - 1 and slow <= lenth - 1:
#             print(nums)
#             print(slow)
#             print(fast)
#             while slow < lenth and nums[slow] != 0:
#                 slow += 1
#             while fast < lenth and nums[fast] == 0:
#                 fast += 1
#             if slow < lenth and fast < lenth:
#                 nums[slow], nums[fast] = nums[fast], nums[slow]
#                 slow += 1
#                 fast += 1
#             # print(nums)
#             # print(slow)
#             # print(fast)
#         return nums


class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """

    def moveZeroes(self, nums):
        # write your code here
        if nums is None:
            return
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
        return nums
