# Description
# 中文
# English
# Given a sorted array, remove the duplicates in place such that each element appear at most twice and return the new length.
# If a number appears more than two times, then keep the number appears twice in array after remove.

# Need to operate in the original array

# Have you met this question in a real interview?  
# Example
# Example 1:
# 	Input: []
# 	Output: 0


# Example 2:
# 	Input:  [1,1,1,2,2,3]
# 	Output: 5
	
# 	Explanation: 
# 	the length is 5: [1,1,2,2,3]

class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        if len(nums) < 3:
            return len(nums)
        count = 1
        for index in range(2,len(nums)):
            if nums[index] == nums[count - 1] and nums[index] == nums[count]:
                continue
            count += 1 
            nums[count] = nums[index]
        return count + 1