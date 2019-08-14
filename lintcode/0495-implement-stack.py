# Description
# 中文
# English
# Implement a stack. You can use any data structure inside a stack except stack itself to implement it.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input:
# push(1)
# pop()
# push(2)
# top()  // return 2
# pop()
# isEmpty() // return true
# push(3)
# isEmpty() // return false
# Example 2:

# Input:
# isEmpty()

class Stack:
    def __init__(self):
        self.array = []
    			
    # åå¥æ°åç´ 
    def push(self, x):
        self.array.append(x)
    
    # æ é¡¶åç´ åºæ 
    def pop(self):
        if not self.isEmpty():
            self.array.pop()
	
    # è¿åæ é¡¶åç´ 
    def top(self):
        return self.array[-1]

    # å¤æ­æ¯å¦æ¯ç©ºæ 
    def isEmpty(self):
        return len(self.array) == 0