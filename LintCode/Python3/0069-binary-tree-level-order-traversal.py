# Description
# 中文
# English
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# The first data is the root node, followed by the value of the left and right son nodes, and "#" indicates that there is no child node.
# The number of nodes does not exceed 20.
# Have you met this question in a real interview?
# Example
# Example 1:

# Input：{1,2,3}
# Output：[[1],[2,3]]
# Explanation：
#   1
#  / \
# 2   3
# it will be serialized {1,2,3}
# level order traversal
# Example 2:

# Input：{1,#,2,3}
# Output：[[1],[2],[3]]
# Explanation：
# 1
#  \
#   2
#  /
# 3
# it will be serialized {1,#,2,3}
# level order traversal
# Challenge
# Challenge 1: Using only 1 queue to implement it.

# Challenge 2: Use BFS algorithm to do it.

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


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
    @return: Level order a list of lists of integer
    """

    def levelOrder(self, root):
        # write your code here
        if root is None:
            return None
        queue = collections.deque([root])
        result = []
        while queue:
            tmp = []
            length = len(queue)
            for i in range(length):
                current = queue.popleft()
                tmp.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            result.append(tmp)
        return result
