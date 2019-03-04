# Find the last position of a target number in a sorted array. Return -1 if target does not exist.
class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def lastPosition(self, nums, target):
        # write your code here
        if nums is None or len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start)//2
            if target == nums[mid]:
                start = mid
            else:
                if target < nums[mid]:
                    end = mid
                else:
                    start = mid
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1
