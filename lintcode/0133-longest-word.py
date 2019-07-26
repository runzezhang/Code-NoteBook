# Description
# 中文
# English
# Given a dictionary, find all of the longest words in the dictionary.

# Have you met this question in a real interview?  
# Example
# Example 1:
# 	Input: {
# 		"dog",
# 		"google",
# 		"facebook",
# 		"internationalization",
# 		"blabla"
# 		}
# 	Output: ["internationalization"]


# Example 2:
# 	Input:  {
# 		"like",
# 		"love",
# 		"hate",
# 		"yes"		
# 		}
# 	Output: ["like", "love", "hate"]
	

# Challenge
# It's easy to solve it in two passes, can you do it in one pass?

class Solution:
    """
    @param: dictionary: an array of strings
    @return: an arraylist of strings
    """
    def longestWords(self, dictionary):
        # write your code here
        max_length = 0
        max_list = []
        for item in dictionary:
            if len(item) > max_length:
                max_length = len(item)
                max_list = []
                max_list.append(item)
            elif len(item) == max_length:
                max_list.append(item)
        return max_list