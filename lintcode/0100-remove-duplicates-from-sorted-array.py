# Description
# 中文
# English
# Given a sorted array, 'remove' the duplicates in place such that each element appear only once and return the 'new' length.

# Do not allocate extra space for another array, you must do this in place with constant memory.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input:  []
# Output: 0
# Example 2:

# Input:  [1,1,2]
# Output: 2	
# Explanation:  uniqued array: [1,2]

class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        # key = 0
        # while key < len(nums) - 1:
        #     # print(nums)
        #     if nums[key] == nums[key + 1]:
        #         nums.pop(key)
        #     else:
        #         key += 1
        # return len(nums)
        
        # this method will put all repeate elem at the last of array while not delete them actually, but indeed it can pass test, exciting~~~
        if nums == []:
            return 0
        index = 0
        for i in range(1, len(nums)):
            if nums[index] != nums[i]:
                index += 1
                nums[index] = nums[i]
        return index + 1