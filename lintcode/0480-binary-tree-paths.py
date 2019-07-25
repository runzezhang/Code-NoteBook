# 480. Binary Tree PathsDescription
# 中文
# English
# Given a binary tree, return all root-to-leaf paths.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input:

#    1
#  /   \
# 2     3
#  \
#   5

# Output:


# [
#   "1->2->5",
#   "1->3"
# ]
# Example 2:

# Input:

#    1
#  /   
# 2     
 

# Output:


# [
#   "1->2"
# ]

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        if root is None:
            return []
        result = []
        path = [str(root.val)]
        self.dfs(result, path, root)
        
        return result
    def dfs(self, result, path, root):
        if root.left is None and root.right is None:
            new_path = '->'.join(path)
            result.append(new_path)
            return
        if root.left:
            path.append(str(root.left.val))
            self.dfs(result, path, root.left)
            path.pop()
        if root.right:
            path.append(str(root.right.val))
            self.dfs(result, path, root.right)
            path.pop()