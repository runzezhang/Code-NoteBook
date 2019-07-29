# Description
# 中文
# English
# Given a string, convert it to an integer. You may assume the string is a valid integer number that can be presented by a signed 32bit integer (-231 ~ 231-1).

# Have you met this question in a real interview?  
# Example
# Example 1:
# 	Input:  "123"
# 	Output: 123
	
# 	Explanation: 
# 	return the Integer.

# Example 2:
# 	Input:  "2"
# 	Output: 2
	
# 	Explanation: 
# 	return the Integer.

class Solution:
    """
    @param str: A string
    @return: An integer
    """
    def stringToInteger(self, str):
        # write your code here
        if str[0] == '-':
            str = str[1:]
            sum = 0
            time = 1
            for i in range(1, len(str) + 1):
                sum += int(str[-i])*time
                time *= 10
            return -sum
        else:
            sum = 0
            time = 1
            for i in range(1, len(str) + 1):
                sum += int(str[-i])*time
                time *= 10
            return sum    
        
        # num, sig = 0, 1
        
        # if str[0] == '-':
        #     sig = -1
        #     str = str[1:]

        # for c in str:
        #     num = num * 10 + ord(c) - ord('0')
            
        # return num * sig