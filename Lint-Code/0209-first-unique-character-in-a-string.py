# Description
# 中文
# English
# Find the first unique character in a given string. You can assume that there is at least one unique character in the string.

# Have you met this question in a real interview?  
# Example
# Example 1:
# 	Input: "abaccdeff"
# 	Output:  'b'
	
# 	Explanation:
# 	There is only one 'b' and it is the first one.


# Example 2:
# 	Input: "aabccd"
# 	Output:  'b'
	
# 	Explanation:
# 	'b' is the first one.

class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        list_str = list(str)
        dict_str = {}
        for i in list_str:
            if i not in dict_str:
                dict_str[i] = 1 
            else:
                dict_str[i] += 1
        for i in list_str:
            if dict_str[i] == 1:
                return i