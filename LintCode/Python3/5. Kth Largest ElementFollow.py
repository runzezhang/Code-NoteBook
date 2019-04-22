# Description
# 中文
# English
# Find K-th largest element in an array.

# You can swap elements in the array

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input:
# n = 1, nums = [1,3,4,2]
# Output:
# 4
# Example 2:

# Input:
# n = 3, nums = [9,3,2,4,8]
# Output:
# 4
# Challenge
# O(n) time, O(1) extra memory.

class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        if nums is None:
            return 0
        return self.quick_sort(nums, 0, len(nums) - 1, n)
        
    def quick_sort(self, nums, start, end, n):
        if start == end:
            return nums[start]
        
        left, right = start, end
        pivot = nums[start+ (end - start) // 2]
        
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1 
            while left <= right and nums[right] < pivot:
                right -= 1 
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right -= 1

        if start + n - 1 <= right:
            return self.quick_sort(nums, start, right, n)
        if start + n - 1 >= left:
            return self.quick_sort(nums, left, end, n - (left - start))
        return nums[right + 1]