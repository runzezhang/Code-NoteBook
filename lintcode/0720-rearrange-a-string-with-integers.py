# Description
# 中文
# English
# Given a string containing uppercase alphabets and integer digits (from 0 to 9), write a function to return the alphabets in the order followed by the sum of digits.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input : str = "AC2BEW3"
# Output : "ABCEW5"
# Explanation : 
# Alphabets in the lexicographic order, followed by the sum of integers(2 and 3).

class Solution:
    """
    @param str: a string containing uppercase alphabets and integer digits
    @return: the alphabets in the order followed by the sum of digits
    """
    def rearrange(self, str):
        # Write your code here
        if str == '':
            return ''
        chars = []
        nums = []
        for char in str:
            if char.isupper():
                chars.append(char)
            else:
                nums.append(int(char))
        chars.sort()
        result = ''.join(chars)
        print(result)
        result = result + repr(sum(nums))
        return result

# 本参考程序来自九章算法，由 @九章算法助教团队 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param str: a string containing uppercase alphabets and integer digits
    @return: the alphabets in the order followed by the sum of digits
    """
    def rearrange(self, str):
        # Write your code here
        Str = list(str)
        Str.sort()
        res = 0
        index = -1
        for i in range(0, len(Str)):
            if Str[i] >= '0' and Str[i] <= '9':
                res += int(Str[i])
                index += 1
            else:
                break
        if index == -1:
            return ''.join(Str)
        else:
            return ''.join(Str[index + 1 : len(Str)]) + repr(res)