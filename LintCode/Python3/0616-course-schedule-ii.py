# Description
# 中文
# English
# There are a total of n courses you have to take, labeled from 0 to n - 1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input: n = 2, prerequisites = [[1,0]] 
# Output: [0,1]
# Example 2:

# Input: n = 4, prerequisites = [1,0],[2,0],[3,1],[3,2]] 
# Output: [0,1,2,3] or [0,2,1,3]

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        if numCourses is None or numCourses == 0:
            return True 
        result = self.top_sort(prerequisites, numCourses)
        if numCourses != len(result):
            return []
        return result
    def top_sort(self, prerequisites, numCourses):
        nodes_with_degree = [ 0 for i in range(numCourses)]
        edges = { i: [] for i in range(numCourses) }
        
        for x, y in prerequisites:
            edges[y].append(x)
            nodes_with_degree[x] += 1
        
        result = []
        queue = collections.deque([])
        
        for i in range(len(nodes_with_degree)):
            if nodes_with_degree[i] == 0:
                queue.append(i)
        
        while queue:
            current_node = queue.popleft()
            result.append(current_node) 
            for child in edges[current_node]:
                nodes_with_degree[child] -= 1
                if nodes_with_degree[child] == 0:
                    queue.append(child)
        
        return result