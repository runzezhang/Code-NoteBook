# Description
# Find the maximum node in a binary tree, return the node.
# Example
# Example 1:
# 	Input:
#      1
#    /   \
#  -5     3
#  / \   /  \
# 1   2 -4  -5 
	
# 	Output: The node with value 3.
# 	Explanation:
# 		return the node with max value.

# Example 1:
# 	Input:
#      10
#    /   \
#  -5     2
#  / \   /  \
# 0   3 -4  -5 
	
# 	Output: The node with value 10.
# 	Explanation:
# 		return the node with max value.
# return the node with value 3.

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param: root: the root of tree
    @return: the max node
    """
    def maxNode(self, root):
        # write your code here
        if root is None:
            return root
            
        left = self.maxNode(root.left)
        right = self.maxNode(root.right)
        
        return self.max(root, self.max(left,right))
        
    def max(self, a, b):
        if a is None:
            return b
        if b is None:
            return a
        if a.val > b.val:
            return a
        return b