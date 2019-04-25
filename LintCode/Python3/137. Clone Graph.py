# Description
# 中文
# English
# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

# How we serialize an undirected graph: http: // www.lintcode.com/help/graph/

# Nodes are labeled uniquely.

# # as a separator for each node, and , as a separator for node label and each neighbor of the node.
# We use

# As an example, consider the serialized graph {0, 1, 2  # 1,2#2,2}.

# # .
# The graph has a total of three nodes, and therefore contains three parts as separated by

# First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
# Second node is labeled as 1. Connect node 1 to node 2.
# Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
# Visually, the graph looks like the following:

#    1
#   / \
#  /   \
# 0 - -- 2
#      / _ /
# Have you met this question in a real interview?
# Example
# return a deep copied graph.

# 本参考程序来自九章算法，由 @令狐冲 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


# class Solution:
#     def cloneGraph(self, node):
#         root = node
#         if node is None:
#             return node

#         # use bfs algorithm to traverse the graph and get all nodes.
#         nodes = self.getNodes(node)

#         # copy nodes, store the old->new mapping information in a hash map
#         mapping = {}
#         for node in nodes:
#             mapping[node] = UndirectedGraphNode(node.label)

#         # copy neighbors(edges)
#         for node in nodes:
#             new_node = mapping[node]
#             for neighbor in node.neighbors:
#                 new_neighbor = mapping[neighbor]
#                 new_node.neighbors.append(new_neighbor)

#         return mapping[root]

#     def getNodes(self, node):
#         q = collections.deque([node])
#         result = set([node])
#         while q:
#             head = q.popleft()
#             for neighbor in head.neighbors:
#                 if neighbor not in result:
#                     result.add(neighbor)
#                     q.append(neighbor)
#         return result


"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """

    def cloneGraph(self, node):
        # write your code here
        if node is None:
            return None
        root = node

        nodes = self.set_nodes(node)

        mapping = {}

        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)

        for node in nodes:
            for neighbor in node.neighbors:
                mapping[node].neighbors.append(mapping[neighbor])
        return mapping[root]

    def set_nodes(self, node):
        queue = collections.deque([node])
        result = set([node])
        while queue:
            current = queue.popleft()
            for neighbor in current.neighbors:
                if neighbor not in result:
                    result.add(neighbor)
                    queue.append(neighbor)
        return result
