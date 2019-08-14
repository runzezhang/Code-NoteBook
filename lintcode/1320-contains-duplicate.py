# Description
# 中文
# English
# Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

# Have you met this question in a real interview?  
# Example
# Example 1：

# Input：nums = [1, 1]
# Output：True
# Example 2：

# Input：nums = [1, 2, 3]
# Output：False

class Solution:
    """
    @param nums: the given array
    @return: if any value appears at least twice in the array
    """
    def containsDuplicate(self, nums):
        # Write your code here
        a = set(nums)
        if len(a) == len(nums):
            return False
        else:
            return True