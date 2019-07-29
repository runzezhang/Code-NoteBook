# Description
# 中文
# English
# Given a binary tree, return the postorder traversal of its nodes' values.

# The first data is the root node, followed by the value of the left and right son nodes, and "#" indicates that there is no child node.
# The number of nodes does not exceed 20.
# Have you met this question in a real interview?  
# Example
# Example 1:

# Input：{1,2,3}
# Output：[2,3,1]
# Explanation:  
#    1
#   / \
#  2   3
#  it will be serialized {1,2,3}
# Post order traversal
# Example 2:

# Input：{1,#,2,3}
# Output：[3,2,1]
# Explanation:  
# 1
#  \
#   2
#  /
# 3
# it will be serialized {1,#,2,3}
# Post order traversal
# Challenge
# Can you do it without recursion?

# Related Problems

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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        # write your code here
        result = []
        self.traverse(root, result)
        
        return result
        
    
    def traverse(self, root, result):
        if not root:
            return
        
        self.traverse(root.left, result)
        self.traverse(root.right, result)
        result.append(root.val)