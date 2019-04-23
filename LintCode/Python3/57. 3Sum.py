# Description
# 中文
# English
# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)

# The solution set must not contain duplicate triplets.

# Have you met this question in a real interview?
# Example
# Example 1:

# Input:[2,7,11,15]
# Output:[]
# Example 2:

# Input:[-1,0,1,2,-1,-4]
# Output:	[[-1, 0, 1],[-1, -1, 2]]


class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):
        # write your code here
        if numbers is None or len(numbers) == 0:
            return []
        numbers.sort()
        result = []
        first = 0
        while first < len(numbers):
            left = first + 1
            right = len(numbers) - 1
            while left < right:
                if numbers[left] + numbers[right] + numbers[first] < 0:
                    left += 1
                elif numbers[left] + numbers[right] + numbers[first] > 0:
                    right -= 1
                else:
                    # print(first)
                    # print(left)
                    # print(right)
                    # print('this is one')
                    if [numbers[first], numbers[left], numbers[right]] not in result:
                        result.append(
                            [numbers[first], numbers[left], numbers[right]])
                    left += 1
                    right -= 1
            first += 1

        return result
