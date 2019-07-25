# 900. Closest Binary Search Tree Value
# Description
# 中文
# English
# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.
# Have you met this question in a real interview?  
# Example
# Example1

# Input: root = {5,4,9,2,#,8,10} and target = 6.124780
# Output: 5
# Example2

# Input: root = {3,2,4,1} and target = 4.142857
# Output: 4

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
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        upper = root
        lower = root
        while root:
            # 当前值比目标值大，更新一下最新的上届，并且找更小值，反过来当前值比目标值小，就更新一下下届，找更大的值，最后卡在最大和最小的两个值之间进行比较
            if root.val == target:
                return root.val
            elif root.val > target:
                upper = root
                root = root.left
            else:
                lower = root
                root = root.right
            # print(upper.val)
            # print(lower.val)
        
        if abs(upper.val - target) <= abs(lower.val - target):
            return upper.val
        return lower.val