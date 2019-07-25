# Description
# 中文
# English
# Given a binary tree, return the inorder traversal of its nodes' values.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input：{1,2,3}
# Output：[2,1,3]
# Explanation:
#    1
#   / \
#  2   3
# it will be serialized {1,2,3}
# Inorder Traversal
# Example 2:

# Input：{1,#,2,3}
# Output：[1,3,2]
# Explanation:
# 1
#  \
#   2
#  /
# 3
# it will be serialized {1,#,2,3}
# Inorder Traversal
# Challenge
# Can you do it without recursion?

# # Related Problems

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        result = []
        self.traverse(root, result)
        
        return result
        
    
    def traverse(self, root, result):
        if not root:
            return
        
        self.traverse(root.left, result)
        result.append(root.val)
        self.traverse(root.right, result)