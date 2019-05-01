# 596. Minimum Subtree
# Description
# 中文
# English
# Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.

# LintCode will print the subtree which root is your return node.
# It's guaranteed that there is only one subtree with minimum sum and the given binary tree is not an empty tree.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input:
# {1,-5,2,1,2,-4,-5}
# Output:1
# Explanation:
# The tree is look like this:
#      1
#    /   \
#  -5     2
#  / \   /  \
# 0   2 -4  -5 
# The sum of whole tree is minimum, so return the root.
# Example 2:

# Input:
# {1}
# Output:1
# Explanation:
# The tree is look like this:
#    1
# There is one and only one subtree in the tree. So we return 1.

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        self.min_weight = sys.maxsize
        self.min_node = None
        self.dfs(root)
        
        return self.min_node
        
    def dfs(self, root):
        if root is None:
            return
        
        left_weight = self.dfs(root.left)
        right_weight = self.dfs(root.right)
        
        
        current_weight = left_weight + right_weight + root.val
        
        if current_weight < self.min_weight:
            self.min_weight = current_weight
            self.min_node = root
        
        return current_weight


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        self.minumum_weight = sys.maxsize
        self.subtree = None
        self.helper(root)

        return self.subtree

    def helper(self, root):
        if root is None:
            return 0

        left_weight = self.helper(root.left)
        right_weight = self.helper(root.right)
        root_weight = left_weight + right_weight + root.val
        
        if root_weight < self.minumum_weight:
            self.minumum_weight = root_weight
            self.subtree = root

        return root_weight