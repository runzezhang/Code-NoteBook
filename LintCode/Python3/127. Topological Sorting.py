# Description
# 中文
# English
# Given an directed graph, a topological order of the graph nodes is defined as follow:

# For each directed edge A -> B in graph, A must before B in the order list.
# The first node in the order can be any node in the graph with no nodes direct to it.
# Find any topological order for the given graph.

# You can assume that there is at least one topological order in the graph.

# Have you met this question in a real interview?
# Clarification
# Learn more about representation of graphs

# Example
# For graph as follow:

# picture

# The topological order can be:

# [0, 1, 2, 3, 4, 5]
# [0, 2, 3, 1, 5, 4]
# ...
# Challenge
# Can you do it in both BFS and DFS?

"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph):
        # write your code here
        nodes_with_indegree = self.get_indegree(graph)

        result = []
        start_queue = [
            node for node in nodes_with_indegree if nodes_with_indegree[node] == 0]
        queue = collections.deque(start_queue)
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in node.neighbors:
                nodes_with_indegree[neighbor] -= 1
                if nodes_with_indegree[neighbor] == 0:
                    queue.append(neighbor)
        return result

    def get_indegree(self, graph):
        nodes_with_indegree = {x: 0 for x in graph}

        for node in graph:
            for neighbor in node.neighbors:
                nodes_with_indegree[neighbor] += 1

        return nodes_with_indegree
