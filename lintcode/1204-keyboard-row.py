# Description
# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.

# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]

class Solution:
    """
    @param words: a list of strings
    @return: return a list of strings
    """
    def findWords(self, words):
        # write your code here
        a = set('qwertyuiop')
        b = set('asdfghjkl')
        c= set('zxcvbnm')
        answer = []
        for word in words:
            if not set(word.lower()).difference(a):
                answer.append(word)
            else:
                if not set(word.lower()).difference(b):
                    answer.append(word)
                else:
                    if not set(word.lower()).difference(c):
                        answer.append(word)
        return answer

# 本参考程序来自九章算法，由 @九章算法助教团队 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param words: a list of strings
    @return: return a list of strings
    """

    def findWords(self, words):
        # write your code here

        res = []
        s = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        for w in words:
            for j in range(3):
                flag = 1
                for i in w:
                    if i.lower() not in s[j]:
                        flag = 0
                        break
                if flag == 1:
                    res.append(w)
                    break
        return res