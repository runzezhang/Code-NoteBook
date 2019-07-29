# Description
# 中文
# English
# Two strings are given and you have to modify 1st string such that all the common characters of the 2nd strings have to be removed and the uncommon characters of the 2nd string have to be concatenated with uncommon characters of the 1st string.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input : s1 = "aacdb", s2 = "gafd"
# Output : "cbgf"
# Example 2:

# Input : s1 = "abcs", s2 = "cxzca"
# Output : "bsxz"

class Solution:
    """
    @param s1: the 1st string
    @param s2: the 2nd string
    @return: uncommon characters of given strings
    """
    def concatenetedString(self, s1, s2):
        # write your code here
        set1 = set(s1)
        set2 = set(s2)
        join_set = set1 & set2
        print(join_set)
        i = 0
        while i < len(s1):
        # for i in range(0, len(s1)):
            if s1[i] in join_set:
                s1 = s1[0:i]+s1[i+1:]
                # !!!index has changed here 
                i -= 1
            i += 1
            
        for j in range(0, len(s2)):
            if s2[j] not in join_set:
                s1 += s2[j]
        return s1