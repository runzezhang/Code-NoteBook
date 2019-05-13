# Description
# 中文
# English
# Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.
# The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.
# Return null if LCA does not exist.

# node A or node B may not exist in tree.

# Have you met this question in a real interview?  
# Example
# Example1

# Input: 
# {4, 3, 7, #, #, 5, 6}
# 3 5
# 5 6
# 6 7 
# 5 8
# Output: 
# 4
# 7
# 7
# null
# Explanation:
#   4
#  / \
# 3   7
#    / \
#   5   6

# LCA(3, 5) = 4
# LCA(5, 6) = 7
# LCA(6, 7) = 7
# LCA(5, 8) = null

# Example2

# Input:
# {1}
# 1 1
# Output: 
# 1
# Explanation:
# The tree is just a node, whose value is 1.



"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        a, b, lca = self.helper(root, A, B)
        if a and b:
            return lca
        else:
            return None

    def helper(self, root, A, B):
        if root is None:
            return False, False, None
            
        left_a, left_b, left_node = self.helper(root.left, A, B)
        right_a, right_b, right_node = self.helper(root.right, A, B)
        
        a = left_a or right_a or root == A
        b = left_b or right_b or root == B
        
        if root == A or root == B:
            return a, b, root

        if left_node is not None and right_node is not None:
            return a, b, root
        if left_node is not None:
            return a, b, left_node
        if right_node is not None:
            return a, b, right_node

        return a, b, None
