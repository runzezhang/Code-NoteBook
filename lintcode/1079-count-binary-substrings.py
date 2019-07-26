# Description
# 中文
# English
# Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

# Substrings that occur multiple times are counted the number of times they occur.

# s.length will be between 1 and 50,000.
# s will only consist of "0" or "1" characters.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input: "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

# Notice that some of these substrings repeat and are counted the number of times they occur.

# Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
# Example 2:

# Input: "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

class Solution:
    """
    @param s: a string
    @return: the number of substrings
    """
    def countBinarySubstrings(self, s):
        # Write your code here
        n = len(s)
        res = 0
        # ç®åè¿ç»­æ°æ®µçå¼å§è®¡æ°ä½ç½®
        start = 0
        # åºç°æ°æ®ååæ¶ï¼ç»è®¡çä¹åè¿ç»­æ°æ®µé¿åº¦
        lastcount = 1
        for i in range(1, n):
            if s[i] != s[i -1]:
              res += 1
              lastcount = i - start
              start = i
            else:
                if i - start < lastcount:
                    res += 1
        return res