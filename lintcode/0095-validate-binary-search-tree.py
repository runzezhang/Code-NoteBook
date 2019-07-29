# 95. Validate Binary Search Tree
# Description
# 中文
# English
# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# A single node tree is a BST
# Have you met this question in a real interview?  
# Example
# Example 1:

# Input:  {-1}
# Output：true
# Explanation：
# For the following binary tree（only one node）:
# 	      -1
# This is a binary search tree.
# Example 2:

# Input:  {2,1,4,#,#,3,5}
# Output: true
# For the following binary tree:
# 	  2
# 	 / \
# 	1   4
# 	   / \
# 	  3   5
# This is a binary search tree.

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
    @return: True if the binary tree is BST, or false
    """
    
    
    def isValidBST(self, root):
        # write your code here
        self.last_node = None
        self.is_valid = True
        self.inorder_traverse(root)
        
        return self.is_valid
        
        
    def inorder_traverse(self, root):
        if root is None:
            return
        
        self.inorder_traverse(root.left)
        if self.last_node is not None and root.val <= self.last_node:
            self.is_valid = False
            return
        self.last_node = root.val
        self.inorder_traverse(root.right)


# 本参考程序来自九章算法，由 @令狐冲 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


# Python3
# Another iteration version

# 直接遍历树做判断。
# 需要注意的是，根要大于左子树中的Max，小于右子树的Min。

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
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        if root is None:
            return True
            
        stack = []
        while root:
            stack.append(root)
            root = root.left
            
        last_node = stack[-1]
        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

            # the only difference compare to an inorder traversal iteration
            # this problem disallowed equal values so it's <= not <
            if stack:
                if stack[-1].val <= last_node.val:
                    return False
                last_node = stack[-1]
        return True

九章算法
更新于 2/20/2019, 9:10:54 PM
Given a binary tree, determine if it is a valid binary search tree (BST). 


Assume a BST is defined as follows: 
        The left subtree of a node contains only nodes with keys less than the node's key. 
        The right subtree of a node contains only nodes with keys greater than the node's key. 
        Both the left and right subtrees must also be binary search trees.

详细题解请见九章算法微博：http://weibo.com/3948019741/BCtxCxBY6
# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        self.lastVal = None
        self.isBST = True
        self.validate(root)
        return self.isBST

    def validate(self, root):
        if root is None:
            return
        self.validate(root.left)
        if self.lastVal is not None and self.lastVal >= root.val:
            self.isBST = False
            return
        self.lastVal = root.val
        self.validate(root.right)

严助教
更新于 3/10/2019, 12:29:44 AM
Divide and conquer version.

# 本参考程序来自九章算法，由 @严助教 提供。版权所有，转发请注明出处。
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
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    
        
    def isValidBST(self, root):
        # write your code here
        isBST, minNode, maxNode = self.divideConquer(root)
        return isBST
        
    def divideConquer(self, root):
        if root is None:
            return True, None, None
        
        leftIsBST, leftMin, leftMax = self.divideConquer(root.left)
        rightIsBST, rightMin, rightMax = self.divideConquer(root.right)
        if not leftIsBST or not rightIsBST:
            return False, None, None
        if leftMax is not None and leftMax >= root.val:
            return False, None, None
        if rightMin is not None and rightMin <= root.val:
            return False, None, None
        
        # is BST
        minNode = leftMin if leftMin is not None else root.val
        maxNode = rightMax if rightMax is not None else root.val
        
        return True, minNode, maxNode

令狐冲
更新于 1/22/2019, 4:46:23 PM
Python3
Iteration version

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
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        if root is None:
            return True
            
        stack = []
        while root:
            stack.append(root)
            root = root.left
            
        last_node = stack[-1]
        while stack:
            if stack[-1].right:
                node = stack[-1].right
                while node:
                    stack.append(node)
                    node = node.left
            else:
                node = stack.pop()
                while stack and stack[-1].right == node:
                    node = stack.pop()

            # the only difference compare to an inorder traversal iteration
            # this problem disallowed equal values so it's <= not <
            if stack:
                if stack[-1].val <= last_node.val:
                    return False
                last_node = stack[-1]
        return True