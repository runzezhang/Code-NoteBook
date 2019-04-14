# Description
# Given an array of integers, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are zero-based.

# You may assume that each input would have exactly one solution

# Have you met this question in a real interview?
# Example
# Example1:
# numbers=[2, 7, 11, 15], target=9
# return [0, 1]
# Example2:
# numbers=[15, 2, 7, 11], target=9
# return [1, 2]
# Challenge
# Either of the following solutions are acceptable:

# O(n) Space, O(nlogn) Time
# O(n) Space, O(n) Time


class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """

    def twoSum(self, numbers, target):
        # write your code here
        # if numbers is None or len(numbers) == 0:
        #     return [-1, -1]
        # if target is None:
        #     return [-1, -1]
        hash = {}
        # 循环nums数值，并添加映射
        for i in range(len(numbers)):
            if target - numbers[i] in hash:
                return [hash[target - numbers[i]], i]
            hash[numbers[i]] = i
        # 无解的情况
        return [-1, -1]
