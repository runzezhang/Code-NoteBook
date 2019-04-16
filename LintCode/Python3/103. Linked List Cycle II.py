# Description
# 中文
# English
# Given a linked list, return the node where the cycle begins.

# If there is no cycle, return null.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input：null,no cycle
# Output：no cycle
# Explanation：
# List is null，so no cycle.
# Example 2:

# Input：-21->10->4->5，tail connects to node index 1
# Output：10
# Explanation：
# The last node 5 points to the node whose index is 1, which is 10, so the entrance of the ring is 10
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
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        if head == None or head.next == None:
            return  None 
        slow = head
        fast = head.next
        while slow != fast:
            if fast == None or fast.next == None:
                return None
                break
            slow = slow.next 
            fast = fast.next.next
            if slow == fast:
                break
            
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        return None
        
        
        # if head == None or head.next == None:
        #     return None
        
        # slow = fast = head      	#初始化快指针和慢指针
        # while fast and fast.next:	
        #     slow = slow.next
        #     fast = fast.next.next
        #     if fast == slow:		#快慢指针相遇
        #         break
        # if slow == fast:
        #     slow = head				#从头移动慢指针
        #     while slow != fast:
        #         slow = slow.next
        #         fast = fast.next
        #     return slow				#两指针相遇处即为环的入口
        # return None