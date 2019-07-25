# Description
# 中文
# English
# Given a big sorted array with non-negative integers sorted by non-decreasing order. The array is so big so that you can not get the length of the whole array directly, and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++).

# Find the first index of a target number. Your algorithm should be in O(log k), where k is the first index of the target number.

# Return -1, if the number doesn't exist in the array.

# If you accessed an inaccessible index (outside of the array), ArrayReader.get will return 2,147,483,647.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input: [1, 3, 6, 9, 21, ...], target = 3
# Output: 1
# Example 2:

# Input: [1, 3, 6, 9, 21, ...], target = 4
# Output: -1
# Challenge
# O(logn) time, n is the first index of the given target number.

"""
Definition of ArrayReader
class ArrayReader(object):
    def get(self, index):
    	# return the number on given index, 
        # return 2147483647 if the index is invalid.
"""
class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        # border check
        if target is None:
            return - 1
        # Assueme start end is 0,1
        start = 0
        end = 1
        # By power 2 each time until we find a index let array(index) is greater than target, it will cost around O(log target) time.
        while reader.get(end) < target and reader.get(end) != 2147483647 :
            end = end * 2
        # Using binary research in our defined array range to find the fianl index of value target
        while start + 1 < end:
            mid = start + (end - start) // 2
            if reader.get(mid) < target:
                start = mid
            if reader.get(mid) >= target:
                end = mid
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1