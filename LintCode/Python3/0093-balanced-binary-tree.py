# Description
# 中文
# English
# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Have you met this question in a real interview?  
# Example
# Example  1:
# 	Input: tree = {1,2,3}
# 	Output: true
	
# 	Explanation:
# 	This is a balanced binary tree.
# 		  1  
# 		 / \                
# 		2  3

	
# Example  2:
# 	Input: tree = {3,9,20,#,#,15,7}
# 	Output: true
	
# 	Explanation:
# 	This is a balanced binary tree.
# 		  3  
# 		 / \                
# 		9  20                
# 		  /  \                
# 		 15   7 

	
# Example  3:
# 	Input: tree = {1,#,2,3,4}
# 	Output: false
	
# 	Explanation:
# 	This is not a balanced tree. 
# 	The height of node 1's right sub-tree is 2 but left sub-tree is 0.
# 		  1  
# 		   \                
# 		   2                
# 		  /  \                
# 		 3   4

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    not_balanced = - 1
    def isBalanced(self, root):
        # write your code here
        result = self.maxDepth(root)
        if  result == self.not_balanced:
            return False 
        else:
             return True
    
    def maxDepth(self, node):
        if node is None:
            return 0
        
        left = self.maxDepth(node.left)
        right = self.maxDepth(node.right)
        
        if left is self.not_balanced or right is self.not_balanced:
            return self.not_balanced
        
        if abs(left - right) > 1:
            return self.not_balanced
        
        return max(left , right) + 1 