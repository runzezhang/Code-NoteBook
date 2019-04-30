# Description
# 中文
# English
# Given two words (start and end), and a dictionary, find the shortest transformation sequence from start to end, output the length of the sequence.
# Transformation rule such that:

# Only one letter can be changed at a time
# Each intermediate word must exist in the dictionary. (Start and end words do not need to appear in the dictionary )
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# Have you met this question in a real interview?  
# Example
# Example 1:

# Input：start = "a"，end = "c"，dict =["a","b","c"]
# Output：2
# Explanation：
# "a"->"c"
# Example 2:

# Input：start ="hit"，end = "cog"，dict =["hot","dot","dog","lot","log"]
# Output：5
# Explanation：
# "hit"->"hot"->"dot"->"dog"->"cog"

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        # I forget to add end in dict so it will miss if some word in dict is only one char differ than end
        dict.add(end)
        queue = collections.deque([start])
        distance = {start: 1}
        
        while queue:
            current = queue.popleft()
            if current == end:
                return distance[current]
            for next_word in self.next_words(current):
                if next_word in dict and next_word not in distance:
                    distance[next_word] = distance[current] + 1
                    queue.append(next_word)
        return 0
    def next_words(self, current):
        words = []
        for i in range(len(current)):
            left, right = current[ :i], current[i + 1: ]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if char != current[i]:
                    words.append(left + char + right)
        return words
            