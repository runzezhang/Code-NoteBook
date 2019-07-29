# For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.

# If the target number does not exist in the array, return -1.


class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """

    def binarySearch(self, nums, target):
        # write your code here
        if len(nums) == 0 or nums is None:
            return -1
        start = 0
        end = len(nums)-1
        while start + 1 < end:
            mid = start + (end - start)//2
            if nums[mid] == target:
                end = mid
            else:
                if nums[mid] < target:
                    start = mid
                else:
                    end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
