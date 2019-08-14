# Description
# 中文
# English
# Given an array of integers, find a contiguous subarray which has the largest sum.

# The subarray should contain at least one number.

# Have you met this question in a real interview?  
# Example
# Example1:

# Input: [−2,2,−3,4,−1,2,1,−5,3]
# Output: 6
# Explanation: the contiguous subarray [4,−1,2,1] has the largest sum = 6.
# Example2:

# Input: [1,2,3,4]
# Output: 10
# Explanation: the contiguous subarray [1,2,3,4] has the largest sum = 10.

class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        now_sum, min_sum, max_sum = 0, 0, -sys.maxsize
        for num in nums:
            now_sum += num
            max_sum = max(max_sum, now_sum - min_sum)
            min_sum = min(min_sum, now_sum)
        return max_sum