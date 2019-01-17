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