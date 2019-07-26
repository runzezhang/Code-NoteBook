# Description
# 中文
# English
# Implement an upper method to convert all characters in a string to uppercase.

# The characters not in alphabet don't need to convert.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input: str = "abc"
# Output: "ABC"
# Example 2:

# Input: str = "aBc"
# Output: "ABC"
# Example 3:

# Input: str = "abC12"
# Output: "ABC12"

class Solution:
    """
    @param str: A string
    @return: A string
    """
    def lowercaseToUppercase2(self, str):
        # write your code here
        result = ''
        for char in str:
            if char.islower():
                char = char.upper()
            result += char
        return result