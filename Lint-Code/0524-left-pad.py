# Description
# 中文
# English
# You know what, left pad is javascript package and referenced by React:
# Github link

# One day his author unpublished it, then a lot of javascript projects in the world broken.

# You can see from github it's only 11 lines.

# You job is to implement the left pad function. If you do not know what left pad does, see examples below and guess.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input:
# leftpad("foo", 5)
# Output:
# "  foo"
# Example 2:

# Input:
# leftpad("foobar", 6)
# Output:
# "foobar"
# Example 3:

# Input:
# leftpad("1", 2, "0")
# Output:
# "01"
# Challenge
# Use as little memory as possible

class StringUtils:
    """
    @param: originalStr: the string we want to append to
    @param: size: the target length of the string
    @param: padChar: the character to pad to the left side of the string
    @return: A string
    """
    @classmethod
    def leftPad(self, originalStr, size, padChar=' '):
        # write your code here
        result = [padChar for i in range(0, size-len(originalStr))]
        result = ''.join(result)
        result += originalStr
        return result