# 453. Flatten Binary Tree to Linked ListDescription
# 中文
# English
# Flatten a binary tree to a fake "linked list" in pre-order traversal.

# Here we use the right pointer in TreeNode as the next pointer in ListNode.

# Don't forget to mark the left child of each node to null. Or you will get Time Limit Exceeded or Memory Limit Exceeded.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input:
# {1,2,5,3,4,#,6}
#      1
#     / \
#    2   5
#   / \   \
#  3   4   6
# Output:
# {1,#,2,#,3,#,4,#,5,#,6}
# 1
# \
#  2
#   \
#    3
#     \
#      4
#       \
#        5
#         \
#          6
# Example 2:

# Input:
# {1}
# 1
# Output:
# {1}
# 1

# 分治法，有返回值，相对不容易出BUG
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        self.helper(root)
        
    def helper(self, root):
        if root is None:
            return
        
        left_last = self.helper(root.left)
        right_last = self.helper(root.right)
        
        if left_last is not None:
            left_last.right = root.right
            root.right = root.left
            root.left = None 
        
        if right_last is not None:
            return right_last
        if left_last is not None:
            return left_last
        return root


# 遍历法 全局变量容易出错，尽量少用


# 本参考程序来自九章算法，由 @令狐冲 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    last_node = None
    
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        if root is None:
            return
        
        if self.last_node is not None:
            self.last_node.left = None
            self.last_node.right = root
            
        self.last_node = root
        right = root.right
        self.flatten(root.left)
        self.flatten(right)