# Description
# 中文
# English
# Given a positive integer, return its corresponding column title as appear in an Excel sheet.

# 1 -> A
# 2 -> B
# 3 -> C
#  ...
# 26 -> Z
# 27 -> AA
# 28 -> AB 
# Have you met this question in a real interview?  
# Example
# Example1

# Input: 28
# Output: "AB"
# Example2

# Input: 29
# Output: "AC"

Description
中文
English
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

1 -> A
2 -> B
3 -> C
 ...
26 -> Z
27 -> AA
28 -> AB 
Have you met this question in a real interview?  
Example
Example1

Input: 28
Output: "AB"
Example2

Input: 29
Output: "AC"

class Solution:
    """
    @param n: a integer
    @return: return a string
    """
    def convertToTitle(self, n):
        # write your code here
        if n is None:
            return -1
        if n == 0:
            return ''
        else:
            return self.convertToTitle((n - 1) // 26) + chr(ord('A') + (n - 1) % 26)

/**
* 本参考程序来自九章算法，由 @九章算法助教团队 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/ 

public class Solution {
    public String convertToTitle (int n) {
        StringBuilder str = new StringBuilder();

        while (n > 0) {
            n--;
            str.append ( (char) ( (n % 26) + 'A'));
            n /= 26;
        }
        return str.reverse().toString();
    }
}


Let's see the relationship between the Excel sheet column title and the number:

A   1     AA    26+ 1     BA  2×26+ 1     ...     ZA  26×26+ 1     AAA  1×26²+1×26+ 1
B   2     AB    26+ 2     BB  2×26+ 2     ...     ZB  26×26+ 2     AAB  1×26²+1×26+ 2
.   .     ..    .....     ..  .......     ...     ..  ........     ...  .............   
.   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
.   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
Z  26     AZ    26+26     BZ  2×26+26     ...     ZZ  26×26+26     AAZ  1×26²+1×26+26
Now we can see that ABCD＝A×26³＋B×26²＋C×26¹＋D＝1×26³＋2×26²＋3×26¹＋4

But how to get the column title from the number? We can't simply use the n%26 method because:

ZZZZ＝Z×26³＋Z×26²＋Z×26¹＋Z＝26×26³＋26×26²＋26×26¹＋26

We can use (n-1)%26 instead, then we get a number range from 0 to 25.

class Solution:
    # @return a string
    def convertToTitle(self, num):
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while num > 0:
            result.append(capitals[(num-1)%26])
            num = (num-1) // 26
        result.reverse()
        return ''.join(result)