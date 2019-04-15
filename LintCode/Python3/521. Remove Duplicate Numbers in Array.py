# Description
# 中文
# English
# Given an array of integers, remove the duplicate numbers in it.

# You should:

# Do it in place in the array.
# Move the unique numbers to the front of the array.
# Return the total number of the unique numbers.
# You don't need to keep the original order of the integers.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input:
# nums = [1,3,1,4,4,2]
# Output:
# [1,3,4,2,?,?]
# 4
# Explanation:

# Move duplicate integers to the tail of nums => nums = [1,3,4,2,?,?].
# Return the number of unique integers in nums => 4.
# Actually we don't care about what you place in ?, we only care about the part which has no duplicate integers.
# Example 2:

# Input:
# nums = [1,2,3]
# Output:
# [1,2,3]
# 3
# Challenge
# Do it in O(n) time complexity.
# Do it in O(nlogn) time without extra space.

class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0
        loop_pointer = 1
        unique_pointer = 0
        nums.sort()
        while loop_pointer < len(nums):
            if nums[loop_pointer] != nums[unique_pointer]:
                nums[unique_pointer+1] = nums[loop_pointer]
                unique_pointer += 1 
            loop_pointer += 1 
        print(nums)
        result = unique_pointer+1
        return result









# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


# O(n) time, O(n) space
class Solution:
    # @param {int[]} nums an array of integers
    # @return {int} the number of unique integers
    def deduplication(self, nums):
        # Write your code here
        d, result = {}, 0
        for num in nums:
            if num not in d:
                d[num] = True
                nums[result] = num
                result += 1

        return result

# O(nlogn) time, O(1) extra space
class Solution:
    # @param {int[]} nums an array of integers
    # @return {int} the number of unique integers
    def deduplication(self, nums):
        # Write your code here
        n = len(nums)
        if n == 0:
            return 0
            
        nums.sort()
        result = 1
        for i in xrange(1, n):
            if nums[i - 1] != nums[i]:
                nums[result] = nums[i]
                result += 1
                
        return result