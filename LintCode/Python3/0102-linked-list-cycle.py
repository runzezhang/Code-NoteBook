# Description
# 中文
# English
# Given a linked list, determine if it has a cycle in it.



# Have you met this question in a real interview?  
# Example
# 	Example 1:
# 		Input: 21->10->4->5,  then tail connects to node index 1(value 10).
# 		Output: true
		
# 	Example 2:
# 		Input: 21->10->4->5->null
# 		Output: false
	
# 	```
# Challenge
# Follow up:
# Can you solve it without using extra space?

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        if head == None or head.next == None:
            return  False 
        slow = head
        fast = head.next
        while slow != fast:
            if fast == None or fast.next == None:
                return False 
            slow = slow.next 
            fast = fast.next.next 
        return True