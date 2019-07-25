# Description
# 中文
# English
# There are a total of n courses you have to take, labeled from 0 to n - 1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# Have you met this question in a real interview?
# Example
# Example 1:

# Input: n = 2, prerequisites = [[1,0]]
# Output: true
# Example 2:

# Input: n = 2, prerequisites = [[1,0],[0,1]]
# Output: false

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        if numCourses is None or numCourses == 0:
            return True 
        count = self.top_sort(prerequisites, numCourses)
        
        return count == numCourses
    def top_sort(self, prerequisites, numCourses):
        nodes_with_degree = [ 0 for i in range(numCourses)]
        edges = { i: [] for i in range(numCourses) }
        
        for x, y in prerequisites:
            edges[y].append(x)
            nodes_with_degree[x] += 1
        
        count = 0
        queue = collections.deque([])
        
        for i in range(len(nodes_with_degree)):
            if nodes_with_degree[i] == 0:
                queue.append(i)
        
        while queue:
            current_node = queue.popleft()
            count += 1 
            for child in edges[current_node]:
                nodes_with_degree[child] -= 1
                if nodes_with_degree[child] == 0:
                    queue.append(child)
        
        return count
                
        