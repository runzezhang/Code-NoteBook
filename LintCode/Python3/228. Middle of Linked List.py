# Description
# 中文
# English
# Find the middle node of a linked list.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input:  1->2->3
# Output: 2	
# Explanation: return the value of the middle node.
# Example 2:

# Input:  1->2
# Output: 1	
# Explanation: If the length of list is  even return the value of center left one.	
# Challenge
# If the linked list is in a data stream, can you find the middle without iterating the linked list again?

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middleNode(self, head):
        # write your code here
        if head is None:
            return None
        mid = head
        final = head.next
        while final != None and final.next != None:
            mid = mid.next
            final = final.next.next
        return mid