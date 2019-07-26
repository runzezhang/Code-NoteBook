# Description
# 中文
# English
# Convert a char to an integer. You can assume the char is in ASCII code (See Definition, so the value of the char should be in 0~255.

# Have you met this question in a real interview?  
# Example
# Example 1:
# 	Input:  'a'
# 	Output: 97
	
# 	Explanation: 
# 	return the number of the char in ASCII.

# Example 2:
# 	Input:  '%'
# 	Output: 37
	
# 	Explanation: 
# 	return the number of the char in ASCII.

class Solution:
    """
    @param character: a character
    @return: An integer
    """
    def charToInteger(self, character):
        # write your code here
        if character is None:
            return 0
        return ord(character)