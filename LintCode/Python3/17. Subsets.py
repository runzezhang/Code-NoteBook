Description
Given a set of distinct integers, return all possible subsets.

Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Have you met this question in a real interview?
Example
Example 1:

Input: [0]
Output:
[
    [],
    [0]
]
Example 2:

Input: [1, 2, 3]
Output:
[
    [3],
    [1],
    [2],
    [1, 2, 3],
    [1, 3],
    [2, 3],
    [1, 2],
    []
]
Challenge
Can you do it in both recursively and iteratively?


class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def subsets(self, nums):
        # write your code here
        nums = sorted(nums)
        result = []
        combine = []
        self.dfs(0, nums, combine, result)
        return result

    def dfs(self, index, nums, combine, result):
        # print(combine)
        # print(result)
        # print(index)
        result.append(list(combine))
        for i in range(index, len(nums)):
            combine.append(nums[i])
            self.dfs(i + 1, nums, combine, result)
            combine.pop()

# 本参考程序来自九章算法，由 @令狐冲 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def subsets(self, nums):
        nums = sorted(nums)
        combinations = []
        self.dfs(nums, 0, [], combinations)
        return combinations

    def dfs(self, nums, index, combination, combinations):
        combinations.append(list(combination))

        for i in range(index, len(nums)):
            combination.append(nums[i])
            self.dfs(nums, i + 1, combination, combinations)
            combination.pop()

# 本参考程序来自九章算法，由 @令狐冲 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:

    def search(self, nums, S, index):
        if index == len(nums):
            self.results.append(list(S))
            return

        S.append(nums[index])
        self.search(nums, S, index + 1)
        S.pop()
        self.search(nums, S, index + 1)

    def subsets(self, nums):
        self.results = []
        self.search(sorted(nums), [], 0)
        return self.results
