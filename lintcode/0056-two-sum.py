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

# 题目描述
# 给一个整数数组，找到两个数使得他们的和等于一个给定的数 target。
# 返回这两个数。

# 使用哈希表来解决
# Java:

public int[] twoSum(int[] numbers, int target) {
    HashSet<Integer> set = new HashSet<>();

    for (int i = 0; i < numbers.length; i++) {
        if (set.contains(target - numbers[i])) {
            int[] pair = new int[2];
            pair[0] = numbers[i];
            pair[1] = target - numbers[i];
            return pair;
        }
        set.add(numbers[i]);
    }

    return null;
}
# Python:

def twoSum(numbers, target):
    hash_set = set()
    
    for i in range(len(numbers)):
        if target-numbers[i] in hash_set:
            return (numbers[i], target-numbers[i])
        hash_set.add(numbers[i])

    return None
我们使用一个HashSet，来记录每个值是否存在。
每次查找 target - numbers[i] 是否存在，存在即说明找到了，返回两个数即可。

使用双指针算法来解决
Java:

public class Solution {
    public int[] twoSum(int[] numbers, int target) {
        Arrays.sort(numbers);

        int L = 0, R = numbers.length - 1;
        while (L < R) {
            if (numbers[L] + numbers[R] == target) {
                int[] pair = new int[2];
                pair[0] = numbers[L];
                pair[1] = numbers[R];
                return pair;
            }
            if (numbers[L] + numbers[R] < target) {
                L++;
            } else {
                R--;
            }
        }
        return null;
    }
}
# Python:

class Solution:
    def twoSum(self, numbers, target):
        numbers.sort()

        L, R = 0, len(numbers)-1
        while L < R:
            if numbers[L]+numbers[R] == target:
                return (numbers[L], numbers[R])
            if numbers[L]+numbers[R] < target:
                L += 1
            else:
                R -= 1
        return None

# 首先我们对数组进行排序。
# 用两个指针(L, R)从左右开始：
# 如果numbers[L] + numbers[R] == target, 说明找到，返回对应的数。
# 如果numbers[L] + numbers[R] < target, 此时L指针右移，只有这样才可能让和更大。
# 反之使R左移。
# L和R相遇还没有找到就说明没有解。
# 两个算法的对比
# Hash方法使用一个Hashmap结构来记录对应的数字是否出现，以及其下标。时间复杂度为O(n)O(n)。空间上需要开辟Hashmap来存储, 空间复杂度是O(n)O(n)。

# Two pointers方法，基于有序数组的特性，不断移动左右指针，减少不必要的遍历，时间复杂度为O(nlogn)O(nlogn)， 主要是排序的复杂度。但是在空间上，不需要额外空间，因此额外空间复杂度是 O(1)O(1)

# 参考资料
# Java Arrays.sort() 排序。
# lintcode Two pointers 算法题目汇总

# 在线练习
# http://www.lintcode.com/problem/two-sum/
# 参考答案