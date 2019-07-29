# Description
# Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.

# You are not suppose to use the library's sort function for this problem.
# k <= n
# Have you met this question in a real interview?
# Example
# Example1

# Input:
# [3,2,2,1,4]
# 4
# Output:
# [1,2,2,3,4]
# Example2

# Input:
# [2,1,1,2,2]
# 2
# Output:
# [1,1,2,2,2]
# Challenge
# A rather straight forward solution is a two-pass algorithm using counting sort. That will cost O(k) extra memory. Can you do it without using extra memory?


class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):
        # write your code here
        if colors is None or len(colors) == 0:
            return -1
        return colors.sort()


使用分治法来解决。
传入两个区间，一个是颜色区间 color_from, color_to。另外一个是待排序的数组区间 index_from, index_to.
找到颜色区间的中点，将数组范围内进行 partition，<= color 的去左边，> color 的去右边。
然后继续递归。
时间复杂度 O(nlogk)O(nlogk) n是数的个数， k 是颜色数目。这是基于比较的算法的最优时间复杂度。

不基于比较的话，可以用计数排序（Counting Sort）

# 本参考程序来自九章算法，由 @令狐冲 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):
        self.sort(colors, 1, k, 0, len(colors) - 1)

    def sort(self, colors, color_from, color_to, index_from, index_to):
        if color_from == color_to or index_from == index_to:
            return

        color = (color_from + color_to) // 2

        left, right = index_from, index_to
        while left <= right:
            while left <= right and colors[left] <= color:
                left += 1
            while left <= right and colors[right] > color:
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1

        self.sort(colors, color_from, color, index_from, right)
        self.sort(colors, color + 1, color_to, left, index_to)


1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
九章算法
更新于 1/20/2019, 12: 39: 40 AM
# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):
        # write your code here
        # for i in xrange(len(colors)):
        i = 0
        n = len(colors)
        while i < n:
            if colors[i] > 0:
                if colors[colors[i]-1] > 0:
                    tmp = colors[i]
                    colors[i] = colors[colors[i]-1]
                    colors[tmp-1] = -1
                    i = i - 1
                else:
                    colors[colors[i]-1] -= 1
                    colors[i] = 0
            i = i + 1

        i = len(colors)-1
        k = i
        while i >= 0:
            if colors[i] < 0:
                pos = k + colors[i]
                while k > pos:
                    colors[k] = i+1
                    k -= 1
            i -= 1
