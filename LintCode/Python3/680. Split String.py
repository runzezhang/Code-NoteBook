# Description
# 中文
# English
# Give a string, you can choose to split the string after one character or two adjacent characters, and make the string to be composed of only one character or two characters. Output all possible results.

# Have you met this question in a real interview?  
# Example
# Example1

# Input: "123"
# Output: [["1","2","3"],["12","3"],["1","23"]]
# Example2

# Input: "12345"
# Output: [["1","23","45"],["12","3","45"],["12","34","5"],["1","2","3","45"],["1","2","34","5"],["1","23","4","5"],["12","3","4","5"],["1","2","3","4","5"]]
# Related Problems

# Own Solution
class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        # s = sorted(s)
        result = []
        combine = []
        if not s:
            return [[]]
        is_full = False
        self.dfs(0, s, combine, result, is_full)
        return result

    def dfs(self, index, s, combine, result, is_full):
        if is_full:
            result.append(list(combine))
        if index < len(s):
            for j in range(2):
                if j == 0:
                    combine.append(s[index])
                    if index == len(s) - 1 and combine[0][0] == s[0]:
                        is_full = True
                    else:
                        is_full = False
                    self.dfs(index + 1, s, combine, result, is_full)
                    combine.pop()
                elif index + 1 < len(s):
                    combine.append(s[index]+s[index + 1])
                    if index + 1 == len(s) - 1 and combine[0][0] == s[0]:
                        is_full = True
                    else:
                        is_full = False
                    self.dfs(index + 2, s, combine, result, is_full)
                    combine.pop()
