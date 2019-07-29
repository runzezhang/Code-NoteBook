# Description
# 中文
# English
# The words are same rotate words if rotate the word to the right by loop, and get another. Count how many different rotate word sets in dictionary.

# E.g. picture and turepic are same rotate words.

# All words are lowercase.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input : ["picture", "turepic", "icturep", "word", "ordw", "lint"]
# Output : 3
# Explanation : 
# "picture", "turepic", "icturep" are same ratote words.
# "word", "ordw" are same too.
# "lint" is the third word that different from the previous two words.

class Solution:
    """
    @param: words: A list of words
    @return: Return how many different rotate words
    """
    def countRotateWords(self, words):
        # Write your code here
        # this methods use 2 loop when words is too large it can sceed time limit
        # counts = set()
        # for word in words:
        #     is_checked = False
        #     for count in counts:
        #         check = count + count
        #         if check.find(word) != -1 and len(word) == len(count):
        #             is_checked = True
        #             break
        #     if not is_checked:
        #         counts.add(word)
        # return len(counts)
        
        counts = set()
        for word in words:
            tmp = word + word
            is_checked = False
            for i in range(0,len(word)):
                if tmp[i: i + len(word)] in counts:
                    is_checked = True
                    break
            if not is_checked:
                counts.add(word)
            
        return len(counts)