# Description
# 中文
# English
# Given number n. Print number from 1 to n. But:

# when number is divided by 3, print "fizz".
# when number is divided by 5, print "buzz".
# when number is divided by both 3 and 5, print "fizz buzz".
# when number can't be divided by either 3 or 5, print the number itself.
# Have you met this question in a real interview?
# Example
# If n = 15, you should return:
# [
#   "1", "2", "fizz",
#   "4", "buzz", "fizz",
#   "7", "8", "fizz",
#   "buzz", "11", "fizz",
#   "13", "14", "fizz buzz"
# ]

# If n = 10, you should return:
# [
#   "1", "2", "fizz",
#   "4", "buzz", "fizz",
#   "7", "8", "fizz",
#   "buzz"
# ]
# Challenge
# Can you do it with only one if statement?


class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """

    def fizzBuzz(self, n):
        # write your code here
        result = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append('fizz buzz')
            elif i % 3 == 0:
                result.append('fizz')
            elif i % 5 == 0:
                result.append('buzz')
            else:
                result.append(str(i))
        return result


class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """

    def fizzBuzz(self, n):
        ret = [str(i+1) for i in range(n)]
        for i in range(2, n, 3):
            ret[i] = "fizz"
        for i in range(4, n, 5):
            ret[i] = "buzz" if ret[i] != "fizz" else "fizz buzz"
        return ret

/**
* 本参考程序来自九章算法，由 @令狐冲 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/ 

class Solution {
    /**
     * param n: As description.
     * return: A list of strings.
     */
    public ArrayList<String> fizzBuzz(int n) {
        ArrayList<String> results = new ArrayList<String>();
        int i = 1;
        //p3表示3的多少倍，p5表示5的多少倍
        int p3 = 1, p5 = 1;
        
        while (i <= n) {
          while (i < p3 * 3 && i < p5 * 5) {
            results.add(i + "");
            i++;
          }
        
          if (i <= n && p3 * 3 == p5 * 5) {
            results.add("fizz buzz");
            p3++;
            p5++;
            i++;
            continue;
          }
        
          while (i <= n && p3 * 3 <= i) {
            results.add("fizz");
            p3++;
            i++;
          }
        
          while (i <= n && p5 * 5 <= i) {
            results.add("buzz");
            p5++;
            i++;
          }
        }
        
        return results;
    }
}