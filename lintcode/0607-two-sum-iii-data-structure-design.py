# 607. Two Sum III - Data structure design
# Description
# 中文
# English
# Design and implement a TwoSum class. It should support the following operations: add and find.

# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.

# Have you met this question in a real interview?  
# Example
# Example 1:

# add(1); add(3); add(5);
# find(4) // return true
# find(7) // return false

class TwoSum:
    def __init__(self):
        # initialize your data structure here
        self.count = {}
    
    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        # write your code here
        if number in self.count:
            self.count[number] += 1
        else:
            self.count[number] = 1 

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        for i in self.count:
            # this is important 
            if value - i in self.count and (value - i != i or self.count[i] > 1):
                return True 
        return False