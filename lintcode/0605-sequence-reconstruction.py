# Description
# 中文
# English
# Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 10^4. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input:org = [1,2,3], seqs = [[1,2],[1,3]]
# Output: false
# Explanation:
# [1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
# Example 2:

# Input: org = [1,2,3], seqs = [[1,2]]
# Output: false
# Explanation:
# The reconstructed sequence can only be [1,2].
# Example 3:

# Input: org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
# Output: true
# Explanation:
# The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
# Example 4:

# Input:org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
# Output:true

class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        graph = self.get_graph(seqs)
        topological_sort = self.topological_sort(graph)
        
        return topological_sort == org
    
    def get_graph(self, seqs):
        graph = {}
        for i in seqs:
            for j in i:
                if j not in graph:
                    graph[j] = set()
        
        for i in seqs:
            for j in range(1, len(i)):
                graph[i[j - 1]].add(i[j])
        return graph
        
    # re-study     
    def get_indegrees(self, graph):
        indegrees = {
            node: 0
            for node in graph
        }
        
        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1
                
        return indegrees
        
    def topological_sort(self, graph):
        indegrees = self.get_indegrees(graph)
        
        queue = []
        for node in graph:
            if indegrees[node] == 0:
                queue.append(node)
        
        topo_order = []
        while queue:
            if len(queue) > 1:
                # there must exist more than one topo orders
                return None
                
            node = queue.pop()
            topo_order.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
                    
        if len(topo_order) == len(graph):
            return topo_order
            
        return None
        