from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for c, p in prerequisites:
            graph[p].append(c)
            indegree[c] += 1

        q = deque()
        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)

        completed = 0
        result = []

        while q:
            c = q.popleft()
            completed += 1
            result.append(c)
            for depn in graph[c]:
                indegree[depn] -= 1
                if indegree[depn] == 0:
                    q.append(depn)
        
        return result if completed == numCourses else []


