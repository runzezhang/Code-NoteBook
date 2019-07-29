# Description
# 中文
# English
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input：{1,#,2},2
# Output：2
# Explanation：
# 	1
# 	 \
# 	  2
# The second smallest element is 2.
# Example 2:

# Input：{2,1,3},1
# Output：1
# Explanation：
#   2
#  / \
# 1   3
# The first smallest element is 1.
# Challenge
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
        
        for i in range(k):
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack is None:
                break
        return stack[-1].val
            