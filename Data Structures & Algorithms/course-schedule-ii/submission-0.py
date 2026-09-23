from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)] # Prereq --> Courses
        indegree = [0] * numCourses # COUNTER: counts prerequisites that are not yet completed

        for c, p in prerequisites:
            graph[p].append(c)
            indegree[c] += 1

        q = deque() # QUEUE: courses that can be taken
        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)

        completed = 0

        result = []

        # In the queue: READY - can take this course
        # Remove from the queue: COMPLETED - have taken this course
        while q: # STOPPING: An empty queue means every remaining course has at least one unmet prerequisite.
            c = q.popleft()
            completed += 1
            result.append(c)
            for depn in graph[c]:
                indegree[depn] -= 1
                if indegree[depn] == 0:
                    q.append(depn)
        
        return result if completed == numCourses else []


