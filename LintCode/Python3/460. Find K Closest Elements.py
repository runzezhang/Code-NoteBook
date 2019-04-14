# Description
# Given target, a non-negative integer k and an integer array A sorted in ascending order, find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. Otherwise, sorted in ascending order by number if the difference is same.

# The value k is a non-negative integer and will always be smaller than the length of the sorted array.
# Length of the given array is positive and will not exceed 10^410
# ​4
# ​​ 
# Absolute value of elements in the array will not exceed 10^410
# ​4
# ​​ 
# Have you met this question in a real interview?  
# Example
# Example 1:

# Input: A = [1, 2, 3], target = 2, k = 3
# Output: [2, 1, 3]
# Example 2:

# Input: A = [1, 4, 6, 8], target = 3, k = 3
# Output: [4, 1, 6]
# Challenge
# O(logn + k) time

class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        if target is None:
            return -1
        if k is None:
            return -1
        if A is None or len(A) == 0 :
            return []
        if k == 0 :
            return []
        right = self.find_upper_target(A, target)
        left = right - 1
        result = []
        for _ in range(k):
            if self.is_left_closer(A, target, left, right):
                result.append(A[left])
                left = left - 1
            else:
                result.append(A[right])
                right = right + 1
        
        return result
        
        
    def find_upper_target(self, A, target):
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] < target:
                start = mid
            if A[mid] >= target:
                end = mid
        if A[start] >= target:
            return start
        if A[end] >= target:
            return end
        return end + 1 
    
    
    def is_left_closer(self, A, target, left, right):
        if left < 0:
            return False
        if right >= len(A):
            return True
        return target - A[left] <= A[right] - target
        


# 本参考程序来自九章算法，由 @令狐冲 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # 找到 A[left] < target, A[right] >= target
        # 也就是最接近 target 的两个数，他们肯定是相邻的
        right = self.find_upper_closest(A, target)
        left = right - 1
    
        # 两根指针从中间往两边扩展，依次找到最接近的 k 个数
        results = []
        for _ in range(k):
            if self.is_left_closer(A, target, left, right):
                results.append(A[left])
                left -= 1
            else:
                results.append(A[right])
                right += 1
        
        return results
    
    def find_upper_closest(self, A, target):
        # find the first number >= target in A
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid
        
        if A[start] >= target:
            return start
        
        if A[end] >= target:            
            return end
        
        # 找不到的情况
        return end + 1
        
    def is_left_closer(self, A, target, left, right):
        if left < 0:
            return False
        if right >= len(A):
            return True
        return target - A[left] <= A[right] - target