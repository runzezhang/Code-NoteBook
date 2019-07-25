# Description
# Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place finally.

# The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

# Example
# Example 1:

# Input: "UD"
# Output: true
# Example 2:

# Input: "LL"
# Output: false

class Solution:
    """
    @param moves: a sequence of its moves
    @return: if this robot makes a circle
    """
    def judgeCircle(self, moves):
        # Write your code here
        x = 0
        y = 0
        for a in moves:
            if a == 'U':
                y += 1 
            if a == 'D':
                y -= 1
            if a == 'L':
                x += 1
            if a == 'R':
                x -= 1
        if x == 0 and y == 0:
            return True
        else:
            return False