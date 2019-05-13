# Description
# 中文
# English
# Design an iterator over a binary search tree with the following rules:

# Elements are visited in ascending order (i.e. an in-order traversal)
# next() and hasNext() queries run in O(1) time in average.
# Have you met this question in a real interview?  
# Example
# Example 1

# Input:  {10,1,11,#,6,#,12}
# Output:  [1, 6, 10, 11, 12]
# Explanation:
# The BST is look like this:
#   10
#   /\
#  1 11
#   \  \
#    6  12
# You can return the inorder traversal of a BST [1, 6, 10, 11, 12]
# Example 2

# Input: {2,1,3}
# Output: [1,2,3]
# Explanation:
# The BST is look like this:
#   2
#  / \
# 1   3
# You can return the inorder traversal of a BST tree [1,2,3]
# Challenge
# Extra memory usage O(h), h is the height of the tree.

# Super Star: Extra memory usage O(1)

# 这是一个非常通用的利用 stack 进行 Binary Tree Iterator 的写法。

# stack 中保存一路走到当前节点的所有节点，stack.peek() 一直指向 iterator 指向的当前节点。
# 因此判断有没有下一个，只需要判断 stack 是否为空
# 获得下一个值，只需要返回 stack.peek() 的值，并将 stack 进行相应的变化，挪到下一个点。

# 挪到下一个点的算法如下：

# 如果当前点存在右子树，那么就是右子树中“一路向西”最左边的那个点
# 如果当前点不存在右子树，则是走到当前点的路径中，第一个左拐的点

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""


class BSTIterator:
    #@param root: The root of binary tree.
    def __init__(self, root):
        self.stack = []
        self.curt = root

    #@return: True if there has next node, or false
    def hasNext(self):
        return self.curt is not None or len(self.stack) > 0

    #@return: return next node
    def next(self):
        while self.curt is not None:
            self.stack.append(self.curt)
            self.curt = self.curt.left
            
        self.curt = self.stack.pop()
        nxt = self.curt
        self.curt = self.curt.right
        return nxt